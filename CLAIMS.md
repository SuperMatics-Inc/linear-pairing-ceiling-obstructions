# BARRIERS2-V2: claim-to-source map

Every numbered statement in `main.tex` is traced below to the source record that
proves it. Paper line numbers refer to `main.tex` as built in this directory; source
line numbers refer to the frozen records under `D:/dev/scratch/ceiling-20261118/`
(paths are relative to that root).

Status legend used in the source records and repeated here:

- **PROVED** the analytical argument in the source record's `RIGOR.md`.
- **CERTIFIED** an exact-rational or outward-rounded interval computation in the
  source record's `replay.py` (and its independent implementation).
- **NUMERICAL** a finite-matrix or floating-point sanity check, not part of any proof.

## 0. Review status of the sources

| Source record | Independent review | Status carried into this paper |
|---|---|---|
| `MASSIVE/STATIC-MODE/REVIEW.md:4-9` | **PASS** (0 P0, 0 P1, 0 P2, 3 P3) | final; the three P3 notes are applied (Section 6 below) |
| `MASSIVE/LINEAR-FRESH/REVIEW.md:4-9` | **PASS** (0 P0, 0 P1, 0 P2, 5 P3) | final; the P3 notes are applied (Section 6 below) |
| `MASSIVE/UNIFORM-SSH/REVIEW.md:5` | **PASS-WITH-FIXES** (0 P0, 0 P1, 2 P2 in `SCOPING.md`, 6 P3) | findings `F1`-`F8` resolved in `FIX.md` |
| `MASSIVE/UNIFORM-SSH/REVIEW2.md:6` | **PASS** (all `F1`-`F8` RESOLVED; no new finding) | final for the source record |
| `ADIABATIC/PURESSH/REVIEW.md:8-18`, verdict table `:20-30` | **PASS** after `F1`-`F6` and `F7`-`F8` | first review final |
| `ADIABATIC/PURESSH/REVIEW2.md` (SHA-256 `25f1115d...6bfe`) | **PASS-WITH-FIXES**: all six `REVIEW.md` findings `F1`-`F6` RESOLVED, every core claim PROVED/CERTIFIED; notes `N1`-`N4` resolved in `ADIABATIC/PURESSH/FIX.md` §4 | final; the `U_eff = 0` `PURESSH` items in Section 5 are PROVED |
| this paper, `REVIEW.md:9` | **PASS-WITH-FIXES** (0 P0, 3 P1, 4 P2, 5 P3) | all 12 findings applied, listed in `FIX.md` |
| this paper, `REVIEW2.md:5` | **PASS-WITH-FIXES**, all 12 findings RESOLVED, 1 new P2 (`N1`) | `N1` (`value` for `derivative`) is applied: `main.tex:1088-1094` now reads "its derivative at $\xi=0$" |

The `U_eff`-uniform generalisation of Section 5 was installed from
`MASSIVE/UNIFORM-SSH/AMENDMENT.md`, which transcribes the reviewed theorems of
`MASSIVE/UNIFORM-SSH/RIGOR.md` (Theorems 1.1-1.5) into this paper's notation. The
transcription has not had its own independent review; every constant, hypothesis and
scope condition below is checked against `RIGOR.md` line by line, and the paper's
`REVIEW.md`/`REVIEW2.md` predate the transcription.

Paper-wide scope statement: every statement is about model quantities (`T_pair`,
`T_lin`, correlation functions, model free energies) of the precisely specified
Holstein, bond-SSH or Hubbard-Holstein-SSH Hamiltonians. Nothing in the paper is a
measured transition temperature and nothing is a materials claim.
`main.tex:1409-1446` (`sec:notclaimed`) states this restriction in the paper.

## 1. Definitions and framework statements

