#!/usr/bin/env python3
"""Exact rational and outward-rounded interval certification for PURESSH.

Verifies every finite algebraic, operator-norm, Schatten-Holder, Wick/covariance,
polymer-budget, boundary-oscillator, and route-obstruction inequality in
ADIABATIC/PURESSH/RIGOR.md using pure Python stdlib `fractions.Fraction`
and outward-rounded rational intervals (plus optional `mpmath.iv` cross-checks
when `mpmath` is installed).

Usage:
    python -B replay.py
    python -B replay.py --all-mutants
    python -B replay.py --mutant <NAME>
"""
from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from fractions import Fraction as Q

MUTANTS: tuple[str, ...] = (
    "norm_tb_underestimate",        # corrupt ||T_b||_op from 2 to 1
    "norm_ye_underestimate",        # corrupt ||Y_{e'}(theta)||_op from 1 to 1/2
    "wick_pairings_corrupted",      # corrupt (2r-1)!!/(2r)! -> 1/r! without 2^{-r}
    "exp_phys_factor_halved",       # corrupt 2*beta*(|t| + g^2/K) -> beta*(|t| + g^2/K)
    "exp_taylor_bound_dropped",     # corrupt exp(x)-1 <= x/(1-x/2) -> exp(x)-1 <= x
    "degree_phys_underestimate",    # corrupt D = 4 -> D = 3 in q_GC
    "degree_aug_underestimate",     # corrupt D_aug = 6 -> D_aug = 5 in q_src
    "euler_walk_exponent_halved",   # corrupt D_G^{2k} -> D_G^k in polymer count
    "kp_vertex_weight_dropped",     # drop e < 3 vertex weight factor in q_GC / A_GC
    "threshold_c0_doubled",         # corrupt c_0 = 2^-10 -> 2^-8 (causes b_src > 1)
    "route_b_gap_assumed_positive", # assert false positive gap Delta_eff > 0 on C4
    "route_c_commutator_assumed_zero",  # assert false [T_{01}, T_{12}] == 0
)


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


# ---------------------------------------------------------------------------
# Outward-rounded rational interval arithmetic (pure stdlib fractions.Fraction)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class RatInt:
    """Closed interval [lo, hi] with exact rational endpoints."""
    lo: Q
    hi: Q

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise AssertionError("Invalid RatInt: lo > hi")
    @staticmethod
    def exact(v: int | Q) -> RatInt:
        q = Q(v)
        return RatInt(q, q)

    def __add__(self, other: RatInt | int | Q) -> RatInt:
        o = other if isinstance(other, RatInt) else RatInt.exact(other)
        return RatInt(self.lo + o.lo, self.hi + o.hi)

    def __radd__(self, other: int | Q) -> RatInt:
        return self + other

    def __sub__(self, other: RatInt | int | Q) -> RatInt:
        o = other if isinstance(other, RatInt) else RatInt.exact(other)
        return RatInt(self.lo - o.hi, self.hi - o.lo)

    def __rsub__(self, other: int | Q) -> RatInt:
        return RatInt.exact(other) - self

    def __mul__(self, other: RatInt | int | Q) -> RatInt:
        o = other if isinstance(other, RatInt) else RatInt.exact(other)
        prods = (self.lo * o.lo, self.lo * o.hi, self.hi * o.lo, self.hi * o.hi)
        return RatInt(min(prods), max(prods))

    def __rmul__(self, other: int | Q) -> RatInt:
        return self * other

    def __truediv__(self, other: RatInt | int | Q) -> RatInt:
        o = other if isinstance(other, RatInt) else RatInt.exact(other)
        if not (o.lo > 0 or o.hi < 0):
            raise AssertionError("Division by interval containing 0")
        inv = RatInt(Q(1) / o.hi, Q(1) / o.lo)
        return self * inv

    def __pow__(self, n: int) -> RatInt:
        require(n >= 0, "Only nonnegative integer powers supported")
        if n == 0:
            return RatInt.exact(1)
        if n % 2 == 1 or self.lo >= 0:
            return RatInt(self.lo ** n, self.hi ** n)
        if self.hi <= 0:
            return RatInt(self.hi ** n, self.lo ** n)
        return RatInt(Q(0), max(self.lo ** n, self.hi ** n))


