# Module 252: Kernel absolute-mass and Holder feasibility

## 1. Precise theorem / claim being advanced

This module tests the kernel side of the one-point feasibility package after
Module 251.

Module 251 reduced the boundary-length route to:

```text
OPMeanErr_244
  <= (C_mean_245+1)A_W(M)GeomModel_251 + MassErr_245.
```

Module 245 also gave the Holder route:

```text
OPMeanErr_244
  <= K_q(M)E_p(s0).
```

Define:

```text
KernelHolderGate_252(s0,D0,rho0)
```

to be the fixed-row kernel package containing:

```text
KernelMassGate_252:
  (C_mean_245+1)A_W(M)GeomModel_251 + MassErr_245=o_W(1),

or

KernelHolderGate_252(p,q):
  K_q(M)E_p(s0)=o_W(1),
  1/p+1/q=1.
```

The conditional claim is:

```text
KernelHolderGate_252(s0,D0,rho0)
  => KernelAvgStrength_245^local(s0,D0,rho0)
```

through either the boundary-length route or the Holder route.

The feasibility verdict is:

```text
The kernel gate is local only if A_W(M), K_q(M), and P_M are controlled in
the same fixed projection used by the row. If boundedness or integrability is
obtained only by replacing P_M with a smoother or different projection, the
route is mixed. If kernel control is obtained only from projected residual
fourth-moment endpoint estimates, the route is endpoint-strength.
```

This module does not prove the kernel gate.

## 2. Status label

`CONDITIONAL`

The module derives fixed-row kernel criteria and blocks projection-changing
shortcuts. It does not prove bounded absolute kernel mass, a Holder saving, or
the one-point boundary mean estimate.

## 3. Definitions and variables

Use the fixed row:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
w fixed, N -> infinity, then w -> infinity.
```

The fixed nonzero projected kernel is:

```text
P_M F(x)=E_t K_M(t)F(x-t),
K_M(t)=sum_xi m_M(xi)e(xi t),
m_M(0)=0.
```

The four-kernel weight is:

```text
W_M(t0,t1,t2,t3)
  = K_M(t0)conj(K_M(t1))conj(K_M(t2))K_M(t3).
```

The one-kernel absolute masses are:

```text
A_1(M)=E_t |K_M(t)|,
K_{1,q}(M)=(E_t |K_M(t)|^q)^(1/q).
```

The four-kernel masses used by Module 245 are:

```text
A_W(M)=E_t |W_M(t)|,
K_q(M)=(E_t |W_M(t)|^q)^(1/q).
```

When the four `t_i` variables are independently averaged with the same
normalization:

```text
A_W(M)=A_1(M)^4,
K_q(M)=K_{1,q}(M)^4.
```

The one-point error norm from Module 245 is:

```text
E_p(s0)
  = ((1/D0)sum_d E_{h,k,t} E_1(s0;d,h,k;t)^p)^(1/p),
```

where:

```text
E_1(s0;d,h,k;t)
  = sum_{r in {L,R}}
      |E_n 1_{J_r}(n)(mu_s0(n-t0)-1)|.
```

The deterministic boundary fraction from Module 251 is:

```text
GeomModel_251(D0,rho0)
  = 2L_N/N + EdgeGeom_251(D0,rho0).
```

## 4. Assumptions

The fixed-row kernel package may be supplied by either route.

### A. Boundary-mass kernel route

There is a fixed-row kernel envelope:

```text
A_W(M) <= a_W_252(N,w,rho0),
```

and:

```text
(C_mean_245+1)a_W_252(N,w,rho0)GeomModel_251
  + MassErr_245=o_W(1).
