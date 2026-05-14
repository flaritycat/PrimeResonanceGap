# Module 251: Deterministic boundary-length feasibility

## 1. Precise theorem / claim being advanced

This module tests the deterministic boundary-length route for the one-point
package from Module 249.

The target route from Module 245 is:

```text
OPMeanErr_244
  <= (C_mean_245+1)BLength_245 + MassErr_245.
```

Define:

```text
BoundaryLengthGate_251(s0,D0,rho0)
```

to be the fixed-row condition that the deterministic boundary geometry, after
the absolute projected-kernel weight, is small enough to make the displayed
right-hand side `o_W(1)`.

The main conditional claim is:

```text
BoundaryLengthGate_251(s0,D0,rho0)
  => KernelAvgStrength_245^local(s0,D0,rho0)
```

through the boundary-length majorant route of Module 245.

The feasibility verdict is:

```text
The deterministic boundary-length route is conditional local exactly when
the normalized boundary length beats the absolute kernel mass and the
one-point mass majorant error. It is false / blocked as a closure route if
A_W(M) times the fixed-row boundary fraction is not o_W(1), unless another
non-boundary-length route is supplied.
```

This module does not prove `BoundaryLengthGate_251`.

## 2. Status label

`CONDITIONAL`

The module derives a conditional feasibility criterion and blocks one
over-optimistic shortcut. It does not prove `BLength_245=o_W(1)`,
`OPMeanErr_244=o_W(1)`, or `OnePointBIHL_242`.

## 3. Definitions and variables

Use the fixed row:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
w fixed, N -> infinity, then w -> infinity.
```

The active one-point form is:

```text
m0(n,t)=n-t0.
```

The active boundary intervals are:

```text
J_L(d,h,k;t)={n: m0(n,t) <= L_N},
J_R(d,h,k;t)={n: m0(n,t) > N-L_N}.
```

Write:

```text
ell_r(d,h,k;t)=E_n 1_{J_r}(n),
r in {L,R}.
```

The absolute kernel mass is:

```text
A_W(M)=E_t |W_M(t)|.
```

The weighted boundary length from Module 245 is:

```text
BLength_245(D0,rho0)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t}|W_M(t)|
        sum_{r in {L,R}} ell_r(d,h,k;t).
```

Define the deterministic boundary fraction:

```text
GeomLen_251(D0,rho0)
  = sup_{D0<|d|<=2D0,h,k,t}
      sum_{r in {L,R}} ell_r(d,h,k;t).
```

Define a more explicit row geometry bound:

```text
GeomModel_251(D0,rho0)
  = 2L_N/N + EdgeGeom_251(D0,rho0),
```

where `EdgeGeom_251` records deterministic losses from truncation, cutoff
placement, empty/overlapping boundary conventions, and row-domain mismatch.

The gate is:

```text
BoundaryLengthGate_251(s0,D0,rho0):
  one-point mass majorant of Module 245 holds, and
  (C_mean_245(w,rho0)+1) A_W(M) GeomModel_251(D0,rho0)
    + MassErr_245(s0,D0,rho0)
  = o_W(1).
```

When the sharper quantity `GeomLen_251` is known directly, `GeomModel_251` may
be replaced by `GeomLen_251`.

## 4. Assumptions

The gate assumes the fixed-row one-point mass majorant from Module 245:

```text
E_n 1_{J_r}(n) mu_s0(m0(n,t))
  <= C_mean_245(w,rho0) ell_r(d,h,k;t)
     + err_r^mass(d,h,k;t),
```

with:

```text
MassErr_245
  = (1/D0) sum_d E_{h,k,t}|W_M(t)|
      sum_r |err_r^mass(d,h,k;t)|
  = o_W(1)
```

after it is included in the gate.

The gate also assumes the deterministic geometry estimate:

```text
sum_{r in {L,R}} ell_r(d,h,k;t)
  <= GeomModel_251(D0,rho0)
```

uniformly over the fixed row.

No assumption may change:

```text
selector class s0,
projection P_M,
kernel K_M,
dyadic shell D0<|d|<=2D0,
boundary intervals J_L,J_R,
cutoff0,
W-residue convention,
normalization,
fixed-w then N -> infinity then w -> infinity limit order.
```

The module does not assume:

```text
A_W(M)=O_W(1),
GeomModel_251=o_W(1),
BLength_245=o_W(1),
OPMeanErr_244=o_W(1),
OnePointSideRows_246^local,
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
RBDH_pair_short,
CPC_3^sharp,
AU^3.
```

## 5. Proof / disproof / reduction

### A. Deterministic bound for `BLength_245`

From the definition of `GeomLen_251`:

```text
sum_{r in {L,R}} ell_r(d,h,k;t)
  <= GeomLen_251(D0,rho0)
```

for every fixed-row parameter. Hence:

```text
BLength_245
  <= GeomLen_251(D0,rho0)
     (1/D0) sum_{D0<|d|<=2D0} E_{h,k,t}|W_M(t)|.
```

The remaining average is the fixed-row absolute kernel mass. Thus:

```text
BLength_245
  <= A_W(M) GeomLen_251(D0,rho0).
```

If:

```text
GeomLen_251 <= GeomModel_251,
```

then:

```text
BLength_245
  <= A_W(M) GeomModel_251(D0,rho0).
```

### B. Boundary-length route to `OPMeanErr_244`

The Module 245 boundary-length route gives:

```text
OPMeanErr_244
  <= (C_mean_245+1)BLength_245 + MassErr_245.
```

Using the deterministic bound:

```text
OPMeanErr_244
  <= (C_mean_245+1) A_W(M) GeomModel_251
     + MassErr_245.
