# Module 267: Proof-or-blocked verdict for projected model neutrality

## 1. Precise theorem / claim being advanced

This module performs the fifth and final proof-or-blocked test required by
`PlanChallenge_5_262`: classify the Phase H model-neutrality branch after the
signed expansion, collision audit, kernel audit, and uniformity ledger.

Define:

```text
ProjectedModelNeutralityVerdict_267(P_adm).
```

The verdict has two conditional routes, with a required naming correction:

```text
absolute route:
  AbsPMNGate_267(P_adm)
    => ProjectedModelNeutralityGate_260(P_adm)
    => ProjectedModelNeutrality_3^major(P_adm),

signed exact-model route:
  SignedExactNeutralGate_267(P_adm)
    => ExactModelNeutral_260(P_adm)
    => ProjectedModelNeutrality_3^major(P_adm).
```

The correction is this:

```text
SignedExactNeutralGate_267(P_adm)
  does not prove CollNeutral_260(P_adm).
```

The signed fork can establish the same target `NeutralErr_major^P=o_W(1)`
only if it is kept as a same-family signed exact-model neutrality theorem. It is
not a proof of the literal absolute collision row inside
`ProjectedModelNeutralityGate_260(P_adm)`.

Thus the current Phase H verdict is:

```text
conditional local/model-side if one complete same-family package is supplied;
mixed if transfer rows are needed;
endpoint-strength if the missing rows are imported from the projected major
  target or endpoint class;
false / blocked as a shortcut if ordinary lower-order inputs are used as
  substitutes for the named rows.
```

This module does not prove either route.

## 2. Status label

`CONDITIONAL`

The module records conditional implications and a classification. It
does not prove `ProjectedModelNeutralityGate_260(P_adm)`,
`ExactModelNeutral_260(P_adm)`, `ProjectedModelNeutrality_3^major`, or any
endpoint object.

## 3. Definitions and variables

Use the Phase H admissible data:

```text
rho=(D,R,eta,P_M,H,K,T,selector,cutoff) in P_adm(N,w),
D<|d|<=2D,
w fixed, N -> infinity, then w -> infinity.
```

For any error term `Err(N,w;rho)`, write:

```text
Err=o_W(1) over P_adm
```

to mean:

```text
lim_{w->infinity} limsup_{N->infinity}
  sup_{rho in P_adm(N,w)} |Err(N,w;rho)|=0.
```

The projected model object is:

```text
NeutralErr_major^P(N,w;rho)
  = |NeutralSigned_major^P(N,w;rho)|,

NeutralSigned_major^P(N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      E_{h,k,t} W_M(t) Omega_w^proj(d,h,k;t).
```

Here:

```text
W_M(t0,t1,t2,t3)
  = K_M(t0)conj(K_M(t1))conj(K_M(t2))K_M(t3),

Omega_w^proj(d,h,k;t)
  = sum_{S subset Lambda_8}
      (-1)^(8-|S|) Theta_{w,S}^proj(d,h,k;t).
```

The exact signed expansion from Module 263 is:

```text
NeutralSigned_major^P
  = Kbar_P Omega_w^gen + CollSigned_263.
```

The absolute generic-defect decomposition from Module 260 is:

```text
Omega_w^proj = Omega_w^gen + Delta_w^coll,

CollNeutral_260(P_adm):
  (1/D) sum_d E_{h,k,t}|W_M(t)|
    |Delta_w^coll(d,h,k;t)|=o_W(1).
```

The distinction between `CollSigned_263=o_W(1)` and `CollNeutral_260` is
structural:

```text
CollNeutral_260 is absolute.
CollSigned_263 is signed.
Neither implies the other in the direction needed for absolute rows.
```

## 4. Assumptions

### A. Exact convention rows

Both routes require:

```text
ModelConv_260(P_adm),
ModelCutNeutral_260(P_adm),
UniformityLedger_266(P_adm).
```

These rows keep fixed:

```text
Omega_w^proj,
P_M,
W_M,
D<|d|<=2D,
selector class,
cutoff convention,
W-residue convention,
fixed-w then N -> infinity then w -> infinity order.
```

If any of these change, the result is not local/model-side until a named
transfer row returns the estimate to the target family.

### B. Absolute package

Define:

```text
AbsPMNGate_267(P_adm)
```

as:

```text
ModelConv_260(P_adm)
+ GenericTail_260(w)
+ KernelAbsBudget_265(P_adm)
+ AbsCollStrataGate_264(P_adm)
+ UniformityLedger_266(P_adm)
+ ModelCutNeutral_260(P_adm).
```

This package includes the absolute costs:

```text
A_W(M)eps_gen(w)=o_W(1),
StructAbs_264=o_W(1),
E_abs B_w^red 1_G=o_W(1),
E_abs exp(C B_w^red)B_w^red 1_{B_w^red>1}1_G=o_W(1),
TailExp_265=o_W(1),
RangeExp_265=o_W(1),
all over P_adm.
```

It is the only route in this module that can supply the literal absolute
collision row:

```text
CollNeutral_260(P_adm).
```

### C. Signed exact-model package

Define:

```text
SignedExactNeutralGate_267(P_adm)
```

as:

```text
ModelConv_260(P_adm)
+ SignedSubsetExpansion_263(P_adm)
+ KernelSignedBudget_265(P_adm)
+ SignedCoverGate_264(P_adm)
+ UniformityLedger_266(P_adm)
+ ModelCutNeutral_260(P_adm).
```

This package includes the signed costs:

```text
GenSigned_265=o_W(1),
StructSigned_264=o_W(1),
proper-support signed compatibility,
full-cover signed cluster estimate,
signed tail and signed range rows,
all in the exact same W_M-weighted average.
```

The signed route is allowed only before absolute values are inserted. It may
conclude:

```text
NeutralSigned_major^P=o_W(1),
NeutralErr_major^P=|NeutralSigned_major^P|=o_W(1).
```

It may not conclude:

```text
CollNeutral_260(P_adm),
AbsCollStrataGate_264(P_adm),
KernelAbsBudget_265(P_adm),
or any |W_M|-weighted boundary row.
```

### D. Forbidden shortcut exclusions

Neither package may be supplied by assuming:

```text
ProjectedMajorTarget_3^B,
WProjectedLocalMatch_3^major,
ProjectedModelNeutrality_3^major,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
or AU^3.
```

Neither package may be supplied by ordinary:

```text
pair-BDH,
rectangle-BDH,
first-moment Hardy-Littlewood,
generic finite-complexity Hardy-Littlewood,
single-prime CRT estimates,
or codimension counting without kernel and local-factor budgets.
```

## 5. Proof / disproof / reduction

### A. Absolute route

Assume `AbsPMNGate_267(P_adm)`.

By Module 265:

```text
KernelAbsBudget_265(P_adm)
  => KernelAbsNeutral_260(P_adm)
```

in the form:

```text
|GenSigned_265|
  <= A_W(M)eps_gen(w)
  = o_W(1).
```

By Module 264:

```text
AbsCollStrataGate_264(P_adm)
  => CollNeutral_260(P_adm).
```

Together with `ModelConv_260`, `ModelCutNeutral_260`, and
`UniformityLedger_266`, the rows of Module 260 are supplied in the same
admissible family:

```text
ProjectedModelNeutralityGate_260(P_adm)
  =
  ModelConv_260
  + GenericTail_260
  + KernelAbsNeutral_260
  + CollNeutral_260
  + DenWProjNeutral_260
  + ModelCutNeutral_260.
```

Therefore:

```text
ProjectedModelNeutralityGate_260(P_adm)
  => NeutralErr_major^P=o_W(1) over P_adm.
```

This gives only the conditional implication:

```text
AbsPMNGate_267(P_adm)
  => ProjectedModelNeutrality_3^major(P_adm).
```

The package `AbsPMNGate_267(P_adm)` itself remains open.

