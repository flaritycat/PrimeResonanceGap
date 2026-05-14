# Module 238: Fixed-row composition and first bottleneck

## 1. Precise theorem / claim being advanced

This module composes the Phase F1 fixed-row subpackages from Modules 233-237
and identifies the first true bottleneck.

The fixed row remains:

```text
BdPrefRow_224^P(s0,D0;N,w,rho0),
Pi=P_M,
edge=cyc_s0 -> int_s0,
same selector class s0,
D0<|d|<=2D0.
```

Define the composed package:

```text
FixedRowPkg_238(s0,D0,rho0).
```

Conditional claim:

```text
FixedRowPkg_238(s0,D0,rho0)
  => BdPrefRow_224^P(s0,D0;N,w,rho0)=o_W(1)
```

and, with Module 224:

```text
FixedRowPkg_238(s0,D0,rho0)
  => (1/D0) sum_{D0<|d|<=2D0}
       |ActualProjCube_{d,cyc,s0}^P
        -ActualProjCube_{d,int,s0}^P|
     = o_W(1).
```

The first bottleneck is:

```text
nonempty fixed-support weighted tuple control,
headed by BoundaryIntervalHL_234(S,lambda) for S nonempty.
```

More precisely, the bottleneck is the family of W-admissible weighted tuple
estimates on the fixed boundary/tail supports:

```text
BoundaryIntervalHL_234(S,lambda),
TailTuple_235(S),
WResTuple_236(S),
PPTupleBoundary_236(S,tau),
```

with exact projected local models and the same fixed selector, projection,
dyadic shell, W-residue convention, and limit order.

This module does not prove that family.

## 2. Status label

`CONDITIONAL`

The composition is deterministic once the named subpackages hold. The
bottleneck estimates remain open.

## 3. Definitions and variables

Use:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
w fixed, N -> infinity, then w -> infinity.
```

The eight labels are:

```text
Lambda_8={(00,0),(00,1),(10,0),(10,1),
          (01,0),(01,1),(11,0),(11,1)}.
```

The fixed residual product is:

```text
ProductB_d(n,h,k;t)
  = B_d(n-t0)
    conj(B_d(n+h-t1))
    conj(B_d(n+k-t2))
    B_d(n+h+k-t3).
```

The boundary and tail support is:

```text
BdPref_224
  <= TailT_224 + sum_{lambda in Lambda_8} Bd_lambda.
```

The Module 225 reduction requires:

```text
AbsMajorant_225(s0),
KernelAbsTail_225(P_M,T0),
BoundaryTupleHL_225(S,lambda),
BoundaryModelMass_225(S,lambda),
WPPBoundary_225,
NormRow_224^P.
```

The Phase F1 replacement rows are:

```text
BoundaryModelVolume_233(S,lambda),
BoundaryIntervalHL_234(S,lambda),
KernelTailBudget_235(P_M,T0;s0,D0,rho0),
WPPBoundaryAudit_236(s0,D0,rho0),
NormZeroAudit_237(s0,D0,rho0).
```

## 4. Assumptions

`FixedRowPkg_238(s0,D0,rho0)` consists of:

### A. Fixed-row discipline

All rows use the same:

```text
P_M,
K_M,
R0 and eta0,
selector class s0,
W-residue convention,
prime-only or prime-power convention,
centering convention,
interval cutoff convention,
dyadic shell D0<|d|<=2D0,
fixed w, then N -> infinity, then w -> infinity limit order.
```

There is no:

```text
fr -> mv,
sm -> fr,
bern -> sm,
fs -> bern,
major/minor partition transfer,
projection smoothing transfer,
denominator-grid transfer.
```

### B. Absolute majorant

The row includes:

```text
AbsMajorant_225(s0).
```

This is needed before the absolute-value reduction of Module 225 can expand
`|ProductB_d|` into positive tuple rows.

### C. Model mass

For every:

```text
S subset Lambda_8,
lambda in Lambda_8,
```

the row includes:

```text
BoundaryModelVolume_233(S,lambda).
```

By Module 233:

```text
BoundaryModelVolume_233(S,lambda)
  => BoundaryModelMass_225(S,lambda).