| Paper item | `main.tex` lines | Source | Status |
|---|---|---|---|
| Holstein Hamiltonian and the two normalisations (`eq:H`, `eq:U`, `eq:dcomm`): `U = F^2/K` is the site relaxation energy, `G_x = sqrt(U_x Omega_x/2)` is the boson-operator coupling, `G_x^2 = U_x Omega_x/2`, and the double commutator equals `U_x Omega_x^2` | 142-181 | `MASSIVE/STATIC-MODE/RIGOR.md:5-18` (model and units, which write the site coupling as `U = g^2/K` with `g` the site force constant); notation harmonised with `ADIABATIC/SSHBOUND3-PAPER/main.tex:22-27`; `main.tex:176-181` states that earlier notes write the site coupling as `U = g^2/K` with lowercase `g` the site force constant, whereas here lowercase `g` is the bond force constant | Definitions, no claim |
| Hubbard-Holstein-SSH Hamiltonian (`eq:Hhubssh`), the effective interaction (`eq:Ueff`), the pure bond-SSH special case (`eq:Hssh`), and `G_b = g^2/K` (`eq:Gb`); bond oscillators carry `M_b > 0` and `Omega_b = sqrt(K/M_b)`, site oscillators carry `Omega_0 > 0` | 182-235 | `ADIABATIC/PURESSH/RIGOR.md:13-47`; `MASSIVE/UNIFORM-SSH/RIGOR.md:15-53` (Hamiltonian, `U_eff = U_0 - 2g_0^2/Omega_0`, Lang-Firsov frame) | Definitions, no claim |
| Definition `def:tpair` (pair-decay temperature as a model quantity, `eq:clustering`) | 241-254 | `ADIABATIC/PURESSH/RIGOR.md:95-104` (canonical pair-correlation decay temperature); `MASSIVE/STATIC-MODE/RIGOR.md:5-18` | Definition; no proof claimed |
| Remark after `def:tpair` (what a linear ceiling would mean) | 256-265 | `ADIABATIC/BARRIERS-PAPER/main.tex` (scope of the released ceilings) | Editorial, no claim |
| Route table `tab:routes` | 272-307 | `MASSIVE/STATIC-MODE/REVIEW.md:46-57`; `MASSIVE/LINEAR-FRESH/REVIEW.md:75-82`; `ADIABATIC/PURESSH/REVIEW.md:20-30`; `MASSIVE/UNIFORM-SSH/REVIEW.md:11-28` | Summary of the sections below |

## 2. Section 3: integrated first dynamic cumulant (`sec:cumulant`)