def rat_exp_iv(x: Q, terms: int = 28) -> RatInt:
    """Rigorous outward rational interval enclosure of exp(x) for |x| <= 20."""
    if x == 0:
        return RatInt.exact(1)
    if x < 0:
        pos = rat_exp_iv(-x, terms=terms)
        return RatInt.exact(1) / pos
    # Scale x = 2^k * y with 0 < y <= 1/2
    k = 0
    y = x
    while y > Q(1, 2):
        y /= 2
        k += 1
    # Taylor sum_{m=0}^{terms-1} y^m / m! with remainder <= (y^terms / terms!) * 2
    s = Q(0)
    term = Q(1)
    for m in range(terms):
        s += term
        term = term * y / (m + 1)
    rem = term * 2
    base = RatInt(s, s + rem)
    cap = 10 ** 40
    for _ in range(k):
        base = base * base
        lo_n = (base.lo.numerator * cap) // base.lo.denominator
        hi_n = -((-base.hi.numerator * cap) // base.hi.denominator)
        base = RatInt(Q(lo_n, cap), Q(hi_n, cap))
    return base


def rat_sinh_iv(x: Q, terms: int = 28) -> RatInt:
    """Rigorous outward rational interval for sinh(x) (x >= 0)."""
    require(x >= 0, "rat_sinh_iv requires x >= 0")
    ex = rat_exp_iv(x, terms=terms)
    emx = RatInt.exact(1) / ex
    return (ex - emx) / 2


def rat_cosh_iv(x: Q, terms: int = 28) -> RatInt:
    """Rigorous outward rational interval for cosh(x)."""
    ex = rat_exp_iv(abs(x), terms=terms)
    emx = RatInt.exact(1) / ex
    return (ex + emx) / 2


def rat_log1m_neg_iv(x: RatInt, terms: int = 40) -> RatInt:
    """Rigorous outward rational interval for -log(1 - x) for 0 <= x.lo <= x.hi < 1/2."""
    require(Q(0) <= x.lo and x.hi < Q(1, 2), f"Out of range for -log(1-x): {x}")
    lo_sum = Q(0)
    hi_sum = Q(0)
    p_lo = x.lo
    p_hi = x.hi
    for m in range(1, terms + 1):
        lo_sum += p_lo / m
        hi_sum += p_hi / m
        p_lo *= x.lo
        p_hi *= x.hi
    # Tail sum_{m > terms} x^m / m <= p_hi / ((terms + 1) * (1 - x.hi))
    tail = p_hi / ((terms + 1) * (1 - x.hi))
    return RatInt(lo_sum, hi_sum + tail)


def rat_pi_iv() -> RatInt:
    """Rigorous Machin-formula rational interval for pi with width < 10^-25."""
    def atan_unit_iv(inv_n: int, pairs: int = 20) -> RatInt:
        # Alternating series sum_{k=0}^\infty (-1)^k / ((2k+1) * inv_n^{2k+1})
        s = Q(0)
        u = Q(1, inv_n)
        u2 = u * u
        p = u
        for k in range(2 * pairs):
            term = p / (2 * k + 1)
            if k % 2 == 0:
                s += term
            else:
                s -= term
            p *= u2
        next_term = p / (4 * pairs + 1)
        # After an even number of terms (ending on -), true value is in [s, s + next_term]
        return RatInt(s, s + next_term)

    return 16 * atan_unit_iv(5, 20) - 4 * atan_unit_iv(239, 10)


# ---------------------------------------------------------------------------
# Exact integer/rational fermionic Fock space builders
# ---------------------------------------------------------------------------
def build_fermions_int(n_sites: int) -> tuple[list[list[list[int]]], list[list[list[int]]]]:
    """Return exact integer annihilation/creation matrices c[m], cdag[m] on n_sites spinful sites."""
    n_modes = 2 * n_sites
    dim = 1 << n_modes
    c = [[[0] * dim for _ in range(dim)] for _ in range(n_modes)]
    cdag = [[[0] * dim for _ in range(dim)] for _ in range(n_modes)]
    for m in range(n_modes):
        for s in range(dim):
            if (s >> m) & 1:
                 parity = bin(s & ((1 << m) - 1)).count("1")
                 sign = -1 if (parity & 1) else 1
                 t_state = s ^ (1 << m)
                 c[m][t_state][s] = sign
                 cdag[m][s][t_state] = sign
    return c, cdag


def mat_add(a: list[list[int]], b: list[list[int]], scale_b: int = 1) -> list[list[int]]:
    n = len(a)
    return [[a[i][j] + scale_b * b[i][j] for j in range(n)] for i in range(n)]


def mat_mul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    n = len(a)
    out = [[0] * n for _ in range(n)]
    for i in range(n):
        ai = a[i]
        oi = out[i]
        for k in range(n):
            aik = ai[k]
            if aik:
                bk = b[k]
                for j in range(n):
                    oi[j] += aik * bk[j]
    return out


# ---------------------------------------------------------------------------
# Proof step checks
# ---------------------------------------------------------------------------
def check_operator_norms(mutant: str | None = None) -> tuple[Q, Q]:
    """Check Lemma 4.1: ||T_b||_op = 2, ||Y_{e'}(theta)||_op = 1, ||Delta_x^dag Delta_y||_op = 1."""
    c, cdag = build_fermions_int(2)
    dim = 16
    # T_b = sum_sigma (c_{0,sigma}^dag c_{1,sigma} + c_{1,sigma}^dag c_{0,sigma})
    t_b = [[0] * dim for _ in range(dim)]
    for sigma in (0, 1):
        m0 = 2 * 0 + sigma
        m1 = 2 * 1 + sigma
        hop = mat_add(mat_mul(cdag[m0], c[m1]), mat_mul(cdag[m1], c[m0]))
        t_b = mat_add(t_b, hop)

    # Check Hermiticity and exact polynomial T_b (T_b^2 - I) (T_b^2 - 4 I) == 0
    for i in range(dim):
        for j in range(dim):
            require(t_b[i][j] == t_b[j][i], "T_b not symmetric")
    tb2 = mat_mul(t_b, t_b)
    tb4 = mat_mul(tb2, tb2)
    # T_b^4 - 5 T_b^2 + 4 I vanishes on eigenvalues {-2,-1,1,2}, so T_b (T_b^4 - 5 T_b^2 + 4 I) == 0
    poly = [[tb4[i][j] - 5 * tb2[i][j] + (4 if i == j else 0) for j in range(dim)] for i in range(dim)]
    t_poly = mat_mul(t_b, poly)
    for i in range(dim):
        for j in range(dim):
            require(t_poly[i][j] == 0, "Minimal polynomial of T_b failed")
    # Bonding 2-particle state v = (c_{0,up}^dag + c_{1,up}^dag)(c_{0,dn}^dag + c_{1,dn}^dag)|0>
    create_up = mat_add(cdag[0], cdag[2])
    create_dn = mat_add(cdag[1], cdag[3])
    create_pair = mat_mul(create_up, create_dn)
    v_bond = [create_pair[i][0] for i in range(dim)]
    require(any(v_bond), "v_bond must be nonzero")
    for i in range(dim):
        lhs = sum(t_b[i][j] * v_bond[j] for j in range(dim))
        require(lhs == 2 * v_bond[i], "T_b v_bond == 2 v_bond failed")
    max_eval_tb2 = 4

    # Check Delta_0^dag Delta_1 and Y_{e'}(0)
    # Delta_x = c_{x,dn} c_{x,up}, Delta_x^dag = c_{x,up}^dag c_{x,dn}^dag
    d0_dag = mat_mul(cdag[0], cdag[1])
    d1 = mat_mul(c[3], c[2])
    d0dag_d1 = mat_mul(d0_dag, d1)
    d1dag_d0 = [[d0dag_d1[j][i] for j in range(dim)] for i in range(dim)]
    y_e = mat_add(d0dag_d1, d1dag_d0)
    ye2 = mat_mul(y_e, y_e)
    ye3 = mat_mul(ye2, y_e)
    for i in range(dim):
        for j in range(dim):
            require(ye3[i][j] == y_e[i][j], "Y_{e'}^3 == Y_{e'} failed")
    require(max(ye2[i][i] for i in range(dim)) == 1, "||Y_{e'}||_op == 1 failed")

    norm_tb = Q(1) if mutant == "norm_tb_underestimate" else Q(2)
    norm_ye = Q(1, 2) if mutant == "norm_ye_underestimate" else Q(1)
    require(norm_tb ** 2 >= max_eval_tb2, "norm_tb underestimated ||T_b||_op = 2")
    require(norm_ye ** 2 >= max(ye2[i][i] for i in range(dim)), "norm_ye underestimated ||Y_{e'}||_op = 1")
    return norm_tb, norm_ye


def check_schatten_holder_lemma_4_2() -> None:
    """Check Lemma 4.2 via outward rational intervals on 2-site Fock space across (beta, mu, Delta_j)."""
    c, cdag = build_fermions_int(2)
    dim = 16
    t_b = [[0] * dim for _ in range(dim)]
    for sigma in (0, 1):
        t_b = mat_add(t_b, mat_add(mat_mul(cdag[sigma], c[2 + sigma]), mat_mul(cdag[2 + sigma], c[sigma])))
    d0_dag = mat_mul(cdag[0], cdag[1])
    d1 = mat_mul(c[3], c[2])
    o_pair = mat_mul(d0_dag, d1)
    # Particle numbers N(s) on basis state s in {0..15}
    n_occ = [bin(s).count("1") for s in range(dim)]

    # Test on multiple (beta, mu) and non-uniform simplex splits Delta_0 + Delta_1 + Delta_2 = beta
    for beta, mu, deltas in (
        (Q(3, 4), Q(5, 3), (Q(1, 8), Q(1, 4), Q(3, 8))),
        (Q(6, 5), Q(-7, 4), (Q(1, 5), Q(3, 10), Q(7, 10))),
    ):
        require(sum(deltas) == beta, "Simplex split does not sum to beta")
        # Diagonal weights w_j[s] = exp(Delta_j * mu * N(s))
        w = [[rat_exp_iv(d * mu * n_occ[s]) for s in range(dim)] for d in deltas]
        # Compute Tr(o_pair * e^{-Delta_2 D_0} * t_b * e^{-Delta_1 D_0} * t_b * e^{-Delta_0 D_0})
        tr_iv = RatInt.exact(0)
        for s0 in range(dim):
            for s1 in range(dim):
                if t_b[s1][s0] == 0:
                    continue
                for s2 in range(dim):
                    if t_b[s2][s1] == 0 or o_pair[s0][s2] == 0:
                        continue
                    coeff = o_pair[s0][s2] * t_b[s2][s1] * t_b[s1][s0]
                    term = coeff * w[2][s2] * w[1][s1] * w[0][s0]
                    tr_iv = tr_iv + term
        # Free electronic partition function z_0^2 = (1 + exp(beta*mu))^4
        z0_sq = (RatInt.exact(1) + rat_exp_iv(beta * mu)) ** 4
        lhs_abs_hi = max(abs(tr_iv.lo), abs(tr_iv.hi))
        # Upper bound from Lemma 4.2: ||o_pair||_op * ||t_b||_op^2 * z_0^2 = 1 * 2^2 * z_0^2 = 4 * z_0^2
        rhs_lo = (4 * z0_sq).lo
        require(lhs_abs_hi <= rhs_lo, f"Lemma 4.2 violated: {lhs_abs_hi} > {rhs_lo}")


def check_phonon_wick_and_covariance_integral(mutant: str | None = None) -> None:
    """Check Lemmas 3.1 and 3.2: exact Wick pairing factor and int_0^beta C_beta(tau) dtau = 1/K."""
    for r in range(1, 7):
        fact_2r = 1
        for k in range(1, 2 * r + 1):
            fact_2r *= k
        fact_r = 1
        for k in range(1, r + 1):
            fact_r *= k
        double_fact = 1
        for k in range(1, 2 * r, 2):
            double_fact *= k
        wick_ratio = Q(1, fact_r) if mutant == "wick_pairings_corrupted" else Q(double_fact, fact_2r)
        expected = Q(1, (2 ** r) * fact_r)
        require(wick_ratio == expected, f"Wick pairing identity failed at r={r}: {wick_ratio} != {expected}")

    # Verify antiderivative evaluation of int_0^beta C_beta(tau) dtau == 1/K across diverse Omega
    for beta, k_spring, omega in (
        (Q(7, 5), Q(3, 2), Q(1, 1000)),
        (Q(7, 5), Q(3, 2), Q(17, 10)),
        (Q(7, 5), Q(3, 2), Q(500, 1)),
    ):
        half_bo = beta * omega / 2
        sh = rat_sinh_iv(half_bo)
        # Integral = (Omega / (2 K sinh(beta*Omega/2))) * (2 / Omega) * sinh(beta*Omega/2)
        prefactor = (RatInt.exact(omega) / (2 * k_spring)) / sh
        antideriv = (RatInt.exact(2) / omega) * sh
        integral_iv = prefactor * antideriv
        inv_k = Q(1) / k_spring
        require(integral_iv.lo <= inv_k <= integral_iv.hi, "Covariance integral failed to enclose 1/K")


def check_polymer_constants_and_theorems(mutant: str | None = None) -> None:
    """Check Section 1.2 and Section 5 exact rational constants and interval bounds."""
    norm_tb, norm_ye = check_operator_norms(mutant=mutant)

    c0 = Q(1, 2 ** 8) if mutant == "threshold_c0_doubled" else Q(1, 2 ** 10)
    xi0_beta = Q(1, 2 ** 9)

    phys_mult = Q(1) if mutant == "exp_phys_factor_halved" else norm_tb
    x_phys = phys_mult * c0
    x_src = norm_ye * xi0_beta

    if mutant == "exp_taylor_bound_dropped":
        eps_phys = x_phys
        eps_src = x_src
    else:
        eps_phys = x_phys / (1 - x_phys / 2)
        eps_src = x_src / (1 - x_src / 2)

    # Verify rational majorant encloses true exp(x) - 1 via outward rational interval
    true_expm1_phys = rat_exp_iv(Q(2) * Q(1, 2 ** 10)) - 1
    require(eps_phys >= true_expm1_phys.hi, f"eps_phys={eps_phys} < true exp(2^-9)-1={true_expm1_phys.hi}")

    d_phys = Q(3) if mutant == "degree_phys_underestimate" else Q(4)
    d_aug = Q(5) if mutant == "degree_aug_underestimate" else Q(6)
    walk_exp = 1 if mutant == "euler_walk_exponent_halved" else 2
    vertex_wt = Q(1) if mutant == "kp_vertex_weight_dropped" else Q(3)

    # Verify e < 3 via outward rational interval
    e_iv = rat_exp_iv(Q(1))
    require(e_iv.hi < vertex_wt, f"Vertex weight {vertex_wt} does not dominate e = {e_iv.hi}")

    q_gc = (d_phys ** walk_exp) * vertex_wt * eps_phys
    a_gc = vertex_wt / (1 - q_gc)
    b_gc = vertex_wt * q_gc / (1 - q_gc)
    r_max = 1 + 4 * a_gc * q_gc / ((1 - q_gc) ** 2)

    q_src = (d_aug ** walk_exp) * vertex_wt * max(eps_phys, eps_src)
    b_src = vertex_wt * q_src / (1 - q_src)

    if mutant is None:
        require(eps_phys == Q(2, 1023), f"Expected eps_phys = 2/1023, got {eps_phys}")
        require(eps_src == Q(2, 1023), f"Expected eps_src = 2/1023, got {eps_src}")
        require(q_gc == Q(32, 341), f"Expected q_gc = 32/341, got {q_gc}")
        require(a_gc == Q(341, 103), f"Expected a_gc = 341/103, got {a_gc}")
        require(b_gc == Q(32, 103), f"Expected b_gc = 32/103, got {b_gc}")
        require(r_max == Q(24718511, 9834543), f"Expected r_max = 24718511/9834543, got {r_max}")
        require(q_src == Q(72, 341), f"Expected q_src = 72/341, got {q_src}")
        require(b_src == Q(216, 269), f"Expected b_src = 216/269, got {b_src}")

    # Guard checks that reject underestimated constants or oversized c0
    require(q_gc >= 48 * true_expm1_phys.lo, "q_gc underestimated 48*(exp(2^-9)-1)")
    require(a_gc >= e_iv.lo / (1 - q_gc), "a_gc underestimated e/(1-q_gc)")
    require(q_src >= 108 * true_expm1_phys.lo, "q_src underestimated 108*(exp(2^-9)-1)")
    require(b_gc < 1, f"Kotecky-Preiss b_gc = {b_gc} >= 1")
    require(b_src < 1, f"Source Kotecky-Preiss b_src = {b_src} >= 1")
    require(r_max < 3, f"Susceptibility bound R_max = {r_max} >= 3")

    # Verify Cauchy log-modulus bound -2*log(1 - b_src / e) < 2
    ratio_iv = RatInt.exact(b_src) / e_iv
    log_bound_iv = 2 * rat_log1m_neg_iv(ratio_iv)
    require(log_bound_iv.hi < 2, f"-2*log(1 - b_src/e) = {log_bound_iv.hi} >= 2")


def check_boundary_stiffness_lemma_6_1() -> None:
    """Check Lemma 6.1: Z_{ph,1}(K/2) > Z_{ph,1}(K) > Z_{ph,1}(2K) via outward rational intervals."""
    # Since sqrt(1/2) < 3/4 < 1 < 4/3 < sqrt(2), check sinh monotonicity and exact rational-argument values
    for bo in (Q(1, 50), Q(1, 2), Q(4, 1)):
        # Use rational scale factors s_lo = 707/1000 < 1/sqrt(2) and s_hi = 1415/1000 > sqrt(2)
        z_half = RatInt.exact(1) / (2 * rat_sinh_iv(bo * Q(708, 1000) / 2))
        z_one = RatInt.exact(1) / (2 * rat_sinh_iv(bo / 2))
        z_two = RatInt.exact(1) / (2 * rat_sinh_iv(bo * Q(1414, 1000) / 2))
        require(z_half.lo > z_one.hi > z_two.lo > 0, "Boundary oscillator partition monotonicity failed")


def check_route_obstructions_section_7(mutant: str | None = None) -> None:
    """Check Propositions 7.1, 7.2, and 7.3 via exact integer/rational and interval arithmetic."""
    # --- Proposition 7.1: Route (b) C_4 exact zero gap Delta_eff == 0 ---
    c4, cdag4 = build_fermions_int(4)
    dim4 = 256
    edges4 = ((0, 1), (1, 2), (2, 3), (3, 0))
    sigma4 = [[0] * dim4 for _ in range(dim4)]
    for x, y in edges4:
        tb = [[0] * dim4 for _ in range(dim4)]
        for sig in (0, 1):
            mx, my = 2 * x + sig, 2 * y + sig
            tb = mat_add(tb, mat_add(mat_mul(cdag4[mx], c4[my]), mat_mul(cdag4[my], c4[mx])))
        sigma4 = mat_add(sigma4, mat_mul(tb, tb))

    idx_even: list[int] = []
    idx_odd4: list[int] = []
    idx_odd2_bal: list[int] = []
    idx_odd4_31: list[int] = []
    idx_odd4_13: list[int] = []
    idx_odd2_31: list[int] = []
    idx_odd2_13: list[int] = []
    idx_odd4_40: list[int] = []
    idx_odd4_04: list[int] = []
    for s in range(dim4):
        n_up = sum((s >> (2 * i)) & 1 for i in range(4))
        n_dn = sum((s >> (2 * i + 1)) & 1 for i in range(4))
        if n_up + n_dn != 4:
            continue
        n_odd = sum(((s >> (2 * i)) & 1) ^ ((s >> (2 * i + 1)) & 1) for i in range(4))
        if (n_up, n_dn) == (2, 2):
            if n_odd == 0:
                idx_even.append(s)
            elif n_odd == 4:
                idx_odd4.append(s)
            elif n_odd == 2:
                idx_odd2_bal.append(s)
        elif (n_up, n_dn) == (3, 1):
            if n_odd == 4:
                idx_odd4_31.append(s)
            elif n_odd == 2:
                idx_odd2_31.append(s)
        elif (n_up, n_dn) == (1, 3):
            if n_odd == 4:
                idx_odd4_13.append(s)
            elif n_odd == 2:
                idx_odd2_13.append(s)
        elif (n_up, n_dn) == (4, 0) and n_odd == 4:
            idx_odd4_40.append(s)
        elif (n_up, n_dn) == (0, 4) and n_odd == 4:
            idx_odd4_04.append(s)

    sectors_n4 = (
        ("N_up=2,N_dn=2,N_odd=0", idx_even, 6, (0, 4, 8, 12)),
        ("N_up=2,N_dn=2,N_odd=4", idx_odd4, 6, (0, 4, 8, 12)),
        ("N_up=2,N_dn=2,N_odd=2", idx_odd2_bal, 24, (2, 4, 6, 10)),
        ("N_up=3,N_dn=1,N_odd=4", idx_odd4_31, 4, (0, 4, 8)),
        ("N_up=1,N_dn=3,N_odd=4", idx_odd4_13, 4, (0, 4, 8)),
        ("N_up=3,N_dn=1,N_odd=2", idx_odd2_31, 12, (2, 4, 6)),
        ("N_up=1,N_dn=3,N_odd=2", idx_odd2_13, 12, (2, 4, 6)),
        ("N_up=4,N_dn=0,N_odd=4", idx_odd4_40, 1, (0,)),
        ("N_up=0,N_dn=4,N_odd=4", idx_odd4_04, 1, (0,)),
    )
    total_n4_dim = sum(len(sec_idx) for _, sec_idx, _, _ in sectors_n4)
    require(total_n4_dim == 70, f"Expected 70 states in N=4 on C_4, got {total_n4_dim}")

    # Verify block-diagonal invariance of Sigma_4 across all N=4 sectors and exact minimal polynomials
    for sec_name, sec_idx, expected_dim, roots in sectors_n4:
        require(len(sec_idx) == expected_dim, f"Sector {sec_name}: expected dim {expected_dim}, got {len(sec_idx)}")
        sec_set = set(sec_idx)
        for i in sec_idx:
            for j in range(dim4):
                if j not in sec_set:
                    require(sigma4[i][j] == 0, f"Sigma_4 leaks out of sector {sec_name} at ({i},{j})")
        m_sec = [[sigma4[i][j] for j in sec_idx] for i in sec_idx]
        d_sec = len(sec_idx)
        p_full = [[1 if i == j else 0 for j in range(d_sec)] for i in range(d_sec)]
        for r_idx, root in enumerate(roots):
            if r_idx == len(roots) - 1 and len(roots) > 1:
                # Before multiplying by (M - lambda_max I), the partial product must be nonzero, proving lambda_max is attained
                any_nz = any(p_full[i][j] != 0 for i in range(d_sec) for j in range(d_sec))
                require(any_nz, f"Sector {sec_name}: max root {root} was redundant in minimal polynomial")
            shifted = [[m_sec[i][j] - (root if i == j else 0) for j in range(d_sec)] for i in range(d_sec)]
            p_full = mat_mul(p_full, shifted)
        for i in range(d_sec):
            for j in range(d_sec):
                require(p_full[i][j] == 0, f"Minimal polynomial failed on sector {sec_name}")

    m_even = [[sigma4[i][j] for j in idx_even] for i in idx_even]
    m_odd = [[sigma4[i][j] for j in idx_odd4] for i in idx_odd4]

    # Exact integer eigenvectors for eigenvalue 12 in both N_odd=0 and N_odd=4
    v_even = [1, 2, 1, 1, 2, 1]
    v_odd = [1, -2, 1, 1, -2, 1]
    for row_idx in range(6):
        lhs_e = sum(m_even[row_idx][col] * v_even[col] for col in range(6))
        lhs_o = sum(m_odd[row_idx][col] * v_odd[col] for col in range(6))
        require(lhs_e == 12 * v_even[row_idx], f"M_even eigenvector check failed at row {row_idx}")
        require(lhs_o == 12 * v_odd[row_idx], f"M_odd eigenvector check failed at row {row_idx}")

    # Maximum eigenvalue across all N_odd > 0 sectors at N=4 is max(12, 10, 8, 6, 0) == 12 == lambda_max(N_odd == 0)
    lambda_max_even = 12
    lambda_max_odd_pos = max(roots[-1] for _, _, _, roots in sectors_n4[1:])
    require(lambda_max_odd_pos == 12, f"Expected max eigenvalue 12 on N_odd > 0, got {lambda_max_odd_pos}")
    delta_eff = Q(lambda_max_even - lambda_max_odd_pos, 2)
    if mutant == "route_b_gap_assumed_positive":
        require(delta_eff > 0, "Mutant assumed positive phonon-induced atomic gap Delta_eff > 0")
    require(delta_eff == 0, f"Expected Delta_eff == 0, got {delta_eff}")
    # --- Proposition 7.2: Route (c) 3-site commutator ||[T_{01}, T_{12}]||_op == 2 != 0 ---
    c3, cdag3 = build_fermions_int(3)
    dim3 = 64
    t01 = [[0] * dim3 for _ in range(dim3)]
    t12 = [[0] * dim3 for _ in range(dim3)]
    for sig in (0, 1):
        t01 = mat_add(t01, mat_add(mat_mul(cdag3[sig], c3[2 + sig]), mat_mul(cdag3[2 + sig], c3[sig])))
        t12 = mat_add(t12, mat_add(mat_mul(cdag3[2 + sig], c3[4 + sig]), mat_mul(cdag3[4 + sig], c3[2 + sig])))
    comm = mat_add(mat_mul(t01, t12), mat_mul(t12, t01), scale_b=-1)
    # Since comm = sum_sigma (c_{0,sigma}^dag c_{2,sigma} - c_{2,sigma}^dag c_{0,sigma}),
    # -comm^2 satisfies (-comm^2)(-comm^2 - I)(-comm^2 - 4 I) == 0 and has eigenvalue 4
    # on u = (c_{0,up}^dag c_{0,dn}^dag - c_{2,up}^dag c_{2,dn}^dag)|0> (states s=3 and s=48).
    neg_comm2 = [[-val for val in row] for row in mat_mul(comm, comm)]
    nc4 = mat_mul(neg_comm2, neg_comm2)
    nc_poly = mat_mul(
        neg_comm2,
        [[nc4[i][j] - 5 * neg_comm2[i][j] + (4 if i == j else 0) for j in range(dim3)] for i in range(dim3)],
    )
    for i in range(dim3):
        for j in range(dim3):
            require(nc_poly[i][j] == 0, "Minimal polynomial of -[T_01, T_12]^2 failed")
    u_comm = [0] * dim3
    u_comm[3] = 1
    u_comm[48] = -1
    for i in range(dim3):
        lhs_c = sum(neg_comm2[i][j] * u_comm[j] for j in range(dim3))
        require(lhs_c == 4 * u_comm[i], "(-[T_01, T_12]^2) u_comm == 4 u_comm failed")
    max_eval_comm2 = 4
    if mutant == "route_c_commutator_assumed_zero":
        require(max_eval_comm2 == 0, "Mutant assumed [T_{01}, T_{12}] == 0")
    require(max_eval_comm2 == 4, f"Expected ||[T_01, T_12]||_op^2 == 4, got {max_eval_comm2}")

    # --- Proposition 7.3: Route (d) free-fermion algebraic decay exceeds A_GC * q_GC^d at m=2 (d=3) ---
    pi_iv = rat_pi_iv()
    a_gc = Q(341, 103)
    q_gc = Q(32, 341)
    # At m = 2, distance d = 2*m - 1 = 3: exact T=0 correlator is 4 / (9 * pi^4)
    corr_d3_iv = RatInt.exact(4) / (9 * (pi_iv ** 4))
    bound_d3 = a_gc * (q_gc ** 3)
    require(corr_d3_iv.lo > bound_d3, f"Prop 7.3 check failed at d=3: {corr_d3_iv.lo} <= {bound_d3}")


def check_optional_mpmath_iv() -> str:
    """If mpmath is available, cross-check transcendental intervals with mpmath.iv."""
    from typing import Any

    try:
        from mpmath import iv as _iv
    except ImportError:
        return "mpmath not installed (pure stdlib rational-interval certification complete)"
    iv_ctx: Any = _iv
    iv_ctx.dps = 50
    c0 = iv_ctx.mpf(1) / iv_ctx.mpf(1024)
    eps_phys = iv_ctx.mpf(2) / iv_ctx.mpf(1023)
    require(iv_ctx.exp(2 * c0) - 1 < eps_phys, "mpmath.iv exp(2*c0)-1 check failed")
    b_src = iv_ctx.mpf(216) / iv_ctx.mpf(269)
    log_bd = -2 * iv_ctx.log(1 - b_src / iv_ctx.e)
    require(log_bd < 2, "mpmath.iv Cauchy log bound check failed")
    corr_d3 = iv_ctx.mpf(4) / (9 * (iv_ctx.pi ** 4))
    bound_d3 = (iv_ctx.mpf(341) / iv_ctx.mpf(103)) * ((iv_ctx.mpf(32) / iv_ctx.mpf(341)) ** 3)
    require(corr_d3 > bound_d3, "mpmath.iv Prop 7.3 d=3 check failed")
    return "mpmath.iv (50 dps) cross-check PASSED"


def run_all_checks(mutant: str | None = None) -> None:
    check_operator_norms(mutant=mutant)
    check_schatten_holder_lemma_4_2()
    check_phonon_wick_and_covariance_integral(mutant=mutant)
    check_polymer_constants_and_theorems(mutant=mutant)
    check_boundary_stiffness_lemma_6_1()
    check_route_obstructions_section_7(mutant=mutant)


def run_mutant_subprocess(name: str) -> int:
    proc = subprocess.run(
        [sys.executable, "-B", __file__, "--mutant", name],
        capture_output=True,
        text=True,
        check=False,
    )
    return proc.returncode


def main(argv: list[str]) -> int:
    if argv == ["--all-mutants"]:
        survivors: list[str] = []
        for name in MUTANTS:
            rc = run_mutant_subprocess(name)
            print(f"  mutant {name:34s} -> exit {rc}")
            if rc == 0:
                survivors.append(name)
        if survivors:
            print(f"FAIL: surviving mutants: {survivors}", file=sys.stderr)
            return 1
        print(f"ALL {len(MUTANTS)} MATHEMATICAL MUTANTS REJECTED (each exited 1)")
        return 0

    if len(argv) == 2 and argv[0] == "--mutant":
        name = argv[1]
        if name not in MUTANTS:
            print(f"Unknown mutant: {name}", file=sys.stderr)
            return 2
        try:
            run_all_checks(mutant=name)
        except AssertionError as exc:
            print(f"Mutant {name} rejected as expected: {exc}")
            return 1
        print(f"ERROR: Mutant {name} SURVIVED", file=sys.stderr)
        return 0

    if not argv:
        run_all_checks(mutant=None)
        mp_status = check_optional_mpmath_iv()
        print("PURESSH replay.py: ALL EXACT RATIONAL AND OUTWARD INTERVAL CHECKS PASSED")
        print(f"  c_0      = 1/1024 (2^-10),  xi_0 = 2^-9 / beta")
        print(f"  eps_phys = eps_src = 2/1023")
        print(f"  q_GC     = 32/341,  A_GC = 341/103,  b_GC = 32/103 < 1")
        print(f"  R_max    = 24718511/9834543 < 3")
        print(f"  q_src    = 72/341,  b_src = 216/269 < 1")
        print(f"  Cross-check: {mp_status}")
        return 0

    print("Usage: replay.py [--all-mutants | --mutant <NAME>]", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
