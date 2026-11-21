# ANNEALED-STATIC: Annealed First Dynamic Cumulant Control and Reflection-Positivity / Separating-Contour Obstructions

**Status: reviewed in `REVIEW.md` (`PASS-WITH-FIXES`; all P1, P2, and P3 fixes applied).** Following the allowed labels in `REVIEW.md`: exact-rational and outward-interval (`flint.arb` and `mpmath.iv`) computations in `replay.py` and `independent.py` carry the **CERTIFIED** label; analytical theorems in §§2--3 (Theorem 1a, Lemma 1, Theorem 1b, Theorem 1c, Theorem 2a, and Theorem 2c Part 1) carry the **PROVED** label (with Theorem 2a(1),(3) **PROVED (computer-assisted)**); the separating-contour vs. vacuum-loop synthesis in Proposition 2b and the adiabatic-window commentary in Theorem 2c Part 2 carry the **HEURISTIC (method-barrier synthesis)** label; finite-lattice floating-point probes carry the **NUMERICAL** label. All statements concern the model pairing scale $T_{\mathrm{pair}}$ of the spinful Holstein Hamiltonian; nothing here asserts a measured critical temperature $T_c$.

---

## 1. Model, Static-Dynamic Split, and the `STATIC-MODE` Baseline

Let $\Lambda$ be a finite simple graph of maximum degree $D \le 4$ without self-loops (in particular, the $d$-dimensional periodic torus $(\mathbb{Z}/L\mathbb{Z})^d$ for $d \in \{1, 2\}$, where $D = 2d \le 4$). Let $\tau = k_{\mathrm{B}} T > 0$, $\beta = 1/\tau$, phonon energy $\Omega = \hbar\sqrt{K/m} > 0$, hopping amplitude $t \ge 0$, onsite attraction scale $U = g_{\mathrm{ep}}^2 / K > 0$, and chemical potential $\mu \in \mathbb{R}$.

With adjacency matrix $(A_{\Lambda})_{xy} = \mathbf{1}_{\{x \sim y\}}$, the one-spin electronic kinetic-plus-static Hamiltonian at a real static site field $b_0 = (b_{0,x})_{x \in \Lambda} \in \mathbb{R}^{\Lambda}$ is
$$h_W = -t A_{\Lambda} + \operatorname{diag}(W), \qquad W_x := b_{0,x} - \mu \quad (x \in \Lambda). \tag{1}$$
As established in `LINEAR8/RIGOR.md` §§0--1 and `STATIC-MODE/RIGOR.md` §1, integrating out the harmonic oscillator coordinates after separating the Matsubara zero mode $b_{0,x}$ from the mean-zero real Gaussian dynamic field $v_x(\cdot)$ with covariance
$$D_{\mathrm{dyn}}(u - u') = \frac{U}{\beta} \sum_{n \neq 0} r_n e^{i \nu_n (u - u')}, \qquad r_n := \frac{\Omega^2}{\nu_n^2 + \Omega^2}, \qquad \nu_n := \frac{2\pi n}{\beta}, \tag{2}$$
yields the exact representation of the grand-canonical partition function
$$Z = \int_{\mathbb{R}^{\Lambda}} \gamma_s(db_0)\, Z(b_0), \qquad \gamma_s(db_0) = \prod_{x \in \Lambda} \sqrt{\frac{\beta}{2\pi U}}\, e^{-\beta b_{0,x}^2 / (2U)}\, db_{0,x}, \tag{3}$$
where the conditional two-spin partition function at fixed $b_0$ (equivalently fixed $W = b_0 - \mu\mathbf{1}$) is
$$Z(b_0) = Z_0(W)\, R_W(1), \qquad Z_0(W) := \det\!\left(I + e^{-\beta h_W}\right)^2 > 0, \tag{4}$$
and the conditional dynamic partition-function ratio with coupling interpolation $s \ge 0$ is
$$R_W(s) := \mathbb{E}_v\!\left[\frac{\det\!\left(I + \mathcal{T}\exp\!\left(-\int_0^{\beta} \bigl(h_W + \sqrt{s}\,\operatorname{diag}(v(u))\bigr)\, du\right)\right)^2}{\det\!\left(I + e^{-\beta h_W}\right)^2}\right]. \tag{5}$$
Because $\int_0^{\beta} D_{\mathrm{dyn}}(u)\, du = 0$, replacing the site density $n_x$ by $n_x - 1$ leaves $R_W(s)$ unchanged. The annealed static marginal on $\mathbb{R}^{\Lambda}$ is the probability measure
$$P_s(db_0) := \frac{\gamma_s(db_0)\, Z(b_0)}{Z}. \tag{6}$$

By `STATIC-MODE/RIGOR.md` Lemma 1 (reviewed PROVED in `STATIC-MODE/REVIEW.md`), the exact first dynamic cumulant of $\log R_W(s)$ at $s = 0$ is
$$\left.\frac{d}{ds} \log R_W(s)\right|_{s=0} = R'_W(0) = \sum_{x \in \Lambda} a_x(W), \tag{7}$$
where for each site $x \in \Lambda$, in the orthonormal eigenbasis $h_W \psi_a = e_a \psi_a$ with $p_a(x) := |\psi_a(x)|^2$ and Fermi function $f(e) := (e^{\beta e} + 1)^{-1}$,
$$a_x(W) = 2 U \sum_{n=1}^{\infty} \frac{\Omega^2}{\nu_n^2 + \Omega^2} \sum_{a, b} p_a(x) p_b(x) \frac{\bigl(f(e_a) - f(e_b)\bigr)(e_b - e_a)}{\nu_n^2 + (e_b - e_a)^2} \ge 0. \tag{8}$$
Moreover, `STATIC-MODE/RIGOR.md` eq. (4) and eq. (7) establish the universal static-field upper bound (valid for every $W \in \mathbb{R}^{\Lambda}$, every $\Lambda$, and every $t \ge 0$)
$$0 \le a_x(W) \le \frac{U}{2\tau} \sum_{n=1}^{\infty} \frac{\Omega^2}{\nu_n^2 + \Omega^2} \le \frac{U \Omega^2}{2\tau} \sum_{n=1}^{\infty} \frac{1}{(2\pi n \tau)^2} = \frac{U \Omega^2}{48 \tau^3}. \tag{9}$$
Conversely, `STATIC-MODE/RIGOR.md` Theorem 1 and Corollary 1 show that for $0 < \Omega \le \tau \le t/4$, the resonant three-site field $W_{\mathrm{bridge}} = (2\tau, \frac{t^2}{2\tau} - 2\tau, 2\tau)$ and its square-torus embedding $W_B$ on $(\mathbb{Z}/L\mathbb{Z})^2$ ($L \ge 4$) satisfy
$$a_{\mathrm{left}}(W_{\mathrm{bridge}}) > \frac{U \Omega^2}{1200 \tau^3}, \qquad a_{(0,0)}(W_B) \ge \frac{U \Omega^2}{2400 \tau^3}, \tag{10}$$
so $\sup_{W \in \mathbb{R}^{\Lambda}} a_x(W) \asymp U \Omega^2 / \tau^3$, which diverges as $\Omega^{-1}$ along any linear ray $\tau = C \Omega$.

---

## 2. Part I: Annealed Suppression of `STATIC-MODE` Resonances and Uniform First-Cumulant Bound

For a static gap threshold $g > 0$, define the defect set of near-Fermi sites
$$D_g(b_0) := \bigl\{x \in \Lambda : |W_x| = |b_{0,x} - \mu| < g\bigr\}. \tag{11}$$
Recall `LINEAR8` Proposition P16 (`ADIABATIC/LINEAR8/RIGOR.md`, lines 131--138, reviewed PROVED): for every finite graph $\Lambda$ of maximum weighted degree $D \le 4$, every $\mu \in \mathbb{R}$, every $0 < g \le U/4$, $0 \le t \le g/64$, and $0 < \Omega \le \tau \le U/16$, and every subset $B \subset \Lambda$, the full interacting annealed static marginal $P_s$ satisfies
$$P_s\bigl(B \subset D_g(b_0)\bigr) \le \exp\!\left(-\frac{\beta U |B|}{48}\right) = \exp\!\left(-\frac{U |B|}{48 \tau}\right). \tag{12}$$

### Theorem 1a (Exponential Rarity of `STATIC-MODE` Resonance Configurations under $P_s$)