| Paper item | `main.tex` lines | Source label and lines | Status |
|---|---|---|---|
| `lem:first` Exact first coefficient, no truncation, with the covariance and ratio definitions `eq:cov`, `eq:RW` and the formulas `eq:first`, `eq:second`, `eq:Kx` | 348-394 | `MASSIVE/STATIC-MODE/RIGOR.md:69-100`, eq. (6) at `:94-98`; PROVED per `MASSIVE/STATIC-MODE/REVIEW.md:6` | **PROVED** |
| `lem:aux` Auxiliary bounds in three items: (i) `q(a) <= a^2/12`, `chi_x(i nu) <= beta/4` and `a_x <= U Omega^2 beta^3/48`; (ii) the spectral variance identity `sum p_a p_b (e_b-e_a)^2 = 2 t^2 d_x` and `a_x <= d_x t^2 U Omega^2 beta^5/1440`; (iii) the static Combes-Thomas bound `|G| <= (25/16) e^{-2 alpha d(x,y)}` with `alpha = 1/(1+16 beta t)` | 395-435 | `MASSIVE/STATIC-MODE/RIGOR.md:103-105` eq. (7); `:108-118` eq. (8); `:40-54` with `:58-64` eq. (5); static decay `:58-67` | **PROVED** |
| Remark after `lem:aux` (items (i)-(ii) bound the cumulant, item (iii) already gives static exponential decay, so any annealed static average inherits it) | 436-444 | `MASSIVE/STATIC-MODE/RIGOR.md:58-67`, `:103-121` | **PROVED** (restates the three bounds) |
| `thm:witness` Fixed-hopping resonance: the lower bound `a_x(W) >= U Omega^2/(1200 tau^3)` on `0 < Omega <= tau <= t/4`, obtained from the certified lower bound `a_left >= 1/1148 > 1/1200` (`eq:fields3`, `eq:witness`, `eq:Aweight`, `eq:witnessgeneral`, `eq:constant`) | 447-507 | `MASSIVE/STATIC-MODE/RIGOR.md:20-24` (proposition, eq. (1)); `:123-139` (three-site open path, exact diagonalisation); `:141-157` (the lower bound `1/1148 > 1/1200`); constants CERTIFIED in `replay.py:exact_constants` (`pi<22/7`, `(22/7)^2<10`, `tanh 1>3/4`, `(2/3)*4*(3/4)/(41*56)=1/1148`), listed in `MASSIVE/STATIC-MODE/REVIEW.md:7` and recomputed independently at `:83-95` | **PROVED**, constants **CERTIFIED** |
| `thm:torus` Embedding on every square torus: `a_x(W_B) >= U Omega^2/(2400 tau^3)` for `L >= 4` (`eq:torus`, `eq:schur`) | 508-550 | `MASSIVE/STATIC-MODE/RIGOR.md:26-30` (eq. (2)); `:159-172` (finite-barrier square-torus embedding); half constant `1/2400` certified in `replay.py:exact_constants`, `MASSIVE/STATIC-MODE/REVIEW.md:7` | **PROVED**, constants **CERTIFIED** |
| `cor:scale` Linear-scale corollary: `a_x >= U/(2400 C^3 Omega)` at `tau = C Omega` (`eq:linear`) | 551-570 | `MASSIVE/STATIC-MODE/RIGOR.md:32-38` (eq. (3)) | **PROVED** |
| `rem:class` Obstructed proof class | 572-583 | `MASSIVE/STATIC-MODE/RIGOR.md:175-183` (scoped method obstruction, section 6) | **PROVED** (as a scoped obstruction) |
| `rem:notclass` What the class argument does not establish | 585-600 | `MASSIVE/STATIC-MODE/RIGOR.md:183-189` | **PROVED** (negative scope statement) |

## 3. Section 4: positive determinants and impurity propagators (`sec:det`)

| Paper item | `main.tex` lines | Source label and lines | Status |
|---|---|---|---|
| `lem:fsum` Interacting nonzero-Matsubara sum rule (`eq:fsum`, `eq:fsum2`, `eq:lehmann`), declared in the paper as a classical oscillator `f`-sum lemma (Placzek/oscillator sum rule), not as a new claim | 618-666 | `MASSIVE/LINEAR-FRESH/RIGOR.md:28-56` (Theorem 2.1, eqs. (2.1)-(2.2)), proof `:58-96` including the commutator identity (2.3) at `:75-81` and the unbounded-oscillator justification at `:85` | **PROVED** (cited as classical) |
| Remark after `lem:fsum` (what the sum rule does and does not obstruct) | 667-678 | `MASSIVE/LINEAR-FRESH/RIGOR.md:89-94` | **PROVED** |
| `thm:amp` Arbitrary conditional amplification, `det(I+U) > 1` with `|G(1,0)_{00}| ~ B^2/(2v^2)` (`eq:impurity`, `eq:Gdef`, `eq:amp`, `eq:Gclosed`, `eq:Glower`) | 681-734 | `MASSIVE/LINEAR-FRESH/RIGOR.md:97-127` (Theorem 3.1, eqs. (3.1)-(3.2)), proof `:128-165` | **PROVED** |
| `rem:smooth` Smooth and finite-action histories, with the oscillator action written in the symbol `epsilon(u)` of `eq:impurity` | 735-750 | `MASSIVE/LINEAR-FRESH/RIGOR.md:166-170` | **PROVED** |
| `cor:fixture` Interval-certified two-slice fixture, `B=6`, `v=1/2`: `det(I+U) > 15`, `|G(1,0)_{00}| > 52.89` (`eq:fixture`) | 752-768 | `MASSIVE/LINEAR-FRESH/RIGOR.md:172-181`; Arb (80 decimal digits) and an independently coded `mpmath.iv` (60 digits) replay, `MASSIVE/LINEAR-FRESH/REVIEW.md:16` | **CERTIFIED** |
| `rem:ward` Finite-matrix Ward and Schur algebra (`eq:ward1`-`eq:ward4`) and the finite-grid moment estimate with the enclosure `67/50 < C_aux < 27/20` | 770-816 | `MASSIVE/LINEAR-FRESH/RIGOR.md:183-233` (eqs. (4.1)-(4.4)) and `:257-264` (eq. (5.2)) | **PROVED** (finite matrices only), enclosure **CERTIFIED** |
| `rem:dimer` Two static dimer anchors, with the Holstein coupling written as `G` in the notation of `eq:U` (`eq:com`, `eq:dimermin`) | 818-845 | `MASSIVE/LINEAR-FRESH/RIGOR.md:303-335` (sections 6.1-6.2, eq. (6.1)) | **PROVED** |

