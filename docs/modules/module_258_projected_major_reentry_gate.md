# Module 258: Projected-major reentry gate

## 1. Precise theorem / claim being advanced

This module compares the fixed-support boundary obstruction from Modules
224-257 with the projected major-arc package from Modules 206-213 and the
analytic side-package audit in Module 229.

The boundary branch currently has:

```text
FixedRowFeasGate_255
  => FixedRowOnePointPkg_249
  => OnePointBIHL_242,

TwoPointEscGate_256
  => TwoPointBIHL_256.
```

Both implications are conditional. Neither proves a local boundary theorem
outside the exact fixed-row hypotheses.

The projected major-arc branch has:

```text
WProjectedLocalMatch_3^major(P_adm)
  + ProjectedModelNeutrality_3^major(P_adm)
    => ProjectedMajorTarget_3^B(P_adm).
```

Module 229 names the full major side package:

```text
MajorAnalyticPkg_229
  = exact projected local model Omega_w^proj
    + residual subset-HL matching
    + structural collision synchronization
    + collision-defect control when a generic model is used
    + kernel absolute-mass and tail control
    + CycIntTransfer_3^major
    + projection-boundary transfer
    + W-residue compatibility
    + prime-power transfer
    + denominator and CRT range admissibility
    + projected model-neutrality
    + selector transfer.
```

Define:

```text
BoundaryMajorReentry_258(s0,D0,rho0;P_adm)
```

to be the routing ledger deciding whether a boundary gate is:

```text
a local slice of projected-major boundary transfer,
mixed because it changes projection, cutoff, denominator range, or selector,
endpoint-strength through ProjectedMajorTarget_3^B,
or false / blocked as a shortcut to WProjectedLocalMatch_3^major.
```

The structural claim is:

```text
Fixed boundary gates can contribute to CycIntTransfer_3^major only as named
boundary-transfer slices. They do not prove WProjectedLocalMatch_3^major,
ProjectedModelNeutrality_3^major, or ProjectedMajorTarget_3^B.
```

Conversely:

```text
ProjectedMajorTarget_3^B
```

does not automatically prove the fixed boundary gates. It is a projected
nonzero-frequency fourth-moment target, while the boundary gates are
absolute, boundary-supported, `|W_M|`-weighted interval/cutoff/residue rows.
Using the projected major-arc target to close them is endpoint-strength unless
one has first isolated a local boundary-transfer theorem in the same fixed
row.

The branch verdict is:

```text
The boundary branch is relevant to the projected-major package, but only as a
local transfer slice. It should not keep expanding into larger tuple rows as
if it were the whole major-arc problem. Module 259 should perform the required
plan update and choose whether the next branch attacks a non-boundary major
row, a localized boundary-transfer slice, or returns to minor arcs.
```

This module does not prove `CycIntTransfer_3^major`,
`WProjectedLocalMatch_3^major`, `ProjectedModelNeutrality_3^major`,
`ProjectedMajorTarget_3^B`, any boundary gate, or the residual cube endpoint.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The module is a routing and comparison audit. It classifies how the fixed
boundary obstruction relates to the projected-major package and records which
uses are local, mixed, endpoint-strength, or blocked. It supplies no new
analytic estimate.

## 3. Definitions and variables

Use the fixed boundary row:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
BdPrefRow_224^P(s0,D0;N,w,rho0),
Pi=P_M,
edge=cyc_s0 -> int_s0,
D0<|d|<=2D0,
w fixed, N -> infinity, then w -> infinity.
```

For this selector class:

```text
nu=nu_s0,
f=nu-1,
B_d(n)=f(n+d)conj(f(n)).
```

The projected major-arc operator is:

```text
widehat{P_M F}(xi)=m_M(xi)widehat{F}(xi),
m_M(0)=0,
supp(m_M) subset Major(R0,eta0)\{0}.
```

Let:

```text
K_M(t)=sum_xi m_M(xi)e(xi t),
W_M(t0,t1,t2,t3)
  = K_M(t0)conj(K_M(t1))conj(K_M(t2))K_M(t3).
```

The four projected `B_d` slots are:

```text
x00=n-t0,
x10=n+h-t1,
x01=n+k-t2,
x11=n+h+k-t3.
```

The eight projected residual vertices are:

```text
v_{00,0}=x00,
v_{00,1}=x00+d,
v_{10,0}=x10,
v_{10,1}=x10+d,
v_{01,0}=x01,
v_{01,1}=x01+d,
v_{11,0}=x11,
v_{11,1}=x11+d.
```

Let:

```text
Lambda_8={(00,0),(00,1),(10,0),(10,1),
          (01,0),(01,1),(11,0),(11,1)}.
