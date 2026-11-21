# Slow-phonon pairing: spectral sum rule and a single-impurity obstruction

Davis Rens, SuperMatics Inc. ORCID 0000-0001-5839-5197.
20 November 2026.

**PROVED (pending independent review)** refers below to complete analytical proof drafts, not reviewed campaign theorems. Interval fixtures and floating-point calculations are identified separately. **The linear-in-frequency bound on the exact model pair temperature remains OPEN.**

AI agents generated the proofs, code and drafts. This work has not been peer reviewed.

## 1. Scope, units and relation to the target

Write tau = k_B T = beta^(-1), and set hbar = 1. Omega denotes phonon energy, not cyclic frequency. Let a finite electronic lattice, or a finite impurity with a finite electronic bath, have the Hamiltonian

```
H = H_el + sum_x [P_x^2/(2M_x) + K_x X_x^2/2 - F_x X_x Q_x],
[X_x,P_y] = i delta_xy,
U_x = F_x^2/K_x,  Omega_x^2 = K_x/M_x,  b_x = F_x X_x.
```

H_el is self-adjoint on a finite electronic Fock space, and Q_x is any bounded self-adjoint electronic operator. All electronic operators commute with the phonon coordinates and momenta. On-site Hubbard repulsion, hopping, a chemical potential, or a fixed-electron-number restriction can be included in H_el. The oscillator springs and masses are strictly positive. Linear coupling to bounded electronic operators makes H bounded below and its Gibbs trace finite at every beta > 0.

The target T_pair is a thermodynamic electronic charge-two correlation temperature, as in ADIABATIC/LINEAR4-PAPER and MASSIVE/CAPSTONE-PAPER. A two-site gap, a nearest-neighbor pair correlator and a normal-branch DMFT eigenvalue are not that quantity. No statement here bounds an exact many-body measured Tc.

These routes do not restart the stopped defect-insertion, polymer, ladder or LINEAR12 programs. The principal new result is a stopping theorem for a single-impurity, determinant-positive route, rather than a new clustering theorem.

## 2. Exact interacting nonzero-Matsubara sum rule

### Theorem 2.1: spectral bound

**PROVED (pending independent review).** Under section 1's hypotheses, define

```
nu_k = 2*pi*k/beta,
C_x(i nu_k) = integral_0^beta exp(i nu_k u) <b_x(u)b_x(0)> du.
```

For every nonzero integer k,

```
0 <= C_x(i nu_k) <= U_x Omega_x^2 / nu_k^2.                 (2.1)
```

In a positive Euclidean path representation, with normalized Fourier coefficients

```
b_{x,k} = beta^(-1) integral_0^beta b_x(u) exp(-i nu_k u) du,
```

this gives

```
E |b_{x,k}|^2 <= U_x Omega_x^2/(4*pi^2*k^2*tau),
sum_{k>=1} E |b_{x,k}|^2 <= U_x Omega_x^2/(24*tau).       (2.2)
```

The sum over both positive and negative k has constant 1/12, not 1/24. The quantum spectral claim (2.1) needs no positive auxiliary-field measure. A pathwise probabilistic use of (2.2) does require such a measure; canonical fermion trace positivity is not assumed automatically.

#### Proof

Since Q_x and H_el commute with b_x,

```
[H,b_x] = -i(F_x/M_x)P_x,
[b_x,[H,b_x]] = F_x^2/M_x = U_x Omega_x^2.                (2.3)
```

The order of the double commutator matters: [[H,b_x],b_x] has the opposite sign.

Let E_a be the exact energies and p_a = exp(-beta E_a)/Z. The Lehmann expansion at nonzero nu gives

```
C_x(i nu) = sum_{a,b} [(p_a-p_b)(E_b-E_a)
                     /((E_b-E_a)^2+nu^2)] |(b_x)_{ab}|^2. (2.4)
```

Terms with E_a = E_b contribute zero at nonzero nu. The imaginary parts cancel between (a,b) and (b,a). Each remaining numerator is nonnegative. Furthermore,

```
sum_{a,b} (p_a-p_b)(E_b-E_a)|(b_x)_{ab}|^2
 = <[b_x,[H,b_x]]> = U_x Omega_x^2.                       (2.5)
```

