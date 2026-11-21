# BARRIERS2-PAPER: build record

This record describes the final build, after the corrections listed in `FIX.md`
(resolution of `REVIEW.md`, verdict `PASS-WITH-FIXES`). The reviewed text is kept as
`main.v1.tex` and the reviewed claim map as `CLAIMS.v1.md`.

## Toolchain

- TeX engine: Tectonic 0.17.0 at `D:/dev/tools/tectonic/tectonic.exe`
  (single binary, fetches and pins its own bundle, runs BibTeX itself).
- Document class `article`, 11pt, `geometry` 1in margins, `amsmath`/`amssymb`/
  `amsthm`/`mathtools`, `hyperref`, `microtype`, `enumitem`, `array`.
- Bibliography: `plain` style over the local `refs.bib` (7 entries, all cited).

## Build command

```
cd D:/dev/scratch/ceiling-20261118/MASSIVE/BARRIERS2-PAPER
D:/dev/tools/tectonic/tectonic.exe --keep-logs main.tex
```

`--keep-logs` keeps `main.log`; add `--keep-intermediates` to keep `main.aux`,
`main.bbl` and `main.blg` as well. Exit status of the recorded build: `0`
(wall time 1.6 s).

Recorded artifacts:

| file | bytes | sha256 / notes |
|---|---|---|
| `main.pdf` | 197114 | 18 pages, 9343 words in the extracted text |
| `main.tex` | 65075 | `dc183d15a0a8d6b1736cc02eeadafd6f3e62c522b77a8878daa61671a4d3f4b6` |
| `refs.bib` | 1806 | `dfdf71b495806aff341f15aa0c5506db25428ec063f04054a1e43be89b7eb896`, 7 released-preprint entries |
| `CLAIMS.md` | 18842 | `a8b36ca8d3c146b96097a5f56b55726919106b71a44794fa03ad22af9ae0a740` |
| `FIX.md` | 8155 | `fd51a479d98622a5ff1e226a553110c2dcb63f64a8b9593e125bfd5f46eee677` |
| `main.txt` | 52279 | extracted PDF text, used only for the checks below |
| `main.v1.tex` | 60129 | reviewed text, `d7cc050845f1fd5a0603d6941f17ffbb1f6a3a7b8b49d2cca3c4ec5134d86a9a` |
| `CLAIMS.v1.md` | 13695 | reviewed claim map, `dca28e6cfa6a4c4e799242cbc1e73e570d04bb84bfb3a87f65273ed05e7fb562` |
| `REVIEW.md` | 18548 | untouched, `5576014f1f459c7e38edc2c4faad2b9c3e22078977bff931de0161ab12a78b5c` |

The PDF is not byte-reproducible: Tectonic records a creation date and a document ID
in every run, so two builds of the identical `main.tex` differ in their sha256 while
agreeing in page count, byte size and extracted text (checked over two consecutive
builds of the recorded source). Reproducibility is therefore recorded at the level of
`main.tex` plus the artifact properties above, not as a PDF hash.

## Warnings

Recorded build, `main.log` 14842 bytes:

- Overfull boxes: **0** (`grep -c "Overfull" main.log` gives 0).
- Underfull boxes: **0** (`grep -c "Underfull" main.log` gives 0).
- Lines containing `undefined`: **0**, so no undefined references, undefined
  citations, multiply defined labels or missing bibliography entries.
- `main.blg` is 185 bytes and carries no warning or error.
- The `Fontconfig error: Cannot load default config file` line that the Tectonic
  executable prints on this host is a font-cache message from the bundled
  XeTeX/xdvipdfmx pipeline, not a document warning; it appears on every build here and
  does not affect the output. It is the only diagnostic of the build.

## Verification checks run on the built PDF

Text was extracted with `pypdf` over all 18 pages into `main.txt` (51034 text
characters), then checked on the extracted text:

| check | result |
|---|---|
| em dash `U+2014` | 0 occurrences |
| en dash `U+2013` | 0 occurrences |
| doubled hyphen `--` | 0 occurrences |
| the word `lane` / `agent` / `worker` / `git` | 0 occurrences (the only hits for the letters `agent` are the two words inside the required AI-assistance disclosure) |
| machine names, file paths, repository names | none (`C:/`, `D:/`, `scratch` all 0) |
| `This preprint has not been peer reviewed.` (exact sentence) | present |
| AI-assistance disclosure | present, verbatim as in the released BARRIERS note |
| author byline `Davis Rens`, affiliation `SuperMatics Inc.`, ORCID `0000-0001-5839-5197` | present |
| `??` (unresolved cross-reference) | 0 |
| `T_pair`, `T_lin` used for model quantities only; no measured `T_c` and no materials claim | confirmed by reading |

