# Independent Pre-Release Review of `BARRIERS2-PAPER`

- **Reviewed artifacts:** `D:/dev/scratch/ceiling-20261118/MASSIVE/BARRIERS2-PAPER/{main.tex,main.pdf,refs.bib,CLAIMS.md,BUILD.md}`
- **Verified against sources:**
  - `MASSIVE/STATIC-MODE/{RIGOR.md,RESULT.md,REVIEW.md}` (PASS)
  - `MASSIVE/LINEAR-FRESH/{RIGOR.md,RESULT.md,REVIEW.md}` (PASS)
  - `ADIABATIC/PURESSH/{RIGOR.md,RESULT.md,FIX.md,REVIEW.md,REVIEW2.md}` (PASS; `REVIEW2.md` N1–N4 resolved in `FIX.md` §4)
  - `ADIABATIC/SSHBOUND3-PAPER/main.tex`, `MASSIVE/CAPSTONE-PAPER/refs.bib`
- **Overall Verdict:** **`PASS-WITH-FIXES`** (0 P0, 3 P1, 4 P2, 5 P3)

All numbered theorem, lemma, corollary, and obstruction **statements** in `main.tex` match their reviewed `RIGOR.md` sources faithfully (hypotheses, constants, domains, and scope), including `thm:canon` ($k_B T_{\mathrm{pair}} \le 1024(|t| + G_{\mathrm{b}})$), which is a **PROVED** theorem in `PURESSH/RIGOR.md` (Theorem 1.2) rather than an extrapolation. The Tectonic build is completely clean (0 overfull/underfull boxes, 0 undefined references, 0 warnings), all publication rules pass (0 em/en dashes, required non-peer-reviewed sentence, AI disclosure, byline/ORCID, no internal leaks), all 7 bibliography DOIs and titles match the released Zenodo records, and the prose is clear and journal-grade.

Three P1 defects (one typo in a matrix inequality in `rem:ward`, one inaccurate condensed proof summary in `thm:canon`, and stale `PENDING REVIEW2` tags in `CLAIMS.md`) plus four P2 defects should be corrected before public release. None requires re-proving any result or changing any main theorem statement.

---

## 1. Per-Claim Verification Table