*Let $\Lambda$ have maximum degree $D \le 4$, and suppose $0 < g \le U/4$, $0 \le t \le g/64$, and $0 < \Omega \le \tau \le \min(U/16, g/2)$ with $\tau < g/2$. For any two distinct endpoint sites $x_1 \neq x_3$ in $\Lambda$, define the `STATIC-MODE` endpoint-resonance event*
$$\mathcal{E}_{\mathrm{res}}(x_1, x_3) := \bigl\{b_0 \in \mathbb{R}^{\Lambda} : |W_{x_1}| \le 2\tau \text{ and } |W_{x_3}| \le 2\tau\bigr\}. \tag{13}$$
*Then every embedded `STATIC-MODE` witness on $(x_1, x_2, x_3)$ (which has $W_{x_1} = W_{x_3} = 2\tau$) belongs to $\mathcal{E}_{\mathrm{res}}(x_1, x_3)$, and under the full interacting static marginal $P_s$,*
$$P_s\bigl(\mathcal{E}_{\mathrm{res}}(x_1, x_3)\bigr) \le \exp\!\left(-\frac{U}{24\tau}\right). \tag{14}$$
*In particular, along any linear ray $\tau = C \Omega$, $P_s(\mathcal{E}_{\mathrm{res}}(x_1, x_3)) \le \exp(-U / (24 C \Omega))$, which decays faster than any power of $\Omega$ as $\Omega \to 0^+$.*

#### Proof of Theorem 1a
Since $\tau < g/2$, any configuration $b_0 \in \mathcal{E}_{\mathrm{res}}(x_1, x_3)$ satisfies $|b_{0,x_1} - \mu| = |W_{x_1}| \le 2\tau < g$ and $|b_{0,x_3} - \mu| = |W_{x_3}| \le 2\tau < g$. Hence the two-point set $B = \{x_1, x_3\}$ of cardinality $|B| = 2$ satisfies $B \subset D_g(b_0)$. Applying (12) (`LINEAR8` Proposition P16) with $|B| = 2$ gives
$$P_s\bigl(\mathcal{E}_{\mathrm{res}}(x_1, x_3)\bigr) \le P_s\bigl(\{x_1, x_3\} \subset D_g(b_0)\bigr) \le \exp\!\left(-\frac{2 U}{48\tau}\right) = \exp\!\left(-\frac{U}{24\tau}\right). \quad \blacksquare$$

---

### Lemma 1 (Exact Matsubara Representation and Global Gapped Bound for $a_x(W)$)

*For every finite graph $\Lambda$, every $W \in \mathbb{R}^{\Lambda}$, and every site $x \in \Lambda$:*
1. *Let $\omega_k := (2k+1)\pi / \beta$ ($k \in \mathbb{Z}$) be the fermionic Matsubara frequencies and $R_W(i\omega_k) := (i\omega_k I - h_W)^{-1}$ the one-particle resolvent. Define the conditional density susceptibility at bosonic frequency $\nu_n = 2\pi n / \beta \neq 0$ by*
   $$\chi_x(i\nu_n; W) := \sum_{a, b} p_a(x) p_b(x) \frac{\bigl(f(e_a) - f(e_b)\bigr)(e_b - e_a)}{\nu_n^2 + (e_b - e_a)^2}. \tag{15}$$
   *Then $\chi_x(i\nu_n; W) = \chi_x(-i\nu_n; W) \ge 0$, and it admits the absolute-square Matsubara convolution identity*
   $$\chi_x(i\nu_n; W) = -\frac{1}{\beta} \sum_{k \in \mathbb{Z}} \bigl(R_W(i\omega_k)_{xx} - R_W(i\omega_k)_{xx}^{\mathrm{static}}\bigr)\, R_W(i\omega_k + i\nu_n)_{xx} = -\frac{1}{\beta} \sum_{k \in \mathbb{Z}} R_W(i\omega_k)_{xx}\, R_W(i\omega_k + i\nu_n)_{xx}, \tag{16}$$
   *where the sum converges absolutely because $R_W(i\omega_k)_{xx} = (i\omega_k)^{-1} + O(|\omega_k|^{-2})$ and $\sum_{k \in \mathbb{Z}} (i\omega_k)^{-1}(i\omega_k + i\nu_n)^{-1} = 0$ for $\nu_n \neq 0$.*
2. *If the spectrum of $h_W$ has a gap $|e_a| \ge g_0 > 0$ for all eigenvalues $e_a$ of $h_W$, then for every $\nu_n \neq 0$,*
   $$0 \le \chi_x(i\nu_n; W) \le \frac{1}{2 g_0}, \tag{17}$$
   *and consequently*
   $$0 \le a_x(W) = 2 U \sum_{n=1}^{\infty} \frac{\Omega^2}{\nu_n^2 + \Omega^2}\, \chi_x(i\nu_n; W) \le \frac{U \Omega^2}{24 \tau^2 g_0}. \tag{18}$$

#### Proof of Lemma 1
For part 1, the partial-fraction identity for $n \neq 0$,
$$\frac{1}{\beta} \sum_{k \in \mathbb{Z}} \frac{1}{(i\omega_k - e_a)(i\omega_k + i\nu_n - e_b)} = \frac{f(e_a) - f(e_b)}{i\nu_n + e_a - e_b},$$
multiplied by $p_a(x) p_b(x)$ and summed over $a, b$ gives $-\frac{1}{\beta}\sum_{k \in \mathbb{Z}} R_W(i\omega_k)_{xx} R_W(i\omega_k + i\nu_n)_{xx}$. Symmetrizing $(a,b) \leftrightarrow (b,a)$ cancels the odd imaginary part $i\nu_n$ in the numerator and yields (15)--(16).

For part 2, suppose $|e_a| \ge g_0 > 0$ for all $a$. For any $e_a \neq e_b$ and $\nu_n \neq 0$, the summand factor in (15) satisfies
$$0 \le Q(e_a, e_b; \nu_n) := \frac{\bigl(f(e_a) - f(e_b)\bigr)(e_b - e_a)}{\nu_n^2 + (e_b - e_a)^2} \le \frac{|f(e_a) - f(e_b)|}{|e_b - e_a|}. \tag{19}$$
We bound the difference quotient $\frac{|f(e_a) - f(e_b)|}{|e_b - e_a|}$ in both sign cases when $|e_a|, |e_b| \ge g_0$:
- **Opposite-sign case ($e_a e_b < 0$):** Because $e_a$ and $e_b$ have opposite signs and $|e_a|, |e_b| \ge g_0$, we have $|e_b - e_a| = |e_a| + |e_b| \ge 2 g_0$, while $|f(e_a) - f(e_b)| \le 1$, so
  $$\frac{|f(e_a) - f(e_b)|}{|e_b - e_a|} \le \frac{1}{2 g_0}. \tag{20a}$$
- **Same-sign case ($e_a e_b > 0$):** Because $e_a$ and $e_b$ lie on the same side of $[-g_0, g_0]$, every point $\xi$ between $e_a$ and $e_b$ satisfies $|\xi| \ge g_0$. By the mean value theorem,
  $$\frac{|f(e_a) - f(e_b)|}{|e_b - e_a|} = |f'(\xi)| = \frac{\beta}{4 \cosh^2(\beta \xi / 2)} \le \frac{\beta}{4 \cosh^2(\beta g_0 / 2)} < \frac{\beta}{4 (\beta g_0 / 2)} = \frac{1}{2 g_0}, \tag{20b}$$
  where we used $\cosh^2(u) \ge 1 + u^2 > 2u > u$ for all $u > 0$.

Combining (19), (20a), and (20b), every pair $(a, b)$ of eigenvalues of a $g_0$-gapped Hamiltonian $h_W$ satisfies
$$0 \le Q(e_a, e_b; \nu_n) \le \frac{1}{2 g_0}. \tag{21}$$
Multiplying (21) by $p_a(x) p_b(x)$ and summing over $a, b$ using $\sum_{a,b} p_a(x) p_b(x) = 1$ proves (17). Multiplying (17) by $2U \frac{\Omega^2}{\nu_n^2 + \Omega^2} \le 2U \frac{\Omega^2}{\nu_n^2}$ and summing over $n \ge 1$ using $\sum_{n=1}^{\infty} \nu_n^{-2} = \frac{1}{4\pi^2 \tau^2} \frac{\pi^2}{6} = \frac{1}{24\tau^2}$ yields (18):
$$0 \le a_x(W) \le 2 U \left(\sum_{n=1}^{\infty} \frac{\Omega^2}{\nu_n^2}\right) \frac{1}{2 g_0} = \frac{U \Omega^2}{24 \tau^2 g_0}. \quad \blacksquare$$
---

### Theorem 1b (Deterministic Local-Buffer Suppression of $a_x(W)$ with Vanishing First-Order Boundary Leakage)

