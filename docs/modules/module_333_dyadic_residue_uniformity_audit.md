# Module 333: Dyadic residue uniformity audit for one-prime compatibility rows

## 1. Precise theorem / claim being advanced

Module 332 showed that one-prime compatibility conditions split into a
kernel `t`-fiber row and a dyadic shift projection row:

```text
pi_d(C) subset F_p^2,
d=(d_1,d_2).
```

This module audits the dyadic part.

Define:

```text
DyadicResidueUniformityAudit_333(P_minor^0).
```

Verdict:

```text
DyadicResidueUniformityAudit_333(P_minor^0):
  STRUCTURAL / EXTRACTION.

BareDyadicResidueCount_333:
  STRUCTURAL / EXTRACTION.

FixedPrimeDyadicSaving_333:
  STRUCTURAL / EXTRACTION.

UniformPrimeRangeCriterion_333:
  CONDITIONAL.

OffDiagonalResidueRemoval_333:
  STRUCTURAL / EXTRACTION.

MaskedDyadicResidueUniformity_333:
  OPEN.

WeightedDyadicProjectionRow_333:
  OPEN.

CurrentDyadicResidueClosure_333:
  FALSE / BLOCKED.

ExactPartitionCoarseningAudit_334(P_minor^0):
  OPEN next target.
```

The audit records the elementary unweighted residue count for the two-sided
dyadic shell. It also shows why that count does not prove the weighted
partition row: the target still contains the localized kernel, data-dependent
threshold masks, finite-prime cutoff, and exact W-limit order.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The bare dyadic count is deterministic arithmetic of intervals modulo a
prime. The weighted dyadic projection row remains open.

This module proves no kernel-weighted partition count, no mask residue
uniformity, no kernel residue uniformity, no multi-prime CRT product estimate,
no finite-prime tail removal, no signed local-model insertion, no threshold
closure, no `PhaseKernelBound_273^0`, no residual cube endpoint, no selector
transfer, and no statement about the original selected-average problem.

## 3. Definitions and variables

Work in:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
N^{delta_D}<=D<=N^{1-delta_D},
2D<=N/16,
D<|d|<=2D.
```

The two-sided integer dyadic shell is:

```text
S_D={d in Z : D<|d|<=2D}.
```

Write:

```text
S=#S_D.
```

Then:

```text
S=2D+O(1)
```

with the harmless integer-rounding convention inherited from Module 278.

For a prime `p>w`, let:

```text
n_a(p)=#{d in S_D : d=a mod p}.
```

For an affine subspace:

```text
E subset F_p^2,
codim(E)=s_d in {0,1,2},
```

define the unweighted projection count:

```text
N_D(E;p)
  =
  #{(d_1,d_2) in S_D^2 : (d_1,d_2) mod p in E}.
```

The off-diagonal count is:

```text
N_D^off(E;p)
  =
  #{(d_1,d_2) in S_D^2 :
      d_1 != d_2,
      (d_1,d_2) mod p in E}.
