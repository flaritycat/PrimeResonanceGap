# Module 262: Fifth plan challenge for Phase H

## 1. Precise theorem / claim being advanced

This module performs the fifth 15-iteration plan challenge required by the
long-term schedule. It questions Phase H after `Reflective_3.md` and
`ProjectedModelNeutralityGate_260(P_adm)`.

Define:

```text
PlanChallenge_5_262.
```

The challenge asks whether the projected model-neutrality branch is genuinely
testing a model-side row smaller than the projected major endpoint, or whether
it is already drifting into endpoint-strength assumptions.

The challenge verdict is:

```text
Continue Phase H, but only in narrowed proof-or-blocked mode through the
model-neutrality subrows.
```

The narrowed rule is:

```text
Modules 263-267 must test the exact signed inclusion-exclusion expansion,
collision-defect row, kernel route, W/denominator/projection uniformity, and
then give a proof-or-blocked verdict. Do not move to full
WProjectedLocalMatch_3^major until model neutrality is classified.
```

This challenge does not prove `ProjectedModelNeutrality_3^major`, does not
prove `WProjectedLocalMatch_3^major`, and does not prove any endpoint object.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is a planning and audit module. It introduces no new analytic estimate
and only narrows the next steps.

## 3. Definitions and variables

The cadence counters before this module were:

```text
Latest completed module: 261
Post-Reflective_1 solving count: 80
Long-term-plan count: 74
```

This module advances the counters to:

```text
Latest completed module: 262
Post-Reflective_1 solving count: 81
Long-term-plan count: 75
```

The cadence arithmetic is:

```text
75 is divisible by 15,
75 is not divisible by 9,
81 is not the next reflection threshold.
```

Therefore:

```text
fifth plan challenge is due,
ninth plan update is not due until Module 268,
next reflection remains expected around Module 301.
```

The Phase H model-side target is:

```text
ProjectedModelNeutrality_3^major(P_adm):
  NeutralErr_major^P(N,w;rho)=o_W(1)
```

uniformly over:

```text
rho in P_adm(N,w).
```

The exact model object remains:

```text
ModelProjCube_d^P
  = E_{h,k,t} W_M(t) Omega_w^proj(d,h,k;t),

NeutralErr_major^P
  = |(1/D) sum_{D<|d|<=2D} ModelProjCube_d^P|.
```

Module 260 defined:

```text
ProjectedModelNeutralityGate_260(P_adm)
```

as:

```text
ModelConv_260
+ GenericTail_260
+ (KernelAbsNeutral_260 or KernelSignedNeutral_260)
+ CollNeutral_260
+ DenWProjNeutral_260
+ ModelCutNeutral_260.
```

The challenge questions are:

```text
Q1. Is ProjectedModelNeutralityGate_260 genuinely smaller than the projected
    major endpoint?
Q2. Does removing CollNeutral_260 collapse the route?
Q3. Does removing signed kernel cancellation collapse the route?
Q4. Is NarrowMinorArc_3^B / transverse incidence now a better target?
Q5. What would make Phase H stop early?
```

## 4. Assumptions

This challenge assumes only the recorded outputs of Modules 259-261:

```text
PlanUpdate_8_259:
  Phase H selected.

ProjectedModelNeutralityGate_260:
  model-neutrality rows named but not proved.

Reflective_3.md:
  Modules 221-260 reviewed and hidden-upgrade risks recorded.
```

It does not assume:

```text
ProjectedModelNeutralityGate_260,
ProjectedModelNeutrality_3^major,
WProjectedLocalMatch_3^major,
ProjectedMajorTarget_3^B,
CollNeutral_260,
KernelSignedNeutral_260,
KernelAbsNeutral_260,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3.
```

The challenge preserves:

```text
exact Omega_w^proj discipline,
fixed-w then N -> infinity then w -> infinity limit order,
declared selector class,
declared projection and kernel convention,
dyadic and denominator admissibility,
no endpoint upgrade without proof.
```

## 5. Proof / disproof / reduction

This section answers the challenge questions.

### Q1. Is the model-neutrality gate smaller than the projected major endpoint?

