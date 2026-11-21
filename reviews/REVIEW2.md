# Independent Follow-Up Review (`REVIEW2`) of `BARRIERS2-PAPER` Fixes

- **Reviewed directory:** `D:/dev/scratch/ceiling-20261118/MASSIVE/BARRIERS2-PAPER/`
- **Reviewed artifacts:** `main.tex` (diffed against `main.v1.tex`), `main.pdf`, `CLAIMS.md`, `FIX.md`, `BUILD.md` (`REVIEW.md` preserved untouched)
- **Overall Verdict:** **`PASS-WITH-FIXES` (all 12 findings from `REVIEW.md` RESOLVED; 0 P0, 0 P1, 1 newly introduced single-word P2 typo `N1` at `main.tex:1007`)**

Every one of the 12 findings from `REVIEW.md` (3 P1, 4 P2, 5 P3) has been cleanly resolved in `main.tex` and `CLAIMS.md`. The newly added `lem:canon` (`main.tex:914–966`) matches `ADIABATIC/PURESSH/RIGOR.md:411–445` (Lemma 6.1) accurately, the Tectonic temp rebuild is completely clean (0 overfull/underfull boxes, 0 undefined references, 0 warnings), all PDF text/rule checks pass, all 8 SHA-256 digests match `BUILD.md` and `CLAIMS.md`, and all `CLAIMS.md` line references match `main.tex`.

One newly introduced single-word mathematical typo (`N1`, P2) appeared in the rewritten `thm:canon` proof summary at `main.tex:1007` (`its value at \xi=0` instead of `its derivative at \xi=0`). Fixing that single word and rebuilding clears the paper for public release.

---

## 1. Resolution of `REVIEW.md` Findings (1–12)

