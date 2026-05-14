# Module 245: Kernel-average strength audit for the one-point row

## 1. Precise theorem / claim being advanced

This module audits how strong the one-point boundary mean input from Module
244 must be after the absolute projected kernel average.

The active row remains:

```text
OnePointBIHL_242(s0,D0,rho0)
  = BoundaryIntervalHL_234({(00,0)},(00,0)).
```

Module 244 reduced the open analytic target to:

```text
OPMeanErr_244(s0,D0,rho0)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t} |W_M(t)|
        sum_{r in {L,R}}
          |E_n 1_{J_r}(n)(mu_s0(n-t0)-1)|.
```

Define:

```text
KernelAvgStrength_245(s0,D0,rho0)
```

to be the package of one-point boundary mean estimates strong enough to make:

```text
OPMeanErr_244(s0,D0,rho0)=o_W(1).
```

The conditional claim is:

```text
KernelAvgStrength_245(s0,D0,rho0)
  => OPMeanErr_244(s0,D0,rho0)=o_W(1).
```

The audit verdict is:

```text
The one-point row is smaller than the projected residual endpoint only if
the required boundary mean saving is proved directly in the |W_M|-weighted
fixed-row normalization, or by a pointwise / Holder route that explicitly
beats the absolute kernel mass.
```

This module does not prove `KernelAvgStrength_245`.

## 2. Status label

`CONDITIONAL`

The module records sufficient strength criteria and their classifications. It
does not prove any W-tricked, smoothed, or frozen boundary mean estimate.

## 3. Definitions and variables

Use the fixed row:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
w fixed, N -> infinity, then w -> infinity.
```

The projected kernel notation is:

```text
W_M(t0,t1,t2,t3)
  = K_M(t0)conj(K_M(t1))conj(K_M(t2))K_M(t3).
```

The absolute kernel mass is:

```text
A_W(M)=E_t |W_M(t)|.
```

For the active boundary intervals:

```text
J_r=J_r(d,h,k;t),  r in {L,R},
ell_r(d,h,k;t)=E_n 1_{J_r}(n).
```

Define the pointwise one-point error:

```text
e_r(s0;d,h,k;t)
  = E_n 1_{J_r}(n)(mu_s0(n-t0)-1).
```

Set:

```text
E_1(s0;d,h,k;t)
  = sum_{r in {L,R}} |e_r(s0;d,h,k;t)|.
```

Then:

```text
OPMeanErr_244(s0,D0,rho0)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t}|W_M(t)| E_1(s0;d,h,k;t).
```

The boundary length budget is:

```text
BLength_245(D0,rho0)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t}|W_M(t)|
        sum_{r in {L,R}} ell_r(d,h,k;t).
```

The worst boundary length is:

```text
ell_*_245(rho0)
  = sup_{d,h,k,t,r} ell_r(d,h,k;t)
```

over the fixed truncated row.

The unweighted one-point error average is:

```text
UMeanErr_245(s0,D0,rho0)
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{h,k,t} E_1(s0;d,h,k;t).
```

For Holder routes, define:

```text
K_q(M) = (E_t |W_M(t)|^q)^(1/q),
E_p(s0) = ((1/D0) sum_d E_{h,k,t} E_1(s0;d,h,k;t)^p)^(1/p),
```

with:

```text
1/p+1/q=1.
```

## 4. Assumptions

`KernelAvgStrength_245(s0,D0,rho0)` is satisfied by any one of the following
routes, always with the same selector class, projection, dyadic shell,
W-residue convention, interval cutoff, and limit order.

### A. Direct weighted route

The direct route is:

```text
DirectOPMean_245(s0,D0,rho0):
  OPMeanErr_244(s0,D0,rho0)=o_W(1).
