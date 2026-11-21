# BARRIERS2-PAPER: claim-to-source map

Every numbered statement in `main.tex` is traced below to the reviewed source record
that proves it. Paper line numbers refer to `main.tex` as built in this directory;
source line numbers refer to the frozen records under
`D:/dev/scratch/ceiling-20261118/` (paths are relative to that root). This map was
refreshed after the independent pre-release review of this paper; the fixes it
prompted are listed in `FIX.md` next to this file.

Status legend used in the source records and repeated here:

- **PROVED** the analytical argument in the source record's `RIGOR.md`.
- **CERTIFIED** an exact-rational or outward-rounded interval computation in the
  source record's `replay.py` (and its independent implementation).
- **NUMERICAL** a finite-matrix or floating-point sanity check, not part of any proof.

Every source record used here has completed independent review:

- `MASSIVE/STATIC-MODE/REVIEW.md`: **PASS** (0 P0, 0 P1, 0 P2, 3 P3).
- `MASSIVE/LINEAR-FRESH/REVIEW.md`: **PASS** (0 P0, 0 P1, 0 P2, 5 P3).
- `ADIABATIC/PURESSH/REVIEW.md`: **PASS** with `F1`-`F6` fixed, and
  `ADIABATIC/PURESSH/REVIEW2.md`: all six findings **RESOLVED**, every core claim
  **PROVED**, every finite rational/interval check **CERTIFIED**. The four notes
  `N1`-`N4` of that second review are resolved in `ADIABATIC/PURESSH/FIX.md` §4 and
  re-verified there (`replay.py`, `replay.py --all-mutants` with 12 rejected mutants,
  and `ed_check.py`, each exit `0`). The frozen digest of the record used for Section 5
  below is `ADIABATIC/PURESSH/RIGOR.md` sha256
  `d04efa00eaa844e1cc1bdde4f8abe275f69daecfb2212b26ac2a25c6540adaa1`.

Paper-wide scope statement: every statement is about model quantities (`T_pair`,
`T_lin`, correlation functions, model free energies) of the precisely specified
Holstein or bond-SSH Hamiltonians. Nothing in the paper is a measured transition
temperature and nothing is a materials claim. `main.tex:1137-1170`
(`sec:notclaimed`) states this restriction in the paper.

## 1. Definitions and framework statements

| Paper item | `main.tex` lines | Source | Status |
|---|---|---|---|
| Holstein Hamiltonian and the two normalisations (`eq:H`, `eq:U`, `eq:dcomm`): `U = F^2/K` is the site relaxation energy, `G_x = sqrt(U_x Omega_x/2)` is the boson-operator coupling, `G_x^2 = U_x Omega_x/2`, and the double commutator equals `U_x Omega_x^2` | 134-171 | `MASSIVE/STATIC-MODE/RIGOR.md:5-18` (model, units, `U=g^2/K` with `g` the site force constant); notation harmonised with `ADIABATIC/SSHBOUND3-PAPER/main.tex:22-27`; the paper states explicitly that earlier notes write the site coupling as `U=g^2/K` with that lowercase `g` the site force constant, while in this paper lowercase `g` is the bond force constant of the Peierls model | Definitions, no claim |
| Pure bond-SSH Hamiltonian, `G_b = g^2/K`, `U_eff = 0` (`eq:Hssh`, `eq:Gb`) | 172-197 | `ADIABATIC/PURESSH/RIGOR.md:13-47` | Definitions, no claim |
| Definition `def:tpair` (pair-decay temperature as a model quantity, `eq:clustering`) | 198-217 | `ADIABATIC/PURESSH/RIGOR.md:95-104` (canonical pair-correlation decay temperature); `MASSIVE/STATIC-MODE/RIGOR.md:5-18` | Definition; no proof claimed |
| Remark after `def:tpair` (what a linear ceiling would mean) | 218-227 | `ADIABATIC/BARRIERS-PAPER/main.tex` (scope of the released ceilings) | Editorial, no claim |
| Route table `tab:routes` | 228-265 | `MASSIVE/STATIC-MODE/REVIEW.md:24-27`; `MASSIVE/LINEAR-FRESH/REVIEW.md:24-26`; `ADIABATIC/PURESSH/REVIEW.md:20-30` | Summary of the sections below |

