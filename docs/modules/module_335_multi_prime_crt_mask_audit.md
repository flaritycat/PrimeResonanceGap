# Module 335: Multi-prime CRT and mask audit for cover families

## 1. Precise theorem / claim being advanced

Modules 331-334 audited one-prime partition rows. Module 330, however, needs
full-cover families that can involve several primes. This module audits the
passage from one-prime rows to multi-prime rows under the same kernel and
masks.

Define:

```text
MultiPrimeCRTMaskAudit_335(P_minor^0).
```

Verdict:

```text
MultiPrimeCRTMaskAudit_335(P_minor^0):
  STRUCTURAL / EXTRACTION.

DistinctPrimeCRTNormalForm_335:
  STRUCTURAL / EXTRACTION.

RepeatedPrimeConsolidation_335:
  STRUCTURAL / EXTRACTION.

UnweightedCRTBenchmark_335:
  STRUCTURAL / EXTRACTION.

CompositeModulusRangeCriterion_335:
  CONDITIONAL.

WeightedCRTMaskCriterion_335:
  CONDITIONAL.

MaskCRTUniformityRows_335:
  OPEN.

KernelCRTUniformityRows_335:
  OPEN.

PrimeIndependenceShortcut_335:
  FALSE / BLOCKED.

CurrentMultiPrimeCRTClosure_335:
  FALSE / BLOCKED.

FinitePrimeTailCoverAudit_336(P_minor^0):
  OPEN next target.
```

The audit records the exact CRT normal form for distinct primes and the
required weighted composite-modulus criterion. It does not prove that
one-prime weighted estimates multiply under the same localized kernel and
data-dependent masks.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The CRT bookkeeping is exact finite algebra. The weighted CRT/mask rows
remain open.

This module proves no multi-prime cover-moment estimate, no finite-prime tail
control, no mask residue uniformity, no kernel residue uniformity, no signed
local-model insertion, no threshold closure, no `PhaseKernelBound_273^0`, no
residual cube endpoint, no selector transfer, and no statement about the
original selected-average problem.

## 3. Definitions and variables

Work in:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d_i|<=2D,
d_1 != d_2.
```

Use the base variables from Modules 331-332:

```text
b=(t,d_1,d_2),  t=h+k.
```

For a finite set of distinct primes:

```text
P_*={p_1,...,p_m},  w<p_a<=Y,
Q=prod_{a=1}^m p_a,
```

let `C_a subset F_{p_a}^3` be the compatibility condition coming from the
chosen one-prime equality envelope or coarsening at `p_a`.

Define the CRT lift:

```text
C_{P_*}
  =
  { b in (Z/QZ)^3 :
      b mod p_a in C_a for every a }.
```

Let:

```text
E_{P_*} subset (Z/QZ)^2
```

be the projection of `C_{P_*}` to `(d_1,d_2)`. Let `Q_t` be the product of
those primes for which the `t`-fiber is a single residue after fixing the
projected `d`-class. If no prime constrains `t`, set `Q_t=1`.

The multi-prime weighted row has schematic form:

```text
W_{P_*}^{335}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    1_{(d_1,d_2) mod Q in E_{P_*}}
    E_t |K_{U,V}^0(d_1,d_2;t)|
      1_{t mod Q_t in a_{P_*}(d_1,d_2)}.
```

Here `a_{P_*}` is the CRT-combined affine residue condition for `t`, when
`Q_t>1`.

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 327-334,
finite CRT for distinct primes,
and the exact local variables above.
```

It does not assume:

```text
WeightedCRTMaskCriterion_335 as a proved estimate,
MaskCRTUniformityRows_335,
KernelCRTUniformityRows_335,
CompositeModulusRangeCriterion_335 as a proved estimate,
FinitePrimeTailCoverAudit_336,
ExactWeightedPartitionRows_334,
CoarseningWeightedUniformityRows_334,
CoarseningWeightedCriterion_334 as a proved estimate,
WeightedDyadicProjectionRow_333,
MaskedDyadicResidueUniformity_333,
UniformPrimeRangeCriterion_333 as a proved estimate,
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

### A. Distinct-prime CRT normal form

For distinct primes, the simultaneous residue conditions:

```text
b mod p_a in C_a,  a=1,...,m,
```

are equivalent by CRT to one composite-modulus condition:

```text
b mod Q in C_{P_*}.
```

If the one-prime conditions have full-base codimensions `c_a`, then the
full-residue benchmark in `(Z/QZ)^3` has density:

```text
prod_a p_a^(-c_a).
```

Classification:

```text
DistinctPrimeCRTNormalForm_335:
  STRUCTURAL / EXTRACTION.
