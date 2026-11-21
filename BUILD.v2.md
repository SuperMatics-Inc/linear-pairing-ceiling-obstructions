# BARRIERS2-PAPER: build record

This record describes the build shipped in this directory: the reviewed text
(`main.v1.tex`), the post-review fixes (verdict of `REVIEW.md`:
`PASS-WITH-FIXES`; findings applied per `FIX.md`, follow-up verdict in
`REVIEW2.md`: `PASS-WITH-FIXES` with the single P2 typo `N1`), and the Section 5
generalisation installed from the reviewed `UNIFORM-SSH` record. Snapshots kept
alongside: `main.v1.tex` (reviewed by `REVIEW.md`), `main.v2.tex` (after the twelve
fixes, reviewed by `REVIEW2.md`), `main.v3.tex` (after the Section 5 generalisation;
byte-identical to `main.tex`).

## Toolchain

- TeX engine: Tectonic 0.17.0 at `D:/dev/tools/tectonic/tectonic.exe` (single binary,
  fetches and pins its own bundle, runs BibTeX itself).
- Document class `article`, 11pt, `geometry` 1in margins,
  `amsmath`/`amssymb`/`amsthm`/`mathtools`, `hyperref`, `microtype`, `enumitem`,
  `array`.
- Bibliography: `plain` style over the local `refs.bib` (10 entries, all cited;
  matching `main.bbl`).

## Build command

```
cd D:/dev/scratch/ceiling-20261118/MASSIVE/BARRIERS2-PAPER
D:/dev/tools/tectonic/tectonic.exe --keep-logs main.tex
```

A single invocation suffices: the engine runs TeX, BibTeX and TeX twice more, then
writes the PDF.

## Build result

- `main.pdf`: 21 pages, 230,911 bytes.
- Overfull boxes: 0. Underfull boxes: 0.
- LaTeX warnings: 0. Package warnings: 0. Undefined references: 0. Undefined
  citations: 0. Multiply-defined labels: 0.
  (Counting command: `grep -c "Overfull\|Underfull\|LaTeX Warning\|Package Warning\|undefined\|Multiply defined" main.log`
  returns 0. The strings `Overfull`/`Underfull`/`Warning` do not otherwise appear in
  `main.log`; the single line containing the word `warning` is the `infwarerr` package
  banner, which is not a diagnostic.)
- BibTeX: no warning in `main.blg`; all 10 database entries appear in `main.bbl`.

## Acceptance checks (all run after the final build)

| Check | Command | Observed |
|---|---|---|
| Text extraction | `pypdf` on `main.pdf`, output kept as `main.txt` | 21 pages, 61,917 characters, 10,967 words |
| Em dash | count of U+2014 in `main.txt` | 0 |
| En dash | count of U+2013 in `main.txt` | 5, all inside publisher page and issue ranges in the bibliography (`118(5–6):973–978`, `95(3–4):693–717`, `4(2):511–522`) |
| Double hyphen | count of `--` in `main.txt` | 0 |
| Unresolved references in the rendered text | count of `??` in `main.txt` | 0 |
| Required sentence | substring search for `This preprint has not been peer reviewed.` | present |
| Byline | substring search for author, affiliation, ORCID | present |
| AI-assistance disclosure | substring search | present in "Acknowledgments and disclosures" |
| Internal naming | word-bounded search for `lane`, `worker`, `git`, machine names, absolute paths, `scratch`, source-record names, `pending review` | 0 hits; `agent` occurs twice, both inside the AI disclosure |
| Digests | `sha256sum` over the deliverables | see below |

## Digests (SHA-256)

```
ec5c2f79ab0a2465b307c8ba964258c37495bddba2c27e7d73b3a9ef3f0801ac  main.tex
ec5c2f79ab0a2465b307c8ba964258c37495bddba2c27e7d73b3a9ef3f0801ac  main.v3.tex  (identical to main.tex)
ddd3554830b187b538f1065051a8f5cb0a52010a41f53569fb801367995cd3c2  main.pdf
d555d2ec1c57c0cdada78e96400e900c33b52f92967d8f4e0c17fe56ac78a675  refs.bib
9e7731ba531b04550ecf82d72d1a16e1a789eb53f110588948c7d3878859e381  CLAIMS.md
96bd60103d690909dc49b6bd9bb47165b3ed4fc78d5bcd15d4159bbdd04548f0  FIX.md
```

(The `main.v3.tex` line above repeats the `main.tex` digest; the file was produced by
copying `main.tex` after the final edit, and `sha256sum main.tex main.v3.tex` prints
the same value twice.)

## Source records behind the paper

| Record | Content used here |
|---|---|
| `MASSIVE/STATIC-MODE/` | Section 3 (integrated first dynamic cumulant, three-site witness, torus embedding) |
| `MASSIVE/LINEAR-FRESH/` | Section 4 (positive-determinant amplification, `f`-sum lemma, two-slice fixture, Ward and dimer remarks) |
| `MASSIVE/UNIFORM-SSH/` | The `U_eff`-uniform half of Section 5 (Theorems 1.1-1.5), transcribed per `AMENDMENT.md` |
| `ADIABATIC/PURESSH/` | The `U_eff = 0` route obstructions of Section 5 and the constants inherited by the uniform bounds |

External numerics are quoted only for bibliographic identification of cited
classical results (oscillator sum rule, Ueltschi hopping expansions and their
Holstein extension); no external data set is used.

## Status of the reviews

- `REVIEW.md` (this directory): `PASS-WITH-FIXES`, 12 findings, all applied.
- `REVIEW2.md` (this directory): `PASS-WITH-FIXES`, all 12 findings RESOLVED, one new
  P2 typo `N1` (`value` for `derivative` in the proof summary of `thm:canon`),
  applied at the start of this build round.
- `MASSIVE/STATIC-MODE`, `MASSIVE/LINEAR-FRESH`: independent `PASS`.
- `MASSIVE/UNIFORM-SSH`: `REVIEW.md` `PASS-WITH-FIXES`, `REVIEW2.md` `PASS`. The
  transcription into this paper has not had a separate independent review; the
  reviewed statements are those of the source record.
- `ADIABATIC/PURESSH`: `REVIEW.md` `PASS`; `REVIEW2.md` is absent from the source
  record at build time, so Section 5 items that rest on `PURESSH` alone are marked
  *pending REVIEW2* in `CLAIMS.md`.

## Source immutability

No source record was modified. This directory contains the paper (`main.tex`), its
bibliography, the built PDF, the extracted text used by the checks (`main.txt`), the
reviewed snapshots (`main.v1.tex`, `main.v2.tex`, `main.v3.tex`, `CLAIMS.v1.md`), the
review (`REVIEW.md`), the follow-up review (`REVIEW2.md`), the fixes record
(`FIX.md`), the claim map (`CLAIMS.md`) and this record. The replay suite referenced
by the paper's data-availability section is a separate deposit; it is not part of this
directory.