## 2. Section 3: integrated first dynamic cumulant (`sec:cumulant`)

| Paper item | `main.tex` lines | Source label and lines | Status |
|---|---|---|---|
| `lem:first` Exact first coefficient, no truncation (`eq:first`, `eq:second`, `eq:Kx`) | 305-351 | `MASSIVE/STATIC-MODE/RIGOR.md:69-100`, eq. (6) at `:94-98`; disclosed by `MASSIVE/STATIC-MODE/REVIEW.md:5-11` as PROVED | **PROVED** |
| `lem:aux` Auxiliary bounds in three items, with no numbered equation of its own: (i) `q(a) <= a^2/12`, `chi_x(i nu) <= beta/4` and `a_x <= U Omega^2 beta^3/48`; (ii) the spectral variance identity `sum p_a p_b (e_b-e_a)^2 = 2 t^2 d_x` and `a_x <= d_x t^2 U Omega^2 beta^5/1440`; (iii) the static Combes-Thomas bound `|G| <= (25/16) e^{-2 alpha d(x,y)}` with `alpha = 1/(1+16 beta t)` | 352-392 | `MASSIVE/STATIC-MODE/RIGOR.md:103-105` eq. (7); `:108-118` eq. (8); `:40-54` with `:58-64` eq. (5); static decay `:58-67` | **PROVED** |
| `remark` after `lem:aux` (items (i)-(ii) bound the cumulant and item (iii) already gives static exponential decay, so any annealed static average inherits it) | 393-401 | `MASSIVE/STATIC-MODE/RIGOR.md:58-67`, `:103-121` | **PROVED** (restates the three bounds) |
| `thm:witness` Fixed-hopping resonance: the lower bound `a_x(W) >= U Omega^2/(1200 tau^3)` on `0 < Omega <= tau <= t/4`, obtained from the certified lower bound `a_left >= 1/1148 > 1/1200` (`eq:fields3`, `eq:witness`, `eq:Aweight`, `eq:witnessgeneral`, `eq:constant`) | 404-464 | `MASSIVE/STATIC-MODE/RIGOR.md:20-24` (proposition, eq. (1)); `:123-139` (three-site open path, exact diagonalisation); `:141-157` (the lower bound `1/1148 > 1/1200`); constants CERTIFIED in the same record's `replay.py:exact_constants` (`pi<22/7`, `(22/7)^2<10`, `tanh 1>3/4`, `(2/3)*4*(3/4)/(41*56)=1/1148`), listed in `MASSIVE/STATIC-MODE/REVIEW.md:16` | **PROVED**, constants **CERTIFIED** |
| `thm:torus` Embedding on every square torus: `a_x(W_B) >= U Omega^2/(2400 tau^3)` for `L >= 4` (`eq:torus`, `eq:schur`) | 465-507 | `MASSIVE/STATIC-MODE/RIGOR.md:26-30` (eq. (2)); `:159-172` (finite-barrier square-torus embedding); half constant `1/2400` certified at `replay.py:exact_constants`, `MASSIVE/STATIC-MODE/REVIEW.md:16` | **PROVED**, constants **CERTIFIED** |
| `cor:scale` Linear-scale corollary: `a_x >= U/(2400 C^3 Omega)` at `tau = C Omega` (`eq:linear`) | 508-526 | `MASSIVE/STATIC-MODE/RIGOR.md:32-38` (eq. (3)) | **PROVED** |
| `rem:class` Obstructed proof class | 529-541 | `MASSIVE/STATIC-MODE/RIGOR.md:175-183` (scoped method obstruction, section 6) | **PROVED** (as a scoped obstruction) |
| `rem:notclass` What the class argument does not establish | 542-558 | `MASSIVE/STATIC-MODE/RIGOR.md:183-189` | **PROVED** (negative scope statement) |

## 3. Section 4: positive determinants and impurity propagators (`sec:det`)