```

This is full-residue algebra only. It has no kernel, masks, dyadic boundary,
or W-limit estimate in it.

### B. Repeated-prime consolidation

A repeated occurrence of the same prime is not a CRT independence event.
Repeated prime-local pieces must be consolidated into a single one-prime
partition/coarsening condition before CRT is applied.

In the finite product:

```text
Def_Y(S)=prod_{w<p<=Y}(1+delta_{p,S})-1,
```

each prime appears once in the product. If a cover envelope or bookkeeping
family lists the same prime more than once, that is an envelope artifact and
must be merged back into one prime-local row.

Classification:

```text
RepeatedPrimeConsolidation_335:
  STRUCTURAL / EXTRACTION.
```

Treating repeated appearances of the same prime as independent CRT factors is
not allowed.

### C. Unweighted composite-modulus benchmark

Let `E subset (Z/QZ)^2` be an affine projected shift condition of residue
density `delta_E=|E|/Q^2`. For the two-sided dyadic shell `S_D`, the same
interval count used in Module 333 gives:

```text
#{(d_1,d_2) in S_D^2 :
    (d_1,d_2) mod Q in E}
  =
  delta_E S^2
  +
  O(S Q + Q^2).
```

Thus:

```text
relative error = O(Q/D)+O(Q^2/D^2).
```

Classification:

```text
UnweightedCRTBenchmark_335:
  STRUCTURAL / EXTRACTION.
```

For fixed `Q` and `D->infinity`, this gives the expected unweighted CRT
benchmark. It is not a weighted row and is not uniform over unrestricted
finite-prime products.

### D. Composite-modulus range criterion

The unweighted CRT benchmark is useful for a finite prime product only if:

```text
Q(P_*)/D -> 0
```

or if the weighted sum of composite-modulus boundary errors is proved
negligible:

```text
sum_{P_*}
  Weight(P_*)
  (Q(P_*)/D + Q(P_*)^2/D^2)
  =
  o_W(1),
```

in the declared limit order and with the same cover-family restrictions.

Classification:

```text
CompositeModulusRangeCriterion_335:
  CONDITIONAL.
```

No such range theorem or weighted summability theorem is supplied here.

### E. Weighted CRT/mask criterion

The criterion needed for the Module 330 cover moment is a same-family
weighted composite-modulus estimate:

```text
WeightedCRTMaskCriterion_335:

For every admissible distinct-prime cover family P_* and its CRT lift
C_{P_*},

W_{P_*}^{335}(U,V)
  <=
  (expected_CRT_density(P_*)+err_CRT(P_*,N,w,U,V))
  D^(-1) sum_{d_1 != d_2}
    E_t |K_{U,V}^0(d_1,d_2;t)|,
```

with errors summable after the prime-local weights from Module 329 and the
coarsening weights from Module 334 are inserted.

Classification:

```text
WeightedCRTMaskCriterion_335:
  CONDITIONAL.

MaskCRTUniformityRows_335:
  OPEN.

KernelCRTUniformityRows_335:
  OPEN.
```

This criterion is not proved by CRT alone.

### F. Why one-prime estimates do not multiply automatically

Even if one-prime weighted rows were available, the multi-prime row has:

```text
one shared absolute kernel |K_{U,V}^0(d_1,d_2;t)|,
one shared pair of masks U,V,
one shared dyadic pair (d_1,d_2),
and one shared t-variable.
```

The masks and kernel can concentrate on a residue class modulo the product
`Q` even if no one-prime diagnostic rules it out. A theorem for every prime
separately does not automatically imply a theorem for the composite modulus
unless it is uniform under conditioning or is stated directly at modulus `Q`.

Classification:

```text
PrimeIndependenceShortcut_335:
  FALSE / BLOCKED.
