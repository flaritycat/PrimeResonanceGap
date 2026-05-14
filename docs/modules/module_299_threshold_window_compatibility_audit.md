# Module 299: Threshold-window compatibility audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

This module performs the threshold-window compatibility audit selected by
Module 298.

Define:

```text
ThresholdWindowCompatibilityAudit_299(P_minor^0).
```

The audit asks whether the same threshold schedules:

```text
mu_0(lambda),
K_0(lambda)
```

can simultaneously make:

```text
bad-shift removals small,
bad-frequency removals small,
row shell ceilings small,
and at least one column shell ceiling small.
```

Verdict:

```text
ThresholdWindowCompatibilityAudit_299(P_minor^0):
  STRUCTURAL / EXTRACTION.

ContinuousRowWindowCriterion_299(q):
  STRUCTURAL / EXTRACTION.

ContinuousColumnWindowCriterion_299(r):
  STRUCTURAL / EXTRACTION.

CurrentTrivialWindowRoute_299:
  FALSE / BLOCKED.

ThresholdWindowClosure_299(q,r):
  OPEN.

BarrierSmallnessPackage_299(q,r):
  OPEN.
```

This module proves only the continuous optimization identity behind the
threshold tension. It does not prove any barrier smallness, any integer
threshold schedule, any same-family uniform threshold theorem, or
`ThresholdBudgetP0Closure_284(q,r)`.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The module extracts necessary algebraic window tests. It does not establish a
useful threshold closure.

## 3. Definitions and variables

Work inside the Module 278 family:

```text
P_minor^0.
```

Use the Module 284 notation:

```text
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d|<=2D,
N^{delta_D}<=D<=N^{1-delta_D},
2D<=N/16,
lambda_j in Lambda_0,
L_j=# { k:lambda_k in Lambda_0, k>=j },
H_j=sum_{k>=j} lambda_k^2,
m_minor^0=#Minor_0(R,eta),
C_D=D^(-1)# { d:D<|d|<=2D },
A_N^0=sup_{d,xi}|beta_0(d,xi)|.
```

The residual coefficients are:

```text
f_0(n)=nu_0(n)-1,
B_d^0(n)=f_0(n+d)conj(f_0(n)),
beta_0(d,xi)=widehat{B_d^0}(xi).
```

For `q,r>1`, write:

```text
M_j^row(q)=ShiftMomentP0_284(q;lambda_j),
M_j^col(r)=MultMomentP0_284(r;lambda_j).
```

Thus:

```text
M_j^row(q)
  =
  D^(-1) sum_{D<|d|<=2D} E_{d,0}(lambda_j)^q,

M_j^col(r)
  =
  D^(-1) sum_{xi in Minor_0(R,eta)}
    N_{xi,0}(lambda_j)^r.
```

The visible row-window cost at level `lambda_j` is:

```text
F_j^row(mu)
  =
  lambda_j^2 [
    M_j^row(q) mu^(1-q)
    + L_j C_D mu
  ].
```

The visible column-window costs are:

```text
F_j^col(K)
  =
  lambda_j^2 [
    (A_N^0)^2 M_j^col(r) K^(1-r)
    + (A_N^0)^2 L_j m_minor^0 K/D
  ],
```

and:

```text
F_j^sig(K)
  =
  lambda_j^2 [
    (A_N^0)^2 M_j^col(r) K^(1-r)
    + m_minor^0 H_j K/D
  ].
```

These are the continuous relaxations of the Module 284 budget tensions. In
the actual threshold package, `K_0(lambda_j)` must be integer-valued and
admissible, and all threshold schedules must be compatible with the declared
family and the final W-limit order.

## 4. Assumptions

This module assumes Modules 278, 284, 297, and 298, plus the active status
ledger.

It does not assume:

```text
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
RowBarrierP0_284(q)=o_W(1),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
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

### A. The elementary window identity

For `s>1` and `a,b>0`, define:

```text
Phi_s(a,b)=inf_{t>0} (a t + b t^(1-s)).
```

The critical point satisfies:

```text
a=(s-1)b t^(-s),
```

so:

```text
t_* = ((s-1)b/a)^(1/s).
```

Therefore:

```text
Phi_s(a,b)
  =
  c_s a^((s-1)/s)b^(1/s),

