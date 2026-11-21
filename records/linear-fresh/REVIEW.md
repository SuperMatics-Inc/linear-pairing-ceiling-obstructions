# Independent Review of LINEAR-FRESH

- **Reviewed files:** `D:/dev/scratch/ceiling-20261118/MASSIVE/LINEAR-FRESH/{RESULT.md,RIGOR.md,replay.py,independent.py,CHECKS.txt,replay.stdout.txt,independent.stdout.txt,mutants.stdout.txt}`
- **Overall Verdict:** **PASS** (0 P0, 0 P1, 0 P2; 5 non-blocking P3 remarks)
- **Target status:** Confirmed **OPEN** — no linear-in-$\Omega$ pairing ceiling is proved, and no existing LINEAR4 / STAGE7R ceiling is improved.
- **Recommended destination:** **Barriers-note section** (grouped with `STATIC-MODE` and `PURESSH` method obstructions), **not** a standalone preprint.

---

## 1. Per-claim adjudication

| # | Claim & location | Verdict | Allowed label | Verification summary |
|---|---|---|---|---|
| 1 | **Theorem 2.1 — Exact interacting nonzero-Matsubara phonon $f$-sum bound** (`RIGOR.md:30-96`, `RESULT.md:19-35`): $0 \le C_x(i\nu_k) \le U_x \Omega_x^2 / \nu_k^2$, $\mathbb{E}\|b_{x,k}\|^2 \le U_x \Omega_x^2/(4\pi^2 k^2 \tau)$, $\sum_{k\ge 1}\mathbb{E}\|b_{x,k}\|^2 \le U_x \Omega_x^2/(24\tau)$ (and $1/12$ for $k\neq 0$), without oscillator truncation. | **PASS** | **PROVED** | Double commutator $[b_x,[H,b_x]] = F_x^2/M_x = U_x\Omega_x^2$, Lehmann representation (2.4), sum rule (2.5), Basel sum, and infinitesimal form-boundedness of $-F_x X_x Q_x$ all verified line by line. Standard/classical sum rule (see §5). |
| 2 | **Theorem 3.1 — Positive-determinant arbitrary Green amplification** (`RIGOR.md:98-166`, `RESULT.md:37-49`): On 1 impurity + 1 bath with $\beta=2$, $b=\mp B$ on $(0,1)$ and $(1,2)$, $U=U_2 U_1$ has positive eigenvalues, $\det(I+U)>1$ (in fact $\ge 4$), $\|G(1,0)_{00}\| \sim B^2/(2v^2) \to \infty$ via exact (3.3) and lower bound (3.4), persisting under smooth periodic finite-action approximations. | **PASS** | **PROVED** | SPD similarity $U \sim U_1^{1/2}U_2 U_1^{1/2}$, off-diagonal cancellation in $U_1^{-1}+U_2$, exact formula (3.3), strict lower bound (3.4), and $L^1$-Gronwall continuity to smooth periodic histories all verified. |
| 3 | **Fixed two-slice interval witness ($B=6, v=1/2$)** (`RIGOR.md:168-178`, `replay.py:282-346`, `independent.py:92-135`): $\det(I+U) > 15$ and $\|G(1,0)_{00}\| > 52.89$ ($\approx 52.8957540935\ldots$). | **PASS** | **CERTIFIED** | Exact closed-form expression evaluated with outward-rounded Arb (80 dps) and independently in `mpmath.iv` (60 dps); also reproduced independently at 50 dps (`det(I+U) = 15.7903...`, `|G00| = 52.89575409...`). Minor P3: `replay.py:345` asserts `> 30` instead of `> 52.89`. |
| 4 | **Exact finite-matrix Ward-Schur algebra** (`RIGOR.md:180-232`, `RESULT.md:53`): Half-space norm bound (4.1), $0 \le Q \le \tilde{Q}$, Schur-Ward identities (4.2), pathwise leakage bound (4.3) with sharp $\alpha=1$ threshold, and row-sum identity (4.4) with factor $2$. | **PASS** | **PROVED** | All finite-matrix identities and inequalities verified algebraically and tested adversarially on non-diagonal $D_\pm > 0$ at $\alpha=0.95$. Minor P3: (4.4) implicitly restricts $D_\pm$ to diagonal positive matrices. |
| 5 | **Hankel moment bound (5.2), uniform-damping bound (5.4), and auxiliary series enclosure (5.3)** (`RIGOR.md:260-302`, `RESULT.md:56`, `replay.py:446-459`, `independent.py:155-162`): $\mathbb{E}\alpha \le \frac{U\Omega^2}{4\pi^4\tau^3} S$, $S \le C_{\text{aux}} \in (67/50, 27/20)$ with tail $[5/2+\ln(2K)]/(4K^2)$. | **PASS** | **PROVED** (5.2, 5.4, tail) / **CERTIFIED** ($C_{\text{aux}}$ enclosure) | Partial fractions, monotone integral upper bound for $H_{\text{odd}}(k)$ and the omitted tail $\int_K^\infty [1+\frac{1}{2}\ln(2x)]/x^3\,dx = [5/2+\ln(2K)]/(4K^2)$ verified exactly. Outward-rounded Arb ($K=200$), `mpmath.iv` ($K=300$), and independent `mpmath.iv` ($K=1000$) all certify $67/50 < C_{\text{aux}} < 27/20$. Explicitly disclaimed as not a ceiling coefficient. |
| 6 | **Dimer COM decoupling & static BO pair admixture** (`RIGOR.md:304-332`, `RESULT.md:54-55`): Shifted COM oscillator decouples at fixed $N$; relaxed BO minima $q=\pm 2\sqrt{U^2-t^2}$ ($U>t>0$) give bare pair expectation $t^2/(4U^2)$ ($1/64$ at $U=4,t=1$, vs $1/68$ at unrelaxed $q=2U$). | **PASS** | **PROVED** | Square completion, $3\times 3$ characteristic polynomial, BO minimization, exact ground eigenvector, and rational evaluations all verified. |
| 7 | **Free Einstein covariance & route disposition** (`RIGOR.md:342-362`, `RESULT.md:58-70`): $\langle X_q X_{-q}\rangle_{\text{free}} = \frac{\Omega}{2K}\coth(\beta\Omega/2)$ is $q$-independent; ordinary canonical RP obstruction credited to LINEAR5; linear step remains open. | **PASS** | **PROVED** (free covariance) | Exact under unitary Fourier normalization; prior LINEAR5 credit and non-overclaim boundaries are accurate. |
| 8 | **Infinite-grid DMFT kernel (5.1), truncated dimer ED, Krylov/Matsubara fixtures, and 10-step Bethe-DMFT scan** (`RIGOR.md:236-248, 333-340`, `RESULT.md:72-80`, `replay.py:67-116, 157-207, 217-276, 480-613`): Preserves earlier $T/\Omega=0.10$ failure (`1.4212687734...`). | **PASS** | **[INFERENCE]** (5.1) / **NUMERICAL** (ED & DMFT) | Appropriately scoped and labeled by the author; no unverified promotion to a theorem or thermodynamic $T_{\text{pair}}$ claim. |