```

The residual product is:

```text
ProductB_d(n,h,k;t)
  = B_d(x00) conj(B_d(x10)) conj(B_d(x01)) B_d(x11).
```

The fixed boundary/prefix row from Module 224 is:

```text
BdPrefRow_224^P
  = (1/D0) sum_{D0<|d|<=2D0}
      E_{n,h,k,t} |W_M(t)| |ProductB_d(n,h,k;t)|
        BdPref_224(d,n,h,k;t).
```

Module 225 reduces this row to:

```text
AbsMajorant_225(s0),
KernelAbsTail_225(P_M,T0),
BoundaryTupleHL_225(S,lambda),
BoundaryModelMass_225(S,lambda),
WPPBoundary_225,
NormRow_224^P.
```

The one-point and two-point diagnostics are:

```text
OnePointBIHL_242
  = BoundaryIntervalHL_234({(00,0)},(00,0)),

TwoPointBIHL_256
  = BoundaryIntervalHL_234({(00,0),(00,1)},(00,0)).
```

Their exact face models are:

```text
Theta_{w,{(00,0)}}^proj=1,
Theta_{w,{(00,0),(00,1)}}^proj=kappa_w(d).
```

The projected major-arc target from Module 206 is:

```text
ProjectedMajorTarget_3^B(N,w;rho):
  |(1/D) sum_{D<|d|<=2D} ActualProjCube_d^P|=o_W(1),
```

where:

```text
ActualProjCube_d^P
  = E_{n,h,k,t} W_M(t)
      ProductB_d(n,h,k;t).
```

The exact projected residual local model is:

```text
Omega_w^proj(d,h,k;t)
  = sum_{S subset Lambda_8}
      (-1)^(8-|S|) Theta_{w,S}^proj(d,h,k;t).
```

The projected model cube is:

```text
ModelProjCube_d^P
  = E_{h,k,t} W_M(t) Omega_w^proj(d,h,k;t).
```

The matching and neutrality errors are:

```text
MatchErr_major^P
  = (1/D) sum_{D<|d|<=2D}
      |ActualProjCube_d^P-ModelProjCube_d^P|,

NeutralErr_major^P
  = |(1/D) sum_{D<|d|<=2D} ModelProjCube_d^P|.
```

Module 209 records:

```text
WProjectedLocalMatch_3^major(P_adm):
  MatchErr_major^P=o_W(1)
```

uniformly over `rho in P_adm(N,w)`, after the required residual subset-HL,
boundary, W-residue, prime-power, projection, denominator, and selector rows
are supplied.

## 4. Assumptions

This module assumes only the definitions above and the project status ledger:

```text
Boundary gates are conditional or open.
CycIntTransfer_3^major is not proved.
WProjectedLocalMatch_3^major is not proved.
ProjectedModelNeutrality_3^major is not proved.
ProjectedMajorTarget_3^B is not proved.
ResCube_3^sharp is open.
```

No comparison may change:

```text
selector class s0,
projection P_M,
dyadic shell D0<|d|<=2D0,
kernel K_M or truncation T0,
cutoff0,
W-residue convention,
interval boundary convention,
fixed-w then N -> infinity then w -> infinity limit order.
```

The module does not assume:

```text
FixedRowFeasGate_255,
TwoPointEscGate_256,
FixedSupportTupleHL_238,
CycIntTransfer_3^major,
WProjectedLocalMatch_3^major,
ProjectedModelNeutrality_3^major,
ProjectedMajorTarget_3^B,
MajorAnalyticPkg_229,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3.
```

## 5. Proof / disproof / reduction

### A. Object comparison

The fixed boundary gates are absolute transfer rows. They measure the part of
the projected cube where at least one residual vertex lies in the boundary or
prefix region, or where a fixed kernel truncation/convention fails:

```text
E |W_M(t)| |ProductB_d| 1_boundary.
```

The projected-major target is a signed nonzero-frequency fourth-moment target:

```text
(1/D) sum_d E W_M(t) ProductB_d=o_W(1).
```

The projected local-model matching theorem is a full actual/model comparison:

```text
ActualProjCube_d^P
  -> ModelProjCube_d^P
  -> projected model neutrality.
