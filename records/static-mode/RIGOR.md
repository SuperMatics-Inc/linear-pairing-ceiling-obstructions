# STATIC-MODE: conditional dynamic-cumulant obstruction

**Status: proof draft; independent mathematical review pending.** The constant guards are exact-rational computations; the finite-matrix probes are NUMERICAL. Neither the argument nor the computations are labelled PROVED or CERTIFIED. This is a method obstruction, not a new bound on the pair-ordering temperature.

## 1. Model, units and precise claim

Let `tau=k_B T`, `beta=1/tau`, and `Omega=hbar sqrt(K/m)` be energies; `t,U=g^2/K>0` are fixed energies. One-spin hopping is `-t` between nearest neighbors. The arbitrary real static site field, including chemical potential, is `W`. Put `h_W=-t A+diag(W)`. There are two identical, independent spin sectors at fixed field. Using centered density `n_x-1` instead of `n_x` changes none of the dynamic formulas because the dynamic covariance has zero integral in either time.

For a mean-zero real Gaussian dynamic field `v`, define

```
D_dyn(u) = (U/beta) sum_{n != 0} r_n exp(i nu_n u),
r_n = Omega^2/(nu_n^2+Omega^2),  nu_n=2 pi n/beta.
R_W(s) = E_v Tr_Fock T exp[-int_0^beta (H_W+sqrt(s) sum_x v_x(u)n_x)du]
         / Tr_Fock exp(-beta H_W).
```

The denominator is strictly positive. Gaussian integration defines a Taylor series in `s` about zero even though the individual field coupling uses `sqrt(s)`. Define the local first coefficient `a_x(W)` by `R'_W(0)=sum_x a_x(W)`. It is also the first derivative of `log R_W(s)` at zero, since `R_W(0)=1`.

**Draft proposition.** For every fixed `t,U>0` and every `0<Omega<=tau<=t/4`, a three-site open path with a real static field has

```
a_endpoint(W) >= U Omega^2/(1200 tau^3).                 (1)
```

For every square torus of side `L>=4`, embedding that path using the fields specified in section 5 and taking a sufficiently large finite positive barrier `B` gives

```
a_endpoint(W_B) >= U Omega^2/(2400 tau^3).               (2)
```

In particular at `tau=C Omega` for any fixed `C>=1` and sufficiently small `Omega`,

```
a_endpoint(W_B) >= U/(2400 C^3 Omega).                   (3)
```

Thus even the exact first local dynamic cumulant, with the zero-frequency cancellation already performed, is not uniformly small over all real static `W` at a linear-in-frequency temperature scale. The obstruction is to an absolute expansion about the static free-fermion reference whose proposed uniform small activity dominates this local first cumulant. It does not assert nonconvergence of every possible expansion or nonclustering of the original Gibbs state.

## 2. What the Matsubara split already accomplishes

The exact full oscillator covariance is

```
D(u) = (U/beta) sum_n Omega^2/(nu_n^2+Omega^2) exp(i nu_n u).
```

The zero mode is a scalar Gaussian `b_0` of variance `U/beta`, independent of `v`. With `a=beta Omega`,

```
Var(v(u)) = (U/beta) q(a),  q(a)=(a/2)coth(a/2)-1,
q(a)=sum_{n!=0} a^2/[(2 pi n)^2+a^2] <= a^2/12.
beta^2 Var(v(u)) = beta U q(a) ~ U Omega^2 beta^3/12.     (4)
```

The energy-valued Fourier coefficient `U r_n` is not a dimensionless interaction activity. Thermal integration introduces another inverse energy. The statement that the nonzero frequencies have total energy strength of order `U Omega^2/tau^2` therefore does not give a small dimensionless perturbation at `tau=C Omega` and fixed `U`.

For completeness the static equal-time pair correlation decays uniformly in `W`, and no static-measure clustering is needed. Here is a direct bound. Set `alpha=(1+16 beta t)^(-1)` and conjugate by `M=exp(alpha d(x,anchor))`. The changed hopping is `P=M h_W M^(-1)-h_W`; its Schur norm is at most `4t(e^alpha-1)<=8t alpha<=1/(2 beta)`. The diagonal field does not change. At each fermionic frequency `omega_k=(2k+1)pi/beta`, the unweighted inverse has norm at most `1/|omega_k|`, the conjugated inverse at most `2/|omega_k|`, and their difference at most `2||P||/omega_k^2`. The difference series for time slices converges absolutely because the identity jump cancels. Since `sum_k omega_k^(-2)=beta^2/4`, the static slice norm after conjugation is at most `1+beta||P||/2<=5/4`. This also holds for the ordered equal-time limits. This is the static part of LINEAR4's argument; it does not require a bounded static potential.