*Let $\Lambda$ be a finite simple graph of maximum degree $D \le 4$. Fix $g > 0$, $0 \le t < g/4$, a site $x \in \Lambda$, and an integer buffer radius $R \ge 0$. Suppose the static potential $W \in \mathbb{R}^{\Lambda}$ satisfies the local gap condition*
$$|W_y| \ge g \quad \text{for every } y \in B_R(x) := \bigl\{y \in \Lambda : \operatorname{dist}_{\Lambda}(x, y) \le R\bigr\}, \tag{22}$$
*while $W_z \in \mathbb{R}$ is completely arbitrary for all $z \in \Lambda \setminus B_R(x)$. Then:*
1. *(Decoupled block gap and vanishing first-order boundary term): Let $h_0$ be the block-diagonal Hamiltonian obtained from $h_W$ by setting the hopping across the boundary $\partial B_R(x) := \{(u, v) \in E(\Lambda) : u \in B_R(x),\, v \notin B_R(x)\}$ to zero, so $h_W = h_0 + T_{\partial}$. The block $h_{B_R(x)}$ of $h_0$ on $\ell^2(B_R(x))$ has spectral gap at least $g_0 := g - 4t > 0$, so its local dynamic cumulant satisfies*
   $$0 \le a_x^{(0)}(W) \le \frac{U \Omega^2}{24 \tau^2 (g - 4t)}. \tag{23}$$
   *Moreover, for every complex $z \in \mathbb{C} \setminus \mathbb{R}$, the first-order boundary perturbation of the diagonal Green's function at $x$ vanishes identically:*
   $$\bigl(R_0(z) T_{\partial} R_0(z)\bigr)_{xx} = 0, \qquad R_0(z) := (z I - h_0)^{-1}, \tag{24}$$
   *and the exact difference between the full resolvent $R_W(z) = (z I - h_W)^{-1}$ and $R_0(z)$ at $(x, x)$ is given by the projected two-step resolvent identity*
   $$R_W(z)_{xx} - R_0(z)_{xx} = \bigl(R_0(z) P_{\partial_{\mathrm{in}}} T_{\partial} R_W(z) T_{\partial} P_{\partial_{\mathrm{in}}} R_0(z)\bigr)_{xx}, \tag{25}$$
   *where $P_{\partial_{\mathrm{in}}}$ is the orthogonal projection onto the inner boundary sphere $\partial_{\mathrm{in}} B_R(x) := \{u \in B_R(x) : \operatorname{dist}_{\Lambda}(x, u) = R\}$.*
2. *(Pointwise Neumann boundary bound): For every fermionic frequency $\omega_k = (2k+1)\pi/\beta$,*
   $$\bigl|R_W(i\omega_k)_{xx} - R_0(i\omega_k)_{xx}\bigr| \le \frac{1}{|\omega_k|} \frac{(4t/g)^{2R+2}}{(1 - 4t/g)^2}. \tag{26}$$
3. *(Local dynamic cumulant bound): The exact local dynamic cumulant $a_x(W)$ of the full Hamiltonian $h_W$ on $\Lambda$ obeys the volume-independent bound*
   $$0 \le a_x(W) \le \frac{U \Omega^2}{24 \tau^2}\left[\frac{1}{g - 4t} + \frac{1}{\tau} \frac{(4t/g)^{2R+2}}{(1 - 4t/g)^2}\right]. \tag{27}$$
   *In particular, if $4t/g \le 1/16$ (i.e. $t \le g/64$) and $R \ge \max\bigl(0, \lceil \frac{\log(g/\tau)}{\log 16}\rceil - 1\bigr)$, then $(4t/g)^{2R+2} \le \tau / g$, and independently of $W|_{\Lambda \setminus B_R(x)}$, $\tau > 0$, and $|\Lambda|$,*
   $$0 \le a_x(W) \le \frac{496}{225}\,\frac{U \Omega^2}{24 \tau^2 g} = \frac{62}{675}\,\frac{U \Omega^2}{\tau^2 g}. \tag{28}$$

#### Proof of Theorem 1b
1. By Gershgorin's circle theorem on $\ell^2(B_R(x))$, since $|W_y| \ge g$ for all $y \in B_R(x)$ and each site has at most $D \le 4$ neighbors, every eigenvalue $e_a^{(0)}$ of $h_{B_R(x)}$ satisfies $|e_a^{(0)}| \ge g - 4t = g_0 > 0$. Because $x \in B_R(x)$ and $h_0 = h_{B_R(x)} \oplus h_{\Lambda \setminus B_R(x)}$ is block-diagonal, the local cumulant $a_x^{(0)}(W)$ of $h_0$ at $x$ depends only on $h_{B_R(x)}$, so Lemma 1 eq. (18) yields (23).
   Next, let $P_{B_R}$ be the orthogonal projection onto $\ell^2(B_R(x))$ and $Q_{B_R} := I - P_{B_R}$. Since $h_0$ commutes with $P_{B_R}$, so does $R_0(z)$, whereas $T_{\partial}$ only connects $\partial_{\mathrm{in}} B_R(x) \subset B_R(x)$ to $\Lambda \setminus B_R(x)$ and therefore satisfies $P_{B_R} T_{\partial} P_{B_R} = 0$ and $Q_{B_R} T_{\partial} P_{B_R} = T_{\partial} P_{\partial_{\mathrm{in}}}$. Because $\delta_x = P_{B_R}\delta_x$, we have
   $$\bigl(R_0(z) T_{\partial} R_0(z)\bigr)_{xx} = \langle \delta_x, P_{B_R} R_0(z) P_{B_R} T_{\partial} P_{B_R} R_0(z) P_{B_R} \delta_x \rangle = 0,$$
   proving (24). Applying the second resolvent identity twice,
   $$R_W(z) - R_0(z) = R_0(z) T_{\partial} R_0(z) + R_0(z) T_{\partial} R_W(z) T_{\partial} R_0(z),$$
   taking the $(x, x)$ matrix element, using (24), and noting that $T_{\partial} P_{B_R} = T_{\partial} P_{\partial_{\mathrm{in}}}$ and $P_{B_R} T_{\partial} = P_{\partial_{\mathrm{in}}} T_{\partial}$ establishes (25).

2. Write $h_{B_R(x)} = W_{B_R} - t A_{B_R}$ on $\ell^2(B_R(x))$, where $W_{B_R} = \operatorname{diag}(W|_{B_R(x)})$. For any real $\omega_k \neq 0$, the diagonal operator $D_k := (i\omega_k I - W_{B_R})^{-1}$ satisfies $\|D_k\|_{\mathrm{op}} = \max_{y \in B_R(x)} (|\omega_k|^2 + W_y^2)^{-1/2} \le g^{-1}$, while $\|t A_{B_R}\|_{\mathrm{op}} \le 4t$. Since $4t/g < 1$, the Neumann series
   $$R_0(i\omega_k)\big|_{\ell^2(B_R(x))} = \sum_{m=0}^{\infty} D_k \bigl(t A_{B_R} D_k\bigr)^m$$
   converges in operator norm. Because $\operatorname{dist}_{\Lambda}(x, \partial_{\mathrm{in}} B_R(x)) = R$ and $(A_{B_R})^m_{ux} = 0$ for all $u \in \partial_{\mathrm{in}} B_R(x)$ whenever $m < R$, all terms with $m < R$ vanish upon multiplying by $P_{\partial_{\mathrm{in}}}$. Thus
   $$\bigl\|P_{\partial_{\mathrm{in}}} R_0(i\omega_k) \delta_x\bigr\|_2 \le \sum_{m=R}^{\infty} g^{-1} \left(\frac{4t}{g}\right)^m = \frac{1}{g} \frac{(4t/g)^R}{1 - 4t/g},$$
   and because $T_{\partial}$ maps $\partial_{\mathrm{in}} B_R(x)$ into $\Lambda \setminus B_R(x)$ with $\|T_{\partial}\|_{\mathrm{op}} \le 4t$,
   $$\bigl\|T_{\partial} P_{\partial_{\mathrm{in}}} R_0(i\omega_k) \delta_x\bigr\|_2 \le \frac{4t}{g} \frac{(4t/g)^R}{1 - 4t/g} = \frac{(4t/g)^{R+1}}{1 - 4t/g}. \tag{29}$$
   Since $h_W$ is self-adjoint on $\ell^2(\Lambda)$, its full resolvent satisfies the universal spectral bound $\|R_W(i\omega_k)\|_{\mathrm{op}} \le |\omega_k|^{-1}$ regardless of $W|_{\Lambda \setminus B_R(x)}$. Taking the inner product in (25) and applying Cauchy-Schwarz with (29) gives
   $$\bigl|R_W(i\omega_k)_{xx} - R_0(i\omega_k)_{xx}\bigr| \le \|R_W(i\omega_k)\|_{\mathrm{op}}\, \bigl\|T_{\partial} P_{\partial_{\mathrm{in}}} R_0(i\omega_k) \delta_x\bigr\|_2^2 \le \frac{1}{|\omega_k|} \frac{(4t/g)^{2R+2}}{(1 - 4t/g)^2},$$
   which proves (26).

