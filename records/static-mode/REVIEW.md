# Independent Review of STATIC-MODE

- **Reviewed files:** `D:/dev/scratch/ceiling-20261118/MASSIVE/STATIC-MODE/{RESULT.md,RIGOR.md,replay.py,CHECKS.txt,replay.stdout.txt,replay.stderr.txt,replay.initial.stderr.txt}`
- **Verdict:** **PASS** (0 P0, 0 P1, 0 P2; 3 non-blocking P3 remarks)
- **Allowed labels:**
  - **PROVED** for the analytical claims in `RIGOR.md` §§1–6 (exact first dynamic cumulant eq. (6), zero-frequency cancellation, three-site witness eq. (1) with constant `1/1200` on `0 < Omega <= tau <= t/4`, finite-barrier square-torus embedding eqs. (2)–(3) with constant `1/2400` for `L >= 4`, auxiliary bounds (4), (5), (7), (8), and the scoped method obstruction in §6).
  - **CERTIFIED** for the exact-rational constant guards in `replay.py:exact_constants` (`pi < 22/7`, `(22/7)^2 < 10`, `tanh(1) > 3/4`, `(2/3)*4*(3/4)/(41*56) = 1/1148 > 1/1200`, half-constant `1/2400`).
  - **NUMERICAL** for the floating-point / `mpmath` finite-matrix and ODE checks in `replay.py` and the independent cross-checks below.
- **Recommendation:** **Fold into a barriers note** (or the capstone method-barriers section). The witness is mathematically clean, genuinely new relative to LINEAR4–11/BARRIERS/LIMITS, and worth preserving, but its scope is a narrow companion obstruction rather than a standalone paper.

---

## 1. Line-by-line mathematical verification

### 1.1 Definition of `a_x(W)`, zero-frequency cancellation, and spin/sign factors (`RIGOR.md` §§1, 3)
- **Zero-frequency invariance (`RIGOR.md:7-16`):** Because `v_x(u)` is centered Gaussian with covariance `D_dyn(u)` supported only on `nu_n != 0`, `int_0^beta v_x(u) du = 0` almost surely. Replacing `n_x` by `n_x - 1` therefore leaves the dynamic exponent unchanged to all orders in `s`.
- **First derivative `R'_W(0)` (`RIGOR.md:75-106`):** Expanding `T exp[-int_0^beta (H_W + sqrt(s) sum_x v_x(u) n_x) du]` to order `s` and taking `E_v` yields `+(1/2) sum_x int_0^beta du int_0^beta du' D_dyn(u-u') <T n_x(u) n_x(u')>_W`. The disconnected Hartree piece `<n_x>_W^2` is time-independent and integrates to zero against `D_dyn`. Cross-spin connected terms vanish at fixed `W`; the two identical spin sectors cancel `1/2`.
- **Eigenbasis formula eq. (6) (`RIGOR.md:88-106`):** In the eigenbasis of `h_W`, `K_x(u) = sum_{a,b} p_a(x) p_b(x) f(e_a)(1-f(e_b)) exp(u(e_a-e_b))` for `0 < u < beta`. Using `f(e_a)(1-f(e_b))(exp(beta(e_a-e_b)) - 1) = f(e_b) - f(e_a)`, integrating against `exp(i nu_n u)` for `nu_n != 0`, and symmetrizing `(a,b) <-> (b,a)` gives
  `chi_x(i nu_n) = sum_{a,b} p_a(x) p_b(x) [f(e_a) - f(e_b)](e_b - e_a) / [nu_n^2 + (e_b - e_a)^2]`.
  Every term is nonnegative, diagonal/degenerate pairs vanish, and `chi_x(i nu_n) = chi_x(-i nu_n)` yields eq. (6) with `2 U sum_{n>=1}`. Since `R_W(0) = 1`, `(d/ds)|_{s=0} log R_W(s) = R'_W(0) = sum_x a_x(W)`.
- **Auxiliary bounds (`RIGOR.md` §§2–3):** Verified eq. (4) (`q(a) <= a^2/12`), eq. (5) (static Combes-Thomas bound `|<Delta_x^dagger Delta_y>_W| <= (25/16) exp(-2 alpha d(x,y))` with `alpha = (1 + 16 beta t)^(-1)`), eq. (7) (`a_x <= U Omega^2 beta^3 / 48`), and eq. (8) (`a_x <= d_x t^2 U Omega^2 beta^5 / 1440` via `sum_{a,b} p_a(x) p_b(x)(e_b - e_a)^2 = 2 d_x t^2` and `sum_{n!=0} nu_n^(-4) = beta^4/720`).

