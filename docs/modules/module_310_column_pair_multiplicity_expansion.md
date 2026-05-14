# Module 310: Column-pair multiplicity expansion inside `P_minor^0`

## 1. Precise theorem / claim being advanced

This module performs the concrete `r=2` column-pair expansion selected by
Module 309.

Define:

```text
ColumnPairMultiplicityExpansion_310(P_minor^0).
```

The question is whether the second column multiplicity moment:

```text
MultMomentP0_284(2;lambda_j)
```

is a genuinely smaller object than the general high-multiplicity tail target,
or whether current tools still reduce it to first-incidence ceilings.

Verdict:

```text
ColumnPairMultiplicityExpansion_310(P_minor^0):
  STRUCTURAL / EXTRACTION.

ColumnPairIdentity_310(lambda_j):
  STRUCTURAL / EXTRACTION.

ColumnDiagonalPair_310(lambda_j):
  STRUCTURAL / EXTRACTION.

OffDiagonalSameFrequencyPair_310(lambda_j):
  OPEN.

FirstIncidencePairCollapse_310(lambda_j):
  FALSE / BLOCKED as a gain route.

WeightedPairEnergyCriterion_310(lambda_j):
  STRUCTURAL / EXTRACTION.

WeightedColumnPairEnergyTarget_310(P_minor^0):
  OPEN.

WeightedColumnPairEnergyAudit_311(P_minor^0):
  OPEN next target.
```

The exact pair expansion is useful, but it does not prove column-barrier
smallness. The current unweighted incidence route collapses back to the
Module 308 first-incidence ceiling. A possible next smaller test is the
weighted coefficient-pair energy forced by the threshold lower bound.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is an exact expansion and proof-or-blocked audit. It proves no
column-barrier smallness, no threshold closure, no adaptive-shell gain, no
minor-arc endpoint, and no selector transfer.

## 3. Definitions and variables

Work inside:

```text
P_minor^0.
```

Use:

```text
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d|<=2D,
S_D=# { d:D<|d|<=2D },
C_D=S_D/D,
m_minor^0=#Minor_0(R,eta).
```

For `lambda_j in Lambda_0`, define the large-spectrum indicator:

```text
a_j(d,xi)
  =
  1_{xi in Minor_0(R,eta)}
  1_{|beta_0(d,xi)|>=lambda_j}.
```

Then:

```text
Spec_{d,0}^minor(lambda_j)
  =
  { xi:a_j(d,xi)=1 },

N_{xi,0}(lambda_j)
  =
  sum_{D<|d|<=2D} a_j(d,xi).
```

The `r=2` column moment is:

```text
MultMomentP0_284(2;lambda_j)
  =
  D^(-1) sum_{xi in Minor_0(R,eta)}
    N_{xi,0}(lambda_j)^2.
```

For two shifts define the same-frequency pair intersection:

```text
P_j(d_1,d_2)
  =
  sum_{xi in Minor_0(R,eta)}
    a_j(d_1,xi)a_j(d_2,xi).
```

Equivalently:

```text
P_j(d_1,d_2)
  =
  #(
    Spec_{d_1,0}^minor(lambda_j)
    cap
    Spec_{d_2,0}^minor(lambda_j)
  ).
```

Define:

```text
PairDiag_310(lambda_j)
  =
  D^(-1) sum_d P_j(d,d),

PairOff_310(lambda_j)
  =
  D^(-1) sum_{d_1 != d_2} P_j(d_1,d_2).
```

## 4. Assumptions

This module assumes Modules 278, 284, 297, 298, 299, 300, 307, 308, and 309,
plus the active status ledger.

It uses only:

```text
finite sums,
the large-spectrum threshold definition,
Module 297's local second-energy bound,
and deterministic first-incidence estimates.
```

It does not assume:

```text
WeightedColumnPairEnergyTarget_310(P_minor^0),
ColumnTailGainTarget_309(r),
ColumnMultiplicityGainTarget_308(r),
ColumnBarrierP0_284(2)=o_W(1),
SigmaColumnBarrierP0_284(2)=o_W(1),
MultMomentP0_284(2;lambda_j) smallness,
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

### A. Exact same-frequency pair identity

By definition:

```text
N_{xi,0}(lambda_j)^2
  =
  sum_{d_1,d_2}
    a_j(d_1,xi)a_j(d_2,xi).