3. By Lemma 1 eq. (16), for each bosonic frequency $\nu_n \neq 0$,
   $$\bigl|\chi_x(i\nu_n; W) - \chi_x^{(0)}(i\nu_n; W)\bigr| = \frac{1}{\beta}\left|\sum_{k \in \mathbb{Z}} \bigl(R_W(i\omega_k)_{xx} R_W(i\omega_k + i\nu_n)_{xx} - R_0(i\omega_k)_{xx} R_0(i\omega_k + i\nu_n)_{xx}\bigr)\right|.$$
   Set $\delta_k := R_W(i\omega_k)_{xx} - R_0(i\omega_k)_{xx}$. Adding and subtracting $R_W(i\omega_k)_{xx} R_0(i\omega_k + i\nu_n)_{xx}$ and using $|R_W(i\omega_k)_{xx}| \le |\omega_k|^{-1}$ and $|R_0(i\omega_k + i\nu_n)_{xx}| \le |\omega_k + \nu_n|^{-1}$ together with $|\delta_k| \le \eta |\omega_k|^{-1}$ from (26), where $\eta := \frac{(4t/g)^{2R+2}}{(1 - 4t/g)^2}$, the triangle inequality and Cauchy-Schwarz give
   $$\bigl|\chi_x(i\nu_n; W) - \chi_x^{(0)}(i\nu_n; W)\bigr| \le \frac{1}{\beta} \sum_{k \in \mathbb{Z}} \bigl(|\delta_k|\, |\omega_k + \nu_n|^{-1} + |\omega_k|^{-1} |\delta_{k+n}|\bigr) \le \frac{2\eta}{\beta} \sum_{k \in \mathbb{Z}} \frac{1}{\omega_k^2} = \frac{2\eta}{\beta} \cdot \frac{\beta^2}{4} = \frac{\eta}{2\tau},$$
   where we used the exact Euler sum $\sum_{k \in \mathbb{Z}} \frac{1}{(2k+1)^2 \pi^2} = \frac{2}{\pi^2} \cdot \frac{\pi^2}{8} = \frac{1}{4}$. Multiplying by $2U \frac{\Omega^2}{\nu_n^2 + \Omega^2}$ and summing over $n \ge 1$ using $\sum_{n=1}^{\infty} \frac{\Omega^2}{\nu_n^2 + \Omega^2} \le \frac{\Omega^2}{24\tau^2}$ yields
   $$\bigl|a_x(W) - a_x^{(0)}(W)\bigr| \le 2 U \left(\sum_{n=1}^{\infty} \frac{\Omega^2}{\nu_n^2 + \Omega^2}\right) \frac{\eta}{2\tau} \le \frac{U \Omega^2}{24 \tau^2}\, \frac{1}{\tau}\, \frac{(4t/g)^{2R+2}}{(1 - 4t/g)^2}.$$
   Combining this with (23) gives (27). Finally, when $4t/g \le 1/16$ and $R \ge \max\bigl(0, \lceil \frac{\log(g/\tau)}{\log 16}\rceil - 1\bigr)$, we have $(4t/g)^{R+1} \le 16^{-(R+1)} \le \min(1/16, \tau/g)$, and therefore $(4t/g)^{2R+2} \le \tau/g$ for all $\tau > 0$ (both when $\tau \le g$, where $(\tau/g)^2 \le \tau/g$, and when $\tau > g$, where $(4t/g)^{2R+2} \le 1 < \tau/g$). Thus $\frac{1}{g - 4t} \le \frac{16}{15 g}$ and $\frac{1}{\tau}\frac{(4t/g)^{2R+2}}{(1 - 4t/g)^2} \le \frac{1}{g (15/16)^2} = \frac{256}{225 g}$. Since
   $$\frac{16}{15} + \frac{256}{225} = \frac{240 + 256}{225} = \frac{496}{225} \quad \text{and} \quad \frac{496}{225 \times 24} = \frac{62}{675},$$
   equation (28) follows. $\blacksquare$

---

### Theorem 1c (Annealed Expectation of the First Dynamic Cumulant under the Full $\det^2$-Weighted Measure $P_s$)

*Let $\Lambda$ be a finite simple graph of maximum degree $D \le 4$ whose graph balls satisfy the quadratic polynomial volume bound*
$$\bigl|B_R(x)\bigr| \le 2 R^2 + 2 R + 1 \qquad \text{for all } x \in \Lambda \text{ and integers } R \ge 0$$
*(in particular, any 1D periodic ring $\mathbb{Z}/L\mathbb{Z}$, where $|B_R(x)| \le 2R+1 \le 2R^2+2R+1$, or any 2D square lattice/torus $(\mathbb{Z}/L\mathbb{Z})^2$ or subgraph thereof, where $|B_R(x)|$ is bounded by the $\mathbb{Z}^2$ $\ell^1$-ball cardinality $1 + 4\sum_{r=1}^R r = 2R^2 + 2R + 1$). Assume $0 < g \le U/4$, $0 \le t \le g/64$, and $0 < \Omega \le \tau \le U/16$. Choose the adaptive buffer radius*
$$R(\tau, g) := \max\!\left(0,\; \left\lceil \frac{\log(g/\tau)}{\log 16}\right\rceil - 1\right). \tag{30}$$
*Then under the full interacting static marginal $P_s$ of (6):*
1. *(Parameterized finite-temperature bound): Uniformly in $|\Lambda|$, $\mu \in \mathbb{R}$, and $x \in \Lambda$,*
   $$\mathbb{E}_{P_s}\bigl[a_x(W)\bigr] \le \frac{U \Omega^2}{24 \tau^2}\left[\frac{496}{225 g} + \frac{2R^2 + 2R + 1}{2\tau} \exp\!\left(-\frac{U}{48\tau}\right)\right] < \left(\frac{62}{675}\frac{U}{g} + 12\right)\frac{\Omega^2}{\tau^2}. \tag{31}$$
2. *(Explicit constant at $g = U/4$): Setting $g = U/4$ (valid whenever $0 \le t \le U/256$ and $0 < \Omega \le \tau \le U/16$),*
   $$\mathbb{E}_{P_s}\bigl[a_x(W)\bigr] \le \frac{8348}{675}\,\frac{\Omega^2}{\tau^2} < \frac{25}{2}\,\frac{\Omega^2}{\tau^2}. \tag{32}$$
3. *(Linear temperature ray $\tau = C \Omega$): Along any linear ray $\tau = C \Omega$ with $C \ge 1$, the annealed first dynamic cumulant is uniformly bounded for all $0 < \Omega \le U/(16 C)$ by $\mathbb{E}_{P_s}[a_x(W)] < \frac{8348}{675 C^2}$, and its adiabatic limit satisfies*
   $$\limsup_{\Omega \to 0^+,\, \tau = C \Omega} \mathbb{E}_{P_s}\bigl[a_x(W)\bigr] \le \frac{62}{675 C^2}\frac{U}{g} = \frac{248}{675 C^2} < \frac{1}{2 C^2} \qquad (g = U/4). \tag{33}$$

#### Proof of Theorem 1c
Fix $x \in \Lambda$ and let $\mathcal{G}_R(x) := \{b_0 \in \mathbb{R}^{\Lambda} : B_R(x) \cap D_g(b_0) = \emptyset\}$ be the event that $|W_y| \ge g$ for all $y \in B_R(x)$.
- On $\mathcal{G}_R(x)$, Theorem 1b eq. (28) applies with $R = R(\tau, g)$ and gives $a_x(W) \le \frac{62}{675}\frac{U \Omega^2}{\tau^2 g}$.
- On the complement $\mathcal{G}_R(x)^c = \bigcup_{y \in B_R(x)} \{y \in D_g(b_0)\}$, the universal bound (9) gives $a_x(W) \le \frac{U \Omega^2}{48 \tau^3}$, while a union bound combined with `LINEAR8` Proposition P16 eq. (12) for singletons $B = \{y\}$ ($|B| = 1$) gives
  $$P_s\bigl(\mathcal{G}_R(x)^c\bigr) \le \sum_{y \in B_R(x)} P_s\bigl(\{y\} \subset D_g(b_0)\bigr) \le |B_R(x)| \exp\!\left(-\frac{U}{48\tau}\right) \le (2R^2 + 2R + 1) \exp\!\left(-\frac{U}{48\tau}\right).$$
  Splitting $\mathbb{E}_{P_s}[a_x(W)] = \mathbb{E}_{P_s}[a_x(W)\mathbf{1}_{\mathcal{G}_R(x)}] + \mathbb{E}_{P_s}[a_x(W)\mathbf{1}_{\mathcal{G}_R(x)^c}]$ yields the first inequality of (31).