With `f(e)=(1+exp(beta e))^(-1)` and `Delta_x=c_{x,down}c_{x,up}`, for distinct sites and real `h_W`, Wick factorization gives

```
<Delta_x^dagger Delta_y>_W = f(h_W)_{xy}^2,
|<Delta_x^dagger Delta_y>_W| <= (25/16) exp(-2 alpha d(x,y)). (5)
```

The real-square notation is appropriate here; arbitrary complex flux hopping would require revisiting the spin pairing convention. Any positive annealed measure over static fields preserves (5) simply by averaging this pointwise inequality. This proves static-reference absence of this pair order at every fixed positive temperature, not absence at positive phonon frequency.

## 3. Exact first coefficient, signs and the spin factor

In finite volume expand the electronic Dyson series to second order in `sqrt(s)` and apply Gaussian Wick. Absolute finite-volume justification follows from the Gaussian exponential moments of `int |v|` and finite-dimensional electronic traces. We obtain

```
R'_W(0) = (1/2) sum_x int du du' D_dyn(u-u')
                        <T n_x(u)n_x(u')>_W.
```

The disconnected Hartree term is independent of both times and vanishes under integration against `D_dyn`. Cross-spin connected terms vanish at fixed `W`. The two same-spin terms cancel the prefactor `1/2`. Write the real orthonormal eigenvectors and eigenvalues of `h_W` as `psi_a,e_a`, and `p_a(x)=|psi_a(x)|^2`. For one spin the connected density correlation for `0<u<beta` is

```
K_x(u) = sum_ab p_a(x)p_b(x) f(e_a)[1-f(e_b)] exp(u(e_a-e_b)).
```

For a nonzero bosonic frequency, direct time integration and pairing `(a,b)` with `(b,a)` give

```
chi_x(i nu) = int_0^beta exp(i nu u) K_x(u)du
 = sum_ab p_a(x)p_b(x) [f(e_a)-f(e_b)](e_b-e_a)
                              / [nu^2+(e_b-e_a)^2].
```

The sum is over **ordered** eigenstate pairs. A diagonal/degenerate pair contributes zero. Every other summand is nonnegative because the Fermi function decreases. The double time integral supplies `beta`, which cancels the `1/beta` in the covariance. Consequently

```
a_x(W) = U sum_{n!=0} r_n chi_x(i nu_n)
       = 2U sum_{n>=1} r_n sum_ab p_a(x)p_b(x)
          [f(e_a)-f(e_b)](e_b-e_a)/[nu_n^2+(e_b-e_a)^2].  (6)
```

This fixes the sign, both signs of the bosonic frequency, and the two-spin normalization. Earlier exploratory inline scripts in this session used inconsistent factors and one negative sign. Their numbers are not evidence for (6). The retained replay compares (6) independently against a time-domain Kubo integral and the cos/sin Gaussian Hessian of the two-spin determinant ratio.

Two useful upper bounds show exactly what is and is not improved by conservation. The Fermi derivative is bounded by `beta/4`, so `chi_x<=beta/4` and

```
a_x <= (beta U/4) q(beta Omega) <= U Omega^2 beta^3/48.   (7)
```

Also the spectral variance identity is

```
sum_ab p_a(x)p_b(x)(e_b-e_a)^2
 = 2[(h_W^2)_{xx}-(h_W)_{xx}^2] = 2 d_x t^2.
```

It follows that `chi_x(i nu)<=beta d_x t^2/(2 nu^2)` and, using `sum_{n!=0} nu_n^(-4)=beta^4/720`,

```
a_x <= d_x t^2 U Omega^2 beta^5/1440.                  (8)
```

This vanishes at zero hopping and helps when `beta t` is small. At fixed hopping and low temperature it is worse than (7); it is not an improved pair ceiling. Bounds (1) and (7) show that the worst-case conditional first-cumulant order `U Omega^2 beta^3` is genuine, not only an absolute-value integration artifact.

## 4. Fixed-hopping resonance and exact constant

Take the open three-site path `left-middle-right` with hopping `-t`. For `delta>0` put

```
W_left=W_right=delta/2,
W_middle=-delta/2+2t^2/delta.
h_3 = [[delta/2,-t,0],[-t,-delta/2+2t^2/delta,-t],[0,-t,delta/2]].
```

Its antisymmetric endpoint eigenvector has energy `e_+=delta/2` and endpoint weight `p_+(left)=1/2`. Its symmetric low eigenvector has energy `e_-=-delta/2` and total endpoint weight

```
A = 1/[1+delta^2/(2t^2)],  p_-(left)=A/2.
```

