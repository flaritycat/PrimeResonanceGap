# Module 284: Threshold-budget feasibility inside `P_minor^0`

## 1. Precise theorem / claim being advanced

This module tests the threshold-budget row isolated in Module 283 against the
row/column ceilings, base-tail shells, low-level leakage, and lambda-summed
target inside the fixed minimal family `P_minor^0`.

Define:

```text
ThresholdBudgetP0Audit_284(P_minor^0).
```

The verdict is:

```text
The threshold budget is not proved by the current Phase J ledger.
```

More precisely, deterministic row and column ceilings give useful necessary
budget tests, but they do not produce the needed `o_W(1)` estimate unless
new moment bounds, a compatible threshold window, and low-level control are
proved in the same family.

This module deliberately does not try to prove `PhaseKernelBound_273^0`.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is a feasibility audit. It proves no threshold closure, no
`PhaseKernelBound_273^0`, no `TransIncBound_269`, and no endpoint estimate.

## 3. Definitions and variables

Work inside `P_minor^0` from Module 278:

```text
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
N^{delta_D}<=D<=N^{1-delta_D},
2D<=N/16.
```

Use:

```text
f_0(n)=nu_0(n)-1,
B_d^0(n)=f_0(n+d)conj(f_0(n)),
beta_0(d,xi)=widehat{B_d^0}(xi),
A_N^0=sup_{d,xi}|beta_0(d,xi)|,
m_minor^0=#Minor_0(R,eta),
C_D=D^(-1)# { d:D<|d|<=2D }.
```

For `lambda_j in Lambda_0`, write:

```text
E_{d,0}(lambda_j)
  =
  sum_{xi in Spec_{d,0}^minor(lambda_j)}
    |beta_0(d,xi)|^2,

N_{xi,0}(lambda_j)
  =
  # { d:D<|d|<=2D,
        xi in Spec_{d,0}^minor(lambda_j) }.
```

The transverse set is:

```text
I_trans_0(lambda_j)
  =
  { (d,xi):
      D<|d|<=2D,
      xi in Minor_0(R,eta),
      |beta_0(d,xi)|>=lambda_j,
      E_{d,0}(lambda_j)<=mu_0(lambda_j),
      N_{xi,0}(lambda_j)<=K_0(lambda_j) }.
```

For shell height `sigma=lambda_k>=lambda_j`, define:

```text
J_{j,k}
  =
  J_trans_0(lambda_j;lambda_k)
  =
  { (d,xi) in I_trans_0(lambda_j):
      lambda_k <= |beta_0(d,xi)| < 2lambda_k }.
```

Let:

```text
L_j=# { k: lambda_k in Lambda_0, k>=j },
H_j=sum_{k>=j} lambda_k^2.
```

The target shell contribution has the schematic form:

```text
sum_j lambda_j^2
  sum_{k>=j} Eng_0(J_{j,k}),
```

where:

```text
Eng_0(J)=D^(-1) sum_{(d,xi) in J}|beta_0(d,xi)|^2.
```

The low-level part below:

```text
lambda_min=A_N^0 N^{-kappa_lambda}
```

is not included in the shell sum and is tracked separately.

## 4. Assumptions

This module assumes only Modules 278-283 and the current status ledger.

It does not assume:

```text
ThresholdBudgetP0_283,
ThresholdBudgetP0Closure_284,
LowLevelCutoffP0_283,
WUniformP0_283,
DyadicUniformityP0_283,
ShellSelectionP0_283,
ShiftMomentP0_284(q),
MultMomentP0_284(r),
RowBarrierP0_284(q),
ColumnBarrierP0_284(r),
SigmaColumnBarrierP0_284(r),
SideRowsP0Ready_283,
DegRowsP0Small_282,
MajorDiffBound_282,
PhysDiagLocal_282,
DegFreePhaseGate_282,
LargeSieveBesselClosure_281,
AdaptiveBesselGain_281,
UniformFiberBound_280,
SelectionTransfer_280,
DirectShellBound_280,
PhaseKernelBound_273^0,
PhaseKernelBound_273,
TransverseGateProofPkg_276,
TransGateSideRows_274,
TransIncBound_269,
ThresholdOnlyClosure_270,
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

### A. Shell ceilings inherited from Modules 270, 273, and 281

On `J_{j,k}`, the row ceiling gives:

```text
Eng_0(J_{j,k}) <= C_D mu_0(lambda_j).
```

The Module 273 column ceiling gives:

```text
Eng_0(J_{j,k})
  <= (A_N^0)^2 K_0(lambda_j)m_minor^0/D.
