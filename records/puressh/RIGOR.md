# PURESSH: Frequency-Uniform High-Temperature Pair-Correlation Ceiling and Route Obstructions for the Pure Bond-SSH Model ($U_{\rm eff} = 0$)

Labels follow the program standard:
- **PROVED (pending independent review)**: complete analytical proof given step-by-step in this document with no unproved "standard" gaps.
- **CERTIFIED**: exact rational (`fractions.Fraction`) or outward-rounded rational-interval check verified by `PURESSH/replay.py`.
- **NUMERICAL**: finite-cutoff exact diagonalization or floating-point quadrature check (`PURESSH/ed_check.py`, not a proof).
- **[INFERENCE]** / **OPEN**: explicitly labeled where applicable.

---

## 1. Model, Conventions, and Main Results

### 1.1 Hamiltonian and Hilbert Space

Let $\Lambda_L = (\mathbb{Z}/L\mathbb{Z})^2$ be a finite 2D square torus of side $L \ge 4$, with vertex set $\Lambda_L$ of size $|\Lambda_L| = L^2$, undirected nearest-neighbor physical bond set $\mathcal{E}_{\Lambda_L}$ of size $|\mathcal{E}_{\Lambda_L}| = 2L^2$, and uniform vertex degree $D = 4$. In units with $\hbar = 1$, the spinful pure bond-SSH (Peierls) Hamiltonian ($U_{\rm eff} = 0$) on the tensor-product Hilbert space
\[
\mathcal{H}_{\Lambda_L} = \mathcal{F}_{\rm el}(\Lambda_L) \otimes \mathcal{H}_{\rm ph}(\Lambda_L), \qquad \mathcal{F}_{\rm el}(\Lambda_L) \cong \mathbb{C}^{4^{|\Lambda_L|}}, \qquad \mathcal{H}_{\rm ph}(\Lambda_L) = \bigotimes_{b \in \mathcal{E}_{\Lambda_L}} L^2(\mathbb{R}, dx_b),
\]
is
\[
H_{\Lambda_L} = D_0 + V_t + V_g + \sum_{b \in \mathcal{E}_{\Lambda_L}} H_{\mathrm{ph},b},
\]
with:
1. **Chemical-potential generator ($U_{\rm eff} = 0$):**
   \[
   D_0 := -\mu N = -\mu \sum_{x \in \Lambda_L} n_x, \qquad n_x := n_{x\uparrow} + n_{x\downarrow}, \qquad n_{x\sigma} := c_{x\sigma}^\dagger c_{x\sigma} \in \{0,1\};
   \]
2. **Nearest-neighbor hopping and bond-SSH coupling:** for each undirected bond $b = \{x,y\} \in \mathcal{E}_{\Lambda_L}$,
   \[
   T_b := \sum_{\sigma \in \{\uparrow,\downarrow\}} \left(c_{x\sigma}^\dagger c_{y\sigma} + c_{y\sigma}^\dagger c_{x\sigma}\right), \qquad V_t := -t \sum_{b \in \mathcal{E}_{\Lambda_L}} T_b, \qquad V_g := g \sum_{b \in \mathcal{E}_{\Lambda_L}} X_b T_b;
   \]
