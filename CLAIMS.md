# Claim-to-source map

Every numbered statement of `paper/main.tex` is traced below to the record that
proves it. Paper line ranges refer to `paper/main.tex` as shipped in this repository
and denote the full extent of the environment that carries the label. Source line
numbers refer to the record files under `records/`, named in each row.

Label taxonomy used in the paper and here: **PROVED** (analytic derivation in the
source record, step by step), **CERTIFIED** (verified by exact rational arithmetic or
outward-rounded interval arithmetic in the record's replay suite), **NUMERICAL**
(floating-point or finite-matrix diagnostics, explicitly not part of any proof),
**KNOWN** (statement of a cited released result), **HEURISTIC** (a synthesis recorded
as a synthesis, carrying no theorem status), **OPEN**.

## Review status of the sources

| Record | Independent review | Status carried into this paper |
|---|---|---|
| `records/static-mode/` | PASS (0 P0/P1/P2, 3 non-blocking P3) | final; the P3 notes are applied |
| `records/linear-fresh/` | PASS (0 P0/P1/P2, 5 non-blocking P3) | final; the P3 notes are applied |
| `records/annealed-static/` | PASS after one fix round (all P1 and P2 resolved; two P3 slips in a HEURISTIC proposition and in an immaterial sign in a Duhamel proof) | final for the transcribed statements |
| `records/puressh/` | PASS after one fix round, then PASS | final; the `U_eff = 0` items are PROVED on twice-reviewed text |
| `records/uniform-ssh/` | PASS-WITH-FIXES, then PASS | final for the transcribed theorems |

The reviews of the source records are part of those records' own history; the review
records of the paper are part of the version 1.0.0 and 1.1.0 history of this
repository and of the version 3 review rounds recorded in `BUILD.md`. Neither is
shipped in this tree.

## 1. Setting and definitions

| Paper item | `paper/main.tex` | Content | Source | Status |
|---|---|---|---|---|
| `def:tpair` | 278-291 | definition of `T_pair` and of the model quantities `C(t,U)` | `records/puressh/RIGOR.md:95-104` | definition, no claim |
| `eq:U`, `eq:dcomm`, `eq:Hhubssh`, `eq:Hssh`, `eq:Gb` | 200-260 | Holstein and bond-SSH Hamiltonians, `U = g^2/K`, `U_eff` for the combined model, `G_b` | `records/static-mode/RIGOR.md:5-19`; `records/puressh/RIGOR.md:13-47`; `records/uniform-ssh/RIGOR.md:15-53` | model |
| `tab:routes` | 309-343 | table of proof routes and their status | this work, synthesis of the records below | survey |

The obstruction sections use `U = g^2/K` exactly as in `records/static-mode/`; the
surviving-regimes section uses `U_eff = U - 2g_0^2/Omega_0` exactly as in
`records/uniform-ssh/` and `records/puressh/`. The paper states both symbols where
they meet, so no letter names two quantities.

## 2. Obstruction one: the integrated first dynamic cumulant

| Paper item | `paper/main.tex` | Content | Source | Status |
|---|---|---|---|---|
| `lem:first` | 385-398 | exact first coefficient `a_x(W)` of `R_W(s)` with the dynamic Gaussian integrated out, `eq:first` | `records/static-mode/RIGOR.md:69-100`, eq. (6) | **PROVED** |
| `lem:aux` | 432-445 | auxiliary bounds: zero-frequency cancellation, resolvent bounds, `|a_x(W)| <= U/4`, the `1/2` factor | `records/static-mode/RIGOR.md:40-64`, `103-121` | **PROVED** |
| `thm:witness` | 484-499 | three-site witness, `eq:witness`, constant `1/1200` for `0 < Omega <= tau <= t/4` | `records/static-mode/RIGOR.md:20-27`, `123-157` | **PROVED**, constants **CERTIFIED** (`1/1148 > 1/1200`) |
| `thm:torus` | 545-557 | square-torus embedding, `eq:torus`, constant `1/2400` for `L >= 4` with a finite barrier | `records/static-mode/RIGOR.md:159-172` | **PROVED**, constants **CERTIFIED** |
| `cor:scale` | 588-600 | at `tau = C Omega`, `C >= 1`: `a >= U/(2400 C^3 Omega)` | `records/static-mode/RIGOR.md:29-36`, eq. (3) | **PROVED** |
| `rem:class` | 609-620 | the obstructed proof class: condition on a static field, expand the Gaussian-integrated dynamic interaction about the positive reference without resumming it, and require a local activity uniform in `Omega`; the third item fails | `records/static-mode/RIGOR.md:40-64` | **PROVED** as a scoped obstruction |
| `rem:notclass` | 622-637 | the class argument establishes no ceiling | `records/static-mode/RIGOR.md:175-189` | **PROVED**, negative scope statement |

## 3. Obstruction two: annealing the static field

| Paper item | `paper/main.tex` | Content | Source | Status |
|---|---|---|---|---|
| `def:defect` | 686-691 | defect set of static fields near the Fermi level | `records/annealed-static/PROOF.md:42-51` | definition |
| `lem:rarity` | 693-703 | defect rarity `P_s(B subset D_kappa) <= exp(-U|B|/(48 tau))` on the square torus for `sqrt(252) Omega <= tau <= U/64`, `kappa <= U/4`, `t <= kappa/64` | `records/annealed-static/PROOF.md:39`; the relaxed form is Theorem 1 of the released limits paper (`10.5281/zenodo.24385569`) | **KNOWN** released theorem, **PROVED** specialization |
| `lem:gapped` | 730-755 | gapped expansion, `eq:gapped`-`eq:quot`, radius `R(tau,kappa)`, `kappa - 4t > 0`, `4t <= kappa/16` | `records/annealed-static/PROOF.md:42-51`, `55-86`, `90-135` | **PROVED**, matrix identities **CERTIFIED** |
| `thm:annealed` | 809-836 | annealed first cumulant `E[a_x(W)] < (25/2) Omega^2/tau^2`, exactly `8348/675` at `kappa = U/4`, `eq:annealed`, `eq:annealed4`, `eq:ray` | `records/annealed-static/PROOF.md:139-169`, eqs. (31)-(33) | **PROVED**, rational constants **CERTIFIED** |
| `rem:nottceil` | 879-892 | the bound is not a ceiling: the corridor is already covered by the frequency-uniform ceiling | this work, arithmetic on `thm:annealed` | **PROVED** arithmetic, remark |
| `thm:rp` | 917-968 | dimer direct reflection kernel is not positive semidefinite, `eq:dimerfail`; the `C_4` particle-hole kernels fail, `eq:c4h`, `eq:c4fail`; the dimer particle-hole control is positive | `records/annealed-static/PROOF.md:178-210`, eqs. (34)-(37); the four minors in `records/annealed-static/replay.py` and `records/annealed-static/independent.py` | **PROVED** computer-assisted for the two failures, **CERTIFIED** finite minors |
| `rem:rpscope` | 1044-1055 | what the reflection-kernel failure does and does not exclude | `records/annealed-static/PROOF.md:189` | **PROVED** scope |
| `rem:contour` | 1064-1095 | uncut and cut separator localization, determinant-zero obstruction, synthesis | `records/annealed-static/PROOF.md:213-233` | **HEURISTIC**, explicitly not a theorem |
| `prop:collapse` | 1100-1108 | gapped corridor: `2^27 t^2/U <= 2^19 t` and `min(2^10 t, 2^27 t^2/U) <= 2^10 t` | `records/annealed-static/PROOF.md:237-250`, eq. (42) | **PROVED** (Part 1) |
| `rem:corridor` | 1115-1131 | the open window sits inside the corridor at `Omega <= U/64` | `records/annealed-static/PROOF.md:237-250` and this work's arithmetic | **HEURISTIC** (Part 2), explicitly a synthesis |

`thm:annealed` is a restriction of Theorem 1c of the annealed record, never an
extension of it:

| Hypothesis | Record Theorem 1c | `thm:annealed` | Relation |
|---|---|---|---|
| geometry | any finite simple graph of maximum degree at most 4 with `|B_R(x)| <= 2R^2 + 2R + 1` | square torus, which satisfies that bound | subset |
| coupling | `0 < g <= U/4` | `0 < kappa <= U/4` | identical |
| hopping | `0 <= t <= g/64` | `0 <= t <= kappa/64` | identical |
| temperature | `0 < Omega <= tau <= U/16` | `sqrt(252) Omega <= tau <= U/64` | subset; the ray window is an added hypothesis |
| buffer radius | `R(tau,g)` as in the record | `R(tau,kappa)` | identical |
| constants | `496/225`, `62/675`, `12`, `248/675`, `8348/675`, `25/2` | the same six | identical |

Adding a hypothesis cannot widen a statement, so every estimate of the section is one
the reviewed theorem already asserts. Nothing in the paper strengthens it: no
temperature scale below `U/64` and no fixed-hopping bound uniform in `Omega` is
asserted anywhere.

## 4. Obstruction three: a positive determinant does not bound the propagator

| Paper item | `paper/main.tex` | Content | Source | Status |
|---|---|---|---|---|
| `lem:fsum` | 1151-1174 | classical oscillator `f`-sum rule `0 <= C_x(i nu_k) <= U_x Omega_x^2/nu_k^2`, `eq:fsum`, `eq:fsum2` | `records/linear-fresh/RIGOR.md:28-88` | **KNOWN**, marked in the text as classical and not a new claim |
| `thm:amp` | 1219-1241 | two-slice histories with strictly positive determinant and arbitrarily large conditional amplification, `eq:amp`, `eq:Gclosed` | `records/linear-fresh/RIGOR.md:97-165`, eqs. (3.1)-(3.2) | **PROVED** |
| `rem:smooth` | 1273-1288 | the family is continuous in the history, so the witness is not a distributional artifact | `records/linear-fresh/RIGOR.md:166-170` | **PROVED** |
| `cor:fixture` | 1290-1304 | `B = 6`, `v = 1/2`: `det(1+U) > 15`, `|G(1,0)_00| > 52.89` | `records/linear-fresh/RIGOR.md:172-181`; `records/linear-fresh/replay.py`, `records/linear-fresh/independent.py` | **CERTIFIED**, flagged in the text as interval facts |
| `rem:ward` | 1308-1354 | finite-matrix Ward-Schur identities, `eq:ward1`-`eq:ward4`, and the enclosure `67/50 < C_aux < 27/20` | `records/linear-fresh/RIGOR.md:183-233`, `257-264` | **PROVED**, enclosure **CERTIFIED** |
| `rem:dimer` | 1356-1383 | exact center-of-mass separation and exact static pair admixture, `eq:com`, `eq:dimermin` | `records/linear-fresh/RIGOR.md:303-335` | **PROVED** |

## 5. What survives

| Paper item | `paper/main.tex` | Content | Source | Status |
|---|---|---|---|---|
| `thm:gc` | 1422-1450 | `U_eff`-uniform grand-canonical bound, `A_GC = 341/103`, `q = 32/341`, `eq:gcb`, `eq:rmax`, `eq:source`, `eq:activity` | `records/uniform-ssh/RIGOR.md:93-103`, constants at `54-89` | **PROVED**, constants **CERTIFIED** |
| `rem:uelschi` | 1529-1539 | in the pure Hubbard limit the `U`-uniform hopping expansion inside the unperturbed semigroup is attributed to Ueltschi and Frohlich-Ueltschi; what the paper adds is unbounded bond-SSH oscillators | `records/uniform-ssh/RIGOR.md:100-102`; the cited external works | **KNOWN** |
| `lem:canon` | 1541-1565 | canonical transfer with unbounded boundary hopping, `eq:bdry` | `records/uniform-ssh/RIGOR.md:104-113`; `records/puressh/RIGOR.md:407-471` for the `U_eff = 0` case | **PROVED** |
| `thm:canon` | 1594-1614 | `k_B T_pair <= 1024(|t| + G_b)` uniformly in `U_eff`, density, chemical potential and frequencies, `eq:canon`, `eq:tpair` | `records/uniform-ssh/RIGOR.md:104-113`; `records/puressh/RIGOR.md:75-116` | **PROVED**, constants **CERTIFIED** |
| `thm:min-att` | 1662-1685 | minimum ceiling for `U_eff < 0`, `eq:minatt` | `records/uniform-ssh/RIGOR.md:114-121` | **PROVED** |
| `thm:min-rep` | 1706-1741 | minimum ceiling for `U_eff > 0` at half filling, `eq:minrep` | `records/uniform-ssh/RIGOR.md:122-130`, `220-243` | **PROVED** |
| `prop:nonmonotone` | 1775-1816 | neither `chi_pair` nor `|langle Delta^dagger Delta rangle|` is monotone non-increasing in repulsive `U_0 >= 0` | `records/uniform-ssh/RIGOR.md:131-139`, `261-277` | **PROVED**, finite minors **CERTIFIED** |
| `thm:routes` | 1836-1888 | three route obstructions at `U_eff = 0`: no instantaneous atomic pairing gap on `C_4`, spectrum `{0,4,4,4,8,12}`; non-terminating bond Lang-Firsov expansion, `eq:bondcomm`; algebraic decay at `g = 0`, `eq:staircase` | `records/puressh/RIGOR.md:474-511`, `512-541`, `542-570` | **PROVED**, spectra and integrals **CERTIFIED** |

`thm:canon` and `thm:min-*` are the `U_eff`-general versions of the released
`U_eff = 0` statements; the paper states the general form only.

## 6. Non-claims and open problems

| Paper item | `paper/main.tex` | Content | Status |
|---|---|---|---|
| `sec:notclaimed` | 1946-1985 | explicit list of what is not claimed: no measured transition temperature, no materials statement, no linear-in-`Omega` ceiling, no claim that the Gaussian histories are the dominant ones, and no claim that the annealed bound is a ceiling | scope |
| `sec:open` | 1986-2029 | open problems: where the corridor stops, the repulsive `t^2/U_eff` window, the linear step, and the reflection and infrared arguments | **OPEN** |

## 7. Numerical and certified numbers

Every number that is a numerical fact rather than a proved inequality is flagged in
the sentence that states it.

| Number | Where | Method | Source |
|---|---|---|---|
| `1/1200`, `1/2400`, `1/1148` | `thm:witness`, `thm:torus` | exact rational arithmetic, with `pi < 22/7`, `(22/7)^2 < 10`, `tanh 1 > 3/4` | `records/static-mode/replay.py` |
| `8348/675`, `248/675`, `62/675`, `496/225`, `12`, `25/2` | `thm:annealed`, `rem:nottceil` | exact rational arithmetic | `records/annealed-static/replay.py`, `records/annealed-static/independent.py` |
| four reflection minors | `thm:rp` | 128-bit outward-rounded ball arithmetic for the `2 x 2` dimer minor, the `3 x 3` dimer particle-hole minor and the `3 x 3` principal minor of the four-by-four ring kernel, plus an independent 80-digit diagonalization summed over the 16 occupation states | `records/annealed-static/replay.py`, `records/annealed-static/independent.py` |
| `det(1+U) > 15`, `|G(1,0)_00| > 52.89` at `B = 6`, `v = 1/2` | `cor:fixture` | outward-rounded interval arithmetic in `arb` (80 digits) and independently in `mpmath.iv` (60 digits) | `records/linear-fresh/replay.py`, `records/linear-fresh/independent.py` |
| `341/103`, `32/341`, `1024`, `2^27`, `2^13`, `2^10` | Section 6 | exact rational arithmetic | `records/uniform-ssh/replay.py` |
| `2^19`, `2^10`, `2^27` corridor constants | `prop:collapse` | exact integer arithmetic | `records/annealed-static/replay.py` |

## 8. Statements deliberately not made

- No upper bound on `T_pair` that is linear in `Omega` is derived or claimed.
- `rem:contour` and `rem:corridor` are labelled HEURISTIC in the text and carry no
  theorem status; the source record labels the same two statements the same way.
- `thm:annealed` is a first-cumulant bound, not a pairing ceiling: it concerns
  `a_x(W)` and the static-field average of `a_x(W)`, not the pair correlator.
- No statement is made about a measured transition temperature, about a material, or
  about any experimental data.
- The `f`-sum bound appears only as the classical lemma `lem:fsum`; it is not
  presented as a new claim of this paper.
