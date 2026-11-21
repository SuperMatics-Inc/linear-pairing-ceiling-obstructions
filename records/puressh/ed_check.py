#!/usr/bin/env python3
"""NUMERICAL exact-diagonalization sanity check for PURESSH.

Computes equal-time on-site pair correlations |<Delta_x^dag Delta_y>| for:
  1. 2-site spinful bond-SSH dimer (1 bond oscillator) with Fock cutoff
     N_ph in {30, 60, 90, 120} across Omega in {0.2, 2.0, 20.0} at three
     parameter points on the theorem threshold beta*|t| + beta*g^2/K = 2^-10.
  2. 4-site spinful bond-SSH ring C_4 (4 bond oscillators) with total-phonon
     cutoff N_tot = sum_b n_b in {2, 3, 4} at distances d = 1 and d = 2,
     compared against the Theorem 1.1 bound A_GC * q_GC^d.

Label: NUMERICAL (floating-point finite-basis check, not part of analytical proof).
"""
from __future__ import annotations

import math
import os
from fractions import Fraction as Q

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

import numpy as np
from scipy.linalg import eigh

def build_fermions(n_sites: int) -> tuple[np.ndarray, np.ndarray]:
    n_modes = 2 * n_sites
    dim = 1 << n_modes
    c = np.zeros((n_modes, dim, dim), dtype=np.float64)
    for m in range(n_modes):
        for s in range(dim):
            if (s >> m) & 1:
                parity = bin(s & ((1 << m) - 1)).count("1")
                sign = -1.0 if (parity & 1) else 1.0
                c[m, s ^ (1 << m), s] = sign
    cdag = np.transpose(c, (0, 2, 1))
    return c, cdag


def run_dimer_ed() -> None:
    c, cdag = build_fermions(2)
    dim_el = 16
    t_op = np.zeros((dim_el, dim_el), dtype=np.float64)
    for sig in (0, 1):
        t_op += cdag[sig] @ c[2 + sig] + cdag[2 + sig] @ c[sig]
    delta0_dag = cdag[0] @ cdag[1]
    delta1 = c[3] @ c[2]
    pair_op_el = delta0_dag @ delta1

    # Partition 16 electronic states by conserved (N_up, N_dn) in {0,1,2}^2;
    # by spin-exchange symmetry (up <-> dn), off-diagonal sectors N_up < N_dn have multiplicity 2.
    dimer_sectors: list[tuple[int, int, int, list[int]]] = []
    for n_up in range(3):
        for n_dn in range(n_up, 3):
            idx = [
                s
                for s in range(dim_el)
                if sum((s >> (2 * i)) & 1 for i in range(2)) == n_up
                and sum((s >> (2 * i + 1)) & 1 for i in range(2)) == n_dn
            ]
            mult = 1 if n_up == n_dn else 2
            dimer_sectors.append((n_up, n_dn, mult, idx))

    bound_d1 = float(Q(341, 103) * Q(32, 341))
    print(f"=== 2-site dimer ED convergence (Theorem 1.1 d=1 bound = 32/103 = {bound_d1:.9f}) ===")

    beta = 1.0
    k_spring = 1.0
    cases = [
        ("joint_endpt", 2.0 ** -11, math.sqrt(2.0 ** -11), 0.0),
        ("joint_mu0.5", 2.0 ** -11, math.sqrt(2.0 ** -11), 0.5),
        ("pure_g_endpt", 0.0, math.sqrt(2.0 ** -10), 0.0),
    ]
    cutoffs = (30, 60, 90, 120)
    cache_dimer: dict[tuple[float, float, float, int], list[tuple[int, int, np.ndarray, np.ndarray]]] = {}

    for label, t_val, g_val, mu_val in cases:
        for omega in (0.2, 2.0, 20.0):
            vals: list[float] = []
            for n_ph in cutoffs:
                key = (t_val, g_val, omega, n_ph)
                if key not in cache_dimer:
                    a = np.zeros((n_ph, n_ph), dtype=np.float64)
                    for n in range(1, n_ph):
                        a[n - 1, n] = math.sqrt(float(n))
                    x_op = math.sqrt(omega / (2.0 * k_spring)) * (a + a.T)
                    h_ph = omega * (np.diag(np.arange(n_ph, dtype=np.float64)) + 0.5 * np.eye(n_ph))
                    eye_ph = np.eye(n_ph, dtype=np.float64)
                    sec_data: list[tuple[int, int, np.ndarray, np.ndarray]] = []
                    for n_up, n_dn, mult, idx in dimer_sectors:
                        d_sec = len(idx)
                        if n_up in (0, 2) and n_dn in (0, 2):
                            ev_sec = np.diag(h_ph).copy()
                            diag_p = np.zeros_like(ev_sec)
                        else:
                            eye_sec = np.eye(d_sec, dtype=np.float64)
                            t_sec = t_op[np.ix_(idx, idx)]
                            p_sec = pair_op_el[np.ix_(idx, idx)]
                            h_sec = (
                                -t_val * np.kron(t_sec, eye_ph)
                                + g_val * np.kron(t_sec, x_op)
                                + np.kron(eye_sec, h_ph)
                            )
                            if n_up in (0, 2) or n_dn in (0, 2):
                                ev_sec = np.linalg.eigvalsh(h_sec)
                                diag_p = np.zeros_like(ev_sec)
                            else:
                                ev_sec, vec_sec = eigh(h_sec)
                                p_full = np.kron(p_sec, eye_ph)
                                diag_p = np.sum(vec_sec * (p_full @ vec_sec), axis=0)
                        sec_data.append((n_up + n_dn, mult, ev_sec, diag_p))
                    cache_dimer[key] = sec_data
                sec_data = cache_dimer[key]
                all_ev = [ev - mu_val * float(n_el) for n_el, _, ev, _ in sec_data]
                emin = min(float(np.min(ev)) for ev in all_ev)
                num = 0.0
                den = 0.0
                for (_, mult, _, diag_p), ev in zip(sec_data, all_ev):
                    w = float(mult) * np.exp(-beta * (ev - emin))
                    den += float(np.sum(w))
                    num += float(np.sum(w * diag_p))
                vals.append(abs(num / den))
            diff = abs(vals[-1] - vals[-2])
            assert vals[-1] <= bound_d1, f"Bound violated: {vals[-1]} > {bound_d1}"
            print(
                f"  {label:12s} Omega={omega:4.1f} | "
                f"N=30:{vals[0]:.9e} N=60:{vals[1]:.9e} N=90:{vals[2]:.9e} N=120:{vals[3]:.9e} "
                f"(|dN|={diff:.2e})"
            )