```

These are not the same object:

```text
boundary rows:
  physical support near interval endpoints,
  absolute `|W_M|` weights,
  fixed selector and fixed dyadic shell,
  cyclic-to-interval transfer purpose;

projected-major target:
  spectral major-arc fourth moment,
  signed projected cube average,
  full admissible parameter family,
  local-model matching plus model-neutrality purpose.
```

Therefore:

```text
ProjectedMajorTarget_3^B
  => FixedRowFeasGate_255
```

is not a local implication. It is endpoint-strength unless converted into the
same absolute boundary row by a named local theorem.

Likewise:

```text
FixedRowFeasGate_255 + TwoPointEscGate_256
  => WProjectedLocalMatch_3^major
```

is false / blocked as a shortcut. Boundary gates do not supply residual
subset-HL matching, collision synchronization, denominator admissibility,
model neutrality, prime-power transfer, projection-boundary transfer, or
selector transfer.

### B. Where boundary gates legitimately enter the major branch

The legitimate entry point is the boundary component of:

```text
CycIntTransfer_3^major(P_adm).
```

Module 210 decomposes that transfer package into:

```text
ActBd_major,
ModelBd_major,
WrapBd_major,
TailBd_major,
CutoffBd_major,
NormBd_major,
ZeroLeak_major,
WResBd_major.
```

The fixed row:

```text
BdPrefRow_224^P(s0,D0;N,w,rho0)
```

is a candidate local slice of `ActBd_major` together with the fixed kernel
tail and normalization conventions, but only for:

```text
one selector class,
one projection,
one dyadic shell,
one cutoff,
one W-residue convention,
one edge cyc_s0 -> int_s0.
```

To become a piece of `CycIntTransfer_3^major(P_adm)`, it would need a lifting
row such as:

```text
MajorBoundarySlice_258(s0,D0,rho0):
  BdPrefRow_224^P
  + NormRow_224^P
  + fixed W-residue, cutoff, zero-leak, and tail conventions
    => the fixed-row ActBd_major contribution is o_W(1).
```

This is local only if all terms stay in the same fixed row.

To become uniform over the full admissible family, one would need:

```text
MajorBoundaryLift_258:
  fixed-row boundary slices for every required rho in P_adm
  + summable or uniform control over dyadic shells, projections, cutoffs,
    denominator ranges, W-residue classes, and selector classes
    => the boundary part of CycIntTransfer_3^major(P_adm).
```

This is mixed, not a fixed-row local theorem, because it changes the scope
from one `rho0` to the whole family `P_adm`.

### C. Boundary tuple rows versus residual subset-HL matching

`BoundaryTupleHL_225(S,lambda)` has the shape:

```text
E |W_M(t)| 1_{v_lambda boundary}
  prod_{sigma in S} mu_s0(v_sigma)
  =
E |W_M(t)| BdVol_lambda Theta_{w,S}^proj
  + o_W(1).
```

The projected local-model matching row in Module 209 has the residual signed
shape:

```text
E W_M(t)
  sum_{S subset Lambda_8} (-1)^(8-|S|)
    Error_S(d,h,k;t)
  = o_W(1).
```

The first is positive, boundary-supported, and absolute in the kernel. The
second is signed, full-domain, and residual after inclusion-exclusion.

Thus neither row automatically implies the other:

```text
BoundaryTupleHL_225(S,lambda)
  does not prove ResHLErr_major=o_W(1),

ResHLErr_major=o_W(1)
  does not prove BoundaryTupleHL_225(S,lambda)
```

unless the proof supplies a named boundary subset-HL estimate in the same
norm. A possible named row is:

```text
MajorBoundarySubsetHL_258(S,lambda;s0,D0,rho0):
  the projected subset-HL asymptotic for S remains valid after inserting
  the boundary support 1_{v_lambda boundary} and replacing W_M by |W_M|.
```

This row is local only in the fixed `rho0` form. It becomes mixed when lifted
to all selectors, projections, denominators, and dyadic shells.

### D. Boundary model mass versus projected model neutrality

`BoundaryModelMass_225(S,lambda)` asks for absolute local-model mass on a
boundary support:

```text
E |W_M(t)| BdVol_lambda |Theta_{w,S}^proj(d,h,k;t)|=o_W(1).
```

Projected model neutrality asks for cancellation of the full residual
inclusion-exclusion model:

```text
|(1/D) sum_d E_{h,k,t} W_M(t) Omega_w^proj(d,h,k;t)|=o_W(1).
```

The second does not imply the first. It is signed, full-domain, and residual.
The first is absolute and boundary-supported. Therefore:

```text
ProjectedModelNeutrality_3^major
  => BoundaryModelMass_225(S,lambda)
