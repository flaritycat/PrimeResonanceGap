# Module 308: Column-barrier moment audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

This module performs the column-side audit selected by Module 307.

Define:

```text
ColumnBarrierMomentAudit_308(P_minor^0).
```

The question is whether the current same-family inputs:

```text
pointwise logarithmic envelope,
normalized Parseval,
first-moment incidence counting,
the local low-level fourth-moment tail,
and vacuous removal schedules
```

prove either of the Module 284 column barriers:

```text
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1)
```

for some fixed `r>1`.

Verdict:

```text
ColumnBarrierMomentAudit_308(P_minor^0):
  STRUCTURAL / EXTRACTION.

ColumnIncidenceFirstMoment_308(lambda_j):
  STRUCTURAL / EXTRACTION.

EnergyIncidenceColumnCeiling_308(r):
  STRUCTURAL / EXTRACTION.

SigmaEnergyIncidenceCeiling_308(r):
  STRUCTURAL / EXTRACTION.

CurrentColumnBarrierRoute_308(r):
  FALSE / BLOCKED.

LowLevelTailToColumnBarrier_308:
  FALSE / BLOCKED.

VacuousRemovalToColumnBarrier_308:
  FALSE / BLOCKED.

ColumnMultiplicityGainTarget_308(r):
  OPEN.
```

The audit gives useful ceilings, but no `o_W(1)` column-barrier estimate.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module extracts the best visible column-multiplicity bounds from current
local inputs and classifies the route. It proves no column-barrier smallness,
no threshold closure, no adaptive-shell gain, no minor-arc endpoint, and no
selector transfer.

## 3. Definitions and variables

Work inside the Module 278 family:

```text
P_minor^0.
```

Use:

```text
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d|<=2D,
N^{delta_D}<=D<=N^{1-delta_D},
2D<=N/16.
```

Let:

```text
S_D=# { d:D<|d|<=2D },
C_D=S_D/D,
m_minor^0=#Minor_0(R,eta),
L_{N,w}=1+log(WN+b).
```

The local residual derivative coefficients are:

```text
f_0(n)=nu_0(n)-1,
B_d^0(n)=f_0(n+d)conj(f_0(n)),
beta_0(d,xi)=widehat{B_d^0}(xi),
A_N^0=sup_{d,xi}|beta_0(d,xi)|.
```

For `lambda_j in Lambda_0`, define:

```text
Spec_{d,0}^minor(lambda_j)
  =
  { xi in Minor_0(R,eta):
      |beta_0(d,xi)|>=lambda_j },

N_{xi,0}(lambda_j)
  =
  # { d:D<|d|<=2D,
      xi in Spec_{d,0}^minor(lambda_j) }.
```

The column multiplicity moment is:

```text
MultMomentP0_284(r;lambda_j)
  =
  D^(-1) sum_{xi in Minor_0(R,eta)}
    N_{xi,0}(lambda_j)^r.
```

Write:

```text
theta_r=(r-1)/r.
```

The two Module 284 column barriers are:

```text
ColumnBarrierP0_284(r)
  =
  sum_j lambda_j^2
    (A_N^0)^2
    (L_j m_minor^0/D)^theta_r
    MultMomentP0_284(r;lambda_j)^(1/r),

SigmaColumnBarrierP0_284(r)
  =
  sum_j lambda_j^2
    ((A_N^0)^2 MultMomentP0_284(r;lambda_j))^(1/r)
    (m_minor^0 H_j/D)^theta_r.
```

For the dyadic grid:

```text
lambda_j=2^(-j)A_N^0,
lambda_min=A_N^0 N^(-kappa_lambda),
lambda_j>=lambda_min,
```

when `A_N^0>0`; if `A_N^0=0`, the grid is empty.

## 4. Assumptions

This module assumes Modules 278, 284, 297, 298, 299, 300, and 307, plus the
active status ledger.

It uses only:

```text
normalized Parseval on G_N,
the P_minor^0 pointwise logarithmic envelope,
the Module 297 local second-energy bound,
incidence counting,
and deterministic dyadic-grid estimates.
```

It does not assume:

```text
ColumnMultiplicityGainTarget_308(r),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
MultMomentP0_284(r;lambda_j) smallness,
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ThresholdBudgetP0Closure_284(q,r),
ShiftRemovalBudget_284(q)=o_W(1),
FreqRemovalBudget_284(r)=o_W(1),
RowBarrierP0_284(q)=o_W(1),
SizeSensitiveClosure_306,
FixedFiberRowSquareGain_305(P_minor^0),
SameShiftSquareKernelGain_303(P_minor^0),
RowSquareMomentTarget_302,
RowMomentGainTarget_300(q),
SideRowsP0Ready_283,
SidePkg_291,
SidePkgReady_293,
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
PhaseKernelBound_273,
DirectShellCrossTermGain_287,
SelectionTransfer_280,
UniformFiberBound_280,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
selector transfer,
the original selected-average problem,
the all-alpha theorem,
or the unconditional finite-type theorem.
```

## 5. Proof / disproof / reduction

### A. Current local inputs

Module 297 gives, inside `P_minor^0`:

```text
|beta_0(d,xi)| <= L_{N,w}^2,
A_N^0 <= L_{N,w}^2,
E2_minor^0(D;R,eta)
  =
  D^(-1) sum_d
    sum_{xi in Minor_0(R,eta)} |beta_0(d,xi)|^2
  <= C_D L_{N,w}^4.
```

It also proves the below-`lambda_min` fourth-moment tail inside `P_minor^0`.
That low-level tail is not a high-level column multiplicity estimate.

### B. Pure counting cap

For every `xi` and `lambda_j`:

```text
0 <= N_{xi,0}(lambda_j) <= S_D.
```

Therefore:

```text
MultMomentP0_284(r;lambda_j)
  <=
  D^(-1) m_minor^0 S_D^r
  =
  C_D^r m_minor^0 D^(r-1).
```

This is the raw counting cap. It uses no coefficient energy. Inserted into
the column barriers it gives only large deterministic ceilings with an
uncontrolled frequency-count factor. It cannot force `o_W(1)` under the
declared `P_minor^0` family.

### C. First-moment incidence bound

Let:

```text
I_j
  =
  sum_{xi in Minor_0(R,eta)} N_{xi,0}(lambda_j)
  =
  sum_d #Spec_{d,0}^minor(lambda_j).
```

On `Spec_{d,0}^minor(lambda_j)`:

```text
lambda_j^2 <= |beta_0(d,xi)|^2.
```

Hence:

```text
I_j
  <=
  lambda_j^(-2)
  sum_d sum_{xi in Minor_0(R,eta)}
    |beta_0(d,xi)|^2
  =
  D lambda_j^(-2) E2_minor^0(D;R,eta).
```

Using `N_{xi,0}(lambda_j)<=S_D`:

```text
N_{xi,0}(lambda_j)^r
  <=
  S_D^(r-1) N_{xi,0}(lambda_j).
```

Therefore:

```text
MultMomentP0_284(r;lambda_j)
  <=
  D^(-1) S_D^(r-1) I_j
  <=
  S_D^(r-1) lambda_j^(-2) E2_minor^0(D;R,eta).
```

Classification:

```text
ColumnIncidenceFirstMoment_308(lambda_j):
  STRUCTURAL / EXTRACTION.
```

This is better than raw counting when the energy incidence is small, but it is
still a first-moment incidence estimate. It contains no high-multiplicity
repulsion beyond `N_{xi,0}<=S_D`.

### D. Column barrier ceiling from incidence

Taking the `r`th root gives:

```text
MultMomentP0_284(r;lambda_j)^(1/r)
  <=
  S_D^theta_r
  E2_minor^0(D;R,eta)^(1/r)
  lambda_j^(-2/r).
```

Insert this into `ColumnBarrierP0_284(r)`:

```text
ColumnBarrierP0_284(r)
  <=
  (A_N^0)^2 E2_minor^0(D;R,eta)^(1/r) C_D^theta_r
  sum_j lambda_j^(2 theta_r)
    (L_j m_minor^0)^theta_r.
```

Using:

```text
E2_minor^0(D;R,eta) <= C_D L_{N,w}^4,
```

this becomes:

```text
ColumnBarrierP0_284(r)
  <=
  C_D (A_N^0)^2 L_{N,w}^{4/r}
  sum_j lambda_j^(2 theta_r)
    (L_j m_minor^0)^theta_r.
```

For the dyadic grid, with `J_Lambda=#Lambda_0`:

```text
L_j <= J_Lambda,
sum_j lambda_j^(2 theta_r) <= C_r (A_N^0)^(2 theta_r),
```

where `C_r` depends only on fixed `r>1`. Thus:

```text
ColumnBarrierP0_284(r)
  <=
  C_r C_D J_Lambda^theta_r
  (m_minor^0)^theta_r
  L_{N,w}^{4/r}
  (A_N^0)^(2+2 theta_r).
```

Since `A_N^0<=L_{N,w}^2`:

```text
ColumnBarrierP0_284(r)
  <=
  C_r C_D J_Lambda^theta_r
  (m_minor^0)^theta_r
  L_{N,w}^8.
```

Classification:

```text
EnergyIncidenceColumnCeiling_308(r):
  STRUCTURAL / EXTRACTION.
```

This is a ceiling, not smallness. The factor `(m_minor^0)^theta_r` is not
forced to be small in `P_minor^0`; in a cyclic group it may grow with `N`.

### E. Sigma column barrier ceiling from incidence

The same incidence estimate in `SigmaColumnBarrierP0_284(r)` gives:

```text
SigmaColumnBarrierP0_284(r)
  <=
  (A_N^0)^(2/r) E2_minor^0(D;R,eta)^(1/r) C_D^theta_r
  sum_j lambda_j^(2 theta_r)
    (m_minor^0 H_j)^theta_r.
```

Using the Module 297 energy ceiling:

```text
SigmaColumnBarrierP0_284(r)
  <=
  C_D (A_N^0)^(2/r) L_{N,w}^{4/r}
  sum_j lambda_j^(2 theta_r)
    (m_minor^0 H_j)^theta_r.
```

For the dyadic grid:

```text
H_j=sum_{k>=j}lambda_k^2 <= C lambda_j^2.
```

Hence:

```text
sum_j lambda_j^(2 theta_r) H_j^theta_r
  <=
  C_r (A_N^0)^(4 theta_r).
```

Therefore:

```text
SigmaColumnBarrierP0_284(r)
  <=
  C_r C_D
  (m_minor^0)^theta_r
  L_{N,w}^{4/r}
  (A_N^0)^(2/r+4 theta_r).
```

Since `A_N^0<=L_{N,w}^2`, the exponent again collapses to:

```text
SigmaColumnBarrierP0_284(r)
  <=
  C_r C_D
  (m_minor^0)^theta_r
  L_{N,w}^8.
```

Classification:

```text
SigmaEnergyIncidenceCeiling_308(r):
  STRUCTURAL / EXTRACTION.
```

The sigma barrier removes the visible `J_Lambda^theta_r` loss from the crude
display, but it still leaves the frequency-count factor
`(m_minor^0)^theta_r`. That factor is not an `o_W(1)` gain.

### F. Why this does not prove the column barriers

For fixed `w`, the current ceilings are of the form:

```text
C_r C_D J_Lambda^theta_r (m_minor^0)^theta_r L_{N,w}^8
```

or:

```text
C_r C_D (m_minor^0)^theta_r L_{N,w}^8.
```

The active family does not impose a smallness condition on `m_minor^0`; it is
a count of minor frequencies. The current estimates also contain only first
incidence information and the pointwise logarithmic envelope. They do not
show that high-multiplicity frequencies are rare at the strength needed after
the lambda weights and Module 284 normalization are restored.

Therefore:

```text
CurrentColumnBarrierRoute_308(r):
  FALSE / BLOCKED.
```

This is not a disproof of column-barrier smallness. It says the present
pointwise, Parseval, first-incidence, low-level, and vacuous-removal inputs do
not prove it.

### G. Why the low-level tail does not help here

Module 297 controls:

```text
|beta_0(d,xi)| < lambda_min
```

in a fourth-moment tail. The column barriers in this module concern
high-level sets:

```text
|beta_0(d,xi)| >= lambda_j >= lambda_min.
```

The low-level tail does not bound the distribution of:

```text
N_{xi,0}(lambda_j)
```

for the high-level coefficients. Thus:

```text
LowLevelTailToColumnBarrier_308:
  FALSE / BLOCKED.
```

### H. Why vacuous removal does not help here

Module 298 showed that bad-frequency sets can be made empty by taking:

```text
K_0(lambda)=S_D.
```

That removes bad frequencies, but it is exactly the largest possible
threshold and it enlarges the column shell budgets. The optimized column
barriers ask whether removal and shell budgets can be small for one compatible
schedule. Empty bad sets alone do not supply that schedule.

Thus:

```text
VacuousRemovalToColumnBarrier_308:
  FALSE / BLOCKED.
```

### I. The next genuine column target

The missing input is not another first-moment incidence count. A useful column
route needs a same-family high-multiplicity estimate strong enough that:

```text
min(
  ColumnBarrierP0_284(r),
  SigmaColumnBarrierP0_284(r)
)
=o_W(1)
```

after the lambda sum, dyadic ranges, W-limit order, and threshold schedules
are all restored.

Define:

```text
ColumnMultiplicityGainTarget_308(r):
  a same-family estimate for MultMomentP0_284(r;lambda_j), or for the
  distribution of N_{xi,0}(lambda_j), beating first-moment incidence by enough
  to make at least one Module 284 column barrier o_W(1).
```

Classification:

```text
ColumnMultiplicityGainTarget_308(r):
  OPEN.
```

## 6. Edge cases

If `A_N^0=0`, then the declared dyadic grid is empty. This is a degenerate
local case, not a useful column-barrier theorem.

If `Lambda_0` is empty, all displayed lambda sums vanish for that tuple. That
vacuity is not threshold-window closure in the useful regime.

If `m_minor^0=0`, the column barriers vanish locally because there are no
minor frequencies. This is not the active minor-arc problem.

If `r` is allowed to vary with `N`, the constants `C_r` and the exponents in
the dyadic sums must be re-audited. This module treats fixed `r>1`.

If a future estimate controls `sum_xi N_{xi,0}` only, it is still a
first-moment incidence estimate. It must control the `r`-moment or its
distribution tail after all Module 284 weights are restored.

Nothing in this module transfers from `P_minor^0` to the actual sharp moving
selector.

## 7. Project-map location

The threshold-window branch now reads:

```text
Module 299:
  useful windows require row barrier smallness and at least one column
  barrier.

Module 300:
  current energy-only row-barrier route gives only a ceiling.

Modules 302-306:
  row distribution, row-square, and fixed-fiber row-square routes remain
  open or blocked under current tools.

Module 307:
  row-square continuation is paused as the immediate next move.

Module 308:
  current first-incidence column route gives only ceilings and leaves
  ColumnMultiplicityGainTarget_308(r) open.
```

This means the current threshold-window toolkit is blocked on both sides:

```text
row side:
  needs a genuine row-energy distribution or same-shift kernel gain;

column side:
  needs a genuine high-multiplicity distribution gain.
```

Even a future column gain would not close the threshold window without the row
side and all schedule/uniformity rows.

## 8. What remains open

Still open:

```text
ColumnMultiplicityGainTarget_308(r),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
MultMomentP0_284(r;lambda_j) smallness,
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ThresholdBudgetP0Closure_284(q,r),
FreqRemovalBudget_284(r)=o_W(1),
RowBarrierP0_284(q)=o_W(1),
SizeSensitiveClosure_306,
FixedFiberRowSquareGain_305(P_minor^0),
SameShiftSquareKernelGain_303(P_minor^0),
RowSquareMomentTarget_302,
RowMomentGainTarget_300(q),
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

Do not cite `ColumnIncidenceFirstMoment_308`,
`EnergyIncidenceColumnCeiling_308`, or
`SigmaEnergyIncidenceCeiling_308` as column-barrier smallness.

Do not cite `CurrentColumnBarrierRoute_308(r)` as a theorem that no column
barrier can be proved. It blocks only the current route.

Do not cite `LowLevelTailToColumnBarrier_308` or
`VacuousRemovalToColumnBarrier_308` as a threshold-window theorem.

Do not turn a first-moment incidence bound for:

```text
sum_xi N_{xi,0}(lambda_j)
```

into an `r`-moment estimate without paying the `S_D^(r-1)` loss or proving a
genuine high-multiplicity distribution theorem.

Do not prove the column barriers by assuming:

```text
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
PhaseKernelBound_273^0,
selector transfer,
or the original selected-average problem.
```

Do not move this local `P_minor^0` audit to the actual sharp moving selector
without transfer rows.

## 10. Next target

The next natural target is:

```text
Module 309:
  ColumnMultiplicityDistributionAudit_309(P_minor^0).
```

That module should decide whether a layer-cake or distributional formulation
of `N_{xi,0}(lambda_j)` produces a genuinely smaller subtarget than
`ColumnMultiplicityGainTarget_308(r)`, or whether it only repeats the
first-incidence ceiling in another form.
