# Module 259: Eighth plan update and branch decision

## 1. Precise theorem / claim being advanced

This module performs the eighth 9-iteration plan update required by the
long-term schedule.

Define:

```text
PlanUpdate_8_259.
```

The update follows the Phase G feasibility gates and the two reentry audits:

```text
Module 257:
  BoundaryMinorReentry_257,

Module 258:
  BoundaryMajorReentry_258.
```

The decision is:

```text
Close Phase G as a useful diagnostic window.
Do not continue blind boundary tuple expansion.
Do not treat fixed boundary gates as minor-arc cancellation or as projected
major-arc matching.
Begin Phase H by testing a non-boundary projected-major bottleneck:
ProjectedModelNeutrality_3^major.
```

The next branch is:

```text
Phase H:
  projected model-neutrality feasibility window.
```

The immediate next module should be:

```text
Module 260:
  ProjectedModelNeutralityGate_260(P_adm),
  a structural/conditional gate for the model-side projected major-arc
  neutrality error.
```

This is a plan update only. It proves no analytic estimate and upgrades no
endpoint object.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module updates the project schedule, records the Phase G verdict, and
extracts the next target window. It does not prove `FixedRowFeasGate_255`,
`CycIntTransfer_3^major`, `WProjectedLocalMatch_3^major`,
`ProjectedModelNeutrality_3^major`, `ProjectedMajorTarget_3^B`, any minor-arc
package, or any endpoint theorem.

## 3. Definitions and variables

Before this module the counters were:

```text
Latest completed module before this update: 258
Post-Reflective_1 solving count before this update: 77
Long-term-plan count before this update: 71
```

This module advances the counters to:

```text
Latest completed module: 259
Post-Reflective_1 solving count: 78
Long-term-plan count: 72
```

The cadence arithmetic is:

```text
72 is divisible by 9,
72 is not divisible by 15,
78 is not the next reflection threshold.
```

Therefore:

```text
eighth plan update is due,
fifth plan challenge is not due until Module 262,
next reflective log remains expected at Module 261.
```

The fixed boundary row from Phase G remains:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
BdPrefRow_224^P(s0,D0;N,w,rho0),
Pi=P_M,
edge=cyc_s0 -> int_s0,
D0<|d|<=2D0,
w fixed, N -> infinity, then w -> infinity.
```

The projected major-arc parameter family remains:

```text
rho=(D,R,eta,P_M,H,K,T,selector,cutoff) in P_adm(N,w).
```

For:

```text
f=nu-1,
B_d(n)=f(n+d)conj(f(n)),
```

the projected major-arc physical cube is:

```text
ActualProjCube_d^P
  = E_{n,h,k,t} W_M(t)
      B_d(n-t0)
      conj(B_d(n+h-t1))
      conj(B_d(n+k-t2))
      B_d(n+h+k-t3).
```

The exact projected residual local model is:

```text
Omega_w^proj(d,h,k;t)
  = sum_{S subset Lambda_8}
      (-1)^(8-|S|) Theta_{w,S}^proj(d,h,k;t).
```

The model cube is:

```text
ModelProjCube_d^P
  = E_{h,k,t} W_M(t) Omega_w^proj(d,h,k;t).
```

The projected model-neutrality target is:

```text
ProjectedModelNeutrality_3^major(P_adm):
  NeutralErr_major^P(N,w;rho)
    = |(1/D) sum_{D<|d|<=2D} ModelProjCube_d^P|
    = o_W(1)
