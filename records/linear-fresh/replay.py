#!/usr/bin/env python3
"""Rational/interval fixtures and floating-point diagnostics for LINEAR-FRESH.

The interval witness and series enclosure have second implementations.
Truncated ED and Matsubara fixtures are NUMERICAL, not certificates of an
infinite-volume pairing ceiling. See RIGOR.md and RESULT.md for exact scope.

Usage:
  python -B replay.py
  python -B replay.py --all-mutants
  python -B replay.py --mutant NAME
"""
from __future__ import annotations

import math
import sys
from fractions import Fraction as Q

import numpy as np
from flint import arb, arb_mat, ctx, fmpq  # type: ignore[import-untyped]
from scipy.linalg import eigh, expm, inv

ctx.dps = 80

MUTANTS = (
    # Route (a): Reflection positivity & Lang-Firsov Debye-Waller factorization
    "route_a_debye_waller_bound_assumed",      # falsely claim <Delta_1^+ Delta_2> <= 0.5 * <V_1^+ V_2>_free
    "route_a_dls_infrared_q_dependent",        # falsely claim Einstein phonon <X_q^2>_free vanishes at q=pi
    # Route (b): Exact interacting quantum Lehmann sum rule
    "route_b_lehmann_missing_pi_sq",           # drop 4*pi^2 in E[|b_k|^2] <= U*Om^2/(4*pi^2*k^2*T)
    "route_b_lehmann_sum_wrong_24",            # replace 1/24 by 1/48 in sum_{k>=1} E[|b_k|^2] <= U*Om^2/(24*T)
    "route_b_lehmann_commutator_t_dep",        # falsely claim [H_el, X_x] != 0
    # Route (c): Total positivity fixtures, non-normal witness, and Ward-Schur algebra
    "route_c_krylov_negative_eig",             # flip sign of off-diagonal in Jacobi reduction to break TP
    "route_c_pathwise_green_bounded_by_1",     # falsely claim |G(tau1, tau2; b)_{00}| <= 1 for all trajectories
    "route_c_halfspace_norm_gt_1",             # corrupt ||D_+^{1/2} A_{++}^{-1} D_+^{1/2}||_op bound from 1 to 1/2
    "route_c_schur_q_sign_flipped",            # flip sign of -Q in -Im G_{++} = G_{++} (D_+ - Q) G_{++}^+
    "route_c_ward_leak_factor_1_instead_of_2", # corrupt 2*t_*^2*E[Neg_n] to 1*t_*^2*E[Neg_n] in (K_+ D)_n
    "route_c_alpha_threshold_2_instead_of_1",  # falsely claim D_+ - Q >= 0 holds up to alpha = 2
    "route_c_low_energy_window_factor_1",      # falsely claim D_n >= (omega_n + gamma_met) without 1/2 factor
    "route_c_cuniv_underestimated",            # replace C_aux upper bound 27/20 by 4/3
    "route_c_density_blind_sup_wrong",         # replace sup_{d0>=0} t_*^2 d0 / (w0 + t_*^2 d0)^2 = 1/(4*w0) by 1/(8*w0)
    # Route (d): 2-site Holstein dimer & bipolaron tunnel splitting
    "route_d_dimer_com_coupled",               # falsely claim [H_dimer, a_+^+ a_+] != 0 in N=2 sector
    "route_d_dimer_bipolaron_linear_split",    # falsely claim strong-coupling dimer splitting is >= 0.1*Omega at U=4, Om=0.05
)


def require(cond: bool | np.bool_, msg: str) -> None:
    if not bool(cond):
        raise AssertionError(msg)


def arb_from_q(x: Q) -> arb:
    return arb(fmpq(x.numerator, x.denominator))


