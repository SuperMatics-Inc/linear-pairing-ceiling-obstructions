# Amendment to `W/MASSIVE/BARRIERS2-PAPER/main.tex` and `refs.bib`

This document provides exact, self-contained replacement LaTeX text for `W/MASSIVE/BARRIERS2-PAPER/main.tex` and `W/MASSIVE/BARRIERS2-PAPER/refs.bib` to incorporate the $U_{\rm eff}$-uniform Hubbard-SSH extension, the combined attractive and repulsive minimum-ceiling theorems, and the exact $U$-non-monotonicity counterexamples. The existing source files in `W/MASSIVE/BARRIERS2-PAPER/` are left untouched.

## Summary of Scope and Labels

- **Modified existing labels in `main.tex`:** `sec:survives`, `tab:routes`, `thm:gc`, `lem:canon`, `thm:canon`, `sec:notclaimed`, `sec:open`.
- **Unchanged existing theorem at $\Ueff=0$:** `thm:routes` (Theorem 5.4, items (i) and (iii) genuinely require $\Ueff=0$; item (ii) is an operator identity on bond commutators that holds regardless of $\Ueff$, and the theorem stays scoped to the pure bond-SSH model).
- **New labels added to `main.tex`:** `eq:Hhubssh`, `rem:uelschi`, `thm:min-att`, `thm:min-rep`, `prop:nonmonotone`.
- **New BibTeX keys added to `refs.bib`:** `uelschi1999`, `uelschi2004`, `frohlich2005`.


## 1. Abstract (`main.tex` lines 60-66)

Replace lines 60-66 (`Third, for the pure bond-SSH model ... no materials claim is made.`) with:

```latex
Third, for the Hubbard-Holstein-SSH model at every effective on-site interaction
$\Ueff\in\R$, the high-temperature regime closes with identical constants: for
$\beta|t|+\beta\Gb\le2^{-10}$ the pair correlator is at most
$(341/103)(32/341)^{d}$, uniformly in $\Ueff$, phonon frequencies, chemical potential
and density, so $k_B\Tpair\le1024(|t|+\Gb)$, while three further proof routes
remain obstructed at $\Ueff=0$. Combining this uniform ceiling with strong-coupling
bounds gives explicit minimum ceilings for $\Ueff<0$ at all densities and for
$\Ueff>0$ at half filling, whereas exact dimer calculations show that neither
$\chi_{\pair}$ nor $|\langle\Delta_x^\dagger\Delta_y\rangle|$ is monotone
non-increasing in repulsive $U\ge0$. Nothing here is a bound on a measured
transition temperature, and no materials claim is made.
```


## 2. Introduction (`main.tex` lines 112-117)

Replace lines 112-117 (item `(C)` of the summary list) with:

```latex
\item For the Hubbard-Holstein-SSH model at arbitrary effective on-site interaction
$\Ueff\in\R$, the high-temperature regime is closed by a frequency- and
$\Ueff$-uniform polymer expansion giving $k_B\Tpair\le1024(|t|+\Gb)$, which combines
with strong-coupling bounds into minimum ceilings for $\Ueff<0$ and half-filled
$\Ueff>0$, while exact two-site bounds refute monotonicity of pair correlations in
$U\ge0$. At $\Ueff=0$, three further routes are obstructed by exact identities: no
phonon-induced instantaneous atomic gap, a non-terminating bond Lang-Firsov
expansion, and free-fermion algebraic decay that forbids any hopping-uniform
exponential clustering (Section~\ref{sec:survives}).
```


## 3. Model Section 2.2 (`main.tex` lines 172-197)

Replace lines 172-197 (`\subsection{The pure bond-SSH model}` through `which is the case that Section~\ref{sec:survives} closes.`) with:

```latex
\subsection{The bond-SSH and Hubbard-Holstein-SSH models}

For the Hubbard-Holstein-SSH model, each bond $b=\{x,y\}\in\mathcal{E}_\Lambda$
carries a Peierls oscillator $(X_b,P_b)$ with mass $M_b>0$, spring constant $K>0$,
and frequency $\Omega_b=\sqrt{K/M_b}>0$, and each site $x\in\Lambda$ may carry an
optional Holstein mode $(a_x,a_x^\dagger)$ of frequency $\Omega_0>0$ and coupling
$g_0\in\R$ together with an on-site Hubbard parameter $U_0\in\R$:
\begin{equation}
\begin{aligned}
H_\Lambda
&=-\mu N+U_0\sum_{x\in\Lambda}
\Bigl(n_{x\uparrow}-\tfrac12\Bigr)\Bigl(n_{x\downarrow}-\tfrac12\Bigr)
-t\sum_{b\in\mathcal{E}_\Lambda}T_b
+g\sum_{b\in\mathcal{E}_\Lambda}X_bT_b \\
&\quad+\sum_{b\in\mathcal{E}_\Lambda}
\left(\frac{P_b^2}{2M_b}+\frac{K}{2}X_b^2\right)
+\sum_{x\in\Lambda}\Bigl[\Omega_0 a_x^\dagger a_x
+g_0(n_x-1)(a_x+a_x^\dagger)\Bigr],
\end{aligned}
\label{eq:Hhubssh}
\end{equation}
where $T_b=\sum_\sigma(c_{x\sigma}^\dagger c_{y\sigma}+c_{y\sigma}^\dagger
c_{x\sigma})$ and $n_x=n_{x\uparrow}+n_{x\downarrow}$. Defining the Holstein
relaxation energy $U_{\mathrm{Hol}}:=2g_0^2/\Omega_0\ge0$, the effective on-site
interaction after completing the square in the Holstein mode is
\begin{equation}
\Ueff:=U_0-\frac{2g_0^2}{\Omega_0}\in\R,
\label{eq:Ueff}
\end{equation}
so that $\Ueff>0$ is net repulsive, $\Ueff<0$ is net attractive, and $\Ueff=0$ is the
pure bond-SSH model ($U_0=g_0=0$, where \eqref{eq:Hhubssh} reduces to
\begin{equation}
H_\Lambda=-\mu N-t\sum_{b\in\mathcal{E}_\Lambda}T_b
+g\sum_{b\in\mathcal{E}_\Lambda}X_bT_b+\sum_{b\in\mathcal{E}_\Lambda}
\left(\frac{P_b^2}{2M_b}+\frac{K}{2}X_b^2\right)
\label{eq:Hssh}
\end{equation}
up to a scalar). We write
\begin{equation}
\Gb:=\frac{g^2}{K}
\label{eq:Gb}
\end{equation}
for the bond relaxation energy. Here $g$ is a bond force constant and must not be
confused with the site value $G_x$ of \eqref{eq:U}; when both models appear in one
sentence we write the Holstein site coupling out in full. In the attractive
Hubbard-bond-SSH convention of \cite{sshbond3}, the interaction parameter is written
$\Ueff^{\mathrm{att}}:=-\Ueff>0$, and the proved pair bound of \cite{sshbond3} assumes
$\beta t^2/\Ueff^{\mathrm{att}}\le2^{-27}$ together with $\beta\Gb\le2^{-13}$, with
prefactor $1965840/475579$ and decay base $48645/524224$. As $\Ueff\to0$ at $t>0$
that first hypothesis fails, and Section~\ref{sec:survives} now closes the full
high-temperature regime uniformly across all $\Ueff\in\R$, derives the combined
minimum ceilings for $\Ueff<0$ and $\Ueff>0$, and resolves the status of
$U$-monotonicity.
```