The remaining eigenvalue is `delta/2+2t^2/delta`. These formulas follow by diagonalizing the symmetric block in the basis `(left+right)/sqrt(2),middle`: at energy `-delta/2` the middle/symmetric-endpoint amplitude ratio is `delta/(sqrt(2)t)`. The eigenvalue separation `delta` can be arbitrarily small at **fixed** bare hopping by increasing the middle barrier.

Keep only the two ordered low-state pairs and `n=1` in (6). Their Fermi difference is `tanh(beta delta/4)` and their two ordered weight products sum to `A/2`. Hence

```
a_left >= U A Omega^2 delta tanh(beta delta/4)
          / [(4pi^2 tau^2+Omega^2)(4pi^2 tau^2+delta^2)]. (9)
```

Set `delta=4tau`. For `Omega<=tau<=t/4`, `A>=2/3`, `tanh(1)>3/4`, and `pi^2<10`. Therefore

```
a_left > [ (2/3)*4*(3/4) / ((40+1)*(40+16)) ]
             * U Omega^2/tau^3
       = (1/1148) U Omega^2/tau^3
       > (1/1200) U Omega^2/tau^3.
```

The strict constant is conservative. Its elementary numerical inequalities have exact-rational replay: the positive integral `int_0^1 x^4(1-x)^4/(1+x^2)dx=22/7-pi` gives `pi<22/7` and `(22/7)^2<10`; the Taylor terms of `exp(2)` through degree four sum to `7`, with a strictly positive remaining tail, giving `tanh(1)>3/4`. `replay.py:exact_constants` verifies the polynomial identity and all rational comparisons, including `1/1148>1/1200`. Independent checking of the argument is still pending.

## 5. Embedding in an allowed square torus

Fix any side `L>=4`. Use the three collinear torus sites `(0,0),(0,1),(0,2)`. Their induced graph is the open path, including when `L=4`; its two endpoints are not adjacent. Assign them, respectively,

```
W=(2tau, t^2/(2tau)-2tau, 2tau),
```

and assign **every other site** the same real field `B>0`. The bare hopping remains `-t` on every torus edge, including edges into the barrier region. There is no bond deletion. Call this full static matrix `h_B`.

In path/complement block form `h_B=[[h_3,V],[V^*,B I-t A_complement]]`. The complementary spectrum is at least `B-4t`, and `||V||<=4t`. For each fixed finite `L,t,tau,Omega`, as `B` tends to infinity the three low eigenvalues and their spectral projections converge to those of `h_3` extended by zero, while all other eigenvalues diverge to positive infinity. One elementary proof uses the low-sector Schur complement `h_3-z - V(B I-t A_complement-z)^(-1)V^*`: the correction tends uniformly to zero on compact sets away from the three simple low eigenvalues. Its resolvent therefore converges on small contours around those eigenvalues, giving spectral-projection convergence by contour integration. Residues then give the eigenvalues and local weights. No limit exchange in an infinite Matsubara sum is needed for the lower bound: retain only the positive `n=1` contributions of the two converging low states in (6).

Their contribution converges to the right side of (9), strictly larger than (1). Thus there exists a finite `B_0(L,t,tau,Omega)` such that **every** `B>=B_0` satisfies (2). This is an existence assertion with explicitly specified site configuration and coefficient; no explicit numerical value or uniform estimate for `B_0` is claimed. The retained finite-barrier probes only sanity-check this convergence. They do not certify a barrier threshold for arbitrary parameters.

On the fixed torus, because `a_x>=0`, `R'_W(0)/L^2 >= U Omega^2/(2400 L^2 tau^3)`. Taking `L=4` already disproves a uniform-in-volume, uniform-in-`W` small first-coefficient bound at `tau=C Omega`. In the infinite-barrier limit the conditional electron density is `2[1+f(delta/2+2t^2/delta)]/L^2`: the two low Fermi occupations add to one per spin. As `tau/t` tends to zero with `delta=4tau`, the third occupation vanishes and this density tends to `2/L^2`. At `L=4` the limit is `1/8`, strictly between empty and fully occupied. This is a conditional-state observation, not a statement about the density or probability of this field under the full annealed Gibbs state, nor a canonical thermodynamic-limit proof.

## 6. Exact scope of the obstruction and comparison with LINEAR4-11

The blocked proof class has these specific features:

1. Condition on arbitrary real static `W` and use its positive static free-fermion state as the reference.
2. Expand the Gaussian-integrated nonzero-mode density interaction without absorbing/resumming its connected contributions into a new reference.
3. Require a uniform absolute local activity tending to zero, or bounded below the convergence threshold, at `tau=C Omega`. Its majorant dominates the local first coefficient (6), or its per-volume sum.