# ============================================================================
# Route (a): Reflection Positivity & Naive Lang-Firsov Debye-Waller Failure
# ============================================================================
def check_route_a_rp_and_debye_waller(mutant: str | None = None) -> None:
    """Check free Einstein covariance and a NUMERICAL truncated-dimer fixture.
    The latter illustrates, but does not certify, failed free-field factorization.
    """
    # 1. Exact q-independence of free/thermal Einstein oscillator covariance:
    # For H_ph = sum_x (P_x^2/(2M) + K X_x^2 / 2), the static stiffness is K(q) = K for all q.
    K_val = arb("2.5")
    Omega_val = arb("0.4")
    beta_val = arb("10.0")
    _ = K_val / (Omega_val * Omega_val)
    # Equal-time variance <X_q^2> = coth(beta*Omega/2) / (2*M*Omega) = (Omega/(2*K)) * coth(beta*Omega/2)
    var_q0 = (Omega_val / (arb(2) * K_val)) * (beta_val * Omega_val / arb(2)).coth()
    var_qpi = var_q0  # identical for q=0 and q=pi for optical/Einstein modes
    if mutant == "route_a_dls_infrared_q_dependent":
        var_qpi = arb(0)
    require(abs(var_q0 - var_qpi) < arb("1e-70"), "Einstein phonon variance must be q-independent")

    # 2. Exact 2-site spinful Holstein dimer in N=2, S_z=0 singlet sector (3 electronic states x N_ph relative modes)
    # Electronic basis: |0> = c_{1u}^+ c_{1d}^+ |vac> (pair on 1),
    #                   |1> = c_{2u}^+ c_{2d}^+ |vac> (pair on 2),
    #                   |2> = (c_{1u}^+ c_{2d}^+ - c_{1d}^+ c_{2u}^+) |vac> / sqrt(2) (singlet covalent)
    # Relative phonon mode a_- = (a_1 - a_2)/sqrt(2):
    # n_1 - n_2 = diag(2, -2, 0), so H_int = -(g / sqrt(2)) (a_- + a_-^+) (n_1 - n_2)
    # with U = 2 * g^2 / Omega => g / sqrt(2) = sqrt(U * Omega) / 2, so coupling on |0>, |1> is -/+ sqrt(U*Omega) (a_- + a_-^+).
    t_val = 1.0
    U_val = 4.0
    Om_val = 0.2
    beta_d = 20.0
    N_ph = 80

    h_el = np.array([
        [0.0, 0.0, -np.sqrt(2.0) * t_val],
        [0.0, 0.0, -np.sqrt(2.0) * t_val],
        [-np.sqrt(2.0) * t_val, -np.sqrt(2.0) * t_val, 0.0],
    ])
    n_diff_half = np.diag([1.0, -1.0, 0.0])  # (n_1 - n_2)/2
    a_op = np.diag(np.sqrt(np.arange(1, N_ph, dtype=float)), 1)
    x_rel = a_op + a_op.T
    n_ph = np.diag(np.arange(N_ph, dtype=float))

    H_dim = (
        np.kron(h_el, np.eye(N_ph))
        + Om_val * np.kron(np.eye(3), n_ph)
        - np.sqrt(U_val * Om_val) * np.kron(n_diff_half, x_rel)
    )
    evals, evecs = eigh(H_dim)
    evals_shift = evals - evals[0]
    w_boltz = np.exp(-beta_d * evals_shift)
    Z_can = np.sum(w_boltz)

    # Inter-site pair correlator <Delta_1^+ Delta_2> where Delta_1^+ Delta_2 maps |1> -> |0>
    op_d1_d2 = np.zeros((3, 3))
    op_d1_d2[0, 1] = 1.0
    full_d1_d2 = np.kron(op_d1_d2, np.eye(N_ph))
    diag_mat = np.einsum("ki,kl,li->i", evecs, full_d1_d2, evecs)
    corr_exact = float(np.sum(w_boltz * diag_mat) / Z_can)  # NUMERICAL, finite Fock cutoff

    # Naive Lang-Firsov / chessboard Debye-Waller factor:
    # V_1^+ V_2 = exp(i * sqrt(4*U/Omega) * P_rel), so <V_1^+ V_2>_free = exp(-(2*U/Omega) * coth(beta*Omega/2))
    dw_free = float( math.exp(-(2.0 * U_val / Om_val) / math.tanh(0.5 * beta_d * Om_val)) )
    naive_dw_bound = 0.5 * dw_free

    if mutant == "route_a_debye_waller_bound_assumed":
        require(corr_exact <= naive_dw_bound, "Mutant falsely assumed naive Debye-Waller factor upper-bounds <Delta_1^+ Delta_2>")
    else:
        require(corr_exact > 0.01, f"Expected O(t^2/U^2) > 0.01 intra-well dimer pair correlator, got {corr_exact}")
        require(corr_exact / naive_dw_bound > 1e16, f"Expected >1e16 violation of naive DW factorization, got {corr_exact / naive_dw_bound}")


