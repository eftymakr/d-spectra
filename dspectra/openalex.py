"""
Minimal cached OpenAlex client (https://docs.openalex.org).

Requests are paced, retried with backoff on 429/5xx, and cached on disk
so graph construction is reproducible and reruns make no network calls.
Set OPENALEX_API_KEY (environment or a .env file in the working
directory); without a key OpenAlex allows only a small shared daily budget.
The key is sent with each request but never stored in the cache.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import time
from typing import Dict, List, Optional

import requests

API = "https://api.openalex.org"
WORK_FIELDS = ("id,title,publication_date,publication_year,cited_by_count,"
               "referenced_works,abstract_inverted_index,doi")


def short_id(oa_id: str) -> str:
    return oa_id.rsplit("/", 1)[-1]


def _api_key() -> Optional[str]:
    if os.environ.get("OPENALEX_API_KEY"):
        return os.environ["OPENALEX_API_KEY"]
    if os.path.isfile(".env"):
        with open(".env") as f:
            for line in f:
                k, _, v = line.strip().partition("=")
                if k == "OPENALEX_API_KEY" and v:
                    return v
    return None


def abstract_text(inv: Optional[Dict[str, List[int]]]) -> str:
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[i] for i in sorted(pos))


class OpenAlexClient:
    def __init__(self, cache_dir: str = "data/openalex_cache", min_interval: float = 0.12,
                 max_retries: int = 8):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
        self.min_interval = min_interval
        self.max_retries = max_retries
        self._last = 0.0
        self.session = requests.Session()
        self.api_key = _api_key()
        self.n_requests = 0

    def _get(self, path: str, params: Dict):
        key = json.dumps([path, params], sort_keys=True)
        h = hashlib.sha1(key.encode()).hexdigest()
        cpath = os.path.join(self.cache_dir, h[:2], h + ".json")
        if os.path.isfile(cpath):
            with open(cpath) as f:
                return json.load(f)
        delay = 1.0
        for _ in range(self.max_retries):
            wait = self.min_interval - (time.time() - self._last)
            if wait > 0:
                time.sleep(wait)
            self._last = time.time()
            self.n_requests += 1
            sent = dict(params, api_key=self.api_key) if self.api_key else params
            try:
                r = self.session.get(f"{API}{path}", params=sent, timeout=60)
            except requests.RequestException:
                time.sleep(delay); delay = min(delay * 2, 60); continue
            if r.status_code == 200:
                data = r.json()
                os.makedirs(os.path.dirname(cpath), exist_ok=True)
                with open(cpath, "w") as f:
                    json.dump(data, f)
                return data
            if r.status_code == 404:
                return None
            if r.status_code in (429, 500, 502, 503, 504):
                time.sleep(delay); delay = min(delay * 2, 60); continue
            # not raise_for_status(): its message includes the URL, and so the key
            raise RuntimeError(f"OpenAlex HTTP {r.status_code}: {path} {params}")
        raise RuntimeError(f"OpenAlex request failed after retries: {path} {params}")

    def search(self, query: str, date_to: str, per_page: int = 50,
               select: str = WORK_FIELDS) -> List[Dict]:
        query = " ".join(re.sub(r"[^\w\s\-]", " ", query).split())
        d = self._get("/works", {"search": query,
                                 "filter": f"to_publication_date:{date_to}",
                                 "per-page": per_page, "select": select})
        return (d or {}).get("results", [])

    def works(self, ids: List[str], select: str = WORK_FIELDS) -> List[Dict]:
        out = []
        ids = [short_id(i) for i in ids]
        for k in range(0, len(ids), 100):
            part = ids[k:k + 100]
            d = self._get("/works", {"filter": "openalex:" + "|".join(part),
                                     "per-page": 100, "select": select})
            out.extend((d or {}).get("results", []))
        return out

    def citing(self, oa_id: str, date_to: str, per_page: int = 200,
               select: str = "id,publication_date") -> List[Dict]:
        d = self._get("/works", {"filter": f"cites:{short_id(oa_id)},to_publication_date:{date_to}",
                                 "per-page": per_page, "sort": "cited_by_count:desc",
                                 "select": select})
        return (d or {}).get("results", [])