Equations (2)-(3) contradict step 3. A Taylor derivative can be large while its series remains convergent, and a large source-free first coefficient need not obstruct a source-connected clustering estimate. Thus this does **not** prove that all conditional cluster expansions fail, or that a resummation cannot remove source-free cumulants.

LINEAR4 already uses the zero/dynamic Matsubara split, unrestricted static conditioning, static Combes-Thomas control, O(1) interpolated Wick-minor bounds, and positive reference weights. Its good-history cutoff is `r=tau/64`; the thermal inverse has norm O(beta), and the tail scale is controlled by `r^2/(U beta Omega^2)`, hence `tau^3/(U Omega^2)`. The attachment factor `Q=64(1+4 beta t)` is paid only by a logarithm in the rare-history probability. Neither a static-measure cluster expansion nor a `(beta t)^d` Gram determinant norm is the power-loss mechanism. Source: `PUBLISH/linear4/repo/replay/RIGOR.md`, sections 2-4.

LINEAR5's cutoff sharpness record already makes the two-thirds exponent method-sharp for bounded per-history rare-history references. LINEAR6's gap-conditioned route leaves static near-Fermi fields uncontrolled. LINEAR7's mean-zero `K_{1,3}` histories show unrestricted per-history determinants can vanish and rule out a global normalized Wick/inverse bound. Our argument is different: it expands at the strictly positive **static** trace, integrates the dynamic covariance first, and supplies a fixed-`t`, near-Fermi spectral resonance with a large exact **first cumulant**. Thus it is not a new determinant-zero construction, nor a stronger physical no-go theorem. The dimensionless cubic scale was already identified by LINEAR4-5; the explicit three-site witness survives cancellations those bare norms do not use.

LINEAR8-11 and LIMITS warn that bounded insertions, marginal resonant-site estimates, or a trace cut do not by themselves imply clustering/local buffers. This draft claims none of those missing implications. References: `ADIABATIC/LINEAR5/SHARPNESS.md`, `ADIABATIC/LINEAR6/{RESULT,RIGOR}.md`, `ADIABATIC/LINEAR7/{RESULT,RIGOR}.md`, and `ADIABATIC/LINEAR8` through `LINEAR11` result records. These are internal proof records already read in the resumed history; no outside paper was acquired or used here.

## 7. Annealing, spin-square positivity and gauge integration

For any real time-dependent site history, the one-spin evolution and determinant are real, so the two-spin weight is its square and is nonnegative. However zeros remain possible for unrestricted histories; a square weight does not bound a normalized inverse. More importantly for this draft, positivity of the static trace does not make (6) small. Every term of (6) is already nonnegative.

The annealed static Gaussian assigns positive measure to neighborhoods of every finite barrier configuration, but their probabilities can be arbitrarily small. In particular a barrier of size `t^2/tau` is expensive under the static free Gaussian variance `U tau`. Pointwise bad-field behavior therefore does not establish a bad annealed estimate. The determinant reweighting must also be retained. An estimate of the *joint* annealed resonance weight and source-connected dynamics, or an appropriate resummed comparison, can evade this result.

For a periodic antiderivative `phi'_x=v_x`, conjugation gives the exact identity

```
exp(phi) (partial_u+h_W+diag(v)) exp(-phi)
 = partial_u+diag(W)-t A_xy exp(phi_x-phi_y).
```

Choosing `phi(0)=phi(beta)=0` preserves the monodromy and equal-time insertion at time zero. This confirms atomic cancellation at `t=0`. The similarity is real/hyperbolic, not unitary; it creates exponential hopping factors, and cannot turn the resonance witness into a uniformly small perturbation. On the gauge-centered primitive, the simple variance upper bound is `Var(phi)<=U Omega^2 beta^3/720`, obtained by dividing the nonzero Fourier coefficients by `nu_n^2`. At a linear scale it is not uniformly small. The stronger exact atomic cancellation and the sum rule (8) do not establish a fixed-hopping linear ceiling.

## 8. Evidence and remaining prerequisite

`replay.py` exercises the exact-rational constant guard, high-precision covariance identity, independent time-domain susceptibility, a two-spin cos/sin HS determinant Hessian with step refinement, the analytic three-site spectrum, fixed-temperature-ratio scaling, finite square-barrier convergence, and the spectral variance identity. Positive-frequency numerical sums are truncated and carry a displayed rigorous analytic tail upper bound; the finite-matrix arithmetic itself is not interval-certified. No simulation result is called a measurement. The only unresolved prerequisite for promoting this draft's status is independent mathematical review. No new model-level ceiling, annealed estimate, or public/scientific contract is asserted.
