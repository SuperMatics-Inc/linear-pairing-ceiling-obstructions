# BARRIERS2-PAPER review resolution (`FIX.md`)

Resolves all findings `P1`-`P3` of `MASSIVE/BARRIERS2-PAPER/REVIEW.md`
(verdict `PASS-WITH-FIXES`: 0 P0, 3 P1, 4 P2, 5 P3), while preserving `REVIEW.md`
untouched and archiving the reviewed text as `main.v1.tex` and the reviewed claim map
as `CLAIMS.v1.md`. No theorem statement, hypothesis, constant or scope was changed by
these fixes; every item below is a typo, a citation, a proof-summary wording or a
documentation correction.

Status after the fixes: all 12 findings applied, `main.tex` rebuilt clean, and the
claim map re-verified line by line against the frozen source records.

## 1. Item-by-item resolution

### P1-1: Wrong matrix in the Ward-Schur upper bound

- **Issue:** `main.v1.tex:743` printed $Q=VA_-^{-1}D_-(A_-^{-1})^*V^*\le VA_-^{-1}V^*$,
  but $A_-=R_--iD_-$ is not Hermitian, so $VA_-^{-1}V^*$ is neither Hermitian nor
  positive semidefinite and the matrix inequality is undefined.
- **Fix:** `main.tex:734-740` now prints $0\le Q\le VD_-^{-1}V^*=:\tilde Q$, which is
  the bound proved in `MASSIVE/LINEAR-FRESH/RIGOR.md:201-202` from
  $\|D_-^{1/2}A_-^{-1}D_-^{1/2}\|\le1$, together with the Schur step into
  `eq:ward4`. The remainder of the algebra and the enclosure
  $67/50<C_{\mathrm{aux}}<27/20$ (`main.tex:770-771`) are unchanged.

### P1-2: Inaccurate condensed proof summary of `thm:canon`

- **Issue:** `main.v1.tex:928-935` cited a "Griffith-type derivative bound on the
  single-bond activity" and a "two-dimensional isoperimetric inequality
  $|\partial S|\ge\sqrt{|S|}$"; neither appears in `ADIABATIC/PURESSH/RIGOR.md` §6.
- **Fix:** `main.tex:987-1012` now follows the source: the boundary spring-constant
  bracket $K\to K/2$ and $2K$ by Young's inequality and min-max monotonicity with
  boundary cost $C_{\mathrm{bdry}}|\partial|+\beta|\xi||\partial_{\mathrm{src}}|$ and
  $|\partial|\le4|\Lambda_L|/b$ (Lemma `lem:canon`), particle distribution over blocks
  at cost $O(b^{-2}\log b)|\Lambda_L|$, superadditivity up to $O(b^{-1})|\Lambda_L|$,
  concavity of the canonical free-energy density, a supporting slope $-\beta\mu$, a
  nonnegative finite-volume Legendre discrepancy $\delta_L\to0$, and convexity of
  $\xi\mapsto L^{-2}\log\widehat Z_{\Lambda_L,N}(\xi)$ bounding the value at $\xi=0$
  by the difference quotient with Theorem `thm:gc`; the limits are taken as
  $j\to\infty$ at fixed $\xi$, then $\xi\downarrow0$, then over the phase $\theta$.
  This mirrors `ADIABATIC/PURESSH/RIGOR.md:411-471`.

### P1-3: Stale review status in the claim map

- **Issue:** `CLAIMS.v1.md:12-13, 62-76` tagged the whole `U_eff=0` section as
  pending a second review that had in fact been filed.
- **Fix:** `CLAIMS.md` removes that status entirely, records the frozen digest
  `ADIABATIC/PURESSH/RIGOR.md` sha256
  `d04efa00eaa844e1cc1bdde4f8abe275f69daecfb2212b26ac2a25c6540adaa1`, and states that
  `ADIABATIC/PURESSH/REVIEW.md` passed after `F1`-`F6` and that
  `ADIABATIC/PURESSH/REVIEW2.md` resolved all six findings with the four notes
  `N1`-`N4` fixed and re-verified in `ADIABATIC/PURESSH/FIX.md` §4.
- **Also corrected in the same pass:** every paper line number in `CLAIMS.md` was
  re-derived from the current `main.tex` (`write` of the whole map, sections 1-7), and
  the four P2 entries of finding 7 were rewritten.

### P2-4: Misstated step (2) of the `thm:gc` proof summary

- **Issue:** `main.v1.tex:880-883` spoke of "Cauchy-Schwarz degeneracy bounds" for the
  phonon contractions.
- **Fix:** `main.tex:877-887` now says: bounding the electronic trace by the
  multilinear Schatten-Hölder inequality, which cancels the single-site weight
  $z_0^{|S_E|}$ exactly, and evaluating the exact positive Gaussian Wick contractions
  of the bond oscillators, each pair contributing the frequency-uniform integral
  $\int_0^\beta\int_0^\beta C_\beta(|u-v|)\,du\,dv=\beta/K$.

### P2-5: Misattributed citation after `thm:canon`

- **Issue:** `main.v1.tex:948-950` described `\cite{stage6}` as "purely Peierls
  bookkeeping", whereas that record is the strong-coupling Holstein analysis.