| Paper item | `main.tex` lines | Source label and lines | Status |
|---|---|---|---|
| `lem:fsum` Interacting nonzero-Matsubara sum rule (`eq:fsum`, `eq:fsum2`, `eq:lehmann`), declared in the paper as a classical oscillator `f`-sum lemma, not as a new claim | 575-623 | `MASSIVE/LINEAR-FRESH/RIGOR.md:28-56` (Theorem 2.1, eqs. (2.1)-(2.2)), proof `:58-96` including the commutator identity (2.3) at `:75-81` and the unbounded-oscillator justification at `:85` | **PROVED** (cited as classical; Placzek/oscillator sum rule) |
| `remark` after `lem:fsum` (what the sum rule does and does not obstruct) | 624-635 | `MASSIVE/LINEAR-FRESH/RIGOR.md:89-94` ("What this theorem obstructs and what it supplies") | **PROVED** |
| `thm:amp` Arbitrary conditional amplification, `det(I+U) > 1` with `|G(1,0)_{00}| ~ B^2/(2v^2)` (`eq:impurity`, `eq:Gdef`, `eq:amp`, `eq:Gclosed`, `eq:Glower`) | 638-691 | `MASSIVE/LINEAR-FRESH/RIGOR.md:97-127` (Theorem 3.1, eqs. (3.1)-(3.2)), proof `:128-165` | **PROVED** |
| `rem:smooth` Smooth and finite-action histories, with the oscillator action written in the same symbol `epsilon(u)` as the impurity level of `eq:impurity` | 692-708 | `MASSIVE/LINEAR-FRESH/RIGOR.md:166-170` | **PROVED** |
| `cor:fixture` Interval-certified two-slice fixture, `B=6`, `v=1/2`: `det(I+U) > 15`, `|G(1,0)_{00}| > 52.89` (`eq:fixture`) | 709-724 | `MASSIVE/LINEAR-FRESH/RIGOR.md:172-181`; Arb (80 decimal digits) and an independently coded `mpmath.iv` (60 digits) replay, `MASSIVE/LINEAR-FRESH/REVIEW.md:16` | **CERTIFIED** |
| `rem:ward` Finite-matrix Ward and Schur algebra (`eq:ward1`-`eq:ward4`) and the finite-grid moment estimate with the enclosure `67/50 < C_aux < 27/20` | 727-774 | `MASSIVE/LINEAR-FRESH/RIGOR.md:183-233` (eqs. (4.1)-(4.4)) and `:257-264` (eq. (5.2)) | **PROVED** (finite matrices only), enclosure **CERTIFIED** |
| `rem:dimer` Two static dimer anchors, with the Holstein coupling written as `G` in the notation of `eq:U` (`eq:com`, `eq:dimermin`) | 775-803 | `MASSIVE/LINEAR-FRESH/RIGOR.md:303-335` (sections 6.1-6.2, eq. (6.1)) | **PROVED** |

## 4. Section 5: what survives at `U_eff = 0` (`sec:survives`)

The whole section derives from the PURE-SSH record. That record passed independent
review twice: `ADIABATIC/PURESSH/REVIEW.md` (PASS after `F1`-`F6`) and
`ADIABATIC/PURESSH/REVIEW2.md` (all `F1`-`F6` RESOLVED, every core claim **PROVED**,
every constant **CERTIFIED**), with the second review's four notes `N1`-`N4` resolved
and re-verified in `ADIABATIC/PURESSH/FIX.md` §4. No statement in this section carries
an outstanding review condition.

