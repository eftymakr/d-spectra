"""
Directed SPECTRA: a latent citation-graph model whose realized capacity is
read from the normalized singular-value spectrum of an asymmetric kernel.

Ported from the SPECTRA engine (spectra_code/adaptive_eta_frontier.py):
the SVD parameterisation (QR-orthonormalised factors, softplus singular
values), bounded beta, centered factors, bias warmup and the
eta-weighted entropy term are kept as in the original. What changes:

  undirected (SPECTRA)                    directed (D-SPECTRA)
  logit = a_i + a_j + beta K_ij           logit = a_i + b_j + beta K_ij
  K = n Q S^2 Q^T / sum(sigma^2)          K = n U S V^T / sum(sigma)
  p_k = sigma_k^2 / sum(sigma^2)          p_k = sigma_k / sum(sigma)

sum(sigma) is the nuclear norm of U S V^T, the analogue of SPECTRA's
trace normalisation. a_i absorbs citing activity and b_j popularity.

Graphs here are small (50-500 nodes), so the loss uses every non-edge
exactly instead of SPECTRA's sampled negatives; the loss keeps SPECTRA's
balanced form (mean over edges + mean over non-edges) so eta has the
same scale.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


def set_seed(seed: int) -> None:
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def init_beta_raw_for_bounded_beta(init_beta, beta_max):
    p = min(max(init_beta / beta_max, 1e-6), 1.0 - 1e-6)
    return math.log(p / (1.0 - p))


def _orthonormal(raw: torch.Tensor) -> torch.Tensor:
    centered = raw - raw.mean(0, keepdim=True)
    Q, _ = torch.linalg.qr(centered, mode="reduced")
    return Q


class _SpectraBase(nn.Module):
    def __init__(self, n, rank, beta_max=5.0, init_beta=1.0, init_scale=0.01,
                 device="cpu"):
        super().__init__()
        self.n = n; self.rank = rank; self.beta_max = float(beta_max)
        beta_raw0 = init_beta_raw_for_bounded_beta(init_beta, self.beta_max)
        self.beta_raw = nn.Parameter(torch.tensor(beta_raw0, device=device))
        sigma_init = 1.0 / torch.sqrt(torch.arange(1, rank + 1, dtype=torch.float32,
                                                    device=device))
        self.sigma_raw = nn.Parameter(torch.log(torch.expm1(sigma_init)))

    def beta(self):
        return self.beta_max * torch.sigmoid(self.beta_raw) + 1e-8

    def sigma(self):
        return F.softplus(self.sigma_raw) + 1e-8

    def freeze_factor(self):
        for name in self.factor_param_names():
            getattr(self, name).requires_grad_(False)

    def unfreeze_factor(self):
        for name in self.factor_param_names():
            getattr(self, name).requires_grad_(True)

    def log_dev(self) -> torch.Tensor:
        p = self.occupancy()
        return -(p * torch.log(p.clamp_min(1e-12))).sum()


class DirectedSpectra(_SpectraBase):
    """P(i cites j) = sigmoid(a_i + b_j + beta * K_ij), K = n U S V^T / ||U S V^T||_*."""

    def __init__(self, n, rank, offsets=True, **kw):
        super().__init__(n, rank, **kw)
        dev = self.sigma_raw.device
        self.U_raw = nn.Parameter(kw.get("init_scale", 0.01) * torch.randn(n, rank, device=dev))
        self.V_raw = nn.Parameter(kw.get("init_scale", 0.01) * torch.randn(n, rank, device=dev))
        self.offsets = offsets
        if offsets:
            self.a = nn.Parameter(torch.zeros(n, device=dev))
            self.b = nn.Parameter(torch.zeros(n, device=dev))
        else:
            self.alpha = nn.Parameter(torch.tensor(-3.0, device=dev))

    def factor_param_names(self):
        return ["U_raw", "V_raw", "sigma_raw"]

    def U(self):
        return _orthonormal(self.U_raw)

    def V(self):
        return _orthonormal(self.V_raw)

    def occupancy(self):
        s = self.sigma()
        return s / s.sum()

    def kernel(self):
        s = self.sigma()
        return self.n * (self.U() * s) @ self.V().T / s.sum()

    def logits(self):
        base = (self.a[:, None] + self.b[None, :]) if self.offsets else self.alpha
        return base + self.beta() * self.kernel()

    def offset_reg(self):
        if self.offsets:
            return self.a.pow(2).mean() + self.b.pow(2).mean()
        return self.alpha.pow(2)

    def pair_mask(self):
        return ~torch.eye(self.n, dtype=torch.bool, device=self.sigma_raw.device)


class SymmetricSpectra(_SpectraBase):
    """Original undirected SPECTRA (node-bias, SVD parameterisation), used
    for the symmetrized-graph ablation. Fit on A + A^T over pairs i < j."""

    def __init__(self, n, rank, **kw):
        super().__init__(n, rank, **kw)
        dev = self.sigma_raw.device
        self.U_raw = nn.Parameter(kw.get("init_scale", 0.01) * torch.randn(n, rank, device=dev))
        self.a = nn.Parameter(torch.zeros(n, device=dev))

    def factor_param_names(self):
        return ["U_raw", "sigma_raw"]

    def U(self):
        return _orthonormal(self.U_raw)

    V = U

    def occupancy(self):
        s2 = self.sigma().pow(2)
        return s2 / s2.sum()

    def kernel(self):
        s2 = self.sigma().pow(2)
        Q = self.U()
        return self.n * (Q * s2) @ Q.T / s2.sum()

    def logits(self):
        return self.a[:, None] + self.a[None, :] + self.beta() * self.kernel()

    def offset_reg(self):
        return self.a.pow(2).mean()

    def pair_mask(self):
        return torch.triu(torch.ones(self.n, self.n, dtype=torch.bool,
                                     device=self.sigma_raw.device), diagonal=1)


def loss_components(m, A, mask, lambda_theta=1e-4, lambda_bias=1e-4):
    """Balanced NLL over all pairs in `mask`, the entropy log d_ev, and the
    SPECTRA regulariser (same weights as the original engine)."""
    logits = m.logits()
    pos = mask & (A > 0)
    neg = mask & (A == 0)
    nll = F.softplus(-logits[pos]).mean() + F.softplus(logits[neg]).mean()
    reg = 0.5 * lambda_theta * m.beta().pow(2) + 0.5 * lambda_bias * m.offset_reg()
    return nll, m.log_dev(), reg


@dataclass
class FitConfig:
    rank: int = 32
    epochs: int = 1500
    lr: float = 1e-2
    bias_warmup_epochs: int = 200
    beta_max: float = 5.0
    init_beta: float = 1.0
    lambda_theta: float = 1e-4
    lambda_bias: float = 1e-4
    offsets: bool = True
    device: str = "cpu"


def make_model(kind: str, n: int, cfg: FitConfig):
    kw = dict(beta_max=cfg.beta_max, init_beta=cfg.init_beta, device=cfg.device)
    if kind == "directed":
        return DirectedSpectra(n, cfg.rank, offsets=cfg.offsets, **kw).to(cfg.device)
    if kind == "symmetric":
        return SymmetricSpectra(n, cfg.rank, **kw).to(cfg.device)
    raise ValueError(kind)


def prepare_adjacency(A: np.ndarray, kind: str, device: str) -> torch.Tensor:
    A = (np.asarray(A) > 0).astype(np.float32)
    np.fill_diagonal(A, 0.0)
    if kind == "symmetric":
        A = np.maximum(A, A.T)
    return torch.tensor(A, device=device)


def fit(A: np.ndarray, kind: str = "directed", eta: float = 0.0,
        cfg: Optional[FitConfig] = None, seed: int = 0):
    """Cold-start fixed-epoch fit of  NLL - eta * log d_ev + R  (as in SPECTRA)."""
    cfg = cfg or FitConfig()
    set_seed(seed)
    At = prepare_adjacency(A, kind, cfg.device)
    m = make_model(kind, At.shape[0], cfg)
    mask = m.pair_mask()
    opt = torch.optim.Adam(m.parameters(), lr=cfg.lr)
    if cfg.bias_warmup_epochs > 0:
        m.freeze_factor()
    for epoch in range(1, cfg.epochs + 1):
        if cfg.bias_warmup_epochs > 0 and epoch == cfg.bias_warmup_epochs + 1:
            m.unfreeze_factor()
        opt.zero_grad(set_to_none=True)
        nll, log_v, reg = loss_components(m, At, mask, cfg.lambda_theta, cfg.lambda_bias)
        (nll - eta * log_v + reg).backward()
        opt.step()
    return m


@torch.no_grad()
def diagnostics(m) -> Dict:
    p = m.occupancy().cpu().numpy()
    order = np.argsort(-p)
    p = p[order]
    log_v = float(-(p * np.log(np.maximum(p, 1e-12))).sum())
    cum = np.cumsum(p)
    return {
        "d_ev": float(np.exp(log_v)),
        "k90": int(np.searchsorted(cum, 0.9) + 1),
        "beta": float(m.beta()),
        "p_sorted": p.tolist(),
        "mode_order": order.tolist(),
    }


@torch.no_grad()
def modes(m) -> Dict[str, np.ndarray]:
    """Factors sorted by occupancy: U (citing/hub role), V (cited/authority
    role) and p. For the symmetric model U == V."""
    p = m.occupancy().cpu().numpy()
    order = np.argsort(-p)
    U = m.U().cpu().numpy()[:, order]
    V = m.V().cpu().numpy()[:, order]
    return {"U": U, "V": V, "p": p[order]}


@dataclass
class TargetResult:
    eta: float
    d_ev: float
    model: object
    probes: List[Dict] = field(default_factory=list)


def fit_to_target(A: np.ndarray, d_target: float, kind: str = "directed",
                  cfg: Optional[FitConfig] = None, seed: int = 0, tau: float = 0.02,
                  eta_step: float = 0.1, expand: float = 2.0, eta_lim: float = 10.0,
                  max_expansions: int = 10, max_bisect: int = 20) -> TargetResult:
    """Bracket-then-bisect on eta so the fitted d_ev hits d_target within
    relative tolerance tau. d_ev is increasing in eta (eta > 0 rewards
    spreading occupancy), so the search moves eta up from 0 when the eta=0
    fit is below target and down otherwise, as in SPECTRA's
    from-zero directional search. Every probe is a cold-start fit."""
    cfg = cfg or FitConfig()
    if d_target > cfg.rank:
        raise ValueError(f"d_target={d_target} exceeds rank cap {cfg.rank}")
    probes: List[Dict] = []

    def probe(eta):
        m = fit(A, kind, eta, cfg, seed)
        d = diagnostics(m)["d_ev"]
        probes.append({"eta": eta, "d_ev": d})
        return m, d

    def close(d):
        return abs(d - d_target) <= tau * d_target

    m0, d0 = probe(0.0)
    best = (0.0, d0, m0)
    if close(d0):
        return TargetResult(0.0, d0, m0, probes)

    direction = 1.0 if d0 < d_target else -1.0
    lo_eta, lo_d = 0.0, d0
    step = eta_step
    hi = None
    for _ in range(max_expansions):
        eta = float(np.clip(direction * step, -eta_lim, eta_lim))
        m, d = probe(eta)
        if abs(d - d_target) < abs(best[1] - d_target):
            best = (eta, d, m)
        if close(d):
            return TargetResult(eta, d, m, probes)
        if (d - d_target) * (lo_d - d_target) < 0:
            hi = (eta, d)
            break
        lo_eta, lo_d = eta, d
        step *= expand
    if hi is None:
        return TargetResult(best[0], best[1], best[2], probes)

    a_eta, a_d = lo_eta, lo_d
    b_eta, b_d = hi
    for _ in range(max_bisect):
        mid = 0.5 * (a_eta + b_eta)
        m, d = probe(mid)
        if abs(d - d_target) < abs(best[1] - d_target):
            best = (mid, d, m)
        if close(d) or abs(b_eta - a_eta) < 1e-4:
            break
        if (d - d_target) * (a_d - d_target) < 0:
            b_eta, b_d = mid, d
        else:
            a_eta, a_d = mid, d
    return TargetResult(best[0], best[1], best[2], probes)


@torch.no_grad()
def heldout_auc(m, pos_pairs: np.ndarray, neg_pairs: np.ndarray) -> float:
    from sklearn.metrics import roc_auc_score
    L = m.logits().cpu().numpy()
    s = np.concatenate([L[pos_pairs[:, 0], pos_pairs[:, 1]],
                        L[neg_pairs[:, 0], neg_pairs[:, 1]]])
    y = np.concatenate([np.ones(len(pos_pairs)), np.zeros(len(neg_pairs))])
    return float(roc_auc_score(y, s))