### B. Signed exact-model route

Assume `SignedExactNeutralGate_267(P_adm)`.

From Module 263:

```text
NeutralSigned_major^P
  = Kbar_P Omega_w^gen + CollSigned_263.
```

By `KernelSignedBudget_265(P_adm)`:

```text
GenSigned_265=Kbar_P Omega_w^gen=o_W(1)
```

in the exact same signed `W_M` average.

By `SignedCoverGate_264(P_adm)`:

```text
CollSigned_263=o_W(1)
```

over the same admissible family.

By `UniformityLedger_266(P_adm)`, both estimates use the same projection,
cutoff, denominator family, W-residue convention, selector class, dyadic
shell, and two-stage W-limit. Hence:

```text
NeutralSigned_major^P=o_W(1).
```

Since the model convention row fixes:

```text
NeutralErr_major^P=|NeutralSigned_major^P|,
```

this gives:

```text
NeutralErr_major^P=o_W(1) over P_adm.
```

This gives only the conditional implication:

```text
SignedExactNeutralGate_267(P_adm)
  => ExactModelNeutral_260(P_adm)
  => ProjectedModelNeutrality_3^major(P_adm).
```

It does not prove:

```text
CollNeutral_260(P_adm).
```

Thus, if `ProjectedModelNeutralityGate_260(P_adm)` is read literally as a
gate containing the absolute row `CollNeutral_260`, the signed route is not a
proof of that literal gate. It is a sibling direct route to the same
model-neutrality target.

### C. Classification

The verdict is:

```text
local/model-side
```

only if either `AbsPMNGate_267` or `SignedExactNeutralGate_267` is supplied
in the exact model, projection, cutoff, selector, W-residue, denominator, and
dyadic family.

The verdict is:

```text
mixed
```

if any row is obtained after changing:

```text
projection smoothing,
denominator range,
cyclic versus interval domain,
kernel truncation,
cutoff convention,
W-residue convention,
selector class,
or dyadic shell,
```

and then returning through a named transfer row.

The verdict is:

```text
endpoint-strength
```

if any missing row is supplied by assuming:

```text
ProjectedMajorTarget_3^B,
WProjectedLocalMatch_3^major,
ProjectedModelNeutrality_3^major,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
or actual sharp moving-selector transfer with no transfer proof.
```

The verdict is:

```text
false / blocked as a shortcut
```

if the route asserts projected model neutrality from:

```text
ordinary pair-BDH,
ordinary rectangle-BDH,
first-moment Hardy-Littlewood,
generic finite-complexity Hardy-Littlewood,
single-prime CRT estimates in place of finite-prime-set overflow control,
codimension-one counting without local-factor and kernel budgets,
Kbar_P=0 after boundary or denominator restrictions,
or signed cancellation after an absolute value has been inserted.
```

### D. Final Phase H verdict

The Phase H model-neutrality branch survives only as a conditional route. It
has not produced an analytic estimate.

The honest summary is:

```text
absolute fork:
  viable conditional route to the literal ProjectedModelNeutralityGate_260,
  but all absolute kernel, collision, overflow, range, cutoff, and uniformity
  rows remain open.

signed fork:
  viable conditional route only as SignedExactNeutralGate_267,
  not as a proof of CollNeutral_260 or any absolute row.

shortcut routes:
  blocked.
```

Therefore the next project action should not be to claim model neutrality.
It should be the ninth plan update, deciding whether to:

```text
continue with projected-major matching only after preserving the Phase H
  conditional status,
return to minor-arc transverse incidence,
or isolate a smaller boundary/projection transfer slice.
```

## 6. Edge cases

- If `SignedCoverGate_264` is used to claim `CollNeutral_260`, the signed and
  absolute rows have been merged incorrectly.
- If `KernelSignedBudget_265` uses a cyclic identity such as `Kbar_P=0` after
  interval cutoff, denominator restriction, or W-residue restriction, a
  zero-mode/domain row is missing.