| Paper item | `main.tex` lines | Source label and lines | Status |
|---|---|---|---|
| Constants `eq:constants`, `eq:constants2` (`c_0 = 2^-10`, `xi_0 = 2^-9 beta^-1`, `epsilon = 2/1023`, `q_GC = 32/341`, `A_GC = 341/103`, `b_GC = 32/103`, `R_max = 24718511/9834543 < 3`, `q_src = 72/341`, `b_src = 216/269`) and the source vertex operator `Y_e'(theta) = e^{i theta} Delta_x^dagger Delta_{x+r} + h.c.` of operator norm `1` | 814-836 | `ADIABATIC/PURESSH/RIGOR.md:48-73` (§1.2 explicit constants, **CERTIFIED**); source operator `:41-42`, `:85-88` and `ADIABATIC/PURESSH/FIX.md` §1 `F3` | **CERTIFIED** |
| `thm:gc` Frequency- and `mu`-uniform pair clustering (`eq:gcb`, `eq:rmax`, `eq:source`), with the certified activity `eq:activity` | 837-911 | `ADIABATIC/PURESSH/RIGOR.md:77-93` (Theorem 1.1), proof `:372-406`; ingredients `:145-175` (Lemma 2.2), `:180-210` (Lemmas 3.1-3.2), `:214-249` (Lemmas 4.1-4.2), `:264-278` (Lemma 5.1), `:279-336` (Proposition 5.2 activity bound), `:339-343` (Lemma 5.3), `:344-371` (Lemma 5.4) | **PROVED**, constants **CERTIFIED** |
| `lem:canon` Boundary spring-constant bracket (`eq:bdry`): the two-sided bracket of `log Z_{Lambda_L}(xi)` by block-decoupled log-partitions with boundary spring constant `K/2` and `2K`, with boundary cost `C_bdry |partial| + beta|xi| |partial_src|` | 914-962 | `ADIABATIC/PURESSH/RIGOR.md:411-445` (Lemma 6.1 and its proof: Young's inequality, min-max monotonicity, factorisation of the boundary oscillators) | **PROVED**, **CERTIFIED** (constants `:48-73`) |
| `thm:canon` Thermodynamic canonical decay and `k_B T_pair <= 1024(|t| + G_b)` (`eq:canon`, `eq:tpair`), whose proof summary follows Lemma `lem:canon` plus concavity of the canonical free-energy density, Legendre supporting `mu`, and convexity of `xi -> L^-2 log Zhat` | 968-1012 | `ADIABATIC/PURESSH/RIGOR.md:95-104` (Theorem 1.2); proof `:447-470` (§6, steps 1-2 including the Legendre discrepancy `delta_L -> 0`); `:411-445` (Lemma 6.1) | **PROVED** |
| `remark` after `thm:canon` (closes the `U_eff -> 0` case that the strong-coupling ceilings leave open: the rates of `stage6` and `sshbond3` both contain `t^2/U_eff`, and at `t=0` the `2^13 G_b` threshold of `sshbond3` becomes `2^10 G_b`) | 1013-1023 | `ADIABATIC/SSHBOUND3-PAPER/main.tex:24-34` (released bound `k_B T_pair <= 2^27(t^2/U_eff + G_b)` with `beta G_b <= 2^-13`); `ADIABATIC/STAGE6-PAPER/main.tex:348` (Holstein strong-coupling ceiling `2^27 t^2/U` and the comparator `1024 t`); `ADIABATIC/PURESSH/RIGOR.md:95-104` | **PROVED** as a comparison |
| `thm:routes` (i) no phonon-induced instantaneous atomic gap, `Delta_eff = 0` on `C_4` at `N=4`: exact spectra `{0,4,8,12}` on the two fully singly occupied `S^z=0` sectors, `{2,4,6,10}` on the remaining `S^z=0` sector, and at most `10` on all others | 1027-1123 | `ADIABATIC/PURESSH/RIGOR.md:106-107` (Theorem 1.3(1)); `:476-511` (Proposition 7.1, all nine `(N_up, N_down, N_odd)` sectors, six spin-flip-conjugate classes, `70 = binomial(8,4)` states); sector wording after `ADIABATIC/PURESSH/FIX.md` §4 `N3` | **PROVED**, **CERTIFIED** |
| `thm:routes` (ii) non-terminating bond Lang-Firsov expansion (`eq:bondcomm`), with `||[T_b,T_b']||_op = 2` and first-order terms surviving at `Omega -> 0` | 1027-1029, 1040-1050, 1052-1065 | `ADIABATIC/PURESSH/RIGOR.md:108` (Theorem 1.3(2)); `:514-541` (Proposition 7.2) | **PROVED**, **CERTIFIED** |
| `thm:routes` (iii) free-fermion algebraic decay forbids hopping-uniform clustering (`eq:staircase`), with the rational witness at `m=2` | 1027-1029, 1066-1080, 1081-1088 | `ADIABATIC/PURESSH/RIGOR.md:109-113` (Theorem 1.3(3)); `:544-570` (Proposition 7.3); witness values `:99-107`, `:581` and `ADIABATIC/PURESSH/FIX.md` §4 `N4` | **PROVED**, **CERTIFIED** |
| `remark` after `thm:routes` (what items (i)-(iii) do and do not say, and why `thm:gc` needs the combined condition `beta|t| + beta G_b <= 2^-10`) | 1124-1135 | `ADIABATIC/PURESSH/RIGOR.md:486-493`, `:514-541`, `:544-570` | **PROVED** |

## 5. Numerical facts quoted in the paper

All of these are labelled as numbers in the text and none carries a proof.

| Fact as printed | `main.tex` lines | Source |
|---|---|---|
| `det(I+U) = 15.790282... > 15` and `|G_{00}| = 52.8957540935... > 52.89` at `B=6`, `v=1/2`; interval-certified, not merely numerical | 709-724 | `MASSIVE/LINEAR-FRESH/RIGOR.md:172-181` |
| `4/(9 pi^4) = 4.5627e-3 > A_GC q_GC^3 = 2.7359e-3` at `m=2`, `d=3` | 1066-1088 | `ADIABATIC/PURESSH/RIGOR.md:99-113`, `:581`; `ADIABATIC/PURESSH/FIX.md` §4 `N4` |
| Static electronic pair admixture `t^2/(4U^2) = 1/64` at `U=4`, `t=1` and `1/68` at the unrelaxed field `q=2U` | 775-803 | `MASSIVE/LINEAR-FRESH/RIGOR.md:303-335` (section 6.2); `MASSIVE/LINEAR-FRESH/REVIEW.md:17-20` |
| The oscillator action `int[(eps')^2/Omega^2 + eps^2]/(2U)` stays finite for the smoothing of the step profile | 692-708 | `MASSIVE/LINEAR-FRESH/RIGOR.md:166-170` (continuity and admissible phonon histories) |
| `1/1148 > 1/1200` (a lower bound on `a_left`) and the half constant `1/2400` | 456, 507 | `MASSIVE/STATIC-MODE/RIGOR.md:141-157`; `replay.py:exact_constants` |

## 6. Review notes applied to the paper text

Source-record notes:

- `MASSIVE/STATIC-MODE/REVIEW.md:55-58` P3 note 1 (the symbol `phi` is reused for two
  different quantities): not applicable, the paper does not use `phi`.
- `MASSIVE/STATIC-MODE/REVIEW.md:64-66` P3 note 2 (Schur block wording of the torus
  embedding): applied. The paper says "Schur complement blocks" only of the exact
  Schur complementation used in the proof, and the finite barrier is described as a
  block-diagonal field, not as a Schur block (`main.tex` 465-507).
- `MASSIVE/STATIC-MODE/REVIEW.md:67-69` P3 note 3 (the site coupling `U` versus the
  released linear notes): applied. `main.tex:156-168` defines `U_x = F_x^2/K_x`,
  `F_x X_x = G_x b_x` and `G_x^2 = U_x Omega_x/2`, states that `M_x` and `K_x` enter
  only through `Omega_x` and `U_x`, and states that earlier notes write the site
  coupling as `U = g^2/K` with that lowercase `g` the site force constant, whereas in
  this paper lowercase `g` is the bond force constant of the Peierls model.
- `MASSIVE/LINEAR-FRESH/REVIEW.md:33` P3 note 3 (equation (4.4) assumes diagonal
  `D_pm`): applied. `main.tex:753-758` states the row sums for diagonal
  `D_pm = diag(D_{pm,m})`.
- `MASSIVE/LINEAR-FRESH/REVIEW.md:35-36` P3 note 4 (the finite-particle core phrasing
  in the unbounded-oscillator justification): applied. `main.tex:612-621` replaces the
  "common core of finite-particle vectors" claim by the form-boundedness argument
  `D(H^{1/2}) = D(N_osc^{1/2})` and the Parseval identity for
  `psi_x |psi_a>`.
- `MASSIVE/LINEAR-FRESH/REVIEW.md:24-26` recommendation (Theorem 2.1 and the dimer
  facts are supporting material): applied. `lem:fsum` is introduced as a classical
  `f`-sum lemma and the Ward and dimer results appear as remarks.
- `ADIABATIC/PURESSH/REVIEW.md:14,50` P1 (the staircase ray, the exponent `d^-2` and
  the `m=2` witness): applied, the paper uses `r_m = (m, m-1)` and `4/(pi^4 d^2)`.
- `ADIABATIC/PURESSH/REVIEW.md:53-58` P1 (source operator normalisation and the proved
  rate bound): applied. `main.tex:833-835` defines
  `Y_e'(theta) = e^{i theta} Delta_x^dagger Delta_{x+r} + e^{-i theta}
  Delta_{x+r}^dagger Delta_x` with `||Y_e'(theta)||_op = 1` and no factor `1/2`,
  consistent with `ADIABATIC/PURESSH/RIGOR.md:41-42, 85-88`, and `main.tex:855-862`
  states the `xi`-linear bound `eq:source` with the `4 xi^2/xi_0^2` remainder.
- `ADIABATIC/PURESSH/REVIEW.md:60-63` P2 (Proposition 7.1 must list the `N_odd = 2` and
  `S_z != 0` sectors): applied. `main.tex:1081-1105` lists all nine invariant sectors of
  the half-filled `70`-dimensional space, their dimensions and their maxima, as revised
  by `ADIABATIC/PURESSH/FIX.md` §4 `N3`.
- `ADIABATIC/PURESSH/REVIEW.md:65-68` P2 (2D BKT quasi-long-range order is not
  off-diagonal long-range order): applied. The paper claims neither ODLRO nor the
  absence of it; `sec:open` item (6) (`main.tex:1205-1210`) asks only for the joint
  estimate in `beta t` and `beta G_b`.
- `ADIABATIC/PURESSH/REVIEW.md:70-76` P3 (rounding and notation typos): applied, the
  paper prints `R_max = 24718511/9834543 < 3` without a truncated decimal and prints
  the witness values `4.5627e-3` and `2.7359e-3`.

Notes from the review of this paper (`REVIEW.md`), all applied; the item-by-item list
with file and line is in `FIX.md`:

- the Ward-Schur upper bound now uses the positive semidefinite `V D_-^{-1} V^*`;
- the proof summary of `thm:canon` now follows `ADIABATIC/PURESSH/RIGOR.md` §6 through
  the bracket of Lemma `lem:canon`, the Legendre discrepancy and the convexity of the
  source-dependent partition function, and no longer mentions a single-bond activity
  derivative or an isoperimetric inequality;
- the proof summary of `thm:gc` now names multilinear Schatten-Hoelder and the exact
  Gaussian Wick integral `int int C_beta = beta/K`;
- the `stage6` citation is described as the strong-coupling Holstein ceiling it is;
- `sec:notclaimed` item (a) and item (d) now acknowledge that `thm:canon` improves the
  `U_eff -> 0` behaviour, and only there.

## 7. Items that are NOT claimed

`main.tex:1137-1170` (`sec:notclaimed`) and the disclosures at 1213-1218 state:

- no bound on a measured transition temperature, no materials claim;
- no claim that `T_pair/Omega` can diverge, and no claim that a linear ceiling is
  false;
- no counterexample inside the interacting model, only obstructions to specified
  proof classes;
- no gain at the linear scale `T_lin = C(t,U) Omega`; the only improved model bound is
  `thm:canon` at `U_eff = 0`, which is uniform in `Omega` but does not vanish as
  `Omega -> 0`;
- no interval certification of the finite-matrix and floating-point diagnostics;
- no external data set.