- **Fix:** `main.tex:1013-1023` now reads: the Holstein ceiling of `\cite{stage6}` and
  the attractive-Hubbard bond-SSH ceiling of `\cite{sshbond3}` both carry the rate
  $t^2/U_{\mathrm{eff}}$, infinite at $U_{\mathrm{eff}}=0$, whereas the paper's bound
  is finite there; at $t=0$ the threshold $2^{13}G_{\mathrm b}$ of `\cite{sshbond3}`
  becomes $2^{10}G_{\mathrm b}$. No "Peierls bookkeeping" characterisation remains.

### P2-6: Internal contradiction in `sec:notclaimed` item (a)

- **Issue:** `main.v1.tex:1071` said no upper bound on $T_{\mathrm{pair}}$ is improved
  anywhere, contradicting Theorem `thm:canon`.
- **Fix:** `main.tex:1146-1152` scopes the exclusion to the Holstein or any
  $U_{\mathrm{eff}}>0$ model and names Theorem `thm:canon` as the single exception at
  $U_{\mathrm{eff}}=0$; item (d) records the same limitation.

### P2-7: Four inaccurate entries in the claim map

- **Fix:** in `CLAIMS.md`:
  - the `lem:aux` row now lists the three items actually proved (the inequalities
    $q(a)\le a^2/12$, $\chi_x\le\beta/4$, $a_x\le U\Omega^2\beta^3/48$; the spectral
    variance identity with $a_x\le d_xt^2U\Omega^2\beta^5/1440$; the static
    Combes-Thomas bound) and states that the lemma has no numbered equation;
  - the `thm:witness` row calls $1/1148>1/1200$ a **lower** bound on $a_{\mathrm{left}}$;
  - the notation row says the paper writes $G_x=\sqrt{U_x\Omega_x/2}$, that
    $M_x,K_x$ enter only through $\Omega_x,U_x$, and that earlier notes write the
    **site** coupling as $U=g^2/K$ with that lowercase $g$ the site force constant
    (`main.tex:156-168`);
  - the source-vertex row states that the paper does define
    $Y_{e'}(\theta)=e^{i\theta}\Delta_x^\dagger\Delta_{x+r}+e^{-i\theta}\Delta_{x+r}^\dagger\Delta_x$
    with operator norm $1$ (`main.tex:833-835`) and does state `eq:source`
    (`main.tex:860-862`); the earlier "applied by omission" wording is gone.

### P3-8: Symbol mismatch in `rem:smooth`

- **Fix:** `main.tex:701` writes the oscillator action as
  $\int[(\varepsilon')^2/\Omega^2+\varepsilon^2]/(2U)$, matching the impurity level
  $\varepsilon(u)$ of `eq:impurity`.

### P3-9: Reuse of lowercase `g` in `rem:dimer`

- **Fix:** `main.tex:779-781` uses $G^2=U\Omega/2$ and $GN/\sqrt2$ throughout.

### P3-10: Misplaced $C_{\mathrm{aux}}$ remark inside `thm:gc`

- **Fix:** `main.tex:906-911` ends the `thm:gc` proof summary at the certification of
  the constants of `eq:constants`, `eq:constants2` and the integer polynomial
  identities of Theorem `thm:routes`(i). The single remaining mention of
  $C_{\mathrm{aux}}$ is in `rem:ward` (`main.tex:770-771`), where it belongs.

### P3-11: Wrong environment name in open problem (6)

- **Fix:** `main.tex:1207-1208` cites Theorem `thm:routes`(iii) and Theorem
  `thm:routes`(i).

### P3-12: Plural "Tables" in the data-availability statement

- **Fix:** `main.tex:1226-1227` says "the finite-matrix diagnostics of the Remarks
  above"; the paper has one table, the route summary, which contains no diagnostics.

## 2. Digest of the reviewed and corrected text

| File | sha256 |
|---|---|
| `main.v1.tex` (reviewed) | see `REVIEW.md` |
| `main.tex` (corrected) | recomputed at build time, recorded in `BUILD.md` |
| `CLAIMS.v1.md` (reviewed) | superseded by `CLAIMS.md` |
| `CLAIMS.md` (corrected) | recomputed at build time, recorded in `BUILD.md` |

## 3. Verification performed after the fixes

1. `D:/dev/tools/tectonic/tectonic.exe --keep-logs main.tex` in this directory:
   exit `0`, 0 overfull boxes, 0 underfull boxes, 0 undefined references or citations,
   0 LaTeX or package warnings. Recorded in `BUILD.md`.
2. Extracted PDF text audit: 0 em dashes, 0 en dashes, 0 `--`, the required sentence
   and the AI-assistance disclosure present, byline and ORCID present, 0 unresolved
   `??`, 0 occurrences of internal project words. Recorded in `BUILD.md`.
3. `CLAIMS.md`: every row re-derived against `main.tex` labels and against the frozen
   `RIGOR.md` line ranges; the source digests quoted there were recomputed with
   `sha256sum`.

## Main follow-up (N1 from REVIEW2.md)
main.tex:1006 'value at xi=0' -> 'derivative at xi=0'. Backup: main.v2.tex. Rebuilt with Tectonic, exit 0.