| Paper item (`main.tex` lines) | Source record & statement | Match? | Allowed label | Notes |
|---|---|---|---|---|
| `def:tpair` (`203–216`) | `PURESSH/RIGOR.md:95–104`; `STATIC-MODE/RIGOR.md:5–18` | Exact | Definition | Model quantity only; no measured $T_c$. |
| `lem:first` (`305–351`) | `STATIC-MODE/RIGOR.md:69–100` eq. (6) | Exact | **PROVED** | Exact first dynamic cumulant $a_x(W)$, sign, spin factor, and zero-frequency cancellation verified. |
| `lem:aux` (`352–392`) | `STATIC-MODE/RIGOR.md:40–64, 103–118` eqs. (4), (5), (7), (8) | Exact | **PROVED** | $q(a)\le a^2/12$, $a_x \le U\Omega^2\beta^3/48$, $a_x \le d_x t^2 U\Omega^2\beta^5/1440$, static Combes-Thomas $(25/16)e^{-2\alpha d}$. |
| `thm:witness` (`404–464`) | `STATIC-MODE/RIGOR.md:20–24, 123–157` eq. (1) | Exact | **PROVED** + **CERTIFIED** constants | $a_{\mathrm{left}}(W) \ge U\Omega^2/(1200\tau^3)$ via $1/1148 > 1/1200$ on $0 < \Omega \le \tau \le t/4$; independently re-derived and spot-checked. |
| `thm:torus` (`465–507`) | `STATIC-MODE/RIGOR.md:26–30, 159–172` eq. (2) | Exact | **PROVED** + **CERTIFIED** constant | $a_{(0,0)}(W_B) \ge U\Omega^2/(2400\tau^3)$ on every square torus $L \ge 4$ for $B \ge B_0$; independently verified at $L=4, B=10^5$. |
| `cor:scale` (`508–526`) | `STATIC-MODE/RIGOR.md:32–38` eq. (3) | Exact | **PROVED** | $a_{(0,0)}(W_B) \ge U/(2400 C^3 \Omega)$ at $\tau = C\Omega$, $C \ge 1$, $\Omega \le t/(4C)$; within factor $50$ of `lem:aux`(i). |
| `rem:class`, `rem:notclass` (`529–558`) | `STATIC-MODE/RIGOR.md:175–189` | Exact | **PROVED** (scoped obstruction) | Accurately scopes obstruction to unresummed static-reference expansions; no annealed or $T_{\mathrm{pair}}$ overclaim. |
| `lem:fsum` (`575–623`) | `LINEAR-FRESH/RIGOR.md:28–96` Thm 2.1 | Exact | **PROVED** (classical) | Explicitly presented as a classical oscillator $f$-sum lemma; incorporates `LINEAR-FRESH/REVIEW.md` P3 note 4 (`D(H^{1/2})=D(N_{\mathrm{osc}}^{1/2})`). |
| `thm:amp` (`638–691`) | `LINEAR-FRESH/RIGOR.md:97–165` Thm 3.1 | Exact | **PROVED** | $\det(1+U)>1$, positive monodromy eigenvalues, $|\mathcal{G}(1,0)_{00}| \sim B^2/(2v^2)$; exact closed form `eq:Gclosed` and lower bound `eq:Glower` verified. |
| `rem:smooth` (`692–707`) | `LINEAR-FRESH/RIGOR.md:166–170` | Exact (minor P3 symbol) | **PROVED** | Smooth finite-action continuity via Gronwall; minor `b` vs `\varepsilon` notation slip (Finding 8). |
| `cor:fixture` (`709–723`) | `LINEAR-FRESH/RIGOR.md:172–181` | Exact | **CERTIFIED** | $B=6, v=1/2$: $\det(1+U) = 15.790282\ldots > 15$, $|\mathcal{G}(1,0)_{00}| = 52.8957540935\ldots > 52.89$; independently verified in 60-digit `mpmath.iv`. |
| `rem:ward` (`727–772`) | `LINEAR-FRESH/RIGOR.md:183–233, 257–264` | **1 P1 typo** (`743`) | **PROVED** (after P1 fix) + **CERTIFIED** ($C_{\mathrm{aux}}$) | `main.tex:743` prints $V A_-^{-1} V^*$ instead of $V D_-^{-1} V^*$ (Finding 1). Remainder of algebra and $67/50 < C_{\mathrm{aux}} < 27/20$ verified. |
| `rem:dimer` (`774–801`) | `LINEAR-FRESH/RIGOR.md:303–335` | Exact (minor P3 symbol) | **PROVED** | COM shift and bare pair expectation $t^2/(4U^2)$ ($1/64$ vs $1/68$ at $U=4, t=1$) verified; minor lowercase `g` reuse (Finding 9). |
| `thm:gc` (`836–909`) | `PURESSH/RIGOR.md:48–93, 145–406` Thm 1.1 | Statement exact; **P2 proof summary** (`880–883`) | **PROVED** + **CERTIFIED** constants | Statement and all exact rationals ($c_0=2^{-10}$, $\varepsilon=2/1023$, $q_{\mathrm{GC}}=32/341$, $A_{\mathrm{GC}}=341/103$, $b_{\mathrm{GC}}=32/103$, $R_{\max}=24718511/9834543<3$, $q_{\mathrm{src}}=72/341$, $b_{\mathrm{src}}=216/269$) verified. Proof summary step (2) misstates Schatten-Hölder + Wick covariance integral as "Cauchy-Schwarz degeneracy bounds" (Finding 4). |
| `thm:canon` (`910–941`) | `PURESSH/RIGOR.md:95–104, 411–471` Thm 1.2 | Statement exact; **P1 proof summary** (`928–935`) | **PROVED** | Statement $k_B T_{\mathrm{pair}} \le 1024(|t|+G_{\mathrm{b}})$ matches `PURESSH/RIGOR.md` Thm 1.2 verbatim (PROVED, not an extrapolation) and legitimately closes the $U_{\mathrm{eff}}\to 0$ divergence of `sshbond3`. Proof summary incorrectly cites "single-bond activity" and "2D isoperimetric inequality $|\partial S|\ge\sqrt{|S|}$" (Finding 2). |
| `thm:routes` (`955–1051`) | `PURESSH/RIGOR.md:106–113, 476–570` Thm 1.3 & Props 7.1–7.3 | Exact | **PROVED** + **CERTIFIED** | All 3 obstructions verified: (i) $C_4$ $N=4$ all 9 invariant sectors (6 spin-flip classes, 70 states), $\Delta_{\mathrm{eff}}=0$; (ii) $\|[T_b, T_{b'}]\|_{\mathrm{op}}=2$, diverging BCH; (iii) staircase ray $r_m=(m,m-1)$, $4/(\pi^4 d_m^2)$, $m=2$ witness $4/(9\pi^4) > A_{\mathrm{GC}} q_{\mathrm{GC}}^3$. |

---

## 2. Findings (P0–P3)

No P0 findings.

### P1 (Must fix before release)

1. **[P1] Wrong matrix in Ward-Schur upper bound (`main.tex:743`).**
   In `rem:ward`, line 743 writes:
   `With $Q=VA_-^{-1}D_-(A_-^{-1})^*V^*$ one has $0\le Q\le VA_-^{-1}V^*=:\tilde Q$`
   Because $A_- = R_- - i D_-$ is not Hermitian, $V A_-^{-1} V^*$ is not Hermitian (and not positive semidefinite), so the matrix inequality $Q \le V A_-^{-1} V^*$ is undefined/false. In `LINEAR-FRESH/RIGOR.md:201–202`, the bound is $\tilde Q = V D_-^{-1} V^*$ (following from $\|D_-^{1/2} A_-^{-1} D_-^{1/2}\| \le 1$).
   - **Fix:** Change `VA_-^{-1}V^*` to `VD_-^{-1}V^*` at `main.tex:743`.

2. **[P1] Inaccurate condensed proof summary for `thm:canon` (`main.tex:928–935`).**
   The proof summary of `thm:canon` states:
   > "A Griffith-type derivative bound on the single-bond activity, together with the two-dimensional isoperimetric inequality $|\partial S|\ge\sqrt{|S|}$, controls the difference between the canonical and grand-canonical weights at vanishing source in the thermodynamic limit, giving \eqref{eq:canon}."
   Neither a "single-bond activity" derivative nor the 2D isoperimetric inequality $|\partial S|\ge\sqrt{|S|}$ appears in `PURESSH/RIGOR.md` §6 (Lemma 6.1 and Proof of Theorem 1.2). The actual proof in `PURESSH/RIGOR.md:411–471` uses: (a) Lemma 6.1's boundary spring-constant bracket ($K \to K/2, 2K$ via Young's inequality and min-max monotonicity) on rectangular blocks of side $[b, 2b-1]$ to bound boundary error by $O(b^{-1})|\Lambda_L|$ and establish superadditivity and Legendre duality; and (b) convexity of $\xi \mapsto L_j^{-2}\log\widehat{Z}_{\Lambda_{L_j},N_j}(\xi)$ (Griffiths-type difference-quotient bound on the source derivative at $\xi=0$ bounded by $(p_{\Lambda_{L_j}}(\xi)-p_{\Lambda_{L_j}}(0))/\xi + \delta_{L_j}/\xi$ with Legendre discrepancy $\delta_{L_j}\to 0$).
   - **Fix:** Replace `main.tex:928–936` with an accurate summary of `PURESSH/RIGOR.md` §6 (boundary spring-constant bracket $K\to K/2, 2K$ giving $O(b^{-1})|\Lambda_L|$ superadditivity and Legendre duality, supporting $\mu$ with vanishing Legendre discrepancy $\delta_{L_j}\to 0$, and convexity of $\xi\mapsto L_j^{-2}\log\widehat{Z}_{\Lambda_{L_j}, N_j}(\xi)$ bounding the $\xi=0$ source derivative by Theorem~\ref{thm:gc} as $L_j\to\infty$ then $\xi\downarrow 0$).

3. **[P1] `CLAIMS.md` falsely marks all of Section 5 (`PURESSH`) as `PENDING REVIEW2` (`CLAIMS.md:12–13, 62–76`).**
   `CLAIMS.md` states that `PURESSH`'s second review (`REVIEW2.md`) "had not been filed at the time of writing" and tags every row of Section 4 (`sec:survives`) with **PENDING REVIEW2**. In fact, `ADIABATIC/PURESSH/REVIEW2.md` is on disk (all F1–F6 resolved; core theorems **PROVED**, constants **CERTIFIED**), and its four minor notes `N1`–`N4` were subsequently fixed and re-verified in `ADIABATIC/PURESSH/FIX.md` §4 (`replay.py`, `--all-mutants`, and `ed_check.py` all exit `0`).
   - **Fix:** Remove the `PENDING REVIEW2` legend entry (`CLAIMS.md:12–13`), remove the stale banner (`CLAIMS.md:64–66`), and replace `PENDING REVIEW2` in `CLAIMS.md:69–76` with references to `ADIABATIC/PURESSH/REVIEW2.md` (PASS) and `ADIABATIC/PURESSH/FIX.md` §4.

### P2 (Should fix before release)

4. **[P2] Misstated proof step in `thm:gc` Proof summary (`main.tex:880–883`).**
   Step (2) of `thm:gc`'s proof summary says: "Summing the multiplicities on a connected polymer and using Cauchy-Schwarz degeneracy bounds for the even phonon Wick contractions gives \eqref{eq:activity}". In `PURESSH/RIGOR.md` §§3–5 (Lemmas 3.1, 3.2, 4.2, and Proposition 5.2), there are no "Cauchy-Schwarz degeneracy bounds" for the phonon Wick contractions: the electronic trace is bounded by the multilinear Schatten-Hölder inequality (giving exact cancellation of $z_0^{|S_E|}$), and the even phonon Wick contractions are evaluated exactly by simplex-to-hypercube factorization and the frequency-uniform double integral $\int_0^\beta\int_0^\beta C_\beta(|u-v|)\,du\,dv = \beta/K$.
   - **Fix:** Replace "using Cauchy-Schwarz degeneracy bounds for the even phonon Wick contractions" at `main.tex:880–881` with "bounding the electronic trace by multilinear Schatten-Hölder (which cancels the single-site weight $z_0^{|S_E|}$) and integrating the exact positive Gaussian phonon Wick contractions via $\int_0^\beta\int_0^\beta C_\beta(|u-v|)\,du\,dv=\beta/K$".

5. **[P2] Misattributed citation in Remark after `thm:canon` (`main.tex:946–950`).**
   `main.tex:948–950` writes: "and the purely Peierls bookkeeping of \cite{stage6} is replaced by the explicit constants of Theorem~\ref{thm:gc}." However, `\cite{stage6}` (`10.5281/zenodo.24380128`) is the strong-coupling **Holstein** paper (*Strong-coupling suppression of electronic pair order in the Holstein model...*), not a Peierls/bond-SSH paper.
   - **Fix:** Remove the mischaracterization of `\cite{stage6}` as "purely Peierls bookkeeping" (refer instead to the strong-coupling Holstein analysis `\cite{stage6}` vs. the attractive Hubbard + bond-SSH bound `\cite{sshbond3}`, whose $t^2/U_{\mathrm{eff}}$ rate diverges at $U_{\mathrm{eff}}=0$ and whose $t=0$ threshold $2^{13}G_{\mathrm{b}}$ is tightened to $2^{10}G_{\mathrm{b}}$ by Theorem~\ref{thm:gc}).

6. **[P2] Internal contradiction in Section 6 item (a) (`main.tex:1071–1072`).**
   `main.tex:1071` states: "No upper bound on $\Tpair$ is improved anywhere in this note, and no ceiling at the scale $\Tlin=C(t,U)\Omega$ is proved or disproved." This contradicts Section 5 (`thm:canon`), which establishes the finite bound $k_B\Tpair \le 1024(|t|+\Gb)$ for the pure bond-SSH model at $\Ueff=0$ (closing the $\Ueff\to 0$ divergence of `\cite{sshbond3}` and tightening its $t=0$ constant from $2^{13}\Gb$ to $2^{10}\Gb$).
   - **Fix:** Scope `main.tex:1071` to the Holstein / $\Ueff>0$ problem: e.g., "No upper bound on $\Tpair$ for the attractive Holstein model (or any $\Ueff>0$ model) is improved anywhere in this note, and no ceiling at the scale $\Tlin=C(t,U)\Omega$ is proved or disproved."

7. **[P2] Four inaccurate table/note entries in `CLAIMS.md` (`CLAIMS.md:40, 42, 94, 107`).**
   - `CLAIMS.md:40`: `lem:aux` row lists `(i) eq:second, (ii) eq:Kx, (iii) eq:cov variance scaling`; those labels belong to `lem:first` and the setup, not `lem:aux` (which has no numbered equations and proves $q(a)\le a^2/12$, $a_x\le U\Omega^2\beta^3/48$, $a_x\le d_x t^2 U\Omega^2\beta^5/1440$, and static Combes-Thomas decay).
   - `CLAIMS.md:42`: `thm:witness` row calls `1/1148 > 1/1200` an "upper bound" — it is a **lower** bound on $a_{\mathrm{left}}$.
   - `CLAIMS.md:94`: states `main.tex:158-170` writes `Q_x = sqrt(U_x Omega_x)` and "earlier notes in the series write the bond constant as `g^2/K`"; `main.tex:156-168` actually writes $G_x = \sqrt{U_x\Omega_x/2}$, states $M_x, K_x$ enter only through $\Omega_x, U_x$, and states earlier notes write the **site** coupling as $U=g^2/K$.
   - `CLAIMS.md:107`: broken backticks `eq:(\`source\`)` and inaccurate note "applied by omission, the paper quotes only the source-free clustering bound" (`main.tex:831-835, 855-862` explicitly defines $Y_{e'}(\theta)$ and states `eq:source`).
   - **Fix:** Correct those four entries in `CLAIMS.md`.

### P3 (Minor / polish)

8. **[P3] Symbol mismatch in `rem:smooth` (`main.tex:701`).**
   `eq:impurity` (`main.tex:643`) denotes the time-dependent impurity level by $\varepsilon(u)$, whereas `rem:smooth` (`main.tex:701`) writes the oscillator action as $\int[(b')^2/\Omega^2+b^2]/(2U)$ using $b$ from `LINEAR-FRESH/RIGOR.md`. Change `b` to `\varepsilon` in `main.tex:701` (or note $b(u)=\varepsilon(u)$).
9. **[P3] Reuse of lowercase `g` in `rem:dimer` (`main.tex:776–780`).**
   Section 2 (`main.tex:160, 187`) reserves lowercase $g$ for the bond-SSH force constant and uses $G$ for the Holstein boson-operator coupling $G=\sqrt{U\Omega/2}$, but `rem:dimer` (`main.tex:776–780`) uses lowercase $g$ for $g^2=U\Omega/2$. Align to $G$.
10. **[P3] Misplaced $C_{\mathrm{aux}}$ mention inside `thm:gc` Proof summary (`main.tex:903–907`).**
    Step (5) of `thm:gc`'s proof summary cites `the enclosure 67/50 < C_{\mathrm{aux}} < 27/20 used elsewhere in this programme`, even though $C_{\mathrm{aux}}$ appears in Section 4 (`rem:ward`, from `LINEAR-FRESH`), not in `thm:gc` or `PURESSH`. Move that certification remark to `rem:ward` or Data availability.
11. **[P3] Wrong environment name in Section 7 item (6) (`main.tex:1129`).**
    `Proposition~\ref{thm:routes}(iii)` should be `Theorem~\ref{thm:routes}(iii)`.
12. **[P3] Plural "Tables" in Data availability (`main.tex:1150`).**
    `the finite-matrix diagnostics of Tables and Remarks above` — the paper has only one table (`tab:routes`), which is a route-summary table with no finite-matrix diagnostics. Change to `the Remarks above`.

---

## 3. Checklist Summary (Items 3–7)

- **Novelty framing (Item 3):** **PASS** (after P2 Finding 6). `lem:fsum` is explicitly introduced as a classical oscillator $f$-sum lemma (`main.tex:568–572`); the linear step is repeatedly stated as open (`main.tex:43, 108, 1096`); no measured-$T_c$ or materials claims appear; zero occurrences of `pending review` or draft language in `main.tex`/`main.pdf`.
- **Paper rules & Tectonic rebuild (Item 4):** **PASS**. Rebuilt in `C:/t/Barriers2Review/build` with `D:/dev/tools/tectonic/tectonic.exe --keep-logs main.tex` (exit `0`): **0** overfull boxes, **0** underfull boxes, **0** LaTeX/package/BibTeX warnings, **0** undefined references, 17 pages, extracted text byte-identical to `main.pdf`. PDF text check: `0` em dashes (`U+2014`), `0` en dashes (`U+2013`), `0` `--`, exact sentence `This preprint has not been peer reviewed.` present, AI disclosure present, byline `Davis Rens`, `SuperMatics Inc.`, `ORCID 0000-0001-5839-5197` present, `0` unresolved `??`, `0` lane/machine/path/internal-codeword leaks (`agent` appears only inside the AI-assistance disclosure).
- **Bibliography DOIs and titles (Item 5):** **PASS**. All 7 entries in `refs.bib` (`barriers` `24384373`, `limits` `24385569`, `linear5` `24374043`, `sshbond3` `24406987`, `stage6` `24380128`, `linear4` `24372238`, `slow` `24366508`) match the released DOIs and titles in `CAPSTONE-PAPER/refs.bib` and `SSHBOUND3-PAPER/main.tex` verbatim.
- **`CLAIMS.md` accuracy (Item 6):** **NEEDS FIXES** (Findings 3 and 7).
- **Prose quality (Item 7):** **PASS**. Clear, concise, human, journal-grade mathematical prose throughout.

---

## 4. Verification Commands and Exit Codes

All temporary files were created under `C:/t/Barriers2Review` and deleted at the end of the review.

| Check | Command | Exit code | Result |
|---|---|---:|---|
| Temp Tectonic rebuild + log audit | `cd C:/t/Barriers2Review/build && D:/dev/tools/tectonic/tectonic.exe --keep-logs main.tex` + `grep -c` checks on `main.log` | **0** | 17-page `main.pdf` (187,760 B); Overfull `0`, Underfull `0`, LaTeX Warning `0`, Package Warning `0`, Undefined `0`, Multiply defined `0`. |
| PDF text, dash, rule, and label audit | `UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with pypdf --with mpmath --with numpy python -B C:/t/Barriers2Review/audit_all.py` | **1** (stopped at `mp.iv.dps` default 15 vs `1e-50` assertion after printing all PDF/tex checks) | Confirmed identical extracted text vs `main.pdf`, `0` em/en dashes, required sentences/byline present, `0` forbidden words, `0` `??`, all 68 labels mapped. |
| Independent math & constant verification | `UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with mpmath --with numpy python -B C:/t/Barriers2Review/verify_math.py` | **0** | `ALL_VERIFY_MATH_PASSED`: verified `1/1148 > 1/1200`, 3-site & $L=4$ torus ($B=10^5$) witness, `B=6, v=1/2` fixture ($\det(1+U)=15.790282\ldots>15$, $|\mathcal{G}_{00}|=52.8957540935\ldots>52.89$) in 60-digit `mpmath.iv`, $C_{\mathrm{aux}}\in(67/50, 27/20)$, non-Hermiticity of `main.tex:743`'s $VA_-^{-1}V^*$ vs PSD of $VD_-^{-1}V^*-Q$, dimer $1/64$ vs $1/68$, all `PURESSH` exact rationals, $m=2$ staircase witness, and $C_4$ $M_{\mathrm{even}}$ minimal polynomial. |
