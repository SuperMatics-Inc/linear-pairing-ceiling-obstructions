# Independent Adversarial Review: UNIFORM-SSH

**Date:** 20 November 2026
**Target:** `D:/dev/scratch/ceiling-20261118/MASSIVE/UNIFORM-SSH/` (`SCOPING.md`, `RIGOR.md`, `RESULT.md`, `replay.py`, `CHECKS.txt`)
**Verdict:** **PASS-WITH-FIXES**

All five main theorems in `RIGOR.md` (Theorems 1.1–1.5) are mathematically sound, every finite-dimensional identity, constant, and dimer counterexample in `replay.py` is exact and independently reproduced, and all 8 adversarial mutants fail with exit code 1. There are **no P0 or P1 defects** in `RIGOR.md` or `replay.py`. Two **P2** factual errors appear in `SCOPING.md` (neither is used in `RIGOR.md`'s proofs), alongside several **P3** terminology, rounding, and cross-reference issues across `SCOPING.md`, `RIGOR.md`, and `RESULT.md`.

---

## 1. Per-Claim Audit Table

| Claim / Result | Location | Label | Assessment |
|---|---|---|---|
| **Theorem 1.1** ($U_{\rm eff}$-uniform GC bound, $\beta(|t|+G_b) \le 2^{-10}$, $A_{\rm GC}=341/103$, $q_{\rm GC}=32/341$, $R_{\max} < 3$, analytic source disk) | `RIGOR.md` §1.3, §3.1 | **PROVED** (`CERTIFIED` constants) | Every step of `PURESSH` survives for arbitrary $U_{\rm eff} \in \mathbb{R}, \mu \in \mathbb{R}$ and optional Holstein phonons $g_0 \in \mathbb{R}, \Omega_0 > 0$. Pure-electronic $g=0$ case is **KNOWN** (Ueltschi 1999; `HUBHOL` Cor. 4.5); the frequency-uniform bond-SSH + Holstein + Hubbard combination is new. |
| **Theorem 1.2** ($U_{\rm eff}$-uniform canonical transfer for $n \in (0,2)$ and $k_B T_{\rm pair} \le 1024(|t|+G_b)$) | `RIGOR.md` §1.3, §3.1 | **PROVED** | Original-frame on-site locality of $D_0$ and $H_{\rm Hol}$ preserves the `PURESSH` Lemma 6.1 boundary spring-constant bracket verbatim. (Fix P3 "convex" $\to$ "concave" slip for $f_{\rm can}$.) |
| **Theorem 1.3** (Attractive $U_{\rm eff} < 0$ combined `min` bound) | `RIGOR.md` §1.3, §4.1 | **PROVED** (`CERTIFIED` constants) | Correctly combines Theorems 1.1–1.2 with `SSHBOUND3` Theorems 1.1–1.2 ($U_{\rm eff}^{\rm SSH3} = -U_{\rm eff}$) and `HUBHOL` Lemma 1.3(1) ($0 < e^{-\Phi_\beta[n]} \le 1$). Constants exact. |
| **Theorem 1.4(1)–(2)** (Repulsive $U_{\rm eff} > 0$ Mott window M & half-filling canonical `min` bound) | `RIGOR.md` §1.3, §4.2 | **PROVED** (`CERTIFIED` constants & $C_4$ PH) | Correctly combines `HUBHOL` §§2–3 ($c=5/4$) with `SSHBOUND3` §5.2. Full particle–hole symmetry on even tori fixes $\mu = 0$, $G(0) = U_{\rm eff}/2$. (`SCOPING.md:52` parenthetical Shiba claim is **WRONG**; see F1.) |
| **Theorem 1.4(3)** (Repulsive $U_{\rm eff} > 0$ dilute windows D±, GC at $2^{-26}$, canonical at $2^{-28}$) | `RIGOR.md` §1.3, §4.2 | **PROVED** (`CERTIFIED` constants) | Correctly inherits `HUBHOL` Lemma 3.4(2) ($c=3/2$) + `SSHBOUND3` §5.2; correctly identifies $b_{\rm src} = 2364147/1571530 > 1$ at $L_t=2^{10}$ and raises to $L_t=2^{11}, L_s=2^{12}$ ($b_{\rm src} = 2737395/3585482 < 1$). |
| **Theorem 1.5(1)–(2)** (Hubbard–Stratonovich and reflection-positivity obstructions) | `RIGOR.md` §1.3, §§5.1–5.2 | **PROVED** / **KNOWN** | Standard obstructions correctly diagnosed. |
| **Theorem 1.5(3), Prop. 5.1** (2-site dimer centered & uncentered $U$-monotonicity refutations) | `RIGOR.md` §5.3, `replay.py` | **CERTIFIED** | Independently reproduced via `numpy`/`scipy` ED: centered $\chi(4)/\chi(0) = 27.2785 > 25$, $c_{01}(4)/c_{01}(0) = 28.3098 > 25$; uncentered $c_{01}(4)/c_{01}(0) = 4.1339 > 4$. (Minor P3 prose overstatements `> 110x` and `> 4.2x`; see F3, F4.) |
| **Prop. 5.1(3)** ($C_4$ canonical $N=4$ non-monotonicity) | `RIGOR.md` §5.3 | **NUMERICAL** | Independently reproduced: $\langle \Delta_0^\dagger \Delta_2 \rangle_{N=4} = -0.0208270$ ($U=0$) $\to$ $-0.0401482$ ($U=1$). |
| **Theorem 1.5(4)** (Mott-edge obstruction at $|\mu|=U_{\rm eff}/2$) | `RIGOR.md` §5.4 | **PROVED** (`CERTIFIED` witness) | Correctly inherited from `HUBHOL` Lemma 6.4; $(\cosh 3 - 1)/4 > 2$ certified. |
| **Theorem 1.5(5), Prop. 5.2** (Atomic limit $t=g=0$: $\langle \Delta_x^\dagger \Delta_y\rangle = 0$ for $x \ne y$, $T_{\rm pair}=0$) | `RIGOR.md` §5.5 | **PROVED** (`CERTIFIED` diagonal check) | Local $n_z$ conservation kills all off-diagonal pair correlators identically in both GC and canonical ensembles. |
| **Lang–Firsov commutation with $\Delta_x^\dagger \Delta_y$** | `SCOPING.md:77` | **WRONG** | $S_{\rm LF}$ does **not** commute with $\Delta_x^\dagger \Delta_y$; `RIGOR.md:162` has the correct transformed operator $\Delta_x^\dagger \Delta_y D_x(2\alpha_{\rm LF}) D_y(-2\alpha_{\rm LF})$. (See F2.) |
| **Shiba unitary equivalence to `SSHBOUND3` at $\mu=0$ for pairing** | `SCOPING.md:52` | **WRONG** | Partial PH (Shiba) maps $\Delta_x^\dagger \Delta_y \mapsto (-1)^{x+y} S_x^+ S_y^-$, not $\Delta_x^\dagger \Delta_y$. (See F1.) |

---

## 2. Technical Verification of the Four Review Questions

### 2.1 Survival of `PURESSH`'s Dyson / Schatten–Hölder Argument for $U_{\rm eff} \ne 0$
1. **$N_{\rm odd}$ and commutation with bond terms:** $N_{\rm odd}$ does **not** commute with $T_b$, and does not need to. The noncommutative multilinear Schatten–Hölder bound (`PURESSH` Lemma 4.2 / `SSHBOUND3` Lemma 4.4) holds for arbitrary Hermitian $D_{0,S}$ and arbitrary bounded $A_j$ without commutation. Meanwhile $n_{x,\mathrm{odd}} = n_{x\uparrow}+n_{x\downarrow}-2n_{x\uparrow}n_{x\downarrow}$ is site-local, fermion-even, and commutes with $n_{x\uparrow}, n_{x\downarrow}$, which is all `PURESSH` Lemma 5.1 needs for polymer factorization and $(N_\uparrow, N_\downarrow)$ conservation.
2. **Factorization of $Z_0$:** Because $D_0 = \sum_{x \in \Lambda_L} h_x(U_{\rm eff}, \mu)$ is a sum of commuting site-local Hermitian operators, $Z_{\rm el,0} = z_0(\beta; U_{\rm eff}, \mu)^{|\Lambda_L|}$ with $z_0 = 1 + 2e^{\beta(\mu + U_{\rm eff}/2)} + e^{2\beta\mu} > 0$, and $\operatorname{Tr}_{\mathcal{F}_{\rm el}(S_E)}(e^{-\beta D_{0,S_E}}) = z_0^{|S_E|}$ cancels $Z_0|_{S_E}$ identically for all $U_{\rm eff} \in \mathbb{R}$ and $\mu \in \mathbb{R}$.
3. **Lemma 4.2 and SSH phonon displacement $X_b$:** $X_b$ acts on $\mathcal{H}_{\rm ph,b}$, commuting with $D_0$ and all electronic operators. At fixed Dyson times $0 < u_1 < \dots < u_{K_{\rm tot}} < \beta$, the trace factors into the electronic trace (bounded by Lemma 4.2) times the strictly positive Gaussian bond-phonon Wick product. No commutation between $D_0$ and $X_b$ or $T_b$ is needed.
4. **Lang–Firsov + SSH bond phonons ($g_0 \ne 0$):** $S_{\rm LF} = \frac{g_0}{\Omega_0}\sum_x (n_x - 1)(a_x^\dagger - a_x)$ acts on $\mathcal{F}_{\rm el} \otimes \mathcal{H}_{\rm ph,0}$ and commutes with $(X_b, P_b)$ on $\mathcal{H}_{\rm ph,b}$. It dresses $T_b \mapsto \widetilde{T}_b$ (inside both $V_t$ and $V_g$) and $\Delta_x^\dagger \Delta_y \mapsto \widetilde{\Delta}_x^\dagger \widetilde{\Delta}_y$ with unitary real-argument displacement operators $D_x(\pm\alpha_{\rm LF})$ and $D_x(\pm 2\alpha_{\rm LF})$, leaving $\|\widetilde{T}_b\|_{\rm op} = 2$ and $\|\widetilde{Y}_{e'}(\theta)\|_{\rm op} = 1$. In imaginary time, $[e^{u\Omega_0}a^\dagger - e^{-u\Omega_0}a, e^{v\Omega_0}a^\dagger - e^{-v\Omega_0}a] = 2\sinh((u-v)\Omega_0) \in \mathbb{R}$, so no complex phases arise: the Holstein oscillator trace for every closed Fock trajectory (including $\pm 2$ jumps from $\widetilde{\Delta}_x^\dagger\widetilde{\Delta}_y$ or $\widetilde{Y}_{e'}$) is the strictly positive real factor $e^{-\Phi_\beta[n]} \in (0, 1]$, independent of the bond-SSH Wick trace. Bounding $e^{-\Phi_\beta[n]} \le 1$ and taking occupation-basis moduli ($B_b = |T_b|$, $X_{e'}^{\rm pair} = |Y_{e'}(\theta)|$) preserves the exact Schatten–Hölder bound.
5. **Canonical transfer:** In the untransformed frame, $D_0(U,\mu)$ and $H_{\rm Hol}$ are strictly on-site and conserve $(N_\uparrow, N_\downarrow)$, so zero terms cross block boundaries $\partial$. The `PURESSH` Lemma 6.1 quadratic-form bracket holds verbatim with unchanged $C_{\rm bdry}$.