```

### B. Holder kernel route

There are exponents:

```text
1<p,q<infinity,
1/p+1/q=1,
```

and fixed-row estimates:

```text
K_q(M) <= k_q_252(N,w,rho0),
E_p(s0) <= e_p_252(N,w,rho0),
```

with:

```text
k_q_252(N,w,rho0)e_p_252(N,w,rho0)=o_W(1).
```

### C. Fixed projection discipline

Both routes must keep:

```text
same P_M,
same K_M,
same selector class s0,
same dyadic shell D0<|d|<=2D0,
same boundary intervals J_L,J_R,
same cutoff0,
same W-residue convention,
same fixed-w then N -> infinity then w -> infinity limit order.
```

The module does not assume:

```text
A_W(M)=O_W(1),
K_q(M)=O_W(1),
K_q(M)E_p(s0)=o_W(1),
projection smoothing transfer,
KernelAvgStrength_245,
OPMeanErr_244=o_W(1),
OnePointSideRows_246^local,
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
RBDH_pair_short,
CPC_3^sharp,
AU^3.
```

## 5. Proof / disproof / reduction

### A. Four-kernel mass reduction

By definition:

```text
A_W(M)
  = E_{t0,t1,t2,t3}
      |K_M(t0)||K_M(t1)||K_M(t2)||K_M(t3)|.
```

With independent `t_i` averages:

```text
A_W(M)=A_1(M)^4.
```

Similarly:

```text
K_q(M)^q
  = E_t |W_M(t)|^q
  = (E_t |K_M(t)|^q)^4,
```

so:

```text
K_q(M)=K_{1,q}(M)^4.
```

These identities are bookkeeping identities for the fixed projection. They do
not prove either mass is bounded.

### B. Boundary-mass route

Module 251 gives:

```text
BLength_245 <= A_W(M)GeomModel_251.
```

Module 245 gives:

```text
OPMeanErr_244
  <= (C_mean_245+1)BLength_245 + MassErr_245.
```

Combining:

```text
OPMeanErr_244
  <= (C_mean_245+1)A_W(M)GeomModel_251 + MassErr_245.
```

Thus if `KernelMassGate_252` holds:

```text
OPMeanErr_244=o_W(1).
```

This supplies `KernelAvgStrength_245^local` through the boundary-length route,
provided the kernel envelope and mass majorant are fixed-row local.

### C. Holder route

Module 245 gives:

```text
OPMeanErr_244
  <= K_q(M)E_p(s0).
```

If:

```text
K_q(M) <= k_q_252,
E_p(s0) <= e_p_252,
k_q_252e_p_252=o_W(1),
```

then:

```text
OPMeanErr_244=o_W(1).
```

This supplies `KernelAvgStrength_245^local` through the Holder route if both
the kernel estimate and the `E_p(s0)` estimate are fixed-row local.

### D. Feasible patterns

A boundary-mass feasible pattern is:

```text
A_W(M)=O_W(1),
C_mean_245=O_W(1),
GeomModel_251=o_W(1),
MassErr_245=o_W(1).
```

More generally, the route permits growth in `A_W(M)` only if:

```text
A_W(M)GeomModel_251=o_W(1)
```

after the `C_mean_245` growth and `MassErr_245` are included.

A Holder feasible pattern is:

```text
K_q(M)=O_W(g_K),
E_p(s0)=o_W(g_K^{-1}).
```

This may work even when the boundary-length route fails, but only if the
unweighted `E_p(s0)` estimate is strong enough and does not change selector
class or projection.

### E. Blocked patterns

The boundary-mass route is blocked if:

```text
(C_mean_245+1)A_W(M)GeomModel_251
```

does not tend to zero and `MassErr_245` does not compensate.

The Holder route is blocked if every available `E_p(s0)` estimate is too weak
to beat `K_q(M)`, or if the only way to improve `K_q(M)` is to replace `P_M`.

The full kernel gate is not blocked merely because one route fails. It is
blocked only if all fixed-row kernel routes fail and no non-kernel route from
Module 245 remains available.

### F. Local versus mixed versus endpoint-strength

The gate is local if:

```text
A_W(M), K_q(M), E_p(s0), MassErr_245,
```

are all proved in the same fixed row.

It is mixed if it uses:

```text
smoothed projection replacing P_M,
kernel truncation not already in rho0,
major/minor projection replacement,
selector transfer,
cutoff transfer,
range repair,
changed W-residue convention.
```

It is endpoint-strength if it uses:

```text
(1/D0)sum_d ||P_M B_{d,s0}||_{U^2}^4=o_W(1),
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3.
```

## 6. Edge cases

- If `P_M` is a sharp major-arc projection, `A_1(M)` and `K_{1,q}(M)` may grow;
  bounded absolute mass is not automatic.
- If a smoothed projection makes `A_W(M)=O_W(1)`, the result is mixed unless a
  projection-transfer row returns to the original `P_M`.
- If `A_W(M)` is large but `GeomModel_251` is tiny enough, the boundary route
  may still be feasible.
- If `A_W(M)GeomModel_251` is not small, the Holder route can still survive
  if `K_q(M)E_p(s0)=o_W(1)`.
- If `q` is close to `1`, `K_q(M)` may be smaller but the conjugate `p` is
  large; the required `E_p(s0)` estimate becomes stronger.
- If `q` is large, the kernel norm may see sharp spikes of `K_M`.
- If `E_p(s0)` is proved only after changing selector class, the Holder route
  is mixed.
- If `K_q(M)` is estimated using cancellation in `W_M`, the estimate is not
  applicable to `|W_M|`.
- If the kernel has a nonzero zero mode, the row no longer matches the
  projected nonzero convention.

## 7. Where it fits in the project map

The Phase G feasibility chain is now:

```text
Module 251:
  boundary length is reduced to A_W(M)GeomModel_251.

