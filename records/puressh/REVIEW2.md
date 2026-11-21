# Independent Follow-Up Review (`REVIEW2`) of `PURESSH` Fixes (`F1`–`F6`)

**Reviewed directory:** `D:/dev/scratch/ceiling-20261118/ADIABATIC/PURESSH/`
**Reviewed artifacts:** `FIX.md`, `RESULT.md`, `RIGOR.md`, `ROUTE-SCREEN.md`, `replay.py`, `ed_check.py` (with `RESULT.v1.md` and `REVIEW.md` preserved untouched).
**Verification environment:** `UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with mpmath --with numpy --with scipy python -B` (temp under `C:/t/PureSshReview2`, removed on exit).

---

## 1. Executive Verdict

All **six** findings from `REVIEW.md` (`F1`–`F6`) are **RESOLVED** in the mathematical proofs (`RIGOR.md`), exact verifier (`replay.py`), and main theorem/obstruction statements of `RESULT.md`. Every core claim in `PURESSH` is now **`PROVED`** (with all finite rational/interval/integer checks **`CERTIFIED`** and `ed_check.py` **`NUMERICAL`**).

However, inspecting the revised `RESULT.md`, `RIGOR.md`, `ROUTE-SCREEN.md`, and `FIX.md` surfaced **one newly introduced P2 typo** in the `RESULT.md` comparison table (line 54), **one leftover P2 inaccuracy** in the `SSHBOUND3` column of that table (line 60), and **two minor P3 prose inaccuracies** ("7 invariant sectors" instead of 9 individual / 6 spin-flip-paired classes; two misdescribed F6 line items in `FIX.md`). None of these affect any theorem, proof, or certified bound.

---

## 2. Final Claim-by-Claim Verdict Table

