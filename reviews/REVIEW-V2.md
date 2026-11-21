# Independent Delta Review of `BARRIERS2-V2` (`REVIEW-V2.md`)

- **Reviewed directory:** `D:/dev/scratch/ceiling-20261118/MASSIVE/BARRIERS2-V2/`
- **Reviewed artifacts:** `main.tex` (SHA-256 `ec5c2f79ab0a2465b307c8ba964258c37495bddba2c27e7d73b3a9ef3f0801ac`), `refs.bib` (`d555d2ec1c57c0cdada78e96400e900c33b52f92967d8f4e0c17fe56ac78a675`), `CLAIMS.md` (`9e7731ba531b04550ecf82d72d1a16e1a789eb53f110588948c7d3878859e381`), `BUILD.md`, `main.pdf`.
- **v1 baseline check:** `D:/dev/scratch/ceiling-20261118/MASSIVE/BARRIERS2-PAPER/main.tex` SHA-256 confirmed as `cb0bda1231e1f00006beefd0e4a9fdd5fd22088e84892bb383f07c60d36b7b5f`.
- **Sources checked against:** `MASSIVE/UNIFORM-SSH/{RIGOR.md,REVIEW.md,REVIEW2.md,AMENDMENT.md,replay.py}`, `ADIABATIC/PURESSH/{RIGOR.md,FIX.md,REVIEW.md,REVIEW2.md}`, `PUBLISH/barriers2/repo/records/puressh/REVIEW2.md`, `ADIABATIC/SSHBOUND3-PAPER/main.tex`, and Daniel Ueltschi's publication list (`http://www.ueltschi.org/publications.php`).
- **Verdict:** **PASS-WITH-FIXES** (0 P0, 1 P1, 1 P2, 3 P3).

---

## 1. Summary of Delta Checks

1. **Mathematical fidelity to `UNIFORM-SSH/RIGOR.md` and `N1` fix (`PASS`):**
   - `N1` from `REVIEW2.md` is fixed at `main.tex:1089` (`"so its derivative at $\xi=0$ is bounded by..."`).
   - `thm:gc` (`main.tex:884-989`), `lem:canon` (`1003-1054`), `thm:canon` (`1056-1095`), `thm:min-att` (`1124-1167`), `thm:min-rep` (`1168-1236`), and `prop:nonmonotone` (`1237-1290`) match `MASSIVE/UNIFORM-SSH/RIGOR.md` Theorems 1.1–1.5 and §§3–5 across all constants (`c_0=2^{-10}`, `\xi_0=2^{-9}\beta^{-1}`, `\varepsilon=2/1023`, `q_{\mathrm{GC}}=32/341`, `A_{\mathrm{GC}}=341/103`, `b_{\mathrm{GC}}=32/103`, `R_{\max}=24718511/9834543<3`, `q_{\mathrm{src}}=72/341`, `b_{\mathrm{src}}=216/269<1`; attractive/Mott `1965840/475579`, `48645/524224`, `b_{\mathrm{src}}=6567075/6636364<1`; dilute GC `1179504/232925`, `29187/262112` and canonical `2359008/490429`, `33795/524224`, `b_{\mathrm{src}}=2737395/3585482<1`; dimer intervals `[1.6180,1.6182]\times 10^{-4} \to [4.4138,4.4140]\times 10^{-3}` factor `>25`, `0.017797` `>109.9\times`, uncentered `[1.2879,1.2881]\times 10^{-3} \to [5.3243,5.3245]\times 10^{-3}` factor `>4.1`; Mott-edge `w_\infty(\{e\})\ge (\cosh(\beta t)-1)/4 > 2` at `\beta t=3`), windows, hypotheses, and canonical transfer. `UNIFORM-SSH/replay.py` passed with exit code `0`.
   - `thm:routes` (`main.tex:1298-1408`) remains scoped strictly to the pure bond-SSH model (`U_{\mathrm{eff}}=0`), and `sec:notclaimed`(d) (`main.tex:1441-1445`) explicitly states that items (i) and (iii) apply strictly at `U_{\mathrm{eff}}=0`.
   - **Notation harmonisation (`main.tex:142-235`):** Consistent across the manuscript (`U_x=F_x^2/K_x`, `F_x X_x = G_x b_x`, `G_x^2 = U_x\Omega_x/2`, note on earlier `U=g^2/K` at `176-181`, `U_{\mathrm{eff}} = U_0 - 2g_0^2/\Omega_0` with explicit bridge `U_{\mathrm{eff}}^{\mathrm{att}} := -U_{\mathrm{eff}} > 0` to `\cite{sshbond3}` at `225-235`). The paper does not cite unreleased `HUBHOL` directly; the Mott/dilute SOS-plus-Wick arguments are given self-contained in `thm:min-rep`. Two minor P3 notation nits (`F3`, `F4`) are listed below.