```

This is tautological but important: it is the exact estimate needed and it
has the correct `|W_M|` weighting.

### B. Uniform absolute-error route

There is a pointwise error envelope:

```text
E_1(s0;d,h,k;t) <= eps_abs_245(N,w,rho0)
```

for all fixed-row parameters, and:

```text
A_W(M) eps_abs_245(N,w,rho0)=o_W(1).
```

This route is only useful if the one-point mean error beats the absolute
kernel mass.

### C. Boundary-length majorant route

There is a one-point boundary mass majorant:

```text
E_n 1_{J_r}(n) mu_s0(n-t0)
  <= C_mean_245(w,rho0) ell_r(d,h,k;t)
     + err_r^mass(d,h,k;t),
```

and:

```text
MassErr_245
  = (1/D0) sum_d E_{h,k,t}|W_M(t)|
      sum_r |err_r^mass(d,h,k;t)|
  = o_W(1),
```

with:

```text
(C_mean_245(w,rho0)+1) BLength_245(D0,rho0)=o_W(1).
```

This route does not need cancellation inside each boundary interval, but it
does need the weighted boundary length to beat the kernel mass and any growth
in the one-point majorant.

### D. Relative boundary-PNT route

There is a relative one-point interval estimate:

```text
|e_r(s0;d,h,k;t)|
  <= eps_rel_245(N,w,rho0) ell_r(d,h,k;t)
     + err_r^rel(d,h,k;t),
```

with:

```text
RelErr_245
  = (1/D0) sum_d E_{h,k,t}|W_M(t)|
      sum_r |err_r^rel(d,h,k;t)|
  = o_W(1),
```

and:

```text
eps_rel_245(N,w,rho0) BLength_245(D0,rho0)=o_W(1).
```

This is stronger than the mass-majorant route when `eps_rel_245 -> 0`, but
it may require a genuine short-interval prime theorem in the active selector
class.

### E. Holder route

For some:

```text
1<p,q<infinity,
1/p+1/q=1,
```

one has:

```text
K_q(M) E_p(s0)=o_W(1).
```

This route is useful only if the kernel has better `L^q` behavior than its
absolute mass and the mean errors have corresponding `L^p` control.

## 5. Proof / disproof / reduction

### A. Direct route

The direct route is the target itself:

```text
DirectOPMean_245
  <=> OPMeanErr_244=o_W(1).
```

Thus it implies the target immediately.

### B. Uniform absolute-error route

If:

```text
E_1(s0;d,h,k;t) <= eps_abs_245,
```

then:

```text
OPMeanErr_244
  <= eps_abs_245
     (1/D0) sum_d E_{h,k,t}|W_M(t)|.
```

The remaining average is `A_W(M)` in the fixed normalization. Hence:

```text
OPMeanErr_244 <= A_W(M) eps_abs_245=o_W(1).
```

### C. Boundary-length majorant route

The triangle inequality gives:

```text
|e_r|
  <= E_n 1_{J_r} mu_s0(n-t0) + ell_r.
```

Using the mass majorant:

```text
|e_r|
  <= (C_mean_245+1) ell_r + |err_r^mass|.
```

Multiplying by `|W_M|`, summing over `r`, and averaging gives:

```text
OPMeanErr_244
  <= (C_mean_245+1) BLength_245 + MassErr_245.
```

The assumptions in Route C make this `o_W(1)`.

### D. Relative boundary-PNT route

If:

```text
|e_r| <= eps_rel_245 ell_r + |err_r^rel|,
```

then:

```text
OPMeanErr_244
  <= eps_rel_245 BLength_245 + RelErr_245.
```

The route assumptions make this `o_W(1)`.

### E. Holder route

Apply Holder in the variables:

```text
d,h,k,t
```

with the fixed dyadic-shell average:

```text
OPMeanErr_244
  = E(|W_M| E_1)
  <= (E |W_M|^q)^(1/q) (E E_1^p)^(1/p)
  = K_q(M) E_p(s0).
```

Thus:

```text
K_q(M) E_p(s0)=o_W(1)
  => OPMeanErr_244=o_W(1).