## 4. Section 5: the `U_eff`-uniform ceiling and combined bounds (`sec:survives`)

Section 5 has two source records. The `U_eff`-uniform statements come from the
`UNIFORM-SSH` record (Theorems 1.1-1.5), which inherits the `PURESSH` machinery; the
three `U_eff = 0` route obstructions (`thm:routes`) remain `PURESSH` statements and are
so marked. `UNIFORM-SSH` passed `REVIEW.md` (`PASS-WITH-FIXES`) and `REVIEW2.md`
(`PASS`). `PURESSH` passed `REVIEW.md` and `REVIEW2.md` (`PASS-WITH-FIXES`, all six
first-round findings resolved, `ADIABATIC/PURESSH/FIX.md` §4 closing its notes
`N1`-`N4`), so every item in this section rests on twice-reviewed source text.

| Paper item | `main.tex` lines | Source label and lines | Status |
|---|---|---|---|
| Intro to Section 5 (uniformity in `U_eff`, the combination with strong-coupling bounds, the minimum ceilings, and the `U_eff = 0` closure) | 847-860 | `MASSIVE/UNIFORM-SSH/RIGOR.md:91-138` (main theorems and their union of hypotheses) | **PROVED** as a summary |
| Constants `eq:constants`, `eq:constants2` (`c_0 = 2^-10`, `xi_0 = 2^-9 beta^-1`, `epsilon = 2/1023`, `q_GC = 32/341`, `A_GC = 341/103`, `b_GC = 32/103`, `R_max = 24718511/9834543 < 3`) and the source vertex operator `Y_e'(theta) = e^{i theta} Delta_x^dagger Delta_{x+r} + h.c.` of operator norm `1` | 861-883 | `ADIABATIC/PURESSH/RIGOR.md:48-73` (§1.2 explicit constants, **CERTIFIED**), inherited unchanged by `MASSIVE/UNIFORM-SSH/RIGOR.md:54-90`; source operator `PURESSH/RIGOR.md:41-42`, `:85-88` and `ADIABATIC/PURESSH/FIX.md` §1 `F3` | **CERTIFIED** |
| `thm:gc` Frequency-, `mu`- and `U_eff`-uniform pair clustering (`eq:gcb`, `eq:rmax`, `eq:source`) for all `U_eff` in `R`, with the certified activity `eq:activity` | 884-989 | `MASSIVE/UNIFORM-SSH/RIGOR.md:93-103` (Theorem 1.1), proof `§3.1` at `:169-205`; inherited ingredients `PURESSH/RIGOR.md:145-175` (Lemma 2.2), `:180-210` (Lemmas 3.1-3.2), `:214-249` (Lemmas 4.1-4.2), `:264-371` (polymer and activity bounds); Lang-Firsov site factor `UNIFORM-SSH/RIGOR.md:152-165` | **PROVED**, constants **CERTIFIED** |
| `rem:uelschi` Relation to pure-Hubbard `U`-uniform hopping expansions | 991-1001 | `MASSIVE/UNIFORM-SSH/RIGOR.md:306-312` (§6, literature and scope); `MASSIVE/UNIFORM-SSH/REVIEW2.md:24` (§2.4 RESOLVED); external entries `uelschi1999`, `uelschi2004`, `frohlich2005` transcribed from `MASSIVE/UNIFORM-SSH/AMENDMENT.md:619-657` | **PROVED** as a comparison |
| `lem:canon` Boundary spring-constant bracket (`eq:bdry`): the two-sided bracket of `log Z_{Lambda_L}(xi)` by block-decoupled log-partitions at boundary spring constants `K/2` and `2K`, with boundary cost `C_bdry |partial| + beta|xi| |partial_src|`, valid for every `U_0,g_0,mu` real and `Omega_0,Omega_b > 0` | 1003-1054 | `ADIABATIC/PURESSH/RIGOR.md:411-445` (Lemma 6.1) with the on-site-locality audit of `MASSIVE/UNIFORM-SSH/RIGOR.md:142-150` (item 6) and `:196-205`; second review `ADIABATIC/PURESSH/REVIEW2.md:1-14` (all findings RESOLVED) | **PROVED** (the `U_eff` extension is PROVED in `UNIFORM-SSH`) |
| `thm:canon` Thermodynamic canonical decay uniformly in `U_eff`, `k_B T_pair <= 1024(|t| + G_b)` and `k_B T_pair^can(n) <= 1024(|t| + G_b)` (`eq:canon`, `eq:tpair`), whose proof summary uses Lemma `lem:canon`, concavity of the canonical pressure density, the supporting `mu`, the Legendre discrepancy, and convexity in the real source | 1056-1095 | `MASSIVE/UNIFORM-SSH/RIGOR.md:104-113` (Theorem 1.2), proof `:198-205`; inherited `PURESSH/RIGOR.md:95-104` and `:447-470` | **PROVED** |
| Remark after `thm:canon` (uniformity in `U_eff`, `Omega_b`, `Omega_0`; not a linear ceiling; closes the `U_eff = 0` case; the `t = 0` threshold `2^13 G_b` of `sshbond3` becomes `2^10 G_b`; no `beta U_eff` factor remains) | 1097-1113 | `ADIABATIC/SSHBOUND3-PAPER/main.tex:24-34`; `ADIABATIC/STAGE6-PAPER/main.tex:348`; `MASSIVE/UNIFORM-SSH/RIGOR.md:246-253` (§5.1, why the Hubbard-Stratonovich vertex contributes `e^{beta U/2}-1`) | **PROVED** as a comparison |
| `thm:min-att` Combined minimum ceiling for `U_eff < 0`: (i) the pair bound with prefactor `1965840/475579` and decay base `48645/524224` under `beta t^2/|U_eff| <= 2^-27` and `beta G_b <= 2^-13`, grand canonical and canonical; (ii) the minimum ceiling `eq:minatt`, and `T_pair = 0` at `t = g = 0` for every `U_eff` | 1124-1167 | `MASSIVE/UNIFORM-SSH/RIGOR.md:114-121` (Theorem 1.3) and `:209-218` (§4.1); constants at `:67-77`; atomic-limit vanishing `:286-304` (§5.5) | **PROVED**, constants **CERTIFIED** |
| `thm:min-rep` Repulsive windows and half-filling ceiling for `U_eff > 0`: (i) Mott window with `G = U_eff/2 - |mu|`; (ii) canonical half filling `eq:minrep` via full particle-hole symmetry at `mu = 0`; (iii) dilute windows with prefactors `1179504/232925` and `2359008/490429` and bases `29187/262112` and `33795/524224`; (iv) the Mott-edge obstruction at `|mu| = U_eff/2` | 1168-1236 | `MASSIVE/UNIFORM-SSH/RIGOR.md:122-130` (Theorem 1.4), `:220-242` (§4.2), `:278-284` (§5.4); dilute constants at `:78-89` | **PROVED**, constants **CERTIFIED** |
| `prop:nonmonotone` Refutation of monotonicity in repulsive `U_0 >= 0`: the centered two-site dimer intervals at `beta = 2`, `mu = -3`, the uncentered intervals at `beta = 1/2`, `mu = 5`, and the numerical `C_4`, `N = 4` statement | 1237-1290 | `MASSIVE/UNIFORM-SSH/RIGOR.md:131-138` (Theorem 1.5(3)) and `:261-276` (§5.3, Proposition 5.1) | **CERTIFIED** for the dimer enclosures, **NUMERICAL** for the `C_4` statement |
| `thm:routes` (i) no phonon-induced instantaneous atomic gap, `Delta_eff = 0` on `C_4` at `N=4`, with all nine invariant sectors listed | 1298-1350 | `ADIABATIC/PURESSH/RIGOR.md:106-107` (Theorem 1.3(1)); `:476-511` (Proposition 7.1); sector wording after `ADIABATIC/PURESSH/FIX.md` §4 `N3`; kept at `U_eff = 0` per `MASSIVE/UNIFORM-SSH/AMENDMENT.md:561-563`; second review `ADIABATIC/PURESSH/REVIEW2.md:1-14` | **PROVED**, **CERTIFIED** |
| `thm:routes` (ii) non-terminating bond Lang-Firsov expansion (`eq:bondcomm`), with `||[T_b,T_b']||_op = 2` | 1298-1350 | `ADIABATIC/PURESSH/RIGOR.md:108` (Theorem 1.3(2)); `:514-541` (Proposition 7.2); second review `ADIABATIC/PURESSH/REVIEW2.md:1-14` | **PROVED**, **CERTIFIED** |
| `thm:routes` (iii) free-fermion algebraic decay forbids hopping-uniform clustering (`eq:staircase`), with the rational witness at `m=2` | 1298-1350 | `ADIABATIC/PURESSH/RIGOR.md:109-113` (Theorem 1.3(3)); `:544-570` (Proposition 7.3); witness values `:99-107`, `:581`, `ADIABATIC/PURESSH/FIX.md` §4 `N4`; second review `ADIABATIC/PURESSH/REVIEW2.md:1-14` | **PROVED**, **CERTIFIED** |
| Remark after `thm:routes` (what items (i)-(iii) do and do not say, and why `thm:gc` needs the combined condition `beta|t| + beta G_b <= 2^-10`) | 1395-1408 | `ADIABATIC/PURESSH/RIGOR.md:486-493`, `:514-541`, `:544-570`; second review `ADIABATIC/PURESSH/REVIEW2.md:1-14` | **PROVED** |

