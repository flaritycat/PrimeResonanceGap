# Module 294: Low-level budget triage inside `P_minor^0`

## 1. Precise theorem / claim being advanced

This module performs the low-level leakage triage selected by Module 293.

Define:

```text
LowLevelBudgetTriage_294(P_minor^0).
```

The claim advanced is only a classification:

```text
The contribution below lambda_min is not proved negligible by the
current Phase K ledger, and excluding it from the adaptive shell grid is
only a convention until a separate low-level budget is supplied.
```

The verdict is:

```text
LowLevelBudgetTriage_294(P_minor^0):
  STRUCTURAL / EXTRACTION.

LowLevelBudgetP0_284:
  OPEN.

LowLevelCutoffP0_283:
  OPEN.

LowLevelByDefinition_294:
  FALSE / BLOCKED.

LowLevelCountingBarrier_294:
  OPEN.
```

The useful output is a small criterion: if a future reconstruction of the
local minor-arc target uses only a fixed `a`-power contribution from the
below-`lambda_min` coefficients, then deterministic counting reduces the row
to an explicit barrier. That criterion is not a proof of the row.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module proves no low-level smallness, no threshold closure, no side
package, no adaptive-shell gain, no minor-arc theorem, and no endpoint theorem.

## 3. Definitions and variables

Work inside the Module 278 family:

```text
P_minor^0.
```

Use:

```text
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
N^{delta_D}<=D<=N^{1-delta_D},
2D<=N/16.
```

For the local residual:

```text
f_0(n)=nu_0(n)-1,
B_d^0(n)=f_0(n+d)conj(f_0(n)),
beta_0(d,xi)=widehat{B_d^0}(xi).
```

Let:

```text
A_N^0=sup_{d,xi}|beta_0(d,xi)|,
m_minor^0=#Minor_0(R,eta),
C_D=D^(-1)# { d:D<|d|<=2D },
lambda_min=A_N^0 N^{-kappa_lambda}.
```

The low-level set is:

```text
Low_0(lambda_min)
  =
  { (d,xi):
      D<|d|<=2D,
      xi in Minor_0(R,eta),
      |beta_0(d,xi)|<lambda_min }.
```

For `a>=1`, define the normalized low-level `a`-power:

```text
LowPow_a,0
  =
  D^(-1) sum_{(d,xi) in Low_0(lambda_min)}
    |beta_0(d,xi)|^a.
```

The two most visible cases are:

```text
LowMass_0=LowPow_1,0,
LowEng_0=LowPow_2,0.
```

Module 284 left the exact form of `LowLevelBudgetP0_284` open because it
depends on how a future proof reconstructs the full local minor-arc target
from the large-spectrum shells.

## 4. Assumptions

This module assumes only Modules 278-293 and the active status ledger.

It does not assume:

```text
LowLevelBudgetP0_284,
LowLevelCutoffP0_283,
LowLevelCountingBarrier_294,
ThresholdBudgetP0_283,
ThresholdBudgetP0Closure_284(q,r),
ShiftRemovalBudget_284(q),
FreqRemovalBudget_284(r),
RowShellBudget_284,
ColumnShellBudget_284,
SigmaColumnShellBudget_284,
SideRowsP0Ready_283,
SidePkg_291,
SidePkgReady_293,
DegRowsP0Small_282,
MajorDiffBound_282,
PhysDiagLocal_282,
DegFreePhaseGate_282,
ShellSelectionP0_283,
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

## 5. Proof / disproof / reduction

### A. The low-level row is outside the adaptive shell grid

The shell grid used in `Xi_273^0` begins at:

```text
lambda>=lambda_min.
```

Therefore:

```text
|beta_0(d,xi)|<lambda_min
```

is excluded from the adaptive shell functional by convention. This exclusion
does not make the contribution small in the full local minor-arc target.

Classification:

```text
LowLevelByDefinition_294:
  FALSE / BLOCKED.
```

The low-level row must be proved, absorbed into a later reconstruction, or
the local threshold package remains incomplete.

### B. Deterministic counting gives only an explicit barrier

For every `a>=1`:

```text
LowPow_a,0
  <=
  D^(-1) #Low_0(lambda_min) lambda_min^a
  <=
  C_D m_minor^0 (A_N^0)^a N^{-a kappa_lambda}.
```

Thus a purely deterministic low-level route would require the corresponding
target-weighted barrier to be `o_W(1)`. In the quadratic energy case the
visible barrier is:

```text
LowLevelCountingBarrier_294(2)
  =
  C_D m_minor^0 (A_N^0)^2 N^{-2 kappa_lambda}.
```

In a fourth-moment reconstruction the analogous barrier would be:

```text
LowLevelCountingBarrier_294(4)
  =
  C_D m_minor^0 (A_N^0)^4 N^{-4 kappa_lambda}.
```

In a linear absolute-mass reconstruction it would be:

```text
LowLevelCountingBarrier_294(1)
  =
  C_D m_minor^0 A_N^0 N^{-kappa_lambda}.
```

The active ledger has not proved that any of these target-weighted barriers
are `o_W(1)` uniformly over the declared `P_minor^0` ranges. Choosing
`lambda_min=A_N^0N^{-kappa_lambda}` supplies only the displayed power saving;
it does not control `m_minor^0`, `A_N^0`, target weights, dyadic losses,
W-limit losses, or reconstruction losses.

Classification:

```text
LowLevelCountingCriterion_294:
  STRUCTURAL / EXTRACTION.

