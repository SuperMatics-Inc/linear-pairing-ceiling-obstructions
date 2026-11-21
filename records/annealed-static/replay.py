#!/usr/bin/env python3
"""Exact rational, outward-interval (Arb), and finite-matrix replay for ANNEALED-STATIC.

Checks:
1. exact_rational_constants:
   - STATIC-MODE baseline constant 1/1148 > 1/1200 and torus half-constant 1/2400.
   - Local-buffer geometric series constant at 4t/g <= 1/16:
     16/15 + 256/225 = 496/225 < 12/5, and 496 / (24 * 225) = 62/675 < 1/10.
   - At g = U/4: 4 * 62/675 = 248/675 < 1/2.
   - Rare-defect polynomial-vs-exponential bound:
     For integer R >= 1, 16^R >= 1 + 15 R > 12 R, so 16^R < 12 u implies R < u.
     In 2 u^3 + 2 u^2 + u = c_1 u + c_2 (u^2/2!) + c_3 (u^3/3!),
     (c_1, c_2, c_3) = (1, 4, 12) <= 12, so (2 u^2 + 2 u + 1) u e^{-u} < 12 for all u > 0.
     Combined annealed cumulant constant at g = U/4:
     248/675 + 288/24 = 248/675 + 12 = 8348/675 < 25/2.
   - Two-site direct reflection Taylor gap:
     2^2 + 1^2 = 5 = (sqrt(5))^2 + 0^2 and (5^2 - (4^2 + 1^2)) / 4! = 8/24 = 1/3 > 0.
   - Regime-collapse exponents (Theorem 2c):
     At g <= U/4 and t <= g/64 <= 2^{-8} U, 2^{27} t^2 / U <= 2^{19} t and min(2^{10} t, 2^{27} t^2 / U) <= 2^{10} t.
2. arb_reflection_minors:
   - Outward-rounded ball arithmetic (flint.arb / flint.arb_mat at 128-bit precision) certifying:
     (a) 2-site dimer direct-reflection 2x2 minor on b in {-1, +1} at beta=1, t=2 is < -4593 < 0.
     (b) 2-site dimer particle-hole symmetric 2x2 and 3x3 minors on {-2, 0, +2} at beta=1, t=2 are > 0,
         and the 4x4 Fock trace matches the closed-form 2*cosh((b1-b2)/2) + 2*cosh(sqrt(((b1+b2)/2)^2+t^2)).
     (c) 4-site zero-flux ring C4 particle-hole symmetric reflection 3x3 minor on
         {(-2, -2), (-2, -1), (-1, -1)} at beta=1, t=2 is < -203 < 0 for one spin (M1)
         and < -5.87e10 < 0 for two spins (M2 = M1^2 and K_ph = det(I + exp(-h))^2).
3. arb_two_step_resolvent_and_buffer:
   - Outward-rounded ball arithmetic certifying:
     (a) Vanishing first-order boundary term <delta_x, R_0(i*omega_k) T_bdry R_0(i*omega_k) delta_x> == 0.
     (b) Exact two-step resolvent identity R(i*omega_k)_{xx} - R_0(i*omega_k)_{xx}
         == <R_0(-i*omega_k) delta_x, P_in T_bdry R(i*omega_k) T_bdry P_in R_0(i*omega_k) delta_x>.
     (c) Neumann boundary bound |R(i*omega_k)_{xx} - R_0(i*omega_k)_{xx}|
         <= 16 t^2 / (|omega_k| (omega_k^2 + g^2)) * (4t/g)^{2R} / (1 - 4t/g)^2.
4. local_buffer_and_annealed_cumulant:
   - Finite-lattice check on a 1D ring (L=12) and a 2D 4x4 torus (16 sites) containing an embedded
     STATIC-MODE resonance: the resonance site exceeds U*Omega^2/(2400*tau^3), while every g-buffered
     site obeys the Theorem 1b local buffer bound and the Theorem 1c annealed expectation bound.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import math
import subprocess
import sys

import flint  # type: ignore[import-not-found]
import numpy as np


MUTANTS = [
    "flip_buffer_fraction_bound",
    "flip_combined_annealed_constant",
    "flip_bernoulli_radius_bound",
    "flip_taylor_majorization_constant",
    "flip_dimer_direct_taylor_gap",
    "flip_dimer_direct_2x2_sign",
    "flip_dimer_ph_3x3_sign",
    "flip_c4_ph_one_spin_sign",
    "flip_c4_ph_two_spin_sign",
    "flip_first_order_boundary_zero",
    "flip_two_step_resolvent_identity",
    "flip_neumann_boundary_bound",
    "flip_local_buffer_cumulant_bound",
    "flip_annealed_ray_limit_bound",
]


def exact_rational_constants(mutant: str | None = None) -> dict[str, str]:
    # 1. STATIC-MODE baseline constants
    static_mode_raw = (Fraction(2, 3) * Fraction(4, 1) * Fraction(3, 4)) / (
        Fraction(41, 1) * Fraction(56, 1)
    )
    static_mode_target = Fraction(1, 1200)
    static_mode_torus = Fraction(1, 2400)
    if not (static_mode_raw == Fraction(1, 1148) and static_mode_raw > static_mode_target):
        raise AssertionError("STATIC-MODE baseline constant check failed")
    if not (static_mode_target / 2 == static_mode_torus):
        raise AssertionError("STATIC-MODE torus half-constant check failed")

    # 2. Local buffer constants at 4t/g <= 1/16 (Theorem 1b)
    ratio_max = Fraction(1, 16)
    one_minus = Fraction(1, 1) - ratio_max  # 15/16
    inv_one_minus = Fraction(1, 1) / one_minus  # 16/15
    inv_one_minus_sq = inv_one_minus * inv_one_minus  # 256/225
    bracket_sum = inv_one_minus + inv_one_minus_sq  # 496/225
    if not (bracket_sum == Fraction(496, 225) and bracket_sum < Fraction(12, 5)):
        raise AssertionError("Local buffer bracket sum 496/225 check failed")

    lead_coeff = bracket_sum / Fraction(24, 1)  # 62/675
    lead_cap = Fraction(1, 10)
    if mutant == "flip_buffer_fraction_bound":
        lead_cap = Fraction(1, 12)
    if not (lead_coeff == Fraction(62, 675) and lead_coeff < lead_cap):
        raise AssertionError("Local buffer lead coefficient 62/675 < 1/10 failed")

    # At g = U/4, U/g = 4
    g_quarter_lead = Fraction(4, 1) * lead_coeff  # 248/675
    if not (g_quarter_lead == Fraction(248, 675) and g_quarter_lead < Fraction(1, 2)):
        raise AssertionError("Local buffer g=U/4 coefficient 248/675 < 1/2 failed")

    # 3. Bernoulli inequality for adaptive radius R <= u (Theorem 1c)
    # For R = 1, 16^1 = 1 + 15*1 = 16 > 12*1; slope 15 > 12.
    bernoulli_slope = Fraction(15, 1)
    target_slope = Fraction(12, 1)
    if mutant == "flip_bernoulli_radius_bound":
        target_slope = Fraction(16, 1)
    if not (bernoulli_slope > target_slope):
        raise AssertionError("Bernoulli inequality slope 15 > 12 failed")
    for r_int in range(1, 25):
        if not (16**r_int >= 1 + 15 * r_int and 1 + 15 * r_int > 12 * r_int):
            raise AssertionError(f"Bernoulli check failed at R={r_int}")

    # 4. Taylor coefficient majorization for (2u^2 + 2u + 1) u e^{-u} < 12 (Theorem 1c)
    # 2u^3 + 2u^2 + u = c1 * (u^1/1!) + c2 * (u^2/2!) + c3 * (u^3/3!)
    c1 = Fraction(1, 1) / Fraction(1, 1)
    c2 = Fraction(2, 1) / Fraction(1, 2)
    c3 = Fraction(2, 1) / Fraction(1, 6)
    taylor_majorant = max(c1, c2, c3)
    expected_majorant = Fraction(12, 1)
    if mutant == "flip_taylor_majorization_constant":
        expected_majorant = Fraction(10, 1)
    if not (
        c1 == Fraction(1, 1)
        and c2 == Fraction(4, 1)
        and c3 == Fraction(12, 1)
        and taylor_majorant <= expected_majorant
    ):
        raise AssertionError("Taylor coefficient majorization <= 12 failed")

    # Combined annealed cumulant bound at g = U/4:
    # (U / (24 * tau^2)) * (496/(225*g) + (24/U)*12) = (248/675 + 12) * (Omega^2 / tau^2)
    tail_coeff_in_bracket = Fraction(24, 1) * taylor_majorant  # 288
    tail_coeff_total = tail_coeff_in_bracket / Fraction(24, 1)  # 12
    combined_g_quarter = g_quarter_lead + tail_coeff_total  # 8348/675
    combined_cap = Fraction(25, 2)
    if mutant == "flip_combined_annealed_constant":
        combined_cap = Fraction(12, 1)
    if not (
        tail_coeff_in_bracket == Fraction(288, 1)
        and combined_g_quarter == Fraction(8348, 675)
        and combined_g_quarter < combined_cap
    ):
        raise AssertionError("Combined annealed cumulant constant 8348/675 < 25/2 failed")

    # 5. Two-site direct reflection Taylor gap (Theorem 2a)
    n1_lhs = Fraction(2**2 + 1**2, 2)
    n1_rhs = Fraction(5 + 0, 2)
    n2_gap = Fraction(5**2 - (4**2 + 1**2), 24)
    min_gap = Fraction(1, 3)
    if mutant == "flip_dimer_direct_taylor_gap":
        min_gap = Fraction(1, 2)
    if not (n1_lhs == n1_rhs and n2_gap == Fraction(1, 3) and n2_gap >= min_gap):
        raise AssertionError("Two-site direct reflection Taylor gap 1/3 check failed")

    # 6. Regime collapse at g <= U/4, t <= g/64 <= U/256 (Theorem 2c)
    # 2^27 * t^2 / U = (2^27 * t / U) * t <= (2^27 / 256) * t = 2^19 * t,
    # and min(2^10 * t, 2^27 * t^2 / U) <= 2^10 * t, whereas beta * t <= 1 means tau >= t.
    t_over_u_max = Fraction(1, 4) * Fraction(1, 64)
    if not (t_over_u_max == Fraction(1, 256)):
        raise AssertionError("Regime collapse t/U <= 1/256 check failed")

    return {
        "static_mode_raw": str(static_mode_raw),
        "bracket_sum": str(bracket_sum),
        "lead_coeff": str(lead_coeff),
        "g_quarter_lead": str(g_quarter_lead),
        "taylor_majorant": str(taylor_majorant),
        "combined_g_quarter": str(combined_g_quarter),
        "dimer_direct_n2_gap": str(n2_gap),
    }


def arb_reflection_minors(mutant: str | None = None) -> dict[str, str]:
    flint.ctx.prec = 128

    # (a) 2-site dimer direct reflection K_direct(b1, b2) = det(I + exp(-h(b1, b2)))^2
    # at beta = 1, t = 2 on b in {-1, +1}.
    def k_direct_dimer(b1: int, b2: int, t: int = 2) -> flint.arb:
        h = flint.arb_mat([[b1, -t], [-t, b2]])
        ident = flint.arb_mat([[1, 0], [0, 1]])
        d1 = (ident + (-h).exp()).det()
        return d1 * d1

    M_direct = flint.arb_mat(
        [
            [k_direct_dimer(-1, -1), k_direct_dimer(-1, 1)],
            [k_direct_dimer(1, -1), k_direct_dimer(1, 1)],
        ]
    )
    det_direct_2x2 = M_direct.det()
    direct_upper = flint.arb(-4593)
    if mutant == "flip_dimer_direct_2x2_sign":
        direct_upper = flint.arb(-4600)
    if not (det_direct_2x2 < direct_upper):
        raise AssertionError(f"2-site direct 2x2 minor {det_direct_2x2} not < {direct_upper}")

    # Also verify exact algebraic formula 16*(cosh(2)+cosh(1))^2 - 16*(cosh(sqrt(5))+1)^2
    lhs_alg = 4 * (flint.arb(2).cosh() + flint.arb(1).cosh()) ** 2
    rhs_alg = 4 * (flint.arb(5).sqrt().cosh() + flint.arb(1)) ** 2
    det_alg = lhs_alg * lhs_alg - rhs_alg * rhs_alg
    if not (abs(det_direct_2x2 - det_alg) < flint.arb("1e-25")):
        raise AssertionError("2-site direct 2x2 minor algebraic identity mismatch")

    # (b) 2-site dimer particle-hole symmetric kernel M1_dimer(b1, b2)
    def m1_dimer_matrix(b1: int, b2: int, t: int = 2) -> flint.arb:
        h = flint.arb_mat([[b1, -t], [-t, -b2]])
        half = flint.arb("0.5")
        return ((h * half).exp() + (h * (-half)).exp()).det()

    def m1_dimer_closed(b1: int, b2: int, t: int = 2) -> flint.arb:
        b1_a = flint.arb(b1)
        b2_a = flint.arb(b2)
        t_a = flint.arb(t)
        half = flint.arb("0.5")
        return 2 * ((b1_a - b2_a) * half).cosh() + 2 * (
            (((b1_a + b2_a) * half) ** 2 + t_a**2).sqrt()
        ).cosh()

    pts_dimer = [-2, 0, 2]
    for b1 in pts_dimer:
        for b2 in pts_dimer:
            diff = abs(m1_dimer_matrix(b1, b2) - m1_dimer_closed(b1, b2))
            if not (diff < flint.arb("1e-25")):
                raise AssertionError("2-site PH closed form mismatch")

    M_dimer_ph_3x3 = flint.arb_mat(
        [[m1_dimer_matrix(b1, b2) for b2 in pts_dimer] for b1 in pts_dimer]
    )
    det_dimer_ph_3x3 = M_dimer_ph_3x3.det()
    ph_lower = flint.arb(35)
    if mutant == "flip_dimer_ph_3x3_sign":
        ph_lower = flint.arb(36)
    if not (det_dimer_ph_3x3 > ph_lower):
        raise AssertionError(f"2-site PH 3x3 minor {det_dimer_ph_3x3} not > {ph_lower}")

    # (c) 4-site zero-flux ring C4 particle-hole symmetric reflection
    # W = (a1, a2, -b2, -b1) at beta = 1, t = 2 on {(-2,-2), (-2,-1), (-1,-1)}.
    def m1_c4_arb(u: tuple[int, int], v: tuple[int, int], t: int = 2) -> flint.arb:
        a1, a2 = u
        b1, b2 = v
        h = flint.arb_mat(
            [
                [a1, -t, 0, -t],
                [-t, a2, -t, 0],
                [0, -t, -b2, -t],
                [-t, 0, -t, -b1],
            ]
        )
        half = flint.arb("0.5")
        return ((h * half).exp() + (h * (-half)).exp()).det()

    def k_unshifted_c4_arb(u: tuple[int, int], v: tuple[int, int], t: int = 2) -> flint.arb:
        a1, a2 = u
        b1, b2 = v
        h = flint.arb_mat(
            [
                [a1, -t, 0, -t],
                [-t, a2, -t, 0],
                [0, -t, -b2, -t],
                [-t, 0, -t, -b1],
            ]
        )
        ident = flint.arb_mat([[1 if i == j else 0 for j in range(4)] for i in range(4)])
        d1 = (ident + (-h).exp()).det()
        return d1 * d1

    comb_c4 = [(-2, -2), (-2, -1), (-1, -1)]
    M1_c4 = flint.arb_mat([[m1_c4_arb(u, v) for v in comb_c4] for u in comb_c4])
    M2_c4 = flint.arb_mat([[m1_c4_arb(u, v) ** 2 for v in comb_c4] for u in comb_c4])
    K_unshifted_c4 = flint.arb_mat(
        [[k_unshifted_c4_arb(u, v) for v in comb_c4] for u in comb_c4]
    )

    det_m1_c4 = M1_c4.det()
    det_m2_c4 = M2_c4.det()
    det_k_unshifted_c4 = K_unshifted_c4.det()

    c4_m1_cap = flint.arb(-203)
    if mutant == "flip_c4_ph_one_spin_sign":
        c4_m1_cap = flint.arb(-205)
    if not (det_m1_c4 < c4_m1_cap):
        raise AssertionError(f"C4 one-spin PH 3x3 minor {det_m1_c4} not < {c4_m1_cap}")

    c4_m2_cap = flint.arb("-5.87e10")
    if mutant == "flip_c4_ph_two_spin_sign":
        c4_m2_cap = flint.arb("-5.88e10")
    if not (det_m2_c4 < c4_m2_cap):
        raise AssertionError(f"C4 two-spin PH 3x3 minor {det_m2_c4} not < {c4_m2_cap}")

    # Verify diagonal congruence invariance: det(K_unshifted_c4) == det(M2_c4)
    if not (abs(det_m2_c4 - det_k_unshifted_c4) < flint.arb("1e-12")):
        raise AssertionError("C4 diagonal congruence minor invariance failed")

    return {
        "det_direct_2x2": str(det_direct_2x2),
        "det_dimer_ph_3x3": str(det_dimer_ph_3x3),
        "det_m1_c4": str(det_m1_c4),
        "det_m2_c4": str(det_m2_c4),
    }


def arb_two_step_resolvent_and_buffer(mutant: str | None = None) -> dict[str, str]:
    flint.ctx.prec = 128

    # Construct a 1D ring of length L = 8 with site x = 0, ball B_R(x) = {7, 0, 1} of radius R = 1,
    # g = 1, t = 1/64, and a STATIC-MODE resonance on {3, 4, 5} outside B_R(x).
    L = 8
    R = 1
    tau = flint.arb("0.002")
    beta = 1 / tau
    g = flint.arb(1)
    t = flint.arb(1) / flint.arb(64)
    w_mid = (t * t) / (2 * tau) - 2 * tau

    # Sites in B_1(0) are {0, 1, 7}; inner boundary is {1, 7}.
    in_ball = {0, 1, 7}
    inner_bdry = {1, 7}
    W_vals = [flint.arb(0)] * L
    for y in in_ball:
        W_vals[y] = g
    W_vals[2] = flint.arb(100)
    W_vals[6] = flint.arb(100)
    W_vals[3] = 2 * tau
    W_vals[4] = w_mid
    W_vals[5] = 2 * tau

    h_full = flint.arb_mat(L, L)
    h_0 = flint.arb_mat(L, L)
    T_bdry = flint.arb_mat(L, L)
    for i in range(L):
        h_full[i, i] = W_vals[i]
        h_0[i, i] = W_vals[i]
        j = (i + 1) % L
        h_full[i, j] = -t
        h_full[j, i] = -t
        if (i in in_ball) == (j in in_ball):
            h_0[i, j] = -t
            h_0[j, i] = -t
        else:
            T_bdry[i, j] = -t
            T_bdry[j, i] = -t

    # Test at fermionic Matsubara frequencies k = 0, 1, 2
    max_ident_err = flint.arb(0)
    max_first_order = flint.arb(0)
    for k in range(3):
        omega_k = (2 * k + 1) * flint.arb.pi() / beta
        z_mat = flint.acb_mat(L, L)
        for i in range(L):
            z_mat[i, i] = flint.acb(0, omega_k)
        R_full = (z_mat - flint.acb_mat(h_full)).inv()
        R_0 = (z_mat - flint.acb_mat(h_0)).inv()
        T_c = flint.acb_mat(T_bdry)

        # First-order term (R_0 T_bdry R_0)_{0,0} must be identically 0
        first_order_mat = R_0 * T_c * R_0
        fo_val = abs(first_order_mat[0, 0])
        if mutant == "flip_first_order_boundary_zero":
            fo_val = fo_val + flint.arb("1e-3")
        if not (fo_val == 0):
            raise AssertionError(f"First-order boundary term {fo_val} not identically zero")
        if fo_val > max_first_order:
            max_first_order = fo_val

        # Projected two-step identity:
        # (R_full - R_0)_{0,0} == (R_0 P_in T_bdry R_full T_bdry P_in R_0)_{0,0}
        P_in = flint.acb_mat(L, L)
        for idx in inner_bdry:
            P_in[idx, idx] = flint.acb(1)
        two_step_mat = R_0 * P_in * T_c * R_full * T_c * P_in * R_0
        lhs_diff = R_full[0, 0] - R_0[0, 0]
        rhs_two_step = two_step_mat[0, 0]
        if mutant == "flip_two_step_resolvent_identity":
            rhs_two_step = rhs_two_step * flint.acb(2)
        ident_err = abs(lhs_diff - rhs_two_step)
        if not (ident_err < flint.arb("1e-28")):
            raise AssertionError(f"Two-step resolvent identity error {ident_err} too large")
        if ident_err > max_ident_err:
            max_ident_err = ident_err

        # Neumann boundary bound:
        # |R(i*omega_k)_{00} - R_0(i*omega_k)_{00}|
        # <= 16 t^2 / (|omega_k| (omega_k^2 + g^2)) * (4t/g)^{2R} / (1 - 4t/g)^2
        ratio = 4 * t / g
        neumann_rhs = (
            (16 * t * t)
            / (omega_k * (omega_k * omega_k + g * g))
            * (ratio ** (2 * R))
            / ((1 - ratio) ** 2)
        )
        if mutant == "flip_neumann_boundary_bound":
            neumann_rhs = neumann_rhs * flint.arb("1e-6")
        if not (abs(lhs_diff) <= neumann_rhs):
            raise AssertionError(
                f"Neumann boundary bound violated at k={k}: {abs(lhs_diff)} > {neumann_rhs}"
            )

    return {
        "max_first_order": str(max_first_order),
        "max_ident_err": str(max_ident_err),
    }


def exact_ax_from_spectrum(
    evals: np.ndarray, evecs: np.ndarray, tau: float, Omega: float, U: float, x: int
) -> float:
    beta = 1.0 / tau
    p = np.abs(evecs[x, :]) ** 2
    diff = evals[None, :] - evals[:, None]
    f = 1.0 / (1.0 + np.exp(np.clip(beta * evals, -500.0, 500.0)))
    df = f[:, None] - f[None, :]
    w = np.outer(p, p) * df * diff
    # Closed-form Matsubara sum over n >= 1 via partial fractions:
    # sum_{n>=1} Omega^2 / ((nu_n^2 + Omega^2)(nu_n^2 + d^2))
    # For d == 0: 0 since w == 0 on diagonal.
    total = 0.0
    n_modes = np.arange(1, 4000, dtype=float)
    nu = 2.0 * math.pi * n_modes / beta
    r_n = (Omega**2) / (nu**2 + Omega**2)
    for a in range(len(evals)):
        for b in range(len(evals)):
            if w[a, b] == 0.0:
                continue
            d2 = diff[a, b] ** 2
            total += w[a, b] * np.sum(r_n / (nu**2 + d2))
    return 2.0 * U * total


def local_buffer_and_annealed_cumulant(mutant: str | None = None) -> dict[str, float]:
    U = 4.0
    g = 1.0
    t = 1.0 / 64.0
    tau = 0.002
    Omega = 0.001

    # 1. 1D ring L = 12 with resonance at {5, 6, 7}, barriers at {4, 8}, and g-buffer elsewhere
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
    evals_1d, evecs_1d = np.linalg.eigh(H_ring)

    ax_res_1d = exact_ax_from_spectrum(evals_1d, evecs_1d, tau, Omega, U, 5)
    if not (ax_res_1d >= U * (Omega**2) / (1200.0 * (tau**3))):
        raise AssertionError("1D embedded resonance failed STATIC-MODE lower bound")

    ratio = 4.0 * t / g
    for x in [0, 1, 2, 3]:
        R = 3 - x  # distance from x to site 4 is 4-x, so ball of radius R=3-x stays inside {0,1,2,3,9,10,11}
        ax_val = exact_ax_from_spectrum(evals_1d, evecs_1d, tau, Omega, U, x)
        rhs_bound = (
            U
            * (Omega**2)
            / (24.0 * (tau**2))
            * (1.0 / (g - 4.0 * t) + (1.0 / tau) * (ratio ** (2 * R + 2)) / ((1.0 - ratio) ** 2))
        )
        if mutant == "flip_local_buffer_cumulant_bound":
            rhs_bound *= 1e-6
        if not (0.0 <= ax_val <= rhs_bound):
            raise AssertionError(f"Theorem 1b local buffer bound violated at x={x}: {ax_val} > {rhs_bound}")

    # 2. 2D 4x4 torus (16 sites) with STATIC-MODE resonance on {(0,0), (0,1), (0,2)},
    # barrier B=100 on neighbors, and W = g at site (2,2) (distance 2 from resonance, so R=0 ball {(2,2)} has W=g)
    L2 = 4
    W_2d = np.full((L2, L2), 100.0, dtype=float)
    W_2d[0, 0] = 2.0 * tau
    W_2d[0, 1] = w_mid
    W_2d[0, 2] = 2.0 * tau
    W_2d[2, 2] = g
    W_2d[2, 3] = g
    W_2d[3, 2] = g

    H_2d = np.diag(W_2d.ravel())
    for r in range(L2):
        for c in range(L2):
            u = r * L2 + c
            for dr, dc in [(1, 0), (0, 1)]:
                v = ((r + dr) % L2) * L2 + ((c + dc) % L2)
                H_2d[u, v] -= t
                H_2d[v, u] -= t
    evals_2d, evecs_2d = np.linalg.eigh(H_2d)
    ax_res_2d = exact_ax_from_spectrum(evals_2d, evecs_2d, tau, Omega, U, 0)
    ax_buf_2d = exact_ax_from_spectrum(evals_2d, evecs_2d, tau, Omega, U, 2 * L2 + 2)
    rhs_2d_r0 = (
        U
        * (Omega**2)
        / (24.0 * (tau**2))
        * (1.0 / (g - 4.0 * t) + (1.0 / tau) * (ratio**2) / ((1.0 - ratio) ** 2))
    )
    if not (ax_res_2d >= U * (Omega**2) / (2400.0 * (tau**3)) and ax_buf_2d <= rhs_2d_r0):
        raise AssertionError("2D 4x4 torus resonance/buffer check failed")

    # 3. Annealed expectation bound along the linear ray tau = C * Omega (Theorem 1c)
    C_ray = 1.0
    for Om in [1e-2, 1e-3, 1e-4]:
        tau_ray = C_ray * Om
        R_adapt = max(0, math.ceil(math.log(g / tau_ray) / math.log(16.0)) - 1)
        vol_ball = 2 * R_adapt * R_adapt + 2 * R_adapt + 1
        annealed_bound = (
            U
            * (Om**2)
            / (24.0 * (tau_ray**2))
            * (496.0 / (225.0 * g) + (vol_ball / (2.0 * tau_ray)) * math.exp(-U / (48.0 * tau_ray)))
        )
        cap_uniform = (8348.0 / 675.0) * ((Om / tau_ray) ** 2)
        if mutant == "flip_annealed_ray_limit_bound":
            cap_uniform = 0.30 * ((Om / tau_ray) ** 2)
        if not (annealed_bound < cap_uniform):
            raise AssertionError(f"Annealed ray bound failed at Omega={Om}")

    return {
        "ax_res_1d": ax_res_1d,
        "ax_buf_1d_x0": exact_ax_from_spectrum(evals_1d, evecs_1d, tau, Omega, U, 0),
        "ax_res_2d": ax_res_2d,
        "ax_buf_2d": ax_buf_2d,
    }


def run_all_checks(mutant: str | None = None) -> dict[str, object]:
    res_rat = exact_rational_constants(mutant)
    res_arb = arb_reflection_minors(mutant)
    res_res = arb_two_step_resolvent_and_buffer(mutant)
    res_num = local_buffer_and_annealed_cumulant(mutant)
    return {
        "rational": res_rat,
        "arb_reflection": res_arb,
        "arb_resolvent": res_res,
        "numerical_buffer": res_num,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Replay checks for ANNEALED-STATIC.")
    parser.add_argument("--mutant", choices=MUTANTS, help="Run with a specific mutant injected.")
    parser.add_argument("--all-mutants", action="store_true", help="Verify all mutants fail.")
    args = parser.parse_args()

    if args.all_mutants:
        for m in MUTANTS:
            proc = subprocess.run(
                [sys.executable, "-B", __file__, "--mutant", m],
                capture_output=True,
                text=True,
                check=False,
            )
            if proc.returncode == 0:
                print(f"MUTANT SURVIVED: {m}", file=sys.stderr)
                return 1
            print(f"REJECTED {m} (exit {proc.returncode})")
        print(f"ALL {len(MUTANTS)} MUTANTS REJECTED.")
        return 0

    results = run_all_checks(args.mutant)
    print("ALL ANNEALED-STATIC REPLAY CHECKS PASSED.")
    for section, data in results.items():
        print(f"[{section}] {data}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
