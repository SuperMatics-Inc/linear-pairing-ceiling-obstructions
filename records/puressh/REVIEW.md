# Independent Review of `PURESSH`

**Reviewed directory:** `D:/dev/scratch/ceiling-20261118/ADIABATIC/PURESSH/` (`RESULT.md`, `ROUTE-SCREEN.md`, `RIGOR.md`, `replay.py`, `ed_check.py`)  
**Companion context:** `ADIABATIC/SSHBOUND3/` (Zenodo `10.5281/zenodo.24406987`)

---

## Executive Verdict

The core mathematical proofs in `RIGOR.md` for **Theorems 1.1 and 1.2** and **Propositions 7.2 and 7.3** are **mathematically sound (`PROVED`)**, and the exact rational/interval computations in `replay.py` (including all 12 mutants) and the numerical sanity checks in `ed_check.py` reproduce with exit code `0` (`CERTIFIED` / `NUMERICAL`).

However, **`RESULT.md` cannot be accepted as written** because it contains **two major factual/mathematical errors** that contradict `RIGOR.md` and `replay.py`:
1. **Theorem 1.2 in `RESULT.md` (`RESULT.md:40-42, 60, 75`):** Fabricates a canonical prefactor $A_{\rm c} := 2e\,\beta\xi_0\, b_{\rm src} = \frac{27e}{17216} < \frac{1}{200}$, which (i) contradicts `RIGOR.md` Theorem 1.2 (which proves the prefactor is $A_{\rm GC} = \frac{341}{103}$, ~777× larger), (ii) is falsely claimed to be certified in `replay.py`, and (iii) contains an arithmetic error ($2 \cdot 2^{-9} \cdot \frac{216}{269} = \frac{27}{8608}$, not $\frac{27}{17216}$, and $\frac{27e}{8608} \approx 0.008526 > \frac{1}{200}$).
2. **Proposition 7.3 in `RESULT.md` (`RESULT.md:13, 77`):** Misstates the separation as the odd diagonal $y - x = (2m-1, 2m-1)$ (where the exact $T=0, \mu=0$ correlator is **identically zero**), misstates the decay law as $\frac{4}{\pi^4(2m-1)^4}$ instead of $\frac{4}{\pi^4(2m-1)^2}$, and asserts the false inequality $\frac{4}{81\pi^4} \approx 5.07 \times 10^{-4} > A_{\rm GC} q_{\rm GC}^3 \approx 2.74 \times 10^{-3}$. `RIGOR.md` §7.3 and `replay.py` use the correct staircase ray $r_m = (m, m-1)$ and exact value $\frac{4}{9\pi^4} \approx 4.56 \times 10^{-3} > 2.74 \times 10^{-3}$ at $m = 2$ ($d = 3$).

Additionally, **Proposition 7.1** in `RIGOR.md` and `replay.py` proves $\Delta_{\rm eff} \le 0$ (comparing $N_{\rm odd}=0$ and $N_{\rm odd}=4$ in $S_z = 0$) but omits the $N_{\rm odd}=2$ and $S_z \ne 0$ sectors needed to prove the equality $\Delta_{\rm eff} = 0$. Our independent full-Fock diagonalization confirms $\Delta_{\rm eff} = 0$ holds across all $N=4$ sectors (and all $N$).

---

## Verdict Table by Claim