c_s=s(s-1)^(-(s-1)/s).
```

This identity is the continuous version of the threshold-window tension:
one term wants the threshold small, and the other wants it large.

If either `a=0` or `b=0`, the infimum is `0` in the continuous relaxation.
This is a degenerate case and does not by itself give a uniform threshold
theorem.

### B. Row-window criterion

Apply the identity with:

```text
s=q,
a=L_j C_D,
b=M_j^row(q).
```

Then:

```text
inf_{mu>0} F_j^row(mu)
  =
  c_q lambda_j^2
    (L_j C_D)^((q-1)/q)
    M_j^row(q)^(1/q).
```

Summing over `j` gives exactly the Module 284 row barrier, up to the harmless
constant `c_q`:

```text
sum_j inf_{mu>0} F_j^row(mu)
  =
  c_q RowBarrierP0_284(q).
```

Thus a row-only threshold window cannot be extracted from the current
budgets unless:

```text
RowBarrierP0_284(q)=o_W(1)
```

is proved with the same W-limit order, lambda grid, dyadic range, and local
family conventions.

Classification:

```text
ContinuousRowWindowCriterion_299(q):
  STRUCTURAL / EXTRACTION.
```

It is an optimization identity, not an analytic moment estimate.

### C. Column-window criterion

For the Module 273 column ceiling, apply the identity with:

```text
s=r,
a=(A_N^0)^2 L_j m_minor^0/D,
b=(A_N^0)^2 M_j^col(r).
```

Then:

```text
inf_{K>0} F_j^col(K)
  =
  c_r lambda_j^2
    (A_N^0)^2
    (L_j m_minor^0/D)^((r-1)/r)
    M_j^col(r)^(1/r).
```

Summing gives:

```text
sum_j inf_{K>0} F_j^col(K)
  =
  c_r ColumnBarrierP0_284(r).
```

For the shell-counting column ceiling, apply the identity with:

```text
s=r,
a=m_minor^0 H_j/D,
b=(A_N^0)^2 M_j^col(r).
```

Then:

```text
inf_{K>0} F_j^sig(K)
  =
  c_r lambda_j^2
    ((A_N^0)^2 M_j^col(r))^(1/r)
    (m_minor^0 H_j/D)^((r-1)/r).
```

Summing gives:

```text
sum_j inf_{K>0} F_j^sig(K)
  =
  c_r SigmaColumnBarrierP0_284(r).
```

Therefore a column threshold window cannot be extracted from the current
budgets unless at least one of:

```text
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1)
```

is proved in the same family.

Classification:

```text
ContinuousColumnWindowCriterion_299(r):
  STRUCTURAL / EXTRACTION.
```

Again, this is an optimization identity, not a multiplicity estimate.

### D. What an actual threshold-window closure would require

Define the barrier package:

```text
BarrierSmallnessPackage_299(q,r)
  =
  RowBarrierP0_284(q)
  +
  min(
    ColumnBarrierP0_284(r),
    SigmaColumnBarrierP0_284(r)
  )
```

together with the following non-algebraic rows:

```text
integer/range rounding for K_0(lambda_j),
declared-family threshold selection,
same W-limit order,
dyadic and lambda-grid uniformity,
low-level tail compatibility from Module 297,
and no endpoint-strength input.
```

The natural closure target is:

```text
ThresholdWindowClosure_299(q,r):
  BarrierSmallnessPackage_299(q,r)=o_W(1)
  with all threshold schedules admissible in P_minor^0.
```

This target remains open.

The continuous optimum may choose:

```text
mu_j^* = ((q-1)M_j^row(q)/(L_j C_D))^(1/q),
K_j^* = ((r-1)M_j^col(r)/(L_j m_minor^0/D))^(1/r)
```

in the first column route, or the analogous `H_j` expression in the
shell-counting route. These formulas are oracle diagnostics. They do not by
themselves produce a valid proof because the active family needs a declared
threshold schedule and integer-valued admissible `K_0`.

Classification:

```text
ThresholdWindowClosure_299(q,r):
  OPEN.

BarrierSmallnessPackage_299(q,r):
  OPEN.
