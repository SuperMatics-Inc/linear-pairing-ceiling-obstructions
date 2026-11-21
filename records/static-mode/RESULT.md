# STATIC-MODE result: a fixed-hopping resonance survives dynamic-mode cancellation

**Status: proof draft; independent review pending.** Exact-rational constant replay is supplied, but neither the draft nor its computations are labelled PROVED or CERTIFIED. Finite-matrix checks are NUMERICAL. No new upper bound on `T_pair` is obtained; the linear-in-frequency model target remains open.

## Precise statement

Use energy temperature `tau=k_B T`, phonon energy `Omega=hbar sqrt(K/m)`, fixed nearest-neighbor hopping `t>0`, and fixed `U=g^2/K>0`. Conditional on a real static site field `W` (including chemical potential), let `R_W(s)` be the two-spin electronic partition-function ratio obtained by multiplying the **Gaussian-integrated nonzero Matsubara interaction** by `s`, with the positive static free-fermion state as reference. Write its first coefficient as `R'_W(0)=sum_x a_x(W)`; it is also the first coefficient of `log R_W`. The exact expression is

```
a_x(W) = 2U sum_{n>=1} Omega^2/(nu_n^2+Omega^2)
   * sum_{a,b} |psi_a(x)|^2 |psi_b(x)|^2
   * [f(e_a)-f(e_b)](e_b-e_a)/[nu_n^2+(e_b-e_a)^2],
nu_n=2 pi n tau,  f(e)=(1+exp(e/tau))^(-1).
```

The eigenstate sum is ordered. Every term is nonnegative, and the Hartree/zero-frequency piece has already cancelled.

For `0<Omega<=tau<=t/4`, take the **three-site open path** with unchanged hopping `-t`, fields

```
W_left=W_right=2tau,
W_middle=t^2/(2tau)-2tau.
```

It has two thermally separated eigenvalues `-2tau,+2tau`, plus `2tau+t^2/(2tau)`. The low eigenstates have endpoint weights `A/2` and `1/2`, respectively, where `A=[1+8tau^2/t^2]^(-1)>=2/3`. Keeping only the first bosonic frequency and the two ordered low-state pairs yields

```
a_left >= U A Omega^2 (4tau) tanh(1)
       / [(4pi^2 tau^2+Omega^2)(4pi^2 tau^2+16tau^2)]
       > U Omega^2/(1200 tau^3).
```

The coefficient follows from exact-rational guards for `pi^2<10`, `tanh(1)>3/4` and `1/1148>1/1200`; see `replay.py:exact_constants` and `RIGOR.md`, section 4.

For **any square torus of side `L>=4`**, use the collinear sites `(0,0),(0,1),(0,2)` with those fields and set every other site field to a common positive barrier `B`. All torus bonds retain hopping `-t`. As `B` increases, the low-state spectral data converge to the path data. Thus for every fixed parameter choice and sufficiently large **finite** `B`,

```
a_(0,0)(W_B) >= U Omega^2/(2400 tau^3).
```

The finite barrier threshold exists by a Schur-complement argument; an explicit uniform bound on its value is not claimed. The coefficient `1/2400` is explicit and is one half of the path bound. At `tau=C Omega`, any fixed `C>=1`, the local first coefficient is at least `U/(2400 C^3 Omega)` for sufficiently small `Omega`. Choosing the fixed torus `L=4` also gives this divergent lower bound divided by `16` for the per-volume first coefficient.

## Exactly what this rules out

This rules out an **unresummed absolute expansion uniformly small in every static `W`**, about its static free-fermion reference, when its local activity or per-volume majorant dominates the exact first dynamic coefficient above. That coefficient cannot be made small at `tau=C Omega` by the zero-frequency cancellation, static Combes-Thomas bounds, O(1) Gram bounds, or spin-square positivity alone.

It does **not** rule out convergence of every Taylor/cluster series: large first derivatives alone do not prove nonconvergence. It does **not** rule out a source-connected expansion that resums source-free terms, annealed estimates suppressing resonant static fields with their exact determinant weights, another resummed proof, or the physical linear pairing-ceiling target. No finite-volume resonance is asserted to carry appreciable Gibbs probability or to demonstrate thermodynamic pair order.

## What is new versus LINEAR4-11

- **Already present in LINEAR4:** exact zero/dynamic Matsubara split, unrestricted static conditioning, uniform static Combes-Thomas control, O(1) interpolated Wick minors, positive reference weights, and exact tail restoration. Its power loss is the cutoff `r=tau/64` against dynamic variance `Var(v)~U Omega^2/(12tau)`, giving `tau^3/(U Omega^2)` in the tail exponent. The spatial attachment cost enters only logarithmically, not as a `(beta t)^d` Gram power. Source: `PUBLISH/linear4/repo/replay/RIGOR.md`, sections 2-4.
- **Already obstructed in LINEAR5:** the bounded per-history rare-history cutoff method has the two-thirds scale as its method floor. The cubic dimensionless scale itself is not new.
- **New witness here:** a fixed-bare-hopping three-site static resonance, embedded without bond deletion in a square torus, makes the **exact integrated first dynamic cumulant** have that cubic scale after the Hartree cancellation and with a strictly positive static reference. This specifically answers the suggestion that integrating the dynamic field first, instead of bounding it history by history, automatically recovers a linear perturbative scale.
- **Different from LINEAR6-7:** LINEAR6 leaves the near-Fermi static fields unresolved; LINEAR7's `K_{1,3}` time-mean-zero determinant zero obstructs unrestricted per-history normalized propagator control. The present witness needs neither a dynamic determinant zero nor division by an unrestricted dynamic trace. It complements those barriers, rather than proving a stronger physical no-go theorem.
- **Consistent with LINEAR8-11/LIMITS:** no bounded-insertion estimate is promoted to clustering, no marginal estimate is promoted to a joint spatial buffer, and no trace cut is localized. The missing annealed/resummed step remains missing.

`RIGOR.md` contains the complete derivation, a uniform static-reference pair-decay bound, the exact spin/sign factors, the additional hopping-conservation upper bound `a_x<=d_x t^2 U Omega^2/(1440 tau^5)`, the square embedding, and the scope exclusions. That upper bound helps only at bounded `beta t`; it is not an improved exponent for the fixed-hopping low-temperature target.

## Deliverables, evidence and custody

Changed paths are confined to `MASSIVE/STATIC-MODE/`: this file, `RIGOR.md`, `replay.py`, `CHECKS.txt`, and retained replay stdout/stderr (including the initial numerical failure). `CHECKS.txt` records exercised commands and exits. The replay checks the rational constants, covariance normalization, Kubo sign and two-spin HS factor through independent formulas, exact bridge spectrum, fixed-temperature-ratio scaling, finite square-barrier convergence, and spectral commutator identity. No external source data or paper values are used. No branch or commit was created; no public contract was changed; no cloud, spend, publication, push or merge occurred. The temporary directory was empty and is removed at closure. Independent review is the remaining prerequisite for status promotion.