To prove the uniform rare-defect bound in (31), put $u := \frac{U}{48\tau} \ge \frac{16}{48} = \frac{1}{3}$. Since $g \le U/4$, we have $\frac{g}{\tau} \le \frac{U}{4\tau} = 12 u$. When $R = R(\tau, g) \ge 1$, the definition (30) implies $\frac{\log(g/\tau)}{\log 16} > R$, so $16^R < \frac{g}{\tau} \le 12 u$. By Bernoulli's inequality, for every integer $R \ge 1$,
$$16^R = (1 + 15)^R \ge 1 + 15 R > 12 R \implies R < \frac{16^R}{12} < u.$$
When $R = 0$, $R = 0 < \frac{1}{3} \le u$ also holds. Hence $R \le u$ for all $\tau \le U/16$ and $g \le U/4$. Substituting $R \le u$ and $\frac{U}{48\tau} = u$ into the rare-defect contribution gives
$$\frac{U \Omega^2}{24 \tau^2} \cdot \frac{2R^2 + 2R + 1}{2\tau} e^{-u} = \frac{\Omega^2}{\tau^2} \cdot u (2R^2 + 2R + 1) e^{-u} \le \frac{\Omega^2}{\tau^2} (2u^3 + 2u^2 + u) e^{-u}.$$
Since $e^u = \sum_{m=0}^{\infty} \frac{u^m}{m!} > u + \frac{u^2}{2} + \frac{u^3}{6}$ for all $u > 0$, multiplying by $12 e^{-u}$ gives
$$2u^3 + 2u^2 + u \le 2u^3 + 6u^2 + 12u = 12\left(\frac{u^3}{6} + \frac{u^2}{2} + u\right) < 12 e^u \implies (2u^3 + 2u^2 + u) e^{-u} < 12.$$
This proves the second inequality of (31). Setting $g = U/4$ gives $\frac{62}{675}\cdot 4 + 12 = \frac{248 + 8100}{675} = \frac{8348}{675} < \frac{8437.5}{675} = \frac{25}{2}$, proving (32). Finally, for any fixed $C \ge 1$ and $\tau = C \Omega$, as $\Omega \to 0^+$ we have $u = \frac{U}{48 C \Omega} \to +\infty$ while $R(\tau, g) = O(\log(1/\Omega))$, so $(2R^2 + 2R + 1) u e^{-u} \to 0$, proving (33). $\blacksquare$

---

## 3. Part II: Sharp Obstructions to Upgrading Annealed Static Control to a 2D Linear Pairing Ceiling

Part I closes Step (1) of the annealed static program: under the full $\det^2$-weighted static marginal $P_s$, the `STATIC-MODE` resonance divergence $\tau^{-3}$ is completely eliminated from the annealed first dynamic cumulant $\mathbb{E}_{P_s}[a_x(W)]$. We now determine whether Steps (2) and (3)—combining the sparse defect distribution of $D_g(b_0)$ with reflection positivity / chessboard factorization or a Fröhlich-Spencer / Aizenman separating-contour polymer expansion—can upgrade `LINEAR4`'s $2/3$ exponent ($k_{\mathrm{B}} T_{\mathrm{pair}} \lesssim (U \Omega^2)^{1/3} \log^{1/3}$) to a linear-in-$\Omega$ pair-correlation decay theorem in 2D. We prove three exact obstructions showing that both decoupling routes fail.

### Theorem 2a (Reflection-Positivity / Chessboard Obstruction for Static Fermion Determinant Kernels)

*Let $\Lambda = \Lambda_+ \sqcup \Lambda_-$ be a reflection-symmetric bipartite graph with involutive graph automorphism $\vartheta : \Lambda \to \Lambda$ exchanging $\Lambda_+$ and $\Lambda_-$. For $u \in \mathbb{R}^{\Lambda_+}$ and $v \in \mathbb{R}^{\Lambda_-}$, write $h(u, v) := -t A_{\Lambda} + \operatorname{diag}(u \oplus (v \circ \vartheta))$. Consider both candidate reflection kernels:*
- *the **direct reflection kernel** $K_{\mathrm{direct}}(u, v) := \det\!\left(I + e^{-\beta h(u, v)}\right)^2$; and*
- *the **particle-hole symmetric reflection kernel** $M_1(u, v) := \det\!\left(e^{\beta h(u, -v)/2} + e^{-\beta h(u, -v)/2}\right)$ (for one spin) and $M_2(u, v) := M_1(u, v)^2$ (for two spins, which differs from $\det(I + e^{-\beta h(u, -v)})^2$ only by the rank-one gauge multiplier $e^{\beta \sum_{x \in \Lambda_+} u_x} e^{-\beta \sum_{y \in \Lambda_-} v_y}$).*

*Then:*
1. *(Dimer direct reflection failure): On the 2-site dimer $\Lambda = \{1, 2\}$ with $\beta = 1$: for every $t > 0$ and $b > 0$, $K_{\mathrm{direct}}(b, b) K_{\mathrm{direct}}(-b, -b) < K_{\mathrm{direct}}(b, -b)^2$. At $t = 2$ and $b_1, b_2 \in \{-1, +1\}$, the $2 \times 2$ principal minor of $K_{\mathrm{direct}}$ is CERTIFIED to be*
   $$\det_{a, b \in \{-1, +1\}} K_{\mathrm{direct}}(a, b) = 16\bigl(\cosh 2 + \cosh 1\bigr)^4 - 16\bigl(\cosh\sqrt{5} + 1\bigr)^4 \in [-4593.0291530660,\; -4593.0291530659] < 0. \tag{34}$$
2. *(Dimer particle-hole reflection positivity): On the 2-site dimer $\Lambda = \{1, 2\}$, for every $\beta > 0$ and $t \in \mathbb{R}$, the particle-hole symmetric kernel*
   $$M_1^{\mathrm{dimer}}(b_1, b_2) = 2\cosh\!\left(\frac{\beta(b_1 - b_2)}{2}\right) + 2\cosh\!\left(\beta\sqrt{\left(\frac{b_1 + b_2}{2}\right)^2 + t^2}\right) \tag{35}$$
   *is positive semidefinite on $\mathbb{R} \times \mathbb{R}$, and therefore so is its Hadamard square $M_2^{\mathrm{dimer}} = (M_1^{\mathrm{dimer}})^2$.*
3. *(Cycle / torus particle-hole reflection failure): On the 4-site zero-flux ring $C_4 = \{0, 1, 2, 3\}$ with reflection $\vartheta(0) = 3, \vartheta(1) = 2$ across the two cut bonds $(0,3)$ and $(1,2)$, at $\beta = 1$ and $t = 2$, on the three-point integer set $S = \{(-2, -2), (-2, -1), (-1, -1)\} \subset \mathbb{Z}^2$, both the one-spin and two-spin particle-hole symmetric kernels have strictly negative $3 \times 3$ principal minors (CERTIFIED by outward ball arithmetic and independent 16-state Fock-space trace):*
   $$\det_{u, v \in S} M_1^{C_4}(u, v) \in [-203.8547627359,\; -203.8547627358] < 0, \tag{36}$$
   $$\det_{u, v \in S} M_2^{C_4}(u, v) \in [-5.8763809480 \times 10^{10},\; -5.8763809479 \times 10^{10}] < 0. \tag{37}$$
   *Because $\det(I + e^{-\beta h(u, -v)})^2 = D(u)^{-1} M_2^{C_4}(u, v) D(v)$ with $D(u) := \exp(\beta(u_1 + u_2)) > 0$, the unshifted particle-hole reflected kernel $\widetilde{M}_2^{C_4}(u, v) := \det(I + e^{-\beta h(u, -v)})^2$ is diagonally similar to $M_2^{C_4}(u, v)$ (so every principal minor $\det_{u,v \in S} \widetilde{M}_2^{C_4}(u, v) = \det_{u,v \in S} M_2^{C_4}(u, v)$ is identical and strictly negative on $S$). Furthermore, on any larger bipartite ring $C_{2L}$ ($L \ge 2$) or 2D square torus $(\mathbb{Z}/2L\mathbb{Z})^2$ containing an induced 4-site cycle $C_4$, taking the static field $|W_z| \to +\infty$ on all sites $z \notin C_4$ decouples the external sites and recovers the $C_4$ minor by continuity. Consequently, reflection positivity and chessboard factorization fail for the static fermion determinant on periodic rings and 2D tori.*

#### Proof of Theorem 2a
1. For the 2-site dimer $h(b_1, b_2) = \begin{pmatrix} b_1 & -t \\ -t & b_2 \end{pmatrix}$ at $\beta = 1$, the eigenvalues are $\frac{b_1 + b_2}{2} \pm \sqrt{(\frac{b_1 - b_2}{2})^2 + t^2}$, so
   $$\det\!\left(I + e^{-h(b_1, b_2)}\right) = 1 + e^{-b_1} + e^{-b_2} + e^{-(b_1 + b_2)} = 2 e^{-(b_1 + b_2)/2}\left[\cosh\!\left(\frac{b_1 + b_2}{2}\right) + \cosh\!\sqrt{\left(\frac{b_1 - b_2}{2}\right)^2 + t^2}\right].$$
   Comparing $K_{\mathrm{direct}}(b, b)^{1/4} K_{\mathrm{direct}}(-b, -b)^{1/4} = 2(\cosh b + \cosh t)$ with $K_{\mathrm{direct}}(b, -b)^{1/2} = 2(1 + \cosh\sqrt{b^2 + t^2})$, expand in the even power series of $b$ and $t$:
   $$\cosh\sqrt{b^2 + t^2} - 1 - (\cosh b - 1) - (\cosh t - 1) = \sum_{n=2}^{\infty} \frac{(b^2 + t^2)^n - b^{2n} - t^{2n}}{(2n)!} > \frac{2 b^2 t^2}{4!} = \frac{b^2 t^2}{12} > 0$$
   for all $b, t > 0$ by the binomial theorem! Thus $K_{\mathrm{direct}}(b, b) K_{\mathrm{direct}}(-b, -b) < K_{\mathrm{direct}}(b, -b)^2$ for all $b, t > 0$. Setting $b = 1, t = 2$ gives (34), which is independently enclosed in `replay.py` (`flint.arb`) and `independent.py` (`mpmath.iv` and 4-state Fock trace).