```

### D. Actual boundary tuple matching

For:

```text
S=emptyset,
```

use the exact identity from Module 234:

```text
BoundaryTupleHL_225(emptyset,lambda)
```

has zero error.

For every nonempty:

```text
S subset Lambda_8,
lambda in Lambda_8,
```

the row includes:

```text
BoundaryIntervalHL_234(S,lambda).
```

By Module 234:

```text
BoundaryIntervalHL_234(S,lambda)
  => BoundaryTupleHL_225(S,lambda).
```

### E. Kernel absolute-tail package

The row includes:

```text
KernelTailBudget_235(P_M,T0;s0,D0,rho0).
```

By Module 235:

```text
KernelTailBudget_235
  => KernelAbsTail_225(P_M,T0).
```

This includes `TailCube_225(T0)=o_W(1)` only if the tail residual-product
envelope or `TailTuple_235(S)` rows are supplied.

### F. W-residue and prime-power boundary package

The row includes:

```text
WPPBoundaryAudit_236(s0,D0,rho0).
```

By Module 236:

```text
WPPBoundaryAudit_236
  => WPPBoundary_225=o_W(1).
```

### G. Normalization and zero-mode package

The row includes:

```text
NormZeroAudit_237(s0,D0,rho0).
```

By Module 237:

```text
NormZeroAudit_237
  => NormRow_224^P=o_W(1)
```

and:

```text
ZeroBd_226=o_W(1)
```

when `ZeroBd_226` is active.

## 5. Proof / disproof / reduction

Start from the deterministic Module 225 reduction:

```text
AbsMajorant_225
  + KernelAbsTail_225
  + BoundaryTupleHL_225(S,lambda)
  + BoundaryModelMass_225(S,lambda)
  + WPPBoundary_225
  + NormRow_224^P=o_W(1)

    => BdPrefRow_224^P=o_W(1).
```

Insert the Phase F1 replacement rows:

```text
BoundaryModelVolume_233
  => BoundaryModelMass_225,

BoundaryIntervalHL_234
  => BoundaryTupleHL_225 for S nonempty,

S=emptyset
  => BoundaryTupleHL_225(emptyset,lambda) exactly,

KernelTailBudget_235
  => KernelAbsTail_225,

WPPBoundaryAudit_236
  => WPPBoundary_225,

NormZeroAudit_237
  => NormRow_224^P and active ZeroBd_226.
```

Therefore:

```text
FixedRowPkg_238(s0,D0,rho0)
  => BdPrefRow_224^P(s0,D0;N,w,rho0)=o_W(1).
```

Module 224 then gives the fixed cyclic-to-interval transfer:

```text
(1/D0) sum_{D0<|d|<=2D0}
  |ActualProjCube_{d,cyc,s0}^P
    -ActualProjCube_{d,int,s0}^P|
  = o_W(1).
```

This is a composition theorem only. It proves no endpoint estimate.

### First bottleneck

The individual audits show the following hierarchy.

The most bookkeeping-like rows are:

```text
NormExact_237 / NormDrift_237,
CenterDiff_237,
ZeroBd_226,
WPPOverlap_236 or DisjointAccount_236.
```

These may be delicate, but they are lower-dimensional or convention-driven.

The model-side row:

```text
BoundaryModelVolume_233(S,lambda)
```

is smaller than the projected endpoint if the exact local factors are bounded
or their bad-factor mass is already localized.

The first genuinely analytic bottleneck is the actual weighted tuple family:

```text
BoundaryIntervalHL_234(S,lambda),  S nonempty.
```

It asks for prime-type mass not to concentrate on the boundary intervals in
the same `|W_M|`-weighted fixed-row normalization. This is not supplied by
boundary volume, first-moment HL, ordinary pair-BDH, or the model mass.

The same technology must also cover the tail and W/prime-power support rows:

```text
TailTuple_235(S),
WResTuple_236(S),
PPTupleBoundary_236(S,tau).
```

Thus the honest compressed bottleneck is:

```text
FixedSupportTupleHL_238:
  W-admissible weighted tuple control for the fixed boundary/tail/support
  sets, with exact projected local factors and no selector or projection
  change.