## 5. Numerical facts quoted in the paper

All of these are labelled as numbers in the text and none carries a proof.

| Fact as printed | `main.tex` lines | Source |
|---|---|---|
| `det(I+U) = 15.790282... > 15` and `|G_{00}| = 52.8957540935... > 52.89` at `B=6`, `v=1/2`; interval-certified, not merely numerical | 752-768 | `MASSIVE/LINEAR-FRESH/RIGOR.md:172-181` |
| `4/(9 pi^4) = 4.5627e-3 > A_GC q_GC^3 = 2.7359e-3` at `m=2`, `d=3` | 1298-1350 | `ADIABATIC/PURESSH/RIGOR.md:99-113`, `:581`; `ADIABATIC/PURESSH/FIX.md` §4 `N4` |
| Static electronic pair admixture `t^2/(4U^2) = 1/64` at `U=4`, `t=1` and `1/68` at the unrelaxed field `q=2U` | 818-845 | `MASSIVE/LINEAR-FRESH/RIGOR.md:303-335` (section 6.2); `MASSIVE/LINEAR-FRESH/REVIEW.md:19` |
| The oscillator action `int[(eps')^2/Omega^2 + eps^2]/(2U)` stays finite for the smoothing of the step profile | 735-750 | `MASSIVE/LINEAR-FRESH/RIGOR.md:166-170` |
| `1/1148 > 1/1200` (a lower bound on `a_left`) and the half constant `1/2400` | 499, 508-550 | `MASSIVE/STATIC-MODE/RIGOR.md:141-157`; `replay.py:exact_constants` |
| Dimer intervals `chi_pair(0) in [1.6180,1.6182]e-4`, `chi_pair(4) in [4.4138,4.4140]e-3`, an increase exceeding a factor `25`; `chi_pair(8) ~ 0.017797`, "over `109.9` times `chi_pair(0)`"; the uncentered pair correlator rising from `[1.2879,1.2881]e-3` to `[5.3243,5.3245]e-3`, a factor above `4.1` | 1237-1290 | `MASSIVE/UNIFORM-SSH/RIGOR.md:261-276`, ratios as corrected in `MASSIVE/UNIFORM-SSH/FIX.md` (`F3`, `F4` per `REVIEW2.md:16-17`); independently reproduced in `MASSIVE/UNIFORM-SSH/REVIEW.md:42-53` |
| `C_4`, `N=4`: `|pair(0,2)|` rising from `0.020827` at `U_0=0` to `0.040148` at `U_0=1` | 1237-1290 | `MASSIVE/UNIFORM-SSH/RIGOR.md:261-276`; labelled **NUMERICAL**, reproduction in `MASSIVE/UNIFORM-SSH/REVIEW.md:42-53` |