### 2.2 Inheritance from `SSHBOUND3` and `HUBHOL`
All sign conversions ($U_{\rm eff}^{\rm SSH3} = -U_{\rm eff}$, $U_{\rm eff}^{\rm HH} = -U_{\rm eff}$), window definitions ($G(\mu) = |U_{\rm eff}/2 - |\mu||$), caps ($c=5/4$ for A/M, $c=3/2$ for D±), thresholds ($2^{-26}$ GC in M/D±, $2^{-27}$ at $G=|U_{\rm eff}|/2$, $2^{-28}$ canonical in D±, $2^{-13}$ on $G_b$), and exact rational constants match `SSHBOUND3` and `HUBHOL` verbatim.

### 2.3 Independent Exact-Diagonalization Reproduction
Independent `numpy`/`scipy` exact diagonalization (script in `C:/t/UniformSshReview/verify_ed.py`, deleted after run) reproduced all three counterexamples:
- **Centered 2-site dimer ($t=1, g=0, \beta=2, \mu=-3$):**
  - $U=0$: $\langle\Delta_0^\dagger\Delta_0\rangle = 8.391989\times 10^{-5}$, $\langle\Delta_0^\dagger\Delta_1\rangle = 7.788821\times 10^{-5}$, $\chi_{\rm pair} = 1.618081\times 10^{-4}$.
  - $U=4$: $\langle\Delta_0^\dagger\Delta_0\rangle = 2.208888\times 10^{-3}$, $\langle\Delta_0^\dagger\Delta_1\rangle = 2.204998\times 10^{-3}$, $\chi_{\rm pair} = 4.413886\times 10^{-3}$ ($\chi(4)/\chi(0) = 27.2785$, $c_{01}(4)/c_{01}(0) = 28.3098$).
  - $U=8$: $\chi_{\rm pair} = 1.779685\times 10^{-2}$ ($\chi(8)/\chi(0) = 109.9874$).