| # | Original finding | Status | Verification against `diff -u main.v1.tex main.tex` and `CLAIMS.md` |
|---|---|---|---|
| 1 (P1) | `main.v1.tex:743`: `V A_-^{-1} V^*` (non-Hermitian) | **RESOLVED** | `main.tex:738` now reads `0\le Q\le VD_-^{-1}V^*=:\tilde Q`. |
| 2 (P1) | `main.v1.tex:928–935`: inaccurate `thm:canon` proof summary (single-bond activity / 2D isoperimetric inequality) | **RESOLVED** (see `N1` below) | `main.tex:914–966` adds the complete proof of `lem:canon` (matching `PURESSH/RIGOR.md` Lemma 6.1: Young's inequality $2|g||X_b|\le KX_b^2/4+4g^2/K$, $K\to K/2, 2K$, min-max monotonicity, decoupled boundary oscillators), and `main.tex:987–1011` follows `PURESSH/RIGOR.md` §6 (block superadditivity, concave $f_{\mathrm{can}}$, supporting $-\beta\mu$, Legendre discrepancy $\delta_L\to 0$, convexity in $\xi$). Contains 1-word typo `N1` at line 1007. |
| 3 (P1) | `CLAIMS.v1.md:12–13, 62–76`: stale `PENDING REVIEW2` tags for `PURESSH` | **RESOLVED** | `CLAIMS.md` removes `PENDING REVIEW2`, records `PURESSH/REVIEW2.md` PASS and `PURESSH/FIX.md` §4 (`N1`–`N4`), and cites the verified SHA-256 of `ADIABATIC/PURESSH/RIGOR.md` (`d04efa00...adaa1`). |
| 4 (P2) | `main.v1.tex:880–883`: "Cauchy-Schwarz degeneracy bounds" in `thm:gc` proof summary | **RESOLVED** | `main.tex:877–883` now states multilinear Schatten-Hölder (cancelling $z_0^{|S_E|}$) and exact positive Gaussian Wick contractions via $\int_0^\beta\int_0^\beta C_\beta(|u-v|)\,du\,dv=\beta/K$. |
| 5 (P2) | `main.v1.tex:948–950`: misdescribing `\cite{stage6}` as "purely Peierls bookkeeping" | **RESOLVED** | `main.tex:1016–1022` accurately compares the Holstein ceiling `\cite{stage6}` and attractive-Hubbard bond-SSH ceiling `\cite{sshbond3}` (both carrying $t^2/U_{\mathrm{eff}}$) with `thm:canon` and notes the $2^{13}G_{\mathrm{b}}\to 2^{10}G_{\mathrm{b}}$ improvement at $t=0$. |
| 6 (P2) | `main.v1.tex:1071`: "No upper bound on $T_{\mathrm{pair}}$ is improved anywhere in this note" | **RESOLVED** | `main.tex:1146–1152` and `1164–1169` scope the exclusion to Holstein / $U_{\mathrm{eff}}>0$ and explicitly name `thm:canon` at $U_{\mathrm{eff}}=0$ as the single exception. |
| 7 (P2) | `CLAIMS.v1.md:40, 42, 94, 107`: four inaccurate table/note entries | **RESOLVED** | `CLAIMS.md` fixes `lem:aux` items/labels, calls `1/1148 > 1/1200` a **lower** bound on $a_{\mathrm{left}}$, states $G_x=\sqrt{U_x\Omega_x/2}$ and site coupling $U=g^2/K$, and accurately records $Y_{e'}(\theta)$ and `eq:source`. |
| 8 (P3) | `main.v1.tex:701`: `b` instead of `\varepsilon` in `rem:smooth` | **RESOLVED** | `main.tex:701` now writes $\int[(\varepsilon')^2/\Omega^2+\varepsilon^2]/(2U)$. |
| 9 (P3) | `main.v1.tex:776–780`: lowercase `g` in `rem:dimer` | **RESOLVED** | `main.tex:778–783` uses $G^2=U\Omega/2$ and $GN/\sqrt{2}$ consistently with `eq:U`. |
| 10 (P3) | `main.v1.tex:903–907`: misplaced $C_{\mathrm{aux}}$ mention inside `thm:gc` | **RESOLVED** | Removed from `main.tex:909–911` (now references `Theorem~\ref{thm:routes}(i)`) and noted in `rem:ward` (`main.tex:770–771`). |
| 11 (P3) | `main.v1.tex:1129`: `Proposition~\ref{thm:routes}(iii)` | **RESOLVED** | `main.tex:1206–1208` now cites `Theorem~\ref{thm:routes}(iii)` and `Theorem~\ref{thm:routes}(i)`. |
| 12 (P3) | `main.v1.tex:1150`: plural "Tables and Remarks" | **RESOLVED** | `main.tex:1227` now reads `the finite-matrix diagnostics of the Remarks above`. |

---

## 2. Newly Introduced Finding

- **`N1` [P2] Single-word mathematical typo in `thm:canon` proof summary (`main.tex:1007`, echoed in `FIX.md:40`).**
  `main.tex:1005–1008` reads:
  > "Since the Hamiltonian is linear in the real source $\xi$ and self-adjoint, $\xi\mapsto L^{-2}\log\widehat Z_{\Lambda_L,N}(\xi)$ is convex, so its **value** at $\xi=0$ is bounded by the difference quotient, i.e.\ by $(p_{\Lambda_L}(\xi)-p_{\Lambda_L}(0))/\xi+\delta_L/\xi$ there;"
  Convexity bounds the **derivative** at $\xi=0$ ($\partial_\xi\big|_{\xi=0}[L^{-2}\log\widehat Z_{\Lambda_L,N}(\xi)] = 2\beta\operatorname{Re}(e^{i\theta}\langle\Delta_0^\dagger\Delta_r\rangle_{\Lambda_L,N})$) by the difference quotient for $\xi>0$, not the **value** at $\xi=0$.
  - **Fix:** Replace `so its value at $\xi=0$` with `so its derivative at $\xi=0$` at `main.tex:1007` (and optionally in `FIX.md:40`), then rebuild `main.pdf`.

---

## 3. Verification Commands and Exit Codes

All temporary files were created under `C:/t/Barriers2Review2` and deleted at the end of the review.

| Check | Command | Exit code | Result |
|---|---|---:|---|
| Diff against `main.v1.tex` | `cd D:/dev/scratch/ceiling-20261118/MASSIVE/BARRIERS2-PAPER && diff -u main.v1.tex main.tex` | **1** (diffs present) | Verified all 12 edits; caught 1-word typo `N1` at `main.tex:1007`. |
| Temp Tectonic rebuild + log checks | `cd C:/t/Barriers2Review2/build && D:/dev/tools/tectonic/tectonic.exe --keep-logs main.tex` + `grep -c` on `main.log` | **0** | 18-page `main.pdf` (197,114 B); Overfull `0`, Underfull `0`, LaTeX Warning `0`, Package Warning `0`, Undefined `0`, Multiply defined `0`. |
| PDF text, SHA-256, and `CLAIMS.md` audit | `UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with pypdf python -B C:/t/Barriers2Review2/audit2.py` + word-bounded/primary-range check | **0** | Extracted text byte-identical to `main.pdf`; `0` em dashes, `0` en dashes, `0` `--`, `0` `??`; required non-peer-reviewed sentence, AI disclosure, byline/ORCID all present; `0` word-bounded hits for `lane`/`worker`/`omp`/`git`/`MIKUSSY`/`C:/`/`D:/`/`scratch`/`pending review`; `agent` appears only in the AI disclosure (2 hits); all 8 SHA-256 digests match `BUILD.md`/`CLAIMS.md`; all `CLAIMS.md` primary table ranges and prose line refs match `main.tex`. |