```

The weighted projection row left by Modules 331 and 332 has schematic form:

```text
W_D(E;p;U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    1_{(d_1,d_2) mod p in E}
    H_{U,V}(d_1,d_2),
```

where:

```text
H_{U,V}(d_1,d_2)
  =
  E_t |K_{U,V}^0(d_1,d_2;t)|
      1_{t mod p in C_t(d_1,d_2)}
```

or the corresponding no-`t` condition if the compatibility class has
`s_t=0`.

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 278, 283, 331, and 332,
elementary interval counting modulo p,
and the two-sided dyadic shift shell of P_minor^0.
```

It does not assume:

```text
WeightedDyadicProjectionRow_333,
MaskedDyadicResidueUniformity_333,
UniformPrimeRangeCriterion_333 as a proved estimate,
ExactPartitionCoarseningAudit_334,
KernelResidueMassCriterion_332 as a proved estimate,
AbsoluteMinorKernelResidueUniformity_332,
KernelWeightedPartitionClassCounting_331,
MaskResidueUniformity_331,
PartitionClassCountingRows_330,
StructuralRankUniformityRows_330,
MultiPrimeCoverMomentRows_330,
FinitePrimeTailRows_330,
KernelWeightedMobiusMomentCriterion_330 as a proved estimate,
SharpCoverSmallness_328,
KernelWeightedSharpCoverCriterion_328 as a proved estimate,
FullCoverLoadSmallness_327,
FullCoverRankUniformity_327,
KernelWeightedCoverRows_327,
FullCoverCollisionRows_326,
StratifiedGenericRemainderRows_326,
SignedLocalModelInsertion_326,
ResidualEightSlotMinorCancellation_319,
AdmissiblePhiGain_320,
FiberOverlapGainTarget_321,
SignedMinorKernelGain_318,
AntiDiagonalTwoShiftKernelGain_312,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
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

### A. Bare residue counts in one shift variable

For each residue `a mod p`, the two intervals:

```text
D<d<=2D,
-2D<=d<-D
```

each contribute:

```text
D/p + O(1)
```

points in the residue class `a`. Therefore:

```text
n_a(p)=S/p+O(1),
```

uniformly in `a`.

Classification:

```text
BareDyadicResidueCount_333:
  STRUCTURAL / EXTRACTION.
```

This is only an unweighted count. It contains no information about
`H_{U,V}(d_1,d_2)`.

### B. Affine subspaces in two shift variables

For an affine subspace `E subset F_p^2` of codimension `s_d`, the full-residue
benchmark is:

```text
|E|/p^2=p^(-s_d).
```

Using `n_a(p)=S/p+O(1)`:

```text
N_D(E;p)
  =
  p^(-s_d) S^2
  +
  O_E(S p + p^2).
```

Since all one-prime partition rows have dimension at most two and bounded
complexity, the implicit constant is absolute for the eight-slot family.

Equivalently:

```text
N_D(E;p)/S^2
  =
  p^(-s_d)
  +
  O(p/D)
  +
  O(p^2/D^2).
```

For fixed `p` and `D->infinity`, this gives the expected unweighted dyadic
saving.

Classification:

```text
FixedPrimeDyadicSaving_333:
  STRUCTURAL / EXTRACTION.
```

This fixed-prime statement is not the weighted row and is not uniform over
all possible finite-prime cutoffs.

### C. Uniform finite-prime range criterion

The bare count is useful over a finite prime range only if the boundary
errors stay smaller than the intended saving. A sufficient bookkeeping
condition is:

```text
Y(N,w)/D -> 0
```

in the declared limit order, or a sharper weighted version proving that:

```text
sum_{w<p<=Y(N,w)}
  relevant_weight(p)
  (p/D + p^2/D^2)
```

is negligible in the Module 330 cover-moment sum.

Classification:

```text
UniformPrimeRangeCriterion_333:
  CONDITIONAL.
```

No such finite-prime range or weighted error summability is supplied here.

### D. Off-diagonal removal

The off-diagonal condition removes:

```text
#{d in S_D : (d,d) mod p in E}
```

pairs. This is at most `S`. Thus:

```text
N_D^off(E;p)=N_D(E;p)+O(S).
```

Relative to the unweighted pair shell this is:

```text
O(1/D).
```

Classification:

```text
OffDiagonalResidueRemoval_333:
  STRUCTURAL / EXTRACTION.
```

This is an unweighted off-diagonal statement. In the actual row, the
diagonal removal is already imposed, but weighted diagonal concentration
cannot be controlled by this count alone.

### E. Finite-cyclic wrap and W-residue convention

The dyadic shell is an integer shell of representatives with:

```text
2D<=N/16.
```

Thus the integer representatives of `d` do not wrap around the cyclic group
when merely counted as shifts in the declared shell. The local model still
uses cyclic shifts in `G_N`; this module does not export the count to an
interval model.

The fixed W-residue `b mod W` is part of `P_minor^0`. The primes in this
audit satisfy:

```text
p>w,
```

so they are not W-primes. Large-prime coincidences are local correlation
conditions and are not removed by the W-residue convention.

### F. Why the weighted row remains open

The target row is not:

```text
N_D^off(E;p).
```

It is:

```text
W_D(E;p;U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    1_{(d_1,d_2) mod p in E}
    H_{U,V}(d_1,d_2).
```

The function `H_{U,V}` contains:

```text
the absolute localized kernel,
the t-fiber condition,
the threshold masks U,V,
and the data-dependent shell selection.
```

The bare dyadic count would imply the desired residue saving only under a
same-family weighted equidistribution statement:

```text
WeightedDyadicProjectionRow_333:

W_D(E;p;U,V)
  <=
  (p^(-s_d)+err_D(E,p,N,w,U,V))
  D^(-1) sum_{d_1 != d_2} H_{U,V}(d_1,d_2),
```

with `err_D` summable or absorbable in the Module 330 limit order.

Classification:

```text
WeightedDyadicProjectionRow_333:
  OPEN.

MaskedDyadicResidueUniformity_333:
  OPEN.
```

The project currently has no theorem preventing `U,V` or the absolute kernel
mass from concentrating on a small collection of `d`-residue classes.

### G. Current closure verdict

The current ledger now has:

```text
bare two-sided dyadic residue counts,
fixed-prime unweighted dyadic savings,
unweighted off-diagonal removal,
and a finite-prime range criterion.
```

It does not have:

```text
weighted dyadic projection uniformity,
mask residue uniformity,
absolute kernel residue uniformity,
finite-prime range summability,
coarsening inclusion-exclusion estimates,
multi-prime CRT/mask compatibility,
or finite-prime tail control.
```

Therefore:

```text
CurrentDyadicResidueClosure_333:
  FALSE / BLOCKED.
```

The next target is the exact partition/coarsening row, because even if the
equality envelope were controlled, exact partition classes still require
inequalities between distinct blocks or inclusion-exclusion over coarsenings.

## 6. Edge cases and exclusions

- The count `n_a(p)=S/p+O(1)` is unweighted.
- The relative error is harmless for fixed `p` and large `D`, but not
  automatically for `p` approaching the shift scale.
- If `p>D`, many residue classes in the dyadic shell are empty; a `p^{-1}`
  residue-saving slogan is then misleading.
- The off-diagonal removal is small unweighted, but weighted diagonal
  concentration is a separate row.
- W-residue conventions remove primes `<=w` from the model residue class;
  they do not remove large-prime coincidences with `p>w`.
- Cyclic wrap is absent only for the integer shift shell bookkeeping inside
  `P_minor^0`; this is not interval transfer.
- The masks `U,V` and shell membership remain data-dependent.
- A dyadic interval count is not a kernel-weighted partition estimate.
- A conditional finite-prime range criterion is not a theorem.

## 7. Project-map location

This module lies on the Phase K minor-arc branch:

```text
WeightedPairAutocorrelationExpansion_312
  -> MinorKernelRowSplit_314
  -> SignedMinorKernelCombinationVerdict_318
  -> AntiDiagonalNewInputInventory_319
  -> SizeSensitiveMinorKernelCriterion_320
  -> DataDependentFiberGainAudit_321
  -> PlanUpdate_15_Challenge_9_322
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
  -> ExactPartitionCoarseningAudit_334.
```

It is still inside the local model `P_minor^0`. It does not prove
`AntiDiagonalTwoShiftKernelGain_312`, `PhaseKernelBound_273^0`,
`NarrowMinorArc_3^B`, `ResCube_3^sharp`, or the original selected-average
problem.

## 8. What remains open

The next smaller targets are:

```text
1. ExactPartitionCoarseningAudit_334(P_minor^0):
     decide how exact partition inequalities relate to equality envelopes and
     whether coarsening inclusion-exclusion preserves the same weighted row.

2. WeightedDyadicProjectionRow_333:
     prove or reject residue uniformity for the weighted dyadic projection.

3. MaskedDyadicResidueUniformity_333:
     prove or reject residue uniformity after threshold masks U,V are imposed.

4. UniformPrimeRangeCriterion_333:
     choose and prove an admissible finite-prime range or weighted error
     summability for the dyadic residue errors.

5. MultiPrimeCRTMaskAudit_335:
     decide whether one-prime rows can be combined over several primes under
     the same kernel and mask weights.
```

The current cadence after completing this module is:

```text
Latest completed module: 333
Post-Reflective_1 solving count: 152
Long-term-plan count: 146

146 is not divisible by 9, so no plan update is due in this module.
146 is not divisible by 15, so no plan challenge is due in this module.
Next reflective log remains expected around Module 341.
```

## 9. Forbidden upgrades

This module does not prove:

```text
WeightedDyadicProjectionRow_333,
MaskedDyadicResidueUniformity_333,
UniformPrimeRangeCriterion_333 as an estimate,
ExactPartitionCoarseningAudit_334,
KernelResidueMassCriterion_332 as an estimate,
AbsoluteMinorKernelResidueUniformity_332,
KernelWeightedPartitionClassCounting_331,
MaskResidueUniformity_331,
PartitionClassCountingRows_330,
StructuralRankUniformityRows_330,
MultiPrimeCoverMomentRows_330,
FinitePrimeTailRows_330,
KernelWeightedMobiusMomentCriterion_330 as an estimate,
PrimeMobiusSmallness_329,
KernelWeightedMobiusCoverRows_329,
SharpCoverSmallness_328,
KernelWeightedSharpCoverCriterion_328 as an estimate,
FullCoverLoadSmallness_327,
FullCoverRankUniformity_327,
KernelWeightedCoverRows_327,
FullCoverCollisionRows_326,
StratifiedGenericRemainderRows_326,
SignedLocalModelInsertion_326,
ResidualEightSlotMinorCancellation_319,
AdmissiblePhiGain_320,
FiberOverlapGainTarget_321,
SignedMinorKernelGain_318,
AntiDiagonalTwoShiftKernelGain_312,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the all-alpha theorem,
the finite-type theorem unconditionally,
or the original selected-average problem.
```

Do not cite `BareDyadicResidueCount_333` or
`FixedPrimeDyadicSaving_333` as a weighted partition estimate. They are
unweighted dyadic counts only.