def gen_phonon_states(n_edges: int, n_max: int) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []

    def rec(idx: int, rem: int, cur: list[int]) -> None:
        if idx == n_edges:
            out.append(tuple(cur))
            return
        for v in range(rem + 1):
            cur.append(v)
            rec(idx + 1, rem - v, cur)
            cur.pop()

    rec(0, n_max, [])
    return out


def run_c4_ring_ed() -> None:
    c, cdag = build_fermions(4)
    dim_el = 256
    edges = ((0, 1), (1, 2), (2, 3), (3, 0))
    t_bonds: list[np.ndarray] = []
    for x, y in edges:
        tb = np.zeros((dim_el, dim_el), dtype=np.float64)
        for sig in (0, 1):
            tb += cdag[2 * x + sig] @ c[2 * y + sig] + cdag[2 * y + sig] @ c[2 * x + sig]
        t_bonds.append(tb)
    t_sum = np.zeros((dim_el, dim_el), dtype=np.float64)
    for tb in t_bonds:
        t_sum += tb
    n_tot_el = np.zeros((dim_el, dim_el), dtype=np.float64)
    for m in range(8):
        n_tot_el += cdag[m] @ c[m]

    deltas = [c[2 * x + 1] @ c[2 * x] for x in range(4)]
    deltas_dag = [cdag[2 * x] @ cdag[2 * x + 1] for x in range(4)]
    pair_d1 = deltas_dag[0] @ deltas[1]
    pair_d2 = deltas_dag[0] @ deltas[2]

    # Partition 256 electronic states by conserved (N_up, N_dn) in {0..4}^2;
    # by spin-exchange symmetry (up <-> dn), off-diagonal sectors N_up < N_dn have multiplicity 2.
    sectors: list[tuple[int, int, int, list[int]]] = []
    for n_up in range(5):
        for n_dn in range(n_up, 5):
            idx = [
                s
                for s in range(dim_el)
                if sum((s >> (2 * i)) & 1 for i in range(4)) == n_up
                and sum((s >> (2 * i + 1)) & 1 for i in range(4)) == n_dn
            ]
            mult = 1 if n_up == n_dn else 2
            sectors.append((n_up, n_dn, mult, idx))

    bound_d1 = float(Q(341, 103) * Q(32, 341))
    bound_d2 = float(Q(341, 103) * (Q(32, 341) ** 2))
    print(
        f"\n=== 4-site ring C_4 ED convergence "
        f"(d=1 bound = {bound_d1:.6e}, d=2 bound = {bound_d2:.6e}) ==="
    )

    beta = 1.0
    k_spring = 1.0
    cases = [
        ("pure_t_endpt", 2.0 ** -10, 0.0, 0.0, 3.0),
        ("joint_endpt", 2.0 ** -11, math.sqrt(2.0 ** -11), 0.0, 3.0),
        ("joint_mu0.5", 2.0 ** -11, math.sqrt(2.0 ** -11), 0.5, 3.0),
        ("joint_mu0.5", 2.0 ** -11, math.sqrt(2.0 ** -11), 0.5, 20.0),
    ]
    cache_c4: dict[
        tuple[float, float, float, int],
        list[tuple[int, int, np.ndarray, np.ndarray, np.ndarray]],
    ] = {}

    for label, t_val, g_val, mu_val, omega in cases:
        res: dict[int, tuple[float, float]] = {}
        for n_tot in (2, 3, 4):
            key = (t_val, g_val, omega, n_tot)
            if key not in cache_c4:
                states = gen_phonon_states(4, n_tot)
                idx_map = {st: i for i, st in enumerate(states)}
                d_ph = len(states)
                h_ph = np.diag([omega * (sum(st) + 2.0) for st in states])
                x_ops = [np.zeros((d_ph, d_ph), dtype=np.float64) for _ in range(4)]
                scale = math.sqrt(omega / (2.0 * k_spring))
                for i, st in enumerate(states):
                    for b in range(4):
                        if st[b] + 1 <= n_tot:
                            st_up = list(st)
                            st_up[b] += 1
                            j = idx_map.get(tuple(st_up))
                            if j is not None:
                                val = scale * math.sqrt(float(st[b] + 1))
                                x_ops[b][i, j] = val
                                x_ops[b][j, i] = val
                eye_ph = np.eye(d_ph, dtype=np.float64)
                sec_list: list[tuple[int, int, np.ndarray, np.ndarray, np.ndarray]] = []
                for n_up, n_dn, mult, idx in sectors:
                    d_sec = len(idx)
                    eye_sec = np.eye(d_sec, dtype=np.float64)
                    t_sec = t_sum[np.ix_(idx, idx)]
                    p1_sec = pair_d1[np.ix_(idx, idx)]
                    p2_sec = pair_d2[np.ix_(idx, idx)]
                    h_el_sec = -t_val * t_sec
                    if g_val == 0.0:
                        ev_el, vec_el = eigh(h_el_sec)
                        d1_el = np.sum(vec_el * (p1_sec @ vec_el), axis=0)
                        d2_el = np.sum(vec_el * (p2_sec @ vec_el), axis=0)
                        ev_ph = np.diag(h_ph)
                        ev_sec = (ev_el[:, None] + ev_ph[None, :]).ravel()
                        diag1 = np.repeat(d1_el, d_ph)
                        diag2 = np.repeat(d2_el, d_ph)
                    elif n_up in (0, 4) and n_dn in (0, 4):
                        ev_sec = np.diag(h_ph).copy()
                        diag1 = np.zeros_like(ev_sec)
                        diag2 = np.zeros_like(ev_sec)
                    else:
                        h_sec = np.kron(h_el_sec, eye_ph) + np.kron(eye_sec, h_ph)
                        for b in range(4):
                            tb_sec = t_bonds[b][np.ix_(idx, idx)]
                            h_sec += g_val * np.kron(tb_sec, x_ops[b])
                        if n_up in (0, 4) or n_dn in (0, 4):
                            ev_sec = np.linalg.eigvalsh(h_sec)
                            diag1 = np.zeros_like(ev_sec)
                            diag2 = np.zeros_like(ev_sec)
                        else:
                            ev_sec, vec_sec = eigh(h_sec)
                            p1_full = np.kron(p1_sec, eye_ph)
                            p2_full = np.kron(p2_sec, eye_ph)
                            diag1 = np.sum(vec_sec * (p1_full @ vec_sec), axis=0)
                            diag2 = np.sum(vec_sec * (p2_full @ vec_sec), axis=0)
                    sec_list.append((n_up + n_dn, mult, ev_sec, diag1, diag2))
                cache_c4[key] = sec_list
            sec_list = cache_c4[key]
            all_ev = [ev - mu_val * float(n_el) for n_el, _, ev, _, _ in sec_list]
            emin = min(float(np.min(ev)) for ev in all_ev)
            num1 = 0.0
            num2 = 0.0
            den = 0.0
            for (_, mult, _, d1, d2), ev in zip(sec_list, all_ev):
                w = float(mult) * np.exp(-beta * (ev - emin))
                den += float(np.sum(w))
                num1 += float(np.sum(w * d1))
                num2 += float(np.sum(w * d2))
            avg1 = abs(num1 / den)
            avg2 = abs(num2 / den)
            assert avg1 <= bound_d1 and avg2 <= bound_d2
            res[n_tot] = (avg1, avg2)
        print(
            f"  {label:12s} Omega={omega:4.1f} | "
            f"N_tot=2: ({res[2][0]:.6e}, {res[2][1]:.6e}) | "
            f"N_tot=3: ({res[3][0]:.6e}, {res[3][1]:.6e}) | "
            f"N_tot=4: ({res[4][0]:.6e}, {res[4][1]:.6e})"
        )


if __name__ == "__main__":
    run_dimer_ed()
    run_c4_ring_ed()
    print("PURESSH ed_check.py: ALL NUMERICAL ED CHECKS PASSED")