The optimistic answer is yes, but only in a narrow sense. Model neutrality is
a model-side row:

```text
E_{h,k,t} W_M(t) Omega_w^proj(d,h,k;t),
```

not an actual prime-weight tuple estimate. It avoids residual subset-HL
matching and actual/model comparison.

The cautious answer is that uniformity over:

```text
P_adm(N,w)
```

can make the row much larger than a toy model calculation. In particular,
the following can make the gate endpoint-strength in practice:

```text
uncontrolled collision defects,
kernel mass that overwhelms generic W-tail saving,
signed kernel cancellation that effectively assumes major-arc cancellation,
denominator/CRT ranges that cannot be made uniform,
projection changes that require transfer back to the original target.
```

Verdict:

```text
ProjectedModelNeutralityGate_260 is plausibly smaller than the projected major
endpoint only if Modules 263-266 keep every row model-side and uniform over
P_adm without invoking actual projected major cancellation.
```

### Q2. Does removing `CollNeutral_260` collapse the route?

For the generic route:

```text
Omega_w^proj = Omega_w^gen + Delta_w^coll,
```

yes. Without:

```text
CollNeutral_260,
```

generic W-tail cancellation controls only:

```text
Omega_w^gen.
```

It says nothing about the part of the exact model carried by structural or
congruence collision strata:

```text
Delta_w^coll(d,h,k;t).
```

There are only two honest alternatives:

```text
1. Prove CollNeutral_260.
2. Avoid the generic decomposition and prove a direct exact-model neutrality
   estimate that is smaller than the projected major endpoint.
```

Verdict:

```text
CollNeutral_260 is a critical row. Module 264 should test it before Phase H
is allowed to become a full major-arc matching project.
```

### Q3. Does removing signed kernel cancellation collapse the route?

Not necessarily. Module 260 allows an absolute route:

```text
A_W(M) eps_gen(w)=o_W(1).
```

If this row holds, signed cancellation is unnecessary for the generic term.
But this is a real condition: if the absolute kernel mass grows faster than
the generic W-tail saving, the absolute route fails.

The signed route:

```text
KernelSignedNeutral_260
```

is not forbidden, but it is dangerous. It must be proved for the exact
multiplier, denominator family, kernel truncation, and normalization. It may
not be imported from Phase G boundary rows, because those rows use `|W_M|`.

Verdict:

```text
The route does not collapse without signed cancellation if the absolute
kernel budget survives. Module 265 should decide whether the absolute route
is viable; if not, it must classify the signed route as local/model-side,
mixed, endpoint-strength, or blocked.
```

### Q4. Is the minor-arc transverse-incidence branch now better?

The minor branch remains one of the real obstructions:

```text
NarrowMinorArc_3^B
  = low-level leakage
    + bad-shift moments
    + persistent-frequency multiplicity
    + transverse incidence.
```

Module 257 showed that boundary gates do not prove it. The branch still needs
non-tautological spectral incidence, and that may be closer to the endpoint
than model neutrality is.

However, Module 260 just isolated concrete model-side rows. It would be
premature to abandon Phase H before testing:

```text
signed inclusion-exclusion structure,
collision defects,
kernel budget,
denominator/W-limit uniformity.
```

Verdict:

```text
Do not redirect to minor arcs yet. Keep minor transverse incidence as the main
alternative if Module 264 or Module 265 marks Phase H endpoint-strength.
```

### Q5. What would make Phase H stop early?

Phase H should stop early if any of the following happens:

```text
CollNeutral_260 can only be proved by assuming ProjectedMajorTarget_3^B,
WProjectedLocalMatch_3^major, ResCube_3^sharp, CPC_3^sharp, RBDH_pair_short,
or AU^3.

Both kernel routes fail:
  A_W(M) eps_gen(w) is not o_W(1),
  and KernelSignedNeutral_260 is endpoint-strength or unavailable.

Uniformity over P_adm requires changing projection, cutoff, denominator
family, dyadic shell, W-residue convention, selector class, or limit order
without transfer rows.

The exact residual model Omega_w^proj is replaced by the full eight-form
model, a pair face, a rectangle face, or an unprojected model.
```

