# Module 320: Size-sensitive minor-kernel criterion inside `P_minor^0`

## 1. Precise theorem / claim being advanced

Module 319 selected a smaller target: formulate an exact size-sensitive
criterion for the centered anti-diagonal minor-kernel row, with the Module
310 threshold conversion and Module 284 column-barrier weights still visible.

Define:

```text
SizeSensitiveMinorKernelCriterion_320(P_minor^0).
```

Verdict:

```text
SizeSensitiveMinorKernelCriterion_320(P_minor^0):
  STRUCTURAL / EXTRACTION.

CrossShellWeightedPairIdentity_320:
  STRUCTURAL / EXTRACTION.

PhiCriterion_320(Phi):
  CONDITIONAL.

DeterministicSizeBounds_320:
  STRUCTURAL / EXTRACTION.

CurrentSizeSensitiveClosure_320:
  FALSE / BLOCKED.

AdmissiblePhiGain_320(P_minor^0):
  OPEN.

DataDependentFiberGainAudit_321(P_minor^0):
  OPEN next target.
```

The module supplies an exact criterion. It does not prove the needed
cross-shell gain `Phi`, does not close the column barriers, and does not prove
the anti-diagonal minor-kernel row.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The conditional implication in this module is only a bookkeeping theorem:
if a future same-family cross-shell estimate is proved and if its losses pass
the displayed barriers, then it can be inserted into the `r=2` column-pair
route. No such estimate is proved here.

This module proves no weighted column-pair gain, no threshold closure, no
adaptive-shell gain, no phase-kernel bound, no residual cube endpoint, and no
selector transfer.

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d|<=2D.
```

Use:

```text
beta_0(d,xi)=widehat{B_d^0}(xi),
Minor_0=Minor_0(R,eta),
S_D=# { d:D<|d|<=2D },
C_D=S_D/D,
m_minor^0=#Minor_0(R,eta).
```

For a base threshold `lambda_j in Lambda_0` and shell height
`lambda_k in Lambda_0`, `k>=j`, use the Module 284 shell:

```text
J_{j,k}
  =
  { (d,xi):
      D<|d|<=2D,
      xi in Minor_0,
      lambda_k <= |beta_0(d,xi)| < 2lambda_k,
      (d,xi) satisfies the active transverse row/column caps at lambda_j }.