```

### Smaller-than-endpoint diagnosis

`FixedSupportTupleHL_238` is genuinely smaller than the projected residual
endpoint only if every support set carries a declared smallness mechanism:

```text
boundary interval length,
kernel tail support,
W-residue failure support,
prime-power support,
or a fixed local diagonal/collision support.
```

If those supports are removed and the proof uses the full unlocalized cube,
then the package becomes endpoint-strength.

## 6. Edge cases

- The exact `S=emptyset` tuple row does not help with any nonempty tuple row.
- If `TailTuple_235(S)` is replaced by `Tail_W(T0)=o_W(1)` alone, the
  residual product has not been controlled.
- If `BoundaryIntervalHL_234` is proved using full projected residual
  fourth-moment cancellation, the row is endpoint-strength.
- If W-residue or prime-power artifacts are not supported on the fixed
  boundary/tail set, they are mixed transfer rows outside `LocalBdPkg_226`.
- If `NormRow_224^P` is declared zero without exact normalization equality,
  the composition is invalid.
- If `m_M(0)=0` is used after interval truncation without checking
  `z_M(T0)`, zero-mode leakage may survive.
- If the selector class changes, this is no longer the fixed row from
  Modules 224-237.
- If the projection is smoothed or retuned, a projection-transfer row is
  needed before the composition applies.
- If a local factor is replaced by a generic collision-free model, the exact
  `Theta_{w,S}^proj` discipline has been lost.

## 7. Where it fits in the project map

The Phase F1 fixed-row chain is now:

```text
Module 233
  -> model mass criterion.
Module 234
  -> boundary tuple-HL audit.
Module 235
  -> kernel absolute-tail budget.
Module 236
  -> W-residue and prime-power boundary audit.
Module 237
  -> normalization and zero-mode audit.
Module 238
  -> composition and first bottleneck.
```

The useful output is that `LocalBdPkg_226` now has a sharper internal map:

```text
bookkeeping / convention rows:
  normalization, zero-mode, overlap, exact zero rows;

model rows:
  boundary volume plus local-factor budgets;

first analytic bottleneck:
  fixed-support weighted tuple HL.
```

The next planned step, Module 239, should attempt a model-class proof or
blocked verdict for the easiest subrow. The natural easiest subrow is the
model-side or purely convention-zero case, not the full nonempty actual
weighted tuple family.

## 8. What remains open

This module does not prove:

- `FixedSupportTupleHL_238`;
- any nonempty `BoundaryIntervalHL_234(S,lambda)`;
- any `TailTuple_235(S)`;
- any `WResTuple_236(S)`;
- any `PPTupleBoundary_236(S,tau)`;
- `BoundaryModelVolume_233(S,lambda)` beyond its conditional statement;
- `KernelTailBudget_235(P_M,T0;s0,D0,rho0)` beyond its conditional statement;
- `WPPBoundaryAudit_236(s0,D0,rho0)` beyond its conditional statement;
- `NormZeroAudit_237(s0,D0,rho0)` beyond its conditional statement;
- `FixedRowPkg_238(s0,D0,rho0)` unconditionally;
- `LocalBdPkg_226`;
- `BdPrefRow_224^P=o_W(1)` unconditionally;
- `CycIntTransfer_3^major(P_adm)`;
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

- Do not cite this composition as proving the fixed row unconditionally.
- Do not collapse the five subpackages into an unnamed generic side error.
- Do not treat model mass as actual tuple matching.
- Do not replace nonempty boundary tuple-HL by boundary volume, ordinary
  pair-BDH, or first-moment Hardy-Littlewood.
- Do not use `Tail_W(T0)=o_W(1)` as a substitute for `TailCube_225(T0)`.
- Do not hide W-residue, prime-power, normalization, or zero-mode terms
  inside local factors or tuple notation.
- Do not prove `FixedSupportTupleHL_238` by assuming the projected residual
  endpoint.
- Do not change selector class, projection, W-residue convention, or dyadic
  shell inside this fixed-row composition.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem,
  `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