### 1.2 Three-site witness and constant `1/1200` (`RIGOR.md` §4, `RESULT.md:20-31`)
- For `h_3 = [[delta/2, -t, 0], [-t, -delta/2 + 2t^2/delta, -t], [0, -t, delta/2]]`:
  - Antisymmetric vector `(1, 0, -1)/sqrt(2)` is an exact eigenvector with `e_+ = delta/2`, `p_+(left) = 1/2`.
  - On `span{(1,0,1)/sqrt(2), (0,1,0)}`, the symmetric block `[[delta/2, -sqrt(2)t], [-sqrt(2)t, -delta/2 + 2t^2/delta]]` has trace `2t^2/delta` and determinant `-delta^2/4 - t^2 = (-delta/2)(delta/2 + 2t^2/delta)`, giving exact eigenvalues `e_- = -delta/2` and `e_high = delta/2 + 2t^2/delta`.
  - At `e_- = -delta/2`, the middle/symmetric-endpoint amplitude ratio is `delta/(sqrt(2)t)`, so `p_-(left) = A/2` with `A = [1 + delta^2/(2t^2)]^(-1)`.
- Keeping only `n = 1` and the two ordered low-state pairs `(-,+), (+,-)` in eq. (6) gives `2 U r_1 * (A/2) * delta tanh(beta delta/4) / (4 pi^2 tau^2 + delta^2)`, matching eq. (9) exactly.
- Setting `delta = 4 tau` on `0 < Omega <= tau <= t/4`: `delta/t <= 1 => A >= 2/3`; `tanh(1) = (e^2-1)/(e^2+1) > 3/4` (since `e^2 > sum_{k=0}^4 2^k/k! = 7`); `pi < 22/7 => pi^2 < 484/49 < 10`; hence
  `a_left > [(2/3) * 4 * (3/4) / (41 * 56)] * U Omega^2 / tau^3 = (1/1148) U Omega^2 / tau^3 > (1/1200) U Omega^2 / tau^3`.
  All rational steps are exact and verified.

### 1.3 Square-torus embedding and constant `1/2400` (`RIGOR.md` §5, `RESULT.md:33-41`)
- For any `L >= 4`, the three collinear sites `(0,0), (0,1), (0,2)` on `Z_L^2` induce the open path `P_3` (endpoints `(0,0)` and `(0,2)` are at graph distance `2`, not adjacent, even at `L = 4`).
- In block form `h_B = [[h_3, V], [V^*, B I - t A_complement]]`, `B I - t A_complement >= (B - 4t) I` and `||V|| <= sqrt(6) t < 4t`. Since the three eigenvalues of `h_3` are strictly simple (`-2tau < 2tau < 2tau + t^2/(2tau)`), the Feshbach-Schur block-inversion formula shows `(h_B - z)^(-1) -> (h_3 - z)^(-1) (+) 0` uniformly on small contours around `e_-, e_+` as `B -> +infty`, so the two low eigenvalues and endpoint weights converge to those of `h_3`.
- Because every summand of eq. (6) is nonnegative, retaining only `n = 1` and the two converging low-state pairs avoids any limit exchange in the infinite Matsubara sum. Their sum converges to the RHS of eq. (9) `> U Omega^2 / (1200 tau^3) > U Omega^2 / (2400 tau^3)`, establishing existence of finite `B_0(L, t, tau, Omega)` such that eq. (2) holds for all `B >= B_0`.
- Finite-volume uniformity: `RIGOR.md` explicitly disclaims any uniform estimate on `B_0`, and notes that taking `L = 4` already gives `R'_{W_B}(0)/16 >= U Omega^2 / (2400 * 16 tau^3)`, which suffices to disprove a bound uniform in both `L >= 4` and `W`. (No overclaim.)

### 1.4 Obstructed proof class and non-overclaim check (`RIGOR.md` §§6–7, `RESULT.md:43-47`)
- The obstructed class (`RIGOR.md:159-163`) is precisely defined: (1) condition on arbitrary real static `W` using the static free-fermion reference `H_W`, (2) expand the Gaussian-integrated nonzero-mode interaction without resumming connected contributions into a new reference, (3) require a uniform-in-`W` small local activity (or per-volume majorant) at `tau = C Omega` that dominates the exact `O(s)` local connected term `a_x(W)` (or `R'_W(0)/L^2`).
- The witness genuinely defeats this class: `a_x(W)` is literally the exact `O(s)` connected single-site cumulant of `log R_W(s)`, so any absolute expansion whose local activity majorizes `a_x(W)` uniformly in `W` cannot stay small (or even bounded) at `tau = C Omega` as `Omega -> 0`.
- Scope exclusions are thorough and honest: no claim of nonconvergence of every Taylor/cluster series, no obstruction to source-connected resummations or annealed `det^2`-weighted estimates (noting that `W_middle ~ t^2/(2tau)` is exponentially suppressed under the static Gaussian), and no physical `T_pair` no-go claim.