- **Uncentered 2-site dimer ($t=1, g=0, \beta=0.5, \mu=5$):**
  - $U=0$: $\langle\Delta_0^\dagger\Delta_1\rangle = 1.287986\times 10^{-3}$.
  - $U=4$: $\langle\Delta_0^\dagger\Delta_1\rangle = 5.324393\times 10^{-3}$ (ratio $4.13389$).
- **Canonical $C_4$ ring ($N=4, t=1, g=0, \beta=5$):**
  - $U=0$: $\langle\Delta_0^\dagger\Delta_2\rangle_{N=4} = -0.0208270286$.
  - $U=1$: $\langle\Delta_0^\dagger\Delta_2\rangle_{N=4} = -0.0401482120$.

### 2.4 Novelty and Impact on Released Barriers II (`BARRIERS2-PAPER/main.tex`)
- **Pure-electronic $U$-uniformity ($g=0$):** **KNOWN / standard.** Keeping arbitrary on-site Hubbard interactions in $H_0$ and running a hopping/cluster expansion for $\beta |t| \le c$ uniformly in $U \in \mathbb{R}$ and $\mu \in \mathbb{R}$ is standard in mathematical physics (e.g., Ueltschi, *J. Stat. Phys.* 95 (1999), 693–717; Ueltschi, *Moscow Math. J.* 4 (2004), 511–522; Fröhlich–Ueltschi, *J. Stat. Phys.* 118 (2005), 973–996; also already proved for Hubbard–Holstein in `HUBHOL` Corollary 4.5).
- **What is new here:** Extending the $U$-uniform hopping expansion to **unbounded quantum bond-SSH (Peierls) oscillators** uniformly in $\Omega_b > 0$ (and simultaneously with onsite Holstein phonons uniformly in $\Omega_0 > 0$), plus the explicit combined `min(...)` ceilings across the full $(U_{\rm eff}, \mu)$ plane with certified rational constants and the explicit dimer non-monotonicity refutation.
- **Impact on `BARRIERS2-PAPER/main.tex`:** The released Barriers II paper is **not wrong in any way**—its Theorems 5.1, 5.3, Lemma 5.2, and Theorem 5.4 are completely correct for the pure bond-SSH model ($U_{\rm eff} = 0$). However, `UNIFORM-SSH` shows that Theorems 5.1 and 5.3 of `BARRIERS2-PAPER` are **narrower than necessary** (they hold verbatim for all $U_{\rm eff} \in \mathbb{R}$ with identical constants), whereas Theorem 5.4(i) and (iii) (no phonon-induced atomic gap; free-fermion algebraic decay) genuinely require $U_{\rm eff} = 0$.

