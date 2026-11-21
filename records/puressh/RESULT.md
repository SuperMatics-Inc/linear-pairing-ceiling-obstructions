# PURESSH Result: Frequency-Uniform High-Temperature Pair-Correlation Ceiling and Route Obstructions for the Pure Bond-SSH Model ($U_{\rm eff} = 0$)

## Verdict

**THEOREM (`PROVED (pending independent review)`) + EXACT ROUTE OBSTRUCTIONS (`PROVED (pending independent review)`, finite identities `CERTIFIED`).**

1. **Selected Route (Route (a) — Direct High-Temperature Dyson-Wick Polymer Expansion without Atomic Gap):** Closes completely as an explicit, volume-, chemical-potential-, and frequency-uniform grand-canonical and thermodynamic canonical exponential pair-clustering theorem (Theorems 1.1 and 1.2) whenever $\beta |t| + \frac{\beta g^2}{K} \le 2^{-10}$, giving the ceiling
   $$k_B T_{\rm pair} \le 2^{10}\left(|t| + \frac{g^2}{K}\right) \le 2^{11} \max\left(|t|,\, \frac{g^2}{K}\right),$$
   uniformly in $\Omega = \sqrt{K/M} > 0$, $\mu \in \mathbb{R}$, and torus side $L \ge 4$.
2. **Proved Route Obstructions (Route (b), Route (c), Route (d)):**
   - **Route (b) (Phonon-Induced Effective Instantaneous Gap):** **OBSTRUCTED** (Proposition 7.1). Integrating out the bond oscillators at $\Omega \to \infty$ produces $H_{\rm eff}^{\rm inst} = -\frac{g^2}{2K} \sum_b T_b^2$, which commutes with $N_{\rm odd} = \sum_x (n_{x\uparrow}-n_{x\downarrow})^2$ and has **zero energy gap** $\Delta_{\rm eff}(C_4) := \min\operatorname{spec}(H_{\rm eff}^{\rm inst}|_{N=4, N_{\rm odd}>0}) - \min\operatorname{spec}(H_{\rm eff}^{\rm inst}|_{N=4, N_{\rm odd}=0}) = 0$ across all odd-parity sectors at half-filling $N = 4$ on $C_4$ (both in the spin-balanced $N_\uparrow = N_\downarrow = 2$ space of dimension $36$ and in the full $N = 4$ space of dimension $70$: $\min\operatorname{spec} = -6\frac{g^2}{K}$ on $\{N_{\rm odd}=0, S^z=0\}$ and $\{N_{\rm odd}=4, S^z=0\}$, $-5\frac{g^2}{K}$ on $\{N_{\rm odd}=2, S^z=0\}$, $-4\frac{g^2}{K}$ on $\{N_{\rm odd}=4, S^z=\pm 1\}$, $-3\frac{g^2}{K}$ on $\{N_{\rm odd}=2, S^z=\pm 1\}$, and $0$ on $\{N_{\rm odd}=4, S^z=\pm 2\}$). Moreover, the retarded bond interaction loses its zero-Matsubara-frequency stiffness as $\Omega \downarrow 0$.
   - **Route (c) (Bond Lang-Firsov / Squeezed Unitary Transformation):** **OBSTRUCTED** (Proposition 7.2). Adjacent bond currents fail to commute ($\|[T_{\{x,y\}}, T_{\{y,z\}}]\|_{\rm op} = 2$), generating a non-terminating Baker-Campbell-Hausdorff hierarchy of multi-bond momentum operators whose dimensionless norm $\frac{g}{K}\|P_b\psi\| / \langle H_{\rm ph}\rangle_\psi^{1/2} \propto \sqrt{g^2/(K\Omega)} \to \infty$ diverges as $\Omega \downarrow 0$.
   - **Route (d) (Necessity of a Small-$\beta|t|$ Condition for Uniform Exponential Clustering):** **PROVED OBSTRUCTION** (Proposition 7.3). Even at $g = 0$ (no pairing interaction and no ODLRO), the exact $T = 0$ ($\beta|t| \to \infty$) 2D square-lattice half-filled ($\mu = 0$) pair correlator along the staircase ray $y - x = r_m = (m, m-1)$ at graph distance $d = \|r_m\|_1 = 2m-1 \ge 1$ equals $\frac{4}{\pi^4(2m-1)^2} = \frac{4}{\pi^4 d^2}$ and decays only algebraically as $\|x-y\|_1^{-2}$ (exceeding the Theorem 1.1 bound $A_{\rm GC} q_{\rm GC}^d$ already at $m = 2, d = 3$, where $\frac{4}{9\pi^4} \approx 4.5627 \times 10^{-3} > A_{\rm GC} q_{\rm GC}^3 \approx 2.7359 \times 10^{-3}$). Thus **no** $(\beta t)$-independent exponential decay bound $|\langle \Delta_x^\dagger \Delta_y \rangle| \le A q^{d(x,y)}$ ($q < 1$) can hold under a $\beta g^2/K$-only hypothesis at $U_{\rm eff} = 0$.