Module 252:
  tests A_W(M), K_q(M), and P_M as fixed-row kernel gates.
```

The output is:

```text
KernelHolderGate_252
  => KernelAvgStrength_245^local
```

through either:

```text
boundary mass:
  (C_mean_245+1)A_W(M)GeomModel_251 + MassErr_245=o_W(1),

or Holder:
  K_q(M)E_p(s0)=o_W(1).
```

The next module should test whether the W branch has a matching interval
theorem:

```text
Module 253:
  short-interval W-PNT range audit for WOneBoundaryPNT_244.
```

## 8. What remains open

This module does not prove:

- `KernelHolderGate_252(s0,D0,rho0)`;
- `A_W(M)=O_W(1)`;
- any fixed-row bound for `K_q(M)`;
- `K_q(M)E_p(s0)=o_W(1)`;
- `E_p(s0)=o_W(1)` in any useful range;
- `MassErr_245=o_W(1)`;
- `BoundaryLengthGate_251(s0,D0,rho0)`;
- `KernelAvgStrength_245^local(s0,D0,rho0)` except conditionally;
- `FixedRowOnePointPkg_249(s0,D0,rho0)`;
- `OnePointSideRows_246^local(s0,D0,rho0)`;
- `OPMeanErr_244(W,D0,rho0)=o_W(1)`;
- `OPMeanErr_244(sm,D0,rho0)=o_W(1)`;
- `OPMeanErr_244(fr,D0,rho0)=o_W(1)`;
- `OnePointBIHL_242` outside the exact model convention;
- any short-interval W-tricked PNT;
- any two-point fixed-support row;
- `FixedSupportTupleHL_238`;
- `LocalBdPkg_226`;
- `BdPrefRow_224^P=o_W(1)`;
- selector transfer to the actual sharp moving selector;
- `ProjectedMajorTarget_3^B`;
- `ResCube_3^sharp`;
- `RBDH_pair_short`;
- `CPC_3^sharp`;
- `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not assume `A_W(M)=O_W(1)` for the active projection without proof.
- Do not replace `P_M` by a smoother projection without a projection-transfer
  row.
- Do not use signed cancellation in `W_M` after the row has taken `|W_M|`.
- Do not treat a kernel `L^q` estimate as enough without the matching
  `E_p(s0)` estimate.
- Do not hide selector, cutoff, range, W-residue, or side-row transfer inside
  a kernel estimate.
- Do not treat failure of the boundary-mass route as failure of the Holder or
  short-interval routes.
- Do not close this gate by assuming `ProjectedMajorTarget_3^B`,
  `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`.
- Do not upgrade model, W, smoothed, or frozen selector statements to the
  actual sharp moving selector.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, or endpoint class is proved.
