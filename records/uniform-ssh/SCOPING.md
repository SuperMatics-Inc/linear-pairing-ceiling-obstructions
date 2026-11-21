# UNIFORM-SSH Scoping Note: $U$-Uniform and Combined Pairing Ceilings for the Hubbard–SSH Model

**Date:** 20 November 2026
**Workspace:** `D:/dev/scratch/ceiling-20261118/MASSIVE/UNIFORM-SSH/`
**Status & Labels:**
- Analytical results derived in this directory: **`proof draft`** (complete step-by-step proofs in `RIGOR.md`, independent review pending).
- Upstream reviewed results cited from `W/ADIABATIC/PURESSH/`, `W/ADIABATIC/SSHBOUND3/`, `W/ADIABATIC/HUBHOL/`: cited explicitly by path and theorem number.
- Exact rational (`fractions.Fraction`) and outward-rounded rational-interval checks in `replay.py`: **`CERTIFIED`** (once `replay.py` executes with exit `0`).
- Floating-point exact-diagonalization checks: **`NUMERICAL`** (diagnostics only; never cited as proof).

---

## 1. Exact Model Class and Sign Conventions

Let $\Lambda_L = (\mathbb{Z}/L\mathbb{Z})^2$ be a finite 2D square torus of side $L \ge 4$ ($|\Lambda_L| = L^2$, undirected nearest-neighbor bond set $\mathcal{E}_{\Lambda_L}$ of size $2L^2$, uniform degree $D = 4$). In units $\hbar = k_B = 1$, consider the spinful **Hubbard + Bond-SSH (+ optional onsite Holstein)** Hamiltonian on $\mathcal{H}_{\Lambda_L} = \mathcal{F}_{\rm el}(\Lambda_L) \otimes \mathcal{H}_{\rm ph,b} (\otimes \mathcal{H}_{\rm ph,0})$:
\[
H_{\Lambda_L}(\xi) := D_0 + V_t + V_g + V_{\rm src}(\xi) + \sum_{b \in \mathcal{E}_{\Lambda_L}} \left(\frac{P_b^2}{2M_b} + \frac{K}{2} X_b^2\right) \;\bigl[+ H_{\rm Hol}\bigr],
\]
where:
- $T_b := \sum_{\sigma \in \{\uparrow,\downarrow\}} (c_{x\sigma}^\dagger c_{y\sigma} + c_{y\sigma}^\dagger c_{x\sigma})$ for $b = \{x,y\} \in \mathcal{E}_{\Lambda_L}$, $V_t := -t \sum_{b} T_b$, $V_g := g \sum_b X_b T_b$, $G_b := g^2 / K \ge 0$, $\Omega_b := \sqrt{K/M_b} > 0$.
- $V_{\rm src}(\xi) := -\xi (e^{i\theta} \Delta_0^\dagger \Delta_r + e^{-i\theta} \Delta_r^\dagger \Delta_0)$ with $\Delta_x := c_{x\downarrow} c_{x\uparrow}$ for the canonical transfer.
- Optional onsite Holstein term $H_{\rm Hol} := \sum_{x \in \Lambda_L} \bigl(\Omega_0 a_x^\dagger a_x + g_0 (n_x - 1)(a_x + a_x^\dagger)\bigr)$ with $U_{\rm Hol} := 2g_0^2 / \Omega_0 = F^2 / K_0 \ge 0$ ($\Omega_0 > 0$).
- Onsite electronic Hamiltonian (after optional Lang–Firsov unitary transformation for $H_{\rm Hol}$):
  \[
  D_0 = U_{\rm eff} \sum_{x \in \Lambda_L} \left(n_{x\uparrow} - \frac{1}{2}\right)\left(n_{x\downarrow} - \frac{1}{2}\right) - \mu N = -\frac{U_{\rm eff}}{2} N_{\rm odd} - \mu N + \frac{U_{\rm eff}}{4}|\Lambda_L|,
  \]
  where $N_{\rm odd} := \sum_x \mathbf{1}[n_x = 1]$, $N := \sum_x n_x$, and
  \[
  U_{\rm eff} := U - U_{\rm Hol} \in \mathbb{R} \qquad (U \ge 0 \text{ repulsive Hubbard coupling}).
  \]