## 4. Route Table (`main.tex` lines 253-258)

Replace lines 253-258 in `tab:routes` with:

```latex
High-temperature polymer or cluster expansion at $\Ueff\in\R$ & Not an obstruction;
uniform bound and combined $\min$ ceilings hold & Theorems~\ref{thm:gc},
\ref{thm:canon}, \ref{thm:min-att} and \ref{thm:min-rep},
Section~\ref{sec:survives} \\
\hline
Monotonicity of $\chi_{\pair}$ or $|\langle\Delta_x^\dagger\Delta_y\rangle|$ in
repulsive $U_0\ge0$ & False (explicitly refuted) & Proposition~\ref{prop:nonmonotone},
Section~\ref{sec:survives} \\
\hline
Phonon-induced gap, bond Lang-Firsov, hopping-uniform clustering at $\Ueff=0$ &
Exact identities & Theorem~\ref{thm:routes}, Section~\ref{sec:survives} \\
```


## 5. Section 5 (`main.tex` lines 804-1136)

### 5.1 Section Title, Intro, `thm:gc`, `lem:canon`, and `thm:canon` (`main.tex` lines 804-1023)

Replace lines 804-1023 (`\section{What survives: ...}` through the `Remark` after `thm:canon`) with the following text. Note that `lem:canon` and `thm:routes` keep their exact proofs, while `thm:gc` and `thm:canon` extend verbatim to all $\Ueff\in\R$ (with $U_0,g_0\in\R$ and $\Omega_0,\Omega_b>0$).

