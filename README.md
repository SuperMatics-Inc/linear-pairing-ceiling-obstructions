# Method obstructions to linear-in-frequency pairing ceilings in electron-phonon models

Davis Rens  
SuperMatics Inc.  
[ORCID 0000-0001-5839-5197](https://orcid.org/0000-0001-5839-5197)  
Version 1.0.0

Paper DOI: <https://doi.org/10.5281/zenodo.24408871>  
Replay supplement DOI: <https://doi.org/10.5281/zenodo.24408875>  
Source: <https://github.com/SuperMatics-Inc/linear-pairing-ceiling-obstructions>

This repository accompanies the preprint *Method obstructions to linear-in-frequency pairing ceilings in electron-phonon models: integrated cumulants, positive determinants, and the vanishing effective attraction*. The manuscript source and bibliography are in `paper/`. The statement-to-source map is `CLAIMS.md`, and the build record is `BUILD.md`. The proof, replay and review records are grouped in `records/` as `static-mode`, `linear-fresh` and `puressh`, matching the three obstruction groups of the paper. `MANIFEST.sha256` pins every file in this repository except itself. `ADMITTED.sha256` records the accepted bytes of the shipped files.

## Mathematical scope

The paper asks whether the pair-ordering temperature of a Holstein or bond-SSH electron-phonon model can be bounded at a temperature scale proportional to the phonon frequency, uniformly in that frequency and at fixed hopping and coupling. That linear step remains open and the paper does not close it.

Three exact obstructions restrict which proof methods can reach such a bound. For the Holstein model with arbitrary real static site fields, the exact first coefficient of the local dynamic cumulant, with the dynamic Gaussian already integrated out, is at least `U Omega^2/(1200 tau^3)` on an open three-site path for `0 < Omega <= tau <= t/4`, and at least `U Omega^2/(2400 tau^3)` on every square torus of side at least four with a finite static barrier. On a two-slice history the fermion determinant exceeds one, all monodromy eigenvalues are positive, and the conditional impurity Green function still grows as `B^2/(2 v^2)`, with an interval-certified fixture at `B = 6`, `v = 1/2` giving `det(1+U) > 15` and `|G(1,0)_00| > 52.89`. For the pure bond-SSH model at vanishing effective attraction the high-temperature regime is closed by a frequency-uniform polymer expansion, and three further routes are obstructed by exact identities.

One case survives: for the pure bond-SSH model with vanishing effective attraction and `beta|t| + beta G_b <= 2^-10`, the pair correlator is at most `(341/103)(32/341)^d` uniformly in frequency, chemical potential and density, so `k_B T_pair <= 1024(|t| + G_b)`.

The bounds are on the model quantities `T_pair` and `T_lin`. They are not bounds on a measured transition temperature, they confirm no superconductor, and they make no materials claim. The replays check finite algebraic statements, exact rational identities, outward-rounded intervals and finite-matrix diagnostics with guarded mutants; they do not formalize the analytic arguments, and the finite-matrix computations are numerical sanity checks that are not part of any proof.

## Records

| Record | Directory | Contents |
|---|---|---|
| `static-mode` | `records/static-mode/` | Exact first dynamic cumulant in the Holstein model with arbitrary real static site fields: the three-site resonance witness, its square-torus embedding, exact rational constant guards, and numerical covariance and Hessian diagnostics. |
| `linear-fresh` | `records/linear-fresh/` | Interacting nonzero-Matsubara sum rule, the two-slice conditional amplification witness, its interval-certified fixture, the finite-matrix Ward and Schur algebra with the auxiliary-series enclosure, and two static dimer anchors. |
| `puressh` | `records/puressh/` | Finite-temperature and canonical bond-SSH record: the frequency-uniform pair bound at vanishing effective attraction, the exact constants, and the three obstructed routes together with the finite exact-diagonalisation checks. |

## Replay

Python 3.12 is used with pinned dependencies: `numpy==2.5.5`, `scipy==1.18.1`, `sympy==1.14.0`, `mpmath==1.4.1`, `python-flint==0.9.0`. From the repository root:

```sh
python -m pip install numpy==2.5.5 scipy==1.18.1 mpmath==1.4.1 python-flint==0.9.0
python -m pip install --no-deps sympy==1.14.0
(cd records/static-mode && python -B replay.py)
(cd records/linear-fresh && python -B replay.py && python -B replay.py --all-mutants && python -B independent.py)
(cd records/puressh && python -B replay.py && python -B replay.py --all-mutants && python -B ed_check.py)
```

`sympy` is installed without its dependency solver because it declares `mpmath<1.4` while this suite runs on `mpmath==1.4.1`; its only runtime requirement is `mpmath` itself.

Every command above exits 0 on a correct tree. In each record `replay.py` exits 0 when its fixtures pass, and the guarded-mutant drivers reject every corrupted variant, 16 in `linear-fresh` and 12 in `puressh`, each rejected run exiting 1. `records/static-mode/CHECKS.txt` records the retained failure of the first run of that replay and the numerically diagnosed fix that resolved it.

CI (`.github/workflows/ci.yml`) verifies `MANIFEST.sha256` and `ADMITTED.sha256`, runs the replays above and pins their pass markers, applies the public prose safeguards to the manuscript and this README, and builds the paper with Tectonic, failing on any overfull box, underfull box or undefined reference.

## Disclosure and review

AI agents generated the proofs, code, and manuscript drafts under D. Rens' direction. Separate AI agents performed the independent reviews. This preprint has not been peer reviewed.

## Rights

The manuscript text and bibliography in `paper/` are distributed under CC-BY-4.0 through the paper record. The replay code, records and other software materials in this repository are distributed under Apache-2.0. The paper's license does not change the software license.