```

For two shell sets `U,V subset {d} x Minor_0`, define the cross-shell
weighted pair row:

```text
WOff(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    sum_{xi in Minor_0}
      1_U(d_1,xi)1_V(d_2,xi)
      |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2.
```

Define the shell energy:

```text
Eng(U)
  =
  D^(-1) sum_{(d,xi) in U}|beta_0(d,xi)|^2.
```

For a shell `U=J_{j,k}`, define:

```text
K(U)=sup_{xi in Minor_0} # { d:(d,xi) in U },
R(U)=sup_d # { xi:(d,xi) in U }.
```

The exact centered minor-kernel row from Module 319 is:

```text
M_minor^{circ}=WOff_311.
```

## 4. Assumptions

This module assumes the active status ledger and Modules 278, 284, 297, 308,
309, 310, 311, 312, 313, 314, 315, 316, 317, 318, and 319.

It uses:

```text
the Module 284 shell decomposition,
the Module 310 threshold conversion,
the Module 311 weighted pair row,
and finite cross-shell bookkeeping.
```

It does not assume:

```text
AdmissiblePhiGain_320(P_minor^0),
DataDependentFiberGainAudit_321(P_minor^0),
SizeSensitiveMinorKernelCriterion_320 as an estimate,
DirectSignedMinorKernelTheorem_319(P_minor^0),
DataDependentLargeSpectrumGain_319(P_minor^0),
ResidualEightSlotMinorCancellation_319(P_minor^0),
SignedMinorKernelGain_318(P_minor^0),
SignedMinorKernelCombinationTarget_314(P_minor^0),
MajorKernelCorrectionControl_314(P_minor^0),
CenteredFullAntiDiagonalControl_316(P_minor^0),
AntiDiagonalTwoShiftKernelGain_312(P_minor^0),
WeightedColumnSecondMomentTarget_311(P_minor^0),
WeightedColumnPairEnergyTarget_310(P_minor^0),
OffDiagonalSameFrequencyPair_310(lambda_j),
ColumnTailGainTarget_309(r),
ColumnMultiplicityGainTarget_308(r),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ThresholdBudgetP0Closure_284(q,r),
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
ProjectedMajorTarget_3^B,
WProjectedLocalMatch_3^major,
ProjectedModelNeutralityGate_260,
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

### A. Cross-shell threshold conversion

For the Module 310 pair count at base threshold `lambda_j`, decompose each
large coefficient into its shell:

```text
Spec_{d,0}^minor(lambda_j)
  =
  union_{k>=j} { xi:(d,xi) in J_{j,k} }.
```

For any two shell heights `k,l>=j`, if:

```text
(d_1,xi) in J_{j,k},
(d_2,xi) in J_{j,l},
```

then:

```text
|beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2
  >=
  lambda_k^2 lambda_l^2.
```

Thus the off-diagonal same-frequency pair count satisfies:

```text
PairOff_310(lambda_j)
  <=
  sum_{k,l>=j}
    (lambda_k lambda_l)^(-2)
    WOff(J_{j,k},J_{j,l}).
```

Adding the diagonal row from Module 310 gives the `r=2` multiplicity bound:

```text
MultMomentP0_284(2;lambda_j)
  <=
  M2_320(j),
```

where:

```text
M2_320(j)
  =
  lambda_j^(-2) E2_minor^0(D;R,eta)
  +
  sum_{k,l>=j}
    (lambda_k lambda_l)^(-2)
    WOff(J_{j,k},J_{j,l}).
```

Classification:

```text
CrossShellWeightedPairIdentity_320:
  STRUCTURAL / EXTRACTION.
```

This is an exact threshold conversion. It is not a bound until the
cross-shell rows are controlled.

### B. The `Phi` criterion

Let `Phi_{j;k,l}` be any same-family majorant satisfying:

```text
WOff(J_{j,k},J_{j,l}) <= Phi_{j;k,l}
```

for every active `j,k,l` with `k,l>=j`, in the exact `P_minor^0` conventions.

Define:

```text
M2_320(j;Phi)
  =
  lambda_j^(-2) E2_minor^0(D;R,eta)
  +
  sum_{k,l>=j}
    (lambda_k lambda_l)^(-2)
    Phi_{j;k,l}.
```

Insert this into the two Module 284 `r=2` column barriers:

```text
ColumnBarrier_320(Phi)
  =
  sum_j lambda_j^2
    (A_N^0)^2
    (L_j m_minor^0/D)^(1/2)
    M2_320(j;Phi)^(1/2),

SigmaColumnBarrier_320(Phi)
  =
  sum_j lambda_j^2
    ((A_N^0)^2 M2_320(j;Phi))^(1/2)
    (m_minor^0 H_j/D)^(1/2).
```

Criterion:

```text
if Phi is proved in P_minor^0
and
min(ColumnBarrier_320(Phi), SigmaColumnBarrier_320(Phi))=o_W(1),
then the r=2 column-pair multiplicity route supplies the corresponding
column-barrier input for the Module 284 threshold budget.
```

Classification:

```text
PhiCriterion_320(Phi):
  CONDITIONAL.
```

The criterion does not close the full threshold budget. It addresses only the
`r=2` column-pair component and still leaves the other Module 284 side rows,
low-level leakage, row barriers, transfer, and endpoint objects open.

### C. Deterministic size bounds

The criterion becomes meaningful only if `Phi` beats the current ceilings.
The following deterministic bounds are always available but do not provide
the needed gain by themselves.

For arbitrary `U,V`:

```text
WOff(U,V)
  <=
  D Eng(U)Eng(V).
```

This is the energy-product ceiling.

If `U` is a `lambda_k` shell and `V` is a `lambda_l` shell, then:

```text
sum_{d:(d,xi) in U}|beta_0(d,xi)|^2
  <=
  4 lambda_k^2 K(U),
```

and similarly for `V`. Therefore:

```text
WOff(U,V)
  <=
  4 lambda_k lambda_l
  (K(U)K(V)Eng(U)Eng(V))^(1/2).
```

Also, using only shell incidences:

```text
WOff(U,V)
  <=
  16 lambda_k^2 lambda_l^2
  D^(-1)
  sum_{xi in Minor_0} N_U(xi)N_V(xi),
```

where:

```text
N_U(xi)=# { d:(d,xi) in U }.
```

Classification:

```text
DeterministicSizeBounds_320:
  STRUCTURAL / EXTRACTION.
```

These are valid ceilings. They are not a proof of `AdmissiblePhiGain_320`.

### D. Why current deterministic `Phi` does not close

If `Phi_{j;k,l}` is chosen from the energy-product ceiling:

```text
Phi_{j;k,l}=D Eng(J_{j,k})Eng(J_{j,l}),
```

then the sum over `k,l>=j` reproduces the Module 311 energy-square ceiling
after the shell decomposition.

If `Phi_{j;k,l}` is chosen from the column-cap ceiling:

```text
Phi_{j;k,l}
  =
  4 lambda_k lambda_l
  (K(J_{j,k})K(J_{j,l})
   Eng(J_{j,k})Eng(J_{j,l}))^(1/2),
```

then the criterion is only as good as the declared column caps
`K_0(lambda_j)`. This is the same threshold tension already recorded in
Module 284: small `K_0` helps the shell budget but large `K_0` is needed for
bad-frequency removal.

If `Phi` uses only:

```text
sum_xi N_U(xi)N_V(xi)
  <=
  min(K(U),K(V)) #U_or_V,
```

then it recovers first-incidence or column-ceiling behavior rather than a
same-frequency pair gain.

Therefore:

```text
CurrentSizeSensitiveClosure_320:
  FALSE / BLOCKED.
```

This blocks only the deterministic size bounds presently available. It does
not disprove a future data-dependent fiber theorem.

### E. What an admissible gain must look like

A genuinely useful `Phi` must improve at least one of the following
quantities uniformly enough to survive the `j,k,l` sums:

```text
weighted column overlap:
  sum_xi C_U(xi)C_V(xi),

unweighted fiber overlap:
  sum_xi N_U(xi)N_V(xi),

energy distribution:
  Eng(J_{j,k}) across k>=j,

or row/column entropy:
  simultaneous concentration of large coefficients in d and xi.
```

Here:

```text
C_U(xi)=sum_{d:(d,xi) in U}|beta_0(d,xi)|^2.
```

Define the open target:

```text
AdmissiblePhiGain_320(P_minor^0):
  prove a same-family cross-shell majorant Phi_{j;k,l} that is stronger than
  the deterministic ceilings and makes at least one of
  ColumnBarrier_320(Phi), SigmaColumnBarrier_320(Phi) equal o_W(1), without
  assuming an endpoint or transfer theorem.
```

Status:

```text
AdmissiblePhiGain_320(P_minor^0):
  OPEN.
```

### F. Selected next target

The criterion exposes the next smaller diagnostic question: can the existing
large-spectrum fibers in `P_minor^0` plausibly satisfy a nontrivial overlap
or entropy gain, or do the current row/column caps still allow complete
same-frequency concentration?

Define:

```text
DataDependentFiberGainAudit_321(P_minor^0):
  audit whether any current row cap, column cap, shell height, energy tail,
  or selection rule in P_minor^0 gives a genuine gain for
  sum_xi N_U(xi)N_V(xi) or sum_xi C_U(xi)C_V(xi) beyond first incidence.
```

Status:

```text
DataDependentFiberGainAudit_321(P_minor^0):
  OPEN next target.
```

## 6. Edge cases

If `J_{j,k}` is empty, its cross-shell rows vanish. This is local vacuity, not
a uniform criterion.

If the lambda grid has only one active shell, the `k,l` sum collapses, but
the same `Phi` criterion remains the relevant test.

If `k` or `l` is much larger than `j`, the improved conversion factor
`(lambda_k lambda_l)^(-2)` must still be summed over all base thresholds
`j<=k,l`.

If `Phi` is proved only for fixed frequency sets, it does not apply to the
data-dependent shells unless a selection theorem is also supplied.

If `Phi` is proved with averaged W-residue, altered major/minor boundaries,
or a different limiting order, it is a transfer theorem, not a same-family
input.

The criterion is for the local `r=2` column-pair route only. It does not prove
the original selected-average problem, the residual cube endpoint, or the
full threshold package.

## 7. Project-map location

The Phase K column branch now reads:

```text
Module 319:
  filters anti-diagonal inputs and selects size-sensitive criteria.

Module 320:
  formulates the exact Phi criterion and shows deterministic size bounds
  still recover current ceilings.
```

The selected next target is:

```text
DataDependentFiberGainAudit_321(P_minor^0).
```

## 8. What remains open

Still open:

```text
DataDependentFiberGainAudit_321(P_minor^0),
AdmissiblePhiGain_320(P_minor^0),
SizeSensitiveMinorKernelCriterion_320 as an estimate,
DirectSignedMinorKernelTheorem_319(P_minor^0),
DataDependentLargeSpectrumGain_319(P_minor^0),
ResidualEightSlotMinorCancellation_319(P_minor^0),
SignedMinorKernelGain_318(P_minor^0),
SignedMinorKernelCombinationTarget_314(P_minor^0),
MajorKernelCorrectionControl_314(P_minor^0),
CenteredFullAntiDiagonalControl_316(P_minor^0),
AntiDiagonalTwoShiftKernelGain_312(P_minor^0),
WeightedColumnSecondMomentTarget_311(P_minor^0),
WeightedColumnPairEnergyTarget_310(P_minor^0),
OffDiagonalSameFrequencyPair_310(lambda_j),
ColumnTailGainTarget_309(r),
ColumnMultiplicityGainTarget_308(r),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ThresholdBudgetP0Closure_284(q,r),
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
ProjectedMajorTarget_3^B,
WProjectedLocalMatch_3^major,
ProjectedModelNeutralityGate_260,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the original selected-average problem.
```

## 9. Forbidden upgrades

Do not cite `SizeSensitiveMinorKernelCriterion_320(P_minor^0)` as a proved
minor-kernel estimate.

Do not cite `PhiCriterion_320(Phi)` without separately proving an admissible
`Phi` in the exact `P_minor^0` family.

Do not treat deterministic energy-product, column-cap, or incidence bounds
as anti-diagonal gains. They recover current ceilings.

Do not drop the diagonal term:

```text
lambda_j^(-2)E2_minor^0(D;R,eta)
```

from `M2_320(j;Phi)`.

Do not drop the base-tail `L_j`, shell-sum `H_j`, lambda-conversion factors,
W-residue convention, dyadic shell, or limiting order.

Do not hide an endpoint, projected-major theorem, column-barrier closure, or
selector transfer theorem inside `Phi`.

## 10. Next target

The next target is:

```text
Module 321:
  DataDependentFiberGainAudit_321(P_minor^0).
```

It should audit whether the current `P_minor^0` row caps, column caps,
shell-height restrictions, energy tails, and selection rules imply any
nontrivial bound for the weighted or unweighted column-overlap sums that
would produce an admissible `Phi`.