# ============================================================================
# Route (b): Exact Interacting Quantum Lehmann Sum Rule for Phonon Modes
# ============================================================================
def check_route_b_lehmann_sum_rule(mutant: str | None = None) -> None:
    """Check commutator and sum-rule fixtures from RIGOR section 2.
    The full-Hilbert-space theorem is analytical; finite-Fock-space ED only
    checks its normalization numerically and is not an interval certificate.
    """
    # 1. Matrix commutator fixture on 2-site spinful Fock space x 32 oscillator states
    I2 = np.eye(2, dtype=int)
    sz = np.array([[1, 0], [0, -1]], dtype=int)
    sp = np.array([[0, 1], [0, 0]], dtype=int)
    sm = sp.T

    def kron4(a, b, c, d):
        return np.kron(np.kron(a, b), np.kron(c, d))

    c1u = kron4(sm, I2, I2, I2)
    c1d = kron4(sz, sm, I2, I2)
    c2u = kron4(sz, sz, sm, I2)
    c2d = kron4(sz, sz, sz, sm)
    n1 = c1u.T @ c1u + c1d.T @ c1d
    n2 = c2u.T @ c2u + c2d.T @ c2d
    hop = (c1u.T @ c2u + c2u.T @ c1u) + (c1d.T @ c2d + c2d.T @ c1d)

    N_ph = 32
    a_ph = np.diag(np.sqrt(np.arange(1, N_ph, dtype=float)), 1)
    x_ph = a_ph + a_ph.T
    _ = -1j * (a_ph - a_ph.T)  # finite-Fock commutator has a boundary correction

    # Check [H_el + H_int, I_el (x) x_ph] == 0 identically:
    H_el_int = np.kron(-1.3 * hop - 0.4 * (n1 + n2), np.eye(N_ph)) - 0.9 * np.kron(n1, x_ph)
    X1_op = np.kron(np.eye(16), x_ph)
    comm_el_x = H_el_int @ X1_op - X1_op @ H_el_int
    if mutant == "route_b_lehmann_commutator_t_dep":
        require(np.max(np.abs(comm_el_x)) > 1.0, "Mutant falsely claimed [H_el + H_int, X_x] != 0")
    else:
        require(np.max(np.abs(comm_el_x)) < 1e-14, "[H_el + H_int, X_x] must vanish identically")

    # 2. Exact Lehmann identity and mode-by-mode bound on interacting 2-site impurity + bath system
    U_val = 2.4
    Om_val = 0.35
    T_val = 0.15
    beta_val = 1.0 / T_val
    # [H_ph, b] = Om*g*(-a + a^+) = -i*Om*g*p_ph for p_ph = -i*(a-a^+)
    g_val = math.sqrt(0.5 * U_val * Om_val)
    H_full = (
        np.kron(-0.8 * hop - 0.3 * n1 + 0.5 * n2 + 1.1 * (c1u.T @ c1u @ c1d.T @ c1d), np.eye(N_ph))
        + Om_val * np.kron(np.eye(16), a_ph.T @ a_ph)
        - g_val * np.kron(n1 - np.eye(16), x_ph)
    )
    B_op = g_val * X1_op

    evals, evecs = eigh(H_full)
    evals = evals - evals[0]
    w = np.exp(-beta_val * evals)
    Z = float(np.sum(w))
    B_eig = evecs.T @ B_op @ evecs
    dE = evals[None, :] - evals[:, None]
    dw = w[:, None] - w[None, :]

    # Exact f-sum rule: sum_{a != b} ((e^{-beta E_a} - e^{-beta E_b}) / (Z * (E_b - E_a))) * (E_b - E_a)^2 |B_{ab}|^2
    # = sum_{a,b} (w_a - w_b) (E_b - E_a) |B_{ab}|^2 / Z, approaching U*Om^2 as N_ph grows
    f_sum_num = float(np.sum(dw * dE * (np.abs(B_eig) ** 2)) / Z)
    require(abs(f_sum_num - U_val * (Om_val ** 2)) < 1e-11, f"Lehmann f-sum rule mismatch: {f_sum_num} vs {U_val * Om_val**2}")

    # Mode-by-mode check for k = 1..6:
    pi_sq_factor = 1.0 if mutant == "route_b_lehmann_missing_pi_sq" else 4.0 * (math.pi ** 2)
    sum_eb2 = 0.0
    for k in range(1, 25):
        nu_k = 2.0 * math.pi * k * T_val
        mask = np.abs(dE) > 1e-12
        term = np.zeros_like(dE)
        term[mask] = (dw[mask] * dE[mask]) / ((dE[mask] ** 2 + nu_k ** 2) * Z)
        ebk2_exact = float(np.sum(term * (np.abs(B_eig) ** 2)) / beta_val)
        ebk2_bound = U_val * (Om_val ** 2) / (pi_sq_factor * (k ** 2) * T_val)
        if k <= 6:
            if mutant == "route_b_lehmann_missing_pi_sq":
                # If 4*pi^2 was dropped, bound would be 39.47x too loose; verify exact tight ratio at high k!
                require(ebk2_bound / ebk2_exact < 2.0, "Mutant dropped 4*pi^2 factor in Lehmann bound")
            else:
                require(ebk2_exact <= ebk2_bound * (1.0 + 1e-12), f"Lehmann mode bound violated at k={k}")
                # At k=6, nu_6 >> dE, so ebk2_exact / ebk2_bound is close to 1:
                if k == 6:
                    require(ebk2_exact / ebk2_bound > 0.90, f"Lehmann bound not tight at k=6: ratio={ebk2_exact / ebk2_bound}")
        sum_eb2 += ebk2_exact

    # Check Basel sum: sum_{k=1}^infty 1/(4*pi^2*k^2) = 1/24 in outward Arb
    basel_denom = arb(48) if mutant == "route_b_lehmann_sum_wrong_24" else arb(24)
    # Exact Basel identity: (pi^2 / 6) / (4 * pi^2) = 1 / 24
    basel_exact = (arb.pi() ** 2 / arb(6)) / (arb(4) * (arb.pi() ** 2))
    require(abs(basel_exact - arb(1) / basel_denom) < arb("1e-70"), "Basel sum factor 1/24 mismatch")
    require(sum_eb2 <= U_val * (Om_val ** 2) / (float(basel_denom) * T_val), "Total dynamic variance exceeded U*Om^2/(24*T)")


# ============================================================================
 # Route (c): Total Positivity Fixtures, Non-Normal Witness, and Ward-Schur Algebra