```

### F. Strength classification

The one-point row is local under this audit only if the proof uses one of
the fixed-row routes above without changing:

```text
selector class,
projection,
W-residue convention,
dyadic shell,
denominator grid,
interval cutoff,
fixed-w then N -> infinity then w -> infinity limit order.
```

It is mixed if the proof needs projection smoothing, selector transition,
W-residue-family transfer, denominator-grid movement, or range changes.

It is endpoint-strength if the only way to make `OPMeanErr_244=o_W(1)` is to
assume:

```text
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
(1/D0) sum_d ||P_M B_{d,s0}||_{U^2}^4=o_W(1),
CoreSel_major^P,
MoveLayerCube_3^Pi.
```

## 6. Edge cases

- If `A_W(M)=O_W(1)`, a uniform `eps_abs_245=o_W(1)` is enough. If
  `A_W(M)` grows, the same error must beat that growth.
- If `BLength_245=o_W(1)`, a bounded one-point mass majorant may close the
  row even without cancellation. If `BLength_245` is not small, the boundary
  route has failed.
- If `C_mean_245` grows with `w`, the boundary length must beat that growth
  in the project limit order.
- If the boundary intervals are shorter than the available short-interval
  theorem for the chosen selector class, the relative-PNT route is blocked
  by range rather than by the residual endpoint.
- If only an unweighted average `UMeanErr_245=o_W(1)` is known, it does not
  imply the weighted target unless kernel correlation is controlled, for
  example by Holder or a pointwise bound.
- If the proof uses cancellation in `W_M`, it does not apply to this row
  after the absolute value has been taken.
- If smoothing the projection is used to improve `A_W(M)`, a projection
  transfer row is required and the proof is mixed.
- If the smoothed or frozen selector branch is compared to the W branch, the
  comparison must use the named transfer rows from Module 244.
- Prime-power, W-residue, cutoff, range, normalization, and zero-mode rows
  remain separate from this kernel-average strength audit.

## 7. Where it fits in the project map

The Phase F2 chain now has:

```text
Module 242
  -> fixed OnePointBIHL_242.

Module 243
  -> reduced the local model to Theta=1 and main term ell_r.

Module 244
  -> reduced the row to OPMeanErr_244 by selector class.

Module 245
  -> audits the strength required after the |W_M| average.
```

The next module should audit the side rows:

```text
CutOne_242,
RangeOne_242,
WResOne_242,
PPOne_242,
NormZeroOne_242.
```

## 8. What remains open

This module does not prove:

- `KernelAvgStrength_245(s0,D0,rho0)`;
- `OPMeanErr_244(W,D0,rho0)=o_W(1)`;
- `OPMeanErr_244(sm,D0,rho0)=o_W(1)`;
- `OPMeanErr_244(fr,D0,rho0)=o_W(1)`;
- bounded `A_W(M)` for the chosen projection;
- `BLength_245=o_W(1)`;
- any short-interval W-tricked prime theorem in the required range;
- any smoothed or frozen selector boundary mean theorem;
- `CutOne_242=o_W(1)`;
- `RangeOne_242=o_W(1)`;
- `WResOne_242=o_W(1)`;
- `PPOne_242=o_W(1)`;
- `NormZeroOne_242=o_W(1)`;
- `OnePointBIHL_242` outside the exact normalized model branch;
- any off-vertex one-point row;
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

- Do not treat an unweighted boundary mean estimate as enough after the
  `|W_M|` average.
- Do not assume `A_W(M)=O_W(1)` for a sharp projection without proof.
- Do not use `BLength_245=o_W(1)` without checking kernel absolute mass and
  possible growth of `C_mean_245`.
- Do not replace short boundary interval estimates by full-interval
  first-moment Hardy-Littlewood.
- Do not cite ordinary pair-BDH or rectangle-BDH as a one-point boundary mean
  theorem.
- Do not use cancellation from `W_M` after the row has taken `|W_M|`.
- Do not change selector class, projection, cutoff, W-residue convention,
  denominator grid, or dyadic shell inside a strength route.
- Do not hide prime-power, W-residue, range, cutoff, normalization, or
  zero-mode terms inside `KernelAvgStrength_245`.
- Do not prove the strength package by assuming `ProjectedMajorTarget_3^B`,
  `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, or endpoint class is proved.