```

The sharper shell-counting column ceiling from Module 281 gives:

```text
Eng_0(J_{j,k})
  <= 4 lambda_k^2 K_0(lambda_j)m_minor^0/D.
```

These are deterministic. They are valid for adaptive shells because they use
only row energy, column multiplicity, and shell height. They are not phase
cancellation.

### B. Lambda-summed row budget

Using only the row ceiling in every base-tail shell gives:

```text
RowShellBudget_284
  =
  sum_{lambda_j in Lambda_0}
    lambda_j^2 L_j C_D mu_0(lambda_j).
```

A row-ceiling-only route requires:

```text
RowShellBudget_284=o_W(1).
```

This is not proved by the definition of `mu_0`. It requires a quantitative
choice of thresholds compatible with bad-shift removal and with the final
two-stage W-limit.

### C. Lambda-summed column budgets

The Module 273 column ceiling gives the budget:

```text
ColumnShellBudget_284
  =
  sum_{lambda_j in Lambda_0}
    lambda_j^2 L_j
    (A_N^0)^2 K_0(lambda_j)m_minor^0/D.
```

The shell-counting variant gives:

```text
SigmaColumnShellBudget_284
  =
  sum_{lambda_j in Lambda_0}
    lambda_j^2
    K_0(lambda_j)m_minor^0 H_j/D.
```

A column-ceiling-only route requires at least one of:

```text
ColumnShellBudget_284=o_W(1),
SigmaColumnShellBudget_284=o_W(1).
```

Neither is proved. The second can be better on low shells because it uses
`lambda_k^2` instead of `(A_N^0)^2`, but it still needs a summable threshold
choice and uniform control over all declared parameters.

### D. Bad-shift removal budget

For `q>1`, define the local shift moment:

```text
ShiftMomentP0_284(q;lambda_j)
  =
  D^(-1) sum_{D<|d|<=2D}
    E_{d,0}(lambda_j)^q.
```

Bad-shift removal contributes:

```text
ShiftRemovalBudget_284(q)
  =
  sum_{lambda_j in Lambda_0}
    lambda_j^2
    mu_0(lambda_j)^(1-q)
    ShiftMomentP0_284(q;lambda_j).
```

This term wants `mu_0(lambda_j)` large.

The row shell budget wants the same `mu_0(lambda_j)` small. Therefore the
row threshold route is feasible only if both:

```text
ShiftRemovalBudget_284(q)=o_W(1),
RowShellBudget_284=o_W(1)
```

hold for the same threshold schedule.

No such moment estimate or threshold schedule is proved here.

### E. Persistent-frequency removal budget

For `r>1`, define:

```text
MultMomentP0_284(r;lambda_j)
  =
  D^(-1) sum_{xi in Minor_0(R,eta)}
    N_{xi,0}(lambda_j)^r.
```

Bad-frequency removal contributes:

```text
FreqRemovalBudget_284(r)
  =
  sum_{lambda_j in Lambda_0}
    lambda_j^2
    (A_N^0)^2
    K_0(lambda_j)^(1-r)
    MultMomentP0_284(r;lambda_j).
```

This term wants `K_0(lambda_j)` large.

The column budgets want the same `K_0(lambda_j)` small. Thus a column
threshold route requires the same schedule to satisfy:

```text
FreqRemovalBudget_284(r)=o_W(1)
```

and at least one of the two column shell budgets above.

No such multiplicity moment estimate is proved here.

### F. Optimized row barrier

The row-only threshold tension at a fixed `lambda_j` has the schematic form:

```text
lambda_j^2 [
  mu^(1-q) ShiftMomentP0_284(q;lambda_j)
  + L_j C_D mu
].
```

Continuous optimization gives the diagnostic barrier:

```text
RowBarrierP0_284(q)
  =
  sum_j lambda_j^2
    (L_j C_D)^((q-1)/q)
    ShiftMomentP0_284(q;lambda_j)^(1/q).