| Claim | Source | Verdict / Label | Notes |
|---|---|---|---|
| **Theorem 1.1** (GC exponential pair clustering $A_{\rm GC}=\frac{341}{103}$, $q_{\rm GC}=\frac{32}{341}$, susceptibility $R_{\rm max}=\frac{24718511}{9834543} < 3$, analyticity on $|\xi| < 2^{-9}\beta^{-1}$, uniform in $\Omega, \mu, L \ge 4$ for $\beta|t| + \beta g^2/K \le 2^{-10}$) | `RIGOR.md` §§2–5 | **PROVED** (`CERTIFIED` constants) | Line-by-line verified. Minor P3 proof-step sloppiness in Lemma 2.1 and rounding typo in `RIGOR.md:69`. `RESULT.md:32` misstates $Y_{e'}(\theta)$ (extra $\frac{1}{2}$) and pressure bound ($\le b_{\rm src}$ unproved in `RIGOR.md`). |
| **Theorem 1.2** (Thermodynamic canonical pair clustering with prefactor $A_{\rm GC} = \frac{341}{103}$, base $q_{\rm GC} = \frac{32}{341}$) | `RIGOR.md` §6 | **PROVED** (`CERTIFIED` boundary stiffness monotonicity) | Sound in `RIGOR.md` §6 (minor sign typo `- \mu N` in `RIGOR.md:444`). **`RESULT.md:40-42, 60, 75` REJECTED**: states wrong/unproved prefactor $A_{\rm c} = 27e/17216$ with arithmetic error and false certification claim. |
| **Proposition 7.1** (Route (b) obstruction: zero antiadiabatic instantaneous gap $\Delta_{\rm eff} = 0$ on $C_4$ at $N=4$) | `RIGOR.md` §7.1, `replay.py` | **PROVED** (with minor gap closed by independent check); `CERTIFIED` on $N_{\rm odd} \in \{0,4\}$ | Author proves $\Delta_{\rm eff} \le 0$ (sufficient to obstruct Route (b)); equality $\Delta_{\rm eff} = 0$ requires checking $N_{\rm odd}=2$ and $S_z \ne 0$, which we independently verified ($\lambda_{\max} = 10$ and $8 \le 12$). |
| **Proposition 7.2** (Route (c) obstruction: $\|[T_{\{x,y\}}, T_{\{y,z\}}]\|_{\rm op} = 2$, non-terminating BCH hierarchy diverging as $\Omega \downarrow 0$) | `RIGOR.md` §7.2, `replay.py` | **PROVED** (`CERTIFIED` norm) | Line-by-line verified and independently confirmed ($\|[T_{01}, T_{12}]\|_{\rm op} = 2$). |
| **Proposition 7.3** (Route (d) obstruction: $T=0, g=0, \mu=0$ staircase correlator $\frac{4}{\pi^4(2m-1)^2}$ violates any $(\beta t)$-independent $A q^d$) | `RIGOR.md` §7.3, `replay.py` | **PROVED** (`CERTIFIED` $m=2, d=3$ witness) | Sound in `RIGOR.md` §7.3 (minor P3 rounding typo in `RIGOR.md:574`). **`RESULT.md:13, 77` REJECTED**: wrong ray $(2m-1, 2m-1)$ (correlator $= 0$), wrong power $d^{-4}$, and false inequality $\frac{4}{81\pi^4} > A_{\rm GC} q_{\rm GC}^3$. |
| **Finite-cutoff ED sanity checks** (2-site dimer, $C_4$ ring) | `ed_check.py` | **NUMERICAL** | Reproduced with exit `0`; all reported numbers in `RESULT.md` Tables 1–2 match our rerun. |

---

## Numbered Findings

### Finding 1 (P0): `RESULT.md` Theorem 1.2 states a wrong, unproved canonical prefactor $A_{\rm c} = \frac{27e}{17216}$ with an arithmetic error and a false certification claim
- **Location:** `RESULT.md:40-42`, `RESULT.md:60`, `RESULT.md:75`
- **Details:** `RESULT.md` states Theorem 1.2 with canonical prefactor
  $$A_{\rm c} := 2e\,\beta\xi_0\, b_{\rm src} = 2e \cdot 2^{-9} \cdot \frac{216}{269} = \frac{27e}{17216} < \frac{1}{200} \approx 0.00426308,$$
  and claims in `RESULT.md:75` that `replay.py` gives "Exact rational certification of ... $A_{\rm c} = \frac{27e}{17216} < \frac{1}{200}$."
  1. `RIGOR.md` Theorem 1.2 (`RIGOR.md:97-99`, `RIGOR.md:458-466`) proves the canonical bound with prefactor $A_{\rm GC} = \frac{341}{103} \approx 3.3107$, **not** $A_{\rm c} \approx 0.00426$. Neither `RIGOR.md` nor `replay.py` defines or certifies $A_{\rm c}$.
  2. The arithmetic in `RESULT.md:42` is wrong: $2 \cdot 2^{-9} \cdot \frac{216}{269} = \frac{27}{8608}$ (not $\frac{27}{17216}$), and $\frac{27e}{8608} \approx 0.0085262 > \frac{1}{200} = 0.005$.
  3. The comparison table (`RESULT.md:60`) also attributes an unproved $A_{\rm c} = \frac{6567075 e}{543650940928}$ to `SSHBOUND3`, whereas `SSHBOUND3/RIGOR.md` Theorem 1.2 likewise proves the canonical prefactor is $A_{\rm GC} = \frac{1965840}{475579}$.
- **Fix:** Replace $A_{\rm c}$ in `RESULT.md:40-42, 60` with $A_{\rm GC} = \frac{341}{103}$ (and $\frac{1965840}{475579}$ for `SSHBOUND3`), and remove the false `A_c` certification claim from `RESULT.md:75`.

### Finding 2 (P1): `RESULT.md` Proposition 7.3 misstates the lattice ray, the algebraic exponent, and the numerical witness inequality
- **Location:** `RESULT.md:13`, `RESULT.md:77`
- **Details:** `RESULT.md:13` claims that at $T=0, g=0, \mu=0$, the pair correlator at "odd diagonal separation $y - x = (2m-1, 2m-1)$ equals $\frac{4}{\pi^4(2m-1)^4}$ and decays only algebraically as $\|x-y\|_1^{-4}$." `RESULT.md:77` further claims `replay.py` certifies that "$\frac{4}{81\pi^4}$ at $d=3$ strictly exceeds $A_{\rm GC} q_{\rm GC}^3$."
  1. Along the diagonal $r = (n, n)$ ($n \ge 1$), the exact $T=0$ Green's function is $G_\infty(n, n) \propto \sin(n\pi) = 0$, so the pair correlator at $y - x = (2m-1, 2m-1)$ is **identically zero**, not $\frac{4}{\pi^4(2m-1)^4}$.
  2. `RIGOR.md` §7.3 correctly uses the **staircase ray** $r_m = (m, m-1)$ ($d = 2m-1$), where $G_\infty(m, m-1) = \frac{(-1)^{m-1} 2}{\pi^2(2m-1)}$ and $\langle \Delta_0^\dagger \Delta_{r_m}\rangle = \frac{4}{\pi^4(2m-1)^2} = \frac{4}{\pi^4 d^2}$.
  3. The claimed witness inequality $\frac{4}{81\pi^4} > A_{\rm GC} q_{\rm GC}^3$ is **false**: $\frac{4}{81\pi^4} \approx 5.0696 \times 10^{-4} < 2.7359 \times 10^{-3} \approx A_{\rm GC} q_{\rm GC}^3$. `replay.py` actually certifies the correct staircase witness $\frac{4}{9\pi^4} \approx 4.5627 \times 10^{-3} > 2.7359 \times 10^{-3}$ at $m = 2, d = 3$.
- **Fix:** Update `RESULT.md:13` and `RESULT.md:77` to match `RIGOR.md` §7.3 and `replay.py`: staircase ray $r_m = (m, m-1)$, correlator $\frac{4}{\pi^4(2m-1)^2}$, and $m=2, d=3$ witness $\frac{4}{9\pi^4} \approx 4.563 \times 10^{-3} > A_{\rm GC} q_{\rm GC}^3 \approx 2.736 \times 10^{-3}$.

### Finding 3 (P1): `RESULT.md` Theorem 1.1(3) misstates the source operator $Y_{e'}(\theta)$ and cites an unproved bound on $|p_{\Lambda_L}(\xi) - p_{\Lambda_L}(0)|$
- **Location:** `RESULT.md:32`
- **Details:** `RESULT.md:32` writes $V_{\rm src}(\xi) = -\xi Y_{e'}(\theta)$ with $Y_{e'}(\theta) = \frac{1}{2}(e^{i\theta}\Delta_x^\dagger \Delta_y + e^{-i\theta}\Delta_y^\dagger \Delta_x)$ and claims $|p_{\Lambda_L}(\xi) - p_{\Lambda_L}(0)| \le b_{\rm src} = \frac{216}{269}$.
  1. `RIGOR.md:41` defines $Y_{e'}(\theta) := e^{i\theta}\Delta_x^\dagger \Delta_{x+r} + e^{-i\theta}\Delta_{x+r}^\dagger \Delta_x$ (no $\frac{1}{2}$ factor) and $V_{\rm src}(\xi) := -\xi \sum_{e' \in \mathcal{E}_{\rm src}} Y_{e'}(\theta)$ (translation-invariant sum over all $L^2$ source edges, not a single two-site source). With the $\frac{1}{2}$ factor, $\|Y_{e'}(\theta)\|_{\rm op}$ would be $\frac{1}{2}$ rather than $1$, contradicting Lemma 4.1 and `replay.py`.
  2. `RIGOR.md:394` proves $|p_{\Lambda_L}(\xi) - p_{\Lambda_L}(0)| \le -2\log(1 - b_{\rm src}/e) < 2$, not $\le b_{\rm src}$ (while $-2\log(1 - b_{\rm src}/e) \approx 0.70024 < 0.80297 = b_{\rm src}$ happens to be true numerically, `RIGOR.md` never derives or states the bound $\le b_{\rm src}$).
- **Fix:** Align `RESULT.md:32` with `RIGOR.md:41, 86, 394` (remove $\frac{1}{2}$, restore the sum over $\mathcal{E}_{\rm src}$, and state the proved bound $-2\log(1 - b_{\rm src}/e) < 2$ and quadratic Taylor bound from `RIGOR.md:86`).

### Finding 4 (P2): Proposition 7.1 proves $\Delta_{\rm eff} \le 0$ rather than $\Delta_{\rm eff} = 0$ because $N_{\rm odd}=2$ and $S_z \ne 0$ sectors are omitted
- **Location:** `RIGOR.md:481-505`, `replay.py:488-535`
- **Details:** Proposition 7.1(4) asserts $\min\operatorname{spec}(H_{\rm eff}^{\rm inst}|_{N=4, N_{\rm odd}>0}) = -6 g^2/K$ and hence $\Delta_{\rm eff} = 0$. However, both the proof in `RIGOR.md` §7.1 and the matrix check in `replay.py` only diagonalize $\Sigma_4$ on $\{N_\uparrow=2, N_\downarrow=2, N_{\rm odd}=0\}$ (dim 6) and $\{N_\uparrow=2, N_\downarrow=2, N_{\rm odd}=4\}$ (dim 6). They never check the 24-dimensional $\{N_\uparrow=2, N_\downarrow=2, N_{\rm odd}=2\}$ sector or the $S_z \ne 0$ sectors at $N=4$. Without checking those sectors, one has only proved $\Delta_{\rm eff} \le 0$ (which still obstructs a positive gap, so the Route (b) obstruction stands). Our independent full-Fock diagonalization below confirms $\lambda_{\max} = 10$ on $(2,2, N_{\rm odd}=2)$ and $\lambda_{\max} \le 8$ on $S_z \ne 0$, so $\Delta_{\rm eff} = 0$ is indeed true.
- **Fix:** Add the $N_{\rm odd}=2$ and $S_z \ne 0$ sectors of $N=4$ to `replay.py` and note their upper bound $\le 12$ in `RIGOR.md` §7.1.

### Finding 5 (P2): Open-question framing in `RESULT.md` and `RIGOR.md` conflates 2D BKT quasi-LRO with true ODLRO
- **Location:** `RESULT.md:130`, `RIGOR.md:580`
- **Details:** Both files state as **OPEN**: "whether non-decaying off-diagonal long-range order ($\lim_{|x-y|\to\infty} |\langle \Delta_x^\dagger \Delta_y \rangle| > 0$) is absent for $k_B T \ge C g^2/K$ at arbitrary $\beta|t|$." On the 2D square lattice at $T > 0$, continuous $U(1)$ symmetry cannot be spontaneously broken (Hohenberg-Mermin-Wagner theorem), so $\lim_{|x-y|\to\infty} |\langle \Delta_x^\dagger \Delta_y\rangle| = 0$ already holds at every $T > 0$. The genuinely open physical/mathematical question in 2D is the absence of **BKT algebraic quasi-long-range order / divergent pair susceptibility** ($\chi_{\rm pair} = \infty$, or $|\langle \Delta_x^\dagger \Delta_y\rangle| \sim |x-y|^{-\eta}$ with $\eta \le 1/4$) above $k_B T \ge C g^2/K$ at arbitrary $\beta|t|$ (or true ODLRO in $d \ge 3$).
- **Fix:** Restate the open question accurately for 2D (absence of BKT quasi-LRO / divergent pair susceptibility) and note that true ODLRO at $T > 0$ is the $d \ge 3$ question.

### Finding 6 (P3): Minor proof/notational typos in `RIGOR.md`
- **Location:** `RIGOR.md:69`, `RIGOR.md:133-137`, `RIGOR.md:444`, `RIGOR.md:574`
- **Details:**
  1. `RIGOR.md:69`: Decimal approximation of $R_{\rm max} = \frac{24718511}{9834543}$ is written `2.5134375842`; the exact value is `2.5134376859...` (seventh digit is `6`, not `5`; `RESULT.md:31,58` has the correct `2.51343769`).
  2. `RIGOR.md:133-137` (Lemma 2.1): Deduces $\sum_b 2|g|\|X_b\Psi\| \le \varepsilon \|H_{\rm ph}\Psi\| + \frac{2|\mathcal{E}|g^2}{\varepsilon K}\|\Psi\|$ via a pointwise inequality on $2|g||x_b|$ and $\langle \Psi, H_{\rm ph,b} H_{\rm ph,b'}\Psi\rangle \ge 0$, skipping Cauchy-Schwarz: $\sum_b \|X_b\Psi\| \le \sqrt{|\mathcal{E}|}(\sum_b \|X_b\Psi\|^2)^{1/2} \le \sqrt{\frac{2|\mathcal{E}|}{K}\langle \Psi, H_{\rm ph}\Psi\rangle}$, followed by AM-GM on $\sqrt{\|\Psi\|\|H_{\rm ph}\Psi\|}$, which yields the exact stated bound cleanly.
  3. `RIGOR.md:444` (Proof of Theorem 1.2): Defines $Z_{\Lambda_L, N}(\xi) := \operatorname{Tr}_{\mathcal{H}_{\Lambda_L, N}}(e^{-\beta(H_{\Lambda_L}(\xi) - \mu N)})$. Since $H_{\Lambda_L}(\xi)$ already contains $-\mu N$, this should be $H_{\Lambda_L}(\xi) + \mu N$ (i.e., $H_{\Lambda_L}(\xi)|_{\mu=0}$) so that $\widehat{Z}_{\Lambda_L}(\xi;\mu) = \sum_N e^{\beta\mu N} \widehat{Z}_{\Lambda_L, N}(\xi)$ in line 456 holds.
  4. `RIGOR.md:574`: Prints $\frac{4}{9\pi^4} \approx 4.5647 \times 10^{-3}$ and $A_{\rm GC} q_{\rm GC}^3 \approx 2.7361 \times 10^{-3}$; exact values are `4.562659e-3` and `2.735924e-3`.

---

## Line-by-Line Audit Notes

### 1. Theorem 1.1 Expansion (`RIGOR.md` §§2–5)
- **Reference $D_0 = -\mu N$:** Exact cancellation of $z_0^{|S_E|} = (1 + e^{\beta\mu})^{2|S_E|}$ in Lemma 4.2 via multilinear Schatten-Hölder with $p_j = \beta/\Delta_j$ ($\sum 1/p_j = 1$) is completely rigorous and eliminates the $(5/4)^{|S_E|}$ site overhead of `SSHBOUND3`.
- **Phonon Gaussian integral & $\Omega$-uniformity (Lemmas 3.1–3.2, Prop 5.2):**
  - $C_\beta(\tau) = \frac{\Omega}{2K}\frac{\cosh((\beta/2-\tau)\Omega)}{\sinh(\beta\Omega/2)} > 0$ satisfies $\int_0^\beta C_\beta(\tau)\,d\tau = \frac{1}{K}$ identically for all $\Omega > 0$, with smooth classical limit $C_\beta(\tau) \to \frac{1}{\beta K}$ as $\Omega \downarrow 0$ and antiadiabatic limit $C_\beta(\tau) \to \frac{1}{K}\delta_{\rm per}(\tau)$ as $\Omega \to \infty$.
  - For $2r_b$ visits to a single bond $b$, the Wick sum $W_{2r_b}(v_1, \dots, v_{2r_b}) = \sum_{\pi \in \mathcal{P}_2(2r_b)} \prod_{\{a,c\}\in\pi} C_\beta(|v_a - v_c|)$ is strictly positive and permutation-symmetric. Since the electronic Schatten-Hölder bound $\prod_b (2|t|)^{m_b}(2|g|)^{2r_b} \prod_{e'} |\xi|^{p_{e'}}$ is independent of insertion times and ordering, the multinomial simplex-to-hypercube identity factors the ordered-time integral identically across edges, giving $\frac{(2\beta|t|)^{m_b}}{m_b!} \cdot \frac{(2|g|)^{2r_b}}{(2r_b)!} \frac{(2r_b)!}{2^{r_b} r_b!} (\frac{\beta}{K})^{r_b} = \frac{(2\beta|t|)^{m_b}}{m_b!} \frac{(2\beta g^2/K)^{r_b}}{r_b!}$. Summing over $m_b + r_b \ge 1$ yields $\exp(2\beta|t| + 2\beta g^2/K) - 1$ per physical edge uniformly in $\Omega > 0$.
- **Polymer convergence & susceptibility (Lemmas 5.3–5.4, Proof of Thm 1.1):**
  - Euler-tour bound $D_G^{2k}$ (Lemma 5.3) and Kotecký-Preiss support-deletion induction (Lemma 5.4, using $1/(1-1/e) < e$) are completely sound.
  - Exact rational constants verified independently: $\varepsilon_{\rm phys} = \varepsilon_{\rm src} = \frac{2}{1023}$, $q_{\rm GC} = 48 \cdot \frac{2}{1023} = \frac{32}{341}$, $A_{\rm GC} = \frac{3}{1-q_{\rm GC}} = \frac{341}{103}$, $b_{\rm GC} = \frac{32}{103} < 1$, $R_{\rm max} = 1 + \frac{4 A_{\rm GC} q_{\rm GC}}{(1-q_{\rm GC})^2} = \frac{24718511}{9834543} \approx 2.5134376859 < 3$, $q_{\rm src} = 108 \cdot \frac{2}{1023} = \frac{72}{341}$, $b_{\rm src} = \frac{216}{269} < 1$, $-2\log(1 - b_{\rm src}/e) \approx 0.700243 < 2$.

### 2. Theorem 1.2 Canonical Transfer (`RIGOR.md` §6)
- Lemma 6.1 (boundary spring-constant bracket $K \to K/2, 2K$ via $2|g||X_b| \le \frac{K}{4} X_b^2 + \frac{4g^2}{K}$ and min-max monotonicity in fixed-$N$ and fixed-$(N_\uparrow, N_\downarrow)$ sectors) is completely rigorous and independent of $U_{\rm eff}$.
- Superadditivity up to $O(b^{-1})|\Lambda_L|$, Legendre duality, existence of a supporting $\mu$ for interior densities $n \in (0,2)$ (and spin-balanced $a \in (0,1)$), convexity of $\xi \mapsto L_j^{-2}\log\widehat{Z}_{\Lambda_{L_j}, N_j}(\xi)$, and the $\xi \downarrow 0$ limit after $L_j \to \infty$ cleanly transfer the grand-canonical bound with prefactor $A_{\rm GC} = \frac{341}{103}$ and base $q_{\rm GC} = \frac{32}{341}$ (see Finding 1 regarding `RESULT.md`'s erroneous $A_{\rm c}$).

---

## Rerun Verification Table

All commands were executed with `UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with mpmath --with numpy --with scipy python -B`:

| Command | Exit Code | Key Output / Status |
|---|---:|---|
| `replay.py` | `0` | `ALL EXACT RATIONAL AND OUTWARD INTERVAL CHECKS PASSED`; `mpmath.iv (50 dps) cross-check PASSED` |
| `replay.py --all-mutants` | `0` | `ALL 12 MATHEMATICAL MUTANTS REJECTED (each exited 1)` |
| `ed_check.py` | `0` | `ALL NUMERICAL ED CHECKS PASSED`; all dimer and $C_4$ values match `RESULT.md` Tables 1–2 |
| `sha256sum` on `ROUTE-SCREEN.md`, `RIGOR.md`, `replay.py`, `ed_check.py` | `0` | All 4 digests match `RESULT.md` exactly |

---

## Independent Computations (Propositions 7.1–7.3)

### 1. Independent Full-Fock Diagonalization of $\Sigma_4 = \sum_{b \in \mathcal{E}_{C_4}} T_b^2$ (Proposition 7.1)
We independently constructed the $256 \times 256$ operator $\Sigma_4$ on $C_4$ and verified $\|[\Sigma_4, N_{\rm odd}]\|_{\max} = 0$. Across all $N = 4$ sectors:

| $(N_\uparrow, N_\downarrow)$ | $N_{\rm odd}$ | $\dim$ | $\lambda_{\min}$ | $\lambda_{\max}$ | Exact Spectrum (with multiplicities) |
|---|---:|---:|---:|---:|---|
| $(2, 2)$ | $0$ | $6$ | $0$ | **$12$** | $0(\times 1),\, 4(\times 3),\, 8(\times 1),\, 12(\times 1)$ |
| $(2, 2)$ | $2$ | $24$ | $2$ | **$10$** | $2(\times 4),\, 4(\times 8),\, 6(\times 8),\, 10(\times 4)$ |
| $(2, 2)$ | $4$ | $6$ | $0$ | **$12$** | $0(\times 1),\, 4(\times 3),\, 8(\times 1),\, 12(\times 1)$ |
| $(1, 3), (3, 1)$ | $2$ | $12$ | $2$ | $6$ | $2(\times 4),\, 4(\times 4),\, 6(\times 4)$ |
| $(1, 3), (3, 1)$ | $4$ | $4$ | $0$ | $8$ | $0(\times 1),\, 4(\times 2),\, 8(\times 1)$ |
| $(0, 4), (4, 0)$ | $4$ | $1$ | $0$ | $0$ | $0(\times 1)$ |

Globally at $N=4$ (and also across all $N \in \{0,\dots,8\}$), $\max(\Sigma_4|_{N_{\rm odd}=0}) = \max(\Sigma_4|_{N_{\rm odd}>0}) = 12$, confirming $\Delta_{\rm eff} = 0$.

### 2. Independent 3-Site Commutator Norm (Proposition 7.2)
On the 64-dimensional 3-site Fock space, singular value decomposition of $[T_{\{0,1\}}, T_{\{1,2\}}]$ gives unique singular values $\{0, 1, 2\}$, confirming $\|[T_{\{0,1\}}, T_{\{1,2\}}]\|_{\rm op} = 2.000000000000$.

### 3. Independent Exact Free-Fermion $T=0, g=0, \mu=0$ Pair Correlator (Proposition 7.3)
Using the exact diamond Fermi-sea integral $G_\infty(r_x, r_y) = \frac{1}{2\pi^2} \frac{2\sin((r_x+r_y)\pi/2)}{r_x+r_y} \frac{2\sin((r_x-r_y)\pi/2)}{r_x-r_y}$ (cross-checked against a $512 \times 512$ Brillouin-zone sum at $\beta t = 200$):

**Staircase ray $r_m = (m, m-1)$, $d = 2m - 1$ (`RIGOR.md` §7.3 — exact correlator $\frac{4}{\pi^4(2m-1)^2}$):**

| $m$ | $r_m$ | $d$ | Exact $G_\infty(r_m)^2$ | $L=512, \beta t=200$ | $A_{\rm GC} q_{\rm GC}^d$ | Exceeds? |
|---:|---|---:|---:|---:|---:|---|
| $1$ | $(1, 0)$ | $1$ | `4.106393e-02` | `4.106223e-02` | `3.106796e-01` | No |
| **$2$** | **$(2, 1)$** | **$3$** | **`4.562659e-03`** | **`4.561303e-03`** | **`2.735924e-03`** | **Yes (smallest $m$)** |
| $3$ | $(3, 2)$ | $5$ | `1.642557e-03` | `1.641308e-03` | `2.409324e-05` | Yes |
| $4$ | $(4, 3)$ | $7$ | `8.380394e-04` | `8.368617e-04` | `2.121712e-07` | Yes |
| $5$ | $(5, 4)$ | $9$ | `5.069621e-04` | `5.058383e-04` | `1.868433e-09` | Yes |

**Odd diagonal ray $r_m = (2m-1, 2m-1)$, $d = 4m - 2$ (misstated in `RESULT.md:13`):**
For every $n \ge 1$, $r = (n, n)$ has $r_x + r_y = 2n$, so $\sin(n\pi) = 0 \implies G_\infty(n, n) = 0$ identically; the pair correlator is **$0$** for all $m \ge 1$. (And for the erroneous formula $\frac{4}{\pi^4(2m-1)^4}$ in `RESULT.md:13, 77`, it fails at $m=2, d=3$ where `5.069621e-04 < 2.735924e-03`, and would only exceed $A_{\rm GC} q_{\rm GC}^{2m-1}$ at $m=3, d=5$: `6.570229e-05 > 2.409324e-05`.)

---

## Significance Assessment and Publication Recommendation

1. **Is Theorem 1.1 more than standard high-temperature clustering?**
   - In the electronic hopping parameter $\beta|t| \le 2^{-10}$, Theorem 1.1 **is** standard high-temperature lattice-fermion clustering.
   - In the electron-phonon coupling $\beta g^2/K \le 2^{-10}$, it is **genuinely non-trivial** because $X_b$ is unbounded with thermal variance diverging as both $\Omega \to \infty$ and $\Omega \downarrow 0$; achieving an $\Omega$-uniform bound (including canonical transfer with unbounded boundary SSH hopping) requires the exact Gaussian Wick covariance identity $\int_0^\beta C_\beta = 1/K$ and the $K \to K/2, 2K$ boundary spring-constant bracket. However, both of those technical ingredients were already introduced in `SSHBOUND3`.
2. **What it adds to `SSHBOUND3`:**
   - Closes the $U_{\rm eff} = 0$ endpoint that `SSHBOUND3` left open (where $2^{27} t^2/U_{\rm eff} \to \infty$).
   - Dramatically simplifies the proof at $U_{\rm eff} = 0$ (no SOS absorption, no atomic-ratio overhead), tightening the $t=0$ ceiling by $8\times$ ($2^{10} g^2/K$ vs. $2^{13} g^2/K$) and sharpening $A_{\rm GC}, R_{\rm max}$.
   - Most valuably, Propositions 7.1–7.3 give a clean, rigorous **obstruction map** showing why neither an antiadiabatic gap, nor a bond Lang-Firsov transformation, nor any $(\beta t)$-independent cluster expansion can produce uniform exponential pair clustering at $U_{\rm eff} = 0$.
3. **Publication recommendation:**
   - **Do not** submit as a standalone full-length journal paper (Theorem 1.1 is high-temperature in $|t|$ and reuses the core bosonic machinery of `SSHBOUND3`).
   - **Recommended:** After fixing Findings 1–5, incorporate `PURESSH` either as a **new section / appendix in an `SSHBOUND3` v2 update** (closing its explicitly stated $U_{\rm eff} = 0$ open problem and improving $t = 0$ by $8\times$), or as a **concise barriers/companion note** highlighting the $U_{\rm eff} = 0$ high-$T$ theorem together with the three proved route obstructions (Propositions 7.1–7.3) and the properly framed 2D BKT / 3D ODLRO open problem.