---

## 2. Findings (P0–P3)

No P0, P1, or P2 defects were found. All five findings below are non-blocking P3 items:

1. **[P3] Assertion threshold mismatch on the Arb witness (`replay.py:345` vs `RIGOR.md:173`, `independent.py:130`).**
   `RIGOR.md:173` states that both the Arb replay and `mpmath.iv` replay give `|G(1,0)_{00}| > 52.89`, whereas `replay.py:345` only asserts `require(G00_abs > arb(30), ...)` (while `independent.py:130` asserts `g00_abs.a > mp.mpf("52.89")`, and the Arb enclosure `[52.8957540935... +/- 9.66e-77]` is only printed when running the mutant in `mutants.stdout.txt:13`). Tightening `arb(30)` to `arb("52.89")` in `replay.py:345` aligns the Arb guard with the text.
2. **[P3] Draft-to-final code/comment drift and unreachable mutant guard (`replay.py:217-276, 282, 354, 435-467`; `independent.py:137, 165`).**
   `replay.py` and `independent.py` retain theorem numbers (`Proposition 4.2`, `Theorem 4.3`, `Theorem 4.4(1)`) and three fixtures (4-site Krylov/total-positivity check, low-energy damping window lemma, and density-blind supremum) from an earlier draft of `RIGOR.md` that no longer appear in the final `RIGOR.md` or `RESULT.md`. Additionally, `replay.py:249` (`require(abs(J0[0, 1] - J0[1, 0]) < 1e-12, ...)`) is unreachable dead code because `route_c_krylov_negative_eig` already fails at `replay.py:247`. None of these cause overclaiming in `RIGOR.md`/`RESULT.md`, and the extra checks are mathematically true.