Replacing each denominator by nu^2 proves (2.1). In a translation-invariant thermal path measure, E|b_{x,k}|^2 = C_x(i nu_k)/beta. Summing 1/k^2 = pi^2/6 proves (2.2).

The unbounded coordinate does not require an oscillator Fock cutoff. For a finite electronic space, each linear coordinate coupling is relatively form bounded with arbitrarily small relative bound against the harmonic potential. For a constant c, the quadratic-form inequalities therefore compare H+c with a positive multiple of the oscillator number operator plus a constant. Thermal coordinate and momentum moments are finite. The oscillator finite-particle vectors are a common core for the commutators in (2.3). Spectral sums in (2.4)-(2.5) can be exhausted on this core; the nonnegative summands converge monotonically, while the quadratic commutator form in (2.3) is the constant F_x^2/M_x. This justifies the thermal identity without replacing the canonical commutation relation by a finite matrix relation.

All bounds are volume independent, so any thermodynamic limit in which the local thermal correlator exists inherits them. They give no control of the zero mode k=0.

### What this theorem obstructs and what it supplies

The theorem rules out the claim that an electronic determinant tilt must invalidate every free-scale nonzero-frequency second-moment bound. The exact interacting bound has the same high-frequency coefficient as the free oscillator. It also supplies a route to slow-variable estimates without a convexity assumption on the full effective phonon action.

It does **not** establish Gaussian concentration, independence between sites or frequencies, an exponential moment, a joint rare-event bound, or control of a Green-function-weighted second moment. In particular, root-mean-square fluctuations of order sqrt(U Omega^2/tau) are not a norm bound on every history. Replacing such a moment by a uniform bound is an invalid step toward a linear pairing ceiling.

## 3. Positive determinant does not bound an impurity propagator

### Theorem 3.1: an arbitrary-amplification family

**PROVED (pending independent review).** Consider one electronic impurity coupled to one bath orbital, with one-particle Hamiltonian

```
h(u) = [[b(u), -v], [-v, 0]],   v > 0,
beta = 2,
b(u) = -B for 0<u<1,  +B for 1<u<2,   B > 0.
```

The unit of time is arbitrary; energies are in its inverse unit. Define U_1 = exp(-h_1), U_2 = exp(-h_2), monodromy U = U_2 U_1, and the antiperiodic Green matrix

```
G(1,0) = -U_1(I+U_2 U_1)^(-1)
       = -(U_1^(-1)+U_2)^(-1).
```

Then det(I+U) > 1, every eigenvalue of U is positive, but

```
|G(1,0)_{00}| -> infinity as B -> infinity.               (3.1)
```

Indeed, for fixed v,

```
|G(1,0)_{00}| ~ B^2/(2 v^2).                             (3.2)
```

Thus no pathwise, history-independent bound |G_{00}| <= C follows from positivity or a nonvanishing lower bound on det(I+U), even in a single-impurity problem with a positive grand-canonical electronic trace.

#### Proof

Both U_1 and U_2 are symmetric positive definite. Their product is similar to the symmetric positive-definite matrix U_1^(1/2) U_2 U_1^(1/2). Its eigenvalues are positive, and det U = exp(-Tr h_1-Tr h_2) = 1. Consequently det(I+U) = product_j(1+lambda_j) > 1.

Set

```
d = sqrt(B^2/4+v^2),  a = B/(2d),  c = cosh d,  s = sinh d.
```

The two off-diagonal entries cancel in U_1^(-1)+U_2, giving

```
U_1^(-1)+U_2 = 2 exp(-B/2) diag(c-a*s, c+a*s).
```

Both diagonal entries are positive since 0<a<1. Therefore

```
|G(1,0)_{00}| = exp(B/2)/[(1-a)exp(d)+(1+a)exp(-d)]
 = 1/[(1-a)exp(d-B/2)+(1+a)exp(-d-B/2)].                 (3.3)
```

As B increases at fixed v,

```
d-B/2 = v^2/(d+B/2) = v^2/B + O(B^(-3)),
1-a = v^2/[d(d+B/2)] = 2v^2/B^2 + O(B^(-4)).
```

Substitution gives (3.2). More directly, (3.3) is bounded below by

```
1/[ (2v^2/B^2)exp(v^2/B) + 2exp(-B) ],                  (3.4)
```

