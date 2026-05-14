# Module 265: Kernel absolute budget versus signed kernel cancellation

## 1. Precise theorem / claim being advanced

This module performs the third proof-or-blocked test required by
`PlanChallenge_5_262`: decide what the Phase H model-neutrality branch needs
from the projected kernel.

Define:

```text
KernelBudgetAudit_265(P_adm).
```

The audit separates two routes:

```text
KernelAbsBudget_265(P_adm):
  pay every generic, structural, congruence-load, overflow, tail, and range
  term after replacing W_M by |W_M|;

KernelSignedBudget_265(P_adm):
  prove a same-family signed cancellation theorem for the exact W_M-weighted
  model-neutrality average.
```

The conditional claims are:

```text
KernelAbsBudget_265(P_adm) + AbsCollStrataGate_264(P_adm)
  => the absolute-kernel side of ProjectedModelNeutralityGate_260(P_adm),

KernelSignedBudget_265(P_adm) + SignedCoverGate_264(P_adm)
  => NeutralSigned_major^P=o_W(1) over P_adm.
```

The second route is signed only. It does not imply `CollNeutral_260`, any
absolute boundary row, or projected local-model matching.

This module does not prove either kernel budget.

## 2. Status label

`CONDITIONAL`

The module gives conditional reductions and classifications. It does not prove
bounded kernel absolute mass, signed kernel cancellation, projected model
neutrality, or any endpoint object.

## 3. Definitions and variables

Use:

```text
rho=(D,R,eta,P_M,H,K,T,selector,cutoff) in P_adm(N,w),
D<|d|<=2D,
w fixed, N -> infinity, then w -> infinity.
```

The projected major-arc kernel is:

```text
P_M F(x)=E_t K_M(t)F(x-t),
K_M(t)=sum_xi m_M(xi)e(xi t),
m_M(0)=0.
```

The four-kernel signed weight is:

```text
W_M(t0,t1,t2,t3)
  = K_M(t0)conj(K_M(t1))conj(K_M(t2))K_M(t3).
```

Define:

```text
A_1(M)=E_t |K_M(t)|,
A_W(M)=E_{t0,t1,t2,t3}|W_M(t0,t1,t2,t3)|.
```

When the four `t_i` averages are independent with the same normalization:

```text
A_W(M)=A_1(M)^4.
```

For a truncation scale `T`, define:

```text
tau_M(T)=E_{|t|>T}|K_M(t)|,
Tail_W(T)=E_t |W_M(t)| 1_{max_i |t_i|>T}.
```

The standard union bound gives:

```text
Tail_W(T) <= 4 A_1(M)^3 tau_M(T).
```

The generic W-tail saving from Module 260 is:

```text
|Omega_w^gen| <= eps_gen(w),
eps_gen(w)->0.
```

The signed generic term is:

```text
GenSigned_265
  = (1/D) sum_{D<|d|<=2D}
      E_{h,k,t} W_M(t) Omega_w^gen.
```

Because `Omega_w^gen` is independent of `(d,h,k,t)`, this is:

```text
GenSigned_265 = Kbar_P Omega_w^gen,
```

where:

```text
Kbar_P=(1/D) sum_{D<|d|<=2D}E_{h,k,t}W_M(t).
```

The absolute generic bound is:

```text
|GenSigned_265| <= A_W(M) eps_gen(w).
```

From Module 264, the absolute collision-load expectations use:

```text
E_abs F
  = (1/D) sum_{D<|d|<=2D} E_{h,k,t} |W_M(t)| F(d,h,k;t).
```

The active absolute collision budget terms are:

```text
StructAbs_264,
E_abs B_w^red 1_G,
E_abs exp(C B_w^red) B_w^red 1_{B_w^red>1}1_G,
E_abs tau_w 1_G.
```

The active signed collision terms are:

```text
StructSigned_264,
SignedCoverGate_264 full-cover clusters,
signed generic-tail and domain-error rows.
```

## 4. Absolute kernel budget

Define:

```text
KernelAbsBudget_265(P_adm)
```

as the conjunction of the following rows, all in the same admissible family.

### A. Same projection and normalization

No row may change:

```text
P_M,
K_M,
W_M,
D<|d|<=2D,
H,K,T,
R,eta,
selector class,
cutoff convention,
W-residue convention,
fixed-w then N -> infinity then w -> infinity order.
```

If replacing a sharp `P_M` by a smoothed projection is necessary to obtain
kernel bounds, the result is mixed and needs a projection-transfer row.

### B. Absolute generic tail

The generic W-tail must survive the absolute kernel mass:

```text
GenAbsBudget_265(P_adm):
  A_W(M) eps_gen(w)=o_W(1).
```

With the common generic estimate:

```text
eps_gen(w) <= C_gen G_2(w),
G_2(w)=sum_{p>w}1/p^2,
```

this becomes:

```text
A_W(M)G_2(w)=o_W(1).
```

Bounded `A_W(M)` is sufficient but not required. If `A_W(M)` grows, the
displayed product is the real budget.