The first PDF-level review run of the same source family also confirmed that all 68
labels resolve and that `main.tex` contains no draft-language string.

## Bibliography verification

Every entry is a SuperMatics preprint released on Zenodo. Each DOI string and title
was taken from a released record in this series and compared programmatically against
it, not retyped from memory: `MASSIVE/CAPSTONE-PAPER/refs.bib` carries six of the
seven entries, `ADIABATIC/BARRIERS-PAPER/refs.bib`,
`ADIABATIC/LINEAR4-PAPER/refs.bib`, `ADIABATIC/LINEAR5-PAPER/refs.bib` and
`ADIABATIC/SSHBOUND3-PAPER/refs.bib` corroborate the rest, and the `SSHBOUND3` entry
itself comes from that paper's own `main.tex` (`\PAPERDOI` on line 10 and `\title` on
line 13). No external reference was added, so no bibliography outside this
series needed verification. The seven entries and their verified titles are:

| key | DOI | title as in the released record |
|---|---|---|
| `barriers` | 10.5281/zenodo.24384373 | Determinant zeros and method-specific barriers to linear-in-frequency pairing bounds in the Holstein model |
| `sshbound3` | 10.5281/zenodo.24406987 | An explicit pair bound for the attractive Hubbard model with bond SSH coupling |
| `linear5` | 10.5281/zenodo.24374043 | Imaginary-time estimates and method barriers beyond the two-thirds adiabatic bound |
| `limits` | 10.5281/zenodo.24385569 | Limits of defect-insertion bounds for slow-phonon pair order in the Holstein model |
| `stage6` | 10.5281/zenodo.24380128 | Strong-coupling suppression of electronic pair order in the Holstein model, uniformly in phonon frequency and without a hopping cutoff |
| `slow` | 10.5281/zenodo.24366508 | Suppression of electronic pair order for slow lattice phonons |
| `linear4` | 10.5281/zenodo.24372238 | A two-thirds-power adiabatic bound for electronic pair order |

## Source immutability

No source record was modified. This directory contains the paper (`main.tex`), its
bibliography, the built PDF, the extracted text used for the checks, the reviewed
snapshots (`main.v1.tex`, `CLAIMS.v1.md`), the review (`REVIEW.md`) and the two
companion records `CLAIMS.md` and `FIX.md`. The replay suite referenced by the
paper's data-availability section is a separate deposit; it is not part of this
directory.

## Release build, version 1.0.0

The sections above record the build of the working record in
`MASSIVE/BARRIERS2-PAPER`, whose reviewed source is archived there as `main.v1.tex`,
`main.v2.tex` and `main.v3.tex`. The release copy in `paper/main.tex` differs from
that source (`main.v3.tex`, SHA-256
`acc237f1313d83d81f4b0fb12d930c15260be60dd9bf430958677aa8df1d875a`, 65080 bytes) in
release metadata only, with no change to any mathematical statement, constant, proof
or scope:

- three macro definitions after `\date{}`: `\PAPERDOI` = `10.5281/zenodo.24408871`,
  `\SUPPDOI` = `10.5281/zenodo.24408875`, `\REPOURL` =
  `https://github.com/SuperMatics-Inc/linear-pairing-ceiling-obstructions`;
- a five-line centred block after `\maketitle` printing the article DOI, the
  supplement DOI and the source-repository URL;
- the data-availability paragraph now names the deposited supplement DOI, the
  source-repository URL and the article DOI, replacing the sentence that announced
  the supplement as a future deposit.

The release build sets `SOURCE_DATE_EPOCH=1795132800` (2026-11-20T00:00:00Z) so that
the hosted CI build and a local build reproduce the same bytes:

```
SOURCE_DATE_EPOCH=1795132800 D:/dev/tools/tectonic/tectonic.exe --keep-logs main.tex
```

Exit status `0`, 18 pages, 201715 bytes, SHA-256
`bbbf3bf89fa392ebd4bf3585e01f672e136f97a5b764492a485490a00f2f7a77`. Two consecutive
builds of the same source under that epoch produced identical bytes. `main.log`
reports 0 `Overfull`, 0 `Underfull` and 0 `undefined` lines, and `main.blg` carries
no warning. The text, dash, disclosure, byline and internal-token checks of the
section above were re-run on the release PDF and all pass; the PDF now also carries
four URL annotations (the ORCID, both DOIs and the repository) with the supplement,
repository and article DOIs repeated in the data-availability paragraph.