2. Replacing $b_2$ by $-b_2$ and multiplying $\det(I + e^{-\beta h(b_1, -b_2)})$ by $e^{\beta(b_1 - b_2)/2}$ gives (35). For any finite sequence $\{c_j\}_{j=1}^m \subset \mathbb{R}$ and points $\{x_j\}_{j=1}^m \subset \mathbb{R}$,
   $$\sum_{j, k=1}^m c_j c_k \cosh\!\left(\frac{\beta(x_j - x_k)}{2}\right) = \frac{1}{2}\left(\sum_{j=1}^m c_j e^{\beta x_j / 2}\right)^2 + \frac{1}{2}\left(\sum_{j=1}^m c_j e^{-\beta x_j / 2}\right)^2 \ge 0,$$
   so the first term of (35) is positive semidefinite. For the second term, put $s_{jk} := \frac{x_j + x_k}{2}$; because $\cosh(\beta\sqrt{s^2 + t^2}) = \sum_{n=0}^{\infty} \frac{\beta^{2n}}{(2n)!} (s^2 + t^2)^n = \sum_{m=0}^{\infty} a_m(\beta, t) s^{2m}$ is an entire function of $s^2$ with all Taylor coefficients $a_m(\beta, t) \ge 0$, and for each $m \ge 0$ the Hankel form
   $$\sum_{j, k=1}^m c_j c_k (x_j + x_k)^{2m} = \sum_{r=0}^{2m} \binom{2m}{r} \left(\sum_{j=1}^m c_j x_j^r\right)\left(\sum_{k=1}^m c_k x_k^{2m-r}\right)$$
   is not automatically nonnegative term-by-term in $r$, we instead give a direct Fock-space proof that $\cosh(\beta\sqrt{(\frac{b_1+b_2}{2})^2 + t^2})$ (and indeed $M_1^{\mathrm{dimer}}(b_1, b_2)$) is positive semidefinite:
   On the 2-site one-spin Fock space $\mathcal{F} = \operatorname{span}\{|00\rangle, |10\rangle, |01\rangle, |11\rangle\}$, apply the unitary particle-hole transformation $U_{\mathrm{ph}} := c_2 - c_2^\dagger$ on site 2 (so $U_{\mathrm{ph}}^2 = -I$, $U_{\mathrm{ph}}^\dagger = -U_{\mathrm{ph}} = U_{\mathrm{ph}}^{-1}$, $U_{\mathrm{ph}} c_2 U_{\mathrm{ph}}^{-1} = -c_2^\dagger$, and $U_{\mathrm{ph}} (n_2 - \frac{1}{2}) U_{\mathrm{ph}}^{-1} = -(n_2 - \frac{1}{2})$). Under $U_{\mathrm{ph}}$, the centered Hamiltonian $H(b_1, -b_2) = b_1(n_1 - \frac{1}{2}) - b_2(n_2 - \frac{1}{2}) - t(c_1^\dagger c_2 + c_2^\dagger c_1)$ is unitarily equivalent to
   $$\widetilde{H}(b_1, b_2) := U_{\mathrm{ph}} H(b_1, -b_2) U_{\mathrm{ph}}^{-1} = b_1\left(n_1 - \frac{1}{2}\right) + b_2\left(n_2 - \frac{1}{2}\right) + t\left(c_1^\dagger c_2^\dagger + c_2 c_1\right).$$
   In the occupation basis, the odd-parity subspace $\operatorname{span}\{|10\rangle, |01\rangle\}$ is annihilated by $c_1^\dagger c_2^\dagger + c_2 c_1$ and has eigenvalues $\pm\frac{b_1 - b_2}{2}$, contributing $2\cosh(\frac{\beta(b_1 - b_2)}{2})$. On the even-parity subspace $\operatorname{span}\{|00\rangle, |11\rangle\}$, writing $D(b) := \operatorname{diag}(-\frac{b}{2}, \frac{b}{2})$ and $J := \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, we have $-\beta \widetilde{H}_{\mathrm{even}}(b_1, b_2) = \beta D(b_1) + \beta D(b_2) - \beta t J$. By the Duhamel expansion of $\operatorname{Tr}_{\mathrm{even}}\exp(\beta D(b_1) + \beta D(b_2) - \beta t J)$, since $J$ flips $|00\rangle \leftrightarrow |11\rangle$, only even powers $(-\beta t J)^{2m} = (\beta t)^{2m} I$ have nonzero diagonal entries, and for an ordered simplex $0 < u_1 < \dots < u_{2m} < 1$ the alternating signs of $D(b_1) + D(b_2)$ on the two states yield the factored integrand $\varphi_{m,\mathbf{u}}(b_1)\varphi_{m,\mathbf{u}}(b_2)$ where $\varphi_{m,\mathbf{u}}(b) := \exp(\frac{\beta b}{2}\sum_{j=0}^{2m} (-1)^j (u_{j+1} - u_j))$. Integrating over the simplex with the positive measure $(\beta t)^{2m} du_1\cdots du_{2m}$ and summing over the two basis states expresses $2\cosh(\beta\sqrt{(\frac{b_1+b_2}{2})^2 + t^2})$ as a positive integral of symmetric rank-one kernels $\varphi(b_1)\varphi(b_2)$, proving that $M_1^{\mathrm{dimer}}$ and $M_2^{\mathrm{dimer}} = (M_1^{\mathrm{dimer}})^2$ are positive semidefinite by the Schur product theorem.

3. Why does the Fock-space positivity of part 2 fail on the 4-site zero-flux ring $C_4$? On a bipartite ring with $L \equiv 0 \pmod 4$ and zero magnetic flux, a unitary particle-hole transformation on $\Lambda_- = \{2, 3\}$ accompanied by the bipartite sublattice sign $(-1)^x$ preserves the sign of hopping on bonds inside $\Lambda_+$ and $\Lambda_-$, while changing the hopping term on the two cut bonds $(0,3)$ and $(1,2)$ to pairing terms with **opposite** fermion-ordering signs because a closed loop of 4 sites carries zero flux rather than Lieb's canonical $\pi$-flux (`Lieb 1994`). Explicitly, at $\beta = 1, t = 2$ on the three integer configurations $u^{(1)} = (-2, -2)$, $u^{(2)} = (-2, -1)$, $u^{(3)} = (-1, -1)$ in $\mathbb{Z}^2$, the $4 \times 4$ matrix is
   $$h(u, -v) = \begin{pmatrix} u_1 & -2 & 0 & -2 \\ -2 & u_2 & -2 & 0 \\ 0 & -2 & -v_2 & -2 \\ -2 & 0 & -2 & -v_1 \end{pmatrix}.$$
   In `replay.py`, $M_1^{C_4}(u^{(i)}, u^{(j)}) = \det(e^{h(u^{(i)}, -u^{(j)})/2} + e^{-h(u^{(i)}, -u^{(j)})/2})$ and $M_2^{C_4}(u^{(i)}, u^{(j)}) = M_1^{C_4}(u^{(i)}, u^{(j)})^2$ are evaluated in 128-bit rigorous ball arithmetic (`flint.arb_mat.exp` and `flint.arb_mat.det`), and in `independent.py` they are independently evaluated by diagonalizing $h(u^{(i)}, -u^{(j)})$ at 80-digit precision and summing $e^{-E_S}$ over all $2^4 = 16$ occupation states of the one-spin Fock space. Both methods agree to more than 25 significant digits and certify (36) and (37). $\blacksquare$

---

### Proposition 2b (Heuristic Synthesis: The 2D Separating-Contour vs. Vacuum-Loop Duality Obstruction)

*(Status: **HEURISTIC (method-barrier synthesis)** summarizing how the proved mechanisms of `LINEAR7` Theorem Z, `LINEAR8` Lemma H, and `LINEAR11` Theorem 1 interact along a 2D separating contour.)*