**Sign-convention reconciliation (critical across program files):**
- In **this note (`UNIFORM-SSH`)** and `BARRIERS2-PAPER`: $U_{\rm eff} > 0$ is **repulsive** and $U_{\rm eff} < 0$ is **attractive**.
- In `SSHBOUND3`: $U_{\rm eff}^{\rm SSH3} := -U_{\rm eff} > 0$ is **attractive** ($D_0^{\rm SSH3} = +\frac{U_{\rm eff}^{\rm SSH3}}{2} N_{\rm odd} - \mu N$).
- In `HUBHOL`: $U_{\rm eff}^{\rm HH} := U_{\rm Hol} - U_c = -U_{\rm eff}$ ($> 0$ attractive, $< 0$ repulsive).
- Note on uncentered $U n_{x\uparrow} n_{x\downarrow} - \mu_{\rm unc} n_x$: this equals $U(n_{x\uparrow}-\tfrac12)(n_{x\downarrow}-\tfrac12) - (\mu_{\rm unc} - \tfrac{U}{2}) n_x - \tfrac{U}{4}$, which is just a shift $\mu = \mu_{\rm unc} - U/2$ plus a cancelling scalar. Any $\mu$-uniform bound in $\mu \in \mathbb{R}$ is convention-independent.

**Definition of $T_{\rm pair}$ (`BARRIERS2-PAPER` Definition 2.1):**
$T_{\rm pair} := \inf \mathcal{Q}$, where $\mathcal{Q}$ is the set of temperatures $T > 0$ for which there exist constants $A < \infty$ and $q < 1$, **independent of $L \ge 4$ and of $\mu \in \mathbb{R}$**, such that $|\langle \Delta_x^\dagger \Delta_y \rangle_{\Lambda_L}| \le A q^{d_{\Lambda_L}(x,y)}$ for all $L \ge 4$, all $\mu \in \mathbb{R}$, and all $x \ne y \in \Lambda_L$.

---

## 2. Exact Target Statements

### Target A — Universal $U_{\rm eff}$-Uniform Bound (`proof draft`)
For **every** $U_{\rm eff} \in \mathbb{R}$ (every $U \ge 0$, every $U_{\rm eff} \ge 0$, and every $U_{\rm eff} < 0$, with or without onsite Holstein phonons at any $\Omega_0 > 0$), every $t, g, \mu \in \mathbb{R}$, every $K > 0, \Omega_b > 0$, and every torus $L \ge 4$, whenever
\[
\beta(|t| + G_b) \le 2^{-10} \qquad \Longleftrightarrow \qquad k_B T \ge 1024(|t| + G_b),
\]
all conclusions of `PURESSH` Theorems 1.1 and 1.2 hold **verbatim with identical constants**:
\[
\left|\langle \Delta_x^\dagger \Delta_y \rangle_{\Lambda_L}\right| \le \frac{341}{103}\left(\frac{32}{341}\right)^{d_{\Lambda_L}(x,y)}, \qquad \sup_{x \in \Lambda_L} \sum_{y \in \Lambda_L} |\langle \Delta_x^\dagger \Delta_y \rangle_{\Lambda_L}| \le \frac{24718511}{9834543} < 3,
\]
and the same exponential bound transfers to every translation-invariant thermodynamic canonical limit at any interior density $n \in (0, 2)$ (and spin-balanced $a \in (0, 1)$). Hence, **uniformly in $U \ge 0$, $U_{\rm eff} \in \mathbb{R}$, $\Omega_b > 0$, $\Omega_0 > 0$:**
\[
k_B T_{\rm pair} \le 1024(|t| + G_b).
\]