```

Up to constants depending on `q`, a row-only threshold closure cannot be
better than this barrier unless a new nontrivial estimate enters.

Classification:

```text
RowBarrierP0_284(q):
  OPEN diagnostic.
```

It is not an estimate. It is the row moment strength a future proof would
have to supply, with the base-tail shell count `L_j` paid.

### G. Optimized column barriers

Using the Module 273 column ceiling gives the diagnostic barrier:

```text
ColumnBarrierP0_284(r)
  =
  sum_j lambda_j^2
    (A_N^0)^2
    (L_j m_minor^0/D)^((r-1)/r)
    MultMomentP0_284(r;lambda_j)^(1/r).
```

Using the shell-counting column ceiling gives:

```text
SigmaColumnBarrierP0_284(r)
  =
  sum_j lambda_j^2
    ((A_N^0)^2 MultMomentP0_284(r;lambda_j))^(1/r)
    (m_minor^0 H_j/D)^((r-1)/r).
```

Classification:

```text
ColumnBarrierP0_284(r),
SigmaColumnBarrierP0_284(r):
  OPEN diagnostics.
```

The shell-counting barrier is a genuine refinement of the audit language, but
not a proof. It still needs same-family multiplicity moment input strong
enough to survive the final lambda sum and W-limit.

### H. Low-level leakage

The shell target excludes:

```text
|beta_0(d,xi)| < lambda_min.
```

A threshold-budget closure must also control:

```text
LowLevelBudgetP0_284
  =
  contribution of all minor-arc coefficients below lambda_min
  to the local transverse target.
```

The exact form depends on how the future proof reconstructs the full
minor-arc energy from the large-spectrum shells. In any case:

```text
LowLevelBudgetP0_284=o_W(1)
```

is not proved by choosing `lambda_min=A_N^0N^{-kappa_lambda}`. It is the same
local row called `LowLevelCutoffP0_283`.

### I. Candidate threshold closure package

Define the strongest threshold-only local package currently visible:

```text
ThresholdBudgetP0Closure_284(q,r)
  =
  LowLevelBudgetP0_284
  + ShiftRemovalBudget_284(q)
  + FreqRemovalBudget_284(r)
  + min(
      RowShellBudget_284,
      ColumnShellBudget_284,
      SigmaColumnShellBudget_284
    ).
```

The desired closure would be:

```text
ThresholdBudgetP0Closure_284(q,r)=o_W(1)
```

for some fixed `q,r>1`, uniformly over `P_minor^0`.

This is a conditional target only. It is not established in the active
ledger.

### J. Why this does not prove `PhaseKernelBound_273^0`

Even if the threshold-only package were proved, it would control the local
transverse energy through deterministic row/column ceilings. It would not be
the same as a phase-kernel estimate for:

```text
Xi_273^0(lambda;sigma).
```

The phase-kernel route still requires one of:

```text
UniformFiberBound_280,
SelectionTransfer_280,
DirectShellBound_280,
or another same-family adaptive shell theorem.
```

Conversely, a future adaptive shell theorem would still need threshold and
low-level compatibility before it could be inserted into the final
lambda-summed target.

Thus the valid map is:

```text
ThresholdBudgetP0Closure_284
  controls the threshold-only row/column route;

ShellSelectionP0_283 plus adaptive shell input
  controls the phase-kernel route.
```

Neither route is currently closed.

### K. Final verdict

The audit produces exact budget tests:

```text
RowShellBudget_284,
ColumnShellBudget_284,
SigmaColumnShellBudget_284,
ShiftRemovalBudget_284(q),
FreqRemovalBudget_284(r),
LowLevelBudgetP0_284,
RowBarrierP0_284(q),
ColumnBarrierP0_284(r),
SigmaColumnBarrierP0_284(r).
```

But it does not prove any of them are `o_W(1)`.

Therefore:

```text
ThresholdBudgetP0Audit_284(P_minor^0)
  is structural only.

