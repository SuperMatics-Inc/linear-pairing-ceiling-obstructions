# Linear-frequency pairing ceiling: a new method obstruction

Davis Rens, SuperMatics Inc. ORCID 0000-0001-5839-5197.
20 November 2026.

## Verdict

**The linear step remains OPEN.** No upper bound of the form k_B T_pair <= C Omega, or C sqrt(lambda) Omega, has been proved here. No model counterexample with T_pair >> Omega has been shown. The reviewed LINEAR4 two-thirds-power bound and the STAGE7R strong-coupling bound are not improved.

**PROVED (pending independent review):** the analytical drafts in RIGOR.md establish an exact interacting nonzero-Matsubara phonon sum rule and an arbitrary-amplification family for a determinant-positive single-impurity propagator. They also give exact finite-matrix Ward-Schur identities and two-site static electronic anchors. A second implementation checks specified fixtures; it is not independent scientific review.

**CERTIFIED, narrow computational scope only:** the fixed two-slice interval witness and the auxiliary series enclosure, not a temperature bound. Floating-point ED, sampled Matsubara matrices and normal-state DMFT diagnostics are **NUMERICAL**. No material is identified as a confirmed superconductor. There are no measurements in this package.

AI agents generated the proofs, code and drafts. This work has not been peer reviewed.

## What is new

### Exact interacting spectral control

For H = H_el + sum_x [P_x^2/(2M_x)+K_x X_x^2/2-F_x X_x Q_x], with a finite electronic Fock space, bounded Q_x, positive springs and masses, let U_x=F_x^2/K_x, Omega_x^2=K_x/M_x, b_x=F_x X_x and tau=k_B T. At nonzero bosonic Matsubara frequency nu_k=2pi k tau,

```
0 <= C_x(i nu_k) <= U_x Omega_x^2/nu_k^2,
E|b_{x,k}|^2 <= U_x Omega_x^2/(4pi^2 k^2 tau),
sum_{k>=1} E|b_{x,k}|^2 <= U_x Omega_x^2/(24 tau).
```

The spectral bound follows from [b_x,[H,b_x]]=U_x Omega_x^2 and the exact Lehmann representation. It remains valid with Hubbard repulsion and at fixed electron number. A positive Euclidean representation is an additional hypothesis for the probabilistic interpretation, not for the spectral theorem. Counting both signs of k doubles 1/24 to 1/12. The oscillator Hilbert space in this proof is not truncated.

**Method consequence:** determinant tilting does not destroy this nonzero-frequency second-moment bound. But this does not give zero-mode, joint concentration or resolvent-weighted control. Replacing an interacting second moment by a pathwise fluctuation bound remains invalid.

### Positive-determinant arbitrary Green amplification

One impurity plus one bath orbital already suffices. With hopping v>0, beta=2, and impurity potential -B in the first unit-time interval and +B in the second, the one-particle propagator has positive eigenvalues and det(I+U)>1. Nevertheless,

```
|G(1,0)_{00}| ~ B^2/(2v^2) -> infinity.
```

RIGOR.md gives an explicit scalar formula and a divergent lower bound. The finite-B witness persists under smoothing to periodic finite-action phonon histories. No claim is made about their annealed probability or an averaged Green-function divergence.

**Method obstruction:** positivity/nonvanishing of the electronic determinant cannot justify a history-independent CAR/Gram bound on the conditional propagator. This blocks one concrete way of turning phonon second moments into a uniform single-impurity/DMFT pairing bound. It does not block all annealed DMFT arguments or all linear-frequency ceilings.

### Exact anchors and their limitations

- Finite-matrix Ward-Schur algebra identifies the negative-frequency leakage term, including its factor two. The needed annealed leakage bound is not proved.
- The two-site COM oscillator decouples at fixed electron number after a canonical displacement. The unshifted COM number is not conserved in general.
- In the static two-electron dimer, the relaxed BO minima for U>t have a bare electronic pair expectation t^2/(4U^2). At U=4,t=1 this is 1/64, while the unrelaxed field q=2U gives 1/68. This is intra-well electronic admixture, not inter-well phonon tunnelling and not thermodynamic order.
- The auxiliary sum C_aux = sum_{k>=1}[2+log(2k-1)]/(2k^3) lies in (67/50,27/20), with an explicit tail bound and two interval implementations. It upper-bounds a Hankel second moment at scale U Omega^2/tau^3. It is not a ceiling coefficient, and it does not improve the two-thirds-power temperature scale.

## Disposition of the four proposed routes