3. **[P3] Implicit diagonal hypothesis on $D_\pm$ in eq. (4.4) (`RIGOR.md:184, 223-228`).**
   Lines 184–221 treat $D_+, D_- > 0$ as general positive-definite Hermitian matrices (under which (4.1)–(4.3) hold), while lines 223–228 write `Pos_n = sum_m |(G_++)_{nm}|^2 D_{+,m}` and `Neg_n = sum_m |(G_+-)_{nm}|^2 D_{-,m}`, which requires $D_+, D_-$ to be diagonal. Adding "When $D_\pm = \mathrm{diag}(D_{\pm,m})$ are diagonal" before (4.4) makes the hypothesis explicit.
4. **[P3] Imprecise core phrasing in the unbounded-oscillator justification (`RIGOR.md:85`).**
   Line 85 writes "Spectral sums in (2.4)-(2.5) can be exhausted on this core" (referring to finite-particle oscillator vectors). Strictly, the interacting eigenstates $\psi_a$ of $H$ are not finite-particle oscillator vectors; rather, infinitesimal form-boundedness gives $D(H^{1/2}) = D(N_{\text{osc}}^{1/2})$ and $b_x \psi_a \in D(H^{1/2})$ for every eigenstate $\psi_a$, which directly justifies $\langle \psi_a | [b_x, [H, b_x]] | \psi_a \rangle = 2 \sum_b (E_b - E_a) |(b_x)_{ab}|^2$ via Parseval and monotone convergence of the nonnegative summands.
5. **[P3] Minimal `CHECKS.txt` log (`CHECKS.txt:1-3`).**
   `CHECKS.txt` records only the three exit-code lines (`replay_exit=0`, `independent_exit=0`, `mutant_driver_exit=0`) without the executed commands themselves (which are instead documented in `RESULT.md:111-120`).

---

## 3. Rerun of `CHECKS.txt` / `RESULT.md` commands

All commands were rerun locally with `OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1`, `UV_OFFLINE=1`, `UV_CACHE_DIR=D:/dev/.cache/uv`, and temporary logs under `C:/t/LinearFreshReview` (deleted at closure). No author files were modified.