### C. Absolute structural strata

The structural contribution must be controlled after the local singular
factors and the full absolute kernel weight are present:

```text
StructAbs_264=o_W(1).
```

A codimension-one count of the set `Z_struct` gives only a geometric factor.
It must be multiplied by the relevant kernel mass and by a bound or
lower-dimensional model for the local factor on the stratum.

### D. Absolute first collision-load moment

The reduced nonstructural load must satisfy:

```text
E_abs B_w^red 1_G=o_W(1).
```

This is not an ordinary first-moment HL row. It is a kernel-weighted divisor
average over the projected forms:

```text
d,
A,
A+d,
A-d,
A in {H_0,K_0,S_0,R_0,K_1,H_1},
```

after structural zero strata and boundary defects have been removed.

### E. Absolute overflow

The exponential local-factor envelope requires:

```text
E_abs exp(C B_w^red) B_w^red
  1_{B_w^red>1}1_G=o_W(1).
```

First-moment control alone does not imply this row. It requires the
exponential-integrability or high-moment infrastructure of Modules 188-190.

### F. Kernel tails and range errors

The kernel tail and finite-range CRT errors must be summable inside the same
exponential expansion:

```text
TailExp_265(lambda,T)=o_W(1),
RangeExp_265(lambda)=o_W(1),
```

for the relevant `lambda=C+epsilon` from the overflow route.

These rows include the absolute kernel factor. They cannot use cancellation
from `W_M`.

## 5. Absolute implication

Assume:

```text
KernelAbsBudget_265(P_adm)
+ AbsCollStrataGate_264(P_adm).
```

The generic term satisfies:

```text
|GenSigned_265|
  <= A_W(M) eps_gen(w)
  = o_W(1).
```

The collision term satisfies `CollNeutral_260(P_adm)` by Module 264:

```text
AbsCollStrataGate_264(P_adm)
  => CollNeutral_260(P_adm).
```

Thus the generic and absolute collision rows needed by the absolute side of
Module 260 are supplied, with all kernel costs paid explicitly. This
establishes only:

```text
KernelAbsBudget_265 + AbsCollStrataGate_264
  => GenericTail_260 + KernelAbsNeutral_260 + CollNeutral_260
```

inside the same `P_adm` family.

It does not prove `DenWProjNeutral_260`, `ModelCutNeutral_260`, or projected
model neutrality.

## 6. Signed kernel budget

Define:

```text
KernelSignedBudget_265(P_adm)
```

as the conjunction of signed rows in the exact same family:

```text
1. Same W_M, not |W_M|, throughout the signed average.

2. Generic signed row:
   GenSigned_265=o_W(1).

3. Structural signed row:
   StructSigned_264=o_W(1), or synchronized exact lower-dimensional signed
   models on every structural stratum.

4. Proper-support signed filter:
   the Boolean cancellation from Module 264 is compatible with the actual
   kernel, cutoff, denominator range, and generic-tail remainders.

5. Full-cover signed clusters:
   the signed average of collision clusters touching all eight labels is
   o_W(1).

6. Signed tail and signed range rows:
   kernel truncation, finite-range CRT errors, and W-limit tails are handled
   without changing the projection or selector.
```

The generic signed row may be supplied in two ways:

```text
Kbar_P=0 exactly in a cyclic independent-kernel model,
```

or:

```text
|Kbar_P Omega_w^gen|=o_W(1)
```

after all cutoff, boundary, denominator, and normalization defects have been
paid.

The first option is fragile. If interval cutoffs, restricted denominator
ranges, W-residue restrictions, or non-cyclic averages are present, the exact
identity `Kbar_P=0` becomes a side row rather than a free zero.

## 7. Signed implication

Assume:

```text
KernelSignedBudget_265(P_adm)
+ SignedCoverGate_264(P_adm).
```

The generic part is:

```text
GenSigned_265=o_W(1).
```

The signed collision part is:

```text
CollSigned_263=o_W(1)
```

by the signed route of Module 264. Therefore:

```text
NeutralSigned_major^P
  = GenSigned_265 + CollSigned_263
  = o_W(1).
```

This gives:

```text
NeutralErr_major^P=o_W(1)
```

for the signed model-neutrality average only if all convention and uniformity
rows match the target `NeutralErr_major^P`.

This route is not `CollNeutral_260`. It cannot be exported to:

```text
absolute boundary rows,
|W_M|-weighted fixed rows,
BoundaryModelMass_225,
AbsCollStrataGate_264,
or projected local-model matching.
```

## 8. Classification of kernel routes

The absolute route is:

```text
local/model-side
```

only if every row in `KernelAbsBudget_265` and
`AbsCollStrataGate_264` is supplied for the same projection, domain, selector,
and W-limit order.

It is:

```text
mixed
```

if bounded kernel mass or tail control is obtained after smoothing the
projection, changing denominator ranges, changing cutoffs, or changing the
selector class.

It is:

```text
endpoint-strength
```

if the required absolute estimates are supplied by assuming
`ProjectedMajorTarget_3^B`, `WProjectedLocalMatch_3^major`,
`ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`.

It is:

```text
false / blocked as a shortcut
```

if it is asserted from ordinary pair-BDH, rectangle-BDH, first-moment HL,
generic finite-complexity HL, or codimension counting without kernel and local
factor budgets.

The signed route is:

```text
local/model-side
```

only if the signed cancellation is established for the exact `W_M` and the
exact model average.

It is:

```text
mixed
```

if it needs cyclic-to-interval, projection, denominator, cutoff, or selector
transfer.

It is:

```text
endpoint-strength
```

if the full-cover signed cluster estimate is essentially the residual
endpoint or projected major target in disguise.

It is:

```text
false / blocked as a shortcut
```

if it is imported from Phase G boundary rows or any row that already took
absolute values.

## 9. Verdict for Phase H

The Phase H kernel branch remains viable only as a fork:

```text
Absolute fork:
  prove KernelAbsBudget_265 and AbsCollStrataGate_264.

Signed fork:
  prove KernelSignedBudget_265 and SignedCoverGate_264,
  while accepting that this does not prove absolute rows.
```

The absolute fork is safer logically but likely expensive. It must pay:

```text
A_W(M) eps_gen(w),
StructAbs_264,
E_abs B_w^red,
E_abs exp(C B_w^red) B_w^red 1_{B_w^red>1},
TailExp_265,
RangeExp_265.
```

The signed fork is potentially smaller but dangerous. It must not become a
renaming of projected major-arc cancellation.

The next module should audit whether the needed rows are uniform in:

```text
w,
D,R,eta,
denominator and CRT ranges,
projection boundary,
cutoff,
dyadic shell,
P_adm.
```

## 10. Edge cases

- If `A_W(M)` is unbounded, every claimed saving must be restated with the
  explicit factor `A_W(M)`.
- If the proof uses a smoothed kernel, the result is for the smoothed
  projection unless a projection-transfer row is supplied.
- If the exact cyclic identity `Kbar_P=0` is used after interval cutoff or
  denominator restriction, a zero-mode/domain-defect row is missing.
- If a signed row is converted into an absolute row, the argument is invalid.
- If a boundary row uses `|W_M|`, it cannot supply signed cancellation in
  `W_M`.
- If a signed full-cover cluster estimate is just the projected major target,
  the route is circular.
- If first-moment divisor control is used for overflow, the large-load region
  is untreated.
- If kernel tails are controlled without the residual product or collision
  load in the tail, the tail estimate is incomplete.
- If range errors are summed prime-by-prime but not over finite prime sets,
  the exponential moment is unsupported.

## 11. Where it fits in the project map

The Phase H chain is now:

```text
Module 260:
  ProjectedModelNeutralityGate_260(P_adm) names absolute or signed kernel rows.

Module 263:
  SignedSubsetExpansion_263(P_adm) isolates GenSigned_265 and CollSigned_263.

Module 264:
  CollStrataAudit_264(P_adm) splits collision control into absolute and
  signed routes.

Module 265:
  KernelBudgetAudit_265(P_adm) tests whether the kernel costs can be paid
  absolutely or only by a signed theorem.
```

The next module should be:

```text
Module 266:
  W-limit, denominator, CRT range, projection-boundary, and dyadic uniformity
  over P_adm.
```

## 12. What remains open

This module does not prove:

- `KernelAbsBudget_265(P_adm)`;
- `KernelSignedBudget_265(P_adm)`;
- `KernelAbsNeutral_260`;
- `KernelSignedNeutral_260`;
- `AbsCollStrataGate_264(P_adm)`;
- `SignedCoverGate_264(P_adm)`;
- `CollNeutral_260`;
- `CollSigned_263=o_W(1)`;
- `NeutralErr_major^P=o_W(1)`;
- `ProjectedModelNeutralityGate_260(P_adm)`;
- `ProjectedModelNeutrality_3^major(P_adm)`;
- `WProjectedLocalMatch_3^major`;
- `ProjectedMajorTarget_3^B`;
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

- Do not say the kernel budget is paid merely because `m_M(0)=0`.
- Do not use signed kernel cancellation after an absolute value has been
  inserted.
- Do not import Phase G `|W_M|` boundary rows as signed cancellation.
- Do not assume `A_W(M)=O_W(1)` for a sharp projection without proof.
- Do not hide kernel-tail, range, denominator, W-limit, cutoff, or selector
  defects inside `KernelAbsNeutral_260` or `KernelSignedNeutral_260`.
- Do not replace exponential overflow control by first-moment divisor
  averages.
- Do not close the signed full-cover cluster row by assuming
  `ProjectedMajorTarget_3^B`, `WProjectedLocalMatch_3^major`,
  `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, `ResCube_3^sharp`, `CPC_3^sharp`,
  `RBDH_pair_short`, or `AU^3` is proved.