---

## 2. Novelty relative to LINEAR4–11, BARRIERS, and LIMITS

- **LINEAR4** (`PUBLISH/linear4/repo/replay/RIGOR.md`): uses the exact static/dynamic Matsubara split and unrestricted static conditioning, but bounds the dynamic field via a per-history sup-norm cutoff `r = tau/64`, producing the `(U Omega^2)^(1/3) log^(1/3)` ceiling.
- **LINEAR5** (`ADIABATIC/LINEAR5/SHARPNESS.md`): proves the `2/3` exponent is sharp for bounded per-history rare-history cutoffs uniform over atomic (`t = 0`) references, and shows the projected dynamic Gaussian is not reflection positive.
- **LINEAR6** (`ADIABATIC/LINEAR6/RESULT.md`): proves a linear-in-`Omega` bound conditional on `g`-gapped static fields (`Theorem C`) and isolates the open near-Fermi static-field gap `(P_loc)` + `(Buf)`.
- **LINEAR7 / BARRIERS** (`ADIABATIC/LINEAR7/RESULT.md`, `PUBLISH/barriers/RESULT.md`, `10.5281/zenodo.24384373`): constructs a time-mean-zero dynamic field on `K_{1,3}` making `det(1 + U_v) = 0` at `beta ||v||_infty <= 5`, obstructing unrestricted per-history normalized propagator bounds.
- **LINEAR8–11 / LIMITS** (`PUBLISH/limits/RESULT.md`): analyzes annealed `det^2`-weighted defect-insertion bounds and shows why they do not localize or imply clustering.

**Assessment:** **New companion obstruction (not subsumed).** While the dimensionless cubic scale `U Omega^2 / tau^3` was already identified in LINEAR4–5, none of LINEAR5–11/BARRIERS/LIMITS rules out integrating out the dynamic Gaussian *first* around the strictly positive static free-fermion reference at fixed bare hopping `t > 0`. STATIC-MODE closes that exact loophole using neither an atomic `t = 0` limit nor a dynamic determinant zero: after exact Hartree cancellation, the exact first integrated cumulant still attains the cubic scale `Theta(U Omega^2 / tau^3)` on a fixed-hopping square torus. Because it only blocks unresummed uniform-in-`W` expansions and does not advance the annealed route or the physical target, it belongs folded into a barriers note rather than as a standalone paper.

---

## 3. Findings

1. **[P3 — minor, non-blocking] Ambiguous reuse of `phi` for mean-zero vs. origin-pinned gauge primitive (`RIGOR.md:181-183`).**
   Line 181 specifies `phi(0) = phi(beta) = 0` to preserve the monodromy and time-zero insertion, and line 183 writes "On the gauge-centered primitive, the simple variance upper bound is `Var(phi) <= U Omega^2 beta^3 / 720`, obtained by dividing the nonzero Fourier coefficients by `nu_n^2`." Dividing the nonzero Fourier variances of `v` by `nu_n^2` bounds the **time-mean-zero** primitive `tilde_phi` (`int_0^beta tilde_phi = 0`), whereas the origin-pinned primitive `phi(u) = tilde_phi(u) - tilde_phi(0)` has larger variance (up to `U Omega^2 beta^3 / 192` at `u = beta/2`, a factor of `15/4` larger). Recommend distinguishing `tilde_phi` (`1/720`) from `phi(u) = tilde_phi(u) - tilde_phi(0)` (`<= 1/192`, or `<= 1/180`). Does not affect the main proposition or any constant in §§1–6.

2. **[P3 — minor, non-blocking] Schur-complement inverse vs. full resolvent wording (`RIGOR.md:151`).**
   Line 151 writes that the Schur complement `h_3 - z - V(B I - t A_complement - z)^(-1) V^*` has "Its resolvent" converging on small contours around the three simple eigenvalues, giving spectral-projection convergence. The inverse of the Schur complement is the upper-left `3x3` block `[(h_B - z)^(-1)]_{11}` of the full resolvent; full-resolvent convergence `(h_B - z)^(-1) -> (h_3 - z)^(-1) (+) 0` follows immediately because the remaining blocks `12, 21, 22` are `O(B^(-1))` uniformly on the contour. Adding one clause noting the `O(B^(-1))` decay of the other three blocks makes the contour-integral step fully explicit.

3. **[P3 — minor, non-blocking] Cross-document coupling symbol `U = g^2/K` (`RESULT.md:7`, `RIGOR.md:7`).**
   STATIC-MODE writes `U = g^2/K` (using `g` for the linear force constant `F` in `F X n_x`), whereas LINEAR4/LINEAR5 use `U = F^2/K` and reserve `g` for the boson-operator coupling `g(a + a^dagger)(n - 1)` with `g^2 = U Omega / 2`. Internally consistent (since `g` does not reappear in any formula), but worth aligning to `U = F^2/K` if folded into a combined barriers document.

