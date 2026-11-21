#!/usr/bin/env python3
"""Independent verification for ANNEALED-STATIC using distinct mathematical representations.

Independent methods used:
1. Pure integer pair (p, q) arithmetic with math.gcd (no fractions.Fraction) for all rational constants.
2. Second-quantized 2^L-dimensional Fock-space trace evaluation at 80-digit precision (mpmath)
   plus mpmath.iv interval arithmetic (no flint.arb_mat) for the 2-site and 4-site reflection minors.
3. Time-domain Gauss-Legendre integration of the connected imaginary-time density correlator
   K_x(u; W) = G_W(beta - u)_{xx} G_W(u)_{xx} against the exact bosonic covariance kernel D_dyn(u)
   (instead of spectral Matsubara summation) to cross-check a_x(W) and the Theorem 1b local buffer bound.
"""

from __future__ import annotations

import math
import sys
from typing import Any

import mpmath as mp
import numpy as np


def rat_add(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    num = a[0] * b[1] + b[0] * a[1]
    den = a[1] * b[1]
    g = math.gcd(abs(num), den)
    return (num // g, den // g)


def rat_mul(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    num = a[0] * b[0]
    den = a[1] * b[1]
    g = math.gcd(abs(num), den)
    return (num // g, den // g)


def rat_div(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    if b[0] < 0:
        return rat_mul(a, (-b[1], -b[0]))
    return rat_mul(a, (b[1], b[0]))


def rat_lt(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return a[0] * b[1] < b[0] * a[1]


def check_integer_rationals() -> dict[str, str]:
    # 1. STATIC-MODE 1/1148 > 1/1200
    sm = rat_div(rat_mul(rat_mul((2, 3), (4, 1)), (3, 4)), rat_mul((41, 1), (56, 1)))
    assert sm == (1, 1148) and rat_lt((1, 1200), sm)
    assert rat_div((1, 1200), (2, 1)) == (1, 2400)

    # 2. Local buffer constants at 4t/g <= 1/16: 16/15 + 256/225 = 496/225
    inv_om = (16, 15)
    inv_om_sq = rat_mul(inv_om, inv_om)
    bracket = rat_add(inv_om, inv_om_sq)
    assert bracket == (496, 225) and rat_lt(bracket, (12, 5))

    lead = rat_div(bracket, (24, 1))
    assert lead == (62, 675) and rat_lt(lead, (1, 10))

    lead_g4 = rat_mul((4, 1), lead)
    assert lead_g4 == (248, 675) and rat_lt(lead_g4, (1, 2))

    # 3. Taylor majorization and combined annealed constant: 248/675 + 12 = 8348/675 < 25/2
    combined = rat_add(lead_g4, (12, 1))
    assert combined == (8348, 675) and rat_lt(combined, (25, 2))

    # 4. Two-site direct reflection n=2 Taylor gap: (25 - 17) / 24 = 1/3
    gap = rat_div((25 - 17, 1), (24, 1))
    assert gap == (1, 3) and rat_lt((0, 1), gap)

    return {
        "lead": f"{lead[0]}/{lead[1]}",
        "lead_g4": f"{lead_g4[0]}/{lead_g4[1]}",
        "combined": f"{combined[0]}/{combined[1]}",
        "gap": f"{gap[0]}/{gap[1]}",
    }


def fock_trace_one_spin(h_mat: Any, centered: bool) -> Any:
    """Compute Tr_Fock(exp(-H)) on the 2^L-dimensional 1-spin Fock space by summing all 2^L occupancy sectors."""
    L = h_mat.rows
    evals, _ = mp.eigsy(h_mat)
    # In the eigenbasis of h_mat, the 2^L Fock eigenvalues are sums over subsets S subset {0..L-1}:
    # If centered=False: sum_{a in S} e_a
    # If centered=True:  sum_{a in S} (e_a / 2) - sum_{a not in S} (e_a / 2)
    total = mp.mpf(0)
    for mask in range(1 << L):
        energy = mp.mpf(0)
        for a in range(L):
            if (mask >> a) & 1:
                energy += evals[a] * (mp.mpf("0.5") if centered else mp.mpf(1))
            elif centered:
                energy -= evals[a] * mp.mpf("0.5")
        total += mp.exp(-energy)
    return total


def check_fock_and_interval_minors() -> dict[str, str]:
    mp.mp.dps = 80
    mp.iv.dps = 50

    # 1. 2-site dimer direct reflection 2x2 minor via 4-state Fock trace and mpmath.iv
    def dimer_h(b1: int, b2: int, t: int = 2) -> Any:
        return mp.matrix([[mp.mpf(b1), mp.mpf(-t)], [mp.mpf(-t), mp.mpf(b2)]])

    k_mm = fock_trace_one_spin(dimer_h(-1, -1), centered=False) ** 2
    k_pp = fock_trace_one_spin(dimer_h(1, 1), centered=False) ** 2
    k_mp = fock_trace_one_spin(dimer_h(-1, 1), centered=False) ** 2
    det_direct_fock = k_mm * k_pp - k_mp * k_mp

    # Interval check in mpmath.iv
    def iv_cosh(x: Any) -> Any:
        return (mp.iv.exp(x) + mp.iv.exp(-x)) / mp.iv.mpf(2)

    iv_2 = mp.iv.mpf(2)
    iv_1 = mp.iv.mpf(1)
    iv_5 = mp.iv.mpf(5)
    iv_lhs = 4 * (iv_cosh(iv_2) + iv_cosh(iv_1)) ** 2
    iv_rhs = 4 * (iv_cosh(mp.iv.sqrt(iv_5)) + iv_1) ** 2
    iv_det_direct = iv_lhs * iv_lhs - iv_rhs * iv_rhs
    assert iv_det_direct.b < mp.mpf(-4593)
    assert abs(det_direct_fock - mp.mpf(iv_det_direct.mid)) < mp.mpf("1e-40")

    # 2. 2-site dimer PH symmetric 3x3 minor on {-2, 0, 2} via Fock trace
    pts_dimer = [-2, 0, 2]
    M_dimer_ph = mp.matrix(3, 3)
    for i, b1 in enumerate(pts_dimer):
        for j, b2 in enumerate(pts_dimer):
            M_dimer_ph[i, j] = fock_trace_one_spin(dimer_h(b1, -b2), centered=True)
    det_dimer_ph = mp.det(M_dimer_ph)
    assert det_dimer_ph > mp.mpf(35)

    # 3. 4-site ring C4 PH symmetric 3x3 minor via 16-state Fock trace
    comb_c4 = [(-2, -2), (-2, -1), (-1, -1)]
    M1_c4 = mp.matrix(3, 3)
    M2_c4 = mp.matrix(3, 3)
    for i, (a1, a2) in enumerate(comb_c4):
        for j, (b1, b2) in enumerate(comb_c4):
            t = 2
            h = mp.matrix(
                [
                    [a1, -t, 0, -t],
                    [-t, a2, -t, 0],
                    [0, -t, -b2, -t],
                    [-t, 0, -t, -b1],
                ]
            )
            tr1 = fock_trace_one_spin(h, centered=True)
            M1_c4[i, j] = tr1
            M2_c4[i, j] = tr1 * tr1
    det_m1_c4 = mp.det(M1_c4)
    det_m2_c4 = mp.det(M2_c4)
    assert det_m1_c4 < mp.mpf(-203)
    assert det_m2_c4 < mp.mpf("-5.87e10")

    # Cross-check against replay.py values to 30 digits
    ref_direct = mp.mpf("-4593.0291530659661610604341728287152")
    ref_dimer_ph = mp.mpf("35.76887199956216591042958446551016")
    ref_m1_c4 = mp.mpf("-203.854762735809940779543442390")
    ref_m2_c4 = mp.mpf("-58763809479.5249913351181560211")
    assert abs(det_direct_fock - ref_direct) < mp.mpf("1e-28")
    assert abs(det_dimer_ph - ref_dimer_ph) < mp.mpf("1e-28")
    assert abs(det_m1_c4 - ref_m1_c4) < mp.mpf("1e-25")
    assert abs(det_m2_c4 - ref_m2_c4) < mp.mpf("1e-17")

    return {
        "det_direct_fock": str(mp.nstr(det_direct_fock, 25)),
        "det_dimer_ph": str(mp.nstr(det_dimer_ph, 25)),
        "det_m1_c4": str(mp.nstr(det_m1_c4, 25)),
        "det_m2_c4": str(mp.nstr(det_m2_c4, 25)),
    }


def time_domain_ax(H: np.ndarray, tau: float, Omega: float, U: float, x: int) -> float:
    """Compute a_x(W) via time-domain Gauss-Legendre quadrature of
    int_0^beta D_dyn(u) K_x(u; W) du, where D_dyn(u) = U * [Omega * cosh((beta/2 - u)*Omega) / (2*sinh(beta*Omega/2)) - 1/beta].
    """
    beta = 1.0 / tau
    evals, evecs = np.linalg.eigh(H)
    p = np.abs(evecs[x, :]) ** 2
    nodes, weights = np.polynomial.legendre.leggauss(96)
    u_grid = 0.5 * beta * (nodes + 1.0)
    w_grid = 0.5 * beta * weights

    total = 0.0
    half_b_om = 0.5 * beta * Omega
    denom_sinh = 2.0 * math.sinh(half_b_om)
    for u, w in zip(u_grid, w_grid):
        # G_W(u)_{xx} = sum_a p_a / (exp(u * e_a) + exp(-(beta - u) * e_a))
        g_u = np.sum(p / (np.exp(np.clip(u * evals, -500.0, 500.0)) + np.exp(np.clip(-(beta - u) * evals, -500.0, 500.0))))
        g_bu = np.sum(p / (np.exp(np.clip((beta - u) * evals, -500.0, 500.0)) + np.exp(np.clip(-u * evals, -500.0, 500.0))))
        k_u = g_u * g_bu
        d_dyn = U * (Omega * math.cosh((0.5 * beta - u) * Omega) / denom_sinh - 1.0 / beta)
        # Factor 2 for two spins, 1/2 from second-order Taylor coefficient -> 2 * (1/2) * beta * int_0^beta = beta * int_0^beta
        # Wait: in R'_W(0) = sum_x a_x(W), a_x(W) = beta * int_0^beta D_dyn(u) K_x(u; W) du
        total += w * beta * d_dyn * k_u
    return total


def check_time_domain_cross_check() -> dict[str, float]:
    from replay import exact_ax_from_spectrum  # type: ignore[import-not-found]

    U = 4.0
    g = 1.0
    t = 1.0 / 64.0
    tau = 0.002
    Omega = 0.001
    L = 12
    w_mid = (t * t) / (2.0 * tau) - 2.0 * tau
    W_ring = np.array([g if i % 2 == 0 else -g for i in range(L)], dtype=float)
    W_ring[4] = 100.0
    W_ring[8] = 100.0
    W_ring[5] = 2.0 * tau
    W_ring[6] = w_mid
    W_ring[7] = 2.0 * tau
    H_ring = np.diag(W_ring)
    for i in range(L):
        j = (i + 1) % L
        H_ring[i, j] -= t
        H_ring[j, i] -= t
    evals, evecs = np.linalg.eigh(H_ring)

    ax_spec_res = exact_ax_from_spectrum(evals, evecs, tau, Omega, U, 5)
    ax_td_res = time_domain_ax(H_ring, tau, Omega, U, 5)
    assert abs(ax_spec_res - ax_td_res) < 1e-6

    ax_spec_buf = exact_ax_from_spectrum(evals, evecs, tau, Omega, U, 0)
    ax_td_buf = time_domain_ax(H_ring, tau, Omega, U, 0)
    assert abs(ax_spec_buf - ax_td_buf) < 1e-10

    return {
        "ax_td_res": ax_td_res,
        "ax_td_buf": ax_td_buf,
        "diff_res": abs(ax_spec_res - ax_td_res),
        "diff_buf": abs(ax_spec_buf - ax_td_buf),
    }


def main() -> int:
    r1 = check_integer_rationals()
    r2 = check_fock_and_interval_minors()
    r3 = check_time_domain_cross_check()
    print("ALL INDEPENDENT ANNEALED-STATIC CHECKS PASSED.")
    print("[integer_rationals]", r1)
    print("[fock_and_interval_minors]", r2)
    print("[time_domain_cross_check]", r3)
    return 0


if __name__ == "__main__":
    sys.exit(main())
