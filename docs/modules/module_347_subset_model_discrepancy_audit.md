# Module 347: Subset model discrepancy audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

Module 346 reduced signed local-model insertion to weighted subset
physical-minus-model discrepancies:

```text
Err_S^{346}(U,V)
  =
  Phys_S^{346}(U,V)-Mod_S^{346}(U,V).
```

This module audits those subset rows. It asks which rows are exact zeros by
the nonzero minor-kernel average, which rows remain genuine weighted
local-model insertion rows, and where the next smaller obstruction begins.

Define:

```text
SubsetModelDiscrepancyAudit_347(P_minor^0).
```

Verdict:

```text
SubsetModelDiscrepancyAudit_347(P_minor^0):
  STRUCTURAL / EXTRACTION.

OneSidedSubsetDiscrepancyZero_347(P_minor^0):
  PROVEN inside P_minor^0.

TwoSidedActiveSubsetCatalog_347:
  STRUCTURAL / EXTRACTION.

TwoSidedActiveSubsetDiscrepancyRows_347:
  OPEN.

AllSubsetDiscrepanciesClose_347:
  FALSE / BLOCKED.

MinimalActivePairDiscrepancyAudit_348(P_minor^0):
  OPEN next target.
```

The useful local fact is that every subset row invisible to at least one of
the two kernel directions is exactly zero inside the current cyclic
nonzero-frequency model. The remaining rows are precisely the subsets that
touch both the `h`-dependent first-block slots and the `k`-dependent
second-block slots.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The module contains one exact local zero statement inside `P_minor^0`. It
proves no `SignedLocalModelInsertion_326`, no `LocalModelInsertion_325`, no
`TwoSidedActiveSubsetDiscrepancyRows_347`, no
`DataDependentKernelSelectionRows_325`, no `PhaseKernelBound_273^0`, no
residual cube endpoint, no selector transfer, and no statement about the
original selected-average problem.

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d_i|<=2D,
d_1 != d_2.
```

Use the eight slots:

```text
L_1=x+d_1,      L_2=x,
L_3=x+h+d_1,    L_4=x+h,
L_5=y+d_2,      L_6=y,
L_7=y+k+d_2,    L_8=y+k,
z=(x,y,h,k,d_1,d_2),
t=h+k,
Lambda_8={1,2,3,4,5,6,7,8}.
```

Define the `h`-active and `k`-active slot sets:

```text
H_*={3,4},
K_*={7,8}.
```

For `S subset Lambda_8`, inherit from Module 346:

```text
Nu_S^{347}(z)
  =
  prod_{i in S} nu_0(L_i(z)),

Theta_{w,S}^{8,min}(z)
  =
  prod_{p>w}
    (1-1/p)^(-|S|)
    (1-r_p(S;z)/p).
```

For threshold-localized masks:

```text
K_{U,V}^0(d_1,d_2;t)
  =
  sum_{xi in Minor_0(R,eta)}
    U(d_1,xi)V(d_2,xi)e_N(xi t).
```

The subset rows are:

```text
Phys_S^{347}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      K_{U,V}^0(d_1,d_2;h+k)
      Nu_S^{347}(z),

Mod_S^{347}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      K_{U,V}^0(d_1,d_2;h+k)
      Theta_{w,S}^{8,min}(z),

Err_S^{347}(U,V)
  =
  Phys_S^{347}(U,V)-Mod_S^{347}(U,V).
```

Call `S` one-sided or kernel-invisible if:

```text
S cap H_* = emptyset
```

or:

```text
S cap K_* = emptyset.
```

Call `S` two-sided active if:

```text
S cap H_* != emptyset
and
S cap K_* != emptyset.
```

There are:

```text
2^8 - 2^6 - 2^6 + 2^4 = 144
```

two-sided active subsets, and:

```text
256 - 144 = 112
```

one-sided or kernel-invisible subsets.

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 323-346,
the nonzero minor-frequency support of K_{U,V}^0,
and the convention that U(d,xi), V(d,xi) do not depend on x,y,h,k.
```

It does not assume:

```text
SignedLocalModelInsertion_326,
LocalModelInsertion_325,
Err_S^{346}(U,V)=o_W(1) for nonempty S,
DataDependentKernelSelectionRows_325,
GenericNoncollisionRow_325,
StructuralDiagonalRows_325,
FinitePrimeCollisionLoadRows_325,
OverflowRows_325,
FullCoverCollisionRows_326,
StratifiedGenericRemainderRows_326,
KernelWeightedMobiusMomentCriterion_330,
WeightedCRTMaskCriterion_335,
KernelWeightedDivisorWindowCriterion_337,
LowEnvelopeMassRows_338,
ExactZeroWeightedRows_339,
InternalZeroKernelRows_339,
CrossZeroKernelRows_339,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
selector transfer,
the all-alpha theorem,
the finite-type theorem unconditionally,
or the original selected-average problem.
```

## 5. Proof / disproof / reduction

### A. Kernel invisibility in one direction

Fix `d_1,d_2` and a nonzero frequency `xi`. If a factor `A(z)` is independent
of `h`, then:

```text
E_{x,y,h,k} A(z)e_N(xi(h+k))
  =
  E_{x,y,k} A(x,y,k,d_1,d_2)e_N(xi k)
    E_h e_N(xi h)
  =
  0.
```

Likewise, if `A(z)` is independent of `k`, then:

```text
E_{x,y,h,k} A(z)e_N(xi(h+k))=0.
```

The masks `U,V` depend on `(d_i,xi)` and not on `h,k`, so the same argument
applies term-by-term inside `K_{U,V}^0`.

### B. Exact zero for one-sided subset discrepancies

If:

```text
S cap H_* = emptyset,
```

then neither `Nu_S^{347}` nor `Theta_{w,S}^{8,min}` depends on `h`. Hence:

```text
Phys_S^{347}(U,V)=0,
Mod_S^{347}(U,V)=0,
Err_S^{347}(U,V)=0.
```

If:

```text
S cap K_* = emptyset,
```

then neither factor depends on `k`, and the same conclusion holds.

Therefore:

```text
OneSidedSubsetDiscrepancyZero_347(P_minor^0):
  PROVEN inside P_minor^0.
```

This is an exact local cyclic Fourier statement. It does not transfer to
boundary-cut, selector-changed, or zero-frequency variants.

### C. Two-sided active subset catalog

The only subset rows not killed by the preceding argument are those with:

```text
S cap {3,4} != emptyset,
S cap {7,8} != emptyset.
```

These are the two-sided active subsets. The minimal such rows have size two:

```text
S in {{3,7},{3,8},{4,7},{4,8}}.
```

Larger active subsets are obtained by adjoining any subset of the remaining
six slots while retaining at least one label from each active direction.

Classification:

```text
TwoSidedActiveSubsetCatalog_347:
  STRUCTURAL / EXTRACTION.
```

This catalog is not an estimate for those rows.

### D. Why the active rows remain open

For a two-sided active subset, both the physical factor and the local model
can depend on `h` and `k`. The nonzero kernel average no longer supplies a
free zero:

```text
K_{U,V}^0(d_1,d_2;h+k)
```

sees exactly the sum of the two active directions.

The remaining target is:

```text
Err_S^{347}(U,V)=o_W(1)
```

for every two-sided active `S`, in the same `P_minor^0` family and with the
same data-dependent threshold masks. Current inputs do not prove this.

Therefore:

```text
TwoSidedActiveSubsetDiscrepancyRows_347:
  OPEN.
```

### E. Closure verdict

Module 346 showed that signed insertion would follow from control of all
subset discrepancies. Module 347 removes the one-sided subset rows exactly,
but leaves the 144 two-sided active rows.

Thus:

```text
AllSubsetDiscrepanciesClose_347:
  FALSE / BLOCKED.
```

The signed local-model insertion row remains open because the active
two-direction discrepancies have not been estimated.

### F. Next smaller target

The smallest active subsets are:

```text
{3,7}, {3,8}, {4,7}, {4,8}.
```

They test the core question without extra passive slots: can a two-point
physical product in the `h` and `k` directions be inserted into its
collision-sensitive local model under the same threshold-localized kernel?

The next module should audit:

```text
MinimalActivePairDiscrepancyAudit_348(P_minor^0).
```

This is still a feasibility audit unless a complete same-family weighted
estimate is supplied.

## 6. Edge cases and exclusions

### Zero-frequency leakage

The exact one-sided zero uses `xi != 0`. If a kernel includes the zero
frequency, the argument fails.

### Data-dependent masks

The argument permits masks depending on `(d_i,xi)`. If future masks depend on
`x,y,h,k`, then the one-sided independence proof must be redone.