---

## 4. Rerun of `CHECKS.txt` commands and exit codes

All commands were executed locally with temporary outputs under `C:/t/StaticReview` (removed at closure); no author files were modified.

| Check | Command | Exit code | Result |
| --- | --- | --- | --- |
| Full replay (`CHECKS.txt` #1/#3) | `UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with numpy --with scipy --with mpmath python -B D:/dev/scratch/ceiling-20261118/MASSIVE/STATIC-MODE/replay.py > C:/t/StaticReview/replay.stdout.txt 2> C:/t/StaticReview/replay.stderr.txt` | **0** | `stderr` 0 bytes; `diff -u` against retained `replay.stdout.txt` exited **0** (byte-for-byte identical). |
| Targeted Hessian diagnostic (`CHECKS.txt` #2) | `UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with numpy --with scipy --with mpmath python -B -c '...'` (verbatim command from `CHECKS.txt` line 17) | **0** | `expected = 0.0014874704743052386`; errors at steps `0.01, 0.005, 0.0025`: `+3.778638216992564e-09`, `+9.314418210251002e-10`, `+1.7016681553433388e-10` (matches `replay.stdout.txt`). |
| `CHECKS.txt` #4 (`rmdir C:/t/StaticMode`) | Author's own temp cleanup (not a verification check) | N/A | Reviewer's own temp dir `C:/t/StaticReview` was removed at closure. |

---

## 5. Independent recomputation of `a_end(W)`

We independently recomputed `a_left(W)` for the three-site witness `W = (2tau, t^2/(2tau) - 2tau, 2tau)` and its `L = 4` torus embedding using two independent methods not used in `replay.py`:
1. **Exact closed-form Matsubara sum (60-digit `mpmath`, zero mode truncation):** using partial fractions and `sum_{n>=1} 1/(nu_n^2 + E^2) = (1/(2 E^2))[(beta E / 2) coth(beta E / 2) - 1]`.
2. **Direct time-domain Kubo integral (`scipy.integrate.quad`):** `a_left = beta int_0^beta D_dyn(u) K_left(u) du` with the closed-form hyperbolic-cosine kernel `D_dyn(u) = (U Omega / 2) cosh(Omega(beta/2 - u))/sinh(beta Omega / 2) - U/beta`.

Independent script (`C:/t/StaticReview/indep.py`, deleted after run) exited **0**:

| Parameter point `(t, U, tau, Omega)` | Exact closed-form `a_left` (`mpmath`, 60 dps) | Time-domain `quad` `a_left` | `|exact - quad|` | Lower bound `U Omega^2/(1200 tau^3)` (ratio) | Upper bound `U Omega^2/(48 tau^3)` | `L=4` torus `a_(0,0)` at `B=10^5` (`|diff|` from bridge) |
| --- | --- | --- | --- | --- | --- | --- |
| **Point 1 (matches `replay.py`):** `(1.0, 1.0, 0.1, 0.01)` | `1.47305039128258901e-04` | `1.47305039128189539e-04` | `6.94e-17` | `8.333333333333333e-05` (`1.7677x`) | `2.083333333333333e-03` | `1.473120774394613e-04` (`7.04e-09`, `>= 1/2400` True) |
| **Point 2 (fresh interior):** `(2.5, 0.7, 0.5, 0.2)` | `3.35124388563844460e-04` | `3.35124388563834766e-04` | `9.70e-18` | `1.866666666666667e-04` (`1.7953x`) | `4.666666666666667e-03` | `3.351433602838232e-04` (`1.90e-08`, `>= 1/2400` True) |
| **Point 3 (domain boundary `Omega = tau = t/4`):** `(4.0, 3.0, 1.0, 1.0)` | `4.43768474902203205e-03` | `4.43768474902201185e-03` | `2.00e-17` | `2.500000000000000e-03` (`1.7751x`) | `6.250000000000000e-02` | `4.438015797172071e-03` (`3.31e-07`, `>= 1/2400` True) |

At Point 1, `replay.py`'s 2000-mode truncated value (`1.4730503911082875e-04`) differs from the exact closed-form value by `1.74e-11`, well within its reported analytic tail bound `6.33e-07`. At all three points, the `L = 4` torus values at `B = 10^2, 10^3, 10^4, 10^5` converge monotonically to the three-site bridge value at rate `O(1/B)` and satisfy `a_(0,0)(W_B) >= U Omega^2 / (2400 tau^3)`.
