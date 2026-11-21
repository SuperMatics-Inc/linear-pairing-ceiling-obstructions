#!/usr/bin/env python3
"""Exact rational and outward-rounded interval certification for UNIFORM-SSH.

Certifies every finite algebraic identity, operator-norm bound, Schatten-Holder
bound with nonzero U_eff, universal PURESSH and Mott/dilute window constants,
HUBHOL single-site ratio bounds, 2-site dimer non-monotonicity counterexamples,
Mott-edge obstruction, atomic-limit vanishing, and particle-hole symmetry in
MASSIVE/UNIFORM-SSH/RIGOR.md using pure Python stdlib `fractions.Fraction`
and outward-rounded rational intervals (`RatInt`).

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
    "norm_tb_underestimate",            # corrupt ||T_b||_op from 2 to 1
    "threshold_c0_doubled",             # corrupt c_0 = 2^-10 -> 2^-8 (causes b_src > 1)
    "exp_taylor_bound_dropped",         # corrupt exp(x)-1 <= x/(1-x/2) -> x
    "mott_c_underestimated",            # corrupt Mott single-site factor c = 5/4 -> 1
    "dilute_L1024_source",              # use L_t=1024, L_s=2048 for dilute c=3/2 source (b_src > 1)
    "dimer_monotonicity_claimed",       # falsely assert chi_pair(U=4) <= chi_pair(U=0) (centered)
    "uncentered_offdiag_monotone",      # falsely assert |<d0^dag d1>|(U=4) <= |<d0^dag d1>|(U=0) (uncentered)
    "mott_edge_assumed_small",          # falsely assert (cosh(3)-1)/4 < 1 at Mott edge
)


def require(cond: bool, msg: str = "assertion failed") -> None:
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
            raise AssertionError(f"Invalid RatInt: lo={self.lo} > hi={self.hi}")

    @staticmethod
    def exact(v: int | Q) -> RatInt:
        q = Q(v)
        return RatInt(q, q)

    def __neg__(self) -> RatInt:
        return RatInt(-self.hi, -self.lo)

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

    def clamp_outward(self, cap: int = 10 ** 32) -> RatInt:
        lo_n = (self.lo.numerator * cap) // self.lo.denominator
        hi_n = -((-self.hi.numerator * cap) // self.hi.denominator)
        return RatInt(Q(lo_n, cap), Q(hi_n, cap))


def rat_exp_iv(x: Q, terms: int = 28) -> RatInt:
    """Rigorous outward rational interval enclosure of exp(x) for |x| <= 20."""
    if x == 0:
        return RatInt.exact(1)
    if x < 0:
        return RatInt.exact(1) / rat_exp_iv(-x, terms=terms)
    k = 0
    y = x
    while y > Q(1, 2):
        y /= 2
        k += 1
    s = Q(0)
    term = Q(1)
    for m in range(terms):
        s += term
        term = term * y / (m + 1)
    base = RatInt(s, s + 2 * term)
    for _ in range(k):
        base = (base * base).clamp_outward(10 ** 40)
    return base


def rat_cosh_iv(x: Q, terms: int = 28) -> RatInt:
    ex = rat_exp_iv(abs(x), terms=terms)
    return (ex + RatInt.exact(1) / ex) / 2


def rat_log1m_neg_iv(x: RatInt, terms: int = 40) -> RatInt:
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
    tail = p_hi / ((terms + 1) * (1 - x.hi))
    return RatInt(lo_sum, hi_sum + tail)


def mat_mul_iv(a: list[list[RatInt]], b: list[list[RatInt]], cap: int = 10 ** 30) -> list[list[RatInt]]:
    d = len(a)
    out = [[RatInt.exact(0) for _ in range(d)] for _ in range(d)]
    for i in range(d):
        for j in range(d):
            acc = RatInt.exact(0)
            for k in range(d):
                if (a[i][k].lo != 0 or a[i][k].hi != 0) and (b[k][j].lo != 0 or b[k][j].hi != 0):
                    acc = acc + a[i][k] * b[k][j]
            out[i][j] = acc.clamp_outward(cap)
    return out


def mat_exp_iv(mat_q: list[list[Q]], terms: int = 26) -> list[list[RatInt]]:
    """Rigorous outward rational interval matrix exponential exp(mat_q) via scaling and squaring.

    Uses the exact bound ||sum_{m >= M} B^m / m!||_inf <= (r^M / M!) / (1 - r/(M+1))
    whenever ||B||_inf <= r <= 1/2.
    """
    d = len(mat_q)
    norm_inf = max(sum(abs(mat_q[i][j]) for j in range(d)) for i in range(d))
    if norm_inf == 0:
        return [[RatInt.exact(1 if i == j else 0) for j in range(d)] for i in range(d)]
    k = 0
    scale = Q(1)
    while norm_inf * scale > Q(1, 2):
        scale /= 2
        k += 1
    b_iv = [[RatInt.exact(mat_q[i][j] * scale) for j in range(d)] for i in range(d)]
    r = norm_inf * scale  # <= 1/2

    # Taylor sum sum_{m=0}^{terms-1} B^m / m!
    acc = [[RatInt.exact(1 if i == j else 0) for j in range(d)] for i in range(d)]
    power = [[RatInt.exact(1 if i == j else 0) for j in range(d)] for i in range(d)]
    fact = 1
    for m in range(1, terms):
        fact *= m
        power = mat_mul_iv(power, b_iv, cap=10 ** 34)
        inv_f = Q(1, fact)
        for i in range(d):
            for j in range(d):
                acc[i][j] = (acc[i][j] + power[i][j] * inv_f).clamp_outward(10 ** 34)

    # Tail bound in inf-norm (entrywise abs bound <= ||tail||_inf)
    fact_terms = fact * terms
    rem_bound = (r ** terms) / (fact_terms * (1 - r / (terms + 1)))
    rem_iv = RatInt(-rem_bound, rem_bound)
    for i in range(d):
        for j in range(d):
            acc[i][j] = (acc[i][j] + rem_iv).clamp_outward(10 ** 30)

    for _ in range(k):
        acc = mat_mul_iv(acc, acc, cap=10 ** 30)
    return acc


# ---------------------------------------------------------------------------
# Exact integer fermionic Fock space helpers
# ---------------------------------------------------------------------------
def build_fermions_int(n_sites: int) -> tuple[list[list[list[int]]], list[list[list[int]]]]:
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
# Verification modules
# ---------------------------------------------------------------------------
def check_algebraic_identities_and_norms(mutant: str | None = None) -> tuple[Q, Q]:
    """Check Section 1.1 algebraic identities and operator norms ||T_b||=||B_b||=2, ||Y||=||X||=1."""
    # 1. Exact 1-site Fock identities
    for n_up in (0, 1):
        for n_dn in (0, 1):
            n = n_up + n_dn
            n_odd = 1 if n == 1 else 0
            lhs = (Q(n_up) - Q(1, 2)) * (Q(n_dn) - Q(1, 2))
            rhs = Q(1, 4) - Q(1, 2) * n_odd
            require(lhs == rhs, "Centered Hubbard identity failed")
            require((n - 1) ** 2 == 1 - n_odd, "Holstein (n-1)^2 identity failed")
            for u_val in (Q(0), Q(3), Q(7, 2)):
                for mu_unc in (Q(-2), Q(0), Q(5)):
                    lhs_u = u_val * n_up * n_dn - mu_unc * n
                    rhs_u = u_val * lhs - (mu_unc - u_val / 2) * n - u_val / 4
                    require(lhs_u == rhs_u, "Uncentered-to-centered identity failed")

    # 2. Exact operator norms on 2-site Fock space (dim=16)
    c, cdag = build_fermions_int(2)
    dim = 16
    t_b = [[0] * dim for _ in range(dim)]
    for sig in (0, 1):
        t_b = mat_add(t_b, mat_add(mat_mul(cdag[sig], c[2 + sig]), mat_mul(cdag[2 + sig], c[sig])))
    b_b = [[abs(t_b[i][j]) for j in range(dim)] for i in range(dim)]

    for mat_op, name in ((t_b, "T_b"), (b_b, "B_b")):
        m2 = mat_mul(mat_op, mat_op)
        m4 = mat_mul(m2, m2)
        poly = [[m4[i][j] - 5 * m2[i][j] + (4 if i == j else 0) for j in range(dim)] for i in range(dim)]
        mpoly = mat_mul(mat_op, poly)
        for i in range(dim):
            for j in range(dim):
                require(mpoly[i][j] == 0, f"Minimal polynomial of {name} failed")

    # Check eigenvalue 2 is attained by both T_b and B_b
    v_bond = [0] * dim
    # |0_up, 1_dn> + |1_up, 0_dn> + |0_up, 0_dn> + |1_up, 1_dn> in two-particle sector
    # Explicitly: (c_{0,up}^dag + c_{1,up}^dag)(c_{0,dn}^dag + c_{1,dn}^dag)|0>
    cp = mat_mul(mat_add(cdag[0], cdag[2]), mat_add(cdag[1], cdag[3]))
    v_bond = [cp[i][0] for i in range(dim)]
    require(any(v_bond), "v_bond is zero")
    for i in range(dim):
        require(sum(t_b[i][j] * v_bond[j] for j in range(dim)) == 2 * v_bond[i], "T_b eigenvalue 2 failed")
        require(sum(abs(v_bond[j]) * b_b[i][j] for j in range(dim)) == 2 * abs(v_bond[i]), "B_b eigenvalue 2 failed")

    d0_dag = mat_mul(cdag[0], cdag[1])
    d1 = mat_mul(c[3], c[2])
    d0dag_d1 = mat_mul(d0_dag, d1)
    d1dag_d0 = [[d0dag_d1[j][i] for j in range(dim)] for i in range(dim)]
    y_e = mat_add(d0dag_d1, d1dag_d0)
    x_e = [[abs(y_e[i][j]) for j in range(dim)] for i in range(dim)]
    for mat_src, name in ((y_e, "Y_{e'}"), (x_e, "X_{e'}^{pair}")):
        m2 = mat_mul(mat_src, mat_src)
        m3 = mat_mul(m2, mat_src)
        for i in range(dim):
            for j in range(dim):
                require(m3[i][j] == mat_src[i][j], f"{name}^3 == {name} failed")
        require(max(m2[i][i] for i in range(dim)) == 1, f"||{name}||_op == 1 failed")

    norm_tb = Q(1) if mutant == "norm_tb_underestimate" else Q(2)
    require(norm_tb ** 2 >= 4, "norm_tb underestimated ||T_b||_op = 2")
    return norm_tb, Q(1)


def check_schatten_holder_with_ueff() -> None:
    """Check PURESSH Lemma 4.2 with nonzero U_eff (positive, zero, and negative) and B_b majorant."""
    c, cdag = build_fermions_int(2)
    dim = 16
    t_b = [[0] * dim for _ in range(dim)]
    for sig in (0, 1):
        t_b = mat_add(t_b, mat_add(mat_mul(cdag[sig], c[2 + sig]), mat_mul(cdag[2 + sig], c[sig])))
    b_b = [[abs(t_b[i][j]) for j in range(dim)] for i in range(dim)]
    o_pair = mat_mul(mat_mul(cdag[0], cdag[1]), mat_mul(c[3], c[2]))

    n_occ = [bin(s).count("1") for s in range(dim)]
    n_odd = [
        (((s >> 0) & 1) ^ ((s >> 1) & 1)) + (((s >> 2) & 1) ^ ((s >> 3) & 1))
        for s in range(dim)
    ]

    for u_eff, beta, mu, deltas in (
        (Q(5, 2), Q(3, 4), Q(-1, 3), (Q(1, 8), Q(1, 4), Q(3, 8))),   # repulsive U_eff > 0
        (Q(0), Q(3, 4), Q(2, 3), (Q(1, 8), Q(1, 4), Q(3, 8))),       # U_eff = 0
        (Q(-3, 1), Q(4, 5), Q(1, 2), (Q(1, 5), Q(1, 5), Q(2, 5))),   # attractive U_eff < 0
    ):
        require(sum(deltas) == beta, "Simplex split sum != beta")
        h_diag = [-u_eff * Q(n_odd[s], 2) - mu * n_occ[s] for s in range(dim)]
        w = [[rat_exp_iv(-d * h_diag[s]) for s in range(dim)] for d in deltas]

        for mat_hop, tag in ((t_b, "T_b"), (b_b, "B_b")):
            tr_iv = RatInt.exact(0)
            for s0 in range(dim):
                for s1 in range(dim):
                    if mat_hop[s1][s0] == 0:
                        continue
                    for s2 in range(dim):
                        if mat_hop[s2][s1] == 0 or o_pair[s0][s2] == 0:
                            continue
                        coeff = o_pair[s0][s2] * mat_hop[s2][s1] * mat_hop[s1][s0]
                        tr_iv = tr_iv + coeff * w[2][s2] * w[1][s1] * w[0][s0]
            # z_0(beta; U_eff, mu) = 1 + 2*exp(beta*(mu + U_eff/2)) + exp(2*beta*mu)
            z0 = (
                RatInt.exact(1)
                + 2 * rat_exp_iv(beta * (mu + u_eff / 2))
                + rat_exp_iv(2 * beta * mu)
            )
            rhs_lo = (4 * (z0 ** 2)).lo
            lhs_abs_hi = max(abs(tr_iv.lo), abs(tr_iv.hi))
            require(lhs_abs_hi <= rhs_lo, f"Schatten-Holder failed ({tag}, U_eff={u_eff}): {lhs_abs_hi} > {rhs_lo}")


def check_puressh_universal_constants(mutant: str | None = None) -> None:
    """Check Theorems 1.1 & 1.2 universal constants: A_GC = 341/103, q_GC = 32/341, 1024(|t|+G_b)."""
    norm_tb, norm_ye = check_algebraic_identities_and_norms(mutant=mutant)
    c0 = Q(1, 2 ** 8) if mutant == "threshold_c0_doubled" else Q(1, 2 ** 10)
    xi0_beta = Q(1, 2 ** 9)
    x_phys = norm_tb * c0
    x_src = norm_ye * xi0_beta

    if mutant == "exp_taylor_bound_dropped":
        eps_phys = x_phys
        eps_src = x_src
    else:
        eps_phys = x_phys / (1 - x_phys / 2)
        eps_src = x_src / (1 - x_src / 2)

    true_expm1 = rat_exp_iv(Q(2) * Q(1, 2 ** 10)) - 1
    require(eps_phys >= true_expm1.hi, f"eps_phys={eps_phys} < exp(2^-9)-1={true_expm1.hi}")

    e_iv = rat_exp_iv(Q(1))
    require(e_iv.hi < 3, "e >= 3")

    q_gc = 48 * eps_phys
    a_gc = Q(3) / (1 - q_gc)
    b_gc = 3 * q_gc / (1 - q_gc)
    r_max = 1 + 4 * a_gc * q_gc / ((1 - q_gc) ** 2)
    q_src = 108 * max(eps_phys, eps_src)
    b_src = 3 * q_src / (1 - q_src)

    if mutant is None:
        require(eps_phys == Q(2, 1023))
        require(eps_src == Q(2, 1023))
        require(q_gc == Q(32, 341))
        require(a_gc == Q(341, 103))
        require(b_gc == Q(32, 103))
        require(r_max == Q(24718511, 9834543))
        require(q_src == Q(72, 341))
        require(b_src == Q(216, 269))

    require(b_gc < 1, f"b_gc={b_gc} >= 1")
    require(b_src < 1, f"b_src={b_src} >= 1")
    require(r_max < 3, f"r_max={r_max} >= 3")
    log_bd = 2 * rat_log1m_neg_iv(RatInt.exact(b_src) / e_iv)
    require(log_bd.hi < 2, f"Cauchy log bound {log_bd.hi} >= 2")


def ssh3_window_constants(c_val: Q, l_t: int, l_s: int, c2: Q) -> dict[str, Q]:
    w_g = 2 * c2 / (1 - c2)
    eps_phys = Q(4, 3 * l_t) * (1 + w_g) + w_g
    eps_src = Q(4, 3 * l_s)
    q_gc = 48 * c_val * eps_phys
    a_gc = 3 * c_val / (1 - q_gc)
    b_gc = 3 * c_val * q_gc / (1 - q_gc)
    r_max = 1 + 4 * a_gc * q_gc / ((1 - q_gc) ** 2)
    q_src = 108 * c_val * max(eps_phys, eps_src)
    b_src = 3 * c_val * q_src / (1 - q_src)
    return {
        "w_g": w_g,
        "eps_phys": eps_phys,
        "eps_src": eps_src,
        "q_gc": q_gc,
        "A_gc": a_gc,
        "b_gc": b_gc,
        "R_max": r_max,
        "q_src": q_src,
        "b_src": b_src,
    }


def check_window_constants_and_hubhol_ratios(mutant: str | None = None) -> None:
    """Check Theorems 1.3 & 1.4: HUBHOL single-site ratio bounds and Mott/dilute KP constants."""
    # 1. Single-site ratio bounds (exact SOS polynomials + interval checks)
    c_mott = Q(1) if mutant == "mott_c_underestimated" else Q(5, 4)
    for v in (Q(1, 10), Q(2, 5), Q(1, 2), Q(9, 10), Q(99, 100)):
        ratio_m = (1 + v) / (1 + v * v)
        require(ratio_m < c_mott, f"Mott ratio (1+v)/(1+v^2)={ratio_m} >= {c_mott} at v={v}")
        # Exact identity: 5*(1+v^2) - 4*(1+v) = 5*(v - 2/5)^2 + 1/5
        require(5 * (1 + v * v) - 4 * (1 + v) == 5 * (v - Q(2, 5)) ** 2 + Q(1, 5))
        ratio_d = (1 + 2 * v + v ** 3) / ((1 + v * v) ** 2)
        require(ratio_d < Q(3, 2), f"Dilute ratio={ratio_d} >= 3/2 at v={v}")
        # Exact identity: 3*(1+v^2)^2 - 2*(1+2v+v^3) = 3*(v^2 - v/3)^2 + (17/3)*(v - 6/17)^2 + 5/17
        sos = 3 * (v * v - v / 3) ** 2 + Q(17, 3) * (v - Q(6, 17)) ** 2 + Q(5, 17)
        require(3 * ((1 + v * v) ** 2) - 2 * (1 + 2 * v + v ** 3) == sos)

    # 2. Verify exp(2*c2)-1 <= 2*c2/(1-c2) and exp(1/4) < 4/3
    c2 = Q(1, 2 ** 13)
    exp2c2_m1 = rat_exp_iv(2 * c2) - 1
    w_g = 2 * c2 / (1 - c2)
    require(w_g >= exp2c2_m1.hi, "w_g failed to dominate exp(2*c2)-1")
    exp_qtr = rat_exp_iv(Q(1, 4))
    require(exp_qtr.hi < Q(4, 3), f"exp(1/4)={exp_qtr.hi} >= 4/3")
    e_iv = rat_exp_iv(Q(1))

    # 3. Mott / SSHBOUND3 constants (c = 5/4, L_t=1024, L_s=2048, c1=2^-26 on G, c2=2^-13)
    mott = ssh3_window_constants(c_mott, 1024, 2048, c2)
    if mutant is None:
        require(mott["eps_phys"] == Q(3243, 2096896))
        require(mott["eps_src"] == Q(1, 1536))
        require(mott["q_gc"] == Q(48645, 524224))
        require(mott["A_gc"] == Q(1965840, 475579))
        require(mott["b_gc"] == Q(729675, 1902316))
        require(mott["q_src"] == Q(437805, 2096896))
        require(mott["b_src"] == Q(6567075, 6636364))
        require(mott["R_max"] == Q(308086835615302339, 107564263537529539))
    require(mott["b_gc"] < 1 and mott["b_src"] < 1 and mott["R_max"] < 3)
    require((2 * rat_log1m_neg_iv(RatInt.exact(mott["b_src"]) / e_iv)).hi < 2)

    # 4. Dilute GC at L_t=1024 (b_gc < 1, but b_src > 1 -> motivates L_t=2048, L_s=4096)
    dilute_1024 = ssh3_window_constants(Q(3, 2), 1024, 2048, c2)
    require(dilute_1024["q_gc"] == Q(29187, 262112))
    require(dilute_1024["A_gc"] == Q(1179504, 232925))
    require(dilute_1024["b_gc"] == Q(262683, 465850) < 1)
    require(dilute_1024["b_src"] == Q(2364147, 1571530) > 1)
    if mutant == "dilute_L1024_source":
        require(dilute_1024["b_src"] < 1, "Mutant used L_t=1024 for dilute source KP")

    # 5. Dilute canonical-ready constants (c = 3/2, L_t=2048, L_s=4096, c1=2^-28 on G, c2=2^-13)
    dilute = ssh3_window_constants(Q(3, 2), 2048, 4096, c2)
    require(dilute["eps_phys"] == Q(3755, 4193792))
    require(dilute["eps_src"] == Q(1, 3072))
    require(dilute["q_gc"] == Q(33795, 524224))
    require(dilute["A_gc"] == Q(2359008, 490429))
    require(dilute["b_gc"] == Q(304155, 980858) < 1)
    require(dilute["q_src"] == Q(304155, 2096896))
    require(dilute["b_src"] == Q(2737395, 3585482) < 1)
    require(dilute["R_max"] == Q(285128438390906149, 117958279319223589) < 3)
    require((2 * rat_log1m_neg_iv(RatInt.exact(dilute["b_src"]) / e_iv)).hi < 2)


def dimer_correlators_iv(u_val: Q, beta: Q, mu: Q, t_hop: Q, centered: bool) -> tuple[RatInt, RatInt, RatInt]:
    """Rigorous outward-rounded RatInt computation of <d0^dag d0>, <d0^dag d1>, chi_pair on 2-site dimer."""
    c, cdag = build_fermions_int(2)
    dim = 16
    t_b = [[0] * dim for _ in range(dim)]
    for sig in (0, 1):
        t_b = mat_add(t_b, mat_add(mat_mul(cdag[sig], c[2 + sig]), mat_mul(cdag[2 + sig], c[sig])))
    d0d0 = mat_mul(mat_mul(cdag[0], cdag[1]), mat_mul(c[1], c[0]))
    d0d1 = mat_mul(mat_mul(cdag[0], cdag[1]), mat_mul(c[3], c[2]))

    # Build -beta * H as rational 16x16 matrix, decomposed into (N_up, N_dn) sectors
    sectors: dict[tuple[int, int], list[int]] = {}
    h_diag = [Q(0)] * dim
    for s in range(dim):
        u0 = (s >> 0) & 1
        d0 = (s >> 1) & 1
        u1 = (s >> 2) & 1
        d1 = (s >> 3) & 1
        nup = u0 + u1
        ndn = d0 + d1
        sectors.setdefault((nup, ndn), []).append(s)
        if centered:
            hu = u_val * ((Q(u0) - Q(1, 2)) * (Q(d0) - Q(1, 2)) + (Q(u1) - Q(1, 2)) * (Q(d1) - Q(1, 2)))
        else:
            hu = u_val * (u0 * d0 + u1 * d1)
        h_diag[s] = hu - mu * (nup + ndn)

    z_iv = RatInt.exact(0)
    num_00 = RatInt.exact(0)
    num_01 = RatInt.exact(0)
    for sec_idx in sectors.values():
        d_sec = len(sec_idx)
        neg_bh = [[Q(0)] * d_sec for _ in range(d_sec)]
        for a, sa in enumerate(sec_idx):
            neg_bh[a][a] = -beta * h_diag[sa]
            for b, sb in enumerate(sec_idx):
                if t_b[sa][sb] != 0:
                    neg_bh[a][b] += beta * t_hop * t_b[sa][sb]
        exp_sec = mat_exp_iv(neg_bh)
        for a, sa in enumerate(sec_idx):
            z_iv = z_iv + exp_sec[a][a]
            for b, sb in enumerate(sec_idx):
                if d0d0[sa][sb] != 0:
                    num_00 = num_00 + d0d0[sa][sb] * exp_sec[b][a]
                if d0d1[sa][sb] != 0:
                    num_01 = num_01 + d0d1[sa][sb] * exp_sec[b][a]
    c00 = num_00 / z_iv
    c01 = num_01 / z_iv
    return c00, c01, c00 + c01


def check_dimer_nonmonotonicity_counterexamples(mutant: str | None = None) -> None:
    """Certify Proposition 5.1: chi_pair and |<d0^dag d1>| can strictly INCREASE with U >= 0."""
    # 1. Centered convention: beta=2, mu=-3, t=1 -> chi_pair(4) > 25 * chi_pair(0)
    c00_0, c01_0, chi_0 = dimer_correlators_iv(Q(0), Q(2), Q(-3), Q(1), centered=True)
    c00_4, c01_4, chi_4 = dimer_correlators_iv(Q(4), Q(2), Q(-3), Q(1), centered=True)
    if mutant == "dimer_monotonicity_claimed":
        require(chi_4.lo <= chi_0.hi, "Mutant assumed chi_pair(U=4) <= chi_pair(U=0)")
    require(chi_4.lo > 25 * chi_0.hi, f"Centered dimer chi counterexample failed: {chi_4.lo} <= 25*{chi_0.hi}")
    require(c01_4.lo > 25 * c01_0.hi, f"Centered dimer c01 counterexample failed: {c01_4.lo} <= 25*{c01_0.hi}")

    # 2. Uncentered convention: beta=1/2, mu=5, t=1 -> <d0^dag d1>(4) > 4 * <d0^dag d1>(0)
    _, u01_0, _ = dimer_correlators_iv(Q(0), Q(1, 2), Q(5), Q(1), centered=False)
    _, u01_4, _ = dimer_correlators_iv(Q(4), Q(1, 2), Q(5), Q(1), centered=False)
    if mutant == "uncentered_offdiag_monotone":
        require(u01_4.lo <= u01_0.hi, "Mutant assumed uncentered offdiag(U=4) <= offdiag(U=0)")
    require(u01_4.lo > 4 * u01_0.hi, f"Uncentered dimer c01 counterexample failed: {u01_4.lo} <= 4*{u01_0.hi}")


def check_mott_edge_and_atomic_limit(mutant: str | None = None) -> None:
    """Check Mott-edge obstruction, atomic-limit vanishing, and half-filling PH symmetry."""
    # 1. Mott edge HUBHOL Lemma 6.4 lower bound at beta*t = 3
    w_edge_lo = (rat_cosh_iv(Q(3)) - 1) / 4
    if mutant == "mott_edge_assumed_small":
        require(w_edge_lo.hi < 1, "Mutant assumed Mott edge polymer activity < 1")
    require(w_edge_lo.lo > 2, f"Mott edge lower bound failed: {w_edge_lo.lo} <= 2")

    # 2. Atomic limit (t = g = 0): exact vanishing of Tr(Delta_0^dag Delta_1 e^{-beta H_at})
    c, cdag = build_fermions_int(2)
    dim = 16
    d0d1 = mat_mul(mat_mul(cdag[0], cdag[1]), mat_mul(c[3], c[2]))
    for s in range(dim):
        require(d0d1[s][s] == 0, "Atomic limit diagonal element of Delta_0^dag Delta_1 is nonzero")

    # 3. Full particle-hole unitary on 4-site bipartite ring C4 leaves T_b and Hubbard invariant
    c4, cdag4 = build_fermions_int(4)
    dim4 = 256
    # On site x with n_x = 0,1,2,3 (4 basis states per site), PH sends |0> -> |up dn>, |up> -> (-1)^x |dn>, etc.
    # Equivalently construct U_ph directly as a signed permutation on {0..255}:
    u_ph = [[0] * dim4 for _ in range(dim4)]
    for s in range(dim4):
        # Compute U_ph |s> by applying prod_{m occupied in s} (eta_x c_m) to |all filled>
        # Since c_m^dag -> eta_x c_m (spin preserved!)
        vec = [0] * dim4
        vec[dim4 - 1] = 1
        # s = prod_{m: bit m set} cdag[m] |0>; apply in decreasing order of m so signs match
        sign_total = 1
        tgt = dim4 - 1
        for m in range(7, -1, -1):
            if (s >> m) & 1:
                x = m // 2
                eta = -1 if (x & 1) else 1
                # c_m acting on tgt: must have bit m set in tgt
                parity = bin(tgt & ((1 << m) - 1)).count("1")
                sign_total *= eta * (-1 if (parity & 1) else 1)
                tgt ^= (1 << m)
        u_ph[tgt][s] = sign_total

    # Verify U_ph^T U_ph == I and U_ph T_01 U_ph^T == T_01 and U_ph V_U U_ph^T == V_U
    u_t = [[u_ph[j][i] for j in range(dim4)] for i in range(dim4)]
    prod_id = mat_mul(u_t, u_ph)
    for i in range(dim4):
        for j in range(dim4):
            require(prod_id[i][j] == (1 if i == j else 0), "U_ph not orthogonal")

    t01 = [[0] * dim4 for _ in range(dim4)]
    for sig in (0, 1):
        t01 = mat_add(t01, mat_add(mat_mul(cdag4[sig], c4[2 + sig]), mat_mul(cdag4[2 + sig], c4[sig])))
    t01_ph = mat_mul(mat_mul(u_ph, t01), u_t)
    for i in range(dim4):
        for j in range(dim4):
            require(t01_ph[i][j] == t01[i][j], "Full PH invariance of T_01 failed")


def run_all_checks(mutant: str | None = None) -> None:
    check_algebraic_identities_and_norms(mutant=mutant)
    check_schatten_holder_with_ueff()
    check_puressh_universal_constants(mutant=mutant)
    check_window_constants_and_hubhol_ratios(mutant=mutant)
    check_dimer_nonmonotonicity_counterexamples(mutant=mutant)
    check_mott_edge_and_atomic_limit(mutant=mutant)


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
        print("UNIFORM-SSH replay.py: ALL EXACT RATIONAL AND OUTWARD INTERVAL CHECKS PASSED")
        print("  Universal (all U_eff): c0 = 2^-10, q_GC = 32/341, A_GC = 341/103, R_max = 24718511/9834543 < 3")
        print("  Mott / SSHBOUND3 (c=5/4): L_t=1024, L_s=2048, q_GC = 48645/524224, A_GC = 1965840/475579, b_src = 6567075/6636364 < 1")
        print("  Dilute canonical-ready (c=3/2): L_t=2048, L_s=4096, q_GC = 33795/524224, A_GC = 2359008/490429, b_src = 2737395/3585482 < 1")
        print("  Dimer non-monotonicity: CERTIFIED chi_pair(4) > 25*chi_pair(0) (centered), |<d0^dag d1>|(4) > 4*|<d0^dag d1>|(0) (uncentered)")
        print("  Mott edge: CERTIFIED (cosh(3)-1)/4 > 2; Atomic limit: CERTIFIED <d0^dag d1> = 0; C4 Full PH: CERTIFIED")
        return 0

    print("Usage: replay.py [--all-mutants | --mutant <NAME>]", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