| Check | Command | Exit code | Result |
|---|---|---|---|
| `replay_exit` (`CHECKS.txt:1`) | `uv run --no-project --with numpy --with scipy --with sympy --with mpmath --with python-flint python -B replay.py` | **0** | Printed `LINEAR-FRESH replay: ALL FIXTURE CHECKS PASSED; NO PAIRING CEILING CERTIFIED`; matches `replay.stdout.txt` (excluding initial `uv` package-install banner). |
| `independent_exit` (`CHECKS.txt:2`) | `uv run --no-project --with numpy --with scipy --with sympy --with mpmath --with python-flint python -B independent.py` | **0** | Printed `LINEAR-FRESH independent.py (SymPy + mpmath.iv): ALL INDEPENDENT CHECKS PASSED`; identical to `independent.stdout.txt`. |
| `mutant_driver_exit` (`CHECKS.txt:3`) | Python subprocess driver enumerating all 16 entries of `replay.MUTANTS` and running `python -B replay.py --mutant NAME` | **0** (each of 16 mutants exited **1**) | `diff -u mutants.stdout.txt C:/t/LinearFreshReview/mutants_driver.stdout.txt` exited **0** (byte-for-byte identical). |
| Additional `--all-mutants` check | `uv run --no-project --with numpy --with scipy --with sympy --with mpmath --with python-flint python -B replay.py --all-mutants` | **0** | All 16 guarded mutants rejected cleanly. |

---

## 4. Independent adversarial checks

A standalone script (`C:/t/LinearFreshReview/adv_check.py`, not importing `replay.py` or `independent.py`, deleted after execution) exited **0** and independently checked five targets from scratch:

1. **Theorem 2.1 ($f$-sum rule & Matsubara bound via direct time-domain quadrature):**
   On a fresh 2-site Hubbard-Holstein system with Hubbard repulsion $U_{\text{Hub}}=2.3$, asymmetric hoppings/potentials, non-unit oscillator parameters $(K_1, M_1, F_1) = (3.2, 1.7, 2.1)$ ($U_1\Omega_1^2 = F_1^2/M_1 = 2.594117647059$), and a nonlinear bounded coupling operator $Q_1 = n_1 - \frac{1}{2} + 0.3 n_{1\uparrow}n_{1\downarrow}$ at $\beta = 4.0$:
   - Truncation convergence of the $f$-sum rule: $|f\text{-sum} - U_1\Omega_1^2| = 2.859\times 10^{-2}$ at $N_{\text{ph}}=6$, $6.832\times 10^{-10}$ at $N_{\text{ph}}=16$, and $1.688\times 10^{-14}$ at $N_{\text{ph}}=36$ (confirming both the boundary anomaly at small $N_{\text{ph}}$ and exact convergence to $U_1\Omega_1^2$).
   - Direct `scipy.integrate.quad` time-domain Fourier transform of $\mathrm{Tr}(e^{-(\beta-u)H} b_1 e^{-u H} b_1)/Z$ matched the Lehmann formula (2.4) to $< 10^{-11}$ (imaginary part $< 10^{-14}$) and obeyed $0 \le C_1(i\nu_k) \le U_1\Omega_1^2/\nu_k^2$ at $k=1,2,5$ (ratios $0.6455, 0.8642, 0.9718$).
2. **Theorem 3.1 (high-precision asymptotics & explicit $C^\infty$ periodic finite-action history):**
   - In 50-digit `mpmath`, direct matrix exponentials $U_1 = e^{-h_1}, U_2 = e^{-h_2}$ matched the closed-form scalar formula (3.3) to $< 10^{-35}$ and strictly exceeded the lower bound (3.4) across $v \in \{0.5, 1.3\}$ and $B \in \{2, 6, 15, 30\}$ (e.g., at $v=0.5, B=30$: $\det(I+U) = 1.206\times 10^{10}$, $|G(1,0)_{00}| = 1786.553874 > \text{lb}(3.4) = 1785.062326$, approaching $B^2/(2v^2) = 1800$). (Note: at $B=30$, naive float64 `scipy.linalg.expm`/`inv` loses accuracy due to $e^{30} \sim 10^{13}$, underscoring why exact/interval arithmetic is needed.)
   - Explicit $C^\infty$ 2-periodic smoothing $b_\epsilon(u) = -6\tanh(\sin(\pi u)/\epsilon)$ with $\epsilon = 0.01$ at $v=0.5$, integrated with 4000 Magnus midpoint steps, gave positive monodromy eigenvalues $\{13.71386749, 0.07291889\}$, $\det(I+U) = 15.786786 > 15$, $|G(1,0)_{00}| = 51.527145$, and finite oscillator Euclidean action $S_{\text{ph}} = 1.508\times 10^6$ (at $U=1, \Omega=0.1$).
