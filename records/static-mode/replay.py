"""Exact-rational constant guards and NUMERICAL sanity checks, not certification.
Run with the prescribed uv command; no random inputs or external data.
"""
import json
import math
from fractions import Fraction as Q

import mpmath as mp
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.linalg import eigh
from scipy.special import expit


def susceptibility(h, beta, nu):
    """One-spin local density susceptibility for nonzero bosonic nu."""
    energies, vectors = eigh(h)
    p = np.abs(vectors) ** 2
    delta = energies[None, :] - energies[:, None]
    f = expit(-beta * energies)
    kernel = (f[:, None] - f[None, :]) * delta / (nu * nu + delta * delta)
    return np.einsum("xa,xb,ab->x", p, p, kernel)


def first_cumulant(h, beta, omega, coupling, modes=2000):
    total = np.zeros(len(h))
    for n in range(1, modes + 1):
        nu = 2 * math.pi * n / beta
        total += 2 * coupling * omega**2 / (nu**2 + omega**2) * susceptibility(h, beta, nu)
    # Chi_x <= beta/4 and r_n <= omega^2/nu_n^2.
    tail_bound = coupling * omega**2 * beta**3 / (8 * math.pi**2 * modes)
    return total, tail_bound


def bridge(t, delta):
    w = delta / 2
    middle = -delta / 2 + 2 * t * t / delta
    return np.array([[w, -t, 0], [-t, middle, -t], [0, -t, w]], dtype=float)


def square_embedding(t, delta, barrier):
    side = 4
    h = np.diag(np.full(side * side, barrier))
    for x in range(side):
        for y in range(side):
            i = side * x + y
            for xx, yy in [((x + 1) % side, y), (x, (y + 1) % side)]:
                j = side * xx + yy
                h[i, j] = h[j, i] = -t
    sites = [0, 1, 2]
    b = bridge(t, delta)
    for k, i in enumerate(sites):
        h[i, i] = b[k, k]
    return h, sites


def determinant_ratio(h, beta, amplitude, site, n, sine):
    def rhs(u, flat):
        v = np.zeros(len(h))
        angle = 2 * math.pi * n * u / beta
        v[site] = amplitude * (math.sin(angle) if sine else math.cos(angle))
        return (-(h + np.diag(v)) @ flat.reshape(h.shape)).ravel()

    solution = solve_ivp(rhs, (0, beta), np.eye(len(h)).ravel(), method="DOP853", rtol=5e-14, atol=1e-15)
    assert solution.success, solution.message
    monodromy = solution.y[:, -1].reshape(h.shape)
    sign, logdet = np.linalg.slogdet(np.eye(len(h)) + monodromy)
    assert sign > 0  # Only this small-amplitude numerical probe, not a universal claim.
    baseline = np.logaddexp(0, -beta * eigh(h, eigvals_only=True)).sum()
    return math.exp(2 * (logdet - baseline))


def exact_constants():
    # Positive integral: int_0^1 x^4(1-x)^4/(1+x^2) dx = 22/7 - pi.
    # Polynomial division yields quotient x^6-4x^5+5x^4-4x^2+4 and remainder -4.
    quotient = [Q(4), Q(0), Q(-4), Q(0), Q(5), Q(-4), Q(1)]
    product = [Q(0)] * 9
    for k, value in enumerate(quotient):
        product[k] += value
        product[k+2] += value
    product[0] -= 4
    assert product == [Q(0), Q(0), Q(0), Q(0), Q(1), Q(-4), Q(6), Q(-4), Q(1)]
    assert sum(value / (k+1) for k, value in enumerate(quotient)) == Q(22, 7)
    assert Q(22, 7)**2 < 10
    # e^2 exceeds its degree-four Taylor sum 7, hence tanh(1)>3/4.
    assert sum(Q(2**k, math.factorial(k)) for k in range(5)) == 7
    # delta <= t gives A >= 2/3; Omega/tau<=1 bounds the two denominators.
    coefficient = Q(2, 3) * 4 * Q(3, 4) / (41 * 56)
    assert coefficient == Q(1, 1148)
    assert coefficient > Q(1, 1200)
    return {"status": "exact-rational replay, independent review pending", "coefficient_majorized_from_below": str(coefficient), "bridge_constant": "1/1200", "embedded_constant": "1/2400"}


