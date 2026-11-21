# Build record

This record describes the build shipped in `paper/`: the version 3 manuscript
(`main.tex`), its bibliography (`refs.bib`) and the built PDF (`main.pdf`). The
version 1 and version 2 sources and their build records are in the tagged history of
this repository.

## Toolchain

- TeX engine: Tectonic 0.17.0, XeTeX engine, single binary that fetches and pins its
  own bundle and runs BibTeX itself.
- Document class `article`, 11pt, `geometry` 1in margins,
  `amsmath`/`amssymb`/`amsthm`/`mathtools`, `hyperref`, `microtype`, `enumitem`,
  `array`.
- Bibliography: `plain` style over the local `refs.bib` (10 entries, all cited).

## Build command

```
SOURCE_DATE_EPOCH=1795132800 tectonic -X compile --keep-logs main.tex
```

run in `paper/`. One invocation suffices: the engine runs TeX, BibTeX and TeX twice
more, then writes the PDF. A second run needs no network because Tectonic caches the
bundle.

## Build result

- `main.pdf`: 29 pages, 287,920 bytes.
- Overfull boxes: 0. Underfull boxes: 0.
- Undefined references: 0. Undefined citations: 0.
- No line of `main.log` contains `Warning`.
- BibTeX: no warning; all 10 database entries appear in the bibliography.

## Acceptance checks

| Check | Method | Observed |
|---|---|---|
| Text extraction | `pypdf` over `main.pdf` | 29 pages, 86,169 characters |
| Em dash | count of U+2014 in the extracted text | 0 |
| En dash | count of U+2013 in the extracted text | 5, all inside bibliographic page and issue ranges (`118(5-6):973-996`, `95(3-4):693-717`, `4(2):511-522`) |
| Unresolved references | count of `??` in the extracted text | 0 |
| Required sentence | substring search for `This preprint has not been peer reviewed.` | present once, in the disclosure section |
| Byline | substring search for `Davis Rens`, `SuperMatics Inc.`, `ORCID 0000-0001-5839-5197` | all present |
| AI-assistance disclosure | substring search | present, the same wording as the released version 2 |
| Internal naming | word-bounded search for repository paths, machine names, campaign directories, review-record names and `pending review` | 0 hits; the word `agents` occurs only in the AI disclosure |
| URL annotations | `pdfinfo -url` | the author ORCID and the version 2 DOI of this preprint, which the version note cites; nothing else |

## Digests

```
e0771310354e977e7be635ebddc6bdf8925ce45615809efaa69d1a9915d222af  paper/main.tex       111349 bytes
0dde52227a21bf56b996d6395d06fb04b0c2aae8b845cb9a365567c1d6e7f5c0  paper/refs.bib         2746 bytes
9450e22ef9d0c36c376d6000dfedd77be1d7918278c1d10c314d30c6896ab3a7  paper/main.pdf       287920 bytes
```

Tectonic records its own creation date and trailer in the PDF, so `paper/main.pdf`
identifies exactly the deposited bytes below and a rebuild on another date produces
the same content with a different digest. `paper/main.tex` and `paper/refs.bib`
rebuild byte-identically.

## Version 3 relative to version 2

Version 3 supersedes version 2 (paper `10.5281/zenodo.24409383`, supplement
`10.5281/zenodo.24409388`) and leaves every statement of version 2 intact. It adds
the annealed-static section, records the two syntheses of that section as HEURISTIC,
updates the open-problem and not-claimed lists so that the annealed route is recorded
there, and corrects the page range of one cited article. The claim-to-source map is
`CLAIMS.md`.

## Release bytes

The deposited manuscript is the reviewed text and the reviewed build, byte for byte,
with no release-metadata edit:

| File | Bytes | SHA-256 |
|---|---|---|
| `linear-pairing-ceiling-obstructions-paper.pdf` | 287920 | `9450e22ef9d0c36c376d6000dfedd77be1d7918278c1d10c314d30c6896ab3a7` |

The manuscript carries no new DOI: its title page and version note cite only the
version 2 DOI that version 3 supersedes. The version 3 DOIs, the earlier version
DOIs, the supplement DOI and this repository are recorded in the Zenodo record
metadata, in `README.md` and in `CITATION.cff`.

Only em dashes are excluded from the released text; the en dashes in bibliographic
page and issue ranges are reviewed typography and are kept.

## Reproducibility of the deposited PDF

A rebuild of `paper/main.tex` and `paper/refs.bib` with Tectonic 0.17.0 under
`SOURCE_DATE_EPOCH=1795132800` exits 0 with no warning and reproduces `main.pdf` byte
for byte, so the digest above is reproducible on a machine with the pinned engine.
Without the epoch Tectonic records the build date in the PDF and the digest changes,
which is why the build is only byte-reproducible under the pinned epoch. The hosted
CI rebuilds the paper under the same epoch, fails on any overfull box, underfull box
or undefined reference, and re-runs the text checks on its own PDF; it reports the
digest of its PDF without failing on it, because a byte difference between platforms
must not block a correct build.

## Reviews

The version 3 text was reviewed in two rounds. The delta review of the assembled
version returned `PASS-WITH-FIXES` (0 P0, 3 P1, 5 P2, 3 P3); every finding was
applied, and the re-review of the fixed text returned `PASS-WITH-MINOR-FIXES`
(0 P0, 0 P1, 1 P2, 1 P3). Both minor findings are applied in the released bytes: the
version note states only what version 3 changes and no longer claims a change that
version 3 does not make, and the build record of the deposited PDF reports the
digests of the files it ships.
The review records themselves are not shipped in this tree; they are part of the
version 1.0.0 and 1.1.0 history and of the review rounds of the source records listed
in `CLAIMS.md`.