2. **PURESSH review status (`FAIL` in `CLAIMS.md`/`BUILD.md` — Finding `F1`, P1):**
   - `CLAIMS.md` and `BUILD.md` falsely assert that `ADIABATIC/PURESSH/REVIEW2.md` is absent and mark the `U_{\mathrm{eff}}=0` `PURESSH` items as *pending REVIEW2* / provisional.
   - Both `D:/dev/scratch/ceiling-20261118/ADIABATIC/PURESSH/REVIEW2.md` and the archived published copy `D:/dev/scratch/ceiling-20261118/PUBLISH/barriers2/repo/records/puressh/REVIEW2.md` exist on disk and are byte-identical (SHA-256 `25f1115df5b8ce4eb4a246b5a30439ec354d09968cbc8423dd6214fa56926bfe`). `REVIEW2.md` confirmed all six `REVIEW.md` findings (`F1`–`F6`) **RESOLVED** and every core claim **PROVED** / **CERTIFIED**, and its four minor notes (`N1`–`N4`) were resolved and verified in `D:/dev/scratch/ceiling-20261118/ADIABATIC/PURESSH/FIX.md` §4. All `PURESSH` items in Section 5 are fully reviewed.

3. **External bibliographic data and `KNOWN` attribution (`FAIL` on 1 page number — Finding `F2`, P2):**
   - `rem:uelschi` (`main.tex:991-1001`) properly attributes the purely electronic `U`-uniform hopping expansion (`\beta|t|\le c`) as standard in mathematical statistical mechanics (`KNOWN`), citing `uelschi1999`, `uelschi2004`, and `frohlich2005`, and accurately scopes what `thm:gc` adds.
   - Verified against Daniel Ueltschi's official publication list (`http://www.ueltschi.org/publications.php`):
     - `uelschi1999`: Daniel Ueltschi, *Analyticity in Hubbard models*, J. Stat. Phys. **95** (3–4), 693–717 (1999), DOI `10.1023/A:1004599410952`, `cond-mat/9810320`. **Exact match.**
     - `uelschi2004`: Daniel Ueltschi, *Cluster expansions and correlation functions*, Moscow Math. J. **4** (2), 511–522 (2004), DOI `10.17323/1609-4514-2004-4-2-511-522`, `math-ph/0304003`. **Exact match.**
     - `frohlich2005`: Jürg Fröhlich and Daniel Ueltschi, *Hund's rule and metallic ferromagnetism*, J. Stat. Phys. **118** (5–6), **973–996** (2005), DOI `10.1007/s10955-004-2174-y`. **`refs.bib:84` erroneously prints `pages = {973--978}` instead of `973--996` (Finding `F2`, P2).**

4. **Paper rules and clean Tectonic rebuild (`PASS`):**
   - Temp Tectonic rebuild under `C:/t/B2V2Review/build` exited `0`, producing a 21-page PDF (`230,911` B) with `0` overfull boxes, `0` underfull boxes, `0` LaTeX/package warnings, `0` undefined references, and `0` multiply-defined labels; extracted text is identical to `BARRIERS2-V2/main.pdf`.
   - `0` em dashes (`U+2014`), `0` `--`, `0` `??`; the 5 en dashes (`U+2013`) are strictly numeric issue/page ranges in the bibliography (`118(5–6):973–978`, `95(3–4):693–717`, `4(2):511–522`), none used as punctuation dashes.
   - Exact sentence `"This preprint has not been peer reviewed."`, byline (`Davis Rens`, `SuperMatics Inc.`, ORCID `0000-0001-5839-5197`), and AI disclosure (`AI agents generated the proofs, code and drafts under D. Rens's direction...`) are all present.
   - `0` hits for `lane`, `worker`, `omp`, `git`, `MIKUSSY`, `scratch`, `pending review`, `C:/`, `D:/`; the only 2 occurrences of `agent` are inside the AI disclosure.

---

## 2. Findings