```

uniformly over `rho in P_adm(N,w)` in the fixed-`w`, `N -> infinity`, then
`w -> infinity` order.

## 4. Assumptions

This plan update assumes only the recorded status of Modules 251-258.

Phase G established the following conditional diagnostics:

```text
BoundaryLengthGate_251,
KernelHolderGate_252,
WShortRangeGate_253,
SideConventionGate_254,
FixedRowFeasGate_255,
TwoPointEscGate_256,
BoundaryMinorReentry_257,
BoundaryMajorReentry_258.
```

The update does not assume:

```text
FixedRowFeasGate_255,
FixedRowOnePointPkg_249,
TwoPointEscGate_256,
OnePointBIHL_242,
TwoPointBIHL_256,
BdPrefRow_224^P=o_W(1),
CycIntTransfer_3^major,
WProjectedLocalMatch_3^major,
ProjectedModelNeutrality_3^major,
ProjectedMajorTarget_3^B,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3.
```

The next window must preserve:

```text
exact projected residual model Omega_w^proj,
zero-mode exclusion m_M(0)=0,
declared selector class,
W-trick limit order,
projection and kernel conventions,
dyadic range restrictions,
denominator and CRT admissibility.
```

No result in Phase H may be transferred to the actual sharp moving selector
without the named selector-transfer package.

## 5. Proof / disproof / reduction

### A. Cadence proof

The previous long-term-plan count was:

```text
71.
```

This module is one substantive solving iteration, so the new count is:

```text
72.
```

Since:

```text
72=8*9,
```

the eighth plan update is due.

Since:

```text
72 is not a multiple of 15,
```

the fifth plan challenge is not due. It remains scheduled for Module 262.

The post-`Reflective_1` solving count becomes:

```text
78.
```

The next reflection threshold is count `80`, so the reflective log remains
scheduled for Module 261.

### B. What Phase G achieved

Phase G was not a proof window. It was a feasibility and routing window.

It achieved:

```text
1. Boundary length was separated from mean error.
2. Kernel absolute mass and Holder routes were separated.
3. W short-interval range limitations were isolated.
4. Side rows were split into exact conventions and weighted defects.
5. The one-point package was assembled as conditional, not proved.
6. The same-slot two-point row was allowed only as a diagnostic.
7. Boundary/minor routing was blocked as a shortcut.
8. Boundary/projected-major routing was limited to transfer slices.
```

This is useful because it prevents three errors:

```text
boundary volume => minor-arc cancellation,
boundary gates => projected major-arc matching,
projected major target => boundary gates.
```

All three are blocked unless a named localized theorem supplies the missing
norm and scope.

### C. Why Phase G should stop here

Continuing with larger boundary tuple rows would add complexity before the
project has proved even the one-point fixed-row package. Module 258 also
showed that boundary rows are not the whole major-arc problem; they are only
possible slices of:

```text
CycIntTransfer_3^major.
```

Therefore the next useful move is not:

```text
three-point boundary row,
four-point boundary row,
or full FixedSupportTupleHL_238 by escalation.
```

Those would likely rename unresolved local mean, kernel, side-row, and
uniformity problems.

### D. Why not jump directly to minor arcs

Module 257 showed that the minor-arc branch is a distinct obstruction:

```text
large-spectrum density,
bad-shift moments,
persistent-frequency multiplicity,
transverse incidence,
minor selector transfer.
```

Those rows remain important. But they involve actual spectral incidence
estimates, whereas the projected model-neutrality branch is model-side:

```text
E_{h,k,t} W_M(t) Omega_w^proj(d,h,k;t).
```

It is reasonable to test model neutrality first because it asks whether the
exact local model itself cancels after projection and averaging. If the model
side already fails, then actual projected local-model matching is not the
next bottleneck. If it survives, the later choice between `ResHLErr_major`
and `NarrowMinorArc_3^B` is better informed.

### E. Why not attack full `WProjectedLocalMatch_3^major` next

The full matching package contains:

```text
residual subset-HL matching,
structural synchronization,
collision treatment,
boundary transfer,
kernel tails,
W-residue compatibility,
prime-power transfer,
projection-boundary control,
denominator admissibility,
selector transfer.
```

That is too broad for one next step. The non-boundary model-neutrality row is
smaller and does not require proving actual prime tuple estimates. It should
be tested before the project asks for full residual subset-HL matching.

### F. Phase H window

The next 9-iteration window is:

```text
Phase H: Projected model-neutrality feasibility window.
Target window: Modules 260-268.
```

Expected work:

```text
Module 260:
  formulate ProjectedModelNeutralityGate_260(P_adm), fixing the exact
  model-neutrality object, admissibility scope, and sufficient local-factor,
  kernel, collision, denominator, and W-limit rows.

Module 261:
  create Reflective_3.md, the required 40-iteration memory log after
  Reflective_1, reviewing Modules 221-260 and checking whether any Phase G
  or Phase H claims weakened or overreached.

Module 262:
  perform the fifth 15-iteration plan challenge, asking whether the
  model-neutrality branch is still preferable to minor transverse incidence
  or a localized boundary-transfer slice.

Module 263:
  expand NeutralErr_major^P into the signed inclusion-exclusion subset
  average and identify which subset sizes and face factors can cancel
  structurally and which require analytic averaged compatibility.

Module 264:
  audit collision and diagonal strata inside the projected model-neutrality
  average, separating exact local-model collisions from removable
  collision-defect routes.

Module 265:
  audit kernel signed-cancellation versus absolute-mass requirements for
  model neutrality, including the risk that replacing `W_M` by `|W_M|` loses
  the only available cancellation.

Module 266:
  audit W-limit, denominator, CRT range, projection-boundary, and dyadic
  uniformity requirements for model neutrality over `P_adm`.

Module 267:
  give a proof-or-blocked verdict for the projected model-neutrality route:
  conditional local/model-side, mixed, endpoint-strength, or false/blocked as
  a shortcut.

Module 268:
  perform the ninth plan update and choose whether to continue major
  matching, return to minor arcs, or isolate a boundary-transfer slice.