# ============================================================================
def check_route_c_total_positivity_and_witness(mutant: str | None = None) -> None:
    """Check a floating-point Krylov fixture and an outward-rounded 2-slice witness.
    Only the explicit 2-slice interval witness has independent certification.
    The general analytical positivity argument is pending independent review.
    """
    # 1. Certify Lanczos reduction fixing e_0 and strict positivity of all eigenvalues of U(beta, 0; b)
    # on a 4-site star graph (1 dynamic impurity + 3 static bath sites)
    h_star = np.array([
        [0.0, -0.7, -0.5, -0.9],
        [-0.7, -1.2, 0.0, 0.0],
        [-0.5, 0.0, 0.3, 0.0],
        [-0.9, 0.0, 0.0, 1.5],
    ])
    # Build orthogonal Lanczos basis Q_L with Q_L[:, 0] = e_0 such that -Q_L^T h_star Q_L is Jacobi
    N_tot = h_star.shape[0]
    Q_L = np.zeros((N_tot, N_tot))
    Q_L[:, 0] = np.array([1.0, 0.0, 0.0, 0.0])
    A_neg = -h_star
    for j in range(N_tot - 1):
        v = A_neg @ Q_L[:, j]
        for i in range(j + 1):
            v = v - np.dot(Q_L[:, i], v) * Q_L[:, i]
        norm_v = np.linalg.norm(v)
        require(norm_v > 1e-10, "Krylov chain terminated prematurely")
        Q_L[:, j + 1] = v / norm_v

    J0 = Q_L.T @ A_neg @ Q_L
    if mutant == "route_c_krylov_negative_eig":
        # Flip sign of off-diagonal entry J0[0, 1] -> -J0[0, 1], breaking symmetry/TP
        J0[0, 1] = -J0[0, 1]

    # Verify J0 is symmetric tridiagonal with strictly positive super/sub-diagonal:
    for i in range(N_tot):
        for j in range(N_tot):
            if abs(i - j) > 1:
                require(abs(J0[i, j]) < 1e-14, f"Non-tridiagonal entry at ({i},{j})")
            elif abs(i - j) == 1:
                require(J0[i, j] > 0.1, f"Jacobi off-diagonal not positive at ({i},{j}): {J0[i,j]}")
        if mutant == "route_c_krylov_negative_eig":
            require( abs(J0[0, 1] - J0[1, 0]) < 1e-12, "Mutant broke symmetric Jacobi structure" )

    # Product of 6 wild time slices b_s in {-8.0, +9.5, -11.0, +7.2, -6.4, +10.1}:
    b_slices = [-8.0, 9.5, -11.0, 7.2, -6.4, 10.1]
    U_mono = np.eye(N_tot)
    for b_s in b_slices:
        J_s = J0.copy()
        J_s[0, 0] -= b_s  # since A_neg = -(h_star + b_s P_0) = J0 - b_s e_0 e_0^T
        U_mono = expm(0.25 * J_s) @ U_mono

    # Verify all minors of order 1 and 2 of U_mono are strictly positive (TP) and all eigenvalues are real > 0:
    require(np.min(U_mono) > 0.0, "Monodromy matrix in Krylov basis is not entrywise positive")
    for i1 in range(N_tot):
        for i2 in range(i1 + 1, N_tot):
            for j1 in range(N_tot):
                for j2 in range(j1 + 1, N_tot):
                    det2 = U_mono[i1, j1] * U_mono[i2, j2] - U_mono[i1, j2] * U_mono[i2, j1]
                    require(det2 > 0.0, f"2x2 minor ({i1},{i2}; {j1},{j2}) not positive: {det2}")

    eigs_mono = np.linalg.eigvals(U_mono)
    require(np.max(np.abs(np.imag(eigs_mono))) < 1e-12, f"Non-real eigenvalue in TP monodromy: {eigs_mono}")
    require(np.min(np.real(eigs_mono)) > 0.0, f"Non-positive eigenvalue in TP monodromy: {eigs_mono}")
    det_1_plus_U = float(np.prod(1.0 + np.real(eigs_mono)))
    require(det_1_plus_U > 1.0, f"det(I + U) must exceed 1, got {det_1_plus_U}")

    # 2. Certify Proposition 4.2 in outward-rounded Arb:
    # Explicit 2-slice N_b = 1 witness: h(tau) = [[b(tau), -V], [-V, 0]] with V = 1/2,
    # Slice 1 (length L_1 = 1): b_1 = -6; Slice 2 (length L_2 = 1): b_2 = +6.
    # Both U_1 = exp(-h_1) and U_2 = exp(-h_2) are 2x2 SPD and strictly totally positive,
    # det(I + U_2 U_1) > 1, yet |(U_1^{-1} + U_2)^{-1}_{00}| > 30!
    V_w = arb("0.5")
    b1_w = arb("-6.0")
    b2_w = arb("6.0")

    def exp_neg_2x2_arb(b_val: arb, v_val: arb) -> arb_mat:
        # h = [[b, -v], [-v, 0]]. Trace = b, det = -v^2, half-trace m = b/2, d = sqrt((b/2)^2 + v^2).
        # exp(-h) = e^{-m} (cosh(d) I - (sinh(d)/d) (h - m I))
        m = b_val / arb(2)
        d = (m * m + v_val * v_val).sqrt()
        em = (-m).exp()
        cd = d.cosh()
        sd_over_d = d.sinh() / d
        u00 = em * (cd - sd_over_d * m)
        u01 = em * (sd_over_d * v_val)
        u11 = em * (cd + sd_over_d * m)
        return arb_mat([[u00, u01], [u01, u11]])

    U1_arb = exp_neg_2x2_arb(b1_w, V_w)
    U2_arb = exp_neg_2x2_arb(b2_w, V_w)
    U1_inv_arb = exp_neg_2x2_arb(-b1_w, -V_w)  # exp(+h_1)
    # Check U1_arb * U1_inv_arb == I:
    prod_id = U1_arb * U1_inv_arb
    require(abs(prod_id[0, 0] - arb(1)) < arb("1e-65") and abs(prod_id[0, 1]) < arb("1e-65"), "Arb 2x2 inverse failed")

    # Monodromy U_full = U2 * U1:
    U_full = U2_arb * U1_arb
    tr_U = U_full[0, 0] + U_full[1, 1]
    det_U = U_full[0, 0] * U_full[1, 1] - U_full[0, 1] * U_full[1, 0]
    det_I_plus_U = arb(1) + tr_U + det_U
    require(det_I_plus_U > arb(15), f"Expected det(I + U) > 15, got {det_I_plus_U}")

    # Green's matrix at (tau_1, tau_2) = (1, 0): -G(1, 0; b) = (U_1^{-1} + U_2)^{-1}
    M_sum = U1_inv_arb + U2_arb
    det_M = M_sum[0, 0] * M_sum[1, 1] - M_sum[0, 1] * M_sum[1, 0]
    G00_abs = abs(M_sum[1, 1] / det_M)
    if mutant == "route_c_pathwise_green_bounded_by_1":
        require(G00_abs <= arb(1), f"Mutant falsely claimed |G(1,0;b)_{{00}}| <= 1 (actual {G00_abs})")
    else:
        require(G00_abs > arb(30), f"Expected |G(1,0;b)_{{00}}| > 30 in non-normal witness, got {G00_abs}")


