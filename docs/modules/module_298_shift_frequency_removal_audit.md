# Module 298: Shift/frequency removal audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

This module performs the removal-budget audit selected by Module 297.

Define:

```text
ShiftFreqRemovalAudit_298(P_minor^0).
```

The audit separates two different facts:

```text
1. Actual bad-shift and persistent-frequency sets can be made empty by a
   vacuous admissible threshold schedule inside P_minor^0.

2. That vacuous schedule does not close ThresholdBudgetP0Closure_284(q,r),
   because the same large thresholds destroy the row/column shell budgets.
```

Verdict:

```text
ShiftFreqRemovalAudit_298(P_minor^0):
  STRUCTURAL / EXTRACTION.

VacuousActualRemovalP0_298:
  PROVEN inside P_minor^0 as an existence-of-schedule statement.

VacuousRemovalAsThresholdClosure_298:
  FALSE / BLOCKED.

ShiftRemovalBudget_284(q):
  OPEN as a useful moment-budget row.

FreqRemovalBudget_284(r):
  OPEN as a useful moment-budget row.

ThresholdCompatibleRemovalSchedule_298:
  OPEN.
```

This module does not prove threshold closure.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The module contains a local proof that one vacuous schedule removes all bad
shift and bad frequency sets. The module status remains structural because
that schedule is not a usable threshold closure, and the real moment-budget
rows remain open.

## 3. Definitions and variables

Work inside the Module 278 family:

```text
P_minor^0.
```

Use:

```text
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
W=W(w),
G_N=Z/NZ,
D<|d|<=2D,
N^{delta_D}<=D<=N^{1-delta_D},
2D<=N/16.
```

Let:

```text
S_D=# { d:D<|d|<=2D },
C_D=S_D/D.
```

Use the residual coefficients:

```text
f_0(n)=nu_0(n)-1,
B_d^0(n)=f_0(n+d)conj(f_0(n)),
beta_0(d,xi)=widehat{B_d^0}(xi).
```

For `lambda in Lambda_0`, define:

```text
Spec_{d,0}^minor(lambda)
  =
  { xi in Minor_0(R,eta):
      |beta_0(d,xi)|>=lambda },

E_{d,0}(lambda)
  =
  sum_{xi in Spec_{d,0}^minor(lambda)}
    |beta_0(d,xi)|^2,

N_{xi,0}(lambda)
  =
  # { d:D<|d|<=2D,
      xi in Spec_{d,0}^minor(lambda) }.
```

The bad sets are:

```text
BadShift_0(lambda)
  =
  { d:E_{d,0}(lambda)>mu_0(lambda) },

BadFreq_0(lambda)
  =
  { xi in Minor_0(R,eta):
      N_{xi,0}(lambda)>K_0(lambda) }.
```

The moment-budget rows from Module 284 are:

```text
ShiftRemovalBudget_284(q)
  =
  sum_{lambda in Lambda_0}
    lambda^2 mu_0(lambda)^(1-q)
    ShiftMomentP0_284(q;lambda),

ShiftMomentP0_284(q;lambda)
  =
  D^(-1) sum_{D<|d|<=2D} E_{d,0}(lambda)^q,

FreqRemovalBudget_284(r)
  =
  sum_{lambda in Lambda_0}
    lambda^2 (A_N^0)^2 K_0(lambda)^(1-r)
    MultMomentP0_284(r;lambda),

MultMomentP0_284(r;lambda)
  =
  D^(-1) sum_{xi in Minor_0(R,eta)} N_{xi,0}(lambda)^r.
```

## 4. Assumptions

This module assumes Modules 278, 284, and 297, plus the active status ledger.

It uses the Module 297 pointwise/Parseval bounds only inside `P_minor^0`.

It does not assume:

```text
ThresholdCompatibleRemovalSchedule_298,
ShiftRemovalBudget_284(q)=o_W(1),
FreqRemovalBudget_284(r)=o_W(1),
RowShellBudget_284,
ColumnShellBudget_284,
SigmaColumnShellBudget_284,
ThresholdBudgetP0Closure_284(q,r),
SideRowsP0Ready_283,
SidePkg_291,
SidePkgReady_293,
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
PhaseKernelBound_273,
TransverseGateProofPkg_276,
TransIncBound_269,
MinorArcTransfer_3^B,
NarrowMinorArc_3^B,
selector transfer,
ProjectedModelNeutrality_3^major,
WProjectedLocalMatch_3^major,
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the original selected-average problem,
the all-alpha theorem,
or the unconditional finite-type theorem.
```

## 5. Audit

### A. Local row and multiplicity caps

Module 297 proved the pointwise logarithmic envelope. With:

```text
L_{N,w}=1+log(WN+b),
```

it gives:

```text
|beta_0(d,xi)|<=L_{N,w}^2
```

and, by Parseval:

```text
E_{d,0}(lambda)
  <=
  sum_{xi in widehat{G_N}} |beta_0(d,xi)|^2
  <=
  L_{N,w}^4
```

for every `d` and every `lambda`.

Also:

```text
N_{xi,0}(lambda)<=S_D
```

for every `xi` and every `lambda`, by definition.

### B. A vacuous admissible removal schedule

Define:

```text
mu_vac(lambda)=L_{N,w}^4,
K_vac(lambda)=S_D.
```

This is admissible for the local family:

```text
mu_vac(lambda)>0,
K_vac(lambda) in {1,2,...,S_D}.
```

With this schedule:

```text
E_{d,0}(lambda)<=mu_vac(lambda)
```

for all shifts, and:

```text
N_{xi,0}(lambda)<=K_vac(lambda)
```

for all minor frequencies.

The bad sets use strict inequalities. Therefore:

```text
BadShift_0(lambda)=emptyset,
BadFreq_0(lambda)=emptyset
```

for every `lambda in Lambda_0`.

Classification:

```text
VacuousActualRemovalP0_298:
  PROVEN inside P_minor^0 as an existence-of-schedule statement.
```

This is a genuine local bookkeeping fact, but it is not yet useful for the
threshold package.

### C. Why the vacuous schedule is not threshold closure

The same thresholds enter the transverse row/column shell budgets.

For the row shell budget:

```text
RowShellBudget_284
  =
  sum_{lambda_j in Lambda_0}
    lambda_j^2 L_j C_D mu_0(lambda_j).
```

With `mu_0=mu_vac`, the available deterministic bound is of size:

```text
sum_j lambda_j^2 L_j C_D L_{N,w}^4.
```

Since:

```text
sum_j lambda_j^2 L_j
```

is at best a logarithmically weighted multiple of `(A_N^0)^2`, and
`A_N^0` is only bounded by `L_{N,w}^2`, this expression is not forced to be
`o_W(1)` by the definitions.

For the column budgets, the vacuous frequency threshold:

```text
K_0(lambda)=S_D
```

is also the largest possible threshold. It removes all bad frequencies, but
it enlarges:

```text
ColumnShellBudget_284,
SigmaColumnShellBudget_284.
```

Thus:

```text
VacuousRemovalAsThresholdClosure_298:
  FALSE / BLOCKED.
```

The schedule proves that removals can be made empty. It does not prove that
the remaining transverse shell is small.

### D. Moment-budget route remains open

Module 284 did not ask merely for empty bad sets. It isolated a useful
threshold closure in terms of:

```text
ShiftRemovalBudget_284(q),
FreqRemovalBudget_284(r),
RowShellBudget_284,
ColumnShellBudget_284,
SigmaColumnShellBudget_284.
```

Those rows must be small for one compatible schedule.

The present module supplies no new nontrivial estimates for:

```text
ShiftMomentP0_284(q;lambda),
MultMomentP0_284(r;lambda).
```

Trivial pointwise and Parseval bounds reproduce the same threshold tension:

```text
large mu_0, K_0:
  removals shrink;

small mu_0, K_0:
  row/column shell ceilings shrink.
```

No current tool in the ledger proves both sides of this tension for the same
schedule.

Classification:

```text
ShiftRemovalBudget_284(q):
  OPEN as a useful moment-budget row.

FreqRemovalBudget_284(r):
  OPEN as a useful moment-budget row.

ThresholdCompatibleRemovalSchedule_298:
  OPEN.
```

### E. What this changes after Module 297

Before Module 297, the threshold package still had an unresolved low-level
tail. That local fourth-moment low-level tail is now closed inside
`P_minor^0`.

After this module, the remaining threshold side package is better described
as:

```text
ThresholdBudgetP0Closure_284(q,r)
  =
  local low-level tail already handled by Module 297
  + shift/frequency moment-budget rows
  + row/column/shell transverse budgets
  + W/dyadic compatibility rows.
```

The next obstruction is the compatibility of removal thresholds with
row/column shell budgets, not the existence of a vacuous removal schedule.

## 6. Edge cases

If:

```text
Lambda_0=emptyset,
```

then every removal row is empty for that tuple. This is degenerate and does
not prove a uniform threshold theorem.

The proof that the bad sets are empty uses the strict definitions:

```text
E_{d,0}(lambda)>mu_0(lambda),
N_{xi,0}(lambda)>K_0(lambda).
```

If a future module changes these to non-strict inequalities, the vacuous
thresholds must be increased slightly.

The vacuous `K_vac` uses the maximal allowed integer value `S_D`. It is
admissible but maximally unfavorable for column shell ceilings.

The vacuous `mu_vac` depends on the local W-cyclic logarithmic envelope. It
does not transfer to the actual sharp moving selector or to a different
weight model.

## 7. Project-map location

The local side-package status after Module 298 is:

```text
Low-level fourth-moment tail:
  closed locally inside P_minor^0 by Module 297.

Actual bad-shift/frequency sets:
  can be made empty by a vacuous admissible schedule.

Useful threshold-compatible removal:
  still open.

ThresholdBudgetP0Closure_284(q,r):
  still open.
```

This is progress in status discipline, not an endpoint estimate.

## 8. What remains open

Still open:

```text
ThresholdCompatibleRemovalSchedule_298,
ShiftRemovalBudget_284(q)=o_W(1),
FreqRemovalBudget_284(r)=o_W(1),
RowShellBudget_284=o_W(1),
ColumnShellBudget_284=o_W(1),
SigmaColumnShellBudget_284=o_W(1),
ThresholdBudgetP0Closure_284(q,r),
SideRowsP0Ready_283,
SidePkg_291,
SidePkgReady_293,
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the original selected-average problem.
```

## 9. Forbidden upgrades

Do not treat:

```text
BadShift_0(lambda)=BadFreq_0(lambda)=emptyset
```

under the vacuous schedule as threshold closure. It is not.

Do not cite this module as proving:

```text
ShiftRemovalBudget_284(q)=o_W(1),
FreqRemovalBudget_284(r)=o_W(1),
ThresholdBudgetP0Closure_284(q,r),
SidePkg_291,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
or any endpoint object.
```

Do not transfer the local W-cyclic removal schedule to the actual sharp
moving selector without a named transfer theorem.

## 10. Next target

The next target should test the threshold-window compatibility left by this
audit:

```text
Module 299:
  ThresholdWindowCompatibilityAudit_299(P_minor^0).
```

That module should ask whether there is any non-vacuous threshold schedule
that can make the removal budgets and at least one row/column/shell transverse
budget small at the same time, using only same-family non-endpoint inputs.