## 6. Review notes applied to the paper text

Source-record notes:

- `MASSIVE/STATIC-MODE/REVIEW.md:60-62` P3 note 1 (the symbol `phi` is reused for two
  different quantities): not applicable, the paper does not use `phi`.
- `MASSIVE/STATIC-MODE/REVIEW.md:63-65` P3 note 2 (Schur block wording of the torus
  embedding): applied. The paper says "Schur complement" only of the exact
  Schur complementation used in the proof, and describes the finite barrier as a
  block-diagonal field, not as a Schur block (`main.tex:508-550`).
- `MASSIVE/STATIC-MODE/REVIEW.md:66-69` P3 note 3 (the site coupling `U` versus the
  released linear notes): applied. `main.tex:142-181` defines `U_x = F_x^2/K_x`,
  `F_x X_x = G_x b_x` and `G_x^2 = U_x Omega_x/2`, states that `M_x` and `K_x` enter
  only through `Omega_x` and `U_x`, and states that earlier notes write the site
  coupling as `U = g^2/K` with that lowercase `g` the site force constant, whereas in
  this paper lowercase `g` is the bond force constant of the Peierls model. The
  `U_eff`-uniform section keeps that convention and writes bond masses as `M_b`.
- `MASSIVE/LINEAR-FRESH/REVIEW.md:33` P3 note 3 (equation (4.4) assumes diagonal
  `D_pm`): applied, `main.tex:770-816` states the row sums for diagonal
  `D_pm = diag(D_{pm,m})`.