```

Therefore:

```text
BoundaryLengthGate_251
  => OPMeanErr_244=o_W(1).
```

This is precisely:

```text
KernelAvgStrength_245^local
```

through the boundary-length route, provided the mass majorant and geometry
bound are fixed-row local.

### C. Feasible case

The route is feasible when:

```text
GeomModel_251(D0,rho0)
  = 2L_N/N + EdgeGeom_251(D0,rho0),
```

and:

```text
(C_mean_245+1)A_W(M)(2L_N/N + EdgeGeom_251)
  + MassErr_245
  = o_W(1).
```

In particular, a sufficient pattern is:

```text
A_W(M)=O_W(1),
C_mean_245=O_W(1),
L_N/N=o_W(1),
EdgeGeom_251=o_W(1),
MassErr_245=o_W(1).
```

This pattern is conditional local if all quantities are proved inside the same
fixed row.

### D. Blocked case

The boundary-length route is blocked if:

```text
(C_mean_245+1)A_W(M)GeomModel_251
```

does not tend to zero and no compensating `MassErr_245` cancellation is
available. In that case deterministic boundary length alone cannot make:

```text
OPMeanErr_244=o_W(1).
```

This does not disprove other routes from Module 245, such as:

```text
relative boundary-PNT,
uniform pointwise error,
Holder kernel control.
```

It blocks only the deterministic boundary-length majorant route.

### E. Local versus mixed classification

`BoundaryLengthGate_251` is local only if the proof uses the same fixed row.

It becomes mixed if smallness is obtained by:

```text
smoothing P_M,
changing K_M,
altering J_L or J_R,
changing cutoff0,
moving the dyadic shell,
changing W-residue conventions,
changing selector class,
changing the limit order.
```

It becomes endpoint-strength if smallness is obtained by assuming:

```text
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
```

or an equivalent residual fourth-moment theorem.

## 6. Edge cases

- If `J_L` and `J_R` overlap, `sum_r ell_r` is still the quantity appearing in
  `BLength_245`; do not replace it by the measure of the union unless the row
  uses union counting.
- If `cutoff0` removes part of the boundary, the deterministic length may
  improve, but a cutoff side row is then still needed.
- If `m0(n,t)` leaves the allowed interval near an endpoint, the resulting
  loss belongs to `RangeOne_242` or `EdgeGeom_251`, not to the local factor.
- If `A_W(M)` grows with the projection, the boundary length must beat that
  growth in the project limit order.
- If `C_mean_245` grows with `w`, `L_N/N` and `EdgeGeom_251` must beat that
  growth after fixed `w`, `N -> infinity`, and then `w -> infinity`.
- If the active selector weight is signed, the one-point mass majorant must be
  replaced by an absolute mass majorant; positivity cannot be assumed.
- If `BLength_245=o_W(1)` is proved only after smoothing the kernel or
  projection, the route is mixed.
- If the boundary-length route fails, the one-point prototype may still remain
  conditional through a short-interval or Holder route.

## 7. Where it fits in the project map

The Phase G feasibility chain begins with:

```text
Module 249:
  FixedRowOnePointPkg_249 => OnePointBIHL_242.

Module 250:
  Phase G should test FixedRowOnePointPkg_249 before two-point escalation.

Module 251:
  tests the deterministic boundary-length route to KernelAvgStrength_245.
```

The output of this module is:

```text
BoundaryLengthGate_251
  => KernelAvgStrength_245^local
```

and:

```text
if (C_mean_245+1)A_W(M)GeomModel_251 + MassErr_245 is not o_W(1),
then the boundary-length route is blocked.
```

The next module should test the kernel side more directly:

```text
Module 252:
  kernel absolute-mass and Holder feasibility for A_W(M), K_q(M), and P_M.
```

## 8. What remains open

This module does not prove:

- `BoundaryLengthGate_251(s0,D0,rho0)`;
- `BLength_245=o_W(1)`;
- `A_W(M)=O_W(1)`;
- `GeomModel_251=o_W(1)`;
- `MassErr_245=o_W(1)`;
- the one-point mass majorant;
- `KernelAvgStrength_245^local(s0,D0,rho0)` except conditionally;
- `FixedRowOnePointPkg_249(s0,D0,rho0)`;
- `OnePointSideRows_246^local(s0,D0,rho0)`;
- `OPMeanErr_244(W,D0,rho0)=o_W(1)`;
- `OPMeanErr_244(sm,D0,rho0)=o_W(1)`;
- `OPMeanErr_244(fr,D0,rho0)=o_W(1)`;
- `OnePointBIHL_242` outside the exact model convention;
- any short-interval W-tricked PNT;
- any Holder route;
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

- Do not treat `L_N/N=o(1)` as enough without multiplying by `A_W(M)` and
  `C_mean_245`.
- Do not assume `A_W(M)=O_W(1)` for the active projection without proof.
- Do not hide `MassErr_245` inside deterministic geometry.
- Do not replace `sum_r ell_r` by a union length unless the row actually uses
  union counting.
- Do not use smoothing of the projection, kernel, or boundary without marking
  the route mixed.
- Do not treat failure of the boundary-length route as failure of the
  short-interval or Holder routes.
- Do not use ordinary first-moment HL, full-interval PNT, ordinary pair-BDH,
  or rectangle-BDH as a substitute for this fixed-row estimate.
- Do not close this gate by assuming `ProjectedMajorTarget_3^B`,
  `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`.
- Do not upgrade model, W, smoothed, or frozen selector statements to the
  actual sharp moving selector.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, or endpoint class is proved.