```

is false / blocked unless a separate absolute boundary model-mass lemma is
supplied.

Conversely, proving boundary model mass for one `(S,lambda)` does not prove
projected model neutrality, because neutrality requires the full residual
sum over all `S` and the full `h,k,t,d` domain.

### E. One-point and two-point gates inside the projected local model

The one-point row has:

```text
Theta_{w,{(00,0)}}^proj=1.
```

The same-slot two-point diagnostic has:

```text
Theta_{w,{(00,0),(00,1)}}^proj=kappa_w(d).
```

These are exact face identities inside the projected local-model dictionary.
They are useful because they test small faces of:

```text
Theta_{w,S}^proj.
```

They are not the full residual model:

```text
Omega_w^proj
  = sum_{S subset Lambda_8} (-1)^(8-|S|) Theta_{w,S}^proj.
```

Therefore:

```text
OnePointBIHL_242 or TwoPointBIHL_256
  => WProjectedLocalMatch_3^major
```

is false / blocked as a shortcut. These rows can only contribute to the
boundary-transfer or boundary-subset-HL ledger for the labels they actually
test.

### F. Comparison table

| Proposed use | Classification | Reason |
|---|---|---|
| Fixed boundary gates proved in the same `rho0` row | local transfer slice | They may contribute to `ActBd_major`, tails, normalization, or side rows for `CycIntTransfer_3^major`. |
| Fixed boundary gates lifted uniformly to all `P_adm` | mixed | Requires range, projection, denominator, cutoff, W-residue, and selector uniformity beyond one row. |
| Boundary gates used to prove `WProjectedLocalMatch_3^major` | false / blocked | Matching also needs residual subset-HL, collisions, prime powers, projection, denominator, and selector rows. |
| Boundary gates used to prove `ProjectedModelNeutrality_3^major` | false / blocked | Boundary support does not imply full residual model cancellation. |
| `ProjectedMajorTarget_3^B` used to close boundary gates | endpoint-strength | Uses the major endpoint target to prove a local transfer row. |
| `WProjectedLocalMatch_3^major` used through its boundary components only | conditional / mixed | Valid only if the boundary component is explicitly separated from the full package. |
| `BoundaryTupleHL_225(S,lambda)` as residual subset-HL matching | false / blocked | Boundary absolute tuple rows are not full signed residual matching. |
| `ResHLErr_major=o_W(1)` as boundary tuple-HL | false / blocked | Full signed residual matching does not give absolute boundary tuple control. |
| `BoundaryModelMass_225` from projected model neutrality | false / blocked | Signed model cancellation does not imply absolute boundary mass. |
| One-point or two-point face identities as full `Omega_w^proj` control | false / blocked | Face factors are not the residual inclusion-exclusion model. |
| Reentering projected major arcs after Module 257 | structurally justified | It identifies the boundary branch as a slice of the major transfer package, not a substitute for it. |

### G. Conditional routing statement

The valid routing statement is:

```text
BoundaryMajorReentry_258:

1. If a boundary gate is proved in the exact fixed row `rho0`, classify it as
   local and attach it only to the corresponding boundary-transfer slice.

2. If a boundary gate is lifted from fixed `rho0` to `P_adm`, classify the
   lift as mixed unless all projection, denominator, cutoff, W-residue, range,
   and selector uniformity rows are explicitly supplied.

3. If a boundary gate is closed by assuming `ProjectedMajorTarget_3^B`,
   `WProjectedLocalMatch_3^major` as an undivided package, or
   `ResCube_3^sharp`, classify the route as endpoint-strength or circular.

4. If `WProjectedLocalMatch_3^major` is claimed from boundary gates alone,
   classify the route as false / blocked.

5. If `ProjectedMajorTarget_3^B` is claimed from boundary gates alone,
   classify the route as false / blocked.