3. **Independent harmonic bond oscillators:** with spring constant $K > 0$, mass $M > 0$, and phonon frequency $\Omega := \sqrt{K/M} > 0$,
   \[
   H_{\mathrm{ph},b} := \frac{P_b^2}{2M} + \frac{K}{2} X_b^2 = \Omega \left(a_b^\dagger a_b + \frac{1}{2}\right), \qquad [X_b, P_{b'}] = i \delta_{b,b'}, \qquad H_{\rm ph} := \sum_{b \in \mathcal{E}_{\Lambda_L}} H_{\mathrm{ph},b}.
   \]

Replacing $g \mapsto -g$ is unitarily equivalent under the oscillator parity reflection $(X_b, P_b) \mapsto (-X_b, -P_b)$, and our proofs apply directly to arbitrary real $t \in \mathbb{R}$ and $g \in \mathbb{R}$.

For canonical transfer at a fixed nonzero torus displacement $r \in \Lambda_L \setminus \{0\}$, define the source-augmented multigraph $(\Lambda_L, \mathcal{E}_{\rm aug})$ with $\mathcal{E}_{\rm aug} := \mathcal{E}_{\Lambda_L} \sqcup \mathcal{E}_{\rm src}$, where $\mathcal{E}_{\rm src} := \{e'_x = (x, x+r) : x \in \Lambda_L\}$ has $|\mathcal{E}_{\rm src}| = |\Lambda_L|$ source edges. Each vertex $z \in \Lambda_L$ is an endpoint of two source edges ($e'_z$ and $e'_{z-r}$), so $\mathcal{E}_{\rm aug}$ has maximum vertex degree $D_{\rm aug} = 4 + 2 = 6$. For each $e' = e'_x \in \mathcal{E}_{\rm src}$ and phase $\theta \in [0, 2\pi)$, let
\[
\Delta_x := c_{x\downarrow} c_{x\uparrow}, \qquad Y_{e'}(\theta) := e^{i\theta} \Delta_x^\dagger \Delta_{x+r} + e^{-i\theta} \Delta_{x+r}^\dagger \Delta_x, \qquad V_{\rm src}(\xi) := -\xi \sum_{e' \in \mathcal{E}_{\rm src}} Y_{e'}(\theta),
\]
and set $H_{\Lambda_L}(\xi) := H_{\Lambda_L} + V_{\rm src}(\xi)$ (with $H_{\Lambda_L}(0) = H_{\Lambda_L}$). At inverse temperature $\beta = (k_B T)^{-1} > 0$, the grand-canonical state is
\[
\langle \mathcal{O} \rangle_{\Lambda_L} := \frac{\operatorname{Tr}_{\mathcal{H}_{\Lambda_L}}\!\left(\mathcal{O}\, e^{-\beta H_{\Lambda_L}}\right)}{Z_{\Lambda_L}}, \qquad Z_{\Lambda_L}(\xi) := \operatorname{Tr}_{\mathcal{H}_{\Lambda_L}}\!\left(e^{-\beta H_{\Lambda_L}(\xi)}\right), \qquad Z_{\Lambda_L} := Z_{\Lambda_L}(0).
\]

### 1.2 Explicit Constants

Fix the dimensionless threshold and source radius
\[
c_0 := 2^{-10} = \frac{1}{1024}, \qquad \xi_0 := 2^{-9} \beta^{-1} = \frac{k_B T}{512}.
\]
Under the combined high-temperature hypothesis
\[
\beta|t| + \frac{\beta g^2}{K} \le c_0 = 2^{-10}, \qquad \beta|\xi| \le 2^{-9},
\]
set $x_{\rm phys} := 2\beta|t| + \frac{2\beta g^2}{K} \le 2c_0 = 2^{-9}$ and $x_{\rm src} := \beta|\xi| \le 2^{-9}$. Define the exact rational constants (**CERTIFIED** in `replay.py`):
\[
\varepsilon_{\rm phys} := \frac{2c_0}{1 - c_0} = \frac{2}{1023} \approx 0.0019550342, \qquad \varepsilon_{\rm src} := \frac{2^{-9}}{1 - 2^{-10}} = \frac{2}{1023} = \varepsilon_{\rm phys},
\]
\[
q_{\rm GC} := 48 \varepsilon_{\rm phys} = \frac{32}{341} \approx 0.0938416422 < \frac{1}{10}, \qquad A_{\rm GC} := \frac{3}{1 - q_{\rm GC}} = \frac{341}{103} \approx 3.3106796117,
\]
\[
b_{\rm GC} := \frac{3 q_{\rm GC}}{1 - q_{\rm GC}} = \frac{32}{103} \approx 0.3106796117 < 1,
\]
\[
R_{\rm max} := 1 + \frac{4 A_{\rm GC} q_{\rm GC}}{(1 - q_{\rm GC})^2} = \frac{24718511}{9834543} \approx 2.5134376859 < 3,
\]
\[
q_{\rm src} := 108 \max(\varepsilon_{\rm phys}, \varepsilon_{\rm src}) = \frac{72}{341} \approx 0.2111436950 < 1, \qquad b_{\rm src} := \frac{3 q_{\rm src}}{1 - q_{\rm src}} = \frac{216}{269} \approx 0.8029739777 < 1.
\]

### 1.3 Main Theorems and Proved Obstructions

**Theorem 1.1 (Frequency- and $\mu$-uniform grand-canonical pair clustering for pure bond-SSH, PROVED pending independent review).**
*For every torus side $L \ge 4$, every $t \in \mathbb{R}$, every $g \in \mathbb{R}$, every $K > 0$, every $M > 0$ ($\Omega = \sqrt{K/M} > 0$), every $\mu \in \mathbb{R}$, and every $\beta > 0$ satisfying*
\[
\beta|t| + \frac{\beta g^2}{K} \le 2^{-10} \qquad \Longleftrightarrow \qquad k_B T \ge 1024\left(|t| + \frac{g^2}{K}\right),
\]
*the equal-time on-site singlet pair correlator satisfies, for all $x \ne y \in \Lambda_L$ at torus graph distance $d_{\Lambda_L}(x,y) \ge 1$,*
\[
\left|\langle \Delta_x^\dagger \Delta_y \rangle_{\Lambda_L}\right| \le A_{\rm GC} q_{\rm GC}^{d_{\Lambda_L}(x,y)} = \frac{341}{103}\left(\frac{32}{341}\right)^{d_{\Lambda_L}(x,y)},
\]
*and the integrated pair susceptibility is uniformly bounded by*
\[
\sup_{x \in \Lambda_L} \sum_{y \in \Lambda_L} \left|\langle \Delta_x^\dagger \Delta_y \rangle_{\Lambda_L}\right| \le R_{\rm max} = \frac{24718511}{9834543} < 3.
\]
*Moreover, for every fixed nonzero displacement $r \in \Lambda_L \setminus \{0\}$, the normalized grand-canonical log-partition function $p_{\Lambda_L}(\xi) := |\Lambda_L|^{-1} \log Z_{\Lambda_L}(\xi)$ extends to a zero-free analytic function on the complex disk $\{\xi \in \mathbb{C} : |\xi| < \xi_0\}$ and satisfies for all real $\xi \in [0, \xi_0/2]$:*
\[
p_{\Lambda_L}(\xi) - p_{\Lambda_L}(0) \le 2\beta A_{\rm GC} q_{\rm GC}^{d_{\Lambda_L}(0,r)} \xi + \frac{4\xi^2}{\xi_0^2}.
\]

**Theorem 1.2 (Thermodynamic canonical pair-correlation decay for pure bond-SSH, PROVED pending independent review).**
*Under the same condition $\beta|t| + \beta g^2/K \le 2^{-10}$, let $L_j \to \infty$ ($L_j \ge 4$) be any sequence of square tori and let $N_j \in \{0, 1, \dots, 2L_j^2\}$ with $N_j / L_j^2 \to n \in (0, 2)$ (or balanced spin-sector numbers $N_{j\uparrow} = N_{j\downarrow} = N_j/2$ with $N_{j\sigma}/L_j^2 \to a \in (0, 1)$). Then for every fixed nonzero displacement $r \in \mathbb{Z}^2 \setminus \{0\}$ with $\ell_1$ norm $d(0,r) = \|r\|_1 \ge 1$, the canonical expectation $\langle \cdot \rangle_{L_j, \mathrm{can}}$ on $\mathcal{H}_{\Lambda_{L_j}, N_j}$ (or $\mathcal{H}_{\Lambda_{L_j}, (N_{j\uparrow}, N_{j\downarrow})}$) satisfies*
\[
\limsup_{j \to \infty} \left|\langle \Delta_0^\dagger \Delta_r \rangle_{L_j, \mathrm{can}}\right| \le A_{\rm GC} q_{\rm GC}^{d(0,r)} = \frac{341}{103}\left(\frac{32}{341}\right)^{\|r\|_1}.
\]
*Consequently, in both grand-canonical and thermodynamic canonical ensembles, the pair-correlation decay temperature $T_{\rm pair}$ of the pure bond-SSH model ($U_{\rm eff} = 0$) satisfies*
\[
k_B T_{\rm pair} \le 1024\left(|t| + \frac{g^2}{K}\right) = 2^{10}\left(|t| + \frac{g^2}{K}\right),
\]
*uniformly in $\Omega = \sqrt{K/M} > 0$, $\mu \in \mathbb{R}$, and interior density $n \in (0, 2)$.*

**Theorem 1.3 (Proved route obstructions for pure bond-SSH at $U_{\rm eff} = 0$, PROVED pending independent review).**
1. **Absence of a phonon-induced instantaneous atomic gap (Proposition 7.1):** *In the antiadiabatic limit $\Omega \to \infty$ at $t = 0, \mu = 0$, integrating out the bond oscillators produces the exact instantaneous operator $H_{\rm eff}^{\rm inst} = -\frac{g^2}{2K} \sum_{b \in \mathcal{E}_\Lambda} T_b^2$. On the 4-site ring $C_4$ at half-filling $N = 4$ (across both the spin-balanced space $N_\uparrow = N_\downarrow = 2$ of dimension $36$ and the full $N = 4$ space of dimension $70$), the minimum eigenvalue of $H_{\rm eff}^{\rm inst}$ on the purely paired subspace $\{N = 4, N_{\rm odd} = 0\}$ equals $-6g^2/K$, while across all odd-parity sectors $\{N = 4, N_{\rm odd} > 0\}$ ($N_{\rm odd} = 4$ with $S_z = 0, \pm 1, \pm 2$ and $N_{\rm odd} = 2$ with $S_z = 0, \pm 1$) its minimum eigenvalue is also $-6g^2/K$ (achieved on $\{N_\uparrow = N_\downarrow = 2, N_{\rm odd} = 4\}$, whereas $N_{\rm odd} = 2$ and $S_z \ne 0$ have strictly higher minimum energies $-5g^2/K$, $-4g^2/K$, $-3g^2/K$, and $0$). Hence the induced gap between $N_{\rm odd} = 0$ and $N_{\rm odd} > 0$ is identically zero ($\Delta_{\rm eff} = 0$), obstructing Route (b).*
2. **Non-commutativity and adiabatic divergence of bond Lang-Firsov transformations (Proposition 7.2):** *For any two bonds $b = \{x,y\}$ and $b' = \{y,z\}$ sharing vertex $y$, $[T_b, T_{b'}] = \sum_\sigma (c_{x\sigma}^\dagger c_{z\sigma} - c_{z\sigma}^\dagger c_{x\sigma}) \ne 0$ with $\|[T_b, T_{b'}]\|_{\rm op} = 2$. Under the bond Lang-Firsov generator $S = -i(g/K)\sum_b P_b T_b$, $\operatorname{ad}_S^k(H_\Lambda)$ generates an infinite non-terminating hierarchy of multi-bond momentum operators $(\frac{g}{K})^k P_{b_1}\cdots P_{b_k} \operatorname{ad}_{T_{b_1}}\cdots\operatorname{ad}_{T_{b_{k-1}}}(T_{b_k})$ whose thermal RMS norm per factor scales as $\frac{|g|}{K}\sqrt{\langle P_b^2\rangle_{0,\beta}} = \sqrt{\frac{g^2}{2K\Omega}\coth(\frac{\beta\Omega}{2})} \to \infty$ as $\Omega \downarrow 0$, obstructing Route (c).*
3. **Obstruction to $(\beta t)$-independent uniform exponential clustering (Proposition 7.3):** *At $g = 0$ ($\beta g^2/K = 0$) and $\mu = 0$ on $\Lambda_L$, for every integer $m \ge 1$ and staircase displacement $r_m = (m, m-1) \in \mathbb{Z}^2$ of graph distance $d_m = 2m - 1$,*
   \[
   \lim_{\beta t \to \infty} \lim_{L \to \infty} \langle \Delta_0^\dagger \Delta_{(m,m-1)} \rangle_{\Lambda_L}\big|_{g=0,\, \mu=0} = \frac{4}{\pi^4 (2m - 1)^2} = \frac{4}{\pi^4 d_m^2}.
   \]
   *Therefore, for every pair of constants $A > 0$ and $q \in (0, 1)$, there exist $m \ge 1$, $\beta t > 0$, and $L \ge 4$ such that $|\langle \Delta_0^\dagger \Delta_{r_m} \rangle_{\Lambda_L}|_{g=0,\mu=0} > A q^{d_{\Lambda_L}(0,r_m)}$. No uniform exponential clustering bound with $(\beta t)$-independent constants $(A, q)$ can hold under a condition on $\beta g^2/K$ alone.*

---

## 2. Self-Adjointness, Holomorphic Semigroup, and Trace-Norm Dyson Convergence

Let $H_0 := D_0 + H_{\rm ph}$ with natural domain $\mathcal{D}(H_0) = \mathcal{F}_{\rm el}(\Lambda_L) \otimes \mathcal{D}(H_{\rm ph})$. In the occupation-number basis $|\eta\rangle \otimes |\{n_b\}_{b \in \mathcal{E}_{\Lambda_L}}\rangle$ ($n_b \in \mathbb{Z}_{\ge 0}$), $H_0$ is diagonal with eigenvalues
\[
E_0(\eta, \{n_b\}) = -\mu N(\eta) + \Omega \sum_{b \in \mathcal{E}_{\Lambda_L}} \left(n_b + \frac{1}{2}\right), \qquad \operatorname{Tr}_{\mathcal{H}_{\Lambda_L}}\!\left(e^{-\delta H_0}\right) = (1 + e^{\delta\mu})^{2|\Lambda_L|} \left(2\sinh\frac{\delta\Omega}{2}\right)^{-|\mathcal{E}_{\Lambda_L}|} < \infty \quad (\forall\, \delta > 0).
\]
Write the bounded electronic perturbation at $\xi \in \mathbb{C}$ as
\[
W(\xi) := V_t + V_{\rm src}(\xi) = -t \sum_{b \in \mathcal{E}_{\Lambda_L}} T_b - \xi \sum_{e' \in \mathcal{E}_{\rm src}} Y_{e'}(\theta).
\]

**Lemma 2.1 (Kato-Rellich self-adjointness and trace-class semigroup for $\xi \in \mathbb{C}$, PROVED pending independent review).**
*For every real $\xi \in \mathbb{R}$, $H_{\Lambda_L}(\xi) = H_0 + V_g + W(\xi)$ is self-adjoint on $\mathcal{D}(H_0) = \mathcal{D}(H_{\rm ph})$, bounded below, with compact resolvent. Moreover, for every complex $\xi \in \mathbb{C}$ and every $\beta > 0$, $-H_{\Lambda_L}(\xi)$ generates a norm-analytic semigroup $e^{-u H_{\Lambda_L}(\xi)}$ ($u > 0$) such that $e^{-\beta H_{\Lambda_L}(\xi)}$ is trace-class on $\mathcal{H}_{\Lambda_L}$ and the map $\xi \mapsto \operatorname{Tr}(\mathcal{O}\, e^{-\beta H_{\Lambda_L}(\xi)})$ is entire on $\mathbb{C}$ for every bounded operator $\mathcal{O}$.*

*Proof.* On each bond $b \in \mathcal{E}_{\Lambda_L}$, Lemma 4.1 below shows that $T_b$ is Hermitian with $\|T_b\|_{\rm op} = 2$, and that $\|Y_{e'}(\theta)\|_{\rm op} = 1$. For any state $\Psi \in \mathcal{D}(H_{\rm ph})$ and any $\varepsilon > 0$, Young's inequality gives
\[
\|g X_b T_b \Psi\| \le 2|g| \|X_b \Psi\|, \qquad 2|g| |x_b| \le \varepsilon \frac{K}{2} x_b^2 + \frac{2g^2}{\varepsilon K} \le \varepsilon H_{\mathrm{ph},b} + \frac{2g^2}{\varepsilon K}.
\]
Since $\frac{K}{2}\|X_b \Psi\|^2 \le \langle \Psi, H_{\mathrm{ph},b}\Psi\rangle$ for each bond $b \in \mathcal{E}_{\Lambda_L}$ and $\sum_{b \in \mathcal{E}_{\Lambda_L}} \langle \Psi, H_{\mathrm{ph},b}\Psi\rangle = \langle \Psi, H_{\rm ph}\Psi\rangle \le \|\Psi\|\|H_{\rm ph}\Psi\|$, applying the Cauchy-Schwarz inequality over the $|\mathcal{E}_{\Lambda_L}|$ bonds followed by AM-GM gives, for all $\Psi \in \mathcal{D}(H_0)$ and $\varepsilon > 0$:
\[
\|V_g \Psi\| \le \sum_{b \in \mathcal{E}_{\Lambda_L}} 2|g|\|X_b \Psi\| \le 2|g|\sqrt{|\mathcal{E}_{\Lambda_L}|}\left(\sum_{b \in \mathcal{E}_{\Lambda_L}} \|X_b\Psi\|^2\right)^{1/2} \le 2|g|\sqrt{\frac{2|\mathcal{E}_{\Lambda_L}|}{K}}\,\|\Psi\|^{1/2}\|H_{\rm ph}\Psi\|^{1/2} \le \varepsilon \|H_{\rm ph} \Psi\| + \frac{2 |\mathcal{E}_{\Lambda_L}| g^2}{\varepsilon K}\|\Psi\| \le \varepsilon \|H_0 \Psi\| + \left(\varepsilon\|D_0\|_{\rm op} + \frac{2|\mathcal{E}_{\Lambda_L}|g^2}{\varepsilon K}\right)\|\Psi\|.
\]
Since $\varepsilon > 0$ is arbitrary and $V_g$ is symmetric on $\mathcal{D}(H_0)$, $V_g$ is $H_0$-bounded with relative bound $0$. When $\xi \in \mathbb{R}$, $W(\xi)$ is bounded and Hermitian with $\|W(\xi)\|_{\rm op} \le 2|t||\mathcal{E}_{\Lambda_L}| + |\xi||\mathcal{E}_{\rm src}|$, so by the Kato-Rellich theorem $H_{\Lambda_L}(\xi)$ is self-adjoint on $\mathcal{D}(H_0)$ and bounded below by
\[
H_{\Lambda_L}(\xi) \ge -\|D_0\|_{\rm op} - \|W(\xi)\|_{\rm op} - \frac{2|\mathcal{E}_{\Lambda_L}|g^2}{K} \qquad (\xi \in \mathbb{R}).
\]
Choosing $\varepsilon = 1/2$ gives $\|H_0 \Psi\| \le 2\|H_{\Lambda_L}(0)\Psi\| + C\|\Psi\|$, so the resolvent of $H_{\Lambda_L}(0)$ factors through $(H_0 + C' I)^{-1}$ (which is trace-class and hence compact) times a bounded operator, proving compact resolvent. Since $H_{\Lambda_L}(0)$ is self-adjoint and bounded below with $\mathcal{D}(H_{\Lambda_L}(0)) = \mathcal{D}(H_0)$, $e^{-u H_{\Lambda_L}(0)}$ is trace-class for every $u > 0$. For arbitrary $\xi \in \mathbb{C}$, $H_{\Lambda_L}(\xi) = H_{\Lambda_L}(0) + V_{\rm src}(\xi)$ is a bounded perturbation of $H_{\Lambda_L}(0)$ with $\|V_{\rm src}(\xi)\|_{\rm op} \le |\xi||\mathcal{E}_{\rm src}|$, so its norm-convergent Dyson expansion around $H_{\Lambda_L}(0)$ defines a trace-class operator $e^{-\beta H_{\Lambda_L}(\xi)}$ depending holomorphically on $\xi \in \mathbb{C}$ in trace norm $\|\cdot\|_1$. $\square$

**Lemma 2.2 (Absolute trace-norm convergence of the Dyson expansion around $H_0$, PROVED pending independent review).**
*For every $\xi \in \mathbb{C}$, every bounded operator $\mathcal{O}$ on $\mathcal{F}_{\rm el}(\Lambda_L)$ (identified with $\mathcal{O} \otimes I_{\rm ph}$), and every $\beta > 0$, write the total interaction as $V(\xi) := V_t + V_g + V_{\rm src}(\xi)$. Then the Dyson series*
\[
\operatorname{Tr}_{\mathcal{H}_{\Lambda_L}}\!\left(\mathcal{O}\, e^{-\beta H_{\Lambda_L}(\xi)}\right) = \sum_{N=0}^\infty (-1)^N \int_{0 < u_1 < \dots < u_N < \beta} \operatorname{Tr}_{\mathcal{H}_{\Lambda_L}}\!\left(\mathcal{O}\, e^{-(\beta - u_N) H_0} V(\xi) e^{-(u_N - u_{N-1}) H_0} \cdots V(\xi) e^{-u_1 H_0}\right) du_1 \cdots du_N
\]
*converges absolutely in trace norm $\|\cdot\|_1$. The exact same identity holds on any subgraph Hilbert space $\mathcal{H}_E = \mathcal{F}_{\rm el}(S_E) \otimes \bigotimes_{b \in E_{\rm phys}} L^2(\mathbb{R}, dx_b)$.*

*Proof.* For any $\delta > 0$ and $b \in \mathcal{E}_{\Lambda_L}$, the single-oscillator operator $X_b e^{-\delta H_{\mathrm{ph},b}}$ is bounded with
\[
X_b^2 \le \frac{2}{K} H_{\mathrm{ph},b}, \qquad \sup_{E \ge \Omega/2} E e^{-2\delta E} \le \frac{1}{2 e \delta} \implies \|X_b e^{-\delta H_{\mathrm{ph},b}}\|_{\rm op} = \|e^{-\delta H_{\mathrm{ph},b}} X_b\|_{\rm op} \le \frac{1}{\sqrt{e K \delta}}.
\]
Let $C_W(\xi) := \|W(\xi)\|_{\rm op} \le 2|t||\mathcal{E}_{\Lambda_L}| + |\xi||\mathcal{E}_{\rm src}|$. For each $N \ge 0$ and each simplex point $0 < u_1 < \dots < u_N < \beta$, set $\Delta_0 = u_1$, $\Delta_j = u_{j+1}-u_j$ ($1 \le j \le N-1$), and $\Delta_N = \beta - u_N$. Since $\sum_{j=0}^N \Delta_j = \beta$, the pigeonhole principle ensures that at least one index $j^* \in \{0, \dots, N\}$ satisfies $\Delta_{j^*} \ge \frac{\beta}{N+1}$. Split $\Delta_{j^*} = \frac{\Delta_{j^*}}{2} + \frac{\Delta_{j^*}}{2}$ and pair each of the $N$ insertions $V(\xi)$ with half of the adjacent imaginary-time interval to its left (for $j \le j^*$) or to its right (for $j > j^*$). Using $\|e^{-s H_0}\|_{\rm op} \le e^{s\|D_0\|_{\rm op}}$ for $s \ge 0$, every insertion $j \in \{1, \dots, N\}$ has operator norm bounded by
\[
\|V(\xi) e^{-(\Delta_{j-1}/2) H_0}\|_{\rm op} \le e^{\frac{\Delta_{j-1}}{2}\|D_0\|_{\rm op}} \left(C_W(\xi) + \frac{2|g||\mathcal{E}_{\Lambda_L}|}{\sqrt{e K (\Delta_{j-1}/2)}}\right) \qquad (j \le j^*),
\]
and identically with $\Delta_j/2$ for $j > j^*$. Meanwhile, the remaining half-interval $\frac{\Delta_{j^*}}{2} \ge \frac{\beta}{2(N+1)}$ at position $j^*$ supplies a trace-class factor with trace norm bounded by
\[
\left\|e^{-(\Delta_{j^*}/2) H_0}\right\|_1 = \operatorname{Tr}_{\mathcal{F}_{\rm el}(\Lambda_L)}\!\left(e^{-(\Delta_{j^*}/2) D_0}\right) \operatorname{Tr}_{\mathcal{H}_{\rm ph}(\Lambda_L)}\!\left(e^{-(\Delta_{j^*}/2) H_{\rm ph}}\right) \le 4^{|\Lambda_L|} e^{\frac{\Delta_{j^*}}{2}\|D_0\|_{\rm op}} \left(2\sinh\frac{\beta\Omega}{4(N+1)}\right)^{-|\mathcal{E}_{\Lambda_L}|},
\]
where we used $t \mapsto (2\sinh t)^{-1}$ decreasing on $(0, \infty)$. Since $\|A B\|_1 \le \|A\|_{\rm op}\|B\|_1$ and $\prod_{j=0}^N e^{\frac{\Delta_j}{2}\|D_0\|_{\rm op}} \le e^{\beta\|D_0\|_{\rm op}}$, the trace norm of the integrand is bounded by
\[
\|\mathcal{O}\|_{\rm op}\, 4^{|\Lambda_L|} e^{\beta\|D_0\|_{\rm op}} \left(2\sinh\frac{\beta\Omega}{4(N+1)}\right)^{-|\mathcal{E}_{\Lambda_L}|} \prod_{j=1}^N \left(C_W(\xi) + \frac{2\sqrt{2}|g||\mathcal{E}_{\Lambda_L}|}{\sqrt{e K \tilde{\Delta}_j}}\right),
\]
where $\tilde{\Delta}_1, \dots, \tilde{\Delta}_N$ are $N$ distinct intervals among $\Delta_0, \dots, \Delta_N$. Expanding the product into $2^N$ terms, each term with $m$ factors of $\tilde{\Delta}_j^{-1/2}$ integrates over the simplex $\Delta_0 + \dots + \Delta_N = \beta$ via the Dirichlet beta integral
\[
\int_{\Delta_0 + \dots + \Delta_N = \beta} \prod_{r=1}^m \Delta_{i_r}^{-1/2}\, d\Delta_1 \cdots d\Delta_N = \frac{\beta^{N - m/2} \pi^{m/2}}{\Gamma(N + 1 - m/2)} \le \frac{\beta^{N - m/2} \pi^{N/2}}{\Gamma(N/2 + 1)}.
\]
Since $(2\sinh(\frac{\beta\Omega}{4(N+1)}))^{-|\mathcal{E}_{\Lambda_L}|} = O((N+1)^{|\mathcal{E}_{\Lambda_L}|})$ grows only polynomially in $N$ while $\Gamma(N/2 + 1)$ grows super-exponentially, the $N$-series of trace norms is summable for all $\beta > 0$ and $\xi \in \mathbb{C}$. By Fubini's theorem and Duhamel's formula on $\mathcal{D}(H_0)$, the series sums to $\operatorname{Tr}(\mathcal{O}\, e^{-\beta H_{\Lambda_L}(\xi)})$. $\square$

---

## 3. Exact Gaussian Phonon Wick Identity and Frequency-Uniform Covariance Integral

For a single harmonic oscillator $H_{\mathrm{ph},1} = \frac{P^2}{2M} + \frac{K}{2} X^2 = \Omega(a^\dagger a + \frac{1}{2})$ with $\Omega = \sqrt{K/M} > 0$, let $Z_{\mathrm{ph},1} := \operatorname{Tr}_{L^2(\mathbb{R})}(e^{-\beta H_{\mathrm{ph},1}}) = (2\sinh(\beta\Omega/2))^{-1}$ and define the imaginary-time Heisenberg position operator $X(u) := e^{u H_{\mathrm{ph},1}} X e^{-u H_{\mathrm{ph},1}}$ for $u \in [0, \beta]$.

**Lemma 3.1 (Positivity and exact Wick expansion of the thermal oscillator trace, PROVED pending independent review).**
*For any integer $n \ge 1$ and ordered times $0 \le u_1 \le u_2 \le \dots \le u_n \le \beta$:*
1. *If $n$ is odd, $\langle X(u_n) \cdots X(u_1) \rangle_{0,\beta} := Z_{\mathrm{ph},1}^{-1} \operatorname{Tr}_{L^2(\mathbb{R})}\!\left(e^{-\beta H_{\mathrm{ph},1}} X(u_n) \cdots X(u_1)\right) = 0$.*
2. *If $n = 2r$ is even, let $\mathcal{P}_2(2r)$ be the set of all $|\mathcal{P}_2(2r)| = (2r-1)!! = \frac{(2r)!}{2^r r!}$ pair partitions of $\{1, \dots, 2r\}$. Then*
   \[
   \langle X(u_{2r}) \cdots X(u_1) \rangle_{0,\beta} = \sum_{\pi \in \mathcal{P}_2(2r)} \prod_{\{a,b\} \in \pi} C_\beta(|u_a - u_b|),
   \]
   *where the thermal covariance kernel $C_\beta(\tau)$ on $\tau \in [0, \beta]$ is strictly positive:*
   \[
   C_\beta(\tau) := \langle X(\tau) X(0) \rangle_{0,\beta} = \frac{1}{2M\Omega} \frac{\cosh\!\left(\left(\frac{\beta}{2} - \tau\right)\Omega\right)}{\sinh\!\left(\frac{\beta\Omega}{2}\right)} = \frac{\Omega}{2K} \frac{\cosh\!\left(\left(\frac{\beta}{2} - \tau\right)\Omega\right)}{\sinh\!\left(\frac{\beta\Omega}{2}\right)} > 0.
   \]

*Proof.* Under the unitary parity operator $\Pi: \psi(x) \mapsto \psi(-x)$, $\Pi H_{\mathrm{ph},1} \Pi^{-1} = H_{\mathrm{ph},1}$ and $\Pi X(u) \Pi^{-1} = -X(u)$, so inserting $\Pi^{-1}\Pi = I$ inside the trace multiplies by $(-1)^n$, proving (1) for odd $n$. For $n = 2$, substituting $X = \frac{1}{\sqrt{2M\Omega}}(a + a^\dagger)$, $e^{u H_{\mathrm{ph},1}} a e^{-u H_{\mathrm{ph},1}} = e^{-u\Omega} a$, $e^{u H_{\mathrm{ph},1}} a^\dagger e^{-u H_{\mathrm{ph},1}} = e^{u\Omega} a^\dagger$, and $\langle a^\dagger a \rangle_{0,\beta} = (e^{\beta\Omega} - 1)^{-1}$ gives
\[
C_\beta(\tau) = \frac{1}{2M\Omega}\left(\frac{e^{(\beta-\tau)\Omega}}{e^{\beta\Omega}-1} + \frac{e^{\tau\Omega}}{e^{\beta\Omega}-1}\right) = \frac{\Omega}{2K} \frac{\cosh\!\left(\left(\frac{\beta}{2} - \tau\right)\Omega\right)}{\sinh\!\left(\frac{\beta\Omega}{2}\right)} > 0 \qquad (\tau \in [0, \beta]),
\]
since $M\Omega^2 = K$ and $\cosh > 0$, $\sinh(\beta\Omega/2) > 0$. Because $e^{-\beta H_{\mathrm{ph},1}}$ is a centered quasi-free bosonic state and $X(u)$ is linear in $a, a^\dagger$, commuting $a_{u_n} := \frac{1}{\sqrt{2M\Omega}} e^{-u_n\Omega} a$ and $a_{u_n}^\dagger := \frac{1}{\sqrt{2M\Omega}} e^{u_n\Omega} a^\dagger$ around the thermal trace to contract $X(u_{2r})$ against each $X(u_j)$ for $1 \le j \le 2r-1$ and inducting on $r$ yields (2). $\square$

**Lemma 3.2 (Exact frequency-uniform double integral of $C_\beta$, PROVED pending independent review).**
*For every $K > 0$, every $M > 0$, every $\Omega = \sqrt{K/M} > 0$, and every $\beta > 0$:*
\[
\int_0^\beta C_\beta(\tau)\, d\tau = \frac{1}{K}, \qquad \int_0^\beta \int_0^\beta C_\beta(|u - v|)\, du\, dv = \frac{\beta}{K}.
\]

*Proof.* By the fundamental theorem of calculus,
\[
\int_0^\beta \cosh\!\left(\left(\frac{\beta}{2} - \tau\right)\Omega\right) d\tau = \left[-\frac{1}{\Omega}\sinh\!\left(\left(\frac{\beta}{2} - \tau\right)\Omega\right)\right]_0^\beta = \frac{2}{\Omega}\sinh\!\left(\frac{\beta\Omega}{2}\right).
\]
Multiplying by $\frac{\Omega}{2K \sinh(\beta\Omega/2)}$ cancels both $\Omega$ and $\sinh(\beta\Omega/2)$ identically, giving $\int_0^\beta C_\beta(\tau)\, d\tau = \frac{1}{K}$. Since $C_\beta(\beta - \tau) = C_\beta(\tau)$, the function $\tau \mapsto C_\beta(|\tau|)$ is $\beta$-periodic and even, so for every $u \in [0, \beta]$, $\int_0^\beta C_\beta(|u - v|)\, dv = \int_0^\beta C_\beta(\tau)\, d\tau = \frac{1}{K}$. Integrating over $u \in [0, \beta]$ gives $\frac{\beta}{K}$. $\square$

---

## 4. Electronic Operator Norms and Multilinear Schatten-Hölder Bound

**Lemma 4.1 (Operator norms of $T_b$, $Y_{e'}(\theta)$, and $\Delta_x^\dagger \Delta_y$, PROVED pending independent review and CERTIFIED).**
1. *For every bond $b = \{x,y\} \in \mathcal{E}_{\Lambda_L}$, $T_b = \sum_{\sigma \in \{\uparrow,\downarrow\}} (c_{x\sigma}^\dagger c_{y\sigma} + c_{y\sigma}^\dagger c_{x\sigma})$ is Hermitian with spectrum $\{-2, -1, 0, 1, 2\}$ and operator norm $\|T_b\|_{\rm op} = 2$.*
2. *For every source edge $e' = (x, x+r) \in \mathcal{E}_{\rm src}$ and $\theta \in [0, 2\pi)$, $Y_{e'}(\theta) = e^{i\theta} \Delta_x^\dagger \Delta_{x+r} + e^{-i\theta} \Delta_{x+r}^\dagger \Delta_x$ is Hermitian with spectrum $\{-1, 0, 1\}$ and operator norm $\|Y_{e'}(\theta)\|_{\rm op} = 1$.*
3. *For every pair of sites $x, y \in \Lambda_L$, $\|\Delta_x\|_{\rm op} = \|\Delta_x^\dagger\|_{\rm op} = 1$ and $\|\Delta_x^\dagger \Delta_y\|_{\rm op} = 1$.*
4. *Each of the operators $T_b$, $Y_{e'}(\theta)$, and $\Delta_x^\dagger \Delta_y$ commutes with $N_\uparrow := \sum_z n_{z\uparrow}$, $N_\downarrow := \sum_z n_{z\downarrow}$, $N = N_\uparrow + N_\downarrow$, and the fermion parity operator $(-1)^N$.*

*Proof.*
1. For a single spin species $\sigma$, let $h_{b,\sigma} := c_{x\sigma}^\dagger c_{y\sigma} + c_{y\sigma}^\dagger c_{x\sigma}$. Using the canonical anticommutation relations (CAR) $\{c_{u\sigma}, c_{v\sigma}^\dagger\} = \delta_{u,v}$, we compute
   \[
   h_{b,\sigma}^2 = c_{x\sigma}^\dagger c_{y\sigma} c_{y\sigma}^\dagger c_{x\sigma} + c_{y\sigma}^\dagger c_{x\sigma} c_{x\sigma}^\dagger c_{y\sigma} = n_{x\sigma}(1 - n_{y\sigma}) + n_{y\sigma}(1 - n_{x\sigma}) = (n_{x\sigma} - n_{y\sigma})^2,
   \]
   which is an orthogonal projection with eigenvalues $\{0, 1\}$, so $h_{b,\sigma}$ has eigenvalues $\{-1, 0, 1\}$ and $\|h_{b,\sigma}\|_{\rm op} = 1$. Since $[h_{b,\uparrow}, h_{b,\downarrow}] = 0$ and $T_b = h_{b,\uparrow} + h_{b,\downarrow}$, the eigenvalues of $T_b$ are sums of eigenvalues of $h_{b,\uparrow}$ and $h_{b,\downarrow}$, namely $\{-2, -1, 0, 1, 2\}$, so $\|T_b\|_{\rm op} = 2$.
2. On the 2-site electronic Fock space of $\{x, z\}$ ($z = x+r \ne x$), $\Delta_x^\dagger \Delta_z = c_{x\uparrow}^\dagger c_{x\downarrow}^\dagger c_{z\downarrow} c_{z\uparrow}$ maps $|0\rangle_x |\uparrow\downarrow\rangle_z \mapsto |\uparrow\downarrow\rangle_x |0\rangle_z$ and annihilates all other 15 occupation basis states. Hence on $\operatorname{span}\{|0\rangle_x|\uparrow\downarrow\rangle_z, |\uparrow\downarrow\rangle_x|0\rangle_z\}$, $Y_{e'}(\theta)$ acts as the $2\times 2$ Pauli matrix $\bigl(\begin{smallmatrix} 0 & e^{-i\theta} \\ e^{i\theta} & 0 \end{smallmatrix}\bigr)$ with eigenvalues $\pm 1$, and vanishes on the 14-dimensional orthogonal complement. Thus $\|Y_{e'}(\theta)\|_{\rm op} = 1$.
3. Similarly, $\Delta_x^\dagger \Delta_x = n_{x\uparrow} n_{x\downarrow}$ is a projection of norm $1$, so $\|\Delta_x\|_{\rm op} = \sqrt{\|\Delta_x^\dagger \Delta_x\|_{\rm op}} = 1$ and $\|\Delta_x^\dagger \Delta_y\|_{\rm op} \le \|\Delta_x^\dagger\|_{\rm op}\|\Delta_y\|_{\rm op} = 1$ (attained on $|0\rangle_x|\uparrow\downarrow\rangle_y$).
4. Every monomial in $T_b$, $Y_{e'}(\theta)$, and $\Delta_x^\dagger \Delta_y$ has equal numbers of creation and annihilation operators for each spin $\sigma \in \{\uparrow, \downarrow\}$, so it conserves $N_\uparrow$ and $N_\downarrow$ and has even fermion degree. $\square$

**Lemma 4.2 (Multilinear Schatten-Hölder trace bound and exact site cancellation at $U_{\rm eff} = 0$, PROVED pending independent review and CERTIFIED).**
*Let $S \subseteq \Lambda_L$ be any nonempty vertex set, let $D_{0,S} := -\mu \sum_{x \in S} n_x$ on $\mathcal{F}_{\rm el}(S)$, and let $z_0 := (1 + e^{\beta\mu})^2 = \operatorname{Tr}_{\mathcal{F}_{\rm el}(\{x\})}(e^{-\beta D_{0,\{x\}}})$. For every integer $K_{\rm tot} \ge 0$, every sequence of bounded operators $A_0, A_1, \dots, A_{K_{\rm tot}}$ on $\mathcal{F}_{\rm el}(S)$, and every sequence of nonnegative times $\Delta_0, \Delta_1, \dots, \Delta_{K_{\rm tot}} \ge 0$ with $\sum_{j=0}^{K_{\rm tot}} \Delta_j = \beta$:*
\[
\frac{\left|\operatorname{Tr}_{\mathcal{F}_{\rm el}(S)}\!\left(A_0\, e^{-\Delta_{K_{\rm tot}} D_{0,S}} A_{K_{\rm tot}} \cdots A_1 e^{-\Delta_0 D_{0,S}}\right)\right|}{z_0^{|S|}} \le \prod_{j=0}^{K_{\rm tot}} \|A_j\|_{\rm op}.
\]

*Proof.* Since $D_{0,S}$ is Hermitian, $e^{-\Delta_j D_{0,S}}$ is strictly positive definite for every $\Delta_j \ge 0$. Assign Schatten exponent $p_j := \beta / \Delta_j \in [1, \infty]$ to $e^{-\Delta_j D_{0,S}}$ (with $p_j = \infty$ when $\Delta_j = 0$, where $\|e^{-0 D_{0,S}}\|_\infty = \|I\|_{\rm op} = 1$) and $q_j = \infty$ to $A_j$. Since $\sum_{j=0}^{K_{\rm tot}} \frac{1}{p_j} = \sum_{j=0}^{K_{\rm tot}} \frac{\Delta_j}{\beta} = 1$, the multilinear Schatten-Hölder inequality $|\operatorname{Tr}(B_0 B_1 \cdots B_m)| \le \|B_0 B_1 \cdots B_m\|_1 \le \prod_{i=0}^m \|B_i\|_{r_i}$ ($\sum_i 1/r_i = 1$) gives
\[
\left|\operatorname{Tr}_{\mathcal{F}_{\rm el}(S)}\!\left(A_0\, e^{-\Delta_{K_{\rm tot}} D_{0,S}} A_{K_{\rm tot}} \cdots A_1 e^{-\Delta_0 D_{0,S}}\right)\right| \le \left(\prod_{j=0}^{K_{\rm tot}} \|A_j\|_{\rm op}\right) \prod_{j=0}^{K_{\rm tot}} \left\|e^{-\Delta_j D_{0,S}}\right\|_{\beta/\Delta_j}.
\]
For every $\Delta_j > 0$, positivity of $e^{-D_{0,S}}$ yields
\[
\left\|e^{-\Delta_j D_{0,S}}\right\|_{\beta/\Delta_j} = \left(\operatorname{Tr}_{\mathcal{F}_{\rm el}(S)}\!\left(\left(e^{-\Delta_j D_{0,S}}\right)^{\beta/\Delta_j}\right)\right)^{\Delta_j/\beta} = \left(\operatorname{Tr}_{\mathcal{F}_{\rm el}(S)}\!\left(e^{-\beta D_{0,S}}\right)\right)^{\Delta_j/\beta}.
\]
Multiplying over $j = 0, \dots, K_{\rm tot}$ and using $\sum_{j=0}^{K_{\rm tot}} \frac{\Delta_j}{\beta} = 1$ gives
\[
\prod_{j=0}^{K_{\rm tot}} \left\|e^{-\Delta_j D_{0,S}}\right\|_{\beta/\Delta_j} = \operatorname{Tr}_{\mathcal{F}_{\rm el}(S)}\!\left(e^{-\beta D_{0,S}}\right) = \prod_{x \in S} \operatorname{Tr}_{\mathcal{F}_{\rm el}(\{x\})}\!\left(e^{\beta\mu (n_{x\uparrow} + n_{x\downarrow})}\right) = z_0^{|S|}.
\]
Dividing both sides by $z_0^{|S|} > 0$ completes the proof. $\square$

---

## 5. Polymer Expansion, Exact Edge Activity Bound, and Proof of Theorem 1.1

### 5.1 Polymer Factorization of the Normalized Partition Function and Pair Correlator

Define the free reference partition function on $\Lambda_L$:
\[
Z_0(\Lambda_L) := \operatorname{Tr}_{\mathcal{H}_{\Lambda_L}}\!\left(e^{-\beta H_0}\right) = z_0^{|\Lambda_L|} Z_{\mathrm{ph},0}(\Lambda_L), \qquad z_0 = (1 + e^{\beta\mu})^2, \qquad Z_{\mathrm{ph},0}(\Lambda_L) = \left(2\sinh\frac{\beta\Omega}{2}\right)^{-|\mathcal{E}_{\Lambda_L}|},
\]
and the normalized partition function $\widetilde{Z}_{\Lambda_L}(\xi) := Z_{\Lambda_L}(\xi) / Z_0(\Lambda_L)$. Because subtracting $\log Z_0(\Lambda_L)$ shifts $\log Z_{\Lambda_L}(\xi)$ by a $\xi$-independent constant, $p_{\Lambda_L}(\xi) - p_{\Lambda_L}(0) = |\Lambda_L|^{-1}(\log \widetilde{Z}_{\Lambda_L}(\xi) - \log \widetilde{Z}_{\Lambda_L}(0))$.

Expand $\operatorname{Tr}(\mathcal{O}\, e^{-\beta H_{\Lambda_L}(\xi)})$ by Lemma 2.2 into its absolutely convergent Dyson series, where at each insertion time $u_j$ we choose either a $t$-insertion $-t T_b$ on a physical bond $b \in \mathcal{E}_{\Lambda_L}$, a $g$-insertion $g X_b T_b$ on a physical bond $b \in \mathcal{E}_{\Lambda_L}$, or a source insertion $-\xi Y_{e'}(\theta)$ on a source edge $e' \in \mathcal{E}_{\rm src}$. Every Dyson trajectory uses a finite set of edges $E = E_{\rm phys} \sqcup E_{\rm src} \subseteq \mathcal{E}_{\rm aug}$ (meaning each edge in $E$ appears at least once in the trajectory). Decompose $E$ into its connected components (polymers) $E = \bigsqcup_{\alpha=1}^m E_\alpha$ on the vertex set $\Lambda_L$, with pairwise disjoint vertex supports $S_{E_\alpha} \cap S_{E_{\alpha'}} = \emptyset$ ($\alpha \ne \alpha'$).

**Lemma 5.1 (Exact polymer factorization over vertex-disjoint supports, PROVED pending independent review).**
*For every collection of pairwise vertex-disjoint edge sets $E_1, \dots, E_m \subseteq \mathcal{E}_{\rm aug}$:*
1. *For $\mathcal{O} = I$, let $w(E)$ denote the sum/integral of all normalized Dyson trajectories whose set of used edges is exactly the connected nonempty edge set $E$, divided by $Z_0(\Lambda_L)$ (since unused sites and unused bond oscillators cancel against $z_0^{|\Lambda_L\setminus S_E|} Z_{\mathrm{ph},1}^{-|\mathcal{E}_{\Lambda_L}\setminus E_{\rm phys}|}$, $w(E)$ depends only on the subgraph $(S_E, E)$). Then*
   \[
   \widetilde{Z}_{\Lambda_L}(\xi) = 1 + \sum_{m=1}^\infty \frac{1}{m!} \sum_{\substack{(E_1, \dots, E_m) \\ E_\alpha \ne \emptyset \text{ connected} \\ S_{E_\alpha} \cap S_{E_{\alpha'}} = \emptyset}} \prod_{\alpha=1}^m w(E_\alpha).
   \]
2. *For $\xi = 0$ and $\mathcal{O} = \Delta_x^\dagger \Delta_y$ with $x \ne y \in \Lambda_L$, every nonzero trace in the Dyson expansion must connect $x$ and $y$ inside the same connected component $E_* \subseteq \mathcal{E}_{\Lambda_L}$ ($x, y \in S_{E_*}$), because $\Delta_x^\dagger = c_{x\uparrow}^\dagger c_{x\downarrow}^\dagger$ changes $(N_\uparrow, N_\downarrow)$ on $S_{E_*}$ by $(+1, +1)$ while $D_0$ and every $T_b$ conserve $(N_\uparrow, N_\downarrow)$ within each connected component. Letting $w_{xy}(E_*)$ denote the normalized activity of the marked component $E_* \ni x, y$ (with $\mathcal{O} = \Delta_x^\dagger \Delta_y$) and $\widetilde{Z}_{\Lambda_L \setminus S}(0)$ the polymer partition function restricted to polymers disjoint from $S \subseteq \Lambda_L$, we have*
   \[
   \langle \Delta_x^\dagger \Delta_y \rangle_{\Lambda_L} = \sum_{\substack{E_* \subseteq \mathcal{E}_{\Lambda_L} \text{ connected} \\ x, y \in S_{E_*}}} w_{xy}(E_*)\, \frac{\widetilde{Z}_{\Lambda_L \setminus S_{E_*}}(0)}{\widetilde{Z}_{\Lambda_L}(0)}.
   \]

*Proof.* By Lemma 4.1(4), every insertion operator $T_b$, $Y_{e'}(\theta)$, and $\Delta_x^\dagger \Delta_y$ is an even polynomial in the fermionic creation/annihilation operators, and $D_0 = \sum_{z \in \Lambda_L} (-\mu n_z)$ is a sum of single-site even operators. Operators that are even in fermions and supported on disjoint vertex sets $S_{E_\alpha} \cap S_{E_{\alpha'}} = \emptyset$ commute **identically** on $\mathcal{F}_{\rm el}(\Lambda_L)$ (no Jordan-Wigner strings cross between disjoint components), while bond oscillators on distinct edges $E_{\alpha,\mathrm{phys}} \cap E_{\alpha',\mathrm{phys}} = \emptyset$ act on independent tensor factors of $\mathcal{H}_{\rm ph}(\Lambda_L)$. Furthermore, integrating over the ordered global simplex $0 < u_1 < \dots < u_{K_{\rm tot}} < \beta$ and summing over all ways to interleave the ordered insertions of $E_1, \dots, E_m$ of lengths $K_1 + \dots + K_m = K_{\rm tot}$ equals the product of the independent simplex integrals over $0 < u_{1}^{(\alpha)} < \dots < u_{K_\alpha}^{(\alpha)} < \beta$ for $\alpha = 1, \dots, m$ (shuffle identity for simplices). This establishes (1) and (2). $\square$

### 5.2 Direct Dyson-Wick Activity Bound without Atomic Gap

**Proposition 5.2 (Polymer activity bound for pure bond-SSH, PROVED pending independent review).**
*Let $E = E_{\rm phys} \sqcup E_{\rm src} \subseteq \mathcal{E}_{\rm aug}$ be a connected nonempty edge set with $k = |E| = |E_{\rm phys}| + |E_{\rm src}| \ge 1$ edges and $v = |S_E| \le k + 1$ vertices. Then for all $(t, g, K, M, \mu, \beta, \xi)$:*
\[
|w(E)| \le \left(e^{2\beta|t| + 2\beta g^2/K} - 1\right)^{|E_{\rm phys}|} \left(e^{\beta|\xi|} - 1\right)^{|E_{\rm src}|},
\]
*and for $\xi = 0$ and $x \ne y \in S_E$ ($E = E_{\rm phys}$, $E_{\rm src} = \emptyset$), the marked activity $w_{xy}(E)$ satisfies*
\[
|w_{xy}(E)| \le \left(e^{2\beta|t| + 2\beta g^2/K} - 1\right)^{|E|}.
\]
*In particular, when $\beta|t| + \beta g^2/K \le c_0 = 2^{-10}$ and $|\xi| \le \xi_0 = 2^{-9}\beta^{-1}$ (so $2\beta|t| + 2\beta g^2/K \le 2^{-9}$ and $\beta|\xi| \le 2^{-9}$),*
\[
|w(E)| \le \varepsilon_{\rm phys}^{|E_{\rm phys}|} \varepsilon_{\rm src}^{|E_{\rm src}|} = \left(\frac{2}{1023}\right)^{|E|}, \qquad |w_{xy}(E)| \le \varepsilon_{\rm phys}^{|E|} = \left(\frac{2}{1023}\right)^{|E|}.
\]

*Proof.* Fix a connected edge set $E = E_{\rm phys} \sqcup E_{\rm src}$. Every Dyson trajectory using all edges of $E$ is specified by:
- for each physical edge $b \in E_{\rm phys}$, a multiplicity $m_b \ge 0$ of $t$-insertions ($-t T_b$) and a multiplicity $n_b \ge 0$ of $g$-insertions ($g X_b T_b$) such that $m_b + n_b \ge 1$;
- for each source edge $e' \in E_{\rm src}$, a multiplicity $p_{e'} \ge 1$ of source insertions ($-\xi Y_{e'}(\theta)$).

By Lemma 3.1(1), the phonon trace on bond $b \in E_{\rm phys}$ vanishes identically whenever $n_b$ is odd. Thus only even multiplicities $n_b = 2r_b$ ($r_b \ge 0$) with $m_b + 2r_b \ge 1$ (equivalently $m_b + r_b \ge 1$) contribute.

Fix a choice of multiplicities $\{m_b, 2r_b\}_{b \in E_{\rm phys}}$ ($m_b + r_b \ge 1$) and $\{p_{e'}\}_{e' \in E_{\rm src}}$ ($p_{e'} \ge 1$), and let
\[
K_{\rm tot} := \sum_{b \in E_{\rm phys}} (m_b + 2r_b) + \sum_{e' \in E_{\rm src}} p_{e'}.
\]
In the Dyson integral over the simplex $0 < u_1 < \dots < u_{K_{\rm tot}} < \beta$, we sum over all $\frac{K_{\rm tot}!}{\prod_{b \in E_{\rm phys}} (m_b!\, (2r_b)!) \prod_{e' \in E_{\rm src}} p_{e'}!}$ assignments of the $K_{\rm tot}$ time slots to the edge insertion types. For any fixed assignment and any $0 < u_1 < \dots < u_{K_{\rm tot}} < \beta$:
1. **Electronic trace bound:** By Lemma 4.1 ($\|T_b\|_{\rm op} = 2$, $\|Y_{e'}(\theta)\|_{\rm op} = 1$, $\|\mathcal{O}\|_{\rm op} = 1$ for $\mathcal{O} \in \{I, \Delta_x^\dagger \Delta_y\}$) and Lemma 4.2, the normalized electronic trace satisfies
   \[
   \frac{\left|\operatorname{Tr}_{\mathcal{F}_{\rm el}(S_E)}\!\left(\mathcal{O}\, e^{-\Delta_{K_{\rm tot}} D_{0,S_E}} A_{K_{\rm tot}} \cdots A_1 e^{-\Delta_0 D_{0,S_E}}\right)\right|}{z_0^{|S_E|}} \le \prod_{b \in E_{\rm phys}} (2|t|)^{m_b} (2|g|)^{2r_b} \prod_{e' \in E_{\rm src}} |\xi|^{p_{e'}},
   \]
   which depends **only on the multiplicities $\{m_b, r_b, p_{e'}\}$ and is independent of the time coordinates $u_1, \dots, u_{K_{\rm tot}}$ and of the ordering of insertions**.
2. **Phonon Wick factor:** Since bond oscillators on distinct edges $b \in E_{\rm phys}$ are independent, the normalized phonon trace factors over $b \in E_{\rm phys}$ into
   \[
   \prod_{b \in E_{\rm phys}} \sum_{\pi_b \in \mathcal{P}_2(2r_b)} \prod_{\{a,c\} \in \pi_b} C_\beta(|v_{b,a} - v_{b,c}|) > 0,
   \]
   where $0 < v_{b,1} < \dots < v_{b,2r_b} < \beta$ are the $2r_b$ time coordinates assigned to the $g$-insertions on bond $b$.
3. **Simplex-to-hypercube factorization:** Because the electronic bound in Step 1 is constant across all slot assignments and times while the phonon Wick factor in Step 2 is symmetric under permutation of the $2r_b$ coordinates of each bond $b$ (after summing over $\pi_b \in \mathcal{P}_2(2r_b)$) and independent of the $t$-insertion and source-insertion times, summing over all $\frac{K_{\rm tot}!}{\prod_b (m_b!\, (2r_b)!) \prod_{e'} p_{e'}!}$ slot assignments and integrating over the ordered simplex $0 < u_1 < \dots < u_{K_{\rm tot}} < \beta$ equals—by the multinomial simplex identity—the product of independent integrals over $[0, \beta]^{m_b}/m_b!$, $[0, \beta]^{2r_b}/(2r_b)!$, and $[0, \beta]^{p_{e'}}/p_{e'}!$:
   \[
   \prod_{b \in E_{\rm phys}} \left[\frac{(2\beta|t|)^{m_b}}{m_b!} \cdot \frac{(2|g|)^{2r_b}}{(2r_b)!} \sum_{\pi_b \in \mathcal{P}_2(2r_b)} \int_{[0,\beta]^{2r_b}} \prod_{\{a,c\} \in \pi_b} C_\beta(|v_{b,a} - v_{b,c}|)\, dv_{b,1}\cdots dv_{b,2r_b}\right] \prod_{e' \in E_{\rm src}} \frac{(\beta|\xi|)^{p_{e'}}}{p_{e'}!}.
   \]
4. **Evaluation of the hypercube Wick integral:** For each $b \in E_{\rm phys}$ and each pair partition $\pi_b \in \mathcal{P}_2(2r_b)$, the $2r_b$ coordinates split into $r_b$ disjoint pairs $\{a, c\} \in \pi_b$, so Fubini's theorem and Lemma 3.2 give
   \[
   \int_{[0,\beta]^{2r_b}} \prod_{\{a,c\} \in \pi_b} C_\beta(|v_{b,a} - v_{b,c}|)\, dv_{b,1}\cdots dv_{b,2r_b} = \left(\int_0^\beta \int_0^\beta C_\beta(|u - v|)\, du\, dv\right)^{r_b} = \left(\frac{\beta}{K}\right)^{r_b}.
   \]
   Since $|\mathcal{P}_2(2r_b)| = \frac{(2r_b)!}{2^{r_b} r_b!}$, the $g$-insertion factor for bond $b$ at multiplicity $2r_b$ equals
   \[
   \frac{(2|g|)^{2r_b}}{(2r_b)!} \cdot \frac{(2r_b)!}{2^{r_b} r_b!} \left(\frac{\beta}{K}\right)^{r_b} = \frac{1}{r_b!} \left(\frac{2\beta g^2}{K}\right)^{r_b}.
   \]
5. **Summation over multiplicities:** Summing over all $m_b \ge 0, r_b \ge 0$ with $m_b + r_b \ge 1$ independently for each $b \in E_{\rm phys}$, and over all $p_{e'} \ge 1$ independently for each $e' \in E_{\rm src}$, gives
   \[
   \sum_{\substack{m_b \ge 0,\, r_b \ge 0 \\ m_b + r_b \ge 1}} \frac{(2\beta|t|)^{m_b}}{m_b!} \frac{(2\beta g^2/K)^{r_b}}{r_b!} = \left(\sum_{m_b=0}^\infty \frac{(2\beta|t|)^{m_b}}{m_b!}\right)\left(\sum_{r_b=0}^\infty \frac{(2\beta g^2/K)^{r_b}}{r_b!}\right) - 1 = \exp\!\left(2\beta|t| + \frac{2\beta g^2}{K}\right) - 1,
   \]
   and $\sum_{p_{e'}=1}^\infty \frac{(\beta|\xi|)^{p_{e'}}}{p_{e'}!} = e^{\beta|\xi|} - 1$.
6. **Rational upper bound:** For every real $x \in [0, 2)$, the elementary factorial inequality $k! \ge 2^{k-1}$ ($\forall\, k \ge 1$) implies
   \[
   e^x - 1 = \sum_{k=1}^\infty \frac{x^k}{k!} \le \sum_{k=1}^\infty \frac{x^k}{2^{k-1}} = \frac{x}{1 - x/2}.
   \]
   With $x_{\rm phys} = 2\beta|t| + \frac{2\beta g^2}{K} \le 2c_0 = 2^{-9}$ and $x_{\rm src} = \beta|\xi| \le \beta\xi_0 = 2^{-9}$, both $e^{x_{\rm phys}} - 1$ and $e^{x_{\rm src}} - 1$ are bounded by $\frac{2^{-9}}{1 - 2^{-10}} = \frac{2}{1023} = \varepsilon_{\rm phys} = \varepsilon_{\rm src}$. $\square$

### 5.3 Self-Contained Graph Counting, Kotecký-Preiss Support Deletion, and Proof of Theorem 1.1

**Lemma 5.3 (Euler-tour connected edge-set counting bound, PROVED pending independent review).**
*Let $G = (V, \mathcal{E})$ be any graph (or multigraph) of maximum vertex degree $D_G$. For every vertex $x \in V$ and every integer $k \ge 1$, the number of connected edge subsets $E \subseteq \mathcal{E}$ of cardinality $|E| = k$ whose vertex support $S_E$ contains $x$ is at most $D_G^{2k}$.*

*Proof.* For any connected edge subset $E \subseteq \mathcal{E}$ with $|E| = k$ and $x \in S_E$, choose a spanning tree $T_E \subseteq E$ rooted at $x$. Fix a canonical ordering of the $\le D_G$ incident edge half-steps at every vertex of $V$. Performing a depth-first traversal of $T_E$ starting and ending at $x$ that traverses each edge of $T_E$ twice, and inserting at the first visit to each vertex $u \in S_E$ a back-and-forth step along each non-tree edge $e \in E \setminus T_E$ incident to $u$ (attributed to its first-visited endpoint), produces a closed walk on $G$ of length $2|T_E| + 2|E \setminus T_E| = 2k$ starting at $x$ whose set of traversed edges is $E$. Every step of a walk of length $2k$ starting at $x$ chooses one of at most $D_G$ incident edges at the current vertex, so there are at most $D_G^{2k}$ such walks, and the map $E \mapsto \text{walk}(E)$ is injective because $E$ is recovered as the set of traversed edges. $\square$

**Lemma 5.4 (Kotecký-Preiss support-deletion and zero-free analyticity bound, PROVED pending independent review).**
*Suppose the polymer activities $\{w(E)\}$ on $G = (\Lambda_L, \mathcal{E}_{\rm aug})$ satisfy, for some $b \in (0, 1)$,*
\[
\sup_{x \in \Lambda_L} \sum_{E \ni x} |w(E)|\, e^{|S_E|} \le b < 1.
\]
*Then for every subset $V \subseteq \Lambda_L$, the restricted polymer partition function $\widetilde{Z}_V := 1 + \sum_{m \ge 1} \frac{1}{m!} \sum_{E_1, \dots, E_m \subseteq V \text{ disjoint}} \prod_\alpha w(E_\alpha)$ is nonzero and satisfies, for every $S \subseteq V$,*
\[
\left|\frac{\widetilde{Z}_{V \setminus S}}{\widetilde{Z}_V}\right| \le e^{|S|}, \qquad \text{and for every } x \in V, \quad \left|\frac{\widetilde{Z}_V}{\widetilde{Z}_{V \setminus \{x\}}} - 1\right| \le \frac{b}{e} < \frac{1}{e}.
\]

*Proof.* We proceed by induction on $|V|$. For $|V| = 0$, $\widetilde{Z}_\emptyset = 1$. Assume the statement holds for all proper subsets of $V$, and pick $x \in V$. Partition the polymer configurations in $\widetilde{Z}_V$ into those where no polymer contains $x$ (which sum to $\widetilde{Z}_{V \setminus \{x\}} \ne 0$) and those where a unique polymer $E_1$ contains $x$ (and the remaining polymers lie in $V \setminus S_{E_1}$, summing to $\widetilde{Z}_{V \setminus S_{E_1}}$):
\[
\widetilde{Z}_V = \widetilde{Z}_{V \setminus \{x\}} + \sum_{\substack{E_1 \subseteq V \\ x \in S_{E_1}}} w(E_1)\, \widetilde{Z}_{V \setminus S_{E_1}} \implies \frac{\widetilde{Z}_V}{\widetilde{Z}_{V \setminus \{x\}}} - 1 = \sum_{\substack{E_1 \subseteq V \\ x \in S_{E_1}}} w(E_1)\, \frac{\widetilde{Z}_{V \setminus S_{E_1}}}{\widetilde{Z}_{V \setminus \{x\}}}.
\]
Applying the induction hypothesis to the subset $(V \setminus \{x\}) \setminus (S_{E_1} \setminus \{x\}) = V \setminus S_{E_1}$ inside $V \setminus \{x\}$ gives
\[
\left|\frac{\widetilde{Z}_{V \setminus S_{E_1}}}{\widetilde{Z}_{V \setminus \{x\}}}\right| \le e^{|S_{E_1} \setminus \{x\}|} = e^{|S_{E_1}| - 1}.
\]
Therefore,
\[
\left|\frac{\widetilde{Z}_V}{\widetilde{Z}_{V \setminus \{x\}}} - 1\right| \le \frac{1}{e} \sum_{E_1 \ni x} |w(E_1)|\, e^{|S_{E_1}|} \le \frac{b}{e} < \frac{1}{e}.
\]
Since $1 - \frac{1}{e} > 0$, we have $\widetilde{Z}_V \ne 0$ and
\[
\left|\frac{\widetilde{Z}_{V \setminus \{x\}}}{\widetilde{Z}_V}\right| \le \frac{1}{1 - b/e} < \frac{1}{1 - 1/e} < e,
\]
because $(1 - 1/e) e = e - 1 > 1.718 > 1$. Telescoping over the vertices of $S = \{x_1, \dots, x_{|S|}\}$ yields $|\widetilde{Z}_{V \setminus S} / \widetilde{Z}_V| \le e^{|S|}$, completing the induction. $\square$

*Proof of Theorem 1.1.* Assume $\beta|t| + \beta g^2/K \le c_0 = 2^{-10}$.
1. **Grand-canonical pair clustering ($\xi = 0$, $D = 4$, $D^2 = 16$):**
   For every connected edge set $E \subseteq \mathcal{E}_{\Lambda_L}$ with $|E| = k \ge 1$, connectivity implies $|S_E| \le k + 1$. Using $e < 3$, Proposition 5.2, and Lemma 5.3 with $D_G = D = 4$, we bound the Kotecký-Preiss sum at any vertex $x \in \Lambda_L$:
   \[
   \sum_{E \ni x} |w(E)|\, e^{|S_E|} \le \sum_{k=1}^\infty 16^k \varepsilon_{\rm phys}^k 3^{k+1} = 3 \sum_{k=1}^\infty (48 \varepsilon_{\rm phys})^k = \frac{3 q_{\rm GC}}{1 - q_{\rm GC}} = b_{\rm GC} = \frac{32}{103} < 1,
   \]
   where $q_{\rm GC} = 48 \varepsilon_{\rm phys} = 48 \cdot \frac{2}{1023} = \frac{32}{341} < 1$. By Lemma 5.4, $\widetilde{Z}_{\Lambda_L}(0) \ne 0$ and $|\widetilde{Z}_{\Lambda_L \setminus S_{E_*}}(0) / \widetilde{Z}_{\Lambda_L}(0)| \le e^{|S_{E_*}|}$. For any $x \ne y \in \Lambda_L$, every connected edge set $E_*$ with $x, y \in S_{E_*}$ contains a path between $x$ and $y$, so $|E_*| = k \ge d_{\Lambda_L}(x,y)$. By Lemma 5.1(2) and Proposition 5.2,
   \[
   \left|\langle \Delta_x^\dagger \Delta_y \rangle_{\Lambda_L}\right| \le \sum_{\substack{E_* \text{ connected} \\ x, y \in S_{E_*}}} |w_{xy}(E_*)|\, e^{|S_{E_*}|} \le \sum_{k = d_{\Lambda_L}(x,y)}^\infty 16^k \varepsilon_{\rm phys}^k 3^{k+1} = \frac{3}{1 - q_{\rm GC}} q_{\rm GC}^{d_{\Lambda_L}(x,y)} = A_{\rm GC} q_{\rm GC}^{d_{\Lambda_L}(x,y)}.
   \]
   For $y = x$, $\Delta_x^\dagger \Delta_x = n_{x\uparrow} n_{x\downarrow}$ has eigenvalues in $\{0, 1\}$, so $|\langle \Delta_x^\dagger \Delta_x \rangle_{\Lambda_L}| \le 1$. On the 2D torus $\Lambda_L$, the distance shell $\{y \in \Lambda_L : d_{\Lambda_L}(x,y) = d\}$ ($d \ge 1$) contains at most $4d$ vertices, so
   \[
   \sup_{x \in \Lambda_L} \sum_{y \in \Lambda_L} \left|\langle \Delta_x^\dagger \Delta_y \rangle_{\Lambda_L}\right| \le 1 + A_{\rm GC} \sum_{d=1}^\infty 4d\, q_{\rm GC}^d = 1 + \frac{4 A_{\rm GC} q_{\rm GC}}{(1 - q_{\rm GC})^2} = R_{\rm max} = \frac{24718511}{9834543} < 3.
   \]
2. **Source-augmented analyticity and quadratic remainder ($|\xi| \le \xi_0 = 2^{-9}\beta^{-1}$, $D_{\rm aug} = 6$, $D_{\rm aug}^2 = 36$):**
   For every complex $\xi \in \mathbb{C}$ with $|\xi| \le \xi_0$, Proposition 5.2 and Lemma 5.3 with $D_G = D_{\rm aug} = 6$ give
   \[
   \sup_{x \in \Lambda_L} \sum_{E \ni x} |w(E)|\, e^{|S_E|} \le 3 \sum_{k=1}^\infty \left(36 \cdot 3 \max(\varepsilon_{\rm phys}, \varepsilon_{\rm src})\right)^k = \frac{3 q_{\rm src}}{1 - q_{\rm src}} = b_{\rm src} = \frac{216}{269} < 1,
   \]
   where $q_{\rm src} = 108 \cdot \frac{2}{1023} = \frac{72}{341} < 1$. Order the vertices of $\Lambda_L$ as $x_1, \dots, x_{|\Lambda_L|}$ and set $V_j := \{x_j, \dots, x_{|\Lambda_L|}\}$ ($V_1 = \Lambda_L$, $V_{|\Lambda_L|+1} = \emptyset$). By Lemma 2.1 and Lemma 5.4, $\widetilde{Z}_{\Lambda_L}(\xi) = \prod_{j=1}^{|\Lambda_L|} \frac{\widetilde{Z}_{V_j}(\xi)}{\widetilde{Z}_{V_{j+1}}(\xi)}$ is a finite product of entire functions of $\xi$, each satisfying $\left|\frac{\widetilde{Z}_{V_j}(\xi)}{\widetilde{Z}_{V_{j+1}}(\xi)} - 1\right| \le \frac{b_{\rm src}}{e} < \frac{1}{e}$ on $|\xi| \le \xi_0$. Thus $\widetilde{Z}_{\Lambda_L}(\xi)$ is zero-free on $|\xi| \le \xi_0$, and $p_{\Lambda_L}(\xi) - p_{\Lambda_L}(0) = |\Lambda_L|^{-1} \log \widetilde{Z}_{\Lambda_L}(\xi) - |\Lambda_L|^{-1} \log \widetilde{Z}_{\Lambda_L}(0)$ is analytic on $|\xi| < \xi_0$ with uniform modulus bound on $|\xi| \le \xi_0$:
   \[
   |p_{\Lambda_L}(\xi) - p_{\Lambda_L}(0)| \le \frac{1}{|\Lambda_L|} \sum_{j=1}^{|\Lambda_L|} \left(\left|\log\frac{\widetilde{Z}_{V_j}(\xi)}{\widetilde{Z}_{V_{j+1}}(\xi)}\right| + \left|\log\frac{\widetilde{Z}_{V_j}(0)}{\widetilde{Z}_{V_{j+1}}(0)}\right|\right) \le -2\log\!\left(1 - \frac{b_{\rm src}}{e}\right) < 2,
   \]
   since $\frac{b_{\rm src}}{e} < \frac{1}{e} < \frac{1}{2}$ and $-2\log(1 - 1/2) = 2\log 2 < 2$. By Cauchy's integral formula on $|\xi| = \xi_0$, for all real $\xi \in [0, \xi_0/2]$ the Taylor remainder of order $\ge 2$ satisfies
   \[
   \left|p_{\Lambda_L}(\xi) - p_{\Lambda_L}(0) - p_{\Lambda_L}'(0)\xi\right| \le \sum_{m=2}^\infty \frac{2}{\xi_0^m} \xi^m = \frac{2\xi^2}{\xi_0(\xi_0 - \xi)} \le \frac{4\xi^2}{\xi_0^2}.
   \]
   Finally, by translation invariance of $H_{\Lambda_L}(0)$ on $\Lambda_L$,
   \[
   p_{\Lambda_L}'(0) = \frac{\beta}{|\Lambda_L|} \sum_{x \in \Lambda_L} \langle Y_{e'_x}(\theta) \rangle_{\Lambda_L} = 2\beta \operatorname{Re}\!\left(e^{i\theta} \langle \Delta_0^\dagger \Delta_r \rangle_{\Lambda_L}\right) \le 2\beta A_{\rm GC} q_{\rm GC}^{d_{\Lambda_L}(0,r)}.
   \]
   Combining $p_{\Lambda_L}'(0)\xi$ with the quadratic remainder bound $4\xi^2/\xi_0^2$ completes the proof of Theorem 1.1. $\square$

---

## 6. Canonical Transfer with Unbounded Boundary SSH Hopping (Proof of Theorem 1.2)

Because the bond-SSH hopping $(-t + g X_b) T_b$ across block boundaries is an **unbounded** operator on $\mathcal{H}_{\Lambda_L}$, we use the oscillator spring-constant splitting bracket from `SSHBOUND3` Lemma 6.1, which requires only $K > 0$ and is completely independent of $U_{\rm eff}$.

**Lemma 6.1 (Unbounded boundary SSH log-partition bracket at $U_{\rm eff} = 0$, PROVED pending independent review and CERTIFIED).**
*Partition $\Lambda_L$ into rectangular blocks $\{B_\alpha\}_{\alpha=1}^{N_{\rm blk}}$ of side lengths in $[b, 2b-1]$ ($b \ge 2$), and let $\partial \subseteq \mathcal{E}_{\Lambda_L}$ (resp. $\partial_{\rm src} \subseteq \mathcal{E}_{\rm src}$) be the set of physical bonds (resp. source edges) with endpoints in different blocks. Define the block-decoupled Hamiltonian with modified boundary spring constant $K' > 0$:*
\[
H_{\rm blk}(\xi; K') := \sum_{\alpha=1}^{N_{\rm blk}} H_{B_\alpha}(\xi) + \sum_{b \in \partial} H_{\mathrm{ph},b}(K'), \qquad H_{\mathrm{ph},b}(K') := \frac{P_b^2}{2M} + \frac{K'}{2} X_b^2,
\]
*where $H_{B_\alpha}(\xi)$ retains only vertices, physical bonds, and source edges internal to $B_\alpha$. Then for every real $\xi \in \mathbb{R}$, in both the grand-canonical trace and every fixed total-number sector $N$ or spin-number sector $(N_\uparrow, N_\downarrow)$,*
\[
\left|\log Z_{\Lambda_L}(\xi) - \log Z_{\rm blk}(\xi; K)\right| \le C_{\rm bdry} |\partial| + \beta|\xi|\, |\partial_{\rm src}|,
\]
*where $Z_{\mathrm{ph},1}(K') = \left(2\sinh(\frac{\beta}{2}\sqrt{K'/M})\right)^{-1}$ and*
\[
C_{\rm bdry} := \beta\left(2|t| + \frac{4g^2}{K}\right) + \max\!\left(\log\frac{Z_{\mathrm{ph},1}(K/2)}{Z_{\mathrm{ph},1}(K)},\; \log\frac{Z_{\mathrm{ph},1}(K)}{Z_{\mathrm{ph},1}(2K)}\right) < \infty.
\]

*Proof.* On each boundary physical bond $b \in \partial$, Lemma 4.1 gives $\|T_b\|_{\rm op} = 2$. By Young's inequality $2|g||X_b| \le \frac{K}{4} X_b^2 + \frac{4g^2}{K}$, we have as quadratic forms on $\mathcal{D}(H_0)$ (and on every fixed-$N$ or fixed-$(N_\uparrow, N_\downarrow)$ sector, since $T_b$ and $X_b$ commute with $N_\uparrow, N_\downarrow$):
\[
-\frac{K}{4} X_b^2 - \left(2|t| + \frac{4g^2}{K}\right) I \le (-t + g X_b) T_b \le \frac{K}{4} X_b^2 + \left(2|t| + \frac{4g^2}{K}\right) I.
\]
Combining this with the boundary oscillator potential $\frac{K}{2} X_b^2$ gives
\[
\frac{K/2}{2} X_b^2 = \frac{K}{2} X_b^2 - \frac{K}{4} X_b^2, \qquad \frac{K}{2} X_b^2 + \frac{K}{4} X_b^2 = \frac{3K}{4} X_b^2 \le \frac{2K}{2} X_b^2.
\]
Since $\|Y_{e'}(\theta)\|_{\rm op} = 1$ for $e' \in \partial_{\rm src}$, summing over $b \in \partial$ and $e' \in \partial_{\rm src}$ yields the operator inequality on $\mathcal{D}(H_0)$:
\[
H_{\rm blk}(\xi; K/2) - |\partial|\left(2|t| + \frac{4g^2}{K}\right) - |\xi||\partial_{\rm src}| \le H_{\Lambda_L}(\xi) \le H_{\rm blk}(\xi; 2K) + |\partial|\left(2|t| + \frac{4g^2}{K}\right) + |\xi||\partial_{\rm src}|.
\]
By min-max eigenvalue monotonicity for self-adjoint operators with compact resolvent (which applies in each fixed-$N$ or fixed-$(N_\uparrow, N_\downarrow)$ subspace as well as on $\mathcal{H}_{\Lambda_L}$),
\[
\log Z_{\rm blk}(\xi; 2K) - E_{\rm bdry} \le \log Z_{\Lambda_L}(\xi) \le \log Z_{\rm blk}(\xi; K/2) + E_{\rm bdry}, \qquad E_{\rm bdry} := \beta|\partial|\left(2|t| + \frac{4g^2}{K}\right) + \beta|\xi||\partial_{\rm src}|.
\]
Because the boundary oscillators $\sum_{b \in \partial} H_{\mathrm{ph},b}(K')$ act on tensor factors decoupled from all blocks $B_\alpha$ and commute with $N_\uparrow, N_\downarrow$, their partition functions factor out identically in every sector:
\[
\frac{Z_{\rm blk}(\xi; K/2)}{Z_{\rm blk}(\xi; K)} = \left(\frac{Z_{\mathrm{ph},1}(K/2)}{Z_{\mathrm{ph},1}(K)}\right)^{|\partial|}, \qquad \frac{Z_{\rm blk}(\xi; K)}{Z_{\rm blk}(\xi; 2K)} = \left(\frac{Z_{\mathrm{ph},1}(K)}{Z_{\mathrm{ph},1}(2K)}\right)^{|\partial|}.
\]
Taking logarithms completes the proof. $\square$

*Proof of Theorem 1.2.* Fix $(t, g, K, M, \beta)$ satisfying $\beta|t| + \beta g^2/K \le 2^{-10}$ and a nonzero displacement $r \in \mathbb{Z}^2 \setminus \{0\}$. Divide both $Z_{\Lambda_L}(\xi; \mu)$ and the canonical partition function $Z_{\Lambda_L, N}(\xi) := \operatorname{Tr}_{\mathcal{H}_{\Lambda_L, N}}(e^{-\beta(H_{\Lambda_L}(\xi) + \mu N)})$ by the free phonon partition function $Z_{\mathrm{ph},0}(\Lambda_L) = Z_{\mathrm{ph},1}(K)^{|\mathcal{E}_{\Lambda_L}|}$, defining $\widehat{Z}_{\Lambda_L}(\xi; \mu) := Z_{\Lambda_L}(\xi; \mu)/Z_{\mathrm{ph},0}(\Lambda_L)$ and $\widehat{Z}_{\Lambda_L, N}(\xi) := Z_{\Lambda_L, N}(\xi)/Z_{\mathrm{ph},0}(\Lambda_L)$. Note that $p_{\Lambda_L}(\xi) - p_{\Lambda_L}(0) = |\Lambda_L|^{-1}(\log \widehat{Z}_{\Lambda_L}(\xi; \mu) - \log \widehat{Z}_{\Lambda_L}(0; \mu))$.
1. **Existence and concavity of the canonical free-energy density:** By Lemma 6.1 at $\xi = 0$, for any block decomposition of $\Lambda_L$ into $N_{\rm blk}$ blocks of side $\in [b, 2b-1]$ (where $|\partial| \le \frac{4}{b}|\Lambda_L|$), distributing $N$ particles among the $N_{\rm blk}$ blocks has at most $(2(2b)^2 + 1)^{N_{\rm blk}} \le (8b^2 + 1)^{|\Lambda_L|/b^2}$ choices (and $(4b^2 + 1)^{2|\Lambda_L|/b^2}$ in the spin-balanced sector). Thus $\log \widehat{Z}_{\Lambda_L, N}(0)$ is superadditive across blocks up to $C_{\rm bdry}|\partial| + O(\frac{\log b}{b^2})|\Lambda_L| = O(b^{-1})|\Lambda_L|$. By standard subadditive/superadditive convergence on $\mathbb{Z}^2$, as $L_j \to \infty$ with $N_j / L_j^2 \to n \in [0, 2]$, the canonical pressure density $f_{\rm can}(n) := \lim_{j \to \infty} L_j^{-2} \log \widehat{Z}_{\Lambda_{L_j}, N_j}(0)$ exists, is continuous and concave on $[0, 2]$, and satisfies the Legendre duality relation
   \[
   \lim_{L \to \infty} \frac{1}{L^2} \log \widehat{Z}_{\Lambda_L}(0; \mu) = \sup_{n \in [0, 2]} \left\{f_{\rm can}(n) + \beta\mu n\right\} \qquad (\forall\, \mu \in \mathbb{R}).
   \]
2. **Legendre supporting chemical potential and Griffith-type derivative bound:** For any interior density $n \in (0, 2)$ (or balanced interior spin density $(a, a)$ with $a \in (0, 1)$, where spin-flip symmetry $N_\uparrow \leftrightarrow N_\downarrow$ ensures a spin-symmetric supporting chemical potential $\mu_\uparrow = \mu_\downarrow = \mu$), concavity of $f_{\rm can}$ on $[0, 2]$ guarantees the existence of a supporting slope $-\beta\mu \in \mathbb{R}$ such that $f_{\rm can}(n) + \beta\mu n = \sup_{n' \in [0,2]}\{f_{\rm can}(n') + \beta\mu n'\}$. Define the nonnegative finite-volume Legendre discrepancy
   \[
   \delta_{L_j} := \frac{1}{L_j^2}\left(\log \widehat{Z}_{\Lambda_{L_j}}(0; \mu) - \log \widehat{Z}_{\Lambda_{L_j}, N_j}(0) - \beta\mu N_j\right) \ge 0,
   \]
   which satisfies $\lim_{j \to \infty} \delta_{L_j} = 0$. Since $\widehat{Z}_{\Lambda_{L_j}}(\xi; \mu) = \sum_{N=0}^{2L_j^2} e^{\beta\mu N} \widehat{Z}_{\Lambda_{L_j}, N}(\xi) \ge e^{\beta\mu N_j} \widehat{Z}_{\Lambda_{L_j}, N_j}(\xi)$ for all real $\xi$, we have for all $\xi \in (0, \xi_0/2]$:
   \[
   \frac{1}{L_j^2}\left(\log \widehat{Z}_{\Lambda_{L_j}, N_j}(\xi) - \log \widehat{Z}_{\Lambda_{L_j}, N_j}(0)\right) \le p_{\Lambda_{L_j}}(\xi) - p_{\Lambda_{L_j}}(0) + \delta_{L_j}.
   \]
   Because $H_{\Lambda_{L_j}}(\xi)$ is linear in $\xi$ and self-adjoint for real $\xi$, $\xi \mapsto \log \widehat{Z}_{\Lambda_{L_j}, N_j}(\xi)$ is convex on $\mathbb{R}$ (by Hölder's inequality for traces), so its derivative at $\xi = 0$ is bounded above by the difference quotient at $\xi \in (0, \xi_0/2]$:
   \[
   2\beta \operatorname{Re}\!\left(e^{i\theta} \langle \Delta_0^\dagger \Delta_r \rangle_{L_j, \mathrm{can}}\right) = \left.\frac{d}{d\xi}\right|_{\xi=0} \frac{1}{L_j^2} \log \widehat{Z}_{\Lambda_{L_j}, N_j}(\xi) \le \frac{p_{\Lambda_{L_j}}(\xi) - p_{\Lambda_{L_j}}(0)}{\xi} + \frac{\delta_{L_j}}{\xi}.
   \]
   Applying Theorem 1.1 (which holds uniformly for all $\mu \in \mathbb{R}$, including the supporting $\mu$) gives
   \[
   2\beta \operatorname{Re}\!\left(e^{i\theta} \langle \Delta_0^\dagger \Delta_r \rangle_{L_j, \mathrm{can}}\right) \le 2\beta A_{\rm GC} q_{\rm GC}^{d_{\Lambda_{L_j}}(0,r)} + \frac{4\xi}{\xi_0^2} + \frac{\delta_{L_j}}{\xi}.
   \]
   Taking $\limsup_{j \to \infty}$ at fixed $\xi \in (0, \xi_0/2]$ (using $\delta_{L_j} \to 0$ and $d_{\Lambda_{L_j}}(0,r) = \|r\|_1$ for $L_j > 2\|r\|_1$), then letting $\xi \downarrow 0$ and optimizing over $\theta \in [0, 2\pi)$ yields Theorem 1.2. $\square$

---

## 7. Proved Route Obstructions at $U_{\rm eff} = 0$ (Proof of Theorem 1.3)

### 7.1 Obstruction to Route (b): Zero Instantaneous Atomic Pairing Gap on $C_4$

**Proposition 7.1 (Zero phonon-induced atomic gap in the antiadiabatic pure bond-SSH model, PROVED pending independent review and CERTIFIED).**
*In the antiadiabatic limit $\Omega \to \infty$ at fixed $g, K > 0$ and $t = 0, \mu = 0$, completing the square in the bond oscillator coordinates $H_{\mathrm{ph},b} + g X_b T_b = \frac{P_b^2}{2M} + \frac{K}{2}(X_b + \frac{g}{K} T_b)^2 - \frac{g^2}{2K} T_b^2$ yields the exact instantaneous two-body electronic Hamiltonian*
\[
H_{\rm eff}^{\rm inst} := -\frac{g^2}{2K} \sum_{b \in \mathcal{E}_\Lambda} T_b^2.
\]
*On the 4-site ring $C_4$ ($\mathcal{E}_{C_4} = \{\{0,1\}, \{1,2\}, \{2,3\}, \{3,0\}\}$) at half-filling $N = 4$ ($\dim \mathcal{F}_{\rm el}(C_4)|_{N=4} = \binom{8}{4} = 70$, with spin-balanced subspace $\{N_\uparrow = N_\downarrow = 2\}$ of dimension $\binom{4}{2}^2 = 36$):*
1. *Every bond operator $T_b^2$ preserves $(N_\uparrow, N_\downarrow)$ and the local parity $(-1)^{n_x}$ at every site $x \in C_4$, and hence commutes with $N_{\rm odd} := \sum_{x=0}^3 (n_{x\uparrow} - n_{x\downarrow})^2 \in \{0, 2, 4\}$.*
2. *In the purely paired sector $\{N_\uparrow = 2, N_\downarrow = 2, N_{\rm odd} = 0\}$ (dimension $\binom{4}{2} = 6$, which is the entire $\{N = 4, N_{\rm odd} = 0\}$ subspace), the operator $\Sigma_4 := \sum_{b \in \mathcal{E}_{C_4}} T_b^2$ has exact spectrum $\{0, 4, 4, 4, 8, 12\}$ and maximum eigenvalue $\lambda_{\max}(\Sigma_4|_{N=4, N_{\rm odd}=0}) = 12$.*
3. *In the fully singly occupied spin-balanced sector $\{N_\uparrow = 2, N_\downarrow = 2, N_{\rm odd} = 4\}$ (dimension $\binom{4}{2} = 6$), $\Sigma_4$ also has exact spectrum $\{0, 4, 4, 4, 8, 12\}$ and maximum eigenvalue $\lambda_{\max}(\Sigma_4|_{N_\uparrow=N_\downarrow=2, N_{\rm odd}=4}) = 12$.*
4. *In all remaining sectors of $\{N = 4, N_{\rm odd} > 0\}$, the maximum eigenvalue of $\Sigma_4$ is strictly smaller than $12$:*
   - *On $\{N_\uparrow = 2, N_\downarrow = 2, N_{\rm odd} = 2\}$ (dimension $24$), $\operatorname{spec}(\Sigma_4) = \{2, 4, 6, 10\}$ so $\lambda_{\max} = 10 < 12$;*
   - *On $\{N_\uparrow = 3, N_\downarrow = 1, N_{\rm odd} = 4\}$ and $\{N_\uparrow = 1, N_\downarrow = 3, N_{\rm odd} = 4\}$ (dimension $4$ each), $\operatorname{spec}(\Sigma_4) = \{0, 4, 4, 8\}$ so $\lambda_{\max} = 8 < 12$;*
   - *On $\{N_\uparrow = 3, N_\downarrow = 1, N_{\rm odd} = 2\}$ and $\{N_\uparrow = 1, N_\downarrow = 3, N_{\rm odd} = 2\}$ (dimension $12$ each), $\operatorname{spec}(\Sigma_4) = \{2, 4, 6\}$ so $\lambda_{\max} = 6 < 12$;*
   - *On $\{N_\uparrow = 4, N_\downarrow = 0, N_{\rm odd} = 4\}$ and $\{N_\uparrow = 0, N_\downarrow = 4, N_{\rm odd} = 4\}$ (dimension $1$ each), $\Sigma_4 = 0$ so $\lambda_{\max} = 0 < 12$.*
5. *Consequently, across both the spin-balanced space $\{N_\uparrow = N_\downarrow = 2\}$ and the full half-filled space $\{N = 4\}$, $\max\operatorname{spec}(\Sigma_4|_{N_{\rm odd}>0}) = \max\{12, 10, 8, 6, 0\} = 12 = \max\operatorname{spec}(\Sigma_4|_{N_{\rm odd}=0})$, so $\min \operatorname{spec}(H_{\rm eff}^{\rm inst}|_{N=4, N_{\rm odd}=0}) = \min \operatorname{spec}(H_{\rm eff}^{\rm inst}|_{N=4, N_{\rm odd}>0}) = -6 \frac{g^2}{K}$ and the phonon-induced instantaneous gap between $N_{\rm odd} = 0$ and $N_{\rm odd} > 0$ is identically zero:*
   \[
   \Delta_{\rm eff} := \min \operatorname{spec}\!\left(H_{\rm eff}^{\rm inst}\big|_{N=4,\, N_{\rm odd} > 0}\right) - \min \operatorname{spec}\!\left(H_{\rm eff}^{\rm inst}\big|_{N=4,\, N_{\rm odd} = 0}\right) = 0.
   \]

*Proof.*
1. For a bond $b = \{x, y\}$, expand $T_b^2 = (h_{b,\uparrow} + h_{b,\downarrow})^2 = h_{b,\uparrow}^2 + h_{b,\downarrow}^2 + 2 h_{b,\uparrow} h_{b,\downarrow}$. By Lemma 4.1(1), $h_{b,\sigma}^2 = (n_{x\sigma} - n_{y\sigma})^2$ is diagonal in the occupation basis and therefore commutes with every $n_{z\tau}$. Meanwhile, $2 h_{b,\uparrow} h_{b,\downarrow} = 2(c_{x\uparrow}^\dagger c_{y\uparrow} + c_{y\uparrow}^\dagger c_{x\uparrow})(c_{x\downarrow}^\dagger c_{y\downarrow} + c_{y\downarrow}^\dagger c_{x\downarrow})$ transfers both an $\uparrow$-electron and a $\downarrow$-electron simultaneously between $x$ and $y$, changing $n_x$ and $n_y$ by $\pm 2$ or $0$. Thus $(-1)^{n_z}$ and $n_{z,\mathrm{odd}} = n_z \bmod 2$ are conserved at every site $z$, so $[T_b^2, N_{\rm odd}] = 0$.
2. In the sector $\{N_\uparrow = 2, N_\downarrow = 2, N_{\rm odd} = 0\}$, every site is either doubly occupied ($d_x^\dagger |0\rangle := \Delta_x^\dagger |0\rangle$) or empty. For $b = \{x, y\}$, acting on states with $n_{x,\mathrm{odd}} = n_{y,\mathrm{odd}} = 0$, $h_{b,\sigma}^2$ equals $1$ if exactly one of $\{x, y\}$ is doubly occupied and $0$ otherwise, while $2 h_{b,\uparrow} h_{b,\downarrow} = -2(d_x^\dagger d_y + d_y^\dagger d_x)$ (since $c_{x\uparrow}^\dagger c_{y\uparrow} c_{x\downarrow}^\dagger c_{y\downarrow} = -c_{x\uparrow}^\dagger c_{x\downarrow}^\dagger c_{y\uparrow} c_{y\downarrow} = -d_x^\dagger d_y$). In the 6-state hard-core pair basis $\{|01\rangle, |02\rangle, |03\rangle, |12\rangle, |13\rangle, |23\rangle\}$ (where $|ij\rangle := d_i^\dagger d_j^\dagger |0\rangle$), the four adjacent pair states $|01\rangle, |12\rangle, |23\rangle, |03\rangle$ have 2 active bonds (diagonal $\Sigma_4$ entry $2 \times 2 = 4$) and the two antipodal pair states $|02\rangle, |13\rangle$ have 4 active bonds (diagonal $\Sigma_4$ entry $4 \times 2 = 8$). Each active bond hop connects an adjacent state to an antipodal state with matrix element $-2$ (or $+2$ under the bipartite gauge $d_x^\dagger \mapsto (-1)^x d_x^\dagger$), giving the exact $6 \times 6$ integer matrix (after $d_x^\dagger \mapsto (-1)^x d_x^\dagger$):
   \[
   M_{\rm even} = \begin{pmatrix}
   4 & 2 & 0 & 0 & 2 & 0 \\
   2 & 8 & 2 & 2 & 0 & 2 \\
   0 & 2 & 4 & 0 & 2 & 0 \\
   0 & 2 & 0 & 4 & 2 & 0 \\
   2 & 0 & 2 & 2 & 8 & 2 \\
   0 & 2 & 0 & 0 & 2 & 4
   \end{pmatrix}.
   \]
   Direct integer matrix-vector multiplication gives $M_{\rm even} v_{\rm even} = 12 v_{\rm even}$ for $v_{\rm even} = (1, 2, 1, 1, 2, 1)^{\rm T}$, and exact polynomial evaluation verifies $M_{\rm even}(M_{\rm even} - 4I)(M_{\rm even} - 8I)(M_{\rm even} - 12I) = 0$ (eigenvalues $\{0, 4, 4, 4, 8, 12\}$, **CERTIFIED** in `replay.py`). Thus $\lambda_{\max}(M_{\rm even}) = 12$.
3. In the sector $\{N_\uparrow = 2, N_\downarrow = 2, N_{\rm odd} = 4\}$, every site of $C_4$ is singly occupied with spin $\sigma_x \in \{\uparrow, \downarrow\}$. On any bond $b = \{x, y\}$ between singly occupied sites, $T_b^2$ acts as $0$ on spin-parallel states $|\uparrow\uparrow\rangle, |\downarrow\downarrow\rangle$ and acts as $2(I - P_{xy})$ on antiparallel states $|\uparrow\downarrow\rangle, |\downarrow\uparrow\rangle$, where $P_{xy}$ swaps the spins at $x$ and $y$; that is, $\frac{1}{4} T_b^2 = \frac{1}{2}(I - P_{xy}) = \frac{1}{4} - \mathbf{S}_x \cdot \mathbf{S}_y$ is twice the spin-$\frac{1}{2}$ singlet projector on bond $b$. On the 4-site spin-$\frac{1}{2}$ Heisenberg ring $C_4$, $\sum_{b \in \mathcal{E}_{C_4}} (\mathbf{S}_x \cdot \mathbf{S}_y - \frac{1}{4}) = \frac{1}{2}(\mathbf{S}_{02}^2 + \mathbf{S}_{13}^2 - \mathbf{S}_{\rm tot}^2) - \mathbf{S}_{02} \cdot \mathbf{S}_{13} - 1$ achieves its minimum $-3$ on the unique total-spin singlet state ($S_{\rm tot} = 0$, $S_{02} = S_{13} = 1$), so $\Sigma_4 = 4 \sum_{b \in \mathcal{E}_{C_4}} (\frac{1}{4} - \mathbf{S}_x \cdot \mathbf{S}_y)$ achieves maximum eigenvalue $4 \times 3 = 12$ on the explicit integer eigenvector $v_{\rm odd} = (1, -2, 1, 1, -2, 1)^{\rm T}$ in the 6-state $S^z = 0$ basis (**CERTIFIED** in `replay.py`), with spectrum $\{0, 4, 4, 4, 8, 12\}$ identical to $M_{\rm even}$.
4. For the polarized $N_{\rm odd} = 4$ sectors $(N_\uparrow, N_\downarrow) \in \{(3,1), (1,3)\}$ (dimension $4$ each, $S^z = \pm 1$), total spin satisfies $S_{\rm tot} \ge |S^z| = 1$, which excludes the $S_{\rm tot} = 0$ singlet and restricts the Heisenberg operator $\Sigma_4$ to its $S_{\rm tot} \in \{1, 2\}$ eigenvalues $\{0, 4, 4, 8\}$, satisfying the exact integer polynomial identity $\Sigma_4(\Sigma_4 - 4I)(\Sigma_4 - 8I) = 0$ (**CERTIFIED** in `replay.py`). For $(N_\uparrow, N_\downarrow) \in \{(4,0), (0,4)\}$ (dimension $1$ each), Pauli exclusion gives $T_b = 0$ for every bond $b$, so $\Sigma_4 = 0$. Finally, on the partially paired $N_{\rm odd} = 2$ sectors—namely $\{N_\uparrow = N_\downarrow = 2, N_{\rm odd} = 2\}$ of dimension $24$ and $\{N_\uparrow = 3, N_\downarrow = 1, N_{\rm odd} = 2\} \oplus \{N_\uparrow = 1, N_\downarrow = 3, N_{\rm odd} = 2\}$ of dimension $12 + 12$—exact integer matrix multiplication over the restricted occupation bases verifies $(\Sigma_4 - 2I)(\Sigma_4 - 4I)(\Sigma_4 - 6I)(\Sigma_4 - 10I) = 0$ on the 24-dimensional sector ($\lambda_{\max} = 10 < 12$) and $(\Sigma_4 - 2I)(\Sigma_4 - 4I)(\Sigma_4 - 6I) = 0$ on each 12-dimensional sector ($\lambda_{\max} = 6 < 12$, **CERTIFIED** in `replay.py`). Since $6 + 6 + 24 + 2(4) + 2(12) + 2(1) = 70 = \binom{8}{4}$ exhausts $\mathcal{F}_{\rm el}(C_4)|_{N=4}$, the maximum eigenvalue of $\Sigma_4$ on $\{N = 4, N_{\rm odd} > 0\}$ is $\max\{12, 10, 8, 6, 0\} = 12 = \lambda_{\max}(\Sigma_4|_{N=4, N_{\rm odd}=0})$, and hence $\Delta_{\rm eff} = 0$. $\square$

### 7.2 Obstruction to Route (c): Non-Commutativity and Adiabatic Breakdown of Bond Lang-Firsov

**Proposition 7.2 (Non-commuting bond hopping and BCH divergence of bond Lang-Firsov, PROVED pending independent review and CERTIFIED).**
*Let $b = \{x, y\}$ and $b' = \{y, z\}$ ($x \ne z$) be any two physical bonds sharing vertex $y$. Then:*
1. *The bond hopping operators $T_b$ and $T_{b'}$ fail to commute:*
   \[
   [T_b, T_{b'}] = \sum_{\sigma \in \{\uparrow,\downarrow\}} \left(c_{x\sigma}^\dagger c_{z\sigma} - c_{z\sigma}^\dagger c_{x\sigma}\right) \ne 0, \qquad \|[T_b, T_{b'}]\|_{\rm op} = 2.
   \]
2. *Under the unitary bond Lang-Firsov operator $U_{\rm LF} := e^S$ with skew-Hermitian generator $S := -i\frac{g}{K}\sum_{b \in \mathcal{E}_{\Lambda_L}} P_b T_b$ (chosen so that $[S, \sum_b \frac{K}{2} X_b^2] = -g \sum_b X_b T_b$ cancels the linear potential shift), the Baker-Campbell-Hausdorff series $U_{\rm LF}^\dagger H_{\Lambda_L} U_{\rm LF} = \sum_{k=0}^\infty \frac{1}{k!} \operatorname{ad}_S^k(H_{\Lambda_L})$ satisfies:*
   - *At order $k = 1$ on $V_t = -t\sum_b T_b$:*
     \[
     [S, V_t] = i\frac{gt}{K} \sum_{b, b' \in \mathcal{E}_{\Lambda_L}} P_b [T_b, T_{b'}],
     \]
     *whose single-bond thermal root-mean-square norm scales as $\frac{|g||t|}{K}\sqrt{\langle P_b^2 \rangle_{0,\beta}}\|[T_b, T_{b'}]\|_{\rm op} = 2|t|\sqrt{\frac{g^2}{2K\Omega}\coth\frac{\beta\Omega}{2}} \to \infty$ as $\Omega \downarrow 0$ at fixed $(\beta, t, g, K)$.*
   - *At order $k = 1$ on $V_g = g\sum_b X_b T_b$:*
     \[
     [S, V_g] = -\frac{g^2}{K} \sum_{b \in \mathcal{E}_{\Lambda_L}} T_b^2 - i\frac{g^2}{K} \sum_{b \ne b'} P_b X_{b'} [T_b, T_{b'}],
     \]
     *and for every $k \ge 2$, $\operatorname{ad}_S^k(V_t)$ and $\operatorname{ad}_S^k(V_g + H_{\rm ph})$ contain nonvanishing degree-$k$ momentum products $(\frac{g}{K})^k P_{b_1}\cdots P_{b_k} \operatorname{ad}_{T_{b_1}}\cdots\operatorname{ad}_{T_{b_{k-1}}}(T_{b_k})$ along contiguous bond walks $(b_1, \dots, b_k)$.*

*Proof.*
1. Since $[h_{b,\uparrow}, h_{b',\downarrow}] = 0$, $[T_b, T_{b'}] = \sum_\sigma [h_{b,\sigma}, h_{b',\sigma}]$. For each spin $\sigma$, CAR gives
   \[
   [c_{x\sigma}^\dagger c_{y\sigma} + c_{y\sigma}^\dagger c_{x\sigma},\; c_{y\sigma}^\dagger c_{z\sigma} + c_{z\sigma}^\dagger c_{y\sigma}] = c_{x\sigma}^\dagger \{c_{y\sigma}, c_{y\sigma}^\dagger\} c_{z\sigma} - c_{z\sigma}^\dagger \{c_{y\sigma}^\dagger, c_{y\sigma}\} c_{x\sigma} = c_{x\sigma}^\dagger c_{z\sigma} - c_{z\sigma}^\dagger c_{x\sigma}.
   \]
   Since $i(c_{x\sigma}^\dagger c_{z\sigma} - c_{z\sigma}^\dagger c_{x\sigma})$ is Hermitian with square $(n_{x\sigma} - n_{z\sigma})^2$ of norm $1$, summing over the two commuting spin species gives $\|[T_b, T_{b'}]\|_{\rm op} = 1 + 1 = 2$.
2. Using $[P_b, X_{b'}] = -i\delta_{b,b'}$ and $[P_b, P_{b'}] = 0$:
   - $[P_b T_b, X_{b'} T_{b'}] = [P_b, X_{b'}] T_b T_{b'} + X_{b'} P_b [T_b, T_{b'}] = -i\delta_{b,b'} T_b^2 + P_b X_{b'} [T_b, T_{b'}]$ (since $P_b$ and $X_{b'}$ commute for $b \ne b'$ while $[T_b, T_b] = 0$ for $b = b'$). Multiplying by $-i\frac{g^2}{K}$ gives the formula for $[S, V_g]$.
   - Similarly $[S, V_t] = i\frac{gt}{K}\sum_{b,b'} P_b [T_b, T_{b'}]$, and since $[P_b, P_{b'}] = 0$, applying $\operatorname{ad}_S$ repeatedly to $V_t$ multiplies by $-i\frac{g}{K} P_{b_j} \operatorname{ad}_{T_{b_j}}$ at each step $j = 1, \dots, k$. Along any path of distinct bonds $b_1, \dots, b_k$, the nested commutator $\operatorname{ad}_{T_{b_1}}\cdots\operatorname{ad}_{T_{b_{k-1}}}(T_{b_k})$ is the nonvanishing end-to-end hopping/current operator between the endpoints of the path with operator norm $2$. Finally, for a single harmonic oscillator, $\langle P_b^2 \rangle_{0,\beta} = \frac{M\Omega}{2}\coth\frac{\beta\Omega}{2} = \frac{K}{2\Omega}\coth\frac{\beta\Omega}{2}$, so $\frac{|g|}{K}\sqrt{\langle P_b^2\rangle_{0,\beta}} = \sqrt{\frac{g^2}{2K\Omega}\coth\frac{\beta\Omega}{2}} \sim (\beta\Omega)^{-1}\sqrt{\frac{\beta g^2}{K}} \to \infty$ as $\Omega \downarrow 0$. $\square$

### 7.3 Obstruction to Route (d): Algebraic Decay at $g = 0$ Precludes $(\beta t)$-Independent Exponential Bounds

**Proposition 7.3 (Exact algebraic $1/d^2$ decay of free-fermion pair correlations at $g = 0, \mu = 0, T \to 0$, PROVED pending independent review and CERTIFIED).**
*Consider the pure bond-SSH model at $g = 0$ ($\beta g^2/K = 0$), $t > 0$, and half-filling $\mu = 0$ on $\Lambda_L$.*
1. *For every $L \ge 4$, $\beta > 0$, and $r \in \Lambda_L$, the grand-canonical pair correlator factors by spin-independent fermionic Wick's theorem as*
   \[
   \langle \Delta_0^\dagger \Delta_r \rangle_{\Lambda_L}\big|_{g=0,\, \mu=0} = \left(G_{\Lambda_L,\beta}(r)\right)^2, \qquad G_{\Lambda_L,\beta}(r) := \langle c_{0\sigma}^\dagger c_{r\sigma} \rangle_{\Lambda_L}\big|_{g=0,\, \mu=0} = \frac{1}{L^2} \sum_{k \in \frac{2\pi}{L}\mathbb{Z}_L^2} \frac{e^{i k \cdot r}}{1 + e^{\beta \varepsilon(k)}},
   \]
   *where $\varepsilon(k) = -2t(\cos k_x + \cos k_y)$.*
2. *For every integer $m \ge 1$ and staircase displacement $r_m := (m, m-1) \in \mathbb{Z}^2$ of graph distance $d_m = \|r_m\|_1 = 2m - 1$, taking the thermodynamic limit $L \to \infty$ followed by the zero-temperature limit $\beta t \to \infty$ gives the exact closed-form integral*
   \[
   G_\infty(r_m) := \lim_{\beta t \to \infty} \lim_{L \to \infty} G_{\Lambda_L,\beta}(r_m) = \frac{1}{(2\pi)^2} \iint_{\cos k_x + \cos k_y > 0} \cos(m k_x + (m-1) k_y)\, dk_x\, dk_y = \frac{(-1)^{m-1} 2}{\pi^2 (2m - 1)},
   \]
   *and consequently*
   \[
   \lim_{\beta t \to \infty} \lim_{L \to \infty} \langle \Delta_0^\dagger \Delta_{(m,m-1)} \rangle_{\Lambda_L}\big|_{g=0,\, \mu=0} = \frac{4}{\pi^4 (2m - 1)^2} = \frac{4}{\pi^4 d_m^2} > 0.
   \]
3. *Therefore, for every $A > 0$ and $q \in (0, 1)$, choosing $m \ge 1$ large enough that $\frac{4}{\pi^4(2m-1)^2} > 2 A q^{2m-1}$, there exist $\beta t > 0$ and $L \ge 4$ such that $|\langle \Delta_0^\dagger \Delta_{r_m} \rangle_{\Lambda_L}|_{g=0,\mu=0} > A q^{d_{\Lambda_L}(0,r_m)}$. In particular, no uniform exponential clustering bound $|\langle \Delta_x^\dagger \Delta_y \rangle_{\Lambda_L}| \le A q^{d_{\Lambda_L}(x,y)}$ with $(\beta t)$-independent constants $(A, q)$ can hold under a smallness condition on $\beta g^2/K$ alone.*

*Proof.*
1. At $g = 0$, $H_{\Lambda_L} = H_{\rm el} + H_{\rm ph}$ is a sum of a free-fermion hopping Hamiltonian $H_{\rm el} = \sum_{k,\sigma} \varepsilon(k) \hat{c}_{k\sigma}^\dagger \hat{c}_{k\sigma}$ and decoupled oscillators $H_{\rm ph}$. In this product state, $\Delta_0^\dagger \Delta_r = c_{0\uparrow}^\dagger c_{0\downarrow}^\dagger c_{r\downarrow} c_{r\uparrow} = (c_{0\uparrow}^\dagger c_{r\uparrow})(c_{0\downarrow}^\dagger c_{r\downarrow})$ factors over the two independent spin species into $\langle c_{0\uparrow}^\dagger c_{r\uparrow}\rangle \langle c_{0\downarrow}^\dagger c_{r\downarrow}\rangle = G_{\Lambda_L,\beta}(r)^2$, and Fourier inversion gives the formula for $G_{\Lambda_L,\beta}(r)$.
2. As $L \to \infty$ at fixed $\beta t$, the Riemann sum $G_{\Lambda_L,\beta}(r_m)$ converges to $\frac{1}{(2\pi)^2}\int_{[-\pi,\pi]^2} \frac{\cos(m k_x + (m-1) k_y)}{1 + e^{\beta\varepsilon(k)}} dk_x dk_y$. Since the Fermi surface $\{\cos k_x + \cos k_y = 0\}$ has Lebesgue measure zero in $[-\pi, \pi]^2$ and the integrand is bounded by $1$, the dominated convergence theorem gives the $\beta t \to \infty$ limit $G_\infty(r_m)$ over the Fermi sea $\{\cos k_x + \cos k_y > 0\}$. Rotate coordinates to $u := \frac{k_x + k_y}{2}$ and $v := \frac{k_x - k_y}{2}$. Then $\cos k_x + \cos k_y = 2\cos u \cos v$, the Jacobian is $\left|\frac{\partial(k_x, k_y)}{\partial(u, v)}\right| = 2$, and the Fermi sea inside $[-\pi, \pi]^2$ is the diamond $\{|u| < \pi/2, |v| < \pi/2\}$ (where $\cos u > 0$ and $\cos v > 0$; the corner regions where $\cos u < 0$ and $\cos v < 0$ wrap by periodicity $(k_x, k_y) \mapsto (k_x \pm 2\pi, k_y)$ outside $[-\pi, \pi]^2$). Since $m k_x + (m-1) k_y = (2m - 1) u + v$ and $\sin((2m-1)u)\sin v$ is odd in $u$ and $v$, the integral factors into two elementary 1D integrals:
   \[
   G_\infty(r_m) = \frac{2}{(2\pi)^2} \left(\int_{-\pi/2}^{\pi/2} \cos((2m - 1)u)\, du\right)\left(\int_{-\pi/2}^{\pi/2} \cos v\, dv\right) = \frac{1}{2\pi^2} \left[\frac{2\sin((2m-1)\pi/2)}{2m - 1}\right] \cdot 2 = \frac{(-1)^{m-1} 2}{\pi^2 (2m - 1)}.
   \]
   Squaring gives $G_\infty(r_m)^2 = \frac{4}{\pi^4(2m-1)^2}$, and (3) follows immediately since $\frac{4}{\pi^4 d^2}$ dominates $A q^d$ as $d = 2m - 1 \to \infty$ for every $q \in (0, 1)$. $\square$

---

## 8. Verification Summary and Scope Boundaries

- **CERTIFIED (`PURESSH/replay.py`):** Pure Python stdlib `fractions.Fraction` exact rational and outward-rounded rational-interval checks (plus optional `mpmath.iv` cross-check) verify:
  1. Exact 16-state 2-site CAR algebra: $T_b = T_b^\dagger$, $\operatorname{spec}(T_b) = \{-2, -1, 0, 1, 2\}$, $\|T_b\|_{\rm op} = 2$, $\operatorname{spec}(Y_{e'}(\theta)) = \{-1, 0, 1\}$, $\|Y_{e'}(\theta)\|_{\rm op} = 1$, $\|\Delta_x^\dagger \Delta_y\|_{\rm op} = 1$, and exact commutation with $N_\uparrow, N_\downarrow, (-1)^N$ (Lemma 4.1);
  2. Rigorous outward rational-interval certification of the multilinear Schatten-Hölder trace bound (Lemma 4.2) on $16\times 16$ matrices across multiple $(\beta, \mu, \Delta_j)$ splits, verifying exact cancellation of $z_0^{|S|} = (1 + e^{\beta\mu})^{2|S|}$;
  3. Exact rational-interval verification of $\int_0^\beta C_\beta(|u - v|)\, du = 1/K$ across $\Omega \in \{10^{-3}, 1.7, 500\}$ and $n = 4$ bosonic Wick pairing identity $(2r-1)!! = \frac{(2r)!}{2^r r!}$ with infinite-dimensional truncation tail bound (Lemmas 3.1–3.2);
  4. Exact rational verification of all Theorem 1.1–1.2 constants: $c_0 = 2^{-10}$, $\xi_0 = 2^{-9}\beta^{-1}$, $\varepsilon_{\rm phys} = \varepsilon_{\rm src} = 2/1023$, $q_{\rm GC} = 32/341 < 1$, $A_{\rm GC} = 341/103$, $b_{\rm GC} = 32/103 < 1$, $R_{\rm max} = 24718511/9834543 < 3$, $q_{\rm src} = 72/341 < 1$, $b_{\rm src} = 216/269 < 1$, $-2\log(1 - b_{\rm src}/e) < 2$, and the rational majorant $e^x - 1 \le \frac{x}{1 - x/2}$;
  5. Exact rational-interval verification of boundary oscillator stiffness monotonicity $Z_{\mathrm{ph},1}(K/2) > Z_{\mathrm{ph},1}(K) > Z_{\mathrm{ph},1}(2K)$ (Lemma 6.1);
  6. Exact integer matrix verification of Proposition 7.1 across all 9 $(N_\uparrow, N_\downarrow, N_{\rm odd})$ invariant sectors (6 spin-flip-conjugate classes, $70$ states total) of $C_4$ at $N = 4$: $M_{\rm even} v_{\rm even} = 12 v_{\rm even}$ and $M_{\rm even}(M_{\rm even}-4I)(M_{\rm even}-8I)(M_{\rm even}-12I) = 0$ on $\{N_\uparrow=N_\downarrow=2, N_{\rm odd}=0\}$ ($\dim=6$, $\lambda_{\max}=12$); $M_{\rm odd} v_{\rm odd} = 12 v_{\rm odd}$ and $M_{\rm odd}(M_{\rm odd}-4I)(M_{\rm odd}-8I)(M_{\rm odd}-12I) = 0$ on $\{N_\uparrow=N_\downarrow=2, N_{\rm odd}=4\}$ ($\dim=6$, $\lambda_{\max}=12$); $(\Sigma_4-2I)(\Sigma_4-4I)(\Sigma_4-6I)(\Sigma_4-10I) = 0$ on $\{N_\uparrow=N_\downarrow=2, N_{\rm odd}=2\}$ ($\dim=24$, $\lambda_{\max}=10$); $\Sigma_4(\Sigma_4-4I)(\Sigma_4-8I) = 0$ on $\{N_\uparrow,N_\downarrow\}=\{3,1\}$ with $N_{\rm odd}=4$ ($\dim=4+4$, $\lambda_{\max}=8$); $(\Sigma_4-2I)(\Sigma_4-4I)(\Sigma_4-6I) = 0$ on $\{N_\uparrow,N_\downarrow\}=\{3,1\}$ with $N_{\rm odd}=2$ ($\dim=12+12$, $\lambda_{\max}=6$); and $\Sigma_4 = 0$ on $\{N_\uparrow,N_\downarrow\}=\{4,0\}$ ($\dim=1+1$, $\lambda_{\max}=0$), proving $\Delta_{\rm eff} = 0$ across all $N=4$ sectors;
  7. Exact integer matrix verification of Proposition 7.2 on a 3-site chain: $[T_{01}, T_{12}] \ne 0$ and $\|[T_{01}, T_{12}]\|_{\rm op} = 2$;
  8. Outward rational-interval verification of Proposition 7.3: $\frac{4}{\pi^4(2m-1)^2} > A_{\rm GC} q_{\rm GC}^{2m-1}$ for all $m \ge 2$ along the staircase ray $r_m = (m, m-1)$ of graph distance $d_m = 2m-1$ (already at $m = 2$, $r_2 = (2,1)$, $d_2 = 3$: $\frac{4}{9\pi^4} \approx 4.5627 \times 10^{-3} > A_{\rm GC} q_{\rm GC}^3 \approx 2.7359 \times 10^{-3}$).
- **Mutants (`PURESSH/replay.py --all-mutants`):** 12 mathematical mutants (`norm_tb_underestimate`, `norm_ye_underestimate`, `wick_pairings_corrupted`, `exp_phys_factor_halved`, `exp_taylor_bound_dropped`, `degree_phys_underestimate`, `degree_aug_underestimate`, `euler_walk_exponent_halved`, `kp_vertex_weight_dropped`, `threshold_c0_doubled`, `route_b_gap_assumed_positive`, `route_c_commutator_assumed_zero`), every one of which exits `1`.
- **NUMERICAL (`PURESSH/ed_check.py`):** Exact diagonalization on the 2-site dimer ($N_{\rm ph} \in \{30, 60, 90, 120\}$) and 4-site ring $C_4$ ($N_{\rm tot} \in \{2, 3, 4\}$ total phonon excitations across the 4 bonds) across $\Omega \in \{0.2, 2.0, 3.0, 5.0, 20.0\}$ and $\mu \in \{0.0, 0.5\}$, confirming rapid Fock-cutoff convergence and verifying $|\langle \Delta_x^\dagger \Delta_y \rangle| \ll A_{\rm GC} q_{\rm GC}^{d(x,y)}$ at all tested points.
- **Explicitly NOT covered (Scope Boundaries):**
  1. *Low temperatures / large hopping:* The regime $\beta|t| + \beta g^2/K > 2^{-10}$ (in particular $\beta|t| \gg 1$ with $\beta g^2/K \ll 1$, where Proposition 7.3 proves that free-fermion algebraic correlation tails $\sim d^{-2}$ violate any $(\beta t)$-independent exponential decay bound) is not covered by Theorems 1.1–1.2.
  2. *BKT quasi-long-range order / pair-susceptibility divergence in 2D (and ODLRO in $d \ge 3$) at $\beta|t| \gg 1$:* In 2D at any $T > 0$, the Hohenberg-Mermin-Wagner theorem precludes spontaneous breaking of the continuous $U(1)$ charge symmetry, so $\lim_{\|x-y\|_1\to\infty}|\langle \Delta_x^\dagger \Delta_y\rangle| = 0$ holds at every $T > 0$, and superconducting order in 2D is instead characterized by a Berezinskii-Kosterlitz-Thouless (BKT) phase with slow algebraic decay $|\langle \Delta_x^\dagger \Delta_y\rangle| \sim \|x-y\|_1^{-\eta}$ ($\eta \le 1/4 < 2$) and a divergent integrated pair susceptibility $\chi_{\rm pair}(\Lambda_L) = \sum_{y \in \Lambda_L} |\langle \Delta_x^\dagger \Delta_y\rangle_{\Lambda_L}| \to \infty$ as $L \to \infty$ (whereas the free-fermion $T \to 0$ limit in Proposition 7.3 has $\eta = 2$ along the staircase ray and bounded $\sum_y |\langle \Delta_0^\dagger \Delta_y\rangle| \le 1/2$). Whether BKT algebraic quasi-long-range order / divergent $\chi_{\rm pair}$ in 2D (or true non-decaying ODLRO $\lim_{\|x-y\|_1\to\infty}|\langle \Delta_x^\dagger \Delta_y\rangle| > 0$ in $d \ge 3$) is absent for all $k_B T \ge C g^2/K$ at arbitrary $\beta|t| \gg 1$ when $U_{\rm eff} = 0$ remains **OPEN**.
  3. *No material or experimental claims:* All results are rigorous mathematical properties of the lattice model Hamiltonian $H_{\Lambda_L}$. No physical superconductor or experimental $T_c$ is claimed.