```

### G. Immediate next action

The next module should be:

```text
Module 260:
  ProjectedModelNeutralityGate_260(P_adm).
```

It should define:

```text
NeutralErr_major^P(N,w;rho),
ModelProjCube_d^P,
Omega_w^proj(d,h,k;t),
the exact `P_adm` scope,
and the side rows needed before model neutrality may be called smaller than
the projected major endpoint.
```

It must not claim:

```text
WProjectedLocalMatch_3^major,
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3.
```

### H. Self-questioning note

The project has spent many iterations making the boundary branch honest. That
was valuable, but it can become a comfort zone: local boundary rows are easier
to name than endpoint estimates are to prove. The next move deliberately
leaves that comfort zone without jumping all the way to actual prime tuple
matching. Model neutrality is still difficult, but it is a cleaner test of
the projected major route.

## 6. Edge cases

- If projected model neutrality requires the full actual projected major-arc
  target, it is endpoint-strength and should be marked accordingly.
- If neutrality is shown only after changing `P_M`, smoothing the projection,
  or discarding denominator ranges, the route is mixed and needs transfer
  rows back to the original target.
- If the model average is controlled only by replacing
  `Omega_w^proj` with the full eight-form local model, the route is blocked.
- If a proof treats the rectangle local factor as the pointwise square of the
  pair local factor, it violates the exact local-model discipline.
- If signed kernel cancellation is essential, no conclusion may be transferred
  to absolute boundary rows.
- If absolute kernel control is used instead, the model-neutrality proof must
  explicitly pay the absolute mass of `W_M`.
- If collision strata are removed from the model average, the same removal
  must be justified by exact collision-defect rows.
- If W-limit estimates are diagonal in `w=w(N)`, they do not satisfy the
  project double-limit order unless the two-stage estimate is recovered.
- If the selector class changes, the result belongs to selector transfer, not
  to model neutrality.
- If the Module 261 reflection or Module 262 challenge identifies a hidden
  upgrade, Phase H must revise before continuing.

## 7. Where it fits in the project map

The project map after Module 259 is:

```text
Modules 251-258:
  Phase G fixed-row feasibility gates and reentry comparisons.

Module 259:
  eighth plan update;
  Phase G closed as diagnostic;
  Phase H selected as projected model-neutrality feasibility.

Module 260:
  begin Phase H with ProjectedModelNeutralityGate_260.
```

The active major-arc chain is:

```text
ProjectedModelNeutrality_3^major
  + WProjectedLocalMatch_3^major
    => ProjectedMajorTarget_3^B,
```

but Phase H attacks only the first model-side component. It does not assume
the full chain.

The boundary branch remains available only as:

```text
fixed-row or mixed slices of CycIntTransfer_3^major.
```

The minor branch remains available only as:

```text
NarrowMinorArc_3^B + MinorArcTransfer_3^B,
```

with both packages still open.

## 8. What remains open

This module does not prove:

- `ProjectedModelNeutralityGate_260(P_adm)`;
- `ProjectedModelNeutrality_3^major(P_adm)`;
- `NeutralErr_major^P=o_W(1)`;
- `WProjectedLocalMatch_3^major(P_adm)`;
- `ProjectedMajorTarget_3^B(P_adm)`;
- `CycIntTransfer_3^major(P_adm)`;
- `MajorAnalyticPkg_229`;
- `BoundaryMajorReentry_258` as an analytic estimate;
- `BoundaryMinorReentry_257` as an analytic estimate;
- `FixedRowFeasGate_255`;
- `FixedRowOnePointPkg_249`;
- `TwoPointEscGate_256`;
- `OnePointBIHL_242`;
- `TwoPointBIHL_256`;
- `NarrowMinorArc_3^B`;
- `MinorArcTransfer_3^B`;
- `ResCube_3^sharp`;
- `RBDH_pair_short`;
- `CPC_3^sharp`;
- `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not treat this plan update as proof of any model-neutrality estimate.
- Do not continue Phase G by escalating to larger boundary tuples unless a
  future plan update or challenge explicitly reopens that branch.
- Do not use boundary gates as minor-arc cancellation.
- Do not use boundary gates as projected local-model matching.
- Do not use `ProjectedMajorTarget_3^B` to prove boundary rows or model
  neutrality.
- Do not replace the residual model `Omega_w^proj` by the full eight-form
  model or by one face factor.
- Do not replace the rectangle local model pointwise by the square of the pair
  local model.
- Do not move between selector classes, projections, cutoffs, denominator
  ranges, W-residue conventions, dyadic shells, or limit orders without named
  transfer rows.
- Do not cite ordinary pair-BDH, rectangle-BDH, first-moment HL, or generic
  finite-complexity HL as projected model neutrality.
- Do not close any Phase H gate by assuming `ResCube_3^sharp`,
  `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, or endpoint class is proved.
