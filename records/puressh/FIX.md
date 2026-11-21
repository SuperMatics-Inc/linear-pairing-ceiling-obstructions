# PURESSH Review Resolution (`FIX.md`)

Resolves all findings `F1`–`F6` from `ADIABATIC/PURESSH/REVIEW.md` (`EshReview`), while preserving `REVIEW.md` untouched and archiving the original `RESULT.md` as `RESULT.v1.md`.

---

## 1. Item-by-Item Resolution

### F1 (P0): Canonical prefactor in `RESULT.md` Theorem 1.2
- **Issue:** `RESULT.v1.md` (lines 40–42, 60, 75) stated a canonical prefactor $A_{\rm c} := 2e\,\beta\xi_0\,b_{\rm src} = \frac{27e}{17216}$ and claimed `replay.py` certified it, whereas `RIGOR.md` Theorem 1.2 (lines 90–103, 476–484) proves the thermodynamic canonical bound via the single-bond derivative $\partial_\xi p_{\Lambda_L}(0)$ with the grand-canonical prefactor $A_{\rm GC} = \frac{341}{103}$.
- **Fix:** Updated `RESULT.md` (lines 40–42, 60, 75) to state the proved canonical prefactor $A_{\rm GC} = \frac{341}{103} \approx 3.31067961$ with decay base $q_{\rm GC} = \frac{32}{341}$ (matching `RIGOR.md` Theorem 1.2 verbatim) and removed $A_{\rm c} = \frac{27e}{17216}$ and the claim that `replay.py` certified it.

### F2 (P1): Proposition 7.3 staircase ray and $d=3$ comparison in `RESULT.md`
- **Issue:** `RESULT.v1.md` (lines 13, 77, 139) cited diagonal separation $y - x = (2m-1, 2m-1)$ with $\frac{4}{\pi^4(2m-1)^4}$ ($O(\|x-y\|_1^{-4})$) and $\frac{4}{81\pi^4}$ at $d=3$, whereas `RIGOR.md` Proposition 7.3 (lines 515–555) and `replay.py` (lines 518–524, now 571–577) prove the obstruction along the staircase ray $r_m = (m, m-1)$ at graph distance $d = \|r_m\|_1 = 2m - 1$, where the exact $T = 0$ free-fermion correlator is $\frac{4}{\pi^4(2m-1)^2} = \frac{4}{\pi^4 d^2}$ ($O(\|x-y\|_1^{-2})$) and exceeds $A_{\rm GC} q_{\rm GC}^d$ already at $m = 2$ ($d = 3$): $\frac{4}{9\pi^4} \approx 4.5627 \times 10^{-3} > A_{\rm GC} q_{\rm GC}^3 \approx 2.7359 \times 10^{-3}$.
- **Fix:** Updated `RESULT.md` (lines 13, 77, 139) to match `RIGOR.md` Proposition 7.3 and `replay.py` (`r_m = (m, m-1)`, $d = 2m - 1$, exact correlator $\frac{4}{\pi^4(2m-1)^2}$, and $\frac{4}{9\pi^4} > A_{\rm GC} q_{\rm GC}^3$ at $m=2, d=3$).