```latex
\section{What survives: the \texorpdfstring{$\Ueff$}{U\_eff}-uniform ceiling, combined bounds, and \texorpdfstring{$\Ueff=0$}{U\_eff=0} obstructions}
\label{sec:survives}

The obstructions above concern the linear-in-$\Omega$ adiabatic scale and the
propagator machinery used to pursue it. At the temperature scale set by $|t|+\Gb$, a
frequency-uniform ceiling survives not only at $\Ueff=0$ but uniformly across every
$\Ueff\in\R$ (all $U_0,g_0\in\R$, $\Omega_0>0$, and $\Omega_b>0$). This extends the
high-temperature closure uniformly in $\Ueff$, combines with strong-coupling bounds
into minimum ceilings on both the attractive and repulsive sides, and rules out
$U$-monotonicity as a shortcut. All constants below are exact rationals certified by
exact-rational and outward-rounded interval replay.

\subsection{High-temperature clustering uniformly in \texorpdfstring{$\Ueff$}{U\_eff}}

Fix $L\ge4$, the bond relaxation energy $\Gb=g^2/K$, and
\begin{equation}
c_0=2^{-10},\qquad \xi_0=2^{-9}\beta^{-1},\qquad
\varepsilon=\frac{2c_0}{1-c_0}=\frac{2}{1023},\qquad
q_{\mathrm{GC}}=48\varepsilon=\frac{32}{341},
\label{eq:constants}
\end{equation}
so that $q_{\mathrm{GC}}<1/10$, together with
\begin{equation}
A_{\mathrm{GC}}=\frac{3}{1-q_{\mathrm{GC}}}=\frac{341}{103},\qquad
b_{\mathrm{GC}}=\frac{3q_{\mathrm{GC}}}{1-q_{\mathrm{GC}}}=\frac{32}{103},\qquad
R_{\max}=1+\frac{4A_{\mathrm{GC}}\,q_{\mathrm{GC}}}{(1-q_{\mathrm{GC}})^2}
=\frac{24718511}{9834543}<3 .
\label{eq:constants2}
\end{equation}
The source-augmented graph of \eqref{eq:Hhubssh} adds $|\Lambda_L|$ source edges
$e'_x=(x,x+r)$ to the physical bonds, raising the maximum vertex degree from $4$ to
$6$, with source vertex operator
$Y_{e'}(\theta)=e^{i\theta}\Delta_x^\dagger\Delta_{x+r}+e^{-i\theta}
\Delta_{x+r}^\dagger\Delta_x$ of operator norm $1$ and spectrum $\{-1,0,1\}$.

\begin{theorem}[Frequency-, $\mu$-, and $\Ueff$-uniform pair clustering]
\label{thm:gc}
For every $L\ge4$, every real $t,g,U_0,g_0,\mu$, every $K>0$, every $\Omega_b>0$,
every $\Omega_0>0$ (so every $\Ueff=U_0-2g_0^2/\Omega_0\in\R$), and every $\beta>0$
with $\beta|t|+\beta\Gb\le2^{-10}$, the equal-time on-site pair correlator of
\eqref{eq:Hhubssh} satisfies
\begin{equation}
\left|\langle\Delta_x^\dagger\Delta_y\rangle_{\Lambda_L}\right|
\le A_{\mathrm{GC}}\,q_{\mathrm{GC}}^{d(x,y)}
=\frac{341}{103}\left(\frac{32}{341}\right)^{d(x,y)}
\label{eq:gcb}
\end{equation}
for all distinct $x,y\in\Lambda_L$, and
\begin{equation}
\sup_{x\in\Lambda_L}\sum_{y\in\Lambda_L}
\left|\langle\Delta_x^\dagger\Delta_y\rangle_{\Lambda_L}\right|
\le R_{\max}=\frac{24718511}{9834543}<3 .
\label{eq:rmax}
\end{equation}
Moreover, for every fixed nonzero $r$, the density
$p_{\Lambda_L}(\xi)=|\Lambda_L|^{-1}\log Z_{\Lambda_L}(\xi)$ of the
source-augmented model extends to a zero-free analytic function of $\xi$ on
$|\xi|<\xi_0$, and for real $\xi\in[0,\xi_0/2]$ obeys
\begin{equation}
p_{\Lambda_L}(\xi)-p_{\Lambda_L}(0)\le
2\beta A_{\mathrm{GC}}\,q_{\mathrm{GC}}^{d(0,r)}\xi+\frac{4\xi^2}{\xi_0^2}.
\label{eq:source}
\end{equation}
\end{theorem}

\begin{proof}[Proof summary]
Five exact steps, each with a certified constant.
\emph{(1) Lang-Firsov diagonalisation of the site interaction, analyticity, and
polymer factorisation.} Applying the site Lang-Firsov unitary
$S_{\mathrm{LF}}=\frac{g_0}{\Omega_0}\sum_{x\in\Lambda_L}(n_x-1)(a_x^\dagger-a_x)$
(which commutes with $X_b,P_b,n_{x\sigma},N$ and vanishes when $g_0=0$) transforms
$H_{\Lambda_L}(\xi)$ into
\[
\widetilde{H}_{\Lambda_L}(\xi)
=D_0(\Ueff,\mu)+\sum_{x\in\Lambda_L}\Omega_0 a_x^\dagger a_x
+\sum_{b\in\mathcal{E}_{\Lambda_L}}\left(\frac{P_b^2}{2M_b}+\frac{K}{2}X_b^2\right)
+\widetilde{V}_t+\widetilde{V}_g+\widetilde{V}_{\mathrm{src}}(\xi)+C_0 I,
\]
where $C_0=(\frac{U_0}{4}-\frac{g_0^2}{\Omega_0})|\Lambda_L|$ cancels in every
Gibbs ratio, $D_0(\Ueff,\mu)=-\frac{\Ueff}{2}N_{\mathrm{odd}}-\mu N$ with
$N_{\mathrm{odd}}=\sum_x(n_{x\uparrow}-n_{x\downarrow})^2$ is a commuting sum of
local Hermitian terms $h_x=-\frac{\Ueff}{2}(n_{x\uparrow}-n_{x\downarrow})^2-\mu n_x$,
and the bond and source operators acquire unitary Weyl dressings
$\widetilde{T}_b=\sum_\sigma(c_{x\sigma}^\dagger c_{y\sigma}
D_x(\alpha_{\mathrm{LF}})D_y(-\alpha_{\mathrm{LF}})+\mathrm{h.c.})$ and
$\widetilde{Y}_{e'}(\theta)=e^{i\theta}\Delta_x^\dagger\Delta_y
D_x(2\alpha_{\mathrm{LF}})D_y(-2\alpha_{\mathrm{LF}})+\mathrm{h.c.}$ with
$\alpha_{\mathrm{LF}}=g_0/\Omega_0$ and $D_x(\gamma)=e^{\gamma(a_x^\dagger-a_x)}$.
For complex $\xi$ the semigroup is norm analytic and the Dyson series is trace-norm
summable: at Dyson order $K_{\mathrm{tot}}$, the bond phonon trace contributes at
most $(2\sinh(\beta\Omega_b/4(K_{\mathrm{tot}}+1)))^{-|\mathcal{E}_{\Lambda_L}|}$
and, when $g_0\ne0$, the Holstein oscillator trace at the largest time gap
$\Delta_{j^*}\ge\beta/(K_{\mathrm{tot}}+1)$ contributes
$(1-e^{-\Delta_{j^*}\Omega_0})^{-|\Lambda_L|}=O((K_{\mathrm{tot}}+1)^{|\Lambda_L|})$,
both growing only polynomially in $K_{\mathrm{tot}}$ and dominated by
$\Gamma(K_{\mathrm{tot}}/2+1)$. Every insertion operator $\widetilde{T}_b$,
$\widetilde{Y}_{e'}$ and $\widetilde{\Delta}_x^\dagger\widetilde{\Delta}_y$ is even
in fermions and acts only on the endpoints of its edge, so operators on
vertex-disjoint supports commute identically and the normalised partition function
factorises into a sum over vertex-disjoint connected polymers $E$.
\emph{(2) Activity bound without an atomic gap.} Because $D_x(\gamma)$ is unitary on
the site phonon space, $\|\widetilde{T}_b\|_{\mathrm{op}}=\|T_b\|_{\mathrm{op}}=2$
and $\|\widetilde{Y}_{e'}(\theta)\|_{\mathrm{op}}=1$. Keeping $D_0(\Ueff,\mu)$
unexpanded inside the reference semigroup $e^{-\Delta_j H_0}$, the multilinear
Schatten-H\"older inequality uses only positivity of $e^{-\Delta_j D_{0,S_E}}$ and
factorisation of the unperturbed site trace, giving
$\prod_j\|e^{-\Delta_j D_{0,S_E}}\|_{\beta/\Delta_j}
=\operatorname{Tr}(e^{-\beta D_{0,S_E}})=z_0(\beta;\Ueff,\mu)^{|S_E|}$ where
$z_0(\beta;\Ueff,\mu)=1+2e^{\beta(\mu+\Ueff/2)}+e^{2\beta\mu}>0$ cancels
identically against $Z_0=z_0^{|\Lambda_L|}Z_{\mathrm{ph},0}$. Evaluating the exact
positive Gaussian Wick contractions of the bond oscillators, each pair of which
contributes $\int_0^\beta\int_0^\beta C_\beta(|u-v|)\,du\,dv=\beta/K$, gives
\begin{equation}
|w(E)|\le\left(e^{2\beta|t|+2\beta\Gb}-1\right)^{|E_{\mathrm{phys}}|}
\left(e^{\beta|\xi|}-1\right)^{|E_{\mathrm{src}}|},\qquad
|w_{xy}(E)|\le\left(e^{2\beta|t|+2\beta\Gb}-1\right)^{|E|},
\label{eq:activity}
\end{equation}
independently of $\Ueff$, $\mu$, $\Omega_b$ and $\Omega_0$, and $e^x-1\le x/(1-x/2)$
for $x\in[0,2)$ turns the two exponents into $\varepsilon=2/1023$ using
$2\beta|t|+2\beta\Gb\le2^{-9}$ and $\beta|\xi|\le2^{-9}$.
\emph{(3) Graph counting.} A depth-first traversal rooted at any vertex shows that a
degree-$D$ graph has at most $D^{2k}$ connected edge sets of size $k$ containing a
given vertex, and connectivity gives $|S_E|\le k+1$. With $D=4$ the Koteck\'y-Preiss
sum is at most $3\sum_{k\ge1}(48\varepsilon)^k=3q_{\mathrm{GC}}/(1-q_{\mathrm{GC}})
=b_{\mathrm{GC}}<1$.
\emph{(4) Support deletion and the source derivative.} Support deletion gives
$|\widetilde Z_{\Lambda_L\setminus S}/\widetilde Z_{\Lambda_L}|\le e^{|S|}$, so the
marked polymer sum is bounded by $A_{\mathrm{GC}}q_{\mathrm{GC}}^d$. With source
edges the degree rises to $6$ and the criterion holds with
$q_{\mathrm{src}}=108\varepsilon=72/341$ and $b_{\mathrm{src}}=216/269<1$, yielding
\eqref{eq:source}.
\emph{(5) Certification.} Every rational constant in \eqref{eq:constants} and
\eqref{eq:constants2} is replayed in exact rational arithmetic and outward-rounded
interval arithmetic.
\end{proof}

\begin{remark}[Relation to pure-Hubbard hopping expansions]
\label{rem:uelschi}
In the purely electronic Hubbard limit ($g=g_0=0$), keeping arbitrary local
interactions inside the unperturbed semigroup and running a $U$-uniform hopping
expansion for $\beta|t|\le c$ is standard in mathematical statistical mechanics
\cite{uelschi1999,uelschi2004,frohlich2005}. What Theorem~\ref{thm:gc} adds is the
extension of that $U$-uniform framework to unbounded quantum bond-SSH (Peierls)
oscillators uniformly in $\Omega_b>0$ (and jointly with on-site Holstein phonons
uniformly in $\Omega_0>0$), together with the certified constants above and the
combined bounds below.
\end{remark}

\begin{lemma}[Boundary spring-constant bracket]
\label{lem:canon}
Let $b\ge2$, cut $\Lambda_L$ into rectangular blocks $B_\alpha$ of side lengths in
$[b,2b-1]$, let $\partial$ be the set of physical bonds with endpoints in different
blocks and $\partial_{\mathrm{src}}$ the set of source edges with endpoints in
different blocks, and for $K'>0$ define the block-decoupled operator
\[
H_{\mathrm{blk}}(\xi;K')=\sum_\alpha H_{B_\alpha}(\xi)
+\sum_{b\in\partial}\Bigl(\frac{P_b^2}{2M_b}+\frac{K'}{2}X_b^2\Bigr),
\]
where $H_{B_\alpha}(\xi)$ keeps only the vertices, site Hubbard and Holstein
operators, physical bonds and source edges internal to $B_\alpha$. Then for every
real $\xi$, every $U_0,g_0,\mu\in\R$, and every $\Omega_0,\Omega_b>0$, in the full
trace and in every fixed total-number and fixed spin-number sector,
\begin{equation}
\bigl|\log Z_{\Lambda_L}(\xi)-\log Z_{\mathrm{blk}}(\xi;K)\bigr|
\le C_{\mathrm{bdry}}|\partial|+\beta|\xi|\,|\partial_{\mathrm{src}}|,
\label{eq:bdry}
\end{equation}
with
$C_{\mathrm{bdry}}=\beta\bigl(2|t|+4\Gb\bigr)
+\max\bigl\{\log\frac{Z_{\mathrm{ph}}(K/2)}{Z_{\mathrm{ph}}(K)},
\log\frac{Z_{\mathrm{ph}}(K)}{Z_{\mathrm{ph}}(2K)}\bigr\}$ and
$Z_{\mathrm{ph}}(K')=(2\sinh(\beta\sqrt{K'/M_b}/2))^{-1}$.
\end{lemma}
\begin{proof}
In the untransformed frame of \eqref{eq:Hhubssh}, the Hubbard term and the site
Holstein operators are strictly on-site, contribute zero terms crossing $\partial$,
and commute with $N_\uparrow$ and $N_\downarrow$. On each crossing bond
$b=\{x,y\}\in\partial$, $\|T_b\|_{\mathrm{op}}=2$ and $[X_b,T_b]=0$, so Young's
inequality gives
\[
-\Bigl(2|t|+\frac{4g^2}{K}\Bigr)I-\frac{K}{4}X_b^2
\le(-t+gX_b)T_b\le
\Bigl(2|t|+\frac{4g^2}{K}\Bigr)I+\frac{K}{4}X_b^2
\]
on the form domain. Adding $\frac{K}{2}X_b^2$ on both sides yields
$H_{\mathrm{blk}}(\xi;K/2)-|\partial|(2|t|+4\Gb)-|\xi||\partial_{\mathrm{src}}|\le
H_{\Lambda_L}(\xi)\le H_{\mathrm{blk}}(\xi;2K)+|\partial|(2|t|+4\Gb)+|\xi||\partial_{\mathrm{src}}|$.
Min-max eigenvalue monotonicity and factorisation of the decoupled boundary
oscillator traces in every sector yield \eqref{eq:bdry}.
\end{proof}

\begin{theorem}[Thermodynamic canonical decay uniformly in $\Ueff$]
\label{thm:canon}
Under the condition $\beta|t|+\beta\Gb\le2^{-10}$, for every $\Ueff\in\R$ (all
$U_0,g_0\in\R$, $\Omega_0>0$, $\Omega_b>0$), let $L_j\to\infty$ and let
$N_j/L_j^2\to n\in(0,2)$ (or balanced spin sectors with $N_{j\sigma}/L_j^2\to a\in(0,1)$).
Then for every fixed $r\ne0$,
\begin{equation}
\limsup_{j\to\infty}\left|\langle\Delta_0^\dagger\Delta_r\rangle_{L_j,\mathrm{can}}
\right|\le A_{\mathrm{GC}}\,q_{\mathrm{GC}}^{\|r\|_1}.
\label{eq:canon}
\end{equation}
Consequently the pair-decay temperature of the Hubbard-Holstein-SSH model obeys
\begin{equation}
k_B\Tpair\le1024\left(|t|+\Gb\right)
\qquad\text{and}\qquad
k_B\Tpair^{\mathrm{can}}(n)\le1024\left(|t|+\Gb\right)
\label{eq:tpair}
\end{equation}
uniformly in $\Ueff\in\R$, in $\Omega_b,\Omega_0>0$, in $\mu\in\R$, in the interior
density $n\in(0,2)$, and in the torus side.
\end{theorem}

\begin{proof}[Proof summary]
Write $\widehat Z$ for the partition function divided by the free-phonon factor (both
bond and Holstein free oscillators). By Lemma~\ref{lem:canon}, distributing the $N$
particles among the blocks adds at most $O(b^{-2}\log b)|\Lambda_L|$, so
$\log\widehat Z_{\Lambda_L,N}(0)$ is superadditive up to $O(b^{-1})|\Lambda_L|$ and
the canonical pressure density $f_{\mathrm{can}}(n)=\lim_{L\to\infty}L^{-2}\log
\widehat Z_{\Lambda_L,N_L}(0)$ is concave in $n\in[0,2]$. Its supporting slope at
any interior $n\in(0,2)$ is $-\beta\mu$ for an admitted $\mu\in\R$, and the
finite-volume Legendre discrepancy $\delta_L=L^{-2}(\log\widehat Z_{\Lambda_L}(0;\mu)
-\log\widehat Z_{\Lambda_L,N}(0)-\beta\mu N)$ is nonnegative and tends to $0$.
Since $H_{\Lambda_L}(\xi)$ is linear in real $\xi$ and self-adjoint,
$\xi\mapsto L^{-2}\log\widehat Z_{\Lambda_L,N}(\xi)$ is convex, so its derivative at
$\xi=0$ is bounded by $(p_{\Lambda_L}(\xi)-p_{\Lambda_L}(0))/\xi+\delta_L/\xi$.
Because Theorem~\ref{thm:gc} holds uniformly in $\mu$ and $\Ueff$, taking
$\limsup_{j\to\infty}$ at fixed $\xi\in(0,\xi_0/2]$, then $\xi\downarrow0$, and
optimising over the phase $\theta$ gives \eqref{eq:canon}. Inverting
$\beta|t|+\beta\Gb\le2^{-10}$ gives \eqref{eq:tpair}.
\end{proof}

\begin{remark}
Theorem~\ref{thm:canon} is uniform in $\Ueff$, $\Omega_b$, and $\Omega_0$, though it
remains a high-temperature ceiling rather than a linear-in-$\Omega$ adiabatic
ceiling. What is removed here is the $\Ueff=0$ restriction: \eqref{eq:tpair} shows
that a $U_0$-independent bound of the form $1024(|t|+\Gb)$ requires neither small
$|U_0|$ nor Hubbard-Stratonovich positivity, because keeping $D_0(\Ueff,\mu)$
unexpanded in the reference semigroup eliminates all $\beta\Ueff$ factors.
\end{remark}
```

