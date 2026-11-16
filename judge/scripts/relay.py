"""
Localhost relay between the DeepScholar-Bench judge and the vLLM 0.6.3 server.

Recent LiteLLM sends `max_completion_tokens`, which vLLM 0.6.3 rejects; this
renames it to `max_tokens`, caps it at 2048 tokens, turns a json_schema
response_format into vLLM's guided_json, and forwards
everything else unchanged.
Listens on 127.0.0.1:18012, forwards to 127.0.0.1:8011. Non-streaming only.
"""
import json

import httpx
import uvicorn
from fastapi import FastAPI, Request, Response

UPSTREAM = "http://127.0.0.1:8011"
app = FastAPI()
client = httpx.AsyncClient(base_url=UPSTREAM, timeout=1800)


@app.api_route("/{path:path}", methods=["GET", "POST"])
async def relay(path: str, request: Request):
    body = await request.body()
    if request.method == "POST" and body:
        data = json.loads(body)
        if "max_completion_tokens" in data:
            data.setdefault("max_tokens", data.pop("max_completion_tokens"))
            data.pop("max_completion_tokens", None)
        # judge replies are short; cap the reservation so prompt + reply fits the context
        if data.get("max_tokens"):
            data["max_tokens"] = min(int(data["max_tokens"]), 2048)
        # vLLM 0.6.3 ignores a json_schema response_format in chat requests but
        # enforces the same schema given as guided_json (structured output, as
        # OpenAI's API does for gpt-4o)
        rf = data.get("response_format") or {}
        if rf.get("type") == "json_schema" and "schema" in rf.get("json_schema", {}):
            data["guided_json"] = rf["json_schema"]["schema"]
            data.pop("response_format")
        body = json.dumps(data).encode()
    # a pooled keep-alive connection that vLLM's server closed meanwhile gives a
    # ReadError/RemoteProtocolError on the next request (seen once in ~6 h of
    # judging, 2026-11-03); the request never reached the model, so resend it
    for attempt in range(3):
        try:
            r = await client.request(request.method, "/" + path, content=body,
                                     headers={"content-type": "application/json"})
            break
        except (httpx.ReadError, httpx.RemoteProtocolError, httpx.ConnectError, httpx.WriteError):
            if attempt == 2:
                raise
    return Response(content=r.content, status_code=r.status_code,
                    media_type=r.headers.get("content-type"))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=18012, log_level="warning")