```

This blocks the shortcut:

```text
one-prime row for each p  =>  product row for P_*.
```

The missing input is a same-family CRT/mask theorem, not another formal CRT
identity.

### G. Current closure verdict

The current ledger now has:

```text
distinct-prime CRT normal form,
repeated-prime consolidation,
an unweighted composite-modulus benchmark,
and conditional weighted CRT/mask criterion.
```

It does not have:

```text
weighted CRT/mask uniformity,
kernel residue uniformity at composite moduli,
masked dyadic projection uniformity at composite moduli,
finite-prime product range control,
or finite-prime tail control.
```

Therefore:

```text
CurrentMultiPrimeCRTClosure_335:
  FALSE / BLOCKED.
```

The next target is the finite-prime tail audit. The CRT obstruction becomes
more severe when the product modulus `Q(P_*)` grows, so the project must
separate a finite, controlled prime range from the tail above it.

## 6. Edge cases and exclusions

- CRT applies only to distinct primes. Repeated same-prime pieces must be
  consolidated first.
- Full-residue CRT density is not a kernel-weighted estimate.
- The relevant range condition is about the composite modulus `Q`, not only
  each individual prime.
- A one-prime weighted estimate does not automatically tensor through shared
  data-dependent masks.
- Absolute values block signed cancellation between prime factors unless a
  separate signed row is proved before the absolute envelope is formed.
- Composite-modulus residue classes can be sparse in the dyadic shell even
  when each one-prime residue count is harmless.
- The finite-prime cutoff `Y` and the cover-family size affect the size of
  `Q(P_*)`.
- The masks `U,V` and shell membership remain data-dependent.
- The model selector is not the actual sharp moving selector.
- The local W-cyclic prime-only model is not the original full-gap problem.
- A CRT normal form is not an analytic proof.

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
  -> ExactPartitionCoarseningAudit_334
  -> MultiPrimeCRTMaskAudit_335
  -> FinitePrimeTailCoverAudit_336.
```

It is still inside the local model `P_minor^0`. It does not prove
`AntiDiagonalTwoShiftKernelGain_312`, `PhaseKernelBound_273^0`,
`NarrowMinorArc_3^B`, `ResCube_3^sharp`, or the original selected-average
problem.

## 8. What remains open

The next smaller targets are:

```text
1. FinitePrimeTailCoverAudit_336(P_minor^0):
     decide how to choose a finite prime cutoff and how to separate the tail
     above it without assuming the cover moment.

2. WeightedCRTMaskCriterion_335:
     prove or reject composite-modulus weighted CRT uniformity under the same
     kernel and masks.

3. CompositeModulusRangeCriterion_335:
     prove or reject a range/summability theorem for Q(P_*) boundary errors.

4. KernelCRTUniformityRows_335 and MaskCRTUniformityRows_335:
     prove or reject composite-modulus uniformity for the absolute kernel and
     data-dependent masks.

5. FinitePrimeTailRows_330:
     prove or reject tail control after the finite-prime cutoff.
```

The current cadence after completing this module is:

```text
Latest completed module: 335
Post-Reflective_1 solving count: 154
Long-term-plan count: 148

148 is not divisible by 9, so no plan update is due in this module.
148 is not divisible by 15, so no plan challenge is due in this module.
Next reflective log remains expected around Module 341.
```

## 9. Forbidden upgrades

This module does not prove:

```text
WeightedCRTMaskCriterion_335 as an estimate,
MaskCRTUniformityRows_335,
KernelCRTUniformityRows_335,
CompositeModulusRangeCriterion_335 as an estimate,
FinitePrimeTailCoverAudit_336,
ExactWeightedPartitionRows_334,
CoarseningWeightedUniformityRows_334,
CoarseningWeightedCriterion_334 as an estimate,
WeightedDyadicProjectionRow_333,
MaskedDyadicResidueUniformity_333,
UniformPrimeRangeCriterion_333 as an estimate,
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

Do not cite `DistinctPrimeCRTNormalForm_335` or
`UnweightedCRTBenchmark_335` as weighted CRT/mask uniformity. They are
structural and unweighted only.