### F1 (P1) — `CLAIMS.md:24, 79-83, 91, 96-99, 174-178` & `BUILD.md:94-96`: False claim that `ADIABATIC/PURESSH/REVIEW2.md` is missing
- **Issue:** `CLAIMS.md` states that `ADIABATIC/PURESSH/REVIEW2.md` is *"not present in the source record at the time of this build"* and marks `lem:canon`, `thm:routes`(i)–(iii), and the remark after `thm:routes` as *pending REVIEW2* / provisional. `BUILD.md:94-96` repeats the same statement.
- **Evidence:** Both `D:/dev/scratch/ceiling-20261118/ADIABATIC/PURESSH/REVIEW2.md` and `D:/dev/scratch/ceiling-20261118/PUBLISH/barriers2/repo/records/puressh/REVIEW2.md` are present on disk and byte-identical (SHA-256 `25f1115df5b8ce4eb4a246b5a30439ec354d09968cbc8423dd6214fa56926bfe`), confirming `F1`–`F6` **RESOLVED** and every core claim **PROVED**/**CERTIFIED**, with minor notes `N1`–`N4` resolved in `ADIABATIC/PURESSH/FIX.md` §4.
- **Fix:** Update `CLAIMS.md` (§0, §4, §8) and `BUILD.md` ("Status of the reviews") to record `ADIABATIC/PURESSH/REVIEW2.md` (and `FIX.md` §4) as landed and remove all *pending REVIEW2* / provisional labels.

### F2 (P2) — `refs.bib:84` (rendered in `main.pdf` reference `[1]`): Wrong page range for Fröhlich & Ueltschi (2005)
- **Issue:** `@article{frohlich2005}` has `pages = {973--978}`, which prints as `118(5–6):973–978, 2005` in the PDF bibliography. The actual published page range is `973--996` (verified from Daniel Ueltschi's publication list `http://www.ueltschi.org/publications.php` entry `[15]`, DOI `10.1007/s10955-004-2174-y`).
- **Fix:** Change `pages = {973--978}` to `pages = {973--996}` in `refs.bib:84`, rebuild `main.pdf`, and update the bibliography en-dash note in `BUILD.md:49` accordingly.

### F3 (P3) — `main.tex:876`: Equation reference `\eqref{eq:Hssh}` instead of `\eqref{eq:Hhubssh}`
- **Issue:** Line `876` reads *"The source-augmented graph of `\eqref{eq:Hssh}` adds..."* immediately before `thm:gc`, which is stated for the general Hubbard-Holstein-SSH Hamiltonian `\eqref{eq:Hhubssh}` (as `AMENDMENT.md:183` specifies).
- **Fix:** Replace `\eqref{eq:Hssh}` with `\eqref{eq:Hhubssh}` at `main.tex:876`.

### F4 (P3) — `main.tex:1105`: Sign notation `t^2/\Ueff` instead of `t^2/|\Ueff|`
- **Issue:** In the remark after `thm:canon`, `main.tex:1105` writes *"carry the rate $t^2/\Ueff$"* for `\cite{stage6}` and `\cite{sshbond3}`. Under v2's sign convention (`eq:Ueff`), attractive interactions have `\Ueff < 0`.
- **Fix:** Change `$t^2/\Ueff$` to `$t^2/|\Ueff|$` at `main.tex:1105` (matching `eq:minatt` and `main.tex:1443`).

### F5 (P3) — `BUILD.md:1, 22` & `CLAIMS.md:1`: Stale directory name `BARRIERS2-PAPER`
- **Issue:** `BUILD.md` and `CLAIMS.md` headers and the build command (`BUILD.md:22`) still refer to `BARRIERS2-PAPER` rather than `BARRIERS2-V2`.
- **Fix:** Update the directory/title headers to `BARRIERS2-V2` when refreshing `BUILD.md` and `CLAIMS.md` after `F1`–`F4`.

---

## 3. Commands Run and Exit Codes

1. Locate `PURESSH` review files on disk (`ls` / `find`): exit `0` — confirmed both `ADIABATIC/PURESSH/REVIEW2.md` and `PUBLISH/barriers2/repo/records/puressh/REVIEW2.md` exist.
2. Temp Tectonic rebuild (`D:/dev/tools/tectonic/tectonic.exe --keep-logs --keep-intermediates main.tex` in `C:/t/B2V2Review/build`): `TECTONIC_EXIT=0` (`0` Overfull, `0` Underfull, `0` LaTeX/Package Warning, `0` Undefined, `0` Multiply defined; 21 pages, `230,911` B).
3. PDF text, formatting, rule, digest, and `CLAIMS.md` audit (`UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with pypdf python -B C:/t/B2V2Review/audit_v2.py`): `AUDIT_V2_EXIT=0`.
4. En-dash context audit on rebuilt PDF (`pypdf`): `ENDASH_CHECK_EXIT=0` (all 5 `U+2013` are numeric issue/page ranges in the bibliography).
5. Certification replay (`python -B D:/dev/scratch/ceiling-20261118/MASSIVE/UNIFORM-SSH/replay.py`): `REPLAY_EXIT=0` (`ALL EXACT RATIONAL AND OUTWARD INTERVAL CHECKS PASSED`).
6. External bibliographic verification: fetched `http://www.ueltschi.org/publications.php` (confirmed `uelschi1999` and `uelschi2004` exact; caught `frohlich2005` page range `973–996` vs `973–978`).
7. Temp directory cleanup (`rm -rf C:/t/B2V2Review`): executed after writing this review.
