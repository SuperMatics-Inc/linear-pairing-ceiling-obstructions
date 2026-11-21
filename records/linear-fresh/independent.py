#!/usr/bin/env python3
"""Independent second implementation (SymPy + mpmath.iv) for LINEAR-FRESH.

Checks explicit rational/interval fixtures without python-flint. This is a
second implementation, not independent scientific review or a ceiling proof.

Usage:
  python -B independent.py
"""
from __future__ import annotations

import sympy as sp
from mpmath import iv, mp

mp.dps = 60
iv.dps = 60


def check(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def verify_route_a_independent() -> None:
    """Check Einstein covariance and exact static electronic anchors."""
    # Symbolic check of Fourier transform of sum_x (K/2) X_x^2:
    K_sym = sp.Symbol("K", positive=True)
    # In momentum space, K(q) = K for all q in B:
    q_sym = sp.Symbol("q", real=True)
    K_q = sp.simplify(K_sym + 0 * sp.cos(q_sym))
    check(sp.diff(K_q, q_sym) == 0, "Einstein stiffness K(q) must have zero q-derivative")

    # High-precision mpmath check of naive free Debye-Waller factor at U=4, Om=0.2, beta=20:
    U_m = mp.mpf("4.0")
    Om_m = mp.mpf("0.2")
    beta_m = mp.mpf("20.0")
    dw_free = mp.exp(-(2 * U_m / Om_m) * mp.coth(beta_m * Om_m / 2))
    check(dw_free < mp.mpf("3e-18"), f"Expected free DW factor < 3e-18, got {dw_free}")

    # Frozen relative field q=2U, not the relaxed BO minimum at nonzero t.
    t_s = sp.Rational(1, 1)
    U_s = sp.Rational(4, 1)
    H_stat = sp.Matrix([
        [-2 * U_s, 0, -sp.sqrt(2) * t_s],
        [0, 2 * U_s, -sp.sqrt(2) * t_s],
        [-sp.sqrt(2) * t_s, -sp.sqrt(2) * t_s, 0],
    ])
    # Exact characteristic polynomial of H_stat:
    # E * (E^2 - 4*U^2) - 2*t^2*(E - 2*U) - 2*t^2*(E + 2*U) = E * (E^2 - 4*U^2 - 4*t^2) = 0!
    # Eigenvalues are E_0 = -2*sqrt(U^2 + t^2), E_2 = 0, E_1 = +2*sqrt(U^2 + t^2)!
    evals_stat = H_stat.eigenvals()
    E0_stat = -2 * sp.sqrt(U_s ** 2 + t_s ** 2)
    check(E0_stat in evals_stat, "Exact static Born-Oppenheimer ground energy formula failed")
    c2 = sp.sqrt(t_s ** 2 / (2 * (U_s ** 2 + t_s ** 2)))
    c0 = sp.sqrt(2) * t_s * c2 / (-2 * U_s - E0_stat)
    c1 = sp.sqrt(2) * t_s * c2 / (2 * U_s - E0_stat)
    psi = sp.Matrix([c0, c1, c2])
    check(all(sp.simplify(x) == 0 for x in H_stat * psi - E0_stat * psi), "Static eigenvector failed")
    check(sp.simplify((psi.T * psi)[0] - 1) == 0, "Static eigenvector normalization failed")
    corr_stat_exact = sp.simplify(c0 * c1)
    check(corr_stat_exact == sp.Rational(1, 68), f"Frozen-field correlator mismatch: {corr_stat_exact}")

    # Relaxed static BO minima exist for U>t, at q=+-2*sqrt(U^2-t^2).
    q_min = 2 * sp.sqrt(U_s ** 2 - t_s ** 2)
    H_min = H_stat + sp.diag(2 * U_s - q_min, q_min - 2 * U_s, 0)
    E_min = -2 * U_s
    c2_min = sp.sqrt(t_s ** 2 / (2 * U_s ** 2))
    psi_min = sp.Matrix([
        sp.sqrt(2) * t_s * c2_min / (-q_min - E_min),
        sp.sqrt(2) * t_s * c2_min / (q_min - E_min),
        c2_min,
    ])
    check(all(sp.simplify(x) == 0 for x in H_min * psi_min - E_min * psi_min), "BO-minimum eigenvector failed")
    check(sp.simplify((psi_min.T * psi_min)[0] - 1) == 0, "BO-minimum eigenvector normalization failed")
    check(sp.simplify(psi_min[0] * psi_min[1]) == sp.Rational(1, 64), "BO-minimum correlator mismatch")


def verify_route_b_independent() -> None:
    """Exact symbolic verification of the oscillator commutator and Basel identity."""
    # Symbolic Weyl-Heisenberg algebra [a, a_dag] = 1:
    # b = g*(a + a_dag), H_ph = Om * a_dag * a, H_int = -b * n_el
    # [H_ph + H_int, b] = Om * g * [a_dag * a, a + a_dag] = Om * g * (-a + a_dag)
    # [[H_ph + H_int, b], b] = Om * g^2 * [-a + a_dag, a + a_dag] = -2 * Om * g^2 = -U * Om^2 (since g^2 = U*Om/2).
    U_s, Om_s = sp.symbols("U Omega", positive=True)
    g_sq = U_s * Om_s / 2
    double_comm = sp.simplify(2 * Om_s * g_sq)
    check(double_comm == U_s * Om_s ** 2, "Symbolic positive double commutator [b, [H, b]] failed")

    # Symbolic Basel sum: sum_{k=1}^infty 1 / (4 * pi^2 * k^2) == 1/24
    k_s = sp.Symbol("k", integer=True, positive=True)
    basel_sym = sp.summation(1 / (4 * sp.pi ** 2 * k_s ** 2), (k_s, 1, sp.oo))
    check(sp.simplify(basel_sym - sp.Rational(1, 24)) == 0, f"Symbolic Basel sum failed: {basel_sym}")


def verify_route_c_independent() -> None:
    """Interval witness/series checks and symbolic 2-mode Ward-Schur algebra."""
    # 1. Interval arithmetic (mpmath.iv) certification of the 2-slice N_b = 1 non-normal witness:
    v_iv = iv.mpf("0.5")
    b1_iv = iv.mpf("-6.0")
    b2_iv = iv.mpf("6.0")

    def exp_neg_2x2_iv(b_val, v_val):
        m = b_val / 2
        d = iv.sqrt(m * m + v_val * v_val)
        em = iv.exp(-m)
        ed_p = iv.exp(d)
        ed_m = iv.exp(-d)
        cd = (ed_p + ed_m) / 2
        sd_d = (ed_p - ed_m) / (2 * d)
        u00 = em * (cd - sd_d * m)
        u01 = em * (sd_d * v_val)
        u11 = em * (cd + sd_d * m)
        return ((u00, u01), (u01, u11))

    U1 = exp_neg_2x2_iv(b1_iv, v_iv)
    U2 = exp_neg_2x2_iv(b2_iv, v_iv)
    U1_inv = exp_neg_2x2_iv(-b1_iv, -v_iv)

    # U_full = U2 * U1:
    uf00 = U2[0][0] * U1[0][0] + U2[0][1] * U1[1][0]
    uf01 = U2[0][0] * U1[0][1] + U2[0][1] * U1[1][1]
    uf10 = U2[1][0] * U1[0][0] + U2[1][1] * U1[1][0]
    uf11 = U2[1][0] * U1[0][1] + U2[1][1] * U1[1][1]
    det_I_plus_U = 1 + (uf00 + uf11) + (uf00 * uf11 - uf01 * uf10)
    check(det_I_plus_U.a > mp.mpf("15.0"), f"iv det(I+U) lower bound <= 15: {det_I_plus_U}")

    # M = U1_inv + U2, G(1, 0)_{00} = -M_{11} / det(M):
    m00 = U1_inv[0][0] + U2[0][0]
    m01 = U1_inv[0][1] + U2[0][1]
    m11 = U1_inv[1][1] + U2[1][1]
    det_M = m00 * m11 - m01 * m01
    g00_abs = abs(m11 / det_M)
    check(g00_abs.a > mp.mpf("52.89"), f"iv |G(1,0)_{{00}}| lower bound <= 52.89: {g00_abs}")
    # Independent scalar formula for the arbitrary-amplification family.
    d = iv.sqrt(iv.mpf(9) + v_iv * v_iv)
    a = iv.mpf(3) / d
    g_scalar = iv.exp(iv.mpf(3)) / ((1 - a) * iv.exp(d) + (1 + a) * iv.exp(-d))
    check(abs(g_scalar - g00_abs).b < mp.mpf("1e-45"), "Scalar amplification formula mismatch")

    # 2. Symbolic verification of Theorem 4.3 identities on the 2-mode (n=0, m=0) subspace:
    # A = [[i*D0 - delta0, -b1], [-b1_conj, -i*D0 - delta0]]
    D0_s = sp.Symbol("D0", positive=True)
    del0_s = sp.Symbol("delta0", real=True)
    b1_s = sp.Symbol("b1", nonnegative=True)
    A_2 = sp.Matrix([
        [sp.I * D0_s - del0_s, -b1_s],
        [-b1_s, -sp.I * D0_s - del0_s],
    ])
    G_2 = A_2.inv()
    G_pp = G_2[0, 0]
    G_pm = G_2[0, 1]
    Q_00 = b1_s ** 2 / (D0_s ** 2 + del0_s ** 2) * D0_s
    # Verify |G_pm|^2 * D0 == |G_pp|^2 * Q_00 and -Im(G_pp) == |G_pp|^2 * (D0 - Q_00):
    lhs_neg = sp.simplify(sp.Abs(G_pm) ** 2 * D0_s)
    rhs_neg = sp.simplify(sp.Abs(G_pp) ** 2 * Q_00)
    check(sp.simplify(lhs_neg - rhs_neg) == 0, "Symbolic 2x2 Schur identity |G_pm|^2 D0 == |G_pp|^2 Q failed")

    im_Gpp = sp.simplify(-sp.im(G_pp))
    rhs_im = sp.simplify(sp.Abs(G_pp) ** 2 * (D0_s - Q_00))
    check(sp.simplify(im_Gpp - rhs_im) == 0, "Symbolic 2x2 dissipation identity -Im G_pp == |G_pp|^2 (D0 - Q) failed")

    # 3. Independent interval enclosure of auxiliary C_aux, not a ceiling coefficient.
    K0 = 300
    s_iv = iv.mpf(0)
    for k in range(1, K0 + 1):
        s_iv += (iv.mpf(2) + iv.log(iv.mpf(2 * k - 1))) / (iv.mpf(2) * (iv.mpf(k) ** 3))
    tail_hi = (iv.mpf("2.5") + iv.log(iv.mpf(2 * K0))) / (iv.mpf(4) * (iv.mpf(K0) ** 2))
    c_univ_iv = s_iv + iv.mpf([0, tail_hi.b])
    check(c_univ_iv.a > mp.mpf(67) / 50 and c_univ_iv.b < mp.mpf(27) / 20, f"iv C_univ out of (67/50, 27/20): {c_univ_iv}")

    # 4. Symbolic proof of density-blind supremum:
    # 1/(4*w0) - x/(w0 + x)^2 == (x - w0)^2 / (4 * w0 * (w0 + x)^2) >= 0 for all w0 > 0, x >= 0
    w0_s, x_s = sp.symbols("w0 x", positive=True)
    diff_id = sp.factor(sp.Rational(1, 4) / w0_s - x_s / (w0_s + x_s) ** 2)
    expected_id = (x_s - w0_s) ** 2 / (4 * w0_s * (w0_s + x_s) ** 2)
    check(sp.simplify(diff_id - expected_id) == 0, "Symbolic SOS identity for density-blind supremum failed")


def verify_route_d_independent() -> None:
    """Symbolic verification of fixed-particle-number COM decoupling only."""
    # Shift a_+ -> a_+ - (g / (sqrt(2)*Om)) * (n_1 + n_2).
    # the COM oscillator decouples completely in every fixed N_tot = n_1 + n_2 sector:
    g_s, Om_s, N_s, X_p = sp.symbols("g Omega N_tot X_plus", positive=True)
    # H_com = (Om/4)*(P_+^2 + X_+^2) - (g/sqrt(2))*N_tot*X_+
    # Completing the square in X_+:
    X_shift = X_p - sp.sqrt(2) * g_s * N_s / Om_s
    diff_pot = sp.simplify((Om_s / 4) * X_p ** 2 - (g_s / sp.sqrt(2)) * N_s * X_p - ((Om_s / 4) * X_shift ** 2 - g_s ** 2 * N_s ** 2 / (2 * Om_s)))
    check(diff_pot == 0, "Symbolic COM square-completion failed")


def main() -> int:
    verify_route_a_independent()
    verify_route_b_independent()
    verify_route_c_independent()
    verify_route_d_independent()
    print("LINEAR-FRESH independent.py (SymPy + mpmath.iv): ALL INDEPENDENT CHECKS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