Verdict:

```text
Phase H continues only through the named proof-or-blocked tests. It must stop
or redirect if the model-neutrality row becomes endpoint-strength.
```

### F. Branch decision

The challenge decision is:

```text
Continue Phase H through Modules 263-267 in narrowed proof-or-blocked mode.
```

The next steps are:

```text
Module 263:
  expand NeutralErr_major^P into the exact signed inclusion-exclusion subset
  average and identify which cancellations are structural.

Module 264:
  test collision and diagonal strata for CollNeutral_260.

Module 265:
  test kernel absolute budget versus signed kernel cancellation.

Module 266:
  test W-limit, denominator, CRT range, projection-boundary, and dyadic
  uniformity over P_adm.

Module 267:
  give a proof-or-blocked verdict for ProjectedModelNeutralityGate_260.
```

No module in this sequence may assume the full projected major target or the
residual endpoint.

## 6. Edge cases

- If Module 263 finds that all useful cancellation comes from replacing
  `Omega_w^proj` by a simpler model, the route is blocked unless the
  replacement has an averaged compatibility theorem.
- If Module 264 proves only a pointwise collision exclusion by removing
  structural strata from one side, the route is not synchronized.
- If Module 265 uses signed kernel cancellation, the result cannot be
  transferred to absolute boundary rows.
- If Module 265 uses absolute kernel mass, it must pay the full `A_W(M)`
  cost.
- If Module 266 needs a diagonal `w=w(N)` limit, it does not satisfy the
  project W-limit order unless recovered as a two-stage estimate.
- If the selector class changes, the result belongs to selector transfer and
  not to model neutrality.
- If the proof uses ordinary pair-BDH, rectangle-BDH, first-moment HL, or
  generic finite-complexity HL as model neutrality, the route is a blocked
  shortcut.
- If Phase H needs `MajorAnalyticPkg_229` as a black box, it has become too
  broad and should stop.

## 7. Where it fits in the project map

The current route is:

```text
Module 259:
  Phase H selected.

Module 260:
  ProjectedModelNeutralityGate_260 named.

Module 261:
  Reflective_3 checks the previous forty iterations.

Module 262:
  fifth plan challenge narrows Phase H.
```

The next module should be:

```text
Module 263:
  signed inclusion-exclusion expansion of NeutralErr_major^P.
```

This keeps Phase H pointed at a concrete model-side row rather than the full
projected major endpoint.

## 8. What remains open

This module does not prove:

- `ProjectedModelNeutralityGate_260(P_adm)`;
- `ProjectedModelNeutrality_3^major(P_adm)`;
- `NeutralErr_major^P=o_W(1)`;
- `GenericTail_260`;
- `CollNeutral_260`;
- `KernelAbsNeutral_260`;
- `KernelSignedNeutral_260`;
- `DenWProjNeutral_260`;
- `ModelCutNeutral_260`;
- `WProjectedLocalMatch_3^major(P_adm)`;
- `ProjectedMajorTarget_3^B(P_adm)`;
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

- Do not treat this challenge as evidence for model neutrality.
- Do not continue Phase H by adding broad package names instead of testing
  `CollNeutral_260`, kernel budget, and uniformity rows.
- Do not close `CollNeutral_260` by assuming the projected major target or the
  endpoint.
- Do not use signed kernel cancellation unless it is stated as
  `KernelSignedNeutral_260` in the same admissible family.
- Do not import Phase G absolute boundary estimates as signed model
  cancellation.
- Do not replace `Omega_w^proj` by the full eight-form model, a pair face, a
  rectangle face, or an unprojected model.
- Do not move between selectors, projections, cutoffs, denominator families,
  W-residue conventions, dyadic shells, or W-limit orders without named
  transfer rows.
- Do not cite ordinary pair-BDH, rectangle-BDH, first-moment HL, or generic HL
  as model neutrality.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, `ResCube_3^sharp`, `CPC_3^sharp`,
  `RBDH_pair_short`, or `AU^3` is proved.