- `MASSIVE/LINEAR-FRESH/REVIEW.md:35-36` P3 note 4 (the finite-particle core phrasing
  in the unbounded-oscillator justification): applied, the form-boundedness argument
  `D(H^{1/2}) = D(N_osc^{1/2})` replaces the earlier phrasing (`main.tex:618-666`).
- `MASSIVE/LINEAR-FRESH/REVIEW.md:75-82` recommendation (Theorem 2.1 and the dimer
  facts are supporting material): applied. `lem:fsum` is introduced as a classical
  `f`-sum lemma and the Ward and dimer results appear as remarks.
- `ADIABATIC/PURESSH/REVIEW.md:45-51` P1 (the staircase ray, the exponent `d^-2` and
  the `m=2` witness): applied, the paper uses `r_m = (m, m-1)` and `4/(pi^4 d^2)`.
- `ADIABATIC/PURESSH/REVIEW.md:53-58` P1 (source operator normalisation and the proved
  rate bound): applied, `main.tex:861-883` defines `Y_e'(theta)` with
  `||Y_e'(theta)||_op = 1` and no factor `1/2`, and `eq:source` is the `xi`-linear
  bound with the `4 xi^2/xi_0^2` remainder.
- `ADIABATIC/PURESSH/REVIEW.md:60-64` P2 (Proposition 7.1 must list the `N_odd = 2` and
  `S_z != 0` sectors): applied, `thm:routes`(i) lists all nine invariant sectors,
  their dimensions and their maxima, as revised by `ADIABATIC/PURESSH/FIX.md` §4 `N3`.