which diverges. This proves (3.1) without a floating-point asymptotic fit.

### Continuity and admissible phonon histories

The step history itself is not a finite-action harmonic-oscillator path. This does not invalidate the obstruction. For any finite B and any strict target |G_{00}|>C, approximate the step by smooth periodic histories in L^1, closing the transitions near 0, 1 and 2. Finite-dimensional evolution depends continuously on that history by its integral equation and Gronwall's inequality. The determinant and Green matrix depend continuously wherever det(I+U) is nonzero. The strict determinant and amplification inequalities therefore persist for sufficiently close smooth histories.

For each such smooth history, the oscillator action integral of ((b')^2/Omega^2+b^2)/(2U) is finite whenever U,Omega>0. Its magnitude can be large. No lower bound on its interacting probability, and no divergence of an averaged physical propagator, is asserted. A determinant-weighted integral could suppress these histories. The theorem obstructs a **uniform pathwise CAR/Gram estimate obtained solely from determinant positivity**, not an annealed estimate that retains the weights.

### Executed fixed-parameter fixture

At B=6, v=1/2, an Arb replay and a separately coded mpmath.iv replay give

```
det(I+U) > 15,
|G(1,0)_{00}| > 52.89.
```

The earlier replay displayed |G_{00}| = 52.8957540935... with an outward-rounded enclosure. These are calculated interval fixtures, not measured data. The fixture rejects the proposed bound |G_{00}|<=1. The asymptotic theorem is analytical, not established by this one fixture.

## 4. Exact finite-matrix Ward-Schur algebra

**PROVED (pending independent review).** Split a finite Matsubara matrix into positive and negative frequency blocks. Assume

```
A = [[R_+ + iD_+, -V], [-V^*, R_- - iD_-]],
R_+ = R_+^*, R_- = R_-^*, D_+>0, D_->0,
G = A^(-1),
```

with A invertible. The two diagonal blocks A_+ and A_- are automatically invertible. For either sign,

```
||D_+^(1/2) A_+^(-1) D_+^(1/2)|| <= 1,
||D_-^(1/2) A_-^(-1) D_-^(1/2)|| <= 1.                  (4.1)
```

Proof: the normalized block is H+iI or H-iI with H Hermitian. Its inverse singular values are 1/sqrt(1+lambda(H)^2), at most one.

Define

```
Q = V A_-^(-1) D_- (A_-^(-1))^* V^*,
Qtilde = V D_-^(-1) V^*.
```

Then 0<=Q<=Qtilde by (4.1). Schur complementation and the identity Im(S^(-1)) = -S^(-1)(Im S)(S^(-1))^* give

```
G_+- D_- G_+-^* = G_++ Q G_++^*,
-Im G_++ = G_++ (D_+-Q) G_++^*.                         (4.2)
```

Let alpha = ||D_+^(-1/2) V D_-^(-1/2)||^2. If alpha<1, Q<=alpha D_+ and

```
(G_+- D_- G_+-^*)_{nn}
 <= [alpha/(1-alpha)] (-Im G_++)_{nn}.                   (4.3)
```

Proof: Q <= alpha/(1-alpha)(D_+-Q), then multiply by G_++ and its adjoint. The threshold alpha=1 is sharp for positive dissipation in this abstract algebra: the scalar blocks R_+=R_-=0 and |V|^2=alpha D_+D_- give Q=alpha D_+. This is a finite-matrix test, not a claim of an exact physical determinant zero at alpha=1.

The positive- and negative-frequency row sums satisfy exactly

```
Pos_n = sum_m |(G_++)_{nm}|^2 D_{+,m},
Neg_n = sum_m |(G_+-)_{nm}|^2 D_{-,m},
Pos_n+Neg_n = -Im G_nn + 2 Neg_n.                        (4.4)
```

The factor two is not optional. These identities hold under the stated matrix hypotheses. Passing to an infinite Matsubara operator requires convergence and domain control not supplied by the finite-grid fixtures.

## 5. Why this has not proved a linear DMFT ceiling

For a causal normal Bethe-lattice impurity description one expects D_n=omega_n+t_*^2 d_n, omega_n=(2n+1)pi tau and d_n=-Im E G_nn. If the exact singlet linearization is the nonnegative kernel

```
K_nm = t_*^2 E[ |(G_++)_{nm}|^2 + |(G_+-)_{nm}|^2 ],
```

then (4.4) would give

```
(KD)_n = D_n-omega_n + 2t_*^2 E Neg_n.                   (5.1)
```

Both the kernel identification and the infinite-grid/DMFT limit are **[INFERENCE] here**, not theorems of this package. A uniform inequality 2t_*^2 E Neg_n < omega_n with a strict weighted contraction margin would exclude that normal-branch instability. It would still need an argument relating the normal-branch instability to the model correlation definition of T_pair.

There are three specific open steps, not merely an unknown constant:

1. (4.3) cannot be averaged with alpha replaced by E alpha. Histories with alpha>=1 are not excluded by a second moment. Even on alpha<1, alpha, G and the determinant weight are correlated. Theorem 3.1 shows why a uniform propagator bound is unavailable.
2. A diagonal moment is not an operator-norm bound. An N-by-N matrix with every entry 1/N has diagonal 1/N but norm one. A single-row estimate cannot replace all-row or weighted resolvent control.
3. A metallic bath damping floor is additional information about a self-consistent interacting state. It is not established uniformly in Omega, density or coupling here. In a gapped bath it may vanish with tau. It cannot be silently imposed on all Holstein states.

The unconditional sum rule does give an instructive finite-grid estimate. With V_nm=b_{n+m+1} and D_{+,n},D_{-,n} >= (2n+1)pi tau,

```
E alpha <= E ||D_+^(-1/2) V D_-^(-1/2)||_HS^2
 <= U Omega^2/(4 pi^4 tau^3) S,
S = sum_{k>=1} H_odd(k)/k^3,
H_odd(k) = sum_{j=0}^{k-1} 1/(2j+1).                    (5.2)
```

Proof: group the finite or nonnegative infinite double sum by k=n+m+1. Partial fractions give

```
sum_{n=0}^{k-1} 1/[(2n+1)(2k-2n-1)] = H_odd(k)/k.
```

Apply (2.2) mode by mode. Since 1/(2x+1) decreases,

```
H_odd(k) <= 1 + integral_0^{k-1} dx/(2x+1)
         = 1 + (1/2)log(2k-1).
```

Hence S<=C_aux, where

```
C_aux = sum_{k>=1} [2+log(2k-1)]/(2k^3),
67/50 < C_aux < 27/20.                                  (5.3)
```

This last enclosure is calculated with outward-rounded Arb and independently with mpmath.iv. For K terms, the omitted tail is at most

```
integral_K^infinity [1+(1/2)log(2x)]/x^3 dx
 = [5/2+log(2K)]/(4K^2).
```

Replay uses K=200; the independent implementation uses K=300. The integrand is decreasing for x>=1, so the integral bounds the sum starting at K+1. C_aux is **not** a superconducting ceiling coefficient. The tau^(-3) moment scale in (5.2) recovers a two-thirds-power small-moment scale, not a linear temperature law. It does not itself prove clustering.

If D_n>=gamma>0 uniformly, the diagonal estimate improves to

```
E (Qtilde)_{nn}/D_n <= U Omega^2/(24 tau gamma^2).        (5.4)
```

This follows by summing 1/(n+m+1)^2 <= pi^2/6. Its favorable dimensions explain the attraction of the metallic route, but (5.4) does not control E[G_++ Q G_++^*]. No linear theorem follows.

## 6. Dimer and static-ion anchors

### 6.1 Exact center-of-mass separation

**PROVED (pending independent review).** In the two-site spinful Holstein model at fixed total electron number N, write a_+=(a_1+a_2)/sqrt(2), a_-=(a_1-a_2)/sqrt(2), g^2=U Omega/2. The COM part is

```
Omega a_+^* a_+ - (g N/sqrt(2))(a_++a_+^*)
 = Omega c_+^* c_+ - g^2 N^2/(2 Omega),
c_+ = a_+ - g N/(sqrt(2)Omega).
```

The shifted COM oscillator completely decouples. The unshifted COM number does not generally commute with H. The replay's conservation fixture checks total electron number, not the unshifted COM number.

### 6.2 Exact static electronic pair admixture

**PROVED (pending independent review).** In the two-electron singlet sector at a frozen relative field q, the electronic matrix and oscillator elastic energy are

```
h(q) = [[-q,0,-sqrt(2)t], [0,q,-sqrt(2)t],
        [-sqrt(2)t,-sqrt(2)t,0]],
E_elastic(q) = q^2/(4U).
```

The electronic energies are 0 and +-sqrt(q^2+4t^2). Differentiating the lower Born-Oppenheimer surface q^2/(4U)-sqrt(q^2+4t^2) gives two minima at q=+-2sqrt(U^2-t^2) for U>t>0. At either minimum,

```
<Delta_1^* Delta_2>_electronic_ground = t^2/(4U^2).        (6.1)
```

Proof: let R=sqrt(q^2+4t^2). A positive normalized ground vector has covalent weight c_2^2=2t^2/R^2, with c_0=sqrt(2)t c_2/(R-q), c_1=sqrt(2)t c_2/(R+q). These satisfy h(q)c=-Rc and c^*c=1. Therefore c_0 c_1=t^2/R^2; at a minimum R=2U, proving (6.1). At the unrelaxed field q=2U the value is instead t^2/[4(U^2+t^2)]. For U=4,t=1 the two calculated rational values are respectively 1/64 and 1/68.

This is a static electronic calculation, not a full quantum dimer theorem or a limit exchange. It obstructs a Peierls argument that identifies every short-range **bare** electronic pair correlator with a phonon-assisted inter-well tunnelling amplitude. Virtual electronic admixture within one static well already contributes a nonzero value. It says nothing about long-distance ODLRO.

### 6.3 What the finite-oscillator calculations do not prove

Replay diagonalizes 80 or 120 relative oscillator states, rather than the full Hilbert space. It finds small doublet splittings and different behavior for bare and displaced pair operators. There is no interval eigensolver, oscillator-tail bound or rigorous splitting asymptotic. Near-degenerate floating-point gaps cannot be called exponentially small exact gaps on this evidence alone.

A finite dimer has no thermodynamic pair-order transition. A crossover defined from one observable cannot be relabeled T_pair. Extending the BO surface to a volume-uniform quantum free-energy or coherence bound remains open; no controlled Born-Oppenheimer error expansion in Omega/t is provided here.

## 7. Reflection positivity and route disposition

For free independent Einstein oscillators, the spatial stiffness is K(q)=K and

```
<X_q X_-q>_free = Omega/(2K) coth(beta Omega/2),
```

independent of momentum under unitary Fourier normalization. Thus a phonon spatial infrared estimate alone supplies no small-momentum electronic pair-field stiffness and no phonon-to-pair inequality. This is not a proof that every modified reflection or infrared argument fails.

Ordinary spatial reflection positivity in balanced canonical Holstein sectors was already disproved in ADIABATIC/LINEAR5-PAPER, proposition on canonical spatial RP. The negative cross-half zero-mode covariance there is not re-derived or claimed as new here. Grand-canonical or particle-hole modified reflections would need their own proof. A free Debye-Waller average cannot be factored out of the interacting Lang-Firsov trace, because electronic hopping does not commute with the displacement vertices. The finite-dimer fixture is only a numerical illustration of this failed factorization.

| Candidate route | Established here | Where it stops |
|---|---|---|
| (a) Reflection/chessboard/infrared | Free optical covariance has no q-dependent stiffness; prior ordinary canonical RP barrier identified | No valid interacting pair-field domination or modified RP theorem |
| (b) Slow imaginary-time/BO | Exact interacting nonzero-frequency spectral bound; exact two-site static landscape | No weighted rare-history or volume-uniform BO correction/coherence bound |
| (c) Single impurity/DMFT or finite anchor | Positive-determinant arbitrary Green amplification; exact finite-matrix Ward-Schur algebra | Annealed leakage, infinite-grid kernel identification and relation to model T_pair are open |
| (d) Tunnelling/energy-entropy | Exact static intra-well bare pair contribution and COM separation | Bare local correlation is not tunnelling; no controlled many-site dressed-coherence bound |

These are statements about precisely described method classes. None is a physical counterexample with T_pair/Omega diverging. No improvement over the reviewed LINEAR4 or STAGE7R temperature ceilings is established.