### 5.2 New Combined Bounds and Non-Monotonicity Refutation (insert before `\subsection{Three further routes obstructed at ...}` at line 1024)

Insert the following new subsection right before `\subsection{Three further routes obstructed at \texorpdfstring{$\Ueff=0$}{U\_eff = 0}}` (line 1025 of `main.tex`):

```latex
\subsection{Combined strong-coupling ceilings and refutation of \texorpdfstring{$U$}{U}-monotonicity}

For $\Ueff\ne0$, Theorem~\ref{thm:canon} can be combined directly with the
strong-coupling polymer expansion of \cite{sshbond3} (and its repulsive Mott/dilute
analogue), giving explicit minimum ceilings on the attractive side and in the
repulsive Mott/dilute windows, whereas no global $t^2/\Ueff$ bound can hold
$\mu$-uniformly for $\Ueff>0$ and monotonicity in $U_0\ge0$ is false.

\begin{theorem}[Combined minimum ceiling for attractive $\Ueff<0$]
\label{thm:min-att}
Assume $\Ueff<0$ in \eqref{eq:Hhubssh}, with $t,g,\mu\in\R$, $K>0$, and
$\Omega_b,\Omega_0>0$.
\begin{enumerate}[label=(\roman*),leftmargin=2.2em]
\item If $\beta t^2/|\Ueff|\le2^{-27}$ and $\beta\Gb\le2^{-13}$, then the pair
correlator satisfies $|\langle\Delta_x^\dagger\Delta_y\rangle_{\Lambda_L}|\le
\frac{1965840}{475579}(\frac{48645}{524224})^{d(x,y)}$ uniformly in
$L\ge4$, $\mu\in\R$, $\Omega_b>0$ and $\Omega_0>0$, and the same bound holds in
every canonical thermodynamic limit $N_j/L_j^2\to n\in(0,2)$.
\item Combining with Theorems~\ref{thm:gc} and~\ref{thm:canon} yields, uniformly in
$\mu\in\R$, $n\in(0,2)$, $\Omega_b>0$, and $\Omega_0>0$,
\begin{equation}
k_B\Tpair\le\min\!\left(1024(|t|+\Gb),\;
\max\!\left(2^{27}\frac{t^2}{|\Ueff|},\;2^{13}\Gb\right)\right)
\qquad(\forall\,\Ueff<0),
\label{eq:minatt}
\end{equation}
and the same minimum bound holds for $k_B\Tpair^{\mathrm{can}}(n)$. In particular, no
$|\Ueff|_-$ term is needed in any $\Tpair$ ceiling: at $t=g=0$,
$\langle\Delta_x^\dagger\Delta_y\rangle_{\Lambda_L}=0$ identically for all $x\ne y$
and all $\Ueff\in\R$, so $\Tpair=0$.
\end{enumerate}
\end{theorem}

\begin{proof}
Write $\Ueff^{\mathrm{att}}:=-\Ueff>0$. After the Lang-Firsov transformation
$S_{\mathrm{LF}}$ of Theorem~\ref{thm:gc}, $D_0(\Ueff,\mu)=\frac{\Ueff^{\mathrm{att}}}{2}
N_{\mathrm{odd}}-\mu N$ matches \cite{sshbond3} verbatim. When $g_0=0$, part (i)
is \cite{sshbond3}. When $g_0\ne0$, writing the trace in the occupation basis along
imaginary time factors out the real Holstein phonon path-integral weight
$e^{-\Phi_\beta[n]}\in(0,1]$ (\cite{stage6}), which leaves every entrywise
nonnegative majorant of \cite{sshbond3} upper bounded by its $\Phi_\beta\equiv0$
value; since the site Holstein term contributes zero bond terms across block
boundaries, the canonical boundary bracket of \cite{sshbond3} holds verbatim.
Combining the domain of part (i) with Theorem~\ref{thm:canon} yields
\eqref{eq:minatt}. At $t=g=0$, $H_\Lambda$ is diagonal in the site occupation basis,
while $\Delta_x^\dagger\Delta_y$ changes $n_x$ by $+2$ and $n_y$ by $-2$, so
$\langle\Delta_x^\dagger\Delta_y\rangle=0$ for all $x\ne y$, all $\beta>0$, and all
$\mu,\Ueff\in\R$; the scale $T^*\sim|\Ueff|$ governs only local on-site double
occupancy $\langle n_{x\uparrow}n_{x\downarrow}\rangle$, not off-diagonal spatial
pair coherence.
\end{proof}

\begin{theorem}[Repulsive windows and half-filling minimum ceiling for $\Ueff>0$]
\label{thm:min-rep}
Assume $\Ueff>0$ in \eqref{eq:Hhubssh} and define the atomic charge gap
$G(\mu):=\bigl|\frac{\Ueff}{2}-|\mu|\bigr|$.
\begin{enumerate}[label=(\roman*),leftmargin=2.2em]
\item \emph{Mott window ($|\mu|<\Ueff/2$, $G=\Ueff/2-|\mu|>0$).} If
$\beta t^2/G(\mu)\le2^{-26}$ and $\beta\Gb\le2^{-13}$, then
$|\langle\Delta_x^\dagger\Delta_y\rangle_{\Lambda_L}|\le
\frac{1965840}{475579}(\frac{48645}{524224})^{d(x,y)}$ uniformly in
$L\ge4$, $\Omega_b>0$ and $\Omega_0>0$, with analytic source disk
$|\xi|\le2^{-14}/\beta$ and source Koteck\'y-Preiss sum $6567075/6636364<1$.
\item \emph{Canonical half filling ($n=1$, even $L\ge4$).} By full particle-hole
symmetry on even tori, $\mu=0$ (where $G(0)=\Ueff/2$) supports density $n=1$ at
every $T>0$; combining part (i) with Theorem~\ref{thm:canon} gives
\begin{equation}
k_B\Tpair^{\mathrm{can}}(n=1)\le\min\!\left(1024(|t|+\Gb),\;
\max\!\left(2^{27}\frac{t^2}{\Ueff},\;2^{13}\Gb\right)\right)
\qquad(\forall\,\Ueff>0).
\label{eq:minrep}
\end{equation}
\item \emph{Dilute windows ($|\mu|>\Ueff/2$, $G=|\mu|-\Ueff/2>0$).} If
$\beta t^2/G(\mu)\le2^{-26}$ and $\beta\Gb\le2^{-13}$, then
$|\langle\Delta_x^\dagger\Delta_y\rangle_{\Lambda_L}|\le
\frac{1179504}{232925}(\frac{29187}{262112})^{d(x,y)}$. If
$\beta t^2/G(\mu)\le2^{-28}$ and $\beta\Gb\le2^{-13}$, then
$|\langle\Delta_x^\dagger\Delta_y\rangle_{\Lambda_L}|\le
\frac{2359008}{490429}(\frac{33795}{524224})^{d(x,y)}$, with analytic source disk
$|\xi|\le2^{-15}/\beta$ and source Koteck\'y-Preiss sum $2737395/3585482<1$,
transferring to any canonical density $n\in(0,2)$ whose supporting chemical
potential $\mu(n)$ obeys $\beta t^2/G(\mu(n))\le2^{-28}$.
\item \emph{Mott-edge obstruction.} At $|\mu|=\Ueff/2$ ($G(\mu)=0$), no uniform
bound of the form $k_B\Tpair\le\max(C_1 t^2/\Ueff,C_2\Gb)$ can hold across $\mu\in\R$
at $\Ueff>0$, so the $1024(|t|+\Gb)$ term of Theorems~\ref{thm:gc}--\ref{thm:canon}
cannot be dropped $\mu$-uniformly.
\end{enumerate}
\end{theorem}

\begin{proof}
For $\Ueff>0$, on each site $x$ the atomic eigenvalues of
$h_x=-\frac{\Ueff}{2}(n_{x\uparrow}-n_{x\downarrow})^2-\mu n_x$ satisfy
$E(0)-E(1)=\Ueff/2+\mu\ge G$ and $E(2)-E(1)=\Ueff/2-\mu\ge G$ in the Mott window
$|\mu|<\Ueff/2$, whereas in the dilute windows $|\mu|>\Ueff/2$ the ground state is
$n_x=0$ ($\mu<-\Ueff/2$) or $n_x=2$ ($\mu>\Ueff/2$) with excitation gap at least
$G$ to $n_x=1$ and at least $2G$ to the opposite doubly/empty state. Setting
$v=e^{-\beta G/2}\in(0,1)$ and counting the weight after subtracting $\frac{G}{2}$
on excited states gives the single-site factor $z_b/z_a\le(1+v)/(1+v^2)<5/4$ in the
Mott window and $z_b/z_a\le(1+2v+v^3)/(1+v^2)^2<3/2$ in the dilute windows (exact
polynomial inequalities verified in rational arithmetic). Following the SOS-plus-Wick
polymer expansion of \cite{sshbond3} with $e^{-\Phi_\beta[n]}\le1$ and the
signless hopping operator $B_b$ (which satisfies $L_t|t|B_{E_t}\le\frac{G}{2}
\sum_{x\in S_E}\mathbf{1}_{\mathrm{exc},x}+16|E_t|L_t^2 t^2/G$), setting
$L_t=2^{10},L_s=2^{11}$ for $c=5/4$ ($\beta t^2/G\le2^{-26}$) reproduces every
constant of \cite{sshbond3}, and setting $L_t=2^{10}$ (GC) or
$L_t=2^{11},L_s=2^{12}$ (canonical) for $c=3/2$ yields the stated constants in
(i) and (iii). On even tori, the full particle-hole unitary
$U_{\mathrm{ph}}:c_{x\sigma}^\dagger\mapsto(-1)^{x_1+x_2}c_{x\sigma}$,
$a_x\mapsto-a_x$, $X_b\mapsto X_b$ satisfies $U_{\mathrm{ph}}T_b
U_{\mathrm{ph}}^\dagger=T_b$ (since $c_{x\sigma}c_{y\sigma}^\dagger
=-c_{y\sigma}^\dagger c_{x\sigma}$ on distinct sites) and maps $n_x-1\mapsto-(n_x-1)$,
leaving $D_0(\Ueff,0)$ and the Holstein term invariant and mapping
$N\mapsto2|\Lambda_L|-N$. Thus $f_{\mathrm{can}}(n)=f_{\mathrm{can}}(2-n)$ is
symmetric and concave on $[0,2]$, so $\mu=0$ supports $n=1$ at every $T>0$, giving
\eqref{eq:minrep}. For (iv), at $g=g_0=0$ and $|\mu|=\Ueff/2$, two atomic levels
($n_x=1$ and $n_x=0$ or $n_x=2$) are exactly degenerate, so the single-bond polymer
activity in the $\Omega_0\to\infty$ atomic-gap expansion satisfies
$w_\infty(\{e\})\ge(\cosh(\beta t)-1)/4$ independently of $\Ueff>0$, exceeding $2$
at $\beta t=3$ for every $\Ueff>0$ even when $\beta t^2/\Ueff\to0$.
\end{proof}

\begin{proposition}[Refutation of monotonicity in repulsive $U_0\ge0$]
\label{prop:nonmonotone}
Neither the integrated pair susceptibility $\chi_{\pair}=\sum_{y}\langle\Delta_0^\dagger
\Delta_y\rangle$ nor the off-diagonal pair correlator $|\langle\Delta_x^\dagger\Delta_y
\rangle|$ ($x\ne y$) is monotone non-increasing in $U_0\ge0$ at fixed
$(t,g,\beta,\mu)$ or at fixed canonical particle number $N$. Specifically, on the
two-site Hubbard dimer ($t=1$, $g=g_0=0$):
\begin{enumerate}[label=(\roman*),leftmargin=2.2em]
\item In the centered convention $H_U=U_0\sum_{x=0}^1(n_{x\uparrow}-\tfrac12)
(n_{x\downarrow}-\tfrac12)$ at $\beta=2$, $\mu=-3$:
\[
\langle\Delta_0^\dagger\Delta_0\rangle|_{U_0=0}\in[8.391,8.393]\times10^{-5},\quad
\langle\Delta_0^\dagger\Delta_1\rangle|_{U_0=0}\in[7.788,7.790]\times10^{-5},\quad
\chi_{\pair}(0)\in[1.6180,1.6182]\times10^{-4},
\]
whereas at $U_0=4$:
\[
\langle\Delta_0^\dagger\Delta_0\rangle|_{U_0=4}\in[2.2088,2.2090]\times10^{-3},\quad
\langle\Delta_0^\dagger\Delta_1\rangle|_{U_0=4}\in[2.2049,2.2051]\times10^{-3},\quad
\chi_{\pair}(4)\in[4.4138,4.4140]\times10^{-3},
\]
so both $\chi_{\pair}$ and $|\langle\Delta_0^\dagger\Delta_1\rangle|$ increase by a
factor exceeding $25$ from $U_0=0$ to $U_0=4$ (and numerically to
$\chi_{\pair}(8)\approx0.017797$, over $109.9$ times $\chi_{\pair}(0)$).
\item In the uncentered convention $H_U=U_0\sum_{x=0}^1 n_{x\uparrow}n_{x\downarrow}$
at $\beta=1/2$, $\mu=5$:
\[
\langle\Delta_0^\dagger\Delta_1\rangle|_{U_0=0}\in[1.2879,1.2881]\times10^{-3},
\qquad
\langle\Delta_0^\dagger\Delta_1\rangle|_{U_0=4}\in[5.3243,5.3245]\times10^{-3},
\]
an increase by a factor exceeding $4.1$.
\item Numerically in the canonical ensemble on the four-site ring $C_4$ at $N=4$,
$t=1$, $g=g_0=0$, $\beta=5$ (independent of $\mu$ and scalar convention),
$|\langle\Delta_0^\dagger\Delta_2\rangle_{N=4}|$ increases from $0.020827$ at
$U_0=0$ to $0.040148$ at $U_0=1$.
\end{enumerate}
\end{proposition}

\begin{proof}
In the two-site dimer Fock space ($\dim=16$), $H$ is block diagonal in
$(N_\uparrow,N_\downarrow)$ with integer-valued matrix blocks of size at most $4$ at
$U_0\in\{0,4\}$, so the exact eigenvalues are $\{-\mu N_0+E\}$ with rational sums
and simple radicals $\sqrt{16+U_0^2}$ and $\sqrt{4+U_0^2/4}$: in the $(1,1)$ sector
with basis $\{|1\uparrow,1\downarrow\rangle,|2,0\rangle,|0,2\rangle,
|1\downarrow,1\uparrow\rangle\}$, the centered Hamiltonian at $t=1,\mu=0$ has
eigenvalues $\{-U_0/2,\,U_0/2,\,\pm\sqrt{4+(U_0/2)^2}\}$, while $\Delta_0^\dagger
\Delta_1$ couples $|2,0\rangle\leftrightarrow|0,2\rangle$. Outward-rounded rational
interval evaluation of the finite matrix traces certifies all enclosures in (i) and
(ii). Physically, in (i) increasing $U_0$ lowers the singly occupied energy
$E(1)=-U_0/2-\mu$ relative to $E(0)=0$ and populates the $N=2$ pair-coherent
multiplet; in (ii) at $\mu=5$, increasing $U_0$ lifts Pauli blocking of $n=2$
doublons toward empty-doublon resonances.
\end{proof}
```

