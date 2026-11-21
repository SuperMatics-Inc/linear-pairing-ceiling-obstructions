# BARRIERS2-V2: build record

This record describes the build shipped in this directory: the reviewed text
(`main.v1.tex`), the post-review fixes (verdict of `REVIEW.md`:
`PASS-WITH-FIXES`; findings applied per `FIX.md`, follow-up verdict in
`REVIEW2.md`: `PASS-WITH-FIXES` with the single P2 typo `N1`), the Section 5
generalisation installed from the reviewed `UNIFORM-SSH` record, and the delta-review
fixes recorded in `FIX-V2.md` (delta review `REVIEW-V2.md`: `PASS-WITH-FIXES`).
Snapshots kept alongside: `main.v1.tex` (reviewed by `REVIEW.md`), `main.v2.tex`
(after the twelve fixes, reviewed by `REVIEW2.md`), `main.v3.tex` (after the Section 5
generalisation, before the delta-review fixes), and `CLAIMS.v2.md`/`BUILD.v2.md` (the
claim map and this record before the delta-review fixes).

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
cd D:/dev/scratch/ceiling-20261118/MASSIVE/BARRIERS2-V2
D:/dev/tools/tectonic/tectonic.exe --keep-logs main.tex
```

A single invocation suffices: the engine runs TeX, BibTeX and TeX twice more, then
writes the PDF.

## Build result

- `main.pdf`: 21 pages, 230,895 bytes.
- Overfull boxes: 0. Underfull boxes: 0.
- LaTeX warnings: 0. Package warnings: 0. Undefined references: 0. Undefined
  citations: 0. Multiply-defined labels: 0.
  (Counting command: `grep -c "Overfull\|Underfull\|LaTeX Warning\|Package Warning\|undefined\|Multiply defined" main.log`
  returns 0. The strings `Overfull`/`Underfull`/`LaTeX Warning`/`Package Warning` do
  not otherwise appear in `main.log`; the single line containing the word `warning` is
  the `infwarerr` package banner, which is not a diagnostic.)
- BibTeX: no warning in `main.blg`; all 10 database entries appear in `main.bbl`.

## Acceptance checks (all run after the final build)

| Check | Command | Observed |
|---|---|---|
| Text extraction | `pypdf` on `main.pdf`, output kept as `main.txt` | 21 pages, 61,918 characters, 10,966 words |
| Em dash | count of U+2014 in `main.txt` | 0 |
| En dash | count of U+2013 in `main.txt` | 5, all inside publisher page and issue ranges in the bibliography (`118(5–6):973–978`, `95(3–4):693–717`, `4(2):511–522`); neither the issue ranges nor the page ranges were changed, see `FIX-V2.md` on the rejected finding |
| Double hyphen | count of `--` in `main.txt` | 0 |
| Unresolved references in the rendered text | count of `??` in `main.txt` | 0 |
| Required sentence | substring search for `This preprint has not been peer reviewed.` | present |
| Byline | substring search for author, affiliation, ORCID | present |
| AI-assistance disclosure | substring search | present in "Acknowledgments and disclosures" |
| Internal naming | word-bounded search for `lane`, `worker`, `omp`, `git`, machine names, absolute paths, `scratch`, source-record names, `pending review` | 0 hits; the word `agents` occurs only in the AI disclosure |
| Digests | `sha256sum` over the deliverables | see below |

## Digests (SHA-256)

```
f45323746d156dfefd4a7d525beeb7bf7e06445a1a7e397db6fe1d4ef7172c2a  main.tex
fc2154aa254e88e10df1aca0bcacd35cc24d94ff850339efa87e71248c3faa3c  main.pdf
d555d2ec1c57c0cdada78e96400e900c33b52f92967d8f4e0c17fe56ac78a675  refs.bib
b4818379c8f8092e89a380b5114f704639f67118175f28cc9ff37cc0271a7445  CLAIMS.md
96bd60103d690909dc49b6bd9bb47165b3ed4fc78d5bcd15d4159bbdd04548f0  FIX.md
910f931944aabb151f86c3e99b9de8971c9798fb85be8995e968be8403b1bf02  FIX-V2.md
```

Pre-fix snapshots kept for traceability:

```
ec5c2f79ab0a2465b307c8ba964258c37495bddba2c27e7d73b3a9ef3f0801ac  main.v3.tex
9e7731ba531b04550ecf82d72d1a16e1a789eb53f110588948c7d3878859e381  CLAIMS.v2.md
feb73e8e0a9942cd40993f9f402c1e399a6f1c89b51d1dbc6795734f7cd49299  BUILD.v2.md
```

`main.v3.tex` is the text that `REVIEW-V2.md` checked; it no longer equals `main.tex`,
whose current digest appears in the first block. `refs.bib` is byte-identical to the
bytes the delta review checked, as recorded in `FIX-V2.md`.

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
  applied.
- `REVIEW-V2.md` (this directory): `PASS-WITH-FIXES` (0 P0, 1 P1, 1 P2, 3 P3); the
  findings are closed in `FIX-V2.md`.
- `MASSIVE/STATIC-MODE`, `MASSIVE/LINEAR-FRESH`: independent `PASS`.
- `MASSIVE/UNIFORM-SSH`: `REVIEW.md` `PASS-WITH-FIXES`, `REVIEW2.md` `PASS`. The
  transcription into this paper has not had a separate independent review of its own;
  the reviewed statements are those of the source record, and `REVIEW-V2.md` checked
  the transcription against them.
- `ADIABATIC/PURESSH`: `REVIEW.md` `PASS`; `REVIEW2.md` (SHA-256
  `25f1115df5b8ce4eb4a246b5a30439ec354d09968cbc8423dd6214fa56926bfe`)
  `PASS-WITH-FIXES` with all six first-round findings resolved, and
  `ADIABATIC/PURESSH/FIX.md` §4 closes its notes `N1`-`N4`. Every `PURESSH` item in
  Section 5 is therefore PROVED on twice-reviewed source text; no provisional status
  remains in `CLAIMS.md`.

## Source immutability

No source record was modified. This directory contains the paper (`main.tex`), its
bibliography, the built PDF, the extracted text used by the checks (`main.txt`), the
reviewed snapshots (`main.v1.tex`, `main.v2.tex`, `main.v3.tex`, `CLAIMS.v1.md`,
`CLAIMS.v2.md`, `BUILD.v2.md`), the reviews (`REVIEW.md`, `REVIEW2.md`,
`REVIEW-V2.md`), the fix records (`FIX.md`, `FIX-V2.md`), the claim map (`CLAIMS.md`)
and this record. The replay suite referenced by the paper's data-availability section
is a separate deposit; it is not part of this directory.

## Release build, version 1.1.0

The deposited manuscript is the reviewed text and the reviewed build, byte for
byte: `paper/main.tex` (81,203 bytes, SHA-256
`f45323746d156dfefd4a7d525beeb7bf7e06445a1a7e397db6fe1d4ef7172c2a`) is this
directory's reviewed source with no release-metadata edits, `paper/refs.bib`
(2,746 bytes, SHA-256
`d555d2ec1c57c0cdada78e96400e900c33b52f92967d8f4e0c17fe56ac78a675`) is the reviewed
bibliography, and `paper/main.pdf` (230,895 bytes, SHA-256
`fc2154aa254e88e10df1aca0bcacd35cc24d94ff850339efa87e71248c3faa3c`) is the reviewed
PDF built from those two files. Only em dashes are excluded from the released text;
the en dashes in bibliographic page and issue ranges (`693--717`, `511--522`,
`973--978`, `3--4`, `5--6`) are reviewed typography and are kept.

The manuscript therefore carries no DOI and no repository URL. The version 2 DOIs,
the version 1 DOIs, the supplement DOI and the source repository are recorded in the
Zenodo record metadata, in `README.md` and in `CITATION.cff`, not in the deposited
paper.

The build command is

```
SOURCE_DATE_EPOCH=1795132800 D:/dev/tools/tectonic/tectonic.exe --keep-logs main.tex
```

A rebuild of these two files under that epoch exits `0` and reproduces the same
21-page text with the same checks, but not the same bytes: Tectonic records its own
creation date and trailer, so the rebuild is a few bytes shorter. The hosted CI
therefore rebuilds the paper, fails on any overfull box, underfull box or undefined
reference, and re-runs the text checks on its own PDF; it does not pin the PDF bytes.

`main.log` of the deposited build reports 0 `Overfull`, 0 `Underfull` and 0
`undefined` lines, and `main.blg` carries no warning. The text checks were re-run on
the deposited PDF and all pass: no em dash, the exact sentence "This preprint has not
been peer reviewed.", the AI disclosure and the byline are present, and no internal
lane, agent, machine or path token appears outside the disclosure. The only URL
annotation in the PDF is the author ORCID.