### Target B — Combined `min(...)` Bounds (`proof draft`)
1. **Attractive regime ($U_{\rm eff} < 0$, $\mu$-uniform and all canonical $n \in (0,2)$):**
   Combining Target A with `SSHBOUND3` Theorem 1.2 (plus the Lang–Firsov phonon contraction factor $0 < e^{-\Phi_\beta[n]} \le 1$ when $U_{\rm Hol} > 0$) yields the $\mu$-uniform, $n$-uniform, frequency-uniform ceiling
   \[
   k_B T_{\rm pair} \le \min\!\left(1024(|t| + G_b),\; \max\!\left(2^{27}\frac{t^2}{|U_{\rm eff}|},\; 2^{13} G_b\right)\right) \qquad (\forall\, U_{\rm eff} < 0).
   \]
2. **Repulsive regime ($U_{\rm eff} > 0$):**
   - **Canonical half-filling ($n = 1$, even tori) and Mott window ($|\mu| < U_{\rm eff}/2$):** Using `HUBHOL` §2–§3's Mott SOS bound ($G = U_{\rm eff}/2 - |\mu|$, cap $c = 5/4$) together with `SSHBOUND3` §5's bond-SSH Dyson–Wick resummation, we get the exact `SSHBOUND3` constants ($A_{\rm GC} = 1965840/475579$, $q_{\rm GC} = 48645/524224$) for $\beta t^2/G \le 2^{-26}$ and $\beta G_b \le 2^{-13}$. By full particle–hole symmetry at $n = 1$, $\mu = 0$ ($G = U_{\rm eff}/2$) supports $n = 1$, yielding:
     \[
     k_B T_{\rm pair}^{\rm can}(n=1) \le \min\!\left(1024(|t| + G_b),\; \max\!\left(2^{27}\frac{t^2}{U_{\rm eff}},\; 2^{13} G_b\right)\right) \qquad (\forall\, U_{\rm eff} > 0).
     \]
   - **Dilute windows ($|\mu| > U_{\rm eff}/2$, $G = |\mu| - U_{\rm eff}/2$):** With cap $c = 3/2$ (`HUBHOL` Lemma 3.4), GC clustering holds for $\beta t^2/G \le 2^{-26}$, $\beta G_b \le 2^{-13}$ ($L_t = 2^{10}$, $q_{\rm GC} = 29187/262112$), and canonical transfer holds at supported densities for $\beta t^2/G \le 2^{-28}$, $\beta G_b \le 2^{-13}$ ($L_t = 2^{11}, L_s = 2^{12}$, $b_{\rm src} = 2737395/3585482 < 1$).
   - **Why $\mu$-uniformity of $\max(2^{27}t^2/U_{\rm eff}, 2^{13} G_b)$ FAILS for $U_{\rm eff} > 0$:** At the Mott edges $|\mu| = U_{\rm eff}/2$, $G = 0$ and the `HUBHOL` Lemma 6.4 single-bond barrier gives $w_\infty(\{e\}) \ge (\cosh \beta t - 1)/4$ independent of $U_{\rm eff}$. Thus Target A ($1024(|t|+G_b)$) is genuinely required for $\mu$-uniformity and doped densities $n \ne 1$ when $U_{\rm eff} > 0$.

---

## 3. Exact Proof Route