- If `KernelAbsBudget_265` assumes bounded `A_W(M)` for a sharp projection,
  the absolute route is incomplete.
- If collision estimates omit projected diagonal forms `S_0`, `R_0`, or their
  `+d` and `-d` shifts, the collision geometry is incomplete.
- If a proof uses a smoothed projection and returns to a sharp projection
  without `ProjBd_major`, the result is mixed, not local.
- If a theorem is established only for `P_good subset P_adm`, it cannot be
  used over `P_adm` without `BadFamErr_266=o_W(1)`.
- If first-order terms of size `sum_{w<p<=B}1/p` are called generic tails,
  the W-tail bookkeeping is wrong.
- If finite-prime-set CRT overflow is replaced by single-prime estimates,
  the exponential collision expansion is untreated.
- If selector transfer is assumed rather than supplied, the route leaves model
  neutrality and enters the selector-transfer branch.

## 7. Where it fits in the project map

The Phase H chain is now:

```text
Module 260:
  ProjectedModelNeutralityGate_260(P_adm).

Module 263:
  SignedSubsetExpansion_263(P_adm).

Module 264:
  CollStrataAudit_264(P_adm).

Module 265:
  KernelBudgetAudit_265(P_adm).

Module 266:
  UniformityLedger_266(P_adm).

Module 267:
  ProjectedModelNeutralityVerdict_267(P_adm).
```

The outcome is not closure. It is a cleaner fork map:

```text
literal Module 260 gate:
  absolute route only, unless CollNeutral_260 is separately supplied;

direct signed target route:
  same-family signed exact-model neutrality, not an absolute gate.
```

The next scheduled module is:

```text
Module 268:
  ninth plan update.
```

That update should decide the next window after Phase H's verdict.

## 8. What remains open

This module does not prove:

- `AbsPMNGate_267(P_adm)`;
- `SignedExactNeutralGate_267(P_adm)`;
- `ProjectedModelNeutralityGate_260(P_adm)`;
- `ExactModelNeutral_260(P_adm)`;
- `ProjectedModelNeutrality_3^major(P_adm)`;
- `NeutralErr_major^P=o_W(1)`;
- `GenericTail_260`;
- `KernelAbsBudget_265(P_adm)`;
- `KernelSignedBudget_265(P_adm)`;
- `AbsCollStrataGate_264(P_adm)`;
- `SignedCoverGate_264(P_adm)`;
- `UniformityLedger_266(P_adm)`;
- `CollNeutral_260(P_adm)`;
- `CollSigned_263=o_W(1)`;
- `WProjectedLocalMatch_3^major`;
- `ProjectedMajorTarget_3^B`;
- `NarrowMinorArc_3^B`;
- `MinorArcTransfer_3^B`;
- `CycIntTransfer_3^major`;
- `MajorSelectorTransfer_3^P`;
- `ResCube_3^sharp`;
- `RBDH_pair_short`;
- `CPC_3^sharp`;
- `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not call the signed route a proof of `CollNeutral_260`.
- Do not export signed cancellation to `|W_M|` rows.
- Do not cite `ProjectedModelNeutralityVerdict_267` as a proof of projected
  model neutrality; it is a conditional verdict.
- Do not replace `Omega_w^proj` by the full eight-form layer, a pair face, a
  rectangle face, or an unprojected model.
- Do not replace `Sigma_w(d,h)` pointwise by `kappa_w(d)^2`.
- Do not use ordinary pair-BDH, rectangle-BDH, first-moment Hardy-Littlewood,
  or generic finite-complexity Hardy-Littlewood as a substitute for the
  signed or absolute Phase H rows.
- Do not replace the two-stage W-limit by a diagonal `w=w(N)` estimate.
- Do not change projection, denominator range, cutoff, selector, W-residue
  convention, dyadic shell, or cyclic/interval model without a named transfer
  row.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, `ResCube_3^sharp`, `CPC_3^sharp`,
  `RBDH_pair_short`, or `AU^3` is proved.