- `ADIABATIC/PURESSH/REVIEW.md:65-69` P2 (2D BKT quasi-long-range order is not
  off-diagonal long-range order): applied, the paper claims neither.
- `ADIABATIC/PURESSH/REVIEW.md:70-76` P3 (rounding and notation typos): applied, the
  paper prints `R_max = 24718511/9834543 < 3` without a truncated decimal and prints
  the witness values `4.5627e-3` and `2.7359e-3`.
- `MASSIVE/UNIFORM-SSH/REVIEW.md:62-74` findings `F1`-`F6` and `MASSIVE/UNIFORM-SSH/REVIEW2.md:12-27`:
  applied at the level of the source record before transcription: no Shiba
  equivalence, no claim that the Lang-Firsov generator commutes with
  `Delta_x^dagger Delta_y`, `approx 110x` and `> 4.1x` ratios, "concave" for the
  canonical pressure density, "full particle-hole", and the Holstein trace factor at
  the largest time gap (`main.tex:1088-1094` says "concave" and `1237-1290` prints the
  corrected ratios).

Notes from the reviews of this paper (`REVIEW.md`, `REVIEW2.md`), all applied; the
item-by-item list with file and line is in `FIX.md`:

- the Ward-Schur upper bound uses the positive semidefinite `V D_-^{-1} V^*`;
- the proof summary of `thm:canon` follows the source record through the bracket of
  Lemma `lem:canon`, the Legendre discrepancy, and the convexity of the
  source-dependent partition function, and bounds the **derivative** at `xi = 0`;
- the proof summary of `thm:gc` names multilinear Schatten-Hoelder, the exact Gaussian
  Wick integral `int int C_beta = beta/K`, and the Lang-Firsov site factor;
- the `stage6` citation is described as the strong-coupling Holstein ceiling it is;
- `sec:notclaimed` items (a) and (d) state the uniform-`U_eff` scope, the minimum
  ceilings, and the `U_eff = 0` improvement, and the open-problems item names the
  intermediate- and low-temperature regimes.

## 7. Items that are NOT claimed

`main.tex:1409-1446` (`sec:notclaimed`) and the disclosures at `1490-1495` state:

- no bound on a measured transition temperature, no materials claim;
- no claim that `T_pair/Omega` can diverge, and no claim that a linear ceiling is
  false;
- no counterexample inside the interacting model, only obstructions to specified
  proof classes;
- no gain at the linear scale `T_lin = C(t,U) Omega`: the ceilings here are
  frequency-uniform at a temperature scale set by `|t| + G_b` and by the
  strong-coupling rates, and they do not vanish as `Omega -> 0`;
- no interval certification of the finite-matrix and floating-point diagnostics;
- no external data set.

## 8. Open items recorded with this build

- No provisional status remains. `ADIABATIC/PURESSH/REVIEW2.md` (SHA-256
  `25f1115df5b8ce4eb4a246b5a30439ec354d09968cbc8423dd6214fa56926bfe`) resolves
  findings `F1`-`F6` of `ADIABATIC/PURESSH/REVIEW.md`, and `ADIABATIC/PURESSH/FIX.md`
  §4 resolves its notes `N1`-`N4`. Every `U_eff = 0` item in Section 5 (`thm:routes`,
  its remark, and the `PURESSH` inheritance behind `lem:canon` and `thm:gc`) is
  therefore PROVED on twice-reviewed source text.
- The `UNIFORM-SSH` transcription into Section 5 has no independent review of its own;
  the reviewed record is `MASSIVE/UNIFORM-SSH/RIGOR.md` (`REVIEW.md`
  `PASS-WITH-FIXES`, `REVIEW2.md` `PASS`). The delta review of this directory
  (`REVIEW-V2.md`) checked the transcription against that record
  (`PASS-WITH-FIXES`; its findings are closed in `FIX-V2.md`).
- The replay supplement referenced by the data-availability section is a separate
  deposit and is not part of this directory.