---

## Exact Statement of Main Theorems (`RIGOR.md` §1.2)

Let $\Lambda_L = (\mathbb{Z}/L\mathbb{Z})^2$ ($L \ge 4$) be the 2D square torus with undirected nearest-neighbor bond set $\mathcal{E}_{\Lambda_L}$ ($|\mathcal{E}_{\Lambda_L}| = 2L^2$, degree $D = 4$), and let
$$H_{\Lambda_L} = -\sum_{b=\{x,y\} \in \mathcal{E}_{\Lambda_L}} (t - g X_b) \sum_{\sigma \in \{\uparrow,\downarrow\}} (c_{x\sigma}^\dagger c_{y\sigma} + c_{y\sigma}^\dagger c_{x\sigma}) + \sum_{b \in \mathcal{E}_{\Lambda_L}} \left(\frac{P_b^2}{2M} + \frac{K}{2} X_b^2\right) - \mu N$$
on $\mathcal{H}_{\Lambda_L} = \mathcal{F}_{\rm el}(\Lambda_L) \otimes \bigotimes_{b \in \mathcal{E}_{\Lambda_L}} L^2(\mathbb{R})$, with $t \in \mathbb{R}$, $g \in \mathbb{R}$, $K > 0$, $M > 0$, $\Omega = \sqrt{K/M} > 0$, $\mu \in \mathbb{R}$, $U_{\rm eff} = 0$, and on-site pair operator $\Delta_x = c_{x\downarrow} c_{x\uparrow}$.

### Theorem 1.1 (Grand-Canonical Exponential Pair Clustering and Susceptibility Bound — `PROVED (pending independent review)`)
Assume $\beta > 0$, $t \in \mathbb{R}$, $g \in \mathbb{R}$, $K > 0$, $M > 0$ ($\Omega = \sqrt{K/M} > 0$), $\mu \in \mathbb{R}$, and $L \ge 4$ satisfy
$$\beta |t| + \frac{\beta g^2}{K} \le c_0 := 2^{-10} = \frac{1}{1024}$$
(satisfied in particular whenever $\beta|t| \le 2^{-11}$ and $\beta g^2/K \le 2^{-11}$). Then for every $x, y \in \Lambda_L$ at graph distance $d = d_{\Lambda_L}(x, y)$:

1. **Distinct-site exponential decay ($d \ge 1$):**
   $$\left|\langle \Delta_x^\dagger \Delta_y \rangle_{\Lambda_L, \beta, \mu}\right| \le A_{\rm GC}\, q_{\rm GC}^d, \qquad A_{\rm GC} = \frac{341}{103} \approx 3.31067961, \qquad q_{\rm GC} = \frac{32}{341} \approx 0.09384164 < \frac{1}{10}.$$
2. **Uniform $\ell^1$ pair susceptibility bound:**
   $$\chi_{\rm pair}(\Lambda_L, \beta, \mu) := \sum_{y \in \Lambda_L} \left|\langle \Delta_x^\dagger \Delta_y \rangle_{\Lambda_L, \beta, \mu}\right| \le R_{\rm max} := 1 + \frac{4 A_{\rm GC} q_{\rm GC}}{(1 - q_{\rm GC})^2} = \frac{24718511}{9834543} \approx 2.51343769 < 3.$$