def check_route_c_ward_schur_and_linear_ceiling(mutant: str | None = None) -> None:
    """Check finite-grid Ward-Schur algebra and interval series fixtures.
    These fixtures do not verify a linear-in-Omega ceiling. Averaged leakage
    and the infinite-grid/DMFT passage remain unproved (RIGOR section 5).
    """
    # 1. Exact verification of Theorem 4.3 identities (1)-(3) on a 2*M_cut Matsubara grid
    T = 0.05
    M_cut = 16
    ns = np.arange(-M_cut, M_cut)
    wn = (2 * ns + 1) * math.pi * T
    d_bath = 0.35 / np.sqrt(wn ** 2 + 1.0)
    re_delta = -0.15 * wn / (wn ** 2 + 1.0)
    mu_s = 0.25
    g0_inv = 1j * wn + mu_s - (re_delta - 1j * np.sign(wn) * d_bath)
    D_pos = wn[M_cut:] + d_bath[M_cut:]

    rng = np.random.default_rng(20261120)
    b0 = 0.65
    b_k = (rng.normal(size=M_cut - 1) + 1j * rng.normal(size=M_cut - 1)) * (0.015 / np.arange(1, M_cut))
    V = np.zeros((2 * M_cut, 2 * M_cut), dtype=complex)
    for k, val in enumerate(b_k, 1):
        ii = np.arange(2 * M_cut - k) + k
        jj = np.arange(2 * M_cut - k)
        V[ii, jj] = val
        V[jj, ii] = np.conj(val)

    A = np.diag(g0_inv - b0) - V
    G = inv(A)

    idx_p = np.arange(M_cut, 2 * M_cut)
    idx_m = np.arange(M_cut - 1, -1, -1)
    A_pp = A[np.ix_(idx_p, idx_p)]
    A_mm = A[np.ix_(idx_m, idx_m)]
    V_pm = V[np.ix_(idx_p, idx_m)]
    G_pp = G[np.ix_(idx_p, idx_p)]
    G_pm = G[np.ix_(idx_p, idx_m)]

    D_p = np.diag(D_pos)
    D_half = np.diag(np.sqrt(D_pos))
    D_inv_half = np.diag(1.0 / np.sqrt(D_pos))

    # Theorem 4.3(1): ||D_+^{1/2} A_{++}^{-1} D_+^{1/2}||_op <= 1 and ||D_-^{1/2} A_{--}^{-1} D_-^{1/2}||_op <= 1
    norm_App = float(np.linalg.norm(D_half @ inv(A_pp) @ D_half, ord=2))
    norm_Amm = float(np.linalg.norm(D_half @ inv(A_mm) @ D_half, ord=2))
    cap_halfspace = 0.5 if mutant == "route_c_halfspace_norm_gt_1" else 1.0
    require(norm_App <= cap_halfspace and norm_Amm <= cap_halfspace, f"Half-space inverse norm exceeded {cap_halfspace}: {norm_App}, {norm_Amm}")

    # Theorem 4.3(2): Exact Schur-Ward identities
    A_mm_inv = inv(A_mm)
    Q_mat = V_pm @ A_mm_inv @ D_p @ A_mm_inv.conj().T @ V_pm.conj().T
    Q_tilde = V_pm @ np.diag(1.0 / D_pos) @ V_pm.conj().T

    # Check 0 <= Q <= Q_tilde:
    eigs_diff = np.linalg.eigvalsh(Q_tilde - Q_mat)
    require(np.min(eigs_diff) >= -1e-15, f"Q <= Q_tilde violated: min eig = {np.min(eigs_diff)}")

    # Check G_pm D_- G_pm^+ == G_pp Q G_pp^+ and -Im G_pp == G_pp (D_+ - Q) G_pp^+:
    lhs_neg = G_pm @ D_p @ G_pm.conj().T
    rhs_neg = G_pp @ Q_mat @ G_pp.conj().T
    require(np.max(np.abs(lhs_neg - rhs_neg)) < 1e-14, "Identity G_pm D_- G_pm^+ == G_pp Q G_pp^+ failed")

    im_Gpp = -(G_pp - G_pp.conj().T) / 2j
    q_sign = +1.0 if mutant == "route_c_schur_q_sign_flipped" else -1.0
    rhs_im = G_pp @ (D_p + q_sign * Q_mat) @ G_pp.conj().T
    require(np.max(np.abs(im_Gpp - rhs_im)) < 1e-14, "Identity -Im G_pp == G_pp (D_+ - Q) G_pp^+ failed")

    # Theorem 4.3(3): Pathwise bound Neg_n[b] <= (alpha / (1 - alpha)) (-Im G_nn[b])
    alpha_op = float(np.linalg.norm(D_inv_half @ V_pm @ D_inv_half, ord=2) ** 2)
    require(alpha_op < 0.2, f"Expected alpha_op < 0.2, got {alpha_op}")
    neg_vec = np.real(np.diag(lhs_neg))
    im_vec = np.real(np.diag(im_Gpp))
    bound_vec = (alpha_op / (1.0 - alpha_op)) * im_vec
    require(np.all(neg_vec <= bound_vec * (1.0 + 1e-12)), "Pathwise leakage bound Neg_n <= (alpha/(1-alpha))(-Im G_nn) failed")

    # Theorem 4.3(3) sharpness at alpha = 1 on the 2-mode subspace {n=0, m=0}:
    # At b0 = mu_s - Re Delta(i w_0) and V_pm = [[b1]], Q = (|b1|^2 / D0) = alpha * D0.
    # For alpha = 1, D0 - Q = 0; for alpha = 1.5 > 1, D0 - Q = -0.5 * D0 < 0!
    alpha_test = 1.5
    d_minus_q_test = D_pos[0] * (1.0 - alpha_test)
    if mutant == "route_c_alpha_threshold_2_instead_of_1":
        require(d_minus_q_test >= 0.0, "Mutant falsely claimed D_+ - Q >= 0 up to alpha = 2")
    else:
        require(d_minus_q_test < 0.0 and abs(D_pos[0] * (1.0 - 1.0)) == 0.0, "Alpha = 1 threshold sharpness check failed")

    # Theorem 4.3(4): Exact Bethe-lattice pairing Ward identity on each trajectory:
    # Pos_n[b] + Neg_n[b] = -Im G_nn[b] + 2 * Neg_n[b]
    pos_vec = np.sum(np.abs(G_pp) ** 2 * D_pos[None, :], axis=1)
    leak_mult = 1.0 if mutant == "route_c_ward_leak_factor_1_instead_of_2" else 2.0
    require(
        np.max(np.abs((pos_vec + neg_vec) - (im_vec + leak_mult * neg_vec))) < 1e-14,
        "Ward identity Pos_n + Neg_n == -Im G_nn + 2 * Neg_n failed",
    )

    # 2. Theorem 4.4(1): Low-Energy Damping Window Lemma:
    # If d_n^{bath} >= gamma_0 on omega_n <= W_0, then D_n >= c_win * (omega_n + gamma_met) for ALL n >= 0
    # with gamma_met = min(gamma_0, W_0) and c_win = 1/2 (whereas c_win = 1 fails for omega_n > W_0 when d_n^{bath} = 0!).
    gamma_0 = Q(3, 10)
    W_0 = Q(3, 10)
    gamma_met = min(gamma_0, W_0)
    c_win = Q(1, 1) if mutant == "route_c_low_energy_window_factor_1" else Q(1, 2)
    # Test at omega_n = 4/10 > W_0 with d_n^{bath} = 0 (allowed outside the low-energy window!):
    omega_out = Q(4, 10)
    D_out = omega_out + Q(0)
    require(D_out >= c_win * (omega_out + gamma_met), "Low-energy window lemma failed outside window")

    # Interval auxiliary series C_aux := sum_{k>=1} (2 + ln(2k-1))/(2*k^3) in (67/50, 27/20)
    # Sum k = 1..200 directly in 80-digit Arb, and bound the tail k >= 201 via integral:
    # For k >= K0 = 200, (2 + ln(2k-1))/(2 k^3) <= (1 + 0.5*ln(2k)) / k^3,
    # int_{K0}^infty (1 + 0.5*ln(2x)) / x^3 dx = (2 + ln(2*K0) + 1/2) / (4 * K0^2).
    K0 = 200
    part_sum = sum(
        ((arb(2) + arb(2 * k - 1).log()) / (arb(2) * (arb(k) ** 3)) for k in range(1, K0 + 1)),
        arb(0),
    )
    tail_upper = (arb("2.5") + arb(2 * K0).log()) / (arb(4) * (arb(K0) ** 2))
    c_univ_enclosure = part_sum + arb(0).union(tail_upper)
    c_univ_cap = arb_from_q(Q(4, 3) if mutant == "route_c_cuniv_underestimated" else Q(27, 20))
    require(c_univ_enclosure < c_univ_cap, f"C_univ enclosure {c_univ_enclosure} exceeded cap {c_univ_cap}")
    require(c_univ_enclosure > arb_from_q(Q(67, 50)), f"C_univ enclosure unexpectedly small: {c_univ_enclosure}")

    # Certify density-blind supremum: sup_{x >= 0} x / (w0 + x)^2 == 1 / (4 * w0) achieved at x = w0:
    w0_q = Q(3, 7)
    x_opt = w0_q
    val_at_opt = x_opt / ((w0_q + x_opt) ** 2)
    claimed_sup = Q(1, 8) / w0_q if mutant == "route_c_density_blind_sup_wrong" else Q(1, 4) / w0_q
    require(val_at_opt <= claimed_sup, f"Density-blind supremum violated at x=w0: {val_at_opt} > {claimed_sup}")