ThresholdBudgetP0Closure_284(q,r)
  remains OPEN.
```

## 6. Edge cases

- If `A_N^0=0`, the lambda grid is empty for that tuple; this is not a
  uniform threshold theorem.
- `K_0(lambda_j)` is integer-valued, so continuous optimization is only a
  diagnostic.
- `L_j` must be paid. A one-shell threshold choice does not control the
  base-tail sum.
- `H_j=sum_{k>=j}lambda_k^2` must be paid in the shell-counting column route.
- The same `mu_0,K_0` must be used for removals and transverse shell ceilings.
- The schedules must be selected before forming the data-dependent shell.
- If `q` or `r` approaches `1`, the formal optimized barriers can lose their
  moment gain.
- A fixed-`w` estimate is not enough; the `o_W(1)` order is still required.
- Low-level leakage below `lambda_min` is outside the large-spectrum shells
  and cannot be ignored.
- No threshold budget may be proved by assuming `PhaseKernelBound_273^0`,
  `TransIncBound_269`, or `NarrowMinorArc_3^B`.

## 7. Where it fits in the project map

```text
Module 270
  -> broad threshold-removal audit

Module 278
  -> fixed minimal family P_minor^0

Module 281
  -> Bessel benchmark reduces to row/column ceilings

Module 283
  -> ThresholdBudgetP0_283 isolated as an open local side row

Module 284
  -> exact threshold budget barriers inside P_minor^0
```

The next useful step is:

```text
Module 285:
  decide whether Phase J should next test the adaptive shell-selection row
  or issue a proof-or-blocked verdict for PhaseKernelBound_273^0 in the
  current tool set.
```

## 8. What remains open

This module does not prove:

- `ThresholdBudgetP0Closure_284(q,r)`;
- `ThresholdBudgetP0_283`;
- `LowLevelBudgetP0_284`;
- `ShiftMomentP0_284(q)`;
- `MultMomentP0_284(r)`;
- `RowBarrierP0_284(q)`;
- `ColumnBarrierP0_284(r)`;
- `SigmaColumnBarrierP0_284(r)`;
- `SideRowsP0Ready_283`;
- `WUniformP0_283`;
- `LowLevelCutoffP0_283`;
- `DyadicUniformityP0_283`;
- `ShellSelectionP0_283`;
- `DegRowsP0Small_282`;
- `MajorDiffBound_282`;
- `PhysDiagLocal_282`;
- `DegFreePhaseGate_282`;
- `LargeSieveBesselClosure_281`;
- `AdaptiveBesselGain_281`;
- `UniformFiberBound_280`;
- `SelectionTransfer_280`;
- `DirectShellBound_280`;
- `PhaseKernelBound_273^0`;
- `PhaseKernelBound_273`;
- `TransverseGateProofPkg_276`;
- `TransGateSideRows_274`;
- `TransIncBound_269`;
- `ThresholdOnlyClosure_270`;
- `MinorArcTransfer_3^B`;
- `NarrowMinorArc_3^B`;
- selector transfer to the actual sharp moving selector;
- `ProjectedModelNeutrality_3^major`;
- `WProjectedLocalMatch_3^major`;
- `ProjectedMajorTarget_3^B`;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original selected-average problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not treat optimized threshold barriers as estimates.
- Do not choose different `mu_0,K_0` schedules for removals and shells.
- Do not drop the base-tail factor `L_j` or the shell-counting factor `H_j`.
- Do not hide low-level leakage below `lambda_min`.
- Do not call deterministic row/column ceilings phase-kernel cancellation.
- Do not use fixed-set estimates as adaptive shell estimates.
- Do not use `PhaseKernelBound_273^0`, `TransIncBound_269`,
  `NarrowMinorArc_3^B`, `ResCube_3^sharp`, `CPC_3^sharp`,
  `RBDH_pair_short`, or `AU^3` as inputs to prove the threshold budget.
- Do not move this local `P_minor^0` audit to the actual sharp moving
  selector without transfer rows.