| Claim | Location | Final Label | Notes |
|---|---|---|---|
| **Theorem 1.1** (Grand-canonical exponential clustering $A_{\rm GC}=\frac{341}{103}$, $q_{\rm GC}=\frac{32}{341}$, $\chi_{\rm pair} \le R_{\rm max}=\frac{24718511}{9834543} < 3$, analyticity on $\|\xi\| < 2^{-9}\beta^{-1}$ with $\|p(\xi)-p(0)\| \le -2\log(1-b_{\rm src}/e) < 0.7012 < 2$) | `RIGOR.md` §§1–5, `RESULT.md` §Thm 1.1 | **PROVED** | Consistent across `RIGOR.md`, `RESULT.md`, and `replay.py` (minor comparison-table typo at `RESULT.md:54`, see New Defect N1). |
| **Theorem 1.2** (Thermodynamic canonical exponential clustering with prefactor $A_{\rm GC}=\frac{341}{103}$ and base $q_{\rm GC}=\frac{32}{341}$) | `RIGOR.md` §6, `RESULT.md` §Thm 1.2 | **PROVED** | Fabricated $A_{\rm c} = \frac{27e}{17216}$ removed; `RESULT.md` now matches `RIGOR.md` verbatim. |
| **Proposition 7.1** (Route (b) obstruction: $H_{\rm eff}^{\rm inst}$ on $C_4$ at $N=4$ has $\Delta_{\rm eff} = 0$) | `RIGOR.md` §7.1, `replay.py` | **PROVED** + **CERTIFIED** | All 9 $(N_\uparrow,N_\downarrow,N_{\rm odd})$ sectors (total $\dim = 70 = \binom{8}{4}$) verified with zero inter-sector leakage and exact integer minimal polynomials; $\lambda_{\max} = 12$ on both $N_{\rm odd}=0$ and $N_{\rm odd}=4$ ($S^z=0$), and $\lambda_{\max} \le 10$ on all other sectors. |
| **Proposition 7.2** (Route (c) obstruction: $\|[T_b, T_{b'}]\|_{\rm op} = 2$ and $\Omega \downarrow 0$ BCH divergence) | `RIGOR.md` §7.2, `replay.py` | **PROVED** + **CERTIFIED** | Unchanged; remains exact. |
| **Proposition 7.3** (Route (d) obstruction: exact $T=0, g=0, \mu=0$ staircase correlator $\frac{4}{\pi^4(2m-1)^2}$, exceeding $A_{\rm GC} q_{\rm GC}^d$ at $m=2, d=3$) | `RIGOR.md` §7.3, `RESULT.md` §Verdict/§Verification, `replay.py` | **PROVED** + **CERTIFIED** | `RESULT.md` now matches `RIGOR.md` and `replay.py` verbatim ($\frac{4}{9\pi^4} \approx 4.5627\times 10^{-3} > 2.7359\times 10^{-3}$). |
| **Exact rational/interval/integer checks + 12 mutants** | `replay.py` | **CERTIFIED** | Exit `0` on base run (`mpmath.iv` 50 dps cross-check PASSED) and exit `0` on `--all-mutants` (all 12 mutants exit `1`). |
| **Finite-cutoff ED sanity checks** (2-site dimer & $C_4$ ring) | `ed_check.py` | **NUMERICAL** | Exit `0` (`ALL NUMERICAL ED CHECKS PASSED`). |

---

## 3. Finding-by-Finding Resolution Audit (`F1`–`F6`)

| ID | Original Issue (`REVIEW.md`) | Status | Verification Evidence |
|---|---|---|---|
| **F1 (P0)** | `RESULT.v1.md` fabricated canonical prefactor $A_{\rm c} = \frac{27e}{17216}$ and falsely claimed `replay.py` certified it. | **RESOLVED** | `RESULT.md:40-44, 60, 75` now state the proved canonical prefactor $A_{\rm GC} = \frac{341}{103} \approx 3.31067961$ with base $q_{\rm GC} = \frac{32}{341}$ matching `RIGOR.md` Theorem 1.2 verbatim; $A_{\rm c}$ and its false certification claim are gone. (Note: the `SSHBOUND3` column of `RESULT.md:60` still has a leftover error — see New Defect N2.) |
| **F2 (P1)** | `RESULT.v1.md` misstated Prop 7.3 ray as $(2m-1, 2m-1)$ with decay $\frac{4}{\pi^4(2m-1)^4}$ and false inequality $\frac{4}{81\pi^4} > A_{\rm GC} q_{\rm GC}^3$. | **RESOLVED** | `RESULT.md:13, 77, 139` now state the exact staircase ray $r_m = (m, m-1)$ ($d = 2m-1$), exact decay $\frac{4}{\pi^4(2m-1)^2}$, and exact $m=2, d=3$ witness $\frac{4}{9\pi^4} \approx 4.5627\times 10^{-3} > A_{\rm GC} q_{\rm GC}^3 \approx 2.7359\times 10^{-3}$, matching `RIGOR.md` §7.3 and `replay.py`. |
| **F3 (P1)** | `RESULT.v1.md:32` added a spurious factor $\frac{1}{2}$ to $Y_{e'}(\theta)$, omitted $\sum_{e' \in \mathcal{E}_{\rm src}}$, and wrote $\|p(\xi)-p(0)\| \le b_{\rm src}$. | **RESOLVED** | `RESULT.md:32` now gives the exact translation-summed source $V_{\rm src}(\xi) = -\xi \sum_{e' \in \mathcal{E}_{\rm src}} Y_{e'}(\theta)$ with $Y_{e'}(\theta) = e^{i\theta}\Delta_x^\dagger\Delta_{x+r} + e^{-i\theta}\Delta_{x+r}^\dagger\Delta_x$ and the proved bound $\|p_{\Lambda_L}(\xi) - p_{\Lambda_L}(0)\| \le -2\log(1 - b_{\rm src}/e) < 0.7012 < 2$, matching `RIGOR.md` Thm 1.1(3) and `replay.py`. |
| **F4 (P2)** | Prop 7.1 only checked $N_{\rm odd} \in \{0, 4\}$ in $S^z = 0$ on $C_4$ ($\dim = 12$ of $70$), leaving $N_{\rm odd}=2$ and $S^z \ne 0$ unchecked. | **RESOLVED** | `RIGOR.md:505-512` and `replay.py:482-538` now exhaustively verify all 9 $(N_\uparrow, N_\downarrow, N_{\rm odd})$ sectors totaling $\binom{8}{4} = 70$ states (block-diagonal invariance, exact integer minimal polynomials, and non-redundancy of $\lambda_{\max}$). See §4 below for the complete audit and minor "7 vs. 9/6" prose count note (New Defect N3). |
| **F5 (P2)** | `RESULT.v1.md:130` & `RIGOR.md:580` framed the 2D $T>0$ open problem as absence of true ODLRO, overlooking Hohenberg-Mermin-Wagner. | **RESOLVED** | `RESULT.md:140`, `RIGOR.md:587`, and `ROUTE-SCREEN.md:136` now explicitly distinguish 2D BKT algebraic quasi-LRO ($\eta \le 1/4 < 2$, divergent $\chi_{\rm pair}$) from $d \ge 3$ true ODLRO, citing Hohenberg-Mermin-Wagner. |
| **F6 (P3)** | Four minor typos in `RIGOR.md`: decimal rounding on $R_{\rm max}$ (`2.5134375842`) and $\frac{4}{9\pi^4}$ (`4.5647e-3`), skipped Cauchy-Schwarz step in Lemma 2.1, and sign typo $H_{\Lambda_L}(\xi) - \mu N$ at line 444. | **RESOLVED** | All four items are cleanly corrected in `RIGOR.md` (`R_max \approx 2.5134376859`, `\frac{4}{9\pi^4} \approx 4.5627\times 10^{-3} > 2.7359\times 10^{-3}`, Cauchy-Schwarz step added in Lemma 2.1, and $H_{\Lambda_L}(\xi) + \mu N$ in the Proof of Thm 1.2). (See New Defect N4 for a minor inaccuracy in `FIX.md`'s prose summary of F6.) |

---

## 4. Audit of the $C_4$ Half-Filling ($N=4$) Sector Decomposition

`replay.py:482-492` constructs and checks all **9** individual $(N_\uparrow, N_\downarrow, N_{\rm odd})$ sectors of $\mathcal{F}_{\rm el}(C_4)|_{N=4}$:

| $(N_\uparrow, N_\downarrow, N_{\rm odd})$ | $S^z$ | $\dim$ | Exact $\operatorname{spec}(\Sigma_4)$ roots (min. poly) | $\lambda_{\max}(\Sigma_4)$ | $E_{\min}(H_{\rm eff}^{\rm inst})$ |
|---|---:|---:|---|---:|---:|
| $(2, 2, 0)$ | $0$ | $6$ | $\{0, 4, 8, 12\}$ | $12$ | $-6g^2/K$ |
| $(2, 2, 4)$ | $0$ | $6$ | $\{0, 4, 8, 12\}$ | $12$ | $-6g^2/K$ |
| $(2, 2, 2)$ | $0$ | $24$ | $\{2, 4, 6, 10\}$ | $10$ | $-5g^2/K$ |
| $(3, 1, 4)$ | $+1$ | $4$ | $\{0, 4, 8\}$ | $8$ | $-4g^2/K$ |
| $(1, 3, 4)$ | $-1$ | $4$ | $\{0, 4, 8\}$ | $8$ | $-4g^2/K$ |
| $(3, 1, 2)$ | $+1$ | $12$ | $\{2, 4, 6\}$ | $6$ | $-3g^2/K$ |
| $(1, 3, 2)$ | $-1$ | $12$ | $\{2, 4, 6\}$ | $6$ | $-3g^2/K$ |
| $(4, 0, 4)$ | $+2$ | $1$ | $\{0\}$ | $0$ | $0$ |
| $(0, 4, 4)$ | $-2$ | $1$ | $\{0\}$ | $0$ | $0$ |
| **Total** | | **$70 = \binom{8}{4}$** | | **$\max = 12$** | **$\Delta_{\rm eff} = 0$** |

- **Exactness and completeness:** Every dimension, minimal polynomial, maximum eigenvalue, and block-invariance check matches our independent full-Fock diagonalization in `REVIEW.md`. The spin-flip-grouped dimension sum $6 + 6 + 24 + 8 + 24 + 2 = 70 = \binom{8}{4}$ is exact and complete, and both $\{N_{\rm odd}=0, S^z=0\}$ and $\{N_{\rm odd}=4, S^z=0\}$ reach $\lambda_{\max} = 12$, proving $\Delta_{\rm eff}(C_4) = 0$.
- **Terminology note:** Grouping spin-flip pairs $(S^z, -S^z)$ yields **6** classes (and ungrouped gives **9** $(N_\uparrow, N_\downarrow, N_{\rm odd})$ sectors), not **7** — see New Defect N3 below.

---

## 5. New / Remaining Defects Identified

1. **N1 — P2 (Newly introduced in fix; `RESULT.md:54`):**
   In the Comparison Table row `Source edge activity \varepsilon_{\rm src}`, `RESULT.md:54` now reads:
   > `$e^{2\beta|\xi|} - 1 \le \frac{2}{1023}$ at $\beta|\xi| \le 2^{-10}$ (and $b_{\rm src} = \frac{216}{269} < 1$ on $\{|\xi| < \xi_0 = 2^{-9}\beta^{-1}\}$)`
   This is internally inconsistent and contradicts `RIGOR.md:62, 315, 326`, `replay.py:345`, and even `RESULT.v1.md:54` (which was correct!). Because $\|Y_{e'}(\theta)\|_{\rm op} = 1$, the source edge activity is **$e^{\beta|\xi|} - 1 \le \frac{2}{1023}$ at $\beta|\xi| \le 2^{-9}$**, which is why $b_{\rm src} = \frac{216}{269} < 1$ holds on the disk $\{|\xi| < \xi_0 = 2^{-9}\beta^{-1}\}$. (At $\beta|\xi| = 2^{-9}$, $e^{2\beta|\xi|} - 1 = e^{2^{-8}} - 1 \approx \frac{4}{1023}$, not $\frac{2}{1023}$.)
   **Fix:** Restore `RESULT.md:54` to `$e^{\beta|\xi|} - 1 \le \frac{2}{1023}$ at $\beta|\xi| \le 2^{-9}$ (giving $b_{\rm src} = \frac{216}{269} < 1$ on $\{|\xi| < \xi_0 = 2^{-9}\beta^{-1}\}$)`.

2. **N2 — P2 (Leftover from v1; `RESULT.md:60`):**
   In the Comparison Table row `Canonical prefactor (Theorem 1.2)`, the `PURESSH` column was fixed to $A_{\rm GC} = \frac{341}{103}$, but the `SSHBOUND3` column still reads:
   > `$\frac{6567075 e}{543650940928} \approx 3.2836 \times 10^{-5}$ (via Cauchy disk derivative bound)`
   In fact, `SSHBOUND3/RIGOR.md:76-86` (Theorem 1.2) proves the thermodynamic canonical bound with prefactor $A_{\rm GC} = \frac{1965840}{475579} \approx 4.13357192$ via the same single-bond derivative $\partial_\xi p_{\Lambda_M}(0)$ (not a Cauchy disk derivative bound).
   **Fix:** Change the `SSHBOUND3` cell in `RESULT.md:60` to `$A_{\rm GC} = \frac{1965840}{475579} \approx 4.13357192$ (via single-bond derivative $\partial_\xi p_{\Lambda_M}(0)$)`.

3. **N3 — P3 (Newly introduced prose miscount; `RESULT.md:77`, `RIGOR.md:579`, `ROUTE-SCREEN.md:72`, `FIX.md:29`):**
   All four files refer to "all **7** invariant sectors" of $C_4$ at $N=4$ while listing **6** spin-flip-paired classes ($6 + 6 + 24 + 8 + 24 + 2 = 70$) and while `replay.py:482-492` verifies **9** individual $(N_\uparrow, N_\downarrow, N_{\rm odd})$ sectors ($6 + 6 + 24 + 4 + 4 + 12 + 12 + 1 + 1 = 70$).
   **Fix:** Replace "all 7 invariant sectors" with "all 9 $(N_\uparrow, N_\downarrow, N_{\rm odd})$ invariant sectors (6 spin-flip-conjugate classes)".

4. **N4 — P3 (`FIX.md:49-50`):**
   `FIX.md`'s summary of F6 misdescribes two of its own edits: line 49 cites Lemma 6.1 (`Z_{\mathrm{ph},1}(K/2)` vs `Z_{\mathrm{ph},1}(2K)` — Lemma 6.1 was already correct; the actual fix was `H_{\Lambda_L}(\xi) - \mu N \to H_{\Lambda_L}(\xi) + \mu N` in the Proof of Theorem 1.2), and line 50 cites `5.0695 -> 5.0696` (the actual fix in `RIGOR.md` was `4.5647 -> 4.5627` and `2.7361 -> 2.7359` for $\frac{4}{9\pi^4}$ and $A_{\rm GC} q_{\rm GC}^3$). The actual `RIGOR.md` edits themselves are completely accurate.

---

## 6. Rerun Verification Table and SHA-256 Confirmation

| Command | Exit Code | Key Output |
|---|---:|---|
| `UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with mpmath --with numpy --with scipy python -B D:/dev/scratch/ceiling-20261118/ADIABATIC/PURESSH/replay.py` | `0` | `ALL EXACT RATIONAL AND OUTWARD INTERVAL CHECKS PASSED`; `mpmath.iv (50 dps) cross-check PASSED` |
| `UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with mpmath --with numpy --with scipy python -B D:/dev/scratch/ceiling-20261118/ADIABATIC/PURESSH/replay.py --all-mutants` | `0` | `ALL 12 MATHEMATICAL MUTANTS REJECTED (each exited 1)` |
| `UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with mpmath --with numpy --with scipy python -B D:/dev/scratch/ceiling-20261118/ADIABATIC/PURESSH/ed_check.py` | `0` | `ALL NUMERICAL ED CHECKS PASSED` |

All four SHA-256 digests reported in `RESULT.md` and `FIX.md` match the files on disk:
- `ROUTE-SCREEN.md`: `49cd8efb87e8c977bb30420cf3404980bd34b38c57ecedd17aa4cf3de19695d3`
- `RIGOR.md`: `5e3989ca98eb847f01def3d7c5ade8d9192f28d0c3f96592cf042963b7715fc8`
- `replay.py`: `b7b447fc32ea08bd44395cf24d0c0bb986b46f7ea3549ab4e29e83ef67ae2a99`
- `ed_check.py`: `1b1f944f36227915550e89f50416f0f7ca314bc68dc1502b4626511474cfb700`