```

### E. Why the current trivial route is blocked

Modules 297 and 298 supply only deterministic caps of the form:

```text
|beta_0(d,xi)| <= L_{N,w}^2,
E_{d,0}(lambda) <= L_{N,w}^4,
N_{xi,0}(lambda) <= S_D.
```

These imply only crude moment upper bounds such as:

```text
M_j^row(q) <= C_D L_{N,w}^{4q},
M_j^col(r) <= D^(-1) m_minor^0 S_D^r.
```

Inserting these into the continuous barriers does not force:

```text
RowBarrierP0_284(q)=o_W(1),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1).
```

The reason is not subtle: the trivial caps are exactly the row/column ceiling
scale that the threshold window is trying to improve. They do not contain
transverse cancellation, structured sparsity, or a new same-family moment
estimate.

Thus:

```text
CurrentTrivialWindowRoute_299:
  FALSE / BLOCKED.
```

This is not a disproof of future threshold windows. It says only that the
current deterministic caps and vacuous removal schedule do not prove the
window closure.

### F. What this changes after Module 298

Module 298 showed that actual bad sets can be made empty by maximal
thresholds, but that this destroys the shell budgets.

Module 299 sharpens the remaining task:

```text
not merely choose thresholds;
prove barrier-small moments strong enough that the thresholds have a
non-vacuous compatibility window.
```

So the threshold branch is now reduced to a smaller analytic question:

```text
Can one prove RowBarrierP0_284(q)=o_W(1)
and at least one of the two column barriers =o_W(1),
without using endpoint-strength assumptions?
```

No such proof is supplied here.

## 6. Edge cases

If:

```text
Lambda_0=emptyset,
```

then every displayed threshold sum is empty for that tuple. This does not
prove a uniform threshold theorem.

If a moment term is zero at one lambda level, the continuous optimum may put
the corresponding threshold at a degenerate limit. The actual local family
still needs admissible positive thresholds and integer `K_0`.

The continuous minimizer for `K` may be less than `1` or greater than `S_D`.
Rounding and range truncation can only add work; it cannot convert an unproved
barrier into a proof.

The continuous minimizer may depend on the unknown moments
`M_j^row(q)` and `M_j^col(r)`. A future proof must explain whether the
threshold schedule is declared uniformly, chosen by an allowed deterministic
rule, or covered by a supremum over schedules.

The row and column windows use different schedules only in the sense that
`mu_0` and `K_0` are different threshold functions. Within each function, the
same schedule must serve both removals and shell ceilings.

The local low-level fourth-moment tail from Module 297 is already handled
inside `P_minor^0`, but this does not imply barrier smallness.

Nothing here transfers to the actual sharp moving selector.

## 7. Project-map location

The local threshold branch after Module 299 is:

```text
Module 297:
  local fourth-moment low-level tail closed inside P_minor^0.

Module 298:
  vacuous bad-set removal proved, but not threshold closure.

Module 299:
  useful threshold-window compatibility reduced to barrier smallness,
  rounding/range admissibility, and same-family uniform schedule selection.
```

The remaining threshold route is:

```text
BarrierSmallnessPackage_299(q,r)
  + threshold schedule admissibility
  + W/dyadic/lambda uniformity
  => possible ThresholdBudgetP0Closure_284(q,r).
```

This is still a local side-row branch, not a proof of
`PhaseKernelBound_273^0`.

## 8. What remains open

Still open:

```text
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
RowBarrierP0_284(q)=o_W(1),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
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

Do not cite the continuous minimization identity as proving threshold
smallness. It only identifies the barrier.

Do not use the oracle minimizers as valid schedules unless a future module
proves admissibility, rounding, range, and uniformity.

Do not treat the Module 297 low-level tail proof as a proof of row, column,
or multiplicity moment estimates.

Do not treat the Module 298 vacuous removal schedule as threshold closure.

Do not prove any threshold row by assuming:

```text
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
selector transfer,
or the original selected-average problem.
```

## 10. Next target

The next target should audit whether the row barrier can be made small from
current same-family inputs:

```text
Module 300:
  RowBarrierMomentAudit_300(P_minor^0).
```

That module should test whether Module 297's local energy tail, the trivial
pointwise envelope, Parseval, or any recorded same-family input can prove:

```text
RowBarrierP0_284(q)=o_W(1)
```

for some fixed `q>1`, without using an endpoint-strength assumption.