1. **Where `PURESSH` uses $U = 0$:** Only in the definition $D_0 = -\mu N$ (`PURESSH/RIGOR.md` §§1.1, 2, 4.2, 5.1, 6.1).
2. **Direct inclusion of $U_{\rm eff}$ inside $D_0$:**
   - Replace $D_0 = -\mu N$ by $D_0(U_{\rm eff}, \mu) = -\frac{U_{\rm eff}}{2} N_{\rm odd} - \mu N$ (the scalar constant $\frac{U_{\rm eff}}{4}|\Lambda_L|$ cancels identically between numerator and denominator in every Gibbs expectation and polymer normalization).
   - Every site operator $h_x(U_{\rm eff}, \mu) = -\frac{U_{\rm eff}}{2} n_{x,\mathrm{odd}} - \mu n_x$ is finite-dimensional ($4\times 4$), diagonal in the Fock occupation basis, Hermitian, bounded ($\|h_x\|_{\rm op} \le |U_{\rm eff}|/2 + 2|\mu|$), and commutes with $N_\uparrow, N_\downarrow$.
   - **Lemma 2.1 & 2.2 (self-adjointness, compact resolvent, trace-norm Dyson series):** unchanged, since $\|D_0\|_{\rm op} < \infty$.
   - **Lemma 4.1 (edge operator norms):** unchanged ($\|T_b\|_{\rm op} = 2$, $\|Y_{e'}(\theta)\|_{\rm op} = 1$, $\|\Delta_x^\dagger \Delta_y\|_{\rm op} = 1$).
   - **Lemma 4.2 (multilinear Schatten–Hölder):** proved for *arbitrary* Hermitian matrices $M = D_{0,S}$; uses only positivity of $e^{-\Delta_j D_{0,S}}$ and $\sum \Delta_j = \beta$, independent of the spectrum or sign of $U_{\rm eff}$.
   - **Lemma 5.1 (cluster factorization & exact $Z_0$ cancellation):** for any polymer support $S_E$, $D_0 = \sum_{x \in S_E} h_x + \sum_{x \notin S_E} h_x$, so $\operatorname{Tr}_{\mathcal{F}_{\rm el}(\Lambda_L \setminus S_E)}(e^{-\beta D_{0,\Lambda_L \setminus S_E}}) = z_0(\beta; U_{\rm eff}, \mu)^{|\Lambda_L \setminus S_E|}$, and in the Dyson bound $\operatorname{Tr}_{\mathcal{F}_{\rm el}(S_E)}(e^{-\beta D_{0,S_E}}) = z_0(\beta; U_{\rm eff}, \mu)^{|S_E|}$ cancels $z_0^{|S_E|}$ in $Z_0 = z_0^{|\Lambda_L|} Z_{\rm ph,0}$ **identically**! No ratio $z_b/z_a$ is ever formed!
   - **Lemma 6.1 (canonical transfer with unbounded boundary SSH):** $D_0$ is strictly on-site, so it has **zero** edges crossing block boundaries $\partial$. Thus $C_{\rm bdry}$ is unchanged, and the canonical pressure density $f_{\rm can}(n) = \lim L^{-2} \log \widehat{Z}_{\Lambda_L, N}$ remains concave on $[0, 2]$ (as the thermodynamic limit of superadditive block-partitioned canonical log-partition functions), so every interior density $n \in (0, 2)$ has a supporting chemical potential $\mu(n) \in \mathbb{R}$, to which the $\mu$-uniform Theorem 1.1 applies directly.
   - **Optional Holstein phonons ($U_{\rm Hol} > 0$):** In the Lang–Firsov frame (`HUBHOL` §1.2, `STAGE7R` §2), $S_{\rm LF}$ commutes with $D_0$ and $(X_b, P_b)$, dresses $\Delta_x^\dagger \Delta_y$ by unitary displacements $D_x(2\alpha_{\rm LF}) D_y(-2\alpha_{\rm LF})$ (leaving $\|Y_{e'}(\theta)\|_{\rm op} = 1$ and $\|T_b\|_{\rm op} = 2$ unchanged at fixed phonon path), and introduces only a real factor $0 < e^{-\Phi_\beta[n]} \le 1$ per Dyson trajectory (retaining absolute trace-norm convergence via `HUBHOL` Lemma 5.1 and `SSHBOUND3` Lemma 2.2), so every electronic activity bound goes through unchanged with factor $\le 1$.

---

## 4. Failure Points and Refuted Routes

| Candidate route / claim | Verdict | Exact failure point or refutation |
|---|---|---|
| **Direct Dyson-Wick absorbing $U_{\rm eff}$ into $D_0$** | **SUCCEEDS (Target A)** | No gap needed; $z_0(U_{\rm eff}, \mu)^{|S|}$ cancels identically; all constants of `PURESSH` survive verbatim for all $U_{\rm eff} \in \mathbb{R}$. |
| **Hubbard–Stratonovich with sign-definite field for $U > 0$** | **OBSTRUCTED** | Charge HS has imaginary coupling $i\phi_x(n_x - 1)$ (not sign-definite; phase/sign problem). Spin HS has real zero-mean $\phi_x(n_{x\uparrow}-n_{x\downarrow})$ (neither sign-definite nor sign-problem-free for $\mu \ne 0$; unresummed Dyson/Wick expansion gives $e^{O(\beta U)}-1$, blowing up as $U \to \infty$). |
| **Reflection positivity (RP) for $U > 0$** | **OBSTRUCTED** | Requires bipartite even-$L$ torus and exact half-filling $\mu = 0$ ($n = 1$); fails for $\mu \ne 0$, $n \ne 1$, odd $L$. Moreover RP yields chessboard/IR upper bounds, not high-temperature exponential decay $|\langle \Delta_x^\dagger \Delta_y\rangle| \le A q^{d(x,y)}$. |
| **Monotonicity of $\chi_{\rm pair}$ or $|\langle\Delta_x^\dagger \Delta_y\rangle|$ in $U \ge 0$** | **FALSE (Counterexamples)** | Explicitly violated already at $g = 0$ on a 2-site dimer ($\beta = 2, \mu = -3$, centered: $\chi_{\rm pair}$ increases $\approx 110\times$ ($>109.9\times$) from $U=0$ to $U=8$; $\beta=0.5, \mu=5$, uncentered: $|\langle \Delta_0^\dagger \Delta_1\rangle|$ increases $>4.1\times$) and in canonical $N=4$ on $C_4$ ($\beta=5$: $|\langle \Delta_0^\dagger \Delta_2\rangle|$ increases from $0.0208$ at $U=0$ to $0.0401$ at $U=1$). |
| **Attractive $U_{\rm eff} < 0$ unboundedness ($T_{\rm pair} \sim |U_{\rm eff}|$ in atomic limit)** | **FALSE (No $|U_{\rm eff}|_-$ term needed)** | At $t = g = 0$, $H$ is strictly site-diagonal, so $\langle \Delta_x^\dagger \Delta_y \rangle = 0$ identically for all $x \ne y$ in both GC and canonical ensembles for every $T > 0, \mu \in \mathbb{R}, U_{\rm eff} \in \mathbb{R}$; thus $T_{\rm pair} = 0$. The scale $T^* \sim |U_{\rm eff}|$ governs only **local** pair formation $\langle n_{x\uparrow}n_{x\downarrow}\rangle$, not spatial pair coherence. For $t, g \ne 0$, both Target A ($1024(|t|+G_b)$) and Target B ($\max(2^{27}t^2/|U_{\rm eff}|, 2^{13}G_b)$) hold at $U_{\rm eff} < 0$. |
| **$\mu$-uniform $\max(2^{27}t^2/U_{\rm eff}, 2^{13}G_b)$ for repulsive $U_{\rm eff} > 0$** | **OBSTRUCTED at Mott edges** | At $|\mu| = U_{\rm eff}/2$, atomic gap $G(\mu) = 0$; `HUBHOL` Lemma 6.4 gives $w_\infty(\{e\}) \ge (\cosh \beta t - 1)/4$ independent of $U_{\rm eff}$. Thus `SSHBOUND3`-type scaling holds in $U_{\rm eff} > 0$ only inside M ($|\mu| < U_{\rm eff}/2$, canonical $n=1$) and D± ($|\mu| > U_{\rm eff}/2$), not $\mu$-uniformly. |
