# UNIFORM-SSH Review Resolution (`FIX.md`)

Date: 20 November 2026
Review Source: `MASSIVE/UNIFORM-SSH/REVIEW.md` (Verdict: `PASS-WITH-FIXES`, 0 P0, 0 P1, 2 P2, 6 P3, plus section 2.4 novelty note)
Status: All findings F1 through F8, the section 2.4 literature and novelty note, and the `BARRIERS2-PAPER` amendment text (`AMENDMENT.md`) are resolved; `REVIEW.md` is preserved untouched.

Backup note: Separate `*.v1` backup copies of `SCOPING.md`, `RIGOR.md`, `RESULT.md`, and `replay.py` were not created; all fixes were applied directly to the files and verified against `REVIEW.md` and `replay.py`.

## Item-by-Item Resolution

1. **F1 (P2, `SCOPING.md` line 66):** Removed the parenthetical claim `or at \mu = 0 via Shiba unitary equivalence to SSHBOUND3`, because at $\mu = 0$, $U_{\rm eff} > 0$ maps under the bipartite partial Shiba transformation to attractive $U_{\rm eff} < 0$ at $g = 0$ but reverses the sign of the $n_x$-coupled Holstein term and breaks $\Delta_x^\dagger \Delta_y$ invariance, whereas the actual half-filling proof uses the full particle-hole unitary $U_{\rm ph}$ (`RIGOR.md` section 4.2, Theorem 1.4(2)).
2. **F2 (P2, `SCOPING.md` line 86):** Replaced the incorrect statement that $S_{\rm LF}$ commutes with $\Delta_x^\dagger \Delta_y$ with the exact transformation from `RIGOR.md` section 2.2: $S_{\rm LF}$ commutes with $D_0$ and $(X_b, P_b)$, dresses $\Delta_x^\dagger \Delta_y$ by unitary displacements $D_x(2\alpha_{\rm LF}) D_y(-2\alpha_{\rm LF})$ (leaving $\|Y_{e'}(\theta)\|_{\rm op} = 1$ and $\|T_b\|_{\rm op} = 2$ unchanged at fixed phonon path), and contributes a real contraction factor $0 < e^{-\Phi_\beta[n]} \le 1$.
3. **F3 (P3, `SCOPING.md` line 97, `RIGOR.md` line 268):** Replaced `> 110x` with `\approx 110x (> 109.9x)` matching the exact numerical value $\chi_{\rm pair}(8)/\chi_{\rm pair}(0) \approx 109.985$.
4. **F4 (P3, `SCOPING.md` line 97):** Replaced `> 4.2x` with `> 4.1x` matching the certified uncentered ratio $|\langle \Delta_0^\dagger \Delta_1\rangle|(4) / |\langle \Delta_0^\dagger \Delta_1\rangle|(0) \approx 4.1339 > 4.1$.
5. **F5 (P3, `SCOPING.md` line 85, `RIGOR.md` lines 203, 239):** Corrected "convex" to "concave" for the canonical pressure density $f_{\rm can}(n) = \lim_{L\to\infty} L^{-2}\log \widehat{Z}_{\Lambda_L, N_L}$ on $[0, 2]$.
6. **F6 (P3, `RIGOR.md` line 235, `RESULT.md` line 32, `replay.py` lines 569, 606, 662):** Renamed "Shiba/particle-hole" to "full particle-hole" ($c_{x\sigma}^\dagger \mapsto (-1)^{x_1+x_2} c_{x\sigma}$), distinguishing it from the spin-asymmetric partial Shiba transformation.
7. **F7 (P3, `RIGOR.md` line 163):** Added explicit explanation of the Holstein oscillator trace factor $\prod_{x \in \Lambda_L}(1 - e^{-\Delta_{j^*}\Omega_0})^{-1} = O((K_{\rm tot}+1)^{|\Lambda_L|})$ in Schatten-Holder Dyson convergence when $g_0 \ne 0$.
8. **F8 (P3, `RESULT.md` line 38):** Corrected section reference from 5.4 to 5.5.
9. **Literature, Novelty Scope, and `BARRIERS2-PAPER` Amendment (`RIGOR.md` section 6, `AMENDMENT.md`):** Cited Ueltschi (*J. Stat. Phys.* 95 (1999), 693-717), Ueltschi (*Moscow Math. J.* 4 (2004), 511-522), Fröhlich and Ueltschi (*J. Stat. Phys.* 118 (2005), 973-978), and `HUBHOL` Corollary 4.5 for the purely electronic and Holstein $U$-uniform $\beta|t| \le c$ method, and added `AMENDMENT.md` containing exact replacement LaTeX text and BibTeX entries for `W/MASSIVE/BARRIERS2-PAPER/main.tex` and `refs.bib` (extending Theorems 5.1 and 5.3 to all $U_{\rm eff} \in \mathbb{R}$, adding the attractive and repulsive minimum ceilings and the $U$-monotonicity counterexample, and keeping Theorem 5.4(i) and (iii) at $U_{\rm eff} = 0$).

## Post-Fix Verification and File Hashes (SHA-256)

- `python -B D:/dev/scratch/ceiling-20261118/MASSIVE/UNIFORM-SSH/replay.py`: exit `0`
- `python -B D:/dev/scratch/ceiling-20261118/MASSIVE/UNIFORM-SSH/replay.py --all-mutants`: exit `0` (all 8 mutants rejected with exit `1`)
- `SCOPING.md`: `5ada44806e89912e28cb46b00f7d1ef21bed2b5b97ee015521a204a7dbd8aed9`
- `RIGOR.md`: `e531dc33494a9f8e21ed23c3c95ed02cab64c55e31e2ccf3699024aa9649f227`
- `RESULT.md`: `9231d8759d51d1d6d9aafa16fc35644c0948747de4a039de46e614e8f3c368a2`
- `replay.py`: `ad11612ef66bc537b7d4f26978f332ef22a909282a8e1d4ce07266e3a3ba8628`
- `AMENDMENT.md`: `2b3f6fad0cf762ab6036cf200afd4e5c87b8a1a0952dffca9d37b8a4ac2db2c5`
- `REVIEW.md` (untouched): `1d6b3eed7feca76c1c6edae7308681f29294c3f7cdf79c324cc5b7c44e3a57a8`
