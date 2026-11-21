# UNIFORM-SSH Result Summary

**Date:** 20 November 2026
**Directory:** `D:/dev/scratch/ceiling-20261118/MASSIVE/UNIFORM-SSH/`
**Status:** **`proof draft`** (analytical proofs and counterexamples complete in `RIGOR.md`; independent review pending).

---

## 1. Main Scientific Answers

1. **Universal $U$-uniform ceiling (`proof draft`, Theorems 1.1 & 1.2):**
   In the full spinful Hubbard–Holstein–bond-SSH model on 2D square tori $\Lambda_L = (\mathbb{Z}/L\mathbb{Z})^2$ ($L \ge 4$) with arbitrary onsite Hubbard interaction $U \in \mathbb{R}$ ($U \ge 0$ included), Holstein coupling $g_0 \in \mathbb{R}$, $\Omega_0 > 0$, bond-SSH coupling $g \in \mathbb{R}$, $K > 0$, $\Omega > 0$, and effective interaction $U_{\rm eff} := U - 2g_0^2/\Omega_0 \in \mathbb{R}$:
   - **Grand canonical (Theorem 1.1):** Whenever $\beta(|t| + G_b) \le 2^{-10}$ ($G_b := g^2/K$), uniformly in $U_{\rm eff} \in \mathbb{R}$, $\mu \in \mathbb{R}$, $\Omega > 0$, $\Omega_0 > 0$, and $L \ge 4$,
     \[
     |\langle \Delta_x^\dagger \Delta_y \rangle_{\rm GC}| \le \frac{341}{103}\left(\frac{32}{341}\right)^{d_{\Lambda_L}(x,y)} \quad (x \ne y), \qquad \sup_{x \in \Lambda_L} \sum_{y \in \Lambda_L} |\langle \Delta_x^\dagger \Delta_y \rangle_{\rm GC}| \le \frac{24718511}{9834543} < 3.
     \]
     Hence
     \[
     k_B T_{\rm pair} \le 1024\,(|t| + G_b)
     \]
     holds **uniformly across all $U_{\rm eff} \in \mathbb{R}$** (repulsive $U_{\rm eff} > 0$, pure SSH $U_{\rm eff} = 0$, and attractive $U_{\rm eff} < 0$), with **no** $|U_{\rm eff}|_-$ term needed.
   - **Canonical (Theorem 1.2):** For every target density $n \in (0, 2)$, $k_B T_{\rm pair}^{\rm can}(n) \le 1024\,(|t| + G_b)$ uniformly in $U_{\rm eff} \in \mathbb{R}$, $\Omega > 0$, $\Omega_0 > 0$.

2. **Exact mechanism — why `PURESSH` Theorem 1.1 generalizes verbatim to all $U_{\rm eff} \in \mathbb{R}$ (`RIGOR.md` §3):**
   `PURESSH` Theorem 1.1 never used $U_{\rm eff} = 0$ in its analytic expansion; it only needed $D_0 = -\frac{U_{\rm eff}}{2} N_{\rm odd} - \mu N$ to be diagonal in the Fock occupation basis so that $e^{-\delta D_{0,E}} > 0$ entrywise and Lemma 4.2 (multilinear Schatten–Hölder for Hermitian semigroups) cancels $\operatorname{Tr}(e^{-\beta D_{0,E}}) = z_a^{|S_E|}$ identically against $Z_0$. When $g_0 \ne 0$, the Lang–Firsov unitary transformation isolates the Holstein oscillators into a multiplicative trajectory weight $0 < e^{-\Phi_\beta[n]} \le 1$ (`HUBHOL` Lemma 1.3(1)) while shifting $U \mapsto U_{\rm eff}$.

3. **Combined `min` ceilings with `SSHBOUND3` / `HUBHOL` (`proof draft`, Theorems 1.3 & 1.4):**
   - **Attractive ($U_{\rm eff} < 0$, Theorem 1.3):** Combining Theorems 1.1–1.2 with `SSHBOUND3` (extended by the Lang–Firsov factor $e^{-\Phi_\beta[n]} \le 1$ when $g_0 \ne 0$) yields, uniformly in $\mu \in \mathbb{R}$, $\Omega, \Omega_0 > 0$, and at every canonical density $n \in (0, 2)$,
     \[
     k_B T_{\rm pair} \le \min\!\left\{1024\,(|t| + G_b),\;\max\!\left(2^{27}\frac{t^2}{|U_{\rm eff}|},\; 2^{13} G_b\right)\right\}.
     \]
   - **Repulsive gapped windows ($U_{\rm eff} > 0$, Theorem 1.4):** Inside the Mott window $\mathrm{M}$ ($|\mu| < U_{\rm eff}/2$, $G = U_{\rm eff}/2 - |\mu|$, $c = 5/4$, $L_t = 2^{10}, L_s = 2^{11}$) and dilute windows $\mathrm{D}\pm$ ($|\mu| > U_{\rm eff}/2$, $G = |\mu| - U_{\rm eff}/2$, $c = 3/2$, $L_t = 2^{11}, L_s = 2^{12}$), grand-canonical exponential clustering holds with explicit constants whenever $\beta t^2/G \le 2^{-26}$ (in $\mathrm{M}$) or $\le 2^{-28}$ (in $\mathrm{D}\pm$) and $\beta G_b \le 2^{-13}$. At canonical half-filling $n = 1$ (where full particle–hole symmetry fixes $\mu = 0$ and $G(0) = U_{\rm eff}/2$),
     \[
     k_B T_{\rm pair}^{\rm can}(1) \le \min\!\left\{1024\,(|t| + G_b),\;\max\!\left(2^{27}\frac{t^2}{U_{\rm eff}},\; 2^{13} G_b\right)\right\}.
     \]
     At the Mott edges $|\mu| = U_{\rm eff}/2$, the site-gap SOS route is obstructed (`HUBHOL` Lemma 6.4), leaving only the universal $1024(|t|+G_b)$ bound (or direct $\beta|t|$ expansion).