```

Summing over minor frequencies and normalizing by `D` gives:

```text
MultMomentP0_284(2;lambda_j)
  =
  D^(-1) sum_{d_1,d_2} P_j(d_1,d_2).
```

Splitting the shift-pair diagonal:

```text
MultMomentP0_284(2;lambda_j)
  =
  PairDiag_310(lambda_j)
  +
  PairOff_310(lambda_j).
```

Classification:

```text
ColumnPairIdentity_310(lambda_j):
  STRUCTURAL / EXTRACTION.
```

This is an exact identity. It is not a multiplicity estimate.

### B. Diagonal shift-pair row

For `d_1=d_2=d`:

```text
P_j(d,d)=#Spec_{d,0}^minor(lambda_j).
```

Thus:

```text
PairDiag_310(lambda_j)
  =
  D^(-1) sum_d #Spec_{d,0}^minor(lambda_j)
  =
  D^(-1) I_{j,0}.
```

Using Module 308's first-incidence energy bound:

```text
I_{j,0}
  <=
  D lambda_j^(-2) E2_minor^0(D;R,eta),
```

we get:

```text
PairDiag_310(lambda_j)
  <=
  lambda_j^(-2) E2_minor^0(D;R,eta).
```

Classification:

```text
ColumnDiagonalPair_310(lambda_j):
  STRUCTURAL / EXTRACTION.
```

The diagonal is controlled by first energy. This does not close either Module
284 column barrier uniformly, because the barriers still include minor-arc
frequency-count, lambda-sum, threshold-schedule, and W-limit weights. It is a
manageable row only relative to the off-diagonal pair problem.

### C. Off-diagonal same-frequency shift pairs

The nontrivial part is:

```text
PairOff_310(lambda_j)
  =
  D^(-1) sum_{d_1 != d_2}
    #(
      Spec_{d_1,0}^minor(lambda_j)
      cap
      Spec_{d_2,0}^minor(lambda_j)
    ).
```

This counts frequencies that are large for two distinct shifts in the same
dyadic shift shell.

The current ledger has no theorem forcing such repeated same-frequency
large-spectrum events to be rare. In particular, first-incidence counting
allows concentration of many shifts on the same frequency.

Classification:

```text
OffDiagonalSameFrequencyPair_310(lambda_j):
  OPEN.
```

### D. First-incidence collapse

The deterministic cap:

```text
N_{xi,0}(lambda_j) <= S_D
```

gives:

```text
N_{xi,0}(lambda_j)^2
  <=
  S_D N_{xi,0}(lambda_j).
```

Therefore:

```text
MultMomentP0_284(2;lambda_j)
  <=
  D^(-1) S_D I_{j,0}.
```

Using the first-incidence energy bound:

```text
MultMomentP0_284(2;lambda_j)
  <=
  S_D lambda_j^(-2) E2_minor^0(D;R,eta),
```

which is exactly Module 308's `r=2` incidence ceiling.

Equivalently:

```text
PairOff_310(lambda_j)
  <=
  D^(-1)(S_D-1)I_{j,0}.
```

This is not a pair-distribution gain; it is the same first-incidence ceiling
with the off-diagonal loss exposed.

Classification:

```text
FirstIncidencePairCollapse_310(lambda_j):
  FALSE / BLOCKED as a gain route.
```

### E. Weighted coefficient-pair criterion

On the intersection counted by `P_j(d_1,d_2)`:

```text
|beta_0(d_1,xi)| >= lambda_j,
|beta_0(d_2,xi)| >= lambda_j.
```

Therefore:

```text
a_j(d_1,xi)a_j(d_2,xi)
  <=
  lambda_j^(-4)
  |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2.
```

Define the weighted same-frequency pair energy:

```text
WPair_j(d_1,d_2)
  =
  sum_{xi in Minor_0(R,eta)}
    |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2.
```

Then:

```text
P_j(d_1,d_2)
  <=
  lambda_j^(-4) WPair_j(d_1,d_2).
```

Thus a possible route is to prove a same-family estimate for:

```text
D^(-1) sum_{d_1 != d_2} WPair_j(d_1,d_2)
```

stronger than the first-incidence ceiling after the factor
`lambda_j^(-4)` and the Module 284 column-barrier weights are restored.

Classification:

```text
WeightedPairEnergyCriterion_310(lambda_j):
  STRUCTURAL / EXTRACTION.