### Boundary or cutoff restrictions

The exact zero is cyclic and full-average inside `P_minor^0`. Boundary cuts,
lift restrictions, selector-transfer errors, or noncyclic truncations can
introduce `h` or `k` dependence and require separate transfer rows.

### Structural diagonals

One-sided exact zeros do not control structural diagonal rows among two-sided
active subsets. Diagonal constraints can create variable restrictions that
must be budgeted separately.

### Generic versus collision-sensitive model

This module keeps the collision-sensitive `Theta_{w,S}^{8,min}`. It does not
replace it by a generic size-only model.

### Selector and endpoint transfer

Everything here is internal to `P_minor^0`. It does not transfer to the
actual sharp moving selector, full gap averages, the residual cube endpoint,
or the original selected-average problem.

## 7. Where it fits in the project map

```text
Phase K
  -> ResidualEightSlotMinorExpansion_323
  -> CollisionDiagonalStrataAudit_324
  -> GenericCollisionLocalModelSplit_325
  -> SignedInclusionExclusionMinorAudit_326
  -> FullCoverClusterAudit_327
  -> FullCoverLoadCriterion_328
  -> PrimePartitionMobiusAudit_329
  -> PrimePartitionCoverMomentCriterion_330
  -> PartitionClassCountingAudit_331
  -> KernelFiberPartitionAudit_332
  -> DyadicResidueUniformityAudit_333
  -> ExactPartitionCoarseningAudit_334
  -> MultiPrimeCRTMaskAudit_335
  -> FinitePrimeTailCoverAudit_336
  -> HighPrimeDivisorWindowAudit_337
  -> LowHighTailCouplingAudit_338
  -> ExactZeroTailDiagonalAudit_339
  -> CoverMomentRouteVerdict_340
  -> Reflective_5
  -> LowEnvelopeMassPrototype_342
  -> InternalZeroKernelAudit_343
  -> CrossZeroKernelAudit_344
  -> PhaseKPostCoverBranchDecision_345
  -> SignedLocalModelInsertionFeasibility_346
  -> SubsetModelDiscrepancyAudit_347.
```

This module narrows the Module 346 subset-discrepancy criterion. It does not
prove `SignedLocalModelInsertion_326`, `PhaseKernelBound_273^0`,
`NarrowMinorArc_3^B`, `ResCube_3^sharp`, or the original selected-average
problem.

## 8. What remains open

Still open:

```text
MinimalActivePairDiscrepancyAudit_348(P_minor^0),
TwoSidedActiveSubsetDiscrepancyRows_347,
SignedLocalModelInsertion_326,
LocalModelInsertion_325,
DataDependentKernelSelectionRows_325,
GenericNoncollisionRow_325,
StructuralDiagonalRows_325,
FinitePrimeCollisionLoadRows_325,
OverflowRows_325,
FullCoverCollisionRows_326,
StratifiedGenericRemainderRows_326,
KernelWeightedMobiusMomentCriterion_330,
WeightedCRTMaskCriterion_335,
KernelWeightedDivisorWindowCriterion_337,
LowEnvelopeMassRows_338,
ExactZeroWeightedRows_339,
InternalZeroKernelRows_339,
CrossZeroKernelRows_339,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the all-alpha theorem,
the finite-type theorem unconditionally,
and the original selected-average problem.
```

Next target:

```text
MinimalActivePairDiscrepancyAudit_348(P_minor^0).
```

## Red flags / forbidden upgrades

Do not cite `OneSidedSubsetDiscrepancyZero_347` outside the full cyclic
nonzero-frequency `P_minor^0` average.

Do not cite the one-sided zero as signed local-model insertion.

Do not treat two-sided active subsets as controlled by the same argument.

Do not replace the active subset physical rows by local models without a
same-family weighted discrepancy theorem.

Do not use first-moment Hardy-Littlewood, pair-BDH, proper-support signed
cancellation, or generic local density as a substitute for active subset
discrepancy estimates.

Do not use `SignedLocalModelInsertion_326`, `LocalModelInsertion_325`,
`PhaseKernelBound_273^0`, `ResCube_3^sharp`, `CPC_3^sharp`,
`RBDH_pair_short`, or `AU^3` as assumptions.

Do not transfer this local zero statement to the actual sharp moving selector
or to the original selected-average problem.