*Consider the spinful Holstein model on the 2D torus $\Lambda = (\mathbb{Z}/L\mathbb{Z})^2$ with local s-wave pair field $\Delta_x = c_{x\downarrow} c_{x\uparrow}$ and imaginary-time pair correlator*
$$C_{\Delta}(x, y) := \frac{1}{\beta} \int_0^{\beta} \langle \Delta_x^\dagger(s) \Delta_y(0) \rangle\, ds = \int_{\mathbb{R}^{\Lambda}} P_s(db_0)\, \frac{\mathbb{E}_v\bigl[\det(I + Y_{b_0+v})^2\, \mathcal{W}_{b_0+v}(x, y)\bigr]}{\mathbb{E}_v\bigl[\det(I + Y_{b_0+v})^2\bigr]}, \tag{38}$$
*where $Y_w := \mathcal{T}\exp(-\int_0^{\beta} h_{w(u)}\, du)$ is the one-spin time-ordered propagator for the total space-time field $w(u) = b_0 - \mu\mathbf{1} + v(u)$ and $\mathcal{W}_w(x, y) := \frac{1}{\beta}\int_0^{\beta} |G_w(s, 0; x, y)|^2\, ds$ is the conditional Wick pair propagator.*

*Fix a site $x \in \Lambda$ and suppose $b_0 \in \mathbb{R}^{\Lambda}$ has a connected $g$-gapped separating annulus $\Gamma \subset \Lambda \setminus D_g(b_0)$ of thickness $M \ge 1$ separating an interior domain $U_0 \ni x$ (which may contain defect clusters of $D_g(b_0)$) from $y \in \Lambda \setminus (U_0 \cup \Gamma)$. Then the two standard ways to localize $C_{\Delta}(x, y)$ across $\Gamma$ encounter the following mutually dual obstructions:*
1. *(Uncut dynamic vacuum loops — `LINEAR7` Theorem Z determinant zeros inside $U_0$): If the boundary hopping $T_{\partial U_0}$ between $U_0$ and $\Gamma$ is kept inside the determinant weight $\det(I + Y_{b_0+v})^2$, then when $U_0 \cap D_g(b_0)$ contains an induced 4-site star $K_{1,3} \subset (\mathbb{Z}/L\mathbb{Z})^2$ ($L \ge 4$) at the resonant static reference $W|_{K_{1,3}} = (0, 0, 0, 0)$ (isolated from $\Gamma$ by large static fields $|W_z| \gg t$ on neighboring sites), `LINEAR7` Theorem Z (`ADIABATIC/LINEAR7/RIGOR.md`, lines 211--235, 335--340, reviewed CERTIFIED/PROVED) proves that for the certified inverse-hopping values $\beta t \in \{1, 10, 20, 40, 100, 1000\}$ there exists a smooth time-mean-zero dynamic trajectory $v$ supported on the three leaves of $K_{1,3}$ with dimensionless action sup-norm $\beta \|v\|_{\infty} \le \kappa_{\mathrm{hi}}(\beta t)$ (specifically $\beta \|v\|_{\infty} \le 51/10$ at $\beta t = 20$ and $\beta \|v\|_{\infty} \le 5$ at $\beta t \in \{40, 100, 1000\}$) such that*
   $$\det(I + Y_{W_{\mathrm{ref}} + v}) = 0. \tag{39}$$
   *At the determinant zero (39), $(I + Y_{W_{\mathrm{ref}}+v})^{-1}$ has a pole and $\mathcal{W}_{W_{\mathrm{ref}}+v}(x, y)$ is unbounded, so no conditional Combes-Thomas bound on $\mathcal{W}_{b_0+v}(x, y)$ across $\Gamma$ holds uniformly over all static defect configurations $W|_{U_0}$ and bounded dynamic histories $\beta \|v\|_{\infty} \le 5$.*
