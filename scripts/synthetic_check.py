"""
Sanity checks for directed SPECTRA on planted directed graphs (50-500 nodes).

Planted model: G topic groups; node i cites node j with probability
    sigmoid(a_i + b_j + kappa * M[g_i, g_j])
where M is asymmetric (group g cites itself and group g+1 mod G), a_i is
citing activity, and b_j is heavy-tailed popularity. A few "generic"
papers get a large b_j and are cited from every group.

Checks:
  1. eta control: d_ev(eta) is monotone and eta-bisection hits targets.
  2. mode recovery: k-means on the cited-role factor V recovers the
     planted groups; compared against the symmetrized SPECTRA model,
     raw SVD of A, and directed SPECTRA without offsets.
  3. held-out citation AUC for the same variants.

Writes results/synthetic/*.csv and a summary JSON.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import normalized_mutual_info_score

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from dspectra.model import (FitConfig, diagnostics, fit, fit_to_target,  # noqa: E402
                            heldout_auc, modes)


def planted_graph(n, G, kappa, n_generic, out_degree, rng):
    g = rng.integers(0, G, size=n)
    M = np.zeros((G, G))
    for k in range(G):
        M[k, k] = 1.0
        M[k, (k + 1) % G] = 1.0
    a = rng.normal(0.0, 0.5, size=n)
    b = rng.normal(0.0, 0.5, size=n)
    generic = rng.choice(n, size=n_generic, replace=False)
    b[generic] += 3.0
    base = a[:, None] + b[None, :] + kappa * M[g][:, g]
    # global shift chosen by bisection so the expected out-degree is out_degree
    lo, hi = -30.0, 10.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if (1.0 / (1.0 + np.exp(-(base + mid)))).sum() / n > out_degree:
            hi = mid
        else:
            lo = mid
    P = 1.0 / (1.0 + np.exp(-(base + 0.5 * (lo + hi))))
    A = (rng.random((n, n)) < P).astype(np.float32)
    np.fill_diagonal(A, 0.0)
    return A, g, generic


def split_edges(A, frac, rng):
    """Hold out a fraction of directed edges and an equal number of non-edges."""
    n = A.shape[0]
    pos = np.argwhere(A > 0)
    rng.shuffle(pos)
    n_test = int(frac * len(pos))
    test_pos = pos[:n_test]
    A_train = A.copy()
    A_train[test_pos[:, 0], test_pos[:, 1]] = 0.0
    neg = []
    while len(neg) < n_test:
        i, j = rng.integers(0, n, size=2)
        if i != j and A[i, j] == 0:
            neg.append((i, j))
    return A_train, test_pos, np.array(neg)


def cluster_nmi(X, labels, G, seed):
    if X.shape[1] == 0:
        return 0.0
    Xn = X / np.maximum(np.linalg.norm(X, axis=1, keepdims=True), 1e-12)
    pred = KMeans(G, n_init=10, random_state=seed).fit_predict(Xn)
    return float(normalized_mutual_info_score(labels, pred))


def raw_svd(A, k):
    U, s, Vt = np.linalg.svd(A)
    return U[:, :k] * s[:k], Vt[:k].T * s[:k], s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sizes", type=int, nargs="+", default=[50, 100, 200, 500])
    ap.add_argument("--groups", type=int, default=4)
    ap.add_argument("--out_degree", type=float, default=8.0)
    ap.add_argument("--seeds", type=int, nargs="+", default=[0, 1, 2])
    ap.add_argument("--rank", type=int, default=16)
    ap.add_argument("--targets", type=float, nargs="+", default=[2.0, 4.0, 8.0])
    ap.add_argument("--etas", type=float, nargs="+",
                    default=[-0.5, -0.2, -0.1, 0.0, 0.05, 0.1, 0.2, 0.4])
    ap.add_argument("--epochs", type=int, default=1500)
    ap.add_argument("--device", default="cuda")
    ap.add_argument("--out", default="results/synthetic")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)

    sweep_rows, target_rows, recovery_rows = [], [], []
    for n in args.sizes:
        for seed in args.seeds:
            rng = np.random.default_rng(seed)
            A, g, generic = planted_graph(n, args.groups, kappa=3.0,
                                          n_generic=max(2, n // 50),
                                          out_degree=args.out_degree, rng=rng)
            A_train, test_pos, test_neg = split_edges(A, 0.1, rng)
            cfg = FitConfig(rank=args.rank, epochs=args.epochs, device=args.device)
            print(f"n={n} seed={seed} edges={int(A.sum())} "
                  f"density={A.mean():.4f}", flush=True)

            # 1a. eta sweep
            for eta in args.etas:
                m = fit(A_train, "directed", eta, cfg, seed)
                d = diagnostics(m)
                sweep_rows.append({"n": n, "seed": seed, "eta": eta, "d_ev": d["d_ev"],
                                   "k90": d["k90"],
                                   "auc": heldout_auc(m, test_pos, test_neg)})

            # 1b. bisection to targets
            for t in args.targets:
                t0 = time.time()
                res = fit_to_target(A_train, t, "directed", cfg, seed)
                target_rows.append({"n": n, "seed": seed, "target": t,
                                    "achieved": res.d_ev, "eta": res.eta,
                                    "rel_err": abs(res.d_ev - t) / t,
                                    "n_probes": len(res.probes),
                                    "seconds": time.time() - t0})

            # 2-3. recovery of planted groups (rows of V scaled by sqrt(p))
            G = args.groups
            res = fit_to_target(A_train, float(G), "directed", cfg, seed)
            md = modes(res.model)
            V_dir = md["V"][:, :G] * np.sqrt(md["p"][:G])
            U_dir = md["U"][:, :G] * np.sqrt(md["p"][:G])

            res_sym = fit_to_target(A_train, float(G), "symmetric", cfg, seed)
            ms = modes(res_sym.model)
            V_sym = ms["V"][:, :G] * np.sqrt(ms["p"][:G])

            cfg_no = FitConfig(rank=args.rank, epochs=args.epochs, device=args.device,
                               offsets=False)
            res_no = fit_to_target(A_train, float(G), "directed", cfg_no, seed)
            mn = modes(res_no.model)
            V_no = mn["V"][:, :G] * np.sqrt(mn["p"][:G])

            _, V_raw, _ = raw_svd(A_train, G)

            nongeneric = np.setdiff1d(np.arange(n), generic)
            # share of the top mode's cited-role mass on generic papers
            top_generic = lambda V: float((V[generic, 0] ** 2).sum() / (V[:, 0] ** 2).sum())
            for name, V, model in [("directed", V_dir, res.model),
                                   ("directed_no_offsets", V_no, res_no.model),
                                   ("symmetrized", V_sym, res_sym.model),
                                   ("raw_svd", V_raw, None)]:
                recovery_rows.append({
                    "n": n, "seed": seed, "variant": name,
                    "nmi_cited_role": cluster_nmi(V[nongeneric], g[nongeneric], G, seed),
                    "top_mode_generic_share": top_generic(V),
                    "generic_frac_nodes": len(generic) / n,
                    "heldout_auc": heldout_auc(model, test_pos, test_neg) if model else
                                   float("nan"),
                })
            recovery_rows.append({
                "n": n, "seed": seed, "variant": "directed_citing_role(U)",
                "nmi_cited_role": cluster_nmi(U_dir[nongeneric], g[nongeneric], G, seed),
                "top_mode_generic_share": float("nan"),
                "generic_frac_nodes": len(generic) / n, "heldout_auc": float("nan"),
            })
            print(f"   recovery: " + ", ".join(
                f"{r['variant']}={r['nmi_cited_role']:.2f}"
                for r in recovery_rows[-5:]), flush=True)

    import pandas as pd
    sw = pd.DataFrame(sweep_rows); tg = pd.DataFrame(target_rows)
    rc = pd.DataFrame(recovery_rows)
    sw.to_csv(f"{args.out}/eta_sweep.csv", index=False)
    tg.to_csv(f"{args.out}/eta_targets.csv", index=False)
    rc.to_csv(f"{args.out}/recovery.csv", index=False)

    # monotonicity of d_ev in eta, per (n, seed)
    mono = sw.sort_values("eta").groupby(["n", "seed"])["d_ev"].apply(
        lambda s: bool(np.all(np.diff(s.values) >= -0.05 * s.values[:-1])))
    summary = {
        "eta_sweep_monotone_fraction": float(mono.mean()),
        "d_ev_range_by_n": sw.groupby("n")["d_ev"].agg(["min", "max"]).to_dict(),
        "target_rel_err_by_n": tg.groupby("n")["rel_err"].agg(["mean", "max"]).to_dict(),
        "target_hit_rate_tau_0.05": float((tg.rel_err <= 0.05).mean()),
        "recovery_mean": rc.groupby("variant")[["nmi_cited_role", "top_mode_generic_share",
                                                "heldout_auc"]].mean().to_dict(),
        "recovery_by_n": rc.groupby(["variant", "n"])["nmi_cited_role"].mean()
                           .unstack().to_dict(),
    }
    with open(f"{args.out}/summary.json", "w") as f:
        json.dump(summary, f, indent=2, default=str)
    print(json.dumps(summary, indent=2, default=str))


if __name__ == "__main__":
    main()