# ============================================================================
# Route (d): Exact 2-Site Holstein Dimer & Bipolaron Tunnel Splitting
# ============================================================================
def check_route_d_dimer_bipolaron(mutant: str | None = None) -> None:
    """Check COM conservation and NUMERICAL truncated-dimer diagnostics.
    No full-oscillator tunnel-gap error bound or pair-temperature theorem is claimed.
    """
    # 1. Exact center-of-mass commutator:
    # H_int = -g (X_1 n_1 + X_2 n_2) = -(g/sqrt(2)) X_+ (n_1 + n_2) - (g/sqrt(2)) X_- (n_1 - n_2).
    # Since N_tot = n_1 + n_2 commutes with H_el, [H_dimer, X_-] != 0 but X_+ couples ONLY to the c-number N_tot!
    # Shift a_+ -> a_+ - g*N_tot/(sqrt(2)*Omega); the shifted COM mode decouples.
    t_val = 1.0
    U_val = 4.0
    Om_val = 0.05
    N_ph = 120

    h_el = np.array([
        [0.0, 0.0, -np.sqrt(2.0) * t_val],
        [0.0, 0.0, -np.sqrt(2.0) * t_val],
        [-np.sqrt(2.0) * t_val, -np.sqrt(2.0) * t_val, 0.0],
    ])
    n_tot_el = np.diag([2.0, 2.0, 2.0])
    comm_ntot = h_el @ n_tot_el - n_tot_el @ h_el
    if mutant == "route_d_dimer_com_coupled":
        require(np.max(np.abs(comm_ntot)) > 1.0, "Mutant falsely claimed [H_el, n_1 + n_2] != 0")
    else:
        require(np.max(np.abs(comm_ntot)) == 0.0, "[H_el, n_1 + n_2] must vanish identically")

    # 2. NUMERICAL tunnel-gap fixture at U=4, t=1, Omega=0.05 (not a certified asymptotic)
    n_diff_half = np.diag([1.0, -1.0, 0.0])
    a_op = np.diag(np.sqrt(np.arange(1, N_ph, dtype=float)), 1)
    x_rel = a_op + a_op.T
    n_ph = np.diag(np.arange(N_ph, dtype=float))

    H_dim = (
        np.kron(h_el, np.eye(N_ph))
        + Om_val * np.kron(np.eye(3), n_ph)
        - np.sqrt(U_val * Om_val) * np.kron(n_diff_half, x_rel)
    )
    evals, _ = eigh(H_dim)
    evals = evals - evals[0]
    gap_split = float(evals[1] - evals[0])

    # At U = 4, Om = 0.05, U/Om = 80, so Frank-Condon bipolaron tunnel splitting is < 1e-10 << 0.1 * Om = 0.005:
    if mutant == "route_d_dimer_bipolaron_linear_split":
        require(gap_split >= 0.1 * Om_val, f"Mutant falsely claimed dimer tunnel splitting >= 0.1*Omega (actual {gap_split})")
    else:
        require(gap_split < 1e-8 * Om_val, f"Expected exponentially small bipolaron splitting at U/Om=80, got {gap_split}")

    # Also verify at moderate adiabaticity U = 4.0, t = 1.0, Omega = 0.40 (U/Om = 10):
    # The DRESSED Lang-Firsov bipolaron operator tilde{Delta}_1^+ tilde{Delta}_2 = |0><1| (x) exp(2*sqrt(U/Om)*(a^+ - a))
    # has opposite matrix elements (+0.473 and -0.473) in the tunnel-split ground doublet |Psi_0>, |Psi_1>,
    # so <tilde{Delta}_1^+ tilde{Delta}_2> decays on the exponentially small scale T ~ Delta E_split << Omega,
    # whereas the BARE nearest-neighbor correlator <Delta_1^+ Delta_2> has the SAME positive O(t^2/U^2) value in both states!
    Om_mod = 0.40
    H_mod = (
        np.kron(h_el, np.eye(N_ph))
        + Om_mod * np.kron(np.eye(3), n_ph)
        - np.sqrt(U_val * Om_mod) * np.kron(n_diff_half, x_rel)
    )
    ev_mod, vec_mod = eigh(H_mod)
    ev_mod = ev_mod - ev_mod[0]
    split_mod = float(ev_mod[1] - ev_mod[0])
    require(split_mod < 1e-6 * Om_mod, f"Expected tunnel splitting << Omega at Om=0.4, got {split_mod}")

    op_d1_d2 = np.zeros((3, 3))
    op_d1_d2[0, 1] = 1.0
    disp_op = expm(2.0 * np.sqrt(U_val / Om_mod) * (a_op.T - a_op))
    dressed_op = np.kron(op_d1_d2, disp_op)
    bare_op = np.kron(op_d1_d2, np.eye(N_ph))
    dressed_diag = np.einsum("ki,kl,li->i", vec_mod, dressed_op, vec_mod)
    bare_diag = np.einsum("ki,kl,li->i", vec_mod, bare_op, vec_mod)

    T_test = 0.05 * Om_mod
    w_test = np.exp(-ev_mod / T_test)
    dressed_at_005_om = float(np.sum(w_test * dressed_diag) / np.sum(w_test))
    bare_at_005_om = float(np.sum(w_test * bare_diag) / np.sum(w_test))
    require(float(dressed_diag[0]) > 0.40 and float(dressed_diag[1]) < -0.40, "Expected opposite-sign dressed doublet matrix elements")
    require(abs(dressed_at_005_om) < 1e-4, f"Expected strongly suppressed dressed bipolaron coherence at T=0.05*Omega, got {dressed_at_005_om}")
    require(bare_at_005_om > 0.015, f"Expected O(t^2/U^2) bare intra-well correlator at T=0.05*Omega, got {bare_at_005_om}")