3. **Analyticity of grand-canonical pressure:** With the translation-summed two-site pair-hop source $V_{\rm src}(\xi) = -\xi \sum_{e' \in \mathcal{E}_{\rm src}} Y_{e'}(\theta)$, $Y_{e'}(\theta) := e^{i\theta}\Delta_x^\dagger \Delta_{x+r} + e^{-i\theta}\Delta_{x+r}^\dagger \Delta_x$ ($\mathcal{E}_{\rm src} = \{e'_x = \{x, x+r\} : x \in \Lambda_L\}$), $Z_{\Lambda_L}(\xi) \ne 0$ and $p_{\Lambda_L}(\xi) = |\Lambda_L|^{-1}\log Z_{\Lambda_L}(\xi)$ is analytic in $\{|\xi| < \xi_0\}$ with $\xi_0 = 2^{-9}\beta^{-1}$, and satisfies $|p_{\Lambda_L}(\xi) - p_{\Lambda_L}(0)| \le -2\log(1 - b_{\rm src}/e) = -2\log\!\left(1 - \frac{216}{269 e}\right) < 0.7012 < 2$ (with source-augmented Kotecký-Preiss budget $b_{\rm src} := \frac{216}{269} < 1$).

### Theorem 1.2 (Thermodynamic Canonical Pair Clustering — `PROVED (pending independent review)`)
Under the hypothesis $\beta|t| + \frac{\beta g^2}{K} \le 2^{-10}$ of Theorem 1.1, for every fixed nonzero lattice displacement $r \in \mathbb{Z}^2 \setminus \{0\}$ with $d = \|r\|_1 \ge 1$, every fixed parameters $(\beta, t, g, K, M)$, and every sequence of square tori $\Lambda_{L_j}$ ($L_j \to \infty$) and particle numbers:
- at fixed total density $N_j / L_j^2 \to n \in (0, 2)$, or
- in the spin-balanced canonical sector $N_{\uparrow, j} = N_{\downarrow, j} = N_{{\rm pair}, j}$ with $N_{{\rm pair}, j} / L_j^2 \to n_\sigma \in (0, 1)$,

the canonical pair correlator satisfies
$$\limsup_{j \to \infty} \left|\langle \Delta_0^\dagger \Delta_r \rangle_{\Lambda_{L_j}, N_j}^{\rm can}\right| \le A_{\rm GC}\, q_{\rm GC}^{\|r\|_1}, \qquad \limsup_{j \to \infty} \left|\langle \Delta_0^\dagger \Delta_r \rangle_{\Lambda_{L_j}, (N_{{\rm pair}, j}, N_{{\rm pair}, j})}^{\rm can}\right| \le A_{\rm GC}\, q_{\rm GC}^{\|r\|_1},$$
with the same explicit constants as Theorem 1.1:
$$A_{\rm GC} = \frac{341}{103} \approx 3.31067961, \qquad q_{\rm GC} = \frac{32}{341} \approx 0.09384164 < \frac{1}{10}.$$

---

## Constants and Comparison to `SSHBOUND3`

| Quantity | Pure Bond-SSH (`PURESSH`, $U_{\rm eff} = 0$) | Attractive-Hubbard + Bond-SSH (`SSHBOUND3`, $U_{\rm eff} > 0$) |
|---|---|---|
| Electronic unperturbed generator $D_0$ | $-\mu N$ (no atomic gap) | $\frac{U_{\rm eff}}{2} N_{\rm odd} - \mu N$ |
| Small parameter(s) | $\beta|t| + \frac{\beta g^2}{K} \le 2^{-10}$ | $\frac{\beta t^2}{U_{\rm eff}} \le 2^{-27}$ and $\frac{\beta g^2}{K} \le 2^{-13}$ |
| Ceiling on $k_B T_{\rm pair}$ | $\le 2^{10}(|t| + g^2/K) \le 2^{11}\max(|t|, g^2/K)$ | $\le \max(2^{27} t^2/U_{\rm eff},\, 2^{13} g^2/K)$ |
| Physical edge activity $\varepsilon_{\rm phys}$ | $\exp(2(\beta|t| + \beta g^2/K)) - 1 \le \frac{2}{1023}$ | $\frac{593}{134209536} \approx 4.4185 \times 10^{-6}$ |
| Source edge activity $\varepsilon_{\rm src}$ | $e^{\beta|\xi|} - 1 \le \frac{2}{1023}$ at $\beta|\xi| \le 2^{-9}$ (giving $b_{\rm src} = \frac{216}{269} < 1$ on $\{|\xi| < \xi_0 = 2^{-9}\beta^{-1}\}$) | $\frac{1125}{1073676288}$ at $\beta|\xi| \le 2^{-14}$ |
| Grand-canonical decay base $q_{\rm GC}$ | $\frac{32}{341} \approx 0.09384164$ | $\frac{48645}{524224} \approx 0.09279430$ |
| Grand-canonical prefactor $A_{\rm GC}$ | $\frac{341}{103} \approx 3.31067961$ | $\frac{1965840}{475579} \approx 4.13357192$ |
| Grand-canonical KP budget $b_{\rm GC}$ | $\frac{32}{103} \approx 0.31067961 < 1$ | $\frac{729675}{1902316} \approx 0.38357192 < 1$ |
| Susceptibility ceiling $R_{\rm max}$ | $\frac{24718511}{9834543} \approx 2.51343769 < 3$ | $\frac{308086835615302339}{107564263537529539} \approx 2.86421000 < 3$ |
| Source-augmented KP budget $b_{\rm src}$ | $\frac{216}{269} \approx 0.80297398 < 1$ | $\frac{6567075}{6636364} \approx 0.98955919 < 1$ |
| Canonical prefactor (Theorem 1.2) | $A_{\rm GC} = \frac{341}{103} \approx 3.31067961$ (via single-bond derivative $\partial_\xi p_{\Lambda_L}(0)$) | $A_{\rm GC} = \frac{1965840}{475579} \approx 4.13357192$ (via single-bond derivative $\partial_\xi p_{\Lambda_M}(0)$) |