2. *(Cut boundary hopping — `LINEAR8` Lemma H and `LINEAR11` perimeter penalty): If the boundary hopping $T_{\partial U_0}$ across the separating contour $\partial_{\mathrm{out}} U_0$ is removed from the quantum thermal trace via the Duhamel / time-Schatten Hölder interpolation of `LINEAR8` Lemma H (`ADIABATIC/LINEAR8/RIGOR.md`, lines 56--90, eqs. H1, H5) or the block determinant factorization of `LINEAR11` (`ADIABATIC/LINEAR11/RIGOR.md`, Theorem 1), the Hilbert-space operator norm $\|T_{\partial U_0}\|_{\mathrm{op}} \le 8 t |\partial_{\mathrm{out}} U_0|$ produces a boundary-cutting factor of the form*
   $$\exp\!\left(\frac{1}{2}\beta^2 \|T_{\partial U_0}\|_{\mathrm{op}}^2\right) \le \exp\!\left(32\, \beta^2 t^2 |\partial_{\mathrm{out}} U_0|^2\right) \quad \text{(`LINEAR8` Lemma H)} \qquad \text{or} \qquad \exp\!\left(c\, \beta t |\partial_{\mathrm{out}} U_0|\right) \quad \text{(`LINEAR11`)}, \qquad |\partial_{\mathrm{out}} U_0| \ge 4 M \quad (d = 2), \tag{40}$$
   *where any contour surrounding an $\ell^1$ ball of radius $M$ in $\mathbb{Z}^2$ has perimeter $|\partial_{\mathrm{out}} U_0| \ge 4 M$. Consequently, in $d = 2$ the boundary cut penalty grows at least exponentially with the contour perimeter as $\exp(c' \frac{t}{\tau} M)$, which dominates any fixed-rate Combes-Thomas propagator decay $\exp(-\gamma M)$ whenever $\tau \lesssim t$.*

#### Justification of Proposition 2b
Part 1 summarizes the mechanism of `LINEAR7/RIGOR.md` Theorem Z: on the square torus $(\mathbb{Z}/L\mathbb{Z})^2$ with $L \ge 4$, a 4-site star $K_{1,3}$ (center site plus three neighbors) occurs as an induced subgraph when the remaining neighbors are isolated by large static fields in $\Gamma$. At the static reference $W|_{K_{1,3}} = 0$, the leaf-supported zero-mean dynamic perturbation $v$ certified in `LINEAR7` Theorem Z satisfies $\beta \|v\|_{\infty} \le 5$ at $\beta t \in \{40, 100, 1000\}$ (and $\le 51/10$ at $\beta t = 20$) and drives $\det(I + Y)$ through zero. On the zero locus $\det(I + Y_{b_0+v}) = 0$, the conditional Green's function $G_{b_0+v} = (\partial_u + h_{b_0+v})^{-1}$ has a pole; although the polynomial combination $\det(I + Y_{b_0+v})^2 \mathcal{W}_{b_0+v}(x, y)$ extends smoothly across the zero locus by Jacobi's adjugate identity (`LINEAR8/RIGOR.md` line 152), one cannot factorize $\mathcal{W}_{b_0+v}(x, y)$ out of the expectation $\mathbb{E}_v[\det(I + Y_{b_0+v})^2 (\cdots)]$ using a uniform pointwise bound over all static defect interiors.

For Part 2, to bound the numerator $\mathbb{E}_v[\det(I + Y_{b_0+v})^2 \mathcal{W}_{b_0+v}(x, y)]$ by reference to a block-decoupled trace where $U_0$ is disconnected from $\Lambda \setminus U_0$, `LINEAR8/RIGOR.md` Lemma H removes the boundary hopping operator $T_{\partial U_0}$ (which has Hilbert-space operator norm $\|T_{\partial U_0}\|_{\mathrm{op}} \le 8 t |\partial_{\mathrm{out}} U_0|$ by eq. H1) via time-Schatten Hölder inequalities at the cost of the Gaussian factor $\exp(\frac{1}{2}\beta^2 \|T_{\partial U_0}\|_{\mathrm{op}}^2)$ (eq. H5), while `LINEAR11/RIGOR.md` Theorem 1 obtains a linear-in-$\beta t |\partial_{\mathrm{out}} U_0|$ exponential bound $\exp(c \beta t |\partial_{\mathrm{out}} U_0|)$ for determinant splitting. On $\mathbb{Z}^2$, by the discrete isoperimetric inequality, any finite set $U_0$ containing the $\ell^1$ ball $B_M(x)$ has outer vertex boundary $|\partial_{\mathrm{out}} U_0| \ge 4(M + 1) > 4M$, yielding (40). $\blacksquare$

---

### Theorem 2c (Exact Regime Collapse Under the Gapped Static Defect-Suppression Hypothesis)

*Every annealed static defect-suppression theorem in the `LINEAR6`--`LINEAR10` hierarchy (`LINEAR6` Lemma G3, `LINEAR8` Theorem P64 and Proposition P16) requires the gapped hopping condition*
$$0 < g \le \frac{U}{4}, \qquad 0 \le t \le \frac{g}{64} \implies t \le \frac{U}{256}. \tag{41}$$
*Under (41), the strong-coupling polaronic pair-clustering scale $\tau_{\mathrm{strong}} := 2^{27} t^2 / U$ of `STAGE7R` (`ADIABATIC/LINEAR5/STAGE7R/RIGOR.md`, Zenodo `10.5281/zenodo.24380128`) and the high-temperature kinetic scale $\tau_{\mathrm{high}} := 2^{10} t$ of `STAGE4` (`ADIABATIC/LINEAR5/STAGE4/RESULT.md`) satisfy (**PROVED**):*
$$\frac{2^{27} t^2}{U} \le 2^{19} t, \qquad \min\!\left(2^{10} t,\; \frac{2^{27} t^2}{U}\right) \le 2^{10} t. \tag{42}$$
*Consequently:*
1. *(**PROVED**): Any temperature regime $\tau \ge c t$ in which the dimensionless inverse hopping $\beta t = t/\tau \le c^{-1}$ is bounded—as required for any boundary-cutting expansion of Proposition 2b(2) to have an $O(1)$ per-bond penalty—already lies above (up to the fixed numerical constant $2^{10}/c$) the unconditional, $\Omega$-independent pair-clustering threshold $\tau \ge \min(2^{10} t, 2^{27} t^2 / U)$ proved in `STAGE4` and `STAGE7R`.*
2. *(**HEURISTIC** method-barrier commentary): In the remaining low-temperature adiabatic window $\tau \ll \min(t, t^2/U)$ where the linear ceiling $\tau = C(t, U)\Omega$ is open, we necessarily have $\beta t = t/\tau \gg 1$ and $t \gg \tau$; when $t, U > 0$ are held fixed as $\Omega \to 0^+$, the static-gap hypothesis $t \le g/64 \le U/256$ cannot hold whenever $t > U/256$, and even when $t \le U/256$, taking $\Omega \to 0^+$ along $\tau = C(t, U)\Omega$ sends $\beta t = t/(C\Omega) \to +\infty$, activating the dual contour-vs.-loop barriers of Proposition 2b. Thus the annealed static defect expansion does not improve `LINEAR4`'s $2/3$ exponent $k_{\mathrm{B}} T_{\mathrm{pair}} \lesssim (U \Omega^2)^{1/3} \log^{1/3}$.*

#### Proof of Theorem 2c (Part 1) and Justification of Part 2
Substituting $t / U \le 1/256 = 2^{-8}$ from (41) into $2^{27} t^2 / U = 2^{27} (t/U) t$ gives $2^{27} t^2 / U \le 2^{27 - 8} t = 2^{19} t$, and therefore $\min(2^{10} t, 2^{27} t^2 / U) \le 2^{10} t$, proving (42). By `STAGE4` and `STAGE7R`, equal-time and static pair correlations already decay exponentially at rate $\ge 1/2$ for all $\tau \ge \min(2^{10} t, 2^{27} t^2 / U)$ at **every** phonon frequency $\Omega > 0$, proving Part 1. Part 2 follows by inspecting the parameters in the open regime $\tau < \min(2^{10} t, 2^{27} t^2 / U)$ along $\tau = C(t, U)\Omega$ as $\Omega \to 0^+$: since $\beta t = t / (C \Omega) \to +\infty$, both the determinant-zero regime of Proposition 2b(1) and the perimeter cut penalty of Proposition 2b(2) are active. $\blacksquare$

---

## 4. Verification Summary and Traceability Table

Every constant, identity, and matrix minor in Sections 2 and 3 is verified by `replay.py` and independently checked by `independent.py`, with labels matching `REVIEW.md`:

| Claim / Constant | Location | Value / Statement | Method in `replay.py` | Independent Check in `independent.py` | Label |
|---|---|---|---|---|---|
| `STATIC-MODE` baseline constant | §1 eq. (10) | $\frac{1}{1148} > \frac{1}{1200}$, half $\frac{1}{2400}$ | `fractions.Fraction` exact arithmetic | Pure integer `(p, q)` arithmetic (`math.gcd`) | **CERTIFIED** |
| Endpoint resonance rarity | Theorem 1a eq. (14) | $P_s(\mathcal{E}_{\mathrm{res}}) \le e^{-U/(24\tau)}$ for $\tau < g/2$ | Analytic deduction from `LINEAR8` Prop. P16 | Checked in proof & scoping | **PROVED** |
| Gapped susceptibility & cumulant | Lemma 1 eqs. (16)--(18) | $0 \le \chi_x(i\nu_n; W) \le \frac{1}{2g_0}$, $a_x(W) \le \frac{U\Omega^2}{24\tau^2 g_0}$ | Spectral partial-fraction & Matsubara check | Time-domain Gauss-Legendre cross-check | **PROVED** |
| Vanishing 1st-order boundary & 2-step resolvent | Theorem 1b eqs. (24)--(27) | $(R_0 T_{\partial} R_0)_{xx} = 0$, exact 2-step identity, $\frac{1}{\tau}\eta$ bound | 128-bit `flint.acb_mat` exact enclosure (`max_ident_err = 0`) | Time-domain Gauss-Legendre cross-check of $a_x(W)$ | **PROVED** / **CERTIFIED** |
| Local-buffer constant at $4t/g \le 1/16$ | Theorem 1b eq. (28) | $\frac{16}{15} + \frac{256}{225} = \frac{496}{225}$, $\frac{496}{225 \times 24} = \frac{62}{675}$ | `fractions.Fraction` + mutant guard | Pure integer `(p, q)` arithmetic | **PROVED** / **CERTIFIED** |
| Rare-defect polynomial majorant | Theorem 1c eq. (31) | $16^R \ge 12 R$, $(2u^3+2u^2+u)e^{-u} < 12$ on $|B_R(x)| \le 2R^2+2R+1$ | `fractions.Fraction` Taylor coefficient comparison + mutant guards | Pure integer `(p, q)` arithmetic | **PROVED** / **CERTIFIED** |
| Combined annealed constant at $g=U/4$ | Theorem 1c eqs. (32)--(33) | $\frac{248}{675} + 12 = \frac{8348}{675} < \frac{25}{2}$, ray limit $\frac{248}{675 C^2} < \frac{1}{2 C^2}$ | `fractions.Fraction` + finite-lattice ray check + mutant guards | Pure integer `(p, q)` arithmetic | **PROVED** / **CERTIFIED** |
| Dimer direct reflection failure | Theorem 2a(1) eq. (34) | $2 \times 2$ minor on $\{-1, +1\}$ at $t=2$: $-4593.029153\ldots < 0$ | 128-bit `flint.arb` interval enclosure + mutant guard | `mpmath.iv` interval arithmetic + 4-state Fock trace | **PROVED (computer-assisted)** / **CERTIFIED** |
| Dimer PH reflection positivity | Theorem 2a(2) eq. (35) | $M_1^{\mathrm{dimer}}, M_2^{\mathrm{dimer}} \succeq 0$; $3 \times 3$ minor on $\{-2,0,2\}$ at $t=2$: $+35.768871\ldots > 0$ | Analytic Fock Duhamel proof + 128-bit `flint.arb` enclosure | 4-state centered Fock trace | **PROVED** / **CERTIFIED** |
| $C_4$ ring PH reflection failure (1 & 2 spin) | Theorem 2a(3) eqs. (36)--(37) | $3 \times 3$ minors on $\{(-2,-2),(-2,-1),(-1,-1)\}$ at $t=2$: $M_1^{C_4} \approx -203.8548 < 0$, $M_2^{C_4} \approx -5.87638 \times 10^{10} < 0$ | 128-bit `flint.arb_mat.exp` & `.det` + mutant guards | 16-state centered Fock trace in 80-digit `mpmath` | **PROVED (computer-assisted)** / **CERTIFIED** |
| 2D separating-contour vs. vacuum-loop synthesis | Proposition 2b eqs. (39)--(40) | `LINEAR7` Theorem Z ($\beta \|v\|_{\infty} \le 5$) vs. `LINEAR8` Lemma H / `LINEAR11` | Cited from reviewed `LINEAR7`, `LINEAR8`, `LINEAR11` | Cross-checked against source `RIGOR.md` files | **HEURISTIC (method-barrier synthesis)** |
| Regime collapse under $t \le g/64 \le U/256$ | Theorem 2c eqs. (41)--(42) | $2^{27}t^2/U \le 2^{19}t$, $\min(2^{10}t, 2^{27}t^2/U) \le 2^{10}t$ | `fractions.Fraction` + mutant guard | Pure integer arithmetic | **PROVED** (Part 1) / **HEURISTIC** (Part 2) |
| Finite-lattice 1D ($L=12$) & 2D ($4 \times 4$) buffer tests | §2 Theorem 1b | Distant `STATIC-MODE` resonance suppressed by $> 4.5 \times 10^4$ (1D) and $> 1.5 \times 10^8$ (2D) | Exact spectral partial-fraction sum in `replay.py` | 96-node imaginary-time Gauss-Legendre quadrature in `independent.py` (diff $< 8 \times 10^{-12}$) | **NUMERICAL** |