| Route | Outcome | Exact unresolved step |
|---|---|---|
| Reflection positivity / infrared | Free optical phonon covariance has no spatial q-stiffness; ordinary balanced canonical RP already fails in the prior paper | A valid modified interacting reflection and a phonon-to-pair domination theorem |
| Slow-variable / Born-Oppenheimer | Exact nonzero-frequency second moment and exact static dimer landscape | Volume-uniform quantum correction and joint weighted rare-history/coherence control |
| DMFT / exactly solvable anchors | New arbitrary-amplification obstruction, exact finite algebra, static finite-cluster anchors | Exact infinite-grid singlet kernel, annealed leakage estimate and its relation to model T_pair |
| Peierls / phonon-assisted tunnelling | Exact bare pair admixture is not a tunnelling observable | Controlled many-site dressed-pair coherence and phonon Hilbert-space error bounds |

No defect insertion, polymer, ladder expansion or LINEAR12 variant was restarted. RIGOR.md identifies the relevant prior canonical RP obstruction and distinguishes it from the new impurity result.

## Numerical evidence and preserved negatives

The ED calculations use finite relative-oscillator bases (80 or 120 states), with no interval spectral solver or certified omitted-tail estimate. Their small doublet gaps, displaced-operator expectations and bare pair expectations are therefore **NUMERICAL**, not a theorem for the full phonon Hilbert space. A finite dimer has no thermodynamic transition.

The small normal-state Bethe-DMFT diagnostic uses a finite Matsubara grid, sampled dynamic modes, a finite static grid and only ten fixed-point updates. It has no demonstrated continuum-grid, quadrature, sampling or self-consistency convergence. Its replay guard is a numerical diagnostic, not evidence for exact DMFT, a transition temperature, or the linear conjecture.

An earlier guard at U=1, Omega=0.1, T/Omega=0.10 failed because the numerical normalized leakage exceeded one: 1.4212687734.... That negative is retained. The final guard at T/Omega=0.15 checks a different diagnostic point; it does not invalidate the earlier failure or certify a bound. Exploratory scan scripts under the temporary C: scratch directory are not admitted evidence of a Tc, convergence or a theorem.

## Evidence and reproducibility

Files:

- `RIGOR.md`: exact hypotheses, proofs, method scope and open steps.
- `replay.py`: Arb interval witness and series enclosure; finite symbolic/algebra fixtures; explicitly numerical ED and DMFT diagnostics; 16 guarded mutants.
- `independent.py`: separately coded SymPy and mpmath.iv fixture checks, including exact static dimer eigenvectors and a different series cutoff. It does not import replay.py.
- `replay.stdout.txt`, `independent.stdout.txt`, `mutants.stdout.txt`, `CHECKS.txt`: executed-command records.

The final replay and final independent implementation were exercised on 20 November 2026 and each returned **exit 0**. The replay says explicitly: `NO PAIRING CEILING CERTIFIED`. The fixed two-slice witness and auxiliary series have exact/outward-rounded interval checks; the ED and DMFT fixtures do not have tail control.

Commands use the assignment's Python 3.12 environment through cached, offline uv dependency resolution, with BLAS/OpenMP thread counts set to one. This workspace is not Git, so no branch or commit was created. No paper/PDF retrieval, repository build, linter, formatter, broad suite, cloud job, posting, publication, push or email was performed. Paid/cloud spend is zero.

## What remains open

Independent scientific review of these proof drafts is required before a campaign-level PROVED label. Mathematically, the exact linear ceiling itself is still open. The most sharply localized missing quantity in this route is the interacting, resolvent-weighted annealed negative-frequency leakage, not an uncomputed numerical coefficient. A moment bound, a determinant-positive witness, a dimer gap or a floating-point DMFT eigenvalue cannot replace that theorem.

## Final command receipt

With `OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1`, `UV_OFFLINE=1` and `UV_CACHE_DIR=D:/dev/.cache/uv`, the executed commands were:

```
uv run --no-project --with numpy --with scipy --with sympy --with mpmath --with python-flint python -B replay.py
uv run --no-project --with numpy --with scipy --with sympy --with mpmath --with python-flint python -B independent.py
```

Each returned exit 0. A Python subprocess driver enumerated the 16 names in `replay.MUTANTS` and invoked `python -B replay.py --mutant NAME` in a separate process for every name. All 16 mutant processes returned **exit 1** at their named guards; the driver returned **exit 0**. Its full output, including the outward-rounded witness value, is in `mutants.stdout.txt`. The combined command returned exit 0 in 61.60 seconds. These fixture checks do not formalize the infinite-Hilbert-space proof, an infinite-grid DMFT limit or a temperature ceiling.


Cleanup: `powershell -NoProfile -Command "cmd /c rmdir /s /q C:\t\LinearFresh-2; exit $LASTEXITCODE"` returned exit 0 and removed the owned temporary exploratory scripts and caches. The admitted replay, independent implementation, recorded negative and command logs remain in this output directory.