3. **Section 4 (Ward-Schur algebra with non-diagonal $D_\pm > 0$):**
   On a random $6\times 6$ block system with non-diagonal SPD $D_+, D_-$ and complex non-Toeplitz $V$ scaled to $\alpha = 0.95$, all of (4.1)–(4.3) held to $< 10^{-11}$.
4. **Section 5 ($C_{\text{aux}}$ at independent cutoff $K = 1000$):**
   In 50-digit `mpmath.iv`, $C_{\text{aux}} \in [1.347813685631956, 1.347816210857571] \subset (67/50, 27/20) = (1.34, 1.35)$ (and $S \approx 1.298173 < C_{\text{aux}}$).
5. **Section 6.2 (fresh static dimer BO minimum):**
   At $(U, t) = (3.7, 1.1)$, direct diagonalization at $q_{\min} = 2\sqrt{U^2 - t^2} = 7.065409$ gave $c_0 c_1 = 0.022096420745 = t^2/(4U^2)$ to $< 10^{-14}$.

---

## 5. Novelty, significance, and recommended destination

- **Theorem 2.1 ($f$-sum bound):** **Standard / classical.** The identity $\langle [b_x, [H, b_x]] \rangle = F_x^2/M_x = U_x\Omega_x^2$ and the resulting spectral bound $0 \le C_x(i\nu_k) \le U_x\Omega_x^2/\nu_k^2$ are the textbook oscillator $f$-sum (Placzek first-moment) rule applied to coordinate-coupled phonons. Recording it here is a clean orientation check showing that electronic determinant tilting cannot destroy the free high-frequency second-moment scale, but it is not a novel theorem.
- **Theorem 3.1 (positive-determinant arbitrary Green amplification):** **Genuinely new companion obstruction relative to `BARRIERS`, `LIMITS`, and `STATIC-MODE`.**
  - `BARRIERS` (Zenodo `10.5281/zenodo.24384373`, LINEAR7) constructs a determinant *zero* ($\det(I+U_v)=0$) on $K_{1,3}$ to obstruct unrestricted per-history normalized propagator bounds.
  - `LIMITS` (Zenodo `10.5281/zenodo.24385569`, LINEAR8–11) analyzes annealed $\det^2$-weighted defect-insertion estimates and shows why they do not localize or imply clustering.
  - `STATIC-MODE` (`../STATIC-MODE/`) integrates out the dynamic Gaussian first around a strictly positive static reference and exhibits a fixed-hopping three-site resonance whose exact first integrated dynamic cumulant still scales as $\Theta(U\Omega^2/\tau^3)$.
  - `LINEAR-FRESH` Theorem 3.1 closes a distinct loophole: even on a 1-impurity + 1-bath system with strictly positive monodromy eigenvalues and $\det(I+U) \ge 4$ (diverging exponentially with $B$), the conditional imaginary-time Green's function $|G(1,0)_{00}| \sim B^2/(2v^2)$ grows without bound along smooth finite-action histories. Thus determinant positivity/nonvanishing alone cannot yield a history-independent CAR/Gram bound on $G$.
- **Sections 4–6 (Ward-Schur algebra, $C_{\text{aux}}$, static dimer):** Clean, elementary supporting algebra and diagnostic anchors; none is a standalone theorem.
- **Recommended destination:** **Fold into a barriers-note section** (alongside `STATIC-MODE` and `PURESSH` obstructions). Theorem 3.1 is short, sharp, and genuinely complementary to `BARRIERS` and `STATIC-MODE`, whereas the full package does not have the weight of a standalone preprint and leaves the linear-in-$\Omega$ pairing ceiling open.
