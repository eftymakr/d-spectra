"""
Submodular evidence selection over the modes of a fitted operator.

Given cited-role factors V (n x r, unit-norm columns), occupancy p and
query relevance r in [0, 1], pick |S| <= B greedily under

    F(S) = alpha * sum_{i in S} r_i / B
         + (1 - alpha) * sum_k w_k * (1 - exp(-gamma * z_k(S)))

    w_k  ∝ p_k * m_k,     m_k = sum_i r_i V_ik^2   (relevance-weighted mode mass)
    z_k(S) = sum_{i in S} r_i V_ik^2 / m_k

z_k is the proposal's z_k divided by m_k, i.e. the fraction of mode k's
relevant mass already covered; this only rescales gamma per mode, so F
stays monotone submodular and greedy keeps its 1 - 1/e guarantee.
"""
from __future__ import annotations

from typing import List, Optional

import numpy as np


def mode_weights(V: np.ndarray, p: np.ndarray, r: np.ndarray) -> np.ndarray:
    mass = (r[:, None] * V ** 2).sum(0)
    w = p * mass
    return w / max(w.sum(), 1e-12)


def greedy_select(V: np.ndarray, p: np.ndarray, r: np.ndarray, B: int,
                  alpha: float = 0.5, gamma: float = 5.0,
                  candidates: Optional[np.ndarray] = None) -> List[int]:
    n = V.shape[0]
    mass = np.maximum((r[:, None] * V ** 2).sum(0), 1e-12)
    w = mode_weights(V, p, r)
    contrib = r[:, None] * V ** 2 / mass[None, :]
    allowed = np.zeros(n, dtype=bool)
    allowed[candidates if candidates is not None else np.arange(n)] = True
    z = np.zeros(V.shape[1])
    S: List[int] = []
    for _ in range(min(B, int(allowed.sum()))):
        cov_gain = (w[None, :] * (np.exp(-gamma * z)[None, :]
                                  - np.exp(-gamma * (z[None, :] + contrib)))).sum(1)
        gain = alpha * r / B + (1.0 - alpha) * cov_gain
        gain[~allowed] = -np.inf
        i = int(np.argmax(gain))
        S.append(i)
        allowed[i] = False
        z += contrib[i]
    return S


def top_k(score: np.ndarray, B: int, candidates: Optional[np.ndarray] = None) -> List[int]:
    idx = np.arange(len(score)) if candidates is None else np.asarray(candidates)
    order = idx[np.argsort(-score[idx], kind="stable")]
    return order[:B].tolist()


def set_d_ev(V: np.ndarray, p: np.ndarray, S) -> float:
    """Effective number of modes a set occupies: exp(entropy) of
    q_k ∝ p_k * sum_{i in S} V_ik^2."""
    S = list(S)
    if not S:
        return 0.0
    q = p * (V[S] ** 2).sum(0)
    q = q / max(q.sum(), 1e-12)
    return float(np.exp(-(q * np.log(np.maximum(q, 1e-12))).sum()))


def embedding_diversity(E: np.ndarray, S) -> float:
    """1 - mean pairwise cosine similarity of the selected set (E rows unit-norm)."""
    S = list(S)
    if len(S) < 2:
        return 0.0
    G = E[S] @ E[S].T
    k = len(S)
    return float(1.0 - (G.sum() - np.trace(G)) / (k * (k - 1)))