### 5.3 Theorem 5.4 (`thm:routes`, `main.tex` lines 1025-1136)

Keep `\subsection{Three further routes obstructed at \texorpdfstring{$\Ueff=0$}{U\_eff = 0}}` and `thm:routes` (Theorem 5.4, including items (i), (ii), and (iii), its proof, and its remark) unchanged at $\Ueff=0$. Notice that `thm:routes`(i) and (iii) genuinely require $\Ueff=0$ (for $\Ueff<0$ an atomic gap $|\Ueff|/2$ exists, and for $\Ueff>0$ at $\mu=0$ the free-fermion factorization $\langle\Delta_0^\dagger\Delta_r\rangle=G(r)^2$ fails).


## 6. Section 6 (`main.tex` lines 1143-1169)

Replace items `(a)` and `(d)` of `\section{What is not claimed}` (`lines 1148-1155` and `1161-1169`) with:

```latex
\item No upper bound on $\Tpair$ for the attractive Holstein model or for the
Hubbard-Holstein-SSH model at temperatures below $\min(1024(|t|+\Gb),
\max(2^{27}t^2/|\Ueff|,2^{13}\Gb))$ (or inside the doped repulsive regime below
$1024(|t|+\Gb)$) is proved here, and no ceiling at the linear scale
$\Tlin=C(t,U)\Omega$ is proved or disproved. Theorems~\ref{thm:gc}--\ref{thm:min-rep}
extend the $\Ueff=0$ high-temperature bound uniformly to all $\Ueff\in\R$ and supply
explicit minimum ceilings for $\Ueff<0$ and half-filled $\Ueff>0$, whereas the
obstructions of Sections~\ref{sec:cumulant} and~\ref{sec:det} and
Theorem~\ref{thm:routes} remain statements about specified classes of arguments, as
spelled out in Remarks~\ref{rem:class}, \ref{rem:notclass} and~\ref{rem:smooth}.
```