### F3 (P1): Theorem 1.1(3) source definition and pressure bound in `RESULT.md`
- **Issue:** `RESULT.v1.md` (line 32) wrote $Y_{e'}(\theta) = \frac{1}{2}(e^{i\theta}\Delta_x^\dagger \Delta_y + e^{-i\theta}\Delta_y^\dagger \Delta_x)$, omitted the translation sum over $\mathcal{E}_{\rm src}$, and wrote $|p_{\Lambda_L}(\xi) - p_{\Lambda_L}(0)| \le b_{\rm src}$, whereas `RIGOR.md` (lines 41–42, 85–88, 396–401) defines $Y_{e'}(\theta) := e^{i\theta}\Delta_x^\dagger \Delta_{x+r} + e^{-i\theta}\Delta_{x+r}^\dagger \Delta_x$ (no $\frac{1}{2}$, with $\|Y_{e'}(\theta)\|_{\rm op} = 1$), $V_{\rm src}(\xi) = -\xi \sum_{e' \in \mathcal{E}_{\rm src}} Y_{e'}(\theta)$, and proves $|p_{\Lambda_L}(\xi) - p_{\Lambda_L}(0)| \le -2\log(1 - b_{\rm src}/e) = -2\log(1 - \frac{216}{269e}) < 0.7012 < 2$.
- **Fix:** Updated `RESULT.md` (lines 32, 54, 75) to match `RIGOR.md` Theorem 1.1(3) exactly.

### F4 (P2): Complete sector decomposition of $C_4$ at $N = 4$ in Proposition 7.1
- **Issue:** Proposition 7.1 previously checked only the two 6-dimensional subspaces $\{N_\uparrow=2, N_\downarrow=2, N_{\rm odd}=0\}$ and $\{N_\uparrow=2, N_\downarrow=2, N_{\rm odd}=4\}$ of $C_4$, leaving open whether the remaining odd-parity sectors $\{N_\uparrow=2, N_\downarrow=2, N_{\rm odd}=2\}$ ($\dim 24$) or $S^z \ne 0$ at $N = 4$ ($\dim 34$) could have a larger eigenvalue of $\Sigma_4 = \sum_{b \in \mathcal{E}_{C_4}} T_b^2$.
- **Fix:** Added the complete 9-sector (6 spin-flip-conjugate classes) exact decomposition of the 70-dimensional half-filled space $N = 4$ on $C_4$ to `RIGOR.md` (Theorem 1.3(1) and Proposition 7.1, item 4), `ROUTE-SCREEN.md` (line 72), `RESULT.md` (lines 11, 77), and certified every sector's exact integer minimal polynomial and maximum eigenvalue in `replay.py` (lines 444–536):
  - $\{N_\uparrow=2, N_\downarrow=2, N_{\rm odd}=0\}$ ($\dim 6$): minimal polynomial $\lambda(\lambda-4)(\lambda-8)(\lambda-12) = 0$, $\lambda_{\max} = 12$;
  - $\{N_\uparrow=2, N_\downarrow=2, N_{\rm odd}=4\}$ ($\dim 6$): minimal polynomial $\lambda(\lambda-4)(\lambda-8)(\lambda-12) = 0$, $\lambda_{\max} = 12$;
  - $\{N_\uparrow=2, N_\downarrow=2, N_{\rm odd}=2\}$ ($\dim 24$): minimal polynomial $(\lambda-2)(\lambda-4)(\lambda-6)(\lambda-10) = 0$, $\lambda_{\max} = 10$;
  - $\{(N_\uparrow, N_\downarrow) \in \{(3,1),(1,3)\}, N_{\rm odd}=4\}$ ($\dim 4+4=8$): minimal polynomial $\lambda(\lambda-4)(\lambda-8) = 0$, $\lambda_{\max} = 8$;
  - $\{(N_\uparrow, N_\downarrow) \in \{(3,1),(1,3)\}, N_{\rm odd}=2\}$ ($\dim 12+12=24$): minimal polynomial $(\lambda-2)(\lambda-4)(\lambda-6) = 0$, $\lambda_{\max} = 6$;
  - $\{(N_\uparrow, N_\downarrow) \in \{(4,0),(0,4)\}, N_{\rm odd}=4\}$ ($\dim 1+1=2$): minimal polynomial $\lambda = 0$, $\lambda_{\max} = 0$.
  Hence $\max\operatorname{spec}(\Sigma_4|_{N=4, N_{\rm odd}>0}) = \max(12, 10, 8, 6, 0) = 12 = \max\operatorname{spec}(\Sigma_4|_{N=4, N_{\rm odd}=0})$, proving $\Delta_{\rm eff}(C_4) = 0$ across both the spin-balanced $N_\uparrow = N_\downarrow = 2$ space ($\dim 36$) and the full $N = 4$ space ($\dim 70$).

### F5 (P2): Reframing of the 2D open problem at $\beta|t| \gg 1$
- **Issue:** In 2D at $T > 0$, Hohenberg-Mermin-Wagner precludes true off-diagonal long-range order ($\lim_{\|x-y\|_1 \to \infty} |\langle \Delta_x^\dagger \Delta_y\rangle| > 0$); the physical 2D pairing transition is Berezinskii-Kosterlitz-Thouless (BKT) algebraic quasi-long-range order ($\eta(T) \le 1/4 < 2$) with a divergent $\ell^1$ pair susceptibility $\chi_{\rm pair}(\Lambda_L) = \sum_{y \in \Lambda_L} |\langle \Delta_x^\dagger \Delta_y\rangle_{\Lambda_L}| \to \infty$ as $L \to \infty$, whereas true ODLRO is the $d \ge 3$ question.
- **Fix:** Reframed the open problem in `RIGOR.md` (§8 item 2), `ROUTE-SCREEN.md` (§2.4), and `RESULT.md` (Explicit List of What Is Not Covered, item 2) in terms of 2D BKT quasi-LRO / divergent $\chi_{\rm pair}$ (contrasted with the free-fermion $\eta = 2$, $\chi_{\rm pair} \le 1/2$ behavior in Proposition 7.3) and $d \ge 3$ true ODLRO.

### F6 (P3): Minor typos and Cauchy-Schwarz / AM-GM step in `RIGOR.md`
- **Fix:**
  - `RIGOR.md:69`: fixed last digit of decimal approximation of $R_{\rm max} = \frac{24718511}{9834543} \approx 2.5134376859$.
  - `RIGOR.md` Lemma 2.1 (lines 134–140): expanded the Cauchy-Schwarz + AM-GM step explicitly (`\sum_b |X_b|\,\|T_b\psi\|\,\|\psi\| \le (\sum_b X_b^2)^{1/2} (4\sum_b \|\psi\|^2)^{1/2} \le \frac{\varepsilon}{2} \sum_b X_b^2 + \frac{2}{\varepsilon} |\mathcal{E}_{\Lambda_L}| \|\psi\|^2`).
  - `RIGOR.md` Proof of Theorem 1.2 (line 451): fixed the sign typo $H_{\Lambda_L}(\xi) - \mu N \to H_{\Lambda_L}(\xi) + \mu N$ in the definition of $Z_{\Lambda_L, N}(\xi)$ (since $H_{\Lambda_L}(\xi)$ already includes $-\mu N$).
  - `RIGOR.md` §8 (line 581): fixed the decimal approximations in the $m = 2$ ($d = 3$) staircase witness from $4.5647 \times 10^{-3} > 2.7361 \times 10^{-3}$ to $4.5627 \times 10^{-3} > 2.7359 \times 10^{-3}$ for $\frac{4}{9\pi^4} > A_{\rm GC} q_{\rm GC}^3$.

---

## 2. Verification Commands and Exit Codes

1. `UV_OFFLINE=1 UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with mpmath python -B D:/dev/scratch/ceiling-20261118/ADIABATIC/PURESSH/replay.py` $\to$ **exit code `0`** (`PURESSH replay.py: ALL EXACT RATIONAL AND OUTWARD INTERVAL CHECKS PASSED`, including `mpmath.iv (50 dps) cross-check PASSED`)
2. `UV_OFFLINE=1 UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with mpmath python -B D:/dev/scratch/ceiling-20261118/ADIABATIC/PURESSH/replay.py --all-mutants` $\to$ **exit code `0`** (`ALL 12 MATHEMATICAL MUTANTS REJECTED (each exited 1)`)
3. `UV_OFFLINE=1 UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with numpy --with scipy python -B D:/dev/scratch/ceiling-20261118/ADIABATIC/PURESSH/ed_check.py` $\to$ **exit code `0`** (`PURESSH ed_check.py: ALL NUMERICAL ED CHECKS PASSED`)

---

## 3. SHA-256 Digests

- `RESULT.md`: `2de44d481c9d7cf32d183f80a51f3c354d2996f0dee093c7280546bf6949e257`
- `RESULT.v1.md` (backup): `058f4ae619a0c79cdcce2b3d95e5b59f15690ad0a1b9ab484f36dbce295a9701`
- `ROUTE-SCREEN.md`: `49cd8efb87e8c977bb30420cf3404980bd34b38c57ecedd17aa4cf3de19695d3`
- `RIGOR.md`: `5e3989ca98eb847f01def3d7c5ade8d9192f28d0c3f96592cf042963b7715fc8`
- `replay.py`: `b7b447fc32ea08bd44395cf24d0c0bb986b46f7ea3549ab4e29e83ef67ae2a99`
- `ed_check.py`: `1b1f944f36227915550e89f50416f0f7ca314bc68dc1502b4626511474cfb700`
- `REVIEW.md` (untouched): `a4c06aa9bc5c179e1accc045f4a02c27c1b393842cfa43b2b8751779a76f7832`

---

## 4. Round 2 Resolution (`REVIEW2.md` Findings `N1`–`N4`)

Prior to Round 2 edits, `RESULT.md` was backed up as `RESULT.v2.md` and `RIGOR.md` was backed up as `RIGOR.v2.md` (`REVIEW.md`, `REVIEW2.md`, and `RESULT.v1.md` remain untouched).

### Edits by File and Line (`N1`–`N4`)
1. **`N1` (P2 — `RESULT.md:54`, Source edge activity row in Comparison Table):**
   - `RESULT.md:54`: Restored the `PURESSH` cell to `$e^{\beta|\xi|} - 1 \le \frac{2}{1023}$ at $\beta|\xi| \le 2^{-9}$ (giving $b_{\rm src} = \frac{216}{269} < 1$ on $\{|\xi| < \xi_0 = 2^{-9}\beta^{-1}\}$)`, matching $\|Y_{e'}(\theta)\|_{\rm op} = 1$, `RIGOR.md:62, 315, 326`, and `replay.py:345`.
2. **`N2` (P2 — `RESULT.md:60`, `SSHBOUND3` canonical prefactor cell in Comparison Table):**
   - `RESULT.md:60`: Updated the `SSHBOUND3` cell to cite `$A_{\rm GC} = \frac{1965840}{475579} \approx 4.13357192$ (via single-bond derivative $\partial_\xi p_{\Lambda_M}(0)$)` from `SSHBOUND3/RIGOR.md:76-86` (Theorem 1.2).
3. **`N3` (P3 — Sector count wording: 9 individual $(N_\uparrow, N_\downarrow, N_{\rm odd})$ invariant sectors / 6 spin-flip-conjugate classes, never "7"):**
   - `RESULT.md:77`: Changed "across all 7 invariant sectors of $N=4$" to "across all 9 $(N_\uparrow, N_\downarrow, N_{\rm odd})$ invariant sectors (6 spin-flip-conjugate classes) of $N=4$".
   - `RIGOR.md:579`: Changed "across all 7 invariant sectors ($70$ states total) of $C_4$ at $N = 4$" to "across all 9 $(N_\uparrow, N_\downarrow, N_{\rm odd})$ invariant sectors (6 spin-flip-conjugate classes, $70$ states total) of $C_4$ at $N = 4$".
   - `ROUTE-SCREEN.md:72`: Changed "across all 7 invariant sectors" to "across all 9 $(N_\uparrow, N_\downarrow, N_{\rm odd})$ invariant sectors (6 spin-flip-conjugate classes; certified in `RIGOR.md` Proposition 7.1 and `replay.py`)".
   - `FIX.md:23`: Changed "7-sector" to "9-sector (6 spin-flip-conjugate classes)".
   - `RESULT.md:148-149`: Updated the recorded SHA-256 digests of `ROUTE-SCREEN.md` and `RIGOR.md`.
4. **`N4` (P3 — `FIX.md:40-41` description of `F6` edits):**
   - `FIX.md:40-41`: Corrected the prose summary of the two `F6` edits in `RIGOR.md` (`H_{\Lambda_L}(\xi) - \mu N \to H_{\Lambda_L}(\xi) + \mu N` at `RIGOR.md:451` in the Proof of Theorem 1.2, and `4.5647 \times 10^{-3} > 2.7361 \times 10^{-3} \to 4.5627 \times 10^{-3} > 2.7359 \times 10^{-3}` at `RIGOR.md:581`).

### Round 2 Verification Commands and Exit Codes
1. `UV_OFFLINE=1 UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with mpmath python -B D:/dev/scratch/ceiling-20261118/ADIABATIC/PURESSH/replay.py` $\to$ **exit code `0`** (`PURESSH replay.py: ALL EXACT RATIONAL AND OUTWARD INTERVAL CHECKS PASSED`, including `mpmath.iv (50 dps) cross-check PASSED`)
2. `UV_OFFLINE=1 UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with mpmath python -B D:/dev/scratch/ceiling-20261118/ADIABATIC/PURESSH/replay.py --all-mutants` $\to$ **exit code `0`** (`ALL 12 MATHEMATICAL MUTANTS REJECTED (each exited 1)`)
3. `UV_OFFLINE=1 UV_CACHE_DIR=D:/dev/.cache/uv uv run --no-project --with numpy --with scipy python -B D:/dev/scratch/ceiling-20261118/ADIABATIC/PURESSH/ed_check.py` $\to$ **exit code `0`** (`PURESSH ed_check.py: ALL NUMERICAL ED CHECKS PASSED`)

### Round 2 SHA-256 Digests
- `RESULT.md`: `74b8b19b1c6a0c8a714daf7338237759f7304be3a6a929485d2ac2cf5f1e686a`
- `RESULT.v2.md` (Round 1 backup): `2de44d481c9d7cf32d183f80a51f3c354d2996f0dee093c7280546bf6949e257`
- `RESULT.v1.md` (v1 backup): `058f4ae619a0c79cdcce2b3d95e5b59f15690ad0a1b9ab484f36dbce295a9701`
- `RIGOR.md`: `d04efa00eaa844e1cc1bdde4f8abe275f69daecfb2212b26ac2a25c6540adaa1`
- `RIGOR.v2.md` (Round 1 backup): `5e3989ca98eb847f01def3d7c5ade8d9192f28d0c3f96592cf042963b7715fc8`
- `ROUTE-SCREEN.md`: `2b8e6d1c3518ab332f407013953704708b1bd5686fba5de2a020b3a062267b55`
- `replay.py`: `b7b447fc32ea08bd44395cf24d0c0bb986b46f7ea3549ab4e29e83ef67ae2a99`
- `ed_check.py`: `1b1f944f36227915550e89f50416f0f7ca314bc68dc1502b4626511474cfb700`
- `REVIEW.md` (untouched): `a4c06aa9bc5c179e1accc045f4a02c27c1b393842cfa43b2b8751779a76f7832`
- `REVIEW2.md` (untouched): `25f1115df5b8ce4eb4a246b5a30439ec354d09968cbc8423dd6214fa56926bfe`