---

## 3. Findings (P0–P3)

- **F1 [P2] — `SCOPING.md:52`:** Parenthetically claims the Mott-window half-filling bound at $\mu = 0$ can be obtained "(or at $\mu = 0$ via Shiba unitary equivalence to `SSHBOUND3`)". **False:** the partial particle–hole (Shiba) transformation $c_{x\downarrow}^\dagger \mapsto (-1)^{x_1+x_2} c_{x\downarrow}$ maps $\Delta_x^\dagger \Delta_y$ to $(-1)^{x_1+x_2+y_1+y_2} S_x^+ S_y^-$, not to $\Delta_x^\dagger \Delta_y$. (`RIGOR.md` §4.2 does not rely on this—it proves Theorem 1.4 directly via `HUBHOL`'s Mott SOS bound.) **Fix:** delete the parenthetical Shiba equivalence claim.
- **F2 [P2] — `SCOPING.md:77`:** States "$S_{\rm LF}$ commutes with $D_0$ and $\Delta_x^\dagger \Delta_y$". **False:** $\Delta_x^\dagger \Delta_y$ changes $n_x$ by $+2$ and $n_y$ by $-2$, so $e^{S_{\rm LF}} \Delta_x^\dagger \Delta_y e^{-S_{\rm LF}} = \Delta_x^\dagger \Delta_y D_x(2\alpha_{\rm LF}) D_y(-2\alpha_{\rm LF}) \ne \Delta_x^\dagger \Delta_y$ (as `RIGOR.md:162` correctly writes). **Fix:** replace with "$S_{\rm LF}$ commutes with $D_0$ and $(X_b, P_b)$, and dresses $\Delta_x^\dagger \Delta_y$ by unitary displacements $D_x(2\alpha_{\rm LF}) D_y(-2\alpha_{\rm LF})$".
- **F3 [P3] — `SCOPING.md:86`, `RIGOR.md:264`:** Both claim $\chi_{\rm pair}(8) > 110\times \chi_{\rm pair}(0)$ on the centered dimer. Exact ED gives $\chi_{\rm pair}(8)/\chi_{\rm pair}(0) = 109.9874 < 110$. **Fix:** change "$> 110\times$" to "$\approx 110\times$ ($> 109.9\times$)".
- **F4 [P3] — `SCOPING.md:86`:** Claims uncentered dimer $|\langle \Delta_0^\dagger \Delta_1\rangle|$ increases "$> 4.2\times$". Exact ED gives $4.13389 < 4.2$ (`RIGOR.md:269` correctly says "$> 4.1\times$"). **Fix:** change "$> 4.2\times$" to "$> 4.1\times$".
- **F5 [P3] — `SCOPING.md:75`, `RIGOR.md:207, 248`:** Call the canonical pressure density $f_{\rm can}(n)$ "convex" while simultaneously invoking block-partition superadditivity. Superadditivity of $\log \widehat{Z}_{\Lambda_L, N}$ yields **concavity** of $f_{\rm can}(n) = \lim L^{-2}\log \widehat{Z}_{\Lambda_L, N}$ (as in `PURESSH` §6.2, `SSHBOUND3` §6.2, and `HUBHOL` Lemma 4.6). **Fix:** change "convex" to "concave" (or define $f_{\rm can}$ with a minus sign as subadditive free energy).
- **F6 [P3] — `RIGOR.md:242`, `RESULT.md:38`:** Label the full particle–hole unitary $U_{\rm ph}$ ($c_{x\sigma}^\dagger \mapsto (-1)^{x_1+x_2} c_{x\sigma}$ for both spins) as "Shiba/particle–hole". In this codebase (`HUBHOL` Remark 2.5), "Shiba" denotes the single-spin flip $P_\downarrow$. **Fix:** call $U_{\rm ph}$ simply the "particle–hole unitary".
- **F7 [P3] — `RIGOR.md:163–164`:** Cites `SSHBOUND3` Lemmas 2.1–2.2 verbatim for trace-norm Dyson convergence when $g_0 \ne 0$, without explicitly noting the additional trace factor $(1 - e^{-\Delta_{j^*}\Omega_0})^{-|\Lambda_L|} = O((N+1)^{|\Lambda_L|})$ from $\mathcal{H}_{\rm ph,0}$ (still polynomial in $N$, dominated by $\Gamma(N/2+1)$). **Fix:** add one sentence noting this polynomial factor.
- **F8 [P3] — `RESULT.md:41`:** Cross-references `RIGOR.md` §5.4 for the attractive $U_{\rm eff} < 0$ atomic-limit discussion; the actual section is `RIGOR.md` §5.5 (§5.4 is the Mott-edge obstruction). **Fix:** change `§5.4` to `§5.5`.

---

## 4. Exercised Commands and Exit Codes

1. Main certification suite:
   ```
   python -B D:/dev/scratch/ceiling-20261118/MASSIVE/UNIFORM-SSH/replay.py
   ```
   Exit code: `0` (all exact rational and outward-rounded interval checks passed).
2. Adversarial mutant suite:
   ```
   python -B D:/dev/scratch/ceiling-20261118/MASSIVE/UNIFORM-SSH/replay.py --all-mutants
   ```
   Exit code: `0` (all 8 mutants rejected with exit code `1`).
3. Independent exact diagonalization verification (`C:/t/UniformSshReview/verify_ed.py`, deleted after run):
   ```
   uv run --no-project --with numpy --with scipy python -B C:/t/UniformSshReview/verify_ed.py
   ```
   Exit code: `0` (all dimer and $C_4$ counterexample values independently confirmed; temp directory `C:/t/UniformSshReview` removed with exit code `0`).