def run():
    report = {"status": "NUMERICAL", "claims": []}
    report["exact_constants"] = exact_constants()
    mp.mp.dps = 60
    variance_rows = []
    for a in [mp.mpf("0.001"), mp.mpf("0.1"), mp.mpf("1"), mp.mpf("5")]:
        q = a / (2 * mp.tanh(a / 2)) - 1
        qsum = 2 * mp.nsum(lambda n: a*a / ((2*mp.pi*n)**2 + a*a), [1, mp.inf])
        assert abs(q - qsum) < mp.mpf("1e-45")
        assert 0 < q <= a*a/12
        variance_rows.append({"a": str(a), "q": str(q), "q_over_a2": str(q/(a*a))})
    report["variance"] = variance_rows

    # An independent time-domain Kubo integral checks susceptibility and sign.
    h = np.array([[0.2, -0.7], [-0.7, -0.3]])
    beta, omega, coupling = 2.0, 0.3, 1.1
    energies, vectors = eigh(h)
    p = np.abs(vectors) ** 2
    f = expit(-beta * energies)
    nu = 2 * math.pi / beta
    matsubara = susceptibility(h, beta, nu)
    time_values = []
    for x in range(2):
        def integrand(u):
            k = sum(p[x, a] * p[x, b] * f[a] * (1-f[b]) * math.exp(u*(energies[a]-energies[b])) for a in range(2) for b in range(2))
            return math.cos(nu*u)*k
        value, error = quad(integrand, 0, beta, epsabs=1e-12)
        time_values.append(value)
    assert np.max(np.abs(matsubara - time_values)) < 2e-11
    report["time_domain_chi"] = {"matsubara": matsubara.tolist(), "integral": time_values}

    # Two spins, HS Hessian: (1/2)*(2U/beta)*r_n*(F_cc+F_ss).
    expected = sum(2*coupling*omega**2 / ((2*math.pi*n/beta)**2 + omega**2) * susceptibility(h, beta, 2*math.pi*n/beta).sum() for n in range(1, 4))
    hessian_rows = []
    for step in [0.01, 0.005, 0.0025]:
        actual = 0.0
        for n in range(1, 4):
            nu = 2*math.pi*n/beta
            variance = (2*coupling/beta) * omega**2 / (nu**2 + omega**2)
            for site in range(2):
                for sine in [False, True]:
                    positive = determinant_ratio(h, beta, step, site, n, sine)
                    negative = determinant_ratio(h, beta, -step, site, n, sine)
                    second = (positive + negative - 2) / step**2
                    actual += variance * second / 2
        hessian_rows.append({"step": step, "value": actual, "expected": float(expected), "absolute_error": abs(actual-expected)})
    assert hessian_rows[-1]["absolute_error"] < 2e-8
    assert hessian_rows[-1]["absolute_error"] < hessian_rows[0]["absolute_error"]
    report["hs_hessian"] = hessian_rows

    bridge_rows = []
    t, coupling, c, d = 1.0, 1.0, 10.0, 4.0
    for tau in [0.2, 0.1, 0.05, 0.02, 0.01]:
        beta, omega, delta = 1/tau, tau/c, d*tau
        h = bridge(t, delta)
        eigenvalues = eigh(h, eigvals_only=True)
        analytic = [-delta/2, delta/2, delta/2 + 2*t*t/delta]
        assert np.max(np.abs(eigenvalues-analytic)) < 1e-11
        values, tail = first_cumulant(h, beta, omega, coupling)
        aweight = 1 / (1 + delta*delta/(2*t*t))
        lower = coupling*aweight*omega**2*delta*math.tanh(beta*delta/4) / (((2*math.pi/beta)**2+omega**2)*((2*math.pi/beta)**2+delta**2))
        upper = coupling*omega**2*beta**3/48
        assert values[0] >= lower*(1-1e-10)
        assert values[0] <= upper
        bridge_rows.append({"tau": tau, "omega": omega, "endpoint_cumulant": float(values[0]), "one_mode_lower": lower, "general_upper": upper, "sum_tail_bound": tail, "normalized": float(values[0]/(coupling*omega**2*beta**3))})
    report["fixed_t_bridge"] = bridge_rows

    # Finite positive barriers realize the bridge continuously inside a square torus.
    tau, delta, omega = 0.1, 0.4, 0.01
    target, _ = first_cumulant(bridge(t, delta), 1/tau, omega, coupling, modes=500)
    embedded_rows = []
    for barrier in [1e2, 1e3, 1e4, 1e5]:
        full, sites = square_embedding(t, delta, barrier)
        values, tail = first_cumulant(full, 1/tau, omega, coupling, modes=500)
        error = abs(values[sites[0]] - target[0])
        density = 2*expit(-eigh(full, eigvals_only=True)/tau).sum()/len(full)
        embedded_rows.append({"barrier": barrier, "endpoint_cumulant": float(values[sites[0]]), "bridge": float(target[0]), "absolute_error": float(error), "conditional_density": float(density)})
    assert embedded_rows[-1]["absolute_error"] < embedded_rows[0]["absolute_error"] / 100
    report["square_embedding"] = embedded_rows

    # Spectral commutator sum rule, including degree-four square embedding.
    h, sites = square_embedding(0.7, 0.5, 5.0)
    energies, vectors = eigh(h)
    p = np.abs(vectors)**2
    delta = energies[None, :] - energies[:, None]
    spectral = np.einsum("xa,xb,ab->x", p, p, delta**2)
    direct = 2*(np.sum(np.abs(h)**2, axis=1) - np.diag(h)**2)
    assert np.max(np.abs(spectral-direct)) < 1e-10
    values, tail = first_cumulant(h, 2.0, 0.1, 1.0)
    bound = 4*0.7**2*0.1**2*2.0**5/1440
    assert np.max(values) <= bound
    report["sum_rule_max_error"] = float(np.max(np.abs(spectral-direct)))
    report["claims"] = ["variance normalization", "Kubo sign and spin factors", "fixed-t thermal resonance", "square-barrier convergence", "commutator sum rule"]
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    run()