and for item `(d)`:

```latex
\item Theorems~\ref{thm:gc} and~\ref{thm:canon} hold for all $\Ueff\in\R$ on square
tori of side at least four, but only for $\beta|t|+\beta\Gb\le2^{-10}$;
Theorems~\ref{thm:min-att} and~\ref{thm:min-rep} close the additional strong-coupling
regime for $\Ueff<0$ and in the repulsive Mott and dilute windows ($n=1$ and the
stated $\mu$-windows), leaving intermediate-temperature doped repulsive systems and
low-temperature two-dimensional algebraic regimes untouched. Theorem~\ref{thm:routes}(i)
and~(iii) apply strictly to the pure bond-SSH model at $\Ueff=0$ (where
\eqref{eq:tpair} removes the $t^2/|\Ueff|$ divergence of \cite{sshbond3} and lowers
its $t=0$ threshold $2^{13}\Gb$ to $2^{10}\Gb$).
```


## 7. Section 7 Open Problems (`main.tex` lines 1205-1211)

Replace item `(4)` of `\section{Open problems}` (`lines 1205-1211`) with:

```latex
\item \emph{Intermediate and low-temperature regimes beyond the high-temperature and
strong-coupling ceilings.} Theorems~\ref{thm:gc} and~\ref{thm:canon} stop at
$\beta|t|+\beta\Gb=2^{-10}$. At $\Ueff=0$, Theorem~\ref{thm:routes}(iii) and the
exact identities of Theorem~\ref{thm:routes}(i) show that any remaining estimate
must be joint in $\beta t$ and $\beta\Gb$ and must recover algebraic tails at large
hopping. For repulsive $\Ueff>0$, spatial pair decay inside the Mott window below
$\max(2^{27}t^2/\Ueff,2^{13}\Gb)$ at $n=1$ and at doped densities $n\ne1$ below
$1024(|t|+\Gb)$ remains open.
```