---

## Exercised Verification Commands and Mutant Results

1. **Exact-rational and outward-interval proof replay (`CERTIFIED`):**
   ```
   UV_OFFLINE=1 UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with mpmath python -B D:/dev/scratch/ceiling-20261118/ADIABATIC/PURESSH/replay.py
   ```
   - **Exit code:** `0`
   - **Checks verified:**
     - Exact $16 \times 16$ integer Fock-space operator norms and minimal polynomials: $\|T_b\|_{\rm op} = 2$ ($T_b^5 - 5 T_b^3 + 4 T_b = 0$, eigenvector $(T_b^2 - 4 I)v_{\rm bond} = 0$), $\|Y_{e'}(\theta)\|_{\rm op} = 1$, $\|\Delta_x^\dagger \Delta_y\|_{\rm op} = 1$, $[T_b, N_\sigma] = 0$, $[Y_{e'}(\theta), N_\sigma] = 0$.
     - Exact rational matrix exponential and 3-segment Schatten-Hölder trace inequality on random non-commuting $4 \times 4$ Hermitian matrices across 6 uneven simplex splits.
     - Outward-rounded rational interval verification of the phonon covariance integral $\int_0^\beta \int_0^\beta C_\beta(|u-v|)\,du\,dv = \beta g^2/K$, $C_\beta(\tau) > 0$, and the $n = 4$ Gaussian Wick identity across $\Omega \in \{1/5, 1, 5, 50, 500\}$.
     - Exact rational certification of $\varepsilon_{\rm phys} = \frac{2}{1023}$, $\varepsilon_{\rm src} = \frac{2}{1023}$, $q_{\rm GC} = \frac{32}{341} < \frac{1}{10}$, $b_{\rm GC} = \frac{32}{103} < 1$, $A_{\rm GC} = \frac{341}{103}$, $R_{\rm max} = \frac{24718511}{9834543} < 3$, $q_{\rm src} = \frac{72}{341}$, $b_{\rm src} = \frac{216}{269} < 1$, and $-2\log(1 - b_{\rm src}/e) < 2$.
     - Outward-rounded rational interval certification of the canonical boundary oscillator stiffness doubling/halving inequality across $\Omega \in \{1/10, 1, 10, 100\}$.
     - Exact integer certification of the §7 route obstructions: Proposition 7.1 ($256 \times 256$ Fock space of $C_4$, $[T_b^2, N_{\rm odd}] = 0$, exact integer minimal polynomials and maximum eigenvalues across all 9 $(N_\uparrow, N_\downarrow, N_{\rm odd})$ invariant sectors (6 spin-flip-conjugate classes) of $N=4$ showing $\lambda_{\max} = 12$ on $\{N_{\rm odd}=0, S^z=0\}$ and $\{N_{\rm odd}=4, S^z=0\}$, $10$ on $\{N_{\rm odd}=2, S^z=0\}$, $8$ on $\{N_{\rm odd}=4, S^z=\pm 1\}$, $6$ on $\{N_{\rm odd}=2, S^z=\pm 1\}$, and $0$ on $\{N_{\rm odd}=4, S^z=\pm 2\}$, yielding $\Delta_{\rm eff}(C_4) = 0$), Proposition 7.2 ($\|[T_{\{0,1\}}, T_{\{1,2\}}]\|_{\rm op}^2 = 4$ on $64 \times 64$ 3-site Fock space), and Proposition 7.3 ($T=0$ free-fermion correlator $\frac{4}{9\pi^4}$ along the staircase ray $r_m = (m, m-1)$ at $m=2, d=3$ strictly exceeds $A_{\rm GC} q_{\rm GC}^3$).
     - Cross-check of all transcendental bounds with `mpmath.iv` at 50 decimal digits of precision (`mpmath.iv (50 dps) cross-check PASSED`).