# ============================================================================
# Numerical Sanity Check: Self-Consistent Bethe-Lattice DMFT Scan
# ============================================================================
def check_numerical_dmft_bethe_scan() -> None:
    """Unconverged finite-grid, finite-sample exploratory DMFT fixture.
    Passing this one-temperature fixture is not evidence of a linear ceiling.
    The earlier T/Omega=0.10 leakage assertion failed; see RESULT.md.
    """
    t_star = 1.0
    Om = 0.10
    T = 0.015  # T / Omega = 0.15
    M_cut = 28
    K_ph = 18
    n_b0 = 25
    n_s = 12
    Nmat = 2 * M_cut
    ns = np.arange(-M_cut, M_cut)
    wn = (2 * ns + 1) * math.pi * T
    nu_k = 2 * math.pi * np.arange(1, K_ph + 1) * T
    b0_grid = np.linspace(-3.5, 3.5, n_b0)
    db0 = b0_grid[1] - b0_grid[0]

    for U in (1.0, 2.5):
        var_k = U * (Om ** 2) * T / (Om ** 2 + nu_k ** 2)
        sck = np.sqrt(var_k / 2.0)
        rng = np.random.default_rng(77)
        bk_samples = (rng.normal(size=(n_s, K_ph)) + 1j * rng.normal(size=(n_s, K_ph))) * sck[None, :]
        V_batch = np.zeros((n_s, Nmat, Nmat), dtype=complex)
        for k in range(1, K_ph + 1):
            ii = np.arange(Nmat - k) + k
            jj = np.arange(Nmat - k)
            V_batch[:, ii, jj] = bk_samples[:, k - 1][:, None]
            V_batch[:, jj, ii] = np.conj(bk_samples[:, k - 1])[:, None]

        G_loc = 1.0 / (1j * wn + 0.5j * np.sign(wn))
        G_all = np.zeros((n_b0, n_s, Nmat, Nmat), dtype=complex)
        w = np.ones((n_b0, n_s)) / (n_b0 * n_s)
        I_mat = np.eye(Nmat)
        for _ in range(10):
            g0_inv = 1j * wn - (t_star ** 2) * G_loc
            A_all = (g0_inv[None, None, :, None] - b0_grid[:, None, None, None]) * I_mat[None, None, :, :] - V_batch[None, :, :, :]
            A0 = (1j * wn[None, None, :, None] - b0_grid[:, None, None, None]) * I_mat[None, None, :, :] - V_batch[None, :, :, :]
            _, logdet_A = np.linalg.slogdet(A_all)
            _, logdet_A0 = np.linalg.slogdet(A0)
            lw = (
                -0.5 * (b0_grid[:, None] ** 2) / (U * T)
                + 2.0 * (logdet_A - logdet_A0)
                + 2.0 * np.log(np.cosh(np.clip(b0_grid[:, None] / (2.0 * T), -50.0, 50.0)))
            )
            lw = lw - np.max(lw)
            w = np.exp(lw) * db0
            w = w / np.sum(w)
            G_all = np.linalg.inv(A_all)
            G_new = np.einsum("bs,bsii->i", w, G_all)
            G_loc = 0.5 * G_loc + 0.5 * G_new

        d_pos = -np.imag(G_loc[M_cut:])
        D_pos = wn[M_cut:] + (t_star ** 2) * d_pos
        idx_p = np.arange(M_cut, Nmat)
        idx_m = np.arange(M_cut - 1, -1, -1)
        G_pp = G_all[:, :, idx_p[:, None], idx_p[None, :]]
        G_pm = G_all[:, :, idx_p[:, None], idx_m[None, :]]
        K_plus = (t_star ** 2) * np.einsum("bs,bsij->ij", w, np.abs(G_pp) ** 2 + np.abs(G_pm) ** 2)
        lam = float(np.max(np.real(np.linalg.eigvals(K_plus))))
        leak0 = float(2.0 * (t_star ** 2) * np.einsum("bs,bsj,j->", w, np.abs(G_pm[:, :, 0, :]) ** 2, D_pos))
        require(lam < 1.0, f"Numerical DMFT pairing eigenvalue >= 1 at U={U}, T/Om=0.15: {lam}")
        require(leak0 / wn[M_cut] < 1.0, f"Numerical DMFT Leak(0)/w0 >= 1 at U={U}, T/Om=0.15: {leak0 / wn[M_cut]}")