```

This is only a criterion. It is not a weighted pair-energy estimate.

### F. Why current Parseval/Cauchy does not yet close it

For each pair `d_1,d_2`, Cauchy gives:

```text
WPair_j(d_1,d_2)
  <=
  (
    sum_xi |beta_0(d_1,xi)|^4
  )^(1/2)
  (
    sum_xi |beta_0(d_2,xi)|^4
  )^(1/2).
```

The current ledger does not have a same-family fourth-power bound for these
minor coefficients strong enough to feed the column barriers. Using the
pointwise envelope:

```text
|beta_0(d,xi)| <= L_{N,w}^2
```

with Parseval only recovers ceiling-scale bounds.

Alternatively, Cauchy with second energies gives:

```text
WPair_j(d_1,d_2)
  <=
  E_{d_1,0}^minor E_{d_2,0}^minor,
```

and Module 297 only gives logarithmic ceilings for these row energies. After
summing over all off-diagonal shift pairs, this again supplies no
`o_W(1)` gain.

Therefore the weighted criterion identifies a possible next object, but does
not close the column target with current tools.

Define:

```text
WeightedColumnPairEnergyTarget_310(P_minor^0):
  a same-family estimate for the lambda-weighted off-diagonal sum of
  WPair_j(d_1,d_2), strong enough after threshold conversion to beat the
  Module 308 first-incidence ceiling in at least one column barrier.
```

Classification:

```text
WeightedColumnPairEnergyTarget_310(P_minor^0):
  OPEN.
```

## 6. Edge cases

If `A_N^0=0` or `Lambda_0=emptyset`, the large-spectrum grid is empty. This is
local vacuity, not column-barrier closure.

If `S_D=0`, the shift shell is empty. The active dyadic range treats this as
outside the meaningful local test.

If `d_1=d_2`, the pair is diagonal and reduces to first incidence. The new
obstruction is `d_1 != d_2`.

If a frequency is large for every shift, first incidence allows the extreme
`N_{xi,0}=S_D`. Excluding this requires a new multiplicity or weighted
same-frequency theorem.

If the weighted criterion is proved only for a fixed `lambda_j`, it still must
be checked after the full lambda sum, dyadic ranges, W-limit order, and
threshold schedule are restored.

Nothing in this module transfers from `P_minor^0` to the actual sharp moving
selector.

## 7. Project-map location

The column branch now reads:

```text
Module 308:
  first-incidence column estimates give only barrier ceilings.

Module 309:
  layer-cake with first-moment tails collapses back to first incidence.

Module 310:
  the concrete r=2 column moment is an exact same-frequency shift-pair
  incidence problem; the off-diagonal row remains open.
```

The next possible smaller route is:

```text
WeightedColumnPairEnergyTarget_310(P_minor^0),
```

but this is still an open analytic estimate, not a theorem.

## 8. What remains open

Still open:

```text
WeightedColumnPairEnergyAudit_311(P_minor^0),
WeightedColumnPairEnergyTarget_310(P_minor^0),
OffDiagonalSameFrequencyPair_310(lambda_j),
ColumnTailGainTarget_309(r),
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

Do not cite `ColumnPairIdentity_310(lambda_j)` as a pair gain. It is an exact
identity.

Do not cite `ColumnDiagonalPair_310(lambda_j)` as column-barrier smallness.
It only isolates the diagonal row.

Do not cite `FirstIncidencePairCollapse_310(lambda_j)` as a theorem that no
same-frequency pair theorem can exist. It blocks only the first-incidence
route.

Do not cite `WeightedPairEnergyCriterion_310(lambda_j)` as a proved weighted
pair estimate.

Do not cite `WeightedColumnPairEnergyTarget_310(P_minor^0)` or
`WeightedColumnPairEnergyAudit_311(P_minor^0)` as established.

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

The next target is:

```text
Module 311:
  WeightedColumnPairEnergyAudit_311(P_minor^0).
```

It should audit whether the weighted coefficient-pair energy criterion in
Section 5.E is smaller than the column multiplicity problem, or whether
current Parseval/Cauchy inputs again recover only ceiling-scale bounds.