4. **Attractive regime $U_{\rm eff} < 0$ does not blow up (`RIGOR.md` §5.5):**
   The question asked whether $U_{\rm eff} < 0$ is unbounded in $T_{\rm pair} \sim |U_{\rm eff}|$. By Definition 1.1, $T_{\rm pair}$ measures *spatial decay* of $|\langle \Delta_x^\dagger \Delta_y\rangle_{\Lambda_L}|$ ($x \ne y$), not the on-site density of preformed pairs $\langle \Delta_x^\dagger \Delta_x\rangle \le 1$. In the atomic limit ($t = g = 0$), $\langle \Delta_x^\dagger \Delta_y\rangle = 0$ identically for all $x \ne y$ ($T_{\rm pair} = 0$), and for $t, g \ne 0$, Theorems 1.1–1.3 give both $k_B T_{\rm pair} \le 1024(|t| + G_b)$ and $k_B T_{\rm pair} \le \max(2^{27} t^2/|U_{\rm eff}|, 2^{13} G_b)$ uniformly in $U_{\rm eff} < 0$. Thus no $|U_{\rm eff}|_-$ term is required.

5. **Obstructions to alternative $U > 0$ routes (`RIGOR.md` §§5.1–5.3):**
   - **Sign-definite Hubbard–Stratonovich:** Fails for $U > 0$ (charge channel $+\frac{U}{2}(n_x-1)^2$ gives imaginary $i\phi_x$ phases; spin channel $-\frac{U}{2}(n_{x\uparrow}-n_{x\downarrow})^2$ gives opposite signs $\pm \phi_x$ for $\uparrow,\downarrow$ while $\Delta_x^\dagger = c_{x\uparrow}^\dagger c_{x\downarrow}^\dagger$ creates opposite-spin pairs).
   - **Reflection positivity:** Requires $\mu = 0$ and even bipartite tori, and does not produce uniform high-$T$ exponential clustering in graph distance.
   - **Monotonicity of $\chi_{\rm pair}$ or $|\langle \Delta_x^\dagger \Delta_y\rangle|$ in $U \ge 0$:** **False (`CERTIFIED` counterexamples in `replay.py`):**
     - Centered 2-site dimer ($\beta = 2, \mu = -3, t = 1, g = 0$): $\chi_{\rm pair}(4) > 25\,\chi_{\rm pair}(0)$ and $|\langle \Delta_0^\dagger \Delta_1\rangle|(4) > 25\,|\langle \Delta_0^\dagger \Delta_1\rangle|(0)$ (`CERTIFIED`).
     - Uncentered 2-site dimer ($\beta = 1/2, \mu = 5, t = 1, g = 0$): $|\langle \Delta_0^\dagger \Delta_1\rangle|(4) > 4\,|\langle \Delta_0^\dagger \Delta_1\rangle|(0)$ (`CERTIFIED`).
     - Canonical $C_4$ ring ($N = 4, t = 1, g = 0, \beta = 5$): $|\langle \Delta_0^\dagger \Delta_2\rangle|$ increases from $0.020827$ ($U=0$) to $0.040148$ ($U=1$) (`NUMERICAL`).

---

## 2. Verification Summary

- `python -B D:/dev/scratch/ceiling-20261118/MASSIVE/UNIFORM-SSH/replay.py` → exit `0` (`CERTIFIED` exact rational and outward-rounded rational-interval checks).
- `python -B D:/dev/scratch/ceiling-20261118/MASSIVE/UNIFORM-SSH/replay.py --all-mutants` → exit `0` (all 8 mathematical mutants rejected with exit `1`).

---

## 3. Files in `UNIFORM-SSH/`

- `SCOPING.md`: target theorem, sign-convention reconciliation, proof route, and failure points.
- `RIGOR.md`: complete `proof draft` of Theorems 1.1–1.5, obstructions, and counterexamples.
- `RESULT.md`: this summary.
- `replay.py`: pure-Python stdlib exact rational + outward-rounded interval certification and 8-mutant falsification suite.
- `CHECKS.txt`: verbatim check receipts, skipped checks, and file inventory.