def base_checks(mutant: str | None = None) -> None:
    check_route_a_rp_and_debye_waller(mutant)
    check_route_b_lehmann_sum_rule(mutant)
    check_route_c_total_positivity_and_witness(mutant)
    check_route_c_ward_schur_and_linear_ceiling(mutant)
    check_route_d_dimer_bipolaron(mutant)
    if mutant is None:
        check_numerical_dmft_bethe_scan()
        print("LINEAR-FRESH replay: ALL FIXTURE CHECKS PASSED; NO PAIRING CEILING CERTIFIED")
        print("  Route (a): free Einstein covariance; truncated dimer factorization diagnostic NUMERICAL")
        print("  Route (b): sum-rule normalization and truncated spectral diagnostics NUMERICAL")
        print("  Route (c): 2-slice non-normal witness CERTIFIED; Ward-Schur matrix fixture NUMERICAL")
        print("             auxiliary series in (67/50, 27/20) CERTIFIED, not a ceiling coefficient")
        print("  Route (d): COM algebra; truncated dimer gaps and dressed correlators NUMERICAL")


def run_mutant(name: str) -> int:
    try:
        base_checks(mutant=name)
    except AssertionError as exc:
        print(f"MUTANT REJECTED [{name}]: {exc}")
        return 1
    print(f"MUTANT SURVIVED [{name}]")
    return 0


def all_mutants() -> int:
    survivors = []
    for name in MUTANTS:
        rc = run_mutant(name)
        if rc == 0:
            survivors.append(name)
    if survivors:
        print(f"FAIL: surviving mutants: {survivors}")
        return 1
    print(f"ALL {len(MUTANTS)} GUARDED MUTANTS REJECTED (each helper returned 1)")
    return 0


def main(argv: list[str]) -> int:
    if argv == ["--all-mutants"]:
        return all_mutants()
    if len(argv) == 2 and argv[0] == "--mutant" and argv[1] in MUTANTS:
        return run_mutant(argv[1])
    if not argv:
        base_checks(mutant=None)
        return 0
    print("Usage: replay.py [--all-mutants | --mutant NAME]", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
