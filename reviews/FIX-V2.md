# BARRIERS2-V2: delta-review fixes

Findings from `REVIEW-V2.md` (`PASS-WITH-FIXES`: 0 P0, 1 P1, 1 P2, 3 P3) and their
resolution. Source records under `D:/dev/scratch/ceiling-20261118/` were not modified.

Pre-fix state of this directory is preserved: `main.v3.tex`
(`ec5c2f79ab0a2465b307c8ba964258c37495bddba2c27e7d73b3a9ef3f0801ac`), `CLAIMS.v2.md`
(`9e7731ba...8859e381`), `BUILD.v2.md` (`feb73e8e...7cd49299`).

## F1 (P1): `ADIABATIC/PURESSH/REVIEW2.md` exists and lands the second review

**Finding (accepted, fully).** `CLAIMS.md` and `BUILD.md` asserted that
`ADIABATIC/PURESSH/REVIEW2.md` was absent and marked the `U_eff = 0` `PURESSH` items of
Section 5 as pending. The file is present.

**Evidence checked here.** `sha256sum ADIABATIC/PURESSH/REVIEW2.md` =
`25f1115df5b8ce4eb4a246b5a30439ec354d09968cbc8423dd6214fa56926bfe`, matching the
digest in `REVIEW-V2.md` and in the archived published copy
`PUBLISH/barriers2/repo/records/puressh/REVIEW2.md`. Its §1 verdict records all six
first-round findings `F1`-`F6` RESOLVED with every core claim PROVED/CERTIFIED;
`ADIABATIC/PURESSH/FIX.md` §4 resolves its own notes `N1`-`N4`.

**Fix applied.**

- `CLAIMS.md` §0: the `PURESSH` `REVIEW.md` row now also carries the `REVIEW2.md`
  verdict, the digest, and the statement that the `U_eff = 0` items are PROVED.
- `CLAIMS.md` §4 introduction: the sentence that called the `PURESSH` items
  provisional is replaced by the twice-reviewed status.
- `CLAIMS.md` §4 rows for `lem:canon`, `thm:routes` items (i), (ii), (iii) and the
  remark after `thm:routes`: the tag *pending REVIEW2* is removed and the status now
  reads **PROVED**, **CERTIFIED** with `ADIABATIC/PURESSH/REVIEW2.md:1-14` cited in the
  source column.
- `CLAIMS.md` §8: the open item that claimed the file was missing is replaced by a
  record of the landed review and its digest; no provisional status remains.
- `BUILD.md`, "Status of the reviews": the same correction, with the digest.

No statement in `main.tex` changed; the paper never carried the pending tag.

## F2 (P2): page range of Fröhlich and Ueltschi (2005) - REJECTED

**Finding (rejected).** The review states that `refs.bib:89` should read
`pages = {973--996}` and that Ueltschi's publication list gives `973`-`996`.

**Evidence.** The publisher deposit for the cited DOI reports `973`-`978`:

```
curl -s https://api.crossref.org/works/10.1007/s10955-004-2174-y
-> "page": "973-978", "volume": "118", "issue": "5-6",
   "title": "Hund?s Rule and Metallic Ferromagnetism",
   "container-title": "Journal of Statistical Physics"
```

The Semantic Scholar record for the same DOI agrees (`journal.pages` = `973-978`,
volume `118`). The bib entry cites that DOI and nothing else, so its page range
follows the publisher's own metadata for the cited object, and two independent
records of the cited DOI agree with it. The author's publication list carries a
different range; that discrepancy between external bibliographic services is an
external question and does not justify changing bytes that agree with the DOI record. `refs.bib` is therefore unchanged
(`d555d2ec1c57c0cdada78e96400e900c33b52f92967d8f4e0c17fe56ac78a675`), the rendered
reference `[1]` still prints `118(5-6):973-978`, and `BUILD.md` notes that the range
was checked rather than changed.

## F3 (P3): wrong equation reference before `thm:gc`

**Finding (accepted).** The source-augmented graph paragraph named
`\eqref{eq:Hssh}` while `thm:gc` is stated for the general Hubbard-Holstein-SSH
Hamiltonian.

**Fix applied.** `main.tex:878` now reads `\eqref{eq:Hhubssh}`, matching
`MASSIVE/UNIFORM-SSH/AMENDMENT.md:183`.

## F4 (P3): sign in the strong-coupling rate

**Finding (accepted).** The remark after `thm:canon` wrote `$t^2/\Ueff$` for the rates
of `stage6` and `sshbond3`, while attractive interactions have `\Ueff < 0` under the
convention of `eq:Ueff`.

**Fix applied.** `main.tex:1104` now reads `$t^2/|\Ueff|$`, consistent with
`eq:minatt` and the corresponding sentence in `sec:notclaimed`.

## F5 (P3): stale directory name in the companion records

**Finding (accepted).** `CLAIMS.md` and `BUILD.md` still carried the directory name of
the earlier release.

**Fix applied.** The headers now read `BARRIERS2-V2: claim-to-source map` and
`BARRIERS2-V2: build record`, and the build command in `BUILD.md` runs in
`D:/dev/scratch/ceiling-20261118/MASSIVE/BARRIERS2-V2`. The paper itself contains no
directory names.

## Rebuild and checks after the fixes

Commands and observed results, all executed in this directory:

1. `D:/dev/tools/tectonic/tectonic.exe --keep-logs main.tex`: exit 0, `main.pdf`
   21 pages, 230,895 bytes.
2. `grep -c "Overfull\|Underfull\|LaTeX Warning\|Package Warning\|undefined\|Multiply defined" main.log`:
   0. `main.blg` clean; 10 of 10 entries rendered.
3. Text extraction with `pypdf` into `main.txt`: 61,918 characters, 10,966 words; 0 em
   dashes, 5 en dashes (all publisher issue/page ranges in the bibliography), 0 `--`,
   0 `??`; required sentence, byline and AI disclosure present; 0 hits for internal
   naming (`lane`, `worker`, `omp`, `git`, machine names, absolute paths, `scratch`,
   `pending review`), the word `agents` only in the disclosure.

Digests after the fixes: `main.tex` `f45323746d156dfefd4a7d525beeb7bf7e06445a1a7e397db6fe1d4ef7172c2a`,
`main.pdf` `fc2154aa254e88e10df1aca0bcacd35cc24d94ff850339efa87e71248c3faa3c`,
`CLAIMS.md` `b4818379c8f8092e89a380b5114f704639f67118175f28cc9ff37cc0271a7445`,
`refs.bib` unchanged at `d555d2ec1c57c0cdada78e96400e900c33b52f92967d8f4e0c17fe56ac78a675`.

No git operation, publication or spend was performed, and no source record was edited.