2. **All-mutants verification (`12` guarded mathematical mutants, each required to exit `1`):**
   ```
   UV_OFFLINE=1 UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with mpmath python -B D:/dev/scratch/ceiling-20261118/ADIABATIC/PURESSH/replay.py --all-mutants
   ```
   - **Exit code:** `0` (`ALL 12 MATHEMATICAL MUTANTS REJECTED (each exited 1)`):
     1. `norm_tb_underestimate` (corrupts $\|T_b\|_{\rm op}$ from $2$ to $1$) $\to$ exit `1`
     2. `norm_ye_underestimate` (corrupts $\|Y_{e'}(\theta)\|_{\rm op}$ from $1$ to $1/2$) $\to$ exit `1`
     3. `wick_pairings_corrupted` (drops $2^{-r}$ in $(2r-1)!!/(2r)! = 1/(2^r r!)$) $\to$ exit `1`
     4. `exp_phys_factor_halved` (drops factor of $2$ in $\exp(2(\beta|t| + \beta g^2/K)) - 1$) $\to$ exit `1`
     5. `exp_taylor_bound_dropped` (replaces $e^x - 1 \le \frac{x}{1-x/2}$ by $x$) $\to$ exit `1`
     6. `degree_phys_underestimate` (corrupts $D_{\rm phys}^2 = 16$ to $4$) $\to$ exit `1`
     7. `degree_aug_underestimate` (corrupts $D_{\rm aug} = 6 \implies D_{\rm aug}^2 = 36$ to $16$) $\to$ exit `1`
     8. `euler_walk_exponent_halved` (corrupts Euler walk exponent $2|E|-1$ to $|E|-1$) $\to$ exit `1`
     9. `kp_vertex_weight_dropped` (drops vertex weight factor $e^{\sum_{v\in V_g} a(v)}$ in KP budget) $\to$ exit `1`
     10. `threshold_c0_doubled` (doubles threshold $c_0 = 2^{-10}$ to $2^{-9}$, violating $b_{\rm src} < 1$) $\to$ exit `1`
     11. `route_b_gap_assumed_positive` (asserts strictly positive singlet-odd gap $\Delta_{\rm odd}(C_4) > 0$) $\to$ exit `1`
     12. `route_c_commutator_assumed_zero` (asserts $[T_{\{0,1\}}, T_{\{1,2\}}] = 0$) $\to$ exit `1`

3. **Exact-diagonalization sanity check (`NUMERICAL`):**
   ```
   UV_OFFLINE=1 UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with numpy --with scipy python -B D:/dev/scratch/ceiling-20261118/ADIABATIC/PURESSH/ed_check.py
   ```
   - **Exit code:** `0` (`PURESSH ed_check.py: ALL NUMERICAL ED CHECKS PASSED`)

---

## Exact-Diagonalization Tables (`NUMERICAL`)

### Table 1: 2-Site Spinful Bond-SSH Dimer ($d = 1$, $\beta = K = 1$, Theorem 1.1 Bound $A_{\rm GC} q_{\rm GC}^1 = \frac{32}{103} \approx 0.310679612$)

| Parameter Point | $\Omega$ | $N_{\rm ph} = 30$ | $N_{\rm ph} = 60$ | $N_{\rm ph} = 90$ | $N_{\rm ph} = 120$ | $|N_{120} - N_{90}|$ | Theorem 1.1 Bound |
|---|---:|---:|---:|---:|---:|---:|---:|
| `joint_endpt` ($t = 2^{-11}, g^2 = 2^{-11}, \mu = 0$) | $0.2$ | `3.003547978e-05` | `3.053743933e-05` | `3.053992860e-05` | `3.053993787e-05` | `9.27e-12` | `3.106796117e-01` |
| `joint_endpt` ($t = 2^{-11}, g^2 = 2^{-11}, \mu = 0$) | $2.0$ | `3.053993790e-05` | `3.053993790e-05` | `3.053993790e-05` | `3.053993790e-05` | `1.37e-16` | `3.106796117e-01` |
| `joint_endpt` ($t = 2^{-11}, g^2 = 2^{-11}, \mu = 0$) | $20.0$ | `3.053993790e-05` | `3.053993790e-05` | `3.053993790e-05` | `3.053993790e-05` | `5.56e-19` | `3.106796117e-01` |
| `joint_mu0.5` ($t = 2^{-11}, g^2 = 2^{-11}, \mu = 0.5$) | $0.2$ | `2.654057094e-05` | `2.698412930e-05` | `2.698632895e-05` | `2.698633715e-05` | `8.19e-12` | `3.106796117e-01` |
| `joint_mu0.5` ($t = 2^{-11}, g^2 = 2^{-11}, \mu = 0.5$) | $2.0$ | `2.698633718e-05` | `2.698633718e-05` | `2.698633718e-05` | `2.698633718e-05` | `1.26e-16` | `3.106796117e-01` |
| `joint_mu0.5` ($t = 2^{-11}, g^2 = 2^{-11}, \mu = 0.5$) | $20.0$ | `2.698633718e-05` | `2.698633718e-05` | `2.698633718e-05` | `2.698633718e-05` | `8.57e-19` | `3.106796117e-01` |
| `pure_g_endpt` ($t = 0, g^2 = 2^{-10}, \mu = 0$) | $0.2$ | `6.005451551e-05` | `6.105995207e-05` | `6.106494594e-05` | `6.106496457e-05` | `1.86e-11` | `3.106796117e-01` |
| `pure_g_endpt` ($t = 0, g^2 = 2^{-10}, \mu = 0$) | $2.0$ | `6.106496463e-05` | `6.106496463e-05` | `6.106496463e-05` | `6.106496463e-05` | `4.73e-17` | `3.106796117e-01` |
| `pure_g_endpt` ($t = 0, g^2 = 2^{-10}, \mu = 0$) | $20.0$ | `6.106496463e-05` | `6.106496463e-05` | `6.106496463e-05` | `6.106496463e-05` | `5.54e-17` | `3.106796117e-01` |

### Table 2: 4-Site Spinful Bond-SSH Ring $C_4$ ($\beta = K = 1$, Total Phonon Cutoff $N_{\rm tot} = \sum_{b=1}^4 n_b \in \{2, 3, 4\}$)

| Parameter Point | $\Omega$ | $d$ | $N_{\rm tot} = 2$ | $N_{\rm tot} = 3$ | $N_{\rm tot} = 4$ | Theorem 1.1 Bound $A_{\rm GC} q_{\rm GC}^d$ |
|---|---:|---:|---:|---:|---:|---:|
| `pure_t_endpt` ($t = 2^{-10}, g = 0, \mu = 0$) | $3.0$ | $1$ | `5.960461e-08` | `5.960461e-08` | `5.960461e-08` | `3.106796e-01` |
| `pure_t_endpt` ($t = 2^{-10}, g = 0, \mu = 0$) | $3.0$ | $2$ | `1.578541e-18` | `1.353532e-18` | `1.110048e-19` | `2.915468e-02` |
| `joint_endpt` ($t = 2^{-11}, g^2 = 2^{-11}, \mu = 0$) | $3.0$ | $1$ | `2.960517e-05` | `3.042747e-05` | `3.052479e-05` | `3.106796e-01` |
| `joint_endpt` ($t = 2^{-11}, g^2 = 2^{-11}, \mu = 0$) | $3.0$ | $2$ | `7.067871e-10` | `6.760843e-10` | `6.693110e-10` | `2.915468e-02` |
| `joint_mu0.5` ($t = 2^{-11}, g^2 = 2^{-11}, \mu = 0.5$) | $3.0$ | $1$ | `2.616111e-05` | `2.688775e-05` | `2.697374e-05` | `3.106796e-01` |
| `joint_mu0.5` ($t = 2^{-11}, g^2 = 2^{-11}, \mu = 0.5$) | $3.0$ | $2$ | `9.562658e-10` | `9.822874e-10` | `9.853296e-10` | `2.915468e-02` |
| `joint_mu0.5` ($t = 2^{-11}, g^2 = 2^{-11}, \mu = 0.5$) | $20.0$ | $1$ | `2.698594e-05` | `2.698594e-05` | `2.698594e-05` | `3.106796e-01` |
| `joint_mu0.5` ($t = 2^{-11}, g^2 = 2^{-11}, \mu = 0.5$) | $20.0$ | $2$ | `4.940093e-09` | `4.940081e-09` | `4.940081e-09` | `2.915468e-02` |

---

## Explicit List of What Is Not Covered

1. **Large-hopping / Fermi-liquid regime ($\beta|t| > 2^{-10}$ at $U_{\rm eff} = 0$):** Theorems 1.1 and 1.2 require $\beta|t| + \beta g^2/K \le 2^{-10}$. As proved in Proposition 7.3, when $U_{\rm eff} = 0$, the free Fermi surface at $\beta|t| \to \infty$ produces algebraic $O(\|x-y\|_1^{-2})$ decay of the pair correlator along the staircase ray $y - x = (m, m-1)$ even at $g = 0$, so **no** $(\beta t)$-independent uniform exponential decay rate $(A, q)$ ($q < 1$) can hold under a $\beta g^2/K$-only hypothesis.
2. **BKT quasi-long-range order / divergent $\chi_{\rm pair}$ in 2D (and true ODLRO in $d \ge 3$) at $\beta|t| \gg 1$:** By the Hohenberg-Mermin-Wagner theorem, a continuous $U(1)$ symmetry in 2D cannot break spontaneously via true $T > 0$ ODLRO ($\lim_{\|x-y\|_1 \to \infty} |\langle \Delta_x^\dagger \Delta_y \rangle| > 0$); the physical 2D pairing transition is Berezinskii-Kosterlitz-Thouless (BKT) algebraic quasi-long-range order $|\langle \Delta_x^\dagger \Delta_y\rangle| \sim \|x-y\|_1^{-\eta(T)}$ with $\eta(T) \le 1/4 < 2$, characterized by a divergent $\ell^1$ pair susceptibility $\chi_{\rm pair}(\Lambda_L) = \sum_{y \in \Lambda_L} |\langle \Delta_x^\dagger \Delta_y\rangle_{\Lambda_L}| \to \infty$ as $L \to \infty$ (whereas the free-fermion $T \to 0$ limit in Proposition 7.3 has $\eta = 2$ and bounded $\sum_y |\langle \Delta_0^\dagger \Delta_y\rangle| \le 1/2$). Whether BKT quasi-LRO / divergent $\chi_{\rm pair}$ in 2D (or true non-decaying ODLRO in $d \ge 3$) is absent for all $k_B T \ge C g^2/K$ at arbitrary $\beta|t| \gg 1$ when $U_{\rm eff} = 0$ remains **OPEN**.
3. **Phonon-frequency ceiling $k_B T_{\rm pair} \le C(t, g^2/K)\,\Omega$ as $\Omega \downarrow 0$:** Theorems 1.1 and 1.2 provide a frequency-uniform ceiling $k_B T_{\rm pair} \le 2^{10}(|t| + g^2/K)$ valid for all $\Omega > 0$, not a bound vanishing linearly with $\Omega$ as $\Omega \downarrow 0$.
4. **Physical materials and experiments:** All statements are rigorous model-level theorems for the pure bond-SSH Hamiltonian on 2D square tori. No physical superconductor or experimental $T_c$ is claimed.

---

## SHA-256 Digests

- `ROUTE-SCREEN.md`: `2b8e6d1c3518ab332f407013953704708b1bd5686fba5de2a020b3a062267b55`
- `RIGOR.md`: `d04efa00eaa844e1cc1bdde4f8abe275f69daecfb2212b26ac2a25c6540adaa1`
- `replay.py`: `b7b447fc32ea08bd44395cf24d0c0bb986b46f7ea3549ab4e29e83ef67ae2a99`
- `ed_check.py`: `1b1f944f36227915550e89f50416f0f7ca314bc68dc1502b4626511474cfb700`