LowLevelCountingBarrier_294:
  OPEN.
```

### C. Why the current shell tools do not close it

The current adaptive shell tools begin after the low-level set has been
removed. They can diagnose large coefficients, data-dependent shell fibers,
and threshold schedules, but they do not estimate coefficients that never
enter the shell grid.

The following shortcuts are blocked:

```text
Xi_273^0 controls the low-level part:
  FALSE / BLOCKED, because Xi_273^0 is defined over lambda>=lambda_min.

PhaseKernelBound_273^0 controls the low-level part:
  FALSE / BLOCKED, unless a future theorem explicitly includes the
  below-lambda_min reconstruction.

ThresholdBudgetP0_283 controls the low-level part by definition:
  FALSE / BLOCKED, because LowLevelBudgetP0_284 is one of the missing rows
  inside ThresholdBudgetP0Closure_284(q,r).

SidePkg_291 controls the low-level part:
  FALSE / BLOCKED, because SidePkg_291 itself remains open.
```

A total-energy theorem, if proved in the same local family and with the same
normalizations, could close this row. No such theorem is supplied by the
current ledger. Importing endpoint-strength fourth-moment, pair-BDH,
rectangle-BDH, or selector-transfer input would be circular unless those
inputs are proved independently.

### D. The row is local, but uniformity still matters

This is a local model-side row. It is not itself the actual sharp
moving-selector transfer problem.

Even so, a valid low-level estimate must be uniform in:

```text
N,w,b,D,R,eta,Lambda_0,mu_0,K_0,
both signs of d,
minor-arc boundary conventions,
Fourier normalization,
W-residue convention,
dyadic shell conventions,
and the final limiting order.
```

An estimate for one `D`, one sign, one minor-arc cut, one Fourier convention,
or one fixed `w` is not the row needed by `ThresholdBudgetP0Closure_284(q,r)`.

### E. Possible future routes

There are three honest routes left visible.

```text
Route 1: Counting closure.
  Identify the exact target power a and prove that the corresponding
  target-weighted LowLevelCountingBarrier_294(a) is o_W(1) over P_minor^0.

Route 2: Same-family energy input.
  Prove a direct low-level energy estimate for LowEng_0, or the exact
  low-level expression demanded by the future reconstruction, with all
  W-limit and dyadic uniformity rows included.

Route 3: Grid reconstruction.
  Redesign the shell grid or reconstruction so that the below-lambda_min
  part is absorbed with explicit losses, then re-check the threshold budget.
```

None of these routes is completed here.

## 6. Edge cases

If:

```text
A_N^0=0,
```

then all local coefficients vanish and the low-level contribution is zero.
This is a degenerate local case, not a uniform proof of the row.

If:

```text
m_minor^0=0,
```

then there are no local minor-arc frequencies and the row is empty. This is
also only a degenerate case.

The strict inequality:

```text
|beta_0(d,xi)|<lambda_min
```

is paired with shell inclusion at:

```text
|beta_0(d,xi)|>=lambda_min.
```

This avoids double counting on the threshold boundary.

The factor `C_D` keeps both signs of `d` and the dyadic range normalization
visible. It must not be silently replaced by an absolute constant when the
future target is sensitive to dyadic uniformity.

Fourier normalization constants must be kept with the chosen convention. A
future proof may absorb them, but only after the convention is fixed.

## 7. Project-map location

The local dependency chain is:

```text
LowLevelBudgetP0_284
  -> ThresholdBudgetP0Closure_284(q,r)
  -> SideRowsP0Ready_283 / SidePkg_291
  -> PhaseKernelBound_273^0
  -> TransverseGateProofPkg_276
  -> NarrowMinorArc_3^B
  -> ResCube_3^sharp
  -> original selected-average problem.
```

This module advances only the first arrow by clarifying what it would mean.
It does not prove any later object in the chain.

## 8. What remains open

The next proof-level information needed is:

```text
1. The exact reconstruction formula for the below-lambda_min contribution.
2. The target power a and all target weights attached to that reconstruction.
3. A proof or rejection of LowLevelCountingBarrier_294(a)=o_W(1).
4. If counting fails, a same-family low-level energy estimate.
5. Compatibility with the threshold schedule and W/dyadic uniformity rows.
```

Until then:

```text
LowLevelBudgetP0_284:
  OPEN.

LowLevelCutoffP0_283:
  OPEN.

ThresholdBudgetP0Closure_284(q,r):
  OPEN.

SidePkgReady_293:
  OPEN.
```

## 9. Forbidden upgrades

This module does not claim:

```text
LowLevelBudgetP0_284=o_W(1),
LowLevelCutoffP0_283,
ThresholdBudgetP0_283,
ThresholdBudgetP0Closure_284(q,r),
SideRowsP0Ready_283,
SidePkg_291,
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
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

Do not use an endpoint object to prove the low-level row. Do not replace the
actual sharp moving selector by the local model. Do not treat a shell-grid
definition as an analytic estimate. Do not replace `Sigma_w(d,h)` by
`kappa_w(d)^2` pointwise.

## 10. Next target

The next scheduled step should be the twelfth plan update:

```text
Module 295:
  update the long-term plan after LowLevelBudgetTriage_294, and decide
  whether the next proof attempt should test LowLevelCountingBarrier_294,
  shift/frequency removal budgets, or another smaller side row.
```

That update should preserve the status discipline above: the low-level row is
not closed, and the project should not return to a broad adaptive-shell gain
attempt without a genuinely new input.
