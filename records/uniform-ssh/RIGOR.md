# UNIFORM-SSH: $U$-Uniform and Combined Pairing Ceilings, Route Obstructions, and Counterexamples for the Hubbard–SSH Model

**Date:** 20 November 2026
**Status:** **`proof draft`** (complete analytical proofs and counterexample proofs given below; independent review pending).
**Labels:**
- **`proof draft`**: complete step-by-step analytical proof in this document awaiting independent review.
- **`CERTIFIED`**: exact rational (`fractions.Fraction`) or outward-rounded rational-interval calculation verified by `UNIFORM-SSH/replay.py`.
- **`NUMERICAL`**: floating-point exact diagonalization check (diagnostic only; never cited as proof).
- **`[INFERENCE]`** / **`OPEN`**: explicitly labeled where applicable.

---

## 1. Model, Conventions, and Main Results

### 1.1 Hamiltonian and Hilbert Space

Let $\Lambda_L = (\mathbb{Z}/L\mathbb{Z})^2$ be a finite 2D square torus of side $L \ge 4$, with $|\Lambda_L| = L^2$ vertices, undirected nearest-neighbor physical bond set $\mathcal{E}_{\Lambda_L}$ of size $|\mathcal{E}_{\Lambda_L}| = 2L^2$, and uniform vertex degree $D = 4$. In units $\hbar = k_B = 1$, consider the spinful **Hubbard + bond-SSH (+ optional onsite Holstein)** Hamiltonian on
\[
\mathcal{H}_{\Lambda_L} := \mathcal{F}_{\rm el}(\Lambda_L) \otimes \mathcal{H}_{\rm ph,b} \otimes \mathcal{H}_{\rm ph,0}, \qquad \mathcal{H}_{\rm ph,b} := \bigotimes_{b \in \mathcal{E}_{\Lambda_L}} L^2(\mathbb{R}, dX_b), \qquad \mathcal{H}_{\rm ph,0} := \bigotimes_{x \in \Lambda_L} L^2(\mathbb{R}, dq_x),
\]
given (for source parameter $\xi \in \mathbb{R}$, phase $\theta \in \mathbb{R}$, and target displacement $r \in \Lambda_L \setminus \{0\}$) by
\[
H_{\Lambda_L}(\xi) := U \sum_{x \in \Lambda_L} \left(n_{x\uparrow} - \frac{1}{2}\right)\left(n_{x\downarrow} - \frac{1}{2}\right) - \mu N - \sum_{b \in \mathcal{E}_{\Lambda_L}} (t - g X_b) T_b + \sum_{b \in \mathcal{E}_{\Lambda_L}} \left(\frac{P_b^2}{2M_b} + \frac{K}{2} X_b^2\right) + H_{\rm Hol} + V_{\rm src}(\xi),
\]
where:
- $T_b := \sum_{\sigma \in \{\uparrow, \downarrow\}} (c_{x\sigma}^\dagger c_{y\sigma} + c_{y\sigma}^\dagger c_{x\sigma})$ for $b = \{x, y\} \in \mathcal{E}_{\Lambda_L}$, $N := \sum_{x \in \Lambda_L} (n_{x\uparrow} + n_{x\downarrow})$, $N_{\rm odd} := \sum_{x \in \Lambda_L} \mathbf{1}[n_x = 1]$, $G_b := g^2 / K \ge 0$, and $\Omega_b := \sqrt{K / M_b} > 0$;
- $H_{\rm Hol} := \sum_{x \in \Lambda_L} \bigl(\Omega_0 a_x^\dagger a_x + g_0 (n_x - 1)(a_x + a_x^\dagger)\bigr)$ with $\Omega_0 > 0$, $g_0 \in \mathbb{R}$, and $U_{\rm Hol} := 2g_0^2/\Omega_0 \ge 0$ (when $g_0 = 0$, $H_{\rm Hol}$ decouples trivially and $\mathcal{H}_{\rm ph,0}$ cancels in all ratios);
- $V_{\rm src}(\xi) := -\xi \sum_{e' \in \mathcal{E}_{\rm src}} Y_{e'}(\theta)$, where $\mathcal{E}_{\rm src} := \{\{x, x+r\} : x \in \Lambda_L\}$ (each site incident to at most $2$ source edges, so augmented graph degree $D_{\rm aug} = 4 + 2 = 6$) and $Y_{e'}(\theta) := e^{i\theta} \Delta_x^\dagger \Delta_y + e^{-i\theta} \Delta_y^\dagger \Delta_x$, with $\Delta_x := c_{x\downarrow} c_{x\uparrow}$.

Define the effective onsite interaction
\[
U_{\rm eff} := U - U_{\rm Hol} \in \mathbb{R}.
\]
Using $(n_{x\uparrow} - \tfrac{1}{2})(n_{x\downarrow} - \tfrac{1}{2}) = \tfrac{1}{4} - \tfrac{1}{2} \mathbf{1}[n_x = 1]$ and $(n_x - 1)^2 = 1 - \mathbf{1}[n_x = 1]$, the onsite electronic reference after Lang–Firsov transformation (Section 2.2) is, up to the global scalar shift $\bigl(\frac{U}{4} - \frac{U_{\rm Hol}}{2}\bigr)|\Lambda_L|$ that cancels identically in all Gibbs expectations,
\[
D_0(U_{\rm eff}, \mu) := -\frac{U_{\rm eff}}{2} N_{\rm odd} - \mu N = \sum_{x \in \Lambda_L} h_x(U_{\rm eff}, \mu), \qquad h_x(U_{\rm eff}, \mu) := -\frac{U_{\rm eff}}{2} n_{x,\mathrm{odd}} - \mu n_x.
\]

**Sign conventions across program files (`CERTIFIED` algebraic identities):**
- **Here (`UNIFORM-SSH`) and `BARRIERS2-PAPER`:** $U_{\rm eff} > 0$ is **repulsive**, $U_{\rm eff} < 0$ is **attractive**.
- **`SSHBOUND3`:** $U_{\rm eff}^{\rm SSH3} = -U_{\rm eff} > 0$ is attractive ($D_0^{\rm SSH3} = +\frac{U_{\rm eff}^{\rm SSH3}}{2} N_{\rm odd} - \mu N$).
- **`HUBHOL`:** $U_{\rm eff}^{\rm HH} = U_{\rm Hol} - U_c = -U_{\rm eff}$ ($> 0$ attractive, $< 0$ repulsive).
- **Uncentered Hubbard term:** $U n_{x\uparrow} n_{x\downarrow} - \mu_{\rm unc} n_x = U(n_{x\uparrow}-\tfrac{1}{2})(n_{x\downarrow}-\tfrac{1}{2}) - (\mu_{\rm unc} - \tfrac{U}{2}) n_x - \tfrac{U}{4}$, so passing to uncentered chemical potential is a pure shift $\mu = \mu_{\rm unc} - U/2$ plus a global constant $-\tfrac{U}{4}|\Lambda_L|$ that cancels in every Gibbs ratio. Every $\mu$-uniform statement over $\mu \in \mathbb{R}$ is identical in both conventions.

**Definition 1.1 (Pair-decay temperature $T_{\rm pair}$, `BARRIERS2-PAPER` Definition 2.1).**
Fix $(t, g, K, M_b, U, g_0, \Omega_0)$. Let $\mathcal{Q}$ be the set of temperatures $T > 0$ for which there exist constants $A < \infty$ and $q < 1$, independent of $L \ge 4$ and of $\mu \in \mathbb{R}$, such that
\[
\left|\langle \Delta_x^\dagger \Delta_y \rangle_{\Lambda_L}\right| \le A \, q^{d_{\Lambda_L}(x,y)}
\]
holds in the grand-canonical state at $\beta = 1/T$ for every $L \ge 4$, every $\mu \in \mathbb{R}$, and all distinct $x, y \in \Lambda_L$. Set $T_{\rm pair} := \inf \mathcal{Q}$. For a fixed canonical density $n \in (0, 2)$, $T_{\rm pair}^{\rm can}(n)$ denotes the analogous threshold for $\limsup_{L \to \infty} |\langle \Delta_0^\dagger \Delta_r \rangle_{\Lambda_L, N_L}| \le A q^{d(0,r)}$ along sequences $N_L/L^2 \to n$.

---

### 1.2 Explicit Constants (`CERTIFIED` in `replay.py`)

1. **Universal `PURESSH` constants (Theorem 1.1 & 1.2):**
   \[
   c_0 := 2^{-10} = \frac{1}{1024}, \qquad \xi_0 := \frac{2^{-9}}{\beta}, \qquad \varepsilon_{\rm phys} = \varepsilon_{\rm src} := \frac{2c_0}{1 - c_0} = \frac{2}{1023},
   \]
   \[
   q_{\rm GC} := 48\varepsilon_{\rm phys} = \frac{32}{341}, \qquad A_{\rm GC} := \frac{3}{1 - q_{\rm GC}} = \frac{341}{103}, \qquad b_{\rm GC} := \frac{3 q_{\rm GC}}{1 - q_{\rm GC}} = \frac{32}{103} < 1,
   \]
   \[
   R_{\rm max} := 1 + \frac{4 A_{\rm GC} q_{\rm GC}}{(1 - q_{\rm GC})^2} = \frac{24718511}{9834543} < 3, \qquad q_{\rm src} := \frac{72}{341}, \qquad b_{\rm src} := \frac{216}{269} < 1.
   \]

2. **Strong-coupling `SSHBOUND3` / Mott constants (Theorems 1.3 & 1.4, $c = 5/4$):**
   \[
   L_t = 2^{10}, \qquad L_s = 2^{11}, \qquad c_1 = 2^{-26}\text{ (gap }G\text{)},\qquad c_2 = 2^{-13}\text{ (on }G_b\text{)}, \qquad \xi_0^{(5/4)} = \frac{2^{-14}}{\beta},
   \]
   \[
   \varepsilon_{\rm phys}^{(5/4)} = \frac{3243}{2096896}, \qquad \varepsilon_{\rm src}^{(5/4)} = \frac{1}{1536}, \qquad q_{\rm GC}^{(5/4)} = \frac{48645}{524224}, \qquad A_{\rm GC}^{(5/4)} = \frac{1965840}{475579},
   \]
   \[
   b_{\rm GC}^{(5/4)} = \frac{729675}{1902316} < 1, \qquad q_{\rm src}^{(5/4)} = \frac{437805}{2096896}, \qquad b_{\rm src}^{(5/4)} = \frac{6567075}{6636364} < 1, \qquad R_{\rm max}^{(5/4)} = \frac{308086835615302339}{107564263537529539} < 3.
   \]

3. **Dilute-window constants (Theorem 1.4, $c = 3/2$):**
   - **Grand-canonical only ($L_t = 2^{10}, c_1 = 2^{-26}, c_2 = 2^{-13}$):**
     $q_{\rm GC}^{(3/2,\mathrm{GC})} = \frac{29187}{262112}$, $A_{\rm GC}^{(3/2,\mathrm{GC})} = \frac{1179504}{232925}$, $b_{\rm GC}^{(3/2,\mathrm{GC})} = \frac{262683}{465850} < 1$, $R_{\rm max}^{(3/2,\mathrm{GC})} = \frac{48731188880452229}{12637125906453125} < 3.86$. (Source budget at $L_t=2^{10}, L_s=2^{11}$ is $\frac{2364147}{1571530} > 1$, so canonical transfer raises $L_t, L_s$.)
   - **With canonical transfer ($L_t = 2^{11}, L_s = 2^{12}, c_1 = 2^{-28}, c_2 = 2^{-13}, \xi_0^{(3/2)} = 2^{-15}/\beta$):**
     \[
     \varepsilon_{\rm phys}^{(3/2)} = \frac{3755}{4193792}, \qquad \varepsilon_{\rm src}^{(3/2)} = \frac{1}{3072}, \qquad q_{\rm GC}^{(3/2)} = \frac{33795}{524224}, \qquad A_{\rm GC}^{(3/2)} = \frac{2359008}{490429},
     \]
     \[
     b_{\rm GC}^{(3/2)} = \frac{304155}{980858} < 1, \qquad q_{\rm src}^{(3/2)} = \frac{304155}{2096896}, \qquad b_{\rm src}^{(3/2)} = \frac{2737395}{3585482} < 1, \qquad R_{\rm max}^{(3/2)} = \frac{285128438390906149}{117958279319223589} < 2.42.
     \]

---

### 1.3 Main Theorems

**Theorem 1.1 (Universal $U_{\rm eff}$-uniform grand-canonical bound, `proof draft`).**
*For every $U_{\rm eff} \in \mathbb{R}$ (every $U \ge 0$ and every $U_{\rm Hol} \ge 0$), every $t, g, \mu \in \mathbb{R}$, every $K > 0$, every $\Omega_b > 0$, every $\Omega_0 > 0$, every torus side $L \ge 4$, and every $\beta > 0$ satisfying*
\[
\beta\left(|t| + G_b\right) \le 2^{-10} \qquad \Longleftrightarrow \qquad k_B T \ge 1024\left(|t| + G_b\right),
\]
*the grand-canonical pair correlator satisfies, for all distinct $x, y \in \Lambda_L$,*
\[
\left|\langle \Delta_x^\dagger \Delta_y \rangle_{\Lambda_L}\right| \le A_{\rm GC}\, q_{\rm GC}^{d_{\Lambda_L}(x,y)} = \frac{341}{103}\left(\frac{32}{341}\right)^{d_{\Lambda_L}(x,y)}, \qquad \sup_{x \in \Lambda_L}\sum_{y \in \Lambda_L}\left|\langle \Delta_x^\dagger \Delta_y \rangle_{\Lambda_L}\right| \le R_{\rm max} = \frac{24718511}{9834543} < 3,
\]
*and the source-augmented log-partition function $p_{\Lambda_L}(\xi) := |\Lambda_L|^{-1} \log Z_{\Lambda_L}(\xi)$ extends analytically to $\{|\xi| < \xi_0\}$ with $p_{\Lambda_L}(\xi) - p_{\Lambda_L}(0) \le 2\beta A_{\rm GC} q_{\rm GC}^{d_{\Lambda_L}(0,r)}\xi + 4\xi^2/\xi_0^2$ for $\xi \in [0, \xi_0/2]$.*

**Theorem 1.2 (Universal $U_{\rm eff}$-uniform canonical transfer and $T_{\rm pair}$ ceiling, `proof draft`).**
*Under the same condition $\beta(|t| + G_b) \le 2^{-10}$, for every $U_{\rm eff} \in \mathbb{R}$, every nonzero $r \in \mathbb{Z}^2 \setminus \{0\}$, and every translation-invariant thermodynamic canonical limit with $N_L/L^2 \to n \in (0, 2)$ (or spin-balanced $N_{L,\uparrow}/L^2 = N_{L,\downarrow}/L^2 \to a \in (0, 1)$),*
\[
\limsup_{L \to \infty} \left|\langle \Delta_0^\dagger \Delta_r \rangle_{\Lambda_L, N_L}\right| \le \frac{341}{103}\left(\frac{32}{341}\right)^{d(0,r)}.
\]
*Consequently, uniformly in $U \ge 0$, $U_{\rm eff} \in \mathbb{R}$, $\Omega_b > 0$, $\Omega_0 > 0$, and $n \in (0,2)$,*
\[
k_B T_{\rm pair} \le 1024\left(|t| + G_b\right) \qquad \text{and} \qquad k_B T_{\rm pair}^{\rm can}(n) \le 1024\left(|t| + G_b\right).
\]

**Theorem 1.3 (Combined `min` bound in the attractive regime $U_{\rm eff} < 0$, `proof draft`).**
*Assume $U_{\rm eff} < 0$, $\beta > 0$, $t, g, \mu \in \mathbb{R}$, $K > 0$, $\Omega_b > 0$, $\Omega_0 > 0$.*
1. *If $\beta t^2 / |U_{\rm eff}| \le 2^{-27}$ and $\beta G_b \le 2^{-13}$, then the `SSHBOUND3` bounds $|\langle \Delta_x^\dagger \Delta_y \rangle_{\Lambda_L}| \le A_{\rm GC}^{(5/4)} (q_{\rm GC}^{(5/4)})^{d_{\Lambda_L}(x,y)}$ hold uniformly in $\mu, \Omega_b, \Omega_0, L \ge 4$ and transfer to every canonical density $n \in (0,2)$.*
2. *Combining with Theorems 1.1–1.2 yields, uniformly in $\mu \in \mathbb{R}$, $n \in (0, 2)$, $\Omega_b > 0$, and $\Omega_0 > 0$,*
   \[
   k_B T_{\rm pair} \le \min\!\left(1024(|t| + G_b),\; \max\!\left(2^{27}\frac{t^2}{|U_{\rm eff}|},\; 2^{13} G_b\right)\right) \qquad (\forall\, U_{\rm eff} < 0).
   \]

**Theorem 1.4 (Repulsive Mott/dilute windows and combined half-filling bound for $U_{\rm eff} > 0$, `proof draft`).**
*Assume $U_{\rm eff} > 0$ and define the atomic charge gap $G(\mu) := \bigl|\frac{U_{\rm eff}}{2} - |\mu|\bigr|$.*
1. **Mott window M ($|\mu| < U_{\rm eff}/2$, $G = U_{\rm eff}/2 - |\mu| > 0$):** *If $\beta t^2 / G(\mu) \le 2^{-26}$ and $\beta G_b \le 2^{-13}$, then $|\langle \Delta_x^\dagger \Delta_y \rangle_{\Lambda_L}| \le A_{\rm GC}^{(5/4)} (q_{\rm GC}^{(5/4)})^{d_{\Lambda_L}(x,y)}$ uniformly in $\Omega_b, \Omega_0, L \ge 4$, with analytic source disk $|\xi| \le 2^{-14}/\beta$ and $b_{\rm src}^{(5/4)} < 1$.*
2. **Half-filling canonical `min` bound ($n = 1$, even $L \ge 4$):** *By particle–hole symmetry on even tori, $\mu = 0$ (where $G(0) = U_{\rm eff}/2$) supports $n = 1$ at every $T > 0$; hence*
   \[
   k_B T_{\rm pair}^{\rm can}(n=1) \le \min\!\left(1024(|t| + G_b),\; \max\!\left(2^{27}\frac{t^2}{U_{\rm eff}},\; 2^{13} G_b\right)\right) \qquad (\forall\, U_{\rm eff} > 0).
   \]
3. **Dilute windows D± ($|\mu| > U_{\rm eff}/2$, $G = |\mu| - U_{\rm eff}/2 > 0$):** *If $\beta t^2 / G(\mu) \le 2^{-26}$ and $\beta G_b \le 2^{-13}$, then $|\langle \Delta_x^\dagger \Delta_y \rangle_{\Lambda_L}| \le A_{\rm GC}^{(3/2,\mathrm{GC})} (q_{\rm GC}^{(3/2,\mathrm{GC})})^{d_{\Lambda_L}(x,y)}$. If $\beta t^2/G(\mu) \le 2^{-28}$ and $\beta G_b \le 2^{-13}$, then the bound holds with $(A_{\rm GC}^{(3/2)}, q_{\rm GC}^{(3/2)})$ and transfers to canonical densities whose supporting $\mu(n)$ satisfies the hypothesis.*

**Theorem 1.5 (Refuted routes, obstructions, and no-go for $|U_{\rm eff}|_-$, `proof draft`).**
1. **Hubbard–Stratonovich sign-definite obstruction (§5.1):** *For $U > 0$, neither charge HS nor spin HS furnishes a sign-definite field free of the sign problem at general $\mu \in \mathbb{R}$, and an unresummed Dyson-Wick expansion in the HS field produces activity $\ge e^{O(\beta U)} - 1$, diverging as $U \to \infty$.*
2. **Reflection positivity obstruction (§5.2):** *RP is restricted to bipartite even-$L$ tori at exact half-filling $\mu = 0$ ($n = 1$) and does not yield high-temperature exponential decay.*
3. **Refutation of monotonicity in $U \ge 0$ (§5.3, `CERTIFIED` on 2-site dimer):** *Neither $\chi_{\rm pair}$ nor $|\langle \Delta_x^\dagger \Delta_y \rangle|$ is monotone non-increasing in $U \ge 0$ at fixed $(t, g, \beta, \mu)$ or fixed canonical $N$. Explicitly, on the 2-site dimer ($t=1, g=0, \beta=2, \mu=-3$, centered), $\chi_{\rm pair}(U=4) > 25\,\chi_{\rm pair}(U=0)$ and $|\langle \Delta_0^\dagger \Delta_1\rangle|_{U=4} > 25\,|\langle \Delta_0^\dagger \Delta_1\rangle|_{U=0}$; on the uncentered 2-site dimer ($\beta=1/2, \mu=5$), $|\langle \Delta_0^\dagger \Delta_1\rangle|_{U=4} > 4\,|\langle \Delta_0^\dagger \Delta_1\rangle|_{U=0}$; and on canonical $N=4$ on $C_4$ ($\beta=5$, `NUMERICAL`), $|\langle \Delta_0^\dagger \Delta_2\rangle|$ increases from $0.0208$ ($U=0$) to $0.0401$ ($U=1$).*
4. **Mott-edge obstruction for repulsive $t^2/U_{\rm eff}$ (§5.4):** *At $U_{\rm eff} > 0, |\mu| = U_{\rm eff}/2$, $G(\mu) = 0$ and `HUBHOL` Lemma 6.4 gives $w_\infty(\{e\}) \ge (\cosh \beta t - 1)/4$ independent of $U_{\rm eff}$. Thus no $\max(C_1 t^2/U_{\rm eff}, C_2 G_b)$ bound can hold $\mu$-uniformly at $U_{\rm eff} > 0$, and Theorem 1.1–1.2's $1024(|t|+G_b)$ term is strictly needed.*
5. **No $|U_{\rm eff}|_-$ term is needed for $U_{\rm eff} < 0$ (§5.5):** *In the atomic limit $t = g = 0$, $\langle \Delta_x^\dagger \Delta_y \rangle_{\rm GC} = \langle \Delta_x^\dagger \Delta_y \rangle_{\rm can} = 0$ identically for all $x \ne y$, all $T > 0$, all $\mu \in \mathbb{R}$, and all $U_{\rm eff} \in \mathbb{R}$ ($T_{\rm pair} = 0$). The scale $T^* \sim |U_{\rm eff}|$ is only local double-occupancy $\langle n_{x\uparrow} n_{x\downarrow}\rangle$, not spatial pair coherence; for $t, g \ne 0$, Theorems 1.1–1.3 prove $k_B T_{\rm pair} \le \min(1024(|t|+G_b), \max(2^{27} t^2/|U_{\rm eff}|, 2^{13} G_b))$.*

---

## 2. Exact Diagnosis of $U = 0$ in `PURESSH` and Functional-Analytic Setup

### 2.1 Audit of Every Occurrence of $U = 0$ in `ADIABATIC/PURESSH/RIGOR.md`

Inspection of `PURESSH/RIGOR.md` shows that $U = 0$ is used in **one and only one structural place**: setting $D_0 = -\mu N$ in §1.1 (lines 24–25) instead of $D_0(U_{\rm eff}, \mu) = -\frac{U_{\rm eff}}{2} N_{\rm odd} - \mu N$. Tracking every downstream lemma in `PURESSH`:
1. **§2 (Self-adjointness, compact resolvent, trace-norm Dyson series, Lemmas 2.1–2.2):** Uses only that $D_0$ is Hermitian and bounded ($\|D_0\|_{\rm op} < \infty$) on the finite-dimensional electronic space $\mathcal{F}_{\rm el}(\Lambda_L)$. Replacing $-\mu N$ by $D_0(U_{\rm eff}, \mu)$ leaves $\|D_0(U_{\rm eff}, \mu)\|_{\rm op} \le \bigl(\frac{|U_{\rm eff}|}{2} + 2|\mu|\bigr)|\Lambda_L| < \infty$.
2. **§3 (Free-boson thermal Wick identity & $\Omega$-uniform integral $\int_0^\beta C_\beta(|u-v|)du = 1/K$, Lemmas 3.1–3.2):** Purely bosonic; completely independent of $D_0$.
3. **§4.1 (Edge operator norms, Lemma 4.1):** Purely electronic ($T_b, Y_{e'}(\theta), \Delta_x^\dagger \Delta_y$); $\|T_b\|_{\rm op} = 2$, $\|Y_{e'}(\theta)\|_{\rm op} = 1$, $\|\Delta_x^\dagger \Delta_y\|_{\rm op} = 1$, independent of $D_0$.
4. **§4.2 (Multilinear Schatten–Hölder bound, Lemma 4.2):** Explicitly stated and proved for **any** finite-dimensional Hermitian matrix $D_{0,S}$! Its proof uses only positivity of $e^{-\Delta_j D_{0,S}}$ ($\|e^{-\Delta_j D_{0,S}}\|_{\beta/\Delta_j} = (\operatorname{Tr} e^{-\beta D_{0,S}})^{\Delta_j/\beta}$), which holds for every Hermitian matrix regardless of the sign or magnitude of $U_{\rm eff}$.
5. **§5.1 (Polymer factorization & charge conservation, Lemma 5.1):** Uses only that $D_0 = \sum_{x \in \Lambda_L} h_x$ is a **sum of commuting site-local Hermitian operators** and commutes with $N_\uparrow, N_\downarrow$. Both hold for $h_x(U_{\rm eff}, \mu) = -\frac{U_{\rm eff}}{2} n_{x,\mathrm{odd}} - \mu n_x$. Crucially, $z_0(\beta; U_{\rm eff}, \mu) := \operatorname{Tr}_{\mathcal{F}_{\rm el}(\{x\})}(e^{-\beta h_x(U_{\rm eff}, \mu)}) = 1 + 2e^{\beta(\mu + U_{\rm eff}/2)} + e^{2\beta\mu} > 0$ cancels **identically** between numerator $\operatorname{Tr}(e^{-\beta D_{0,S_E}}) = z_0^{|S_E|}$ and denominator $Z_0 = z_0^{|\Lambda_L|} Z_{\rm ph,0}$.
6. **§6 (Boundary spring-constant bracket & canonical transfer, Lemma 6.1):** Uses only that $D_0$ has **zero** bond terms crossing block boundaries $\partial$, commutes with $N_\uparrow$ and $N_\downarrow$, and admits a finite thermal trace. All three hold identically for $D_0(U_{\rm eff}, \mu)$.

### 2.2 Lang–Firsov Transformation When Holstein Phonons Are Present ($g_0 \ne 0$)

Let $S_{\rm LF} := \frac{g_0}{\Omega_0} \sum_{x \in \Lambda_L} (n_x - 1)(a_x^\dagger - a_x)$ (`STAGE6` §2, `HUBHOL` Lemma 1.2). Since $S_{\rm LF}$ commutes with $X_b, P_b, n_{x\sigma}, N$, the unitary $e^{S_{\rm LF}}$ transforms $H_{\Lambda_L}(\xi)$ into
\[
\widetilde{H}_{\Lambda_L}(\xi) := e^{S_{\rm LF}} H_{\Lambda_L}(\xi) e^{-S_{\rm LF}} = D_0(U_{\rm eff}, \mu) + \sum_{x \in \Lambda_L} \Omega_0 a_x^\dagger a_x + \sum_{b \in \mathcal{E}_{\Lambda_L}} H_{\mathrm{ph},b} + \widetilde{V}_t + \widetilde{V}_g + \widetilde{V}_{\rm src}(\xi) + C_0 I,
\]
where $C_0 = \bigl(\frac{U}{4} - \frac{U_{\rm Hol}}{2}\bigr)|\Lambda_L|$ cancels in every Gibbs ratio, and on each bond $b = \{x, y\}$ (with $\alpha_{\rm LF} := g_0/\Omega_0$),
\[
\widetilde{T}_b := e^{S_{\rm LF}} T_b e^{-S_{\rm LF}} = \sum_{\sigma \in \{\uparrow,\downarrow\}} \left(c_{x\sigma}^\dagger c_{y\sigma} D_x(\alpha_{\rm LF}) D_y(-\alpha_{\rm LF}) + \mathrm{h.c.}\right), \qquad D_x(\gamma) := e^{\gamma(a_x^\dagger - a_x)},
\]
while $\widetilde{\Delta}_x^\dagger \widetilde{\Delta}_y = \Delta_x^\dagger \Delta_y D_x(2\alpha_{\rm LF}) D_y(-2\alpha_{\rm LF})$ and $\widetilde{Y}_{e'}(\theta) = e^{i\theta} \widetilde{\Delta}_x^\dagger \widetilde{\Delta}_y + \mathrm{h.c.}$
Because $D_x(\gamma)$ is unitary on $\mathcal{H}_{\rm ph,0}$, $\|\widetilde{T}_b\|_{\rm op} = \|T_b\|_{\rm op} = 2$ and $\|\widetilde{Y}_{e'}(\theta)\|_{\rm op} = 1$. Moreover, when $g_0 \ne 0$, the extra Holstein oscillator trace factor at the largest time gap $\Delta_{j^*} \ge \beta/(K_{\rm tot}+1)$ in Schatten–Hölder contributes $\prod_{x \in \Lambda_L} (1 - e^{-\Delta_{j^*} \Omega_0})^{-1} = (1 - e^{-\Delta_{j^*} \Omega_0})^{-|\Lambda_L|} = O\bigl((K_{\rm tot}+1)^{|\Lambda_L|}\bigr)$, which is purely polynomial in the Dyson order $K_{\rm tot}$ and is dominated by the $\Gamma(K_{\rm tot}/2 + 1)$ decay, so Kato–Rellich + trace-norm Dyson convergence (`SSHBOUND3` Lemmas 2.1–2.2) hold verbatim on $\mathcal{D}(H_0)$ for all real $\xi$ (and analytically for $|\xi| < \xi_0$ as in §3).

---

## 3. Proof of Theorems 1.1 and 1.2 (Universal $1024(|t| + G_b)$ Bound)

### 3.1 Exact Polymer Activity Bound for Arbitrary $U_{\rm eff} \in \mathbb{R}$

*Proof of Theorem 1.1 (`proof draft`).*
**Case 1 ($g_0 = 0$, pure Hubbard + bond-SSH, $U_{\rm eff} = U$):**
Define $Z_0 := Z_{\rm el,0} Z_{\rm ph,b,0}$ with $Z_{\rm el,0} := \operatorname{Tr}(e^{-\beta D_0(U_{\rm eff},\mu)}) = z_0(\beta; U_{\rm eff}, \mu)^{|\Lambda_L|}$ and $Z_{\rm ph,b,0} := \prod_{b} Z_{\rm ph,b,1}(K)$. Expand $\operatorname{Tr}(\mathcal{O} e^{-\beta H_{\Lambda_L}(\xi)})/Z_0$ ($\mathcal{O} \in \{I, \Delta_x^\dagger \Delta_y\}$) in the trace-norm convergent Dyson series (`PURESSH` Lemma 2.2) with elementary bond insertions $(b, t)$ carrying $+t T_b$, $(b, g)$ carrying $-g X_b T_b$, and $(e', \mathrm{src})$ carrying $+\xi Y_{e'}(\theta)$. Exactly as in `PURESSH` Lemma 5.1, every connected component $E = E_{\rm phys} \sqcup E_{\rm src}$ ($E_{\rm phys} = E_t \cup E_g$) factorizes over $S_E$ vs. $\Lambda_L \setminus S_E$, cancelling $z_0^{|\Lambda_L \setminus S_E|}$ and leaving $z_0^{-|S_E|}$ in the denominator of $w(E)$ and $w_{xy}(E)$ (where the marked polymer for $\Delta_x^\dagger \Delta_y$ connects $x$ and $y$, because any component separating $x$ and $y$ has zero trace by $(N_\uparrow, N_\downarrow)$ conservation in $D_0$, $T_b$, $Y_{e'}(\theta)$).

Fix multiplicities $\{m_b, 2r_b\}_{b \in E_{\rm phys}}$ ($m_b + r_b \ge 1$; odd $g$-multiplicities vanish by $X_b \mapsto -X_b$ parity) and $\{p_{e'}\}_{e' \in E_{\rm src}}$ ($p_{e'} \ge 1$), with $K_{\rm tot} := \sum_b (m_b + 2r_b) + \sum_{e'} p_{e'}$. For any slot assignment and $0 < u_1 < \dots < u_{K_{\rm tot}} < \beta$:
1. **Electronic trace (`PURESSH` Lemma 4.2 applied to Hermitian $M = D_{0,S_E}(U_{\rm eff},\mu)$):**
   \[
   \left|\operatorname{Tr}_{\mathcal{F}_{\rm el}(S_E)}\!\left(\mathcal{O}\, e^{-(\beta - u_{K_{\rm tot}}) D_{0,S_E}} A_{K_{\rm tot}} \cdots A_1 e^{-u_1 D_{0,S_E}}\right)\right| \le \left(\prod_{b \in E_{\rm phys}} 2^{m_b + 2r_b}\right) \left(\prod_{e' \in E_{\rm src}} 1^{p_{e'}}\right) z_0(\beta; U_{\rm eff},\mu)^{|S_E|},
   \]
   since $\|T_b\|_{\rm op} = 2$, $\|Y_{e'}(\theta)\|_{\rm op} = 1$, and $\|\mathcal{O}\|_{\rm op} = 1$. Notice that $z_0^{|S_E|}$ **cancels identically** against $Z_0|_{S_E} = z_0^{|S_E|}$, leaving **zero dependence on $U_{\rm eff}$ or $\mu$**!
2. **Bosonic Wick integration (`PURESSH` §5.2 step 2):** Exact hypercube reduction over $[0,\beta]^{2r_b}$ using $\int_0^\beta C_\beta(|u-v|)du = 1/K$ (`PURESSH` Lemma 3.2) and $|\mathcal{P}_2(2r_b)| = (2r_b)!/(2^{r_b} r_b!)$ gives:
   - for each $b \in E_{\rm phys}$: $\sum_{m_b + r_b \ge 1} \frac{(2\beta|t|)^{m_b}}{m_b!} \frac{(2\beta G_b)^{r_b}}{r_b!} = e^{2\beta(|t| + G_b)} - 1 \le \frac{2c_0}{1 - c_0} = \varepsilon_{\rm phys} = \frac{2}{1023}$ when $\beta(|t| + G_b) \le c_0 = 2^{-10}$;
   - for each $e' \in E_{\rm src}$: $\sum_{p_{e'} \ge 1} \frac{(\beta|\xi|)^{p_{e'}}}{p_{e'}!} = e^{\beta|\xi|} - 1 \le \frac{2^{-9}}{1 - 2^{-10}} = \varepsilon_{\rm src} = \frac{2}{1023}$ for $|\xi| \le \xi_0 = 2^{-9}/\beta$.

**Case 2 ($g_0 \ne 0$, full Hubbard + Holstein + bond-SSH, $U_{\rm eff} = U - U_{\rm Hol} \in \mathbb{R}$):**
In the Lang–Firsov frame, expand each hopping and source operator in the Fock occupation basis $\{|\eta\rangle\}$ of $\mathcal{F}_{\rm el}(S_E)$ (`STAGE6` §2, `HUBHOL` Lemma 1.3(1)): for any fixed electronic occupation trajectory $\eta(\cdot)$ on $[0,\beta]$, the bond-SSH oscillators give the positive Wick product $\prod_{b \in E_{\rm phys}} \sum_{\pi_b} \prod C_\beta(|u_a - u_b|) > 0$, while the independent onsite Holstein oscillators evaluate identically to $e^{-\Phi_\beta[n]} \in (0, 1]$ (`HUBHOL` Lemma 1.3(1)). Bounding the electronic trajectory amplitudes by their absolute values replaces each $T_b$ by $B_b = |T_b|$, each $Y_{e'}(\theta)$ by $X_{e'}^{\rm pair} = |Y_{e'}(\theta)|$, and $\Delta_x^\dagger \Delta_y$ by itself (entrywise $\ge 0$), while replacing $e^{-\Phi_\beta[n]} \le 1$. Resumming the occupation-basis trajectories back to matrix products gives **identically**
\[
\operatorname{Tr}_{\mathcal{F}_{\rm el}(S_E)}\!\left(\mathcal{O}\, e^{-(\beta - u_{K_{\rm tot}}) D_{0,S_E}} |A_{K_{\rm tot}}| \cdots |A_1| e^{-u_1 D_{0,S_E}}\right).
\]
Since $\|B_b\|_{\rm op} = 2$ and $\|X_{e'}^{\rm pair}\|_{\rm op} = 1$ (`SSHBOUND3` Lemma 4.1), applying `PURESSH` Lemma 4.2 to this trace yields the **exact same** upper bound $(2^{m_b+2r_b}) z_0^{|S_E|}$, and hence the exact same $\varepsilon_{\rm phys} = \varepsilon_{\rm src} = \frac{2}{1023}$!

**Kotecký–Preiss verification:**
Because the Euler-tour rooted tree counts ($16^k$ for $D=4$ and $36^k$ for $D_{\rm aug}=6$) and $|S_E| \le k+1$ ($e^{|S_E|} \le 3^{k+1}$) are unchanged, we obtain identically:
- $q_{\rm GC} = 16 \cdot 3 \cdot \varepsilon_{\rm phys} = \frac{32}{341} < 1$, $b_{\rm GC} = \frac{32}{103} < 1$, $A_{\rm GC} = \frac{341}{103}$, $R_{\rm max} = \frac{24718511}{9834543} < 3$;
- $q_{\rm src} = 36 \cdot 3 \cdot \frac{2}{1023} = \frac{72}{341} < 1$, $b_{\rm src} = \frac{216}{269} < 1$.
Thus all conclusions of Theorem 1.1 hold verbatim for all $U_{\rm eff} \in \mathbb{R}$. $\square$

*Proof of Theorem 1.2 (`proof draft`).*
In the **untransformed** (original) frame, $D_0(U, \mu)$ and $H_{\rm Hol}$ are **strictly on-site**: zero terms from either cross block boundaries $\partial$. Only the bond-SSH terms $(-t + g X_b) T_b$ ($b \in \partial$) and source terms $Y_{e'}(\theta)$ ($e' \in \partial_{\rm src}$) cross $\partial$. On each $b \in \partial$, the exact quadratic-form bracket
\[
-\frac{K}{4} X_b^2 - \left(2|t| + \frac{4g^2}{K}\right)I \le (-t + g X_b) T_b \le \frac{K}{4} X_b^2 + \left(2|t| + \frac{4g^2}{K}\right)I
\]
holds on $\mathcal{D}(H_0)$ and in every $(N_\uparrow, N_\downarrow)$ and $N$ sector (`PURESSH` Lemma 6.1), giving the identical $C_{\rm bdry}$ independent of $U, g_0, \Omega_0, \mu, L$. Hence the block-partition superadditivity, thermodynamic canonical pressure concavity $f_{\rm can}(n) = \lim_{L\to\infty} L^{-2} \log \widehat{Z}_{\Lambda_L, N_L}$, existence of supporting chemical potential $\mu(n) \in \mathbb{R}$ for every $n \in (0, 2)$, and Cauchy-remainder Legendre transfer (`PURESSH` §6.2) hold verbatim, proving $k_B T_{\rm pair} \le 1024(|t| + G_b)$ and $k_B T_{\rm pair}^{\rm can}(n) \le 1024(|t| + G_b)$. $\square$

---

## 4. Proof of Theorems 1.3 and 1.4 (Combined `min` Bounds)

### 4.1 Attractive Regime ($U_{\rm eff} < 0$, Theorem 1.3)

*Proof (`proof draft`).*
When $U_{\rm eff} < 0$, write $U_{\rm eff}^{\rm SSH3} := -U_{\rm eff} > 0$, so $D_0(U_{\rm eff}, \mu) = +\frac{U_{\rm eff}^{\rm SSH3}}{2} N_{\rm odd} - \mu N$ matches `SSHBOUND3` §1.1 identically.
- If $g_0 = 0$ ($U_{\rm Hol} = 0$), `SSHBOUND3` Theorems 1.1 and 1.2 apply directly verbatim under $\beta t^2/|U_{\rm eff}| \le 2^{-27}$ and $\beta G_b \le 2^{-13}$.
- If $g_0 \ne 0$, by the Lang–Firsov + occupation-basis factorization of §3.1, the Holstein oscillators contribute the multiplicative trajectory factor $0 < e^{-\Phi_\beta[n]} \le 1$ (`HUBHOL` Lemma 1.3(1)), which leaves every entrywise non-negative majorant in `SSHBOUND3` §5.2 (`B_e`, `X_e'`, `C_\beta`) upper-bounded by the same trace with $\Phi_\beta \equiv 0$, while the canonical transfer Lemma 6.1 of `SSHBOUND3` holds verbatim because $H_{\rm Hol}$ is strictly on-site.
Taking the union of the hypotheses of Theorem 1.2 ($\beta(|t|+G_b) \le 2^{-10}$) and `SSHBOUND3` Theorem 1.2 ($\beta t^2/|U_{\rm eff}| \le 2^{-27}$ and $\beta G_b \le 2^{-13}$) immediately gives
\[
k_B T_{\rm pair} \le \min\!\left(1024(|t| + G_b),\; \max\!\left(2^{27}\frac{t^2}{|U_{\rm eff}|},\; 2^{13} G_b\right)\right) \qquad (\forall\, U_{\rm eff} < 0). \qquad \square
\]

### 4.2 Repulsive Mott and Dilute Windows ($U_{\rm eff} > 0$, Theorem 1.4)

*Proof (`proof draft`).*
For $U_{\rm eff} > 0$, let $G(\mu) := \bigl|\frac{U_{\rm eff}}{2} - |\mu|\bigr|$. On each site $x$, define the excess energy $E(s) - E_{\min}$ relative to the atomic ground state of $h_x(U_{\rm eff}, \mu) = -\frac{U_{\rm eff}}{2} n_{x,\mathrm{odd}} - \mu n_x$, and cost operator $\mathbf{1}_{\cdot,x}$ (`HUBHOL` §2):
- In **Mott window M** ($|\mu| < U_{\rm eff}/2$): $G = U_{\rm eff}/2 - |\mu| > 0$, $\mathbf{1}_{\cdot,x} = \mathbf{1}[n_x \in \{0,2\}] = n_{x,\mathrm{even}}$, and $E(0) - E(1) = U_{\rm eff}/2 + \mu \ge G$, $E(2) - E(1) = U_{\rm eff}/2 - \mu \ge G$. By `HUBHOL` Lemma 3.4(1), the single-site ratio $z_b/z_a$ with $\frac{G}{2} n_{x,\mathrm{even}}$ subtracted satisfies $z_b/z_a \le \frac{1+v}{1+v^2} < \frac{5}{4}$ ($v = e^{-\beta G/2}$).
- In **dilute windows D±** ($|\mu| > U_{\rm eff}/2$): $G = |\mu| - U_{\rm eff}/2 > 0$, $\mathbf{1}_{\cdot,x} = n_{x,\mathrm{occ}}$ (for $\mu < -U_{\rm eff}/2$, D−) or $n_{x,\mathrm{hole}}$ (for $\mu > U_{\rm eff}/2$, D+), and `HUBHOL` Lemma 3.4(2) gives $z_b/z_a \le \frac{1 + 2v + v^3}{(1+v^2)^2} < \frac{3}{2}$.

Now follow `SSHBOUND3` §5.2 step-by-step on the signless majorant after replacing $T_b \to B_b$, $Y_{e'}(\theta) \to X_{e'}^{\rm pair}$, and $e^{-\Phi_\beta[n]} \le 1$:
1. Resumming $t$-insertions (with scale $L_t \ge 1$) and source insertions (with scale $L_s \ge 1$) conditioned on $2R$ $g$-insertions gives $\operatorname{Tr}(O e^{-\Delta_{2R} M} B_{e_{2R}} \cdots B_{e_1} e^{-\Delta_0 M}) \le 2^{2R} \operatorname{Tr}(e^{-\beta M})$ where $M = D_{0,S_E} - L_t|t| B_{E_t} - L_s|\xi| X_{E_{\rm src}}^{\rm pair}$.
2. By `HUBHOL` Theorem 2.4 & Corollary 2.6 with $D = 4$ and $\alpha = G/(2D) = G/8$,
   \[
   L_t |t| B_{E_t} \le \frac{G}{2} \sum_{x \in S_E} \mathbf{1}_{\cdot,x} + \frac{16 |E_t| L_t^2 t^2}{G} I.
   \]
   Hence $\operatorname{Tr}(e^{-\beta M})/z_a^{|S_E|} \le c^{|S_E|} e^{\delta_t |E_t|} e^{\delta_s |E_{\rm src}|}$ with $\delta_t := \frac{16 L_t^2 \beta t^2}{G}$ and $\delta_s := \beta L_s |\xi|$.
3. Integrating over the bond-SSH Wick pairings gives the exact same factor $e^{2\beta G_b} - 1 \le \frac{2c_2}{1 - c_2}$ (`c_2 = 2^-13`), so per-edge activities are $\varepsilon_{\rm phys} = \frac{4}{3 L_t}(1 + \frac{2c_2}{1-c_2}) + \frac{2c_2}{1-c_2}$ and $\varepsilon_{\rm src} = \frac{4}{3 L_s}$ whenever $\delta_t \le 1/4$ and $\delta_s \le 1/8$.
4. **In M ($c = 5/4$):** Setting $L_t = 2^{10}, L_s = 2^{11}, \xi_0^{(5/4)} = 2^{-14}/\beta$ gives $\delta_t \le 16 \cdot 2^{20} \cdot 2^{-26} = 1/4$ under $\beta t^2/G \le 2^{-26}$, reproducing **every** `SSHBOUND3` constant verbatim (`CERTIFIED` in `replay.py`). At half-filling $n = 1$ on even tori, the full particle–hole unitary $U_{\rm ph}: c_{x\sigma}^\dagger \mapsto (-1)^{x_1+x_2} c_{x\sigma}$ (with $a_x \mapsto -a_x$ and $X_b \mapsto +X_b$) satisfies, for every nearest-neighbor bond $b = \{x, y\}$,
   \[
   U_{\rm ph}\left(c_{x\sigma}^\dagger c_{y\sigma} + c_{y\sigma}^\dagger c_{x\sigma}\right)U_{\rm ph}^\dagger = (-1)(c_{x\sigma} c_{y\sigma}^\dagger + c_{y\sigma} c_{x\sigma}^\dagger) = +(c_{y\sigma}^\dagger c_{x\sigma} + c_{x\sigma}^\dagger c_{y\sigma}) = T_b,
   \]
   since $c_{x\sigma} c_{y\sigma}^\dagger = -c_{y\sigma}^\dagger c_{x\sigma}$ for $x \ne y$ (`CERTIFIED` on $C_4$ in `replay.py`), while $n_x - 1 \mapsto -(n_x - 1)$ leaves $(n_{x\uparrow}-\tfrac12)(n_{x\downarrow}-\tfrac12)$ and $H_{\rm Hol}$ invariant and maps $-\mu N \mapsto -\mu(2|\Lambda_L| - N)$. Thus $f_{\rm can}(n) = f_{\rm can}(2-n)$ is symmetric and concave on $[0, 2]$, so $\mu = 0$ supports $n = 1$ at every $T > 0$, where $G(0) = U_{\rm eff}/2$, yielding Theorem 1.4(2).
5. **In D± ($c = 3/2$):** At $L_t = 2^{10}$, $q_{\rm GC} = 72\varepsilon_{\rm phys}^{(5/4)} = \frac{29187}{262112} < 1$ and $b_{\rm GC} = \frac{262683}{465850} < 1$, whereas $q_{\rm src} = 162 \varepsilon_{\rm phys}^{(5/4)} = \frac{262683}{1048448}$ gives $b_{\rm src} = \frac{2364147}{1571530} > 1$ (mutant `dilute_L1024_source`). Raising to $L_t = 2^{11}, L_s = 2^{12}$ ($\beta t^2/G \le 2^{-28}, \beta G_b \le 2^{-13}$) gives $\delta_t \le 16 \cdot 2^{22} \cdot 2^{-28} = 1/4$ and $b_{\rm src}^{(3/2)} = \frac{2737395}{3585482} < 1$ (`CERTIFIED`), enabling canonical transfer whenever $\mu(n)$ lies in D± and obeys $\beta t^2/G(\mu(n)) \le 2^{-28}$. $\square$

---

## 5. Obstructions and Counterexamples (Proof of Theorem 1.5)

### 5.1 Why Hubbard–Stratonovich with a Sign-Definite Field Fails for $U > 0$

For $U > 0$, write $U(n_{x\uparrow}-\tfrac12)(n_{x\downarrow}-\tfrac12) = \frac{U}{2}(n_x - 1)^2 - \frac{U}{4} = -\frac{U}{2}(n_{x\uparrow} - n_{x\downarrow})^2 + \frac{U}{4}$.
- **Charge HS channel ($+\frac{U}{2}(n_x-1)^2$):** Because the sign in $e^{-\beta H}$ is $-\frac{U}{2}(n_x-1)^2$ (negative quadratic), Gaussian decoupling requires an **imaginary** coupling $i \phi_x (n_x - 1)$, whose determinant is neither positive nor real-valued (the standard repulsive-Hubbard charge sign problem).
- **Spin HS channel ($-\frac{U}{2}(n_{x\uparrow}-n_{x\downarrow})^2$):** Here the coupling $\phi_x (n_{x\uparrow} - n_{x\downarrow})$ is real, so for a fixed realization $\phi(\cdot)$ the fermion weights factor by spin; however:
  1. Away from $\mu = 0$ (where particle–hole symmetry fails), $\det M_\uparrow(\phi,\mu) \det M_\downarrow(-\phi,\mu)$ is **not** guaranteed non-negative (only real, with fluctuating sign when $\mu \ne 0$ or when $g X_b$ breaks bipartite hopping equivalence), and $\phi_x$ is a **mean-zero Gaussian**, not a sign-definite field;
  2. More fatally for a high-temperature cluster bound: expanding the HS vertex $\phi_x(n_{x\uparrow}-n_{x\downarrow})$ via Wick integration (analogous to `PURESSH` §5.2) yields per-site factor $e^{\beta U/2} - 1$ (or $e^{O(\beta U)} - 1$), which **blows up exponentially** as $U \to \infty$ at fixed $\beta$, violating uniformity in $U \ge 0$! Conversely, Theorem 1.1 keeps $D_0(U_{\rm eff}, \mu)$ **unexpanded** inside the reference semigroup $e^{-\Delta_j D_0}$, avoiding any factor of $\beta U$ completely.

### 5.2 Why Reflection Positivity Fails as a Route Here

Reflection positivity (RP) across a bond-cutting plane requires:
1. Bipartite lattice with **even** side $L$ and reflection symmetry (fails for odd $L$, e.g., odd-size tori if included, and broken by non-uniform/arbitrary $\mu \ne 0$);
2. **Exact half-filling $\mu = 0$** (the centered repulsive Hubbard term $U(n_\uparrow-\tfrac12)(n_\downarrow-\tfrac12)$ is RP-compatible only at $\mu = 0$; any $\mu \ne 0$ breaks spin/particle–hole reflection conjugation, and canonical transfer requires $\mu \in \mathbb{R}$ for all densities $n \ne 1$);
3. Even at $\mu = 0$, RP gives **chessboard/infrared upper bounds** on long-range order ($|\langle \Delta_x^\dagger \Delta_y \rangle|$ bounded via reflection-symmetric averages), **not** high-temperature exponential clustering $|\langle \Delta_x^\dagger \Delta_y \rangle| \le A q^{d(x,y)}$ with explicit decay base $q < 1$ in graph distance.

### 5.3 Explicit Refutation of Monotonicity of $\chi_{\rm pair}(U)$ and $|\langle \Delta_x^\dagger \Delta_y\rangle|(U)$ in $U \ge 0$

**Proposition 5.1 (`CERTIFIED` exact rational-interval counterexamples on the 2-site dimer).**
Consider the 2-site Hubbard dimer ($t = 1, g = 0$, $H = -(c_{0\uparrow}^\dagger c_{1\uparrow} + c_{1\uparrow}^\dagger c_{0\uparrow} + c_{0\downarrow}^\dagger c_{1\downarrow} + c_{1\downarrow}^\dagger c_{0\downarrow}) + H_U - \mu N$):
1. **Centered convention ($H_U = U\sum_{x=0}^1 (n_{x\uparrow}-\tfrac12)(n_{x\downarrow}-\tfrac12)$) at $\beta = 2, \mu = -3$:** Both the off-diagonal pair correlator $|\langle \Delta_0^\dagger \Delta_1\rangle|$ and $\chi_{\rm pair} := \langle \Delta_0^\dagger \Delta_0\rangle + \langle \Delta_0^\dagger \Delta_1\rangle$ **strictly increase** with $U \ge 0$:
   - At $U = 0$: $\langle \Delta_0^\dagger \Delta_0\rangle \in [8.391\times 10^{-5}, 8.393\times 10^{-5}]$, $\langle \Delta_0^\dagger \Delta_1\rangle \in [7.788\times 10^{-5}, 7.790\times 10^{-5}]$, $\chi_{\rm pair}(0) \in [1.6180\times 10^{-4}, 1.6182\times 10^{-4}]$ (`CERTIFIED`).
   - At $U = 4$: $\langle \Delta_0^\dagger \Delta_0\rangle \in [2.2088\times 10^{-3}, 2.2090\times 10^{-3}]$, $\langle \Delta_0^\dagger \Delta_1\rangle \in [2.2049\times 10^{-3}, 2.2051\times 10^{-3}]$, $\chi_{\rm pair}(4) \in [4.4138\times 10^{-3}, 4.4140\times 10^{-3}]$ (`CERTIFIED`, $>27\times$ larger than at $U=0$).
   - (`NUMERICAL` continuation to $U = 8$ gives $\chi_{\rm pair}(8) \approx 0.01779685$, $\approx 110\times$ ($> 109.9\times$) larger than $\chi_{\rm pair}(0)$.)
   *Physical mechanism:* At fixed $\mu = -3 < 0$ in the centered convention (dropping the global scalar $U/4$ per site), the singly-occupied atomic energy is $E(1) = -U/2 - \mu = 3 - U/2$ while $E(2) = -2\mu = 6$ and $E(0) = 0$. On the dimer, the two-electron $(N_\uparrow, N_\downarrow) = (1, 1)$ subspace contains the singly-occupied state $|1\uparrow, 1\downarrow\rangle$ of diagonal energy $2E(1) = 6 - U$, which mixes via $T_b$ with the doubly-occupied pair states $|2, 0\rangle \pm |0, 2\rangle$ ($E = 6$). As $U$ increases from $0$ to $4$ (and $8$), the $(1, 1)$ ground-state energy drops toward (and below) the vacuum $E(0) = 0$, increasing the thermal population of the pair-coherent $N = 2$ sector relative to $N = 0$ by orders of magnitude.
2. **Uncentered convention ($H_U = U\sum_{x=0}^1 n_{x\uparrow} n_{x\downarrow}$) at $\beta = 1/2, \mu = 5$:** $|\langle \Delta_0^\dagger \Delta_1\rangle|$ **strictly increases** with $U \ge 0$:
   - At $U = 0$: $\langle \Delta_0^\dagger \Delta_1\rangle \in [1.2879\times 10^{-3}, 1.2881\times 10^{-3}]$ (`CERTIFIED`).
   - At $U = 4$: $\langle \Delta_0^\dagger \Delta_1\rangle \in [5.3243\times 10^{-3}, 5.3245\times 10^{-3}]$ (`CERTIFIED`, $>4.1\times$ larger than at $U=0$).
   *Physical mechanism:* At $\mu = 5, U = 0$, both sites are nearly doubly occupied ($n \approx 2$, Pauli-blocked pair hopping), whereas increasing $U$ toward $2\mu = 10$ creates empty/doubly-occupied + singly-occupied resonances that enhance off-diagonal pair coherence $\langle \Delta_0^\dagger \Delta_1\rangle$.
3. **Canonical fixed-$N$ counterexample (`NUMERICAL`, $C_4$ ring, $N = 4, t = 1, g = 0, \beta = 5$):** Independent of $\mu$ and centered/uncentered conventions, $|\langle \Delta_0^\dagger \Delta_2\rangle_{N=4}|$ increases from $0.020827$ ($U=0$) to $0.040148$ ($U=1$).

Therefore, **no** monotonicity-in-$U$ argument ($\partial_U |\langle \Delta_x^\dagger \Delta_y\rangle| \le 0$ or $\partial_U \chi_{\rm pair} \le 0$) is valid.

### 5.4 Mott-Edge Obstruction for Repulsive $t^2/U_{\rm eff}$ ($|\mu| = U_{\rm eff}/2$)

By `HUBHOL` Lemma 6.4 (applied at $g = 0$ and $\Omega_0 \to \infty$, which must be covered by any $\Omega_0, \Omega_b$-uniform bound by `HUBHOL` Theorem 5.2), for every $U_{\rm eff} > 0$ at $\mu = \pm U_{\rm eff}/2$ (where $G(\mu) = 0$):
\[
w_\infty(\{e\}) \ge \frac{\cosh(\beta t) - 1}{4} \qquad (\forall\, U_{\rm eff} > 0).
\]
At $\beta t = 3$, $\frac{\cosh(3) - 1}{4} > 2.266 > 2$ (`CERTIFIED`), exceeding the Kotecký–Preiss threshold for **every** $U_{\rm eff} > 0$, even when $\beta t^2 / U_{\rm eff}$ is arbitrarily small! Moreover, in the atomic limit $t = g = 0$ at $U_{\rm eff} > 0$, any canonical density $n \in (0, 1) \cup (1, 2)$ has supporting chemical potential $|\mu(n)| = U_{\rm eff}/2 + O(\tau)$, so $G(\mu(n)) = O(\tau)$ and $\beta t^2/G(\mu(n)) \sim (\beta t)^2$ rather than $\beta t^2/U_{\rm eff}$. Thus $\max(C_1 t^2/U_{\rm eff}, C_2 G_b)$ is genuinely obstructed away from $n = 1$ (and at $|\mu| = U_{\rm eff}/2$), making Theorem 1.1–1.2 ($1024(|t|+G_b)$) essential.

### 5.5 Attractive Regime $U_{\rm eff} < 0$: Atomic Limit and Why No $|U_{\rm eff}|_-$ Term Is Needed

**Proposition 5.2 (Exact vanishing of off-diagonal pair correlations in the atomic limit, `proof draft`).**
*Let $t = g = 0$ (arbitrary $U_{\rm eff} \in \mathbb{R}$, arbitrary $U, U_{\rm Hol} \ge 0$, arbitrary $K, \Omega_b, \Omega_0 > 0$, arbitrary $\beta > 0$, $\mu \in \mathbb{R}$, $L \ge 4$). For every pair of distinct sites $x \ne y \in \Lambda_L$:*
\[
\langle \Delta_x^\dagger \Delta_y \rangle_{\Lambda_L, \mathrm{GC}} = 0 \qquad \text{and} \qquad \langle \Delta_x^\dagger \Delta_y \rangle_{\Lambda_L, N} = 0 \quad (\forall\, 0 \le N \le 2|\Lambda_L|).
\]
*Consequently, $T_{\rm pair} = 0$ and $T_{\rm pair}^{\rm can}(n) = 0$ identically at $t = g = 0$, even when $U_{\rm eff} < 0$ is arbitrarily large!*

*Proof.* At $t = g = 0$, in the original frame $H_{\Lambda_L}(0) = \sum_{z \in \Lambda_L} H_z + \sum_b H_{\mathrm{ph},b}$ is a sum of commuting site-local operators (each $H_z$ commutes with the local particle number $n_z = n_{z\uparrow} + n_{z\downarrow}$). Hence every eigenstate of $H_{\Lambda_L}(0)$ (both in the full Fock space and in every fixed-$N$ canonical subspace) is a tensor product over sites with sharp local particle number $n_z$. Because $\Delta_x^\dagger \Delta_y$ changes $n_x$ by $+2$ and $n_y$ by $-2$ for $x \ne y$, every diagonal matrix element $\langle \psi | \Delta_x^\dagger \Delta_y | \psi \rangle$ in the eigenbasis vanishes identically. Thus $\operatorname{Tr}(\Delta_x^\dagger \Delta_y e^{-\beta H_{\Lambda_L}(0)}) = 0$ and $\operatorname{Tr}_{N}(\Delta_x^\dagger \Delta_y e^{-\beta H_{\Lambda_L}(0)}) = 0$, giving $T_{\rm pair} = 0$ by Definition 1.1. $\square$

**Clarification of the $T^* \sim |U_{\rm eff}|$ atomic-limit crossover:**
In the atomic limit ($t = g = 0, \mu = 0, U_{\rm eff} < 0$), the **on-site** double occupancy / pairing correlator is
\[
\langle \Delta_x^\dagger \Delta_x \rangle_{\mathrm{GC}} = \langle n_{x\uparrow} n_{x\downarrow} \rangle_{\mathrm{GC}} = \frac{1}{2\bigl(1 + e^{-\beta |U_{\rm eff}|/2}\bigr)} \in \left[\frac{1}{4}, \frac{1}{2}\right),
\]
which rises from $1/4$ (high $T$) to $1/2$ (low $T$) around $k_B T^* \sim |U_{\rm eff}|$. However, Definition 1.1 (`BARRIERS2-PAPER` Definition 2.1) defines $T_{\rm pair}$ strictly from **off-diagonal** spatial decay $|\langle \Delta_x^\dagger \Delta_y\rangle| \le A q^{d(x,y)}$ ($x \ne y$). Local preformed pairs at $t = g = 0$ have zero inter-site phase stiffness ($T_{\rm pair} = 0$), and for $t, g \ne 0$, Theorems 1.1–1.3 prove both $k_B T_{\rm pair} \le 1024(|t| + G_b)$ uniformly in $U_{\rm eff} < 0$ and $k_B T_{\rm pair} \le \max(2^{27} t^2/|U_{\rm eff}|, 2^{13} G_b)$ (showing $T_{\rm pair}$ is *bounded above* by $O(t^2/|U_{\rm eff}| + G_b)$ as $|U_{\rm eff}| \to \infty$, never growing like $|U_{\rm eff}|$). Thus **no $|U_{\rm eff}|_-$ term is needed in the bound**.

---

## 6. Open Problems, Scope Boundaries, and Non-Claims

- **`OPEN` (intermediate/low temperature for $U_{\rm eff} > 0$):** Inside the repulsive Mott window below $\max(2^{27}t^2/U_{\rm eff}, 2^{13} G_b)$ (at $n=1$), and at doped densities $n \ne 1$ below $1024(|t| + G_b)$, spatial pair decay remains open (at $g = 0, \mu = 0$, spin exchange is $O(t^2/U_{\rm eff})$, while doped repulsive systems near $|\mu| = U_{\rm eff}/2$ constitute a $t$–$J$-type problem).
- **`OPEN` (linear-in-$\Omega_b$ adiabatic ceiling):** For fixed $t, U_{\rm eff}$, Theorem 1.2 gives $k_B T_{\rm pair} \le 1024(|t| + G_b)$ uniformly in $\Omega_b$, which does not vanish as $\Omega_b \downarrow 0$ (`BARRIERS2-PAPER` covers why $\Omega \downarrow 0$ behaves differently).
- **Non-claims:** No experimental $T_c$ or physical material claim is made; all results are mathematical properties of $H_{\Lambda_L}$ in Definition 1.1. Finite-dimensional `replay.py` checks certify all finite algebra, exact constants, and the 2-site non-monotonicity counterexamples, while infinite-dimensional functional analysis and thermodynamic canonical limits are proved analytically above.
- **Related literature and scope relative to `BARRIERS2-PAPER`:** In the purely electronic Hubbard limit ($g = g_0 = 0$), keeping arbitrary on-site interaction $U \in \mathbb{R}$ inside $D_0$ for a $U$-uniform hopping/cluster expansion at $\beta|t| \le c$ is standard (Ueltschi, *J. Stat. Phys.* 95 (1999), 693–717; Ueltschi, *Moscow Math. J.* 4 (2004), 511–522; Fröhlich–Ueltschi, *J. Stat. Phys.* 118 (2005), 973–978; and `HUBHOL` Corollary 4.5 for Hubbard–Holstein). What is new here is extending the $U$-uniform expansion to **unbounded quantum bond-SSH (Peierls) oscillators** uniformly in $\Omega_b > 0$ (and jointly with Holstein phonons in $\Omega_0 > 0$), establishing the explicit combined `min(...)` ceilings across $(U_{\rm eff}, \mu)$, and certifying the dimer non-monotonicity refutations. `BARRIERS2-PAPER` Theorems 5.1, 5.3, and 5.4 remain completely valid for the pure bond-SSH model ($U_{\rm eff} = 0$); Theorems 1.1–1.2 show that `BARRIERS2-PAPER` Theorems 5.1 and 5.3 extend verbatim to all $U_{\rm eff} \in \mathbb{R}$ with identical constants, whereas `BARRIERS2-PAPER` Theorem 5.4(i) and (iii) genuinely require $U_{\rm eff} = 0$.