```

This routing statement is structural. It proves no estimate.

## 6. Edge cases

- `BdPrefRow_224^P` uses `|W_M|`; projected major-arc cancellation uses the
  signed kernel product `W_M`. Moving between them requires an absolute-mass
  or signed-to-absolute row.
- `ProjectedMajorTarget_3^B` excludes zero frequency through `m_M(0)=0`.
  Interval truncation can reintroduce zero-mode leakage unless
  `ZeroLeak_major` or `NormZeroOne_242` is supplied.
- The fixed row is one dyadic shell. `P_adm` may require uniformity over a
  family of shells and parameter choices.
- One-point and two-point boundary means test only selected faces of the
  projected local model; they do not test all subsets of the residual
  inclusion-exclusion model.
- `BoundaryModelMass_225` is absolute. Projected model neutrality is signed.
  Neither should be used as the other without a named compatibility lemma.
- `CycIntTransfer_3^major` contains model boundary, wraparound, tail, cutoff,
  normalization, zero-leak, and W-residue terms; proving one actual boundary
  row does not prove the whole package.
- Prime powers remain outside pure boundary transfer unless they are included
  in `WPPBoundary_225` or `PPSPTransfer_3^major`.
- Selector class `s0` is fixed. No statement here reaches the actual moving
  selector `mv`.
- Denominator and CRT range admissibility are not boundary estimates. They
  stay in `MajorAnalyticPkg_229`.
- Large-prime collision strata are part of the exact local model; removing
  them requires the collision-defect rows from Modules 187-192 and 208-209.

## 7. Where it fits in the project map

The Phase G boundary diagnostics now stand at:

```text
Module 251:
  BoundaryLengthGate_251.

Module 252:
  KernelHolderGate_252.

Module 253:
  WShortRangeGate_253.

Module 254:
  SideConventionGate_254.

Module 255:
  FixedRowFeasGate_255.

Module 256:
  TwoPointEscGate_256.

Module 257:
  BoundaryMinorReentry_257.

Module 258:
  BoundaryMajorReentry_258.
```

The projected major-arc side remains:

```text
WProjectedLocalMatch_3^major
  + ProjectedModelNeutrality_3^major
    => ProjectedMajorTarget_3^B
```

only conditionally, through `MajorAnalyticPkg_229`.

This module places the fixed boundary branch at:

```text
BdPrefRow_224^P
  -> possible fixed-row slice of CycIntTransfer_3^major
  -> possible component of MajorAnalyticPkg_229,
```

not at:

```text
BdPrefRow_224^P
  -> WProjectedLocalMatch_3^major
  -> ProjectedMajorTarget_3^B.
```

The next module should perform the scheduled plan update:

```text
Module 259:
  eighth long-term plan update and branch decision after the minor-arc and
  projected-major reentry comparisons.
```

## 8. What remains open

This module does not prove:

- `BoundaryMajorReentry_258` as an analytic estimate;
- `MajorBoundarySlice_258`;
- `MajorBoundaryLift_258`;
- `MajorBoundarySubsetHL_258(S,lambda;s0,D0,rho0)`;
- `BdPrefRow_224^P`;
- `BoundaryTupleHL_225(S,lambda)`;
- `BoundaryModelMass_225(S,lambda)`;
- `FixedRowFeasGate_255`;
- `TwoPointEscGate_256`;
- `OnePointBIHL_242`;
- `TwoPointBIHL_256`;
- `CycIntTransfer_3^major`;
- `WProjectedLocalMatch_3^major`;
- `ProjectedModelNeutrality_3^major`;
- `ProjectedMajorTarget_3^B`;
- `MajorAnalyticPkg_229`;
- `ResCube_3^sharp`;
- `RBDH_pair_short`;
- `CPC_3^sharp`;
- `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not use `ProjectedMajorTarget_3^B` as a boundary theorem.
- Do not use `WProjectedLocalMatch_3^major` without separating its boundary,
  local-model matching, collision, prime-power, denominator, projection, and
  selector rows.
- Do not cite a fixed boundary row as full `CycIntTransfer_3^major(P_adm)`.
- Do not cite one-point or two-point local factors as control of
  `Omega_w^proj`.
- Do not replace `Omega_w^proj` by the full eight-form model or by any one
  face model.
- Do not infer absolute boundary mass from signed projected model neutrality.
- Do not move from fixed selector class `s0` to the actual moving selector
  without `MajorSelectorTransfer_3^P`.
- Do not change projection, cutoff, denominator range, dyadic shell, W-residue
  convention, or limit order while calling the route local.
- Do not close this comparison by assuming `ResCube_3^sharp`,
  `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, or endpoint class is proved.