## 8. Additions to `refs.bib`

Append the following verified BibTeX entries to `W/MASSIVE/BARRIERS2-PAPER/refs.bib`:

```bibtex
@article{uelschi1999,
  author = {Ueltschi, Daniel},
  title = {Analyticity in {Hubbard} models},
  journal = {Journal of Statistical Physics},
  volume = {95},
  number = {3--4},
  pages = {693--717},
  year = {1999},
  doi = {10.1023/A:1004599410952},
  eprint = {cond-mat/9810320},
  archivePrefix = {arXiv}
}

@article{uelschi2004,
  author = {Ueltschi, Daniel},
  title = {Cluster expansions and correlation functions},
  journal = {Moscow Mathematical Journal},
  volume = {4},
  number = {2},
  pages = {511--522},
  year = {2004},
  doi = {10.17323/1609-4514-2004-4-2-511-522},
  eprint = {math-ph/0304003},
  archivePrefix = {arXiv}
}

@article{frohlich2005,
  author = {Fr{\"o}hlich, J{\"u}rg and Ueltschi, Daniel},
  title = {Hund's Rule and Metallic Ferromagnetism},
  journal = {Journal of Statistical Physics},
  volume = {118},
  number = {5--6},
  pages = {973--978},
  year = {2005},
  doi = {10.1007/s10955-004-2174-y}
}
```
