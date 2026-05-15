# Module 336: Finite-prime tail cover audit

## 1. Precise theorem / claim being advanced

Modules 328 and 330 introduced finite prime cutoffs `Y` for the sharp-cover
and Mobius-cover functionals. Module 335 audited the finite multi-prime CRT
and mask step for primes `p<=Y`. This module audits the complementary step:
what is required to remove the cutoff or choose `Y=Y(N,w)` without assuming
the cover moment itself.

Define:

```text
FinitePrimeTailCoverAudit_336(P_minor^0).
```

Verdict:

```text
FinitePrimeTailCoverAudit_336(P_minor^0):
  STRUCTURAL / EXTRACTION.

FiniteCutoffDifferenceIdentity_336:
  STRUCTURAL / EXTRACTION.

TailCoverFunctional_336:
  STRUCTURAL / EXTRACTION.

TuplePrimeDivisorCeiling_336:
  STRUCTURAL / EXTRACTION.

CutoffWindowCriterion_336:
  CONDITIONAL.

TailUniformityRows_336:
  OPEN.

LowHighCoverCouplingRows_336:
  OPEN.

ExactZeroDiagonalRows_336:
  OPEN.

TailOnlyShortcut_336:
  FALSE / BLOCKED.

CurrentFinitePrimeTailClosure_336:
  FALSE / BLOCKED.

HighPrimeDivisorWindowAudit_337(P_minor^0):
  OPEN next target.
```

The module gives the exact finite-cutoff difference identity, defines the
tail functional needed by `FinitePrimeTailRows_330`, records a tuple-level
prime-divisor ceiling for nonzero integer lifts, and identifies the cutoff
window obstruction. It does not prove a same-family weighted tail estimate.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The cutoff algebra and tuple divisor ceiling are structural diagnostics. The
weighted tail row, low-high coupling row, and cutoff window remain open.

This module proves no `FinitePrimeTailRows_330`, no
`MultiPrimeCoverMomentRows_330`, no `WeightedCRTMaskCriterion_335`, no
`KernelWeightedMobiusMomentCriterion_330`, no `SharpCoverSmallness_328`, no
`PhaseKernelBound_273^0`, no residual cube endpoint, no selector transfer,
and no statement about the original selected-average problem.

## 3. Definitions and variables

Work in:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d_i|<=2D,
d_1 != d_2.
```

Use the eight residual labels:

```text
Lambda_8={1,...,8},
L_i=L_i(x,y,h,k,d_1,d_2),
Delta_{ij}=L_i-L_j.
```

For a finite cutoff `Y>w`, recall:

```text
Def_Y(S)
  =
  prod_{w<p<=Y} (1+delta_{p,S}) - 1,

m_{Lambda_8}(Def_Y)
  =
  sum_{S subset Lambda_8} (-1)^(8-|S|) Def_Y(S).
```

For `Y<Z`, define the high-prime interval defect:

```text
Def_{Y,Z}(S)
  =
  prod_{Y<p<=Z} (1+delta_{p,S}) - 1.
```

Let a finite cover family be:

```text
F=((p_1,T_1),...,(p_m,T_m)),
```

with:

```text
w<p_a<=Z,
empty != T_a subset Lambda_8,
union_a T_a = Lambda_8.
```

Write:

```text
maxp(F)=max_a p_a.
```

Use the Module 330 pointwise envelope:

```text
Weight(F)
  =
  prod_a C_8 p_a^(-a_{p_a}(T_a)),

a_p(T)=1+|T|-b_max(T,p),
```

with the convention that `mu_p(T)=0` when `b_max(T,p)<=1`.

For a threshold-localized mask pair `U,V`, define the finite high-prime tail
functional:

```text
TailCover_{Y,Z}^{336}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      |K_{U,V}^0(d_1,d_2;h+k)|
      sum_{F full cover, maxp(F)>Y, p_a<=Z}
        1_{E(F)} Weight(F).
```

Here `E(F)` is the same exact compatibility event as in Module 330. The
condition `maxp(F)>Y` means at least one prime in the cover family lies above
the finite cutoff being removed.

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 327-335,
finite cutoff product algebra,
finite Mobius expansion at cutoffs Y<Z,
and elementary integer prime-divisor counting after a declared lift.
```

It does not assume:

```text
TailUniformityRows_336,
LowHighCoverCouplingRows_336,
CutoffWindowCriterion_336 as a proved estimate,
HighPrimeDivisorWindowAudit_337,
WeightedCRTMaskCriterion_335 as a proved estimate,
MaskCRTUniformityRows_335,
KernelCRTUniformityRows_335,
CompositeModulusRangeCriterion_335 as a proved estimate,
ExactWeightedPartitionRows_334,
CoarseningWeightedUniformityRows_334,
WeightedDyadicProjectionRow_333,
MaskedDyadicResidueUniformity_333,
KernelResidueMassCriterion_332 as a proved estimate,
AbsoluteMinorKernelResidueUniformity_332,
KernelWeightedPartitionClassCounting_331,
MaskResidueUniformity_331,
PartitionClassCountingRows_330,
StructuralRankUniformityRows_330,
MultiPrimeCoverMomentRows_330,
FinitePrimeTailRows_330,
KernelWeightedMobiusMomentCriterion_330 as a proved estimate,
PrimeMobiusSmallness_329,
KernelWeightedMobiusCoverRows_329,
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

### A. Finite cutoff difference identity

For cutoffs `w<Y<Z`, the finite products satisfy:

```text
1+Def_Z(S)
  =
  (1+Def_Y(S))(1+Def_{Y,Z}(S)).
```

Therefore:

```text
Def_Z(S)-Def_Y(S)
  =
  (1+Def_Y(S)) Def_{Y,Z}(S).
```

Equivalently, after expanding into prime-local pieces and applying the top
Mobius coefficient:

```text
m_{Lambda_8}(Def_Z)-m_{Lambda_8}(Def_Y)
```

is exactly the sum of finite cover-family terms in which at least one prime
lies in `(Y,Z]`.

Classification:

```text
FiniteCutoffDifferenceIdentity_336:
  STRUCTURAL / EXTRACTION.
```

This identity is finite algebra. It is not a convergence theorem as
`Z->infinity`.

### B. Tail cover functional

The weighted version of the cutoff difference is bounded by:

```text
TailCover_{Y,Z}^{336}(U,V).
```

A usable finite-prime tail row would require a cutoff choice `Y=Y(N,w)` such
that, for every admissible threshold-localized `U,V`,

```text
lim_{w -> infinity} limsup_{N -> infinity}
  sup_{Z>=Y(N,w)}
    TailCover_{Y(N,w),Z}^{336}(U,V)
  =
  0.
```

Classification:

```text
TailCoverFunctional_336:
  STRUCTURAL / EXTRACTION.

TailUniformityRows_336:
  OPEN.
```

The supremum over `Z` is included because removing the cutoff must not depend
on a hidden final upper prime cutoff.

### C. Tuple-level prime-divisor ceiling

Fix an integer lift of the label differences. For a nonzero integer `A`,

```text
sum_{p>Y, p|A} 1/p
  <=
  log(2+|A|) / (Y log Y)
```

up to an absolute harmless constant for `Y>=2`.

Reason: if `p_1,...,p_m` are distinct primes greater than `Y` dividing
`A`, then:

```text
Y^m <= prod_j p_j <= |A|,
```

so `m <= log(2+|A|)/log Y`, and `sum_j 1/p_j <= m/Y`.

Apply this to the nonzero lifted differences `Delta_{ij}`. Define:

```text
DivTail_Y(z)
  =
  sum_{1<=i<j<=8}
    sum_{p>Y, p|Delta_{ij}(z), Delta_{ij}(z) != 0} 1/p.
```

Then:

```text
DivTail_Y(z)
  <=
  C_8 log M(z) / (Y log Y),

M(z)=2+max_{i<j} |Delta_{ij}(z)|.
```

Classification:

```text
TuplePrimeDivisorCeiling_336:
  STRUCTURAL / EXTRACTION.
```

This is a tuple-level divisor ceiling only. If `Delta_{ij}(z)=0` as an exact
integer equality, then every prime divides that difference and this ceiling
does not apply. Those exact-zero strata must be handled by the structural
diagonal ledger, not by high-prime tail summation.

### D. Why the divisor ceiling is not the tail theorem

The tail functional is not just:

```text
E_z DivTail_Y(z).
```

It contains:

```text
the absolute kernel |K_{U,V}^0(d_1,d_2;h+k)|,
the data-dependent masks U,V,
low-prime factors from (1+Def_Y),
multi-prime cover-family products,
exact-zero structural diagonals,
and the declared order N -> infinity first at fixed w.
```

The finite identity in part A shows the obstruction explicitly:

```text
Def_Z-Def_Y = (1+Def_Y) Def_{Y,Z}.
```

Thus the high-prime tail is coupled to the finite low-prime product. Even a
good high-prime divisor bound does not by itself control:

```text
kernel-weighted low-prime cover load times high-prime divisor load.
```

Classification:

```text
LowHighCoverCouplingRows_336:
  OPEN.

TailOnlyShortcut_336:
  FALSE / BLOCKED.
```

### E. Cutoff window criterion

A sufficient criterion for removing the cutoff in the Module 330 cover
moment is the following.

Choose `Y=Y(N,w)` with `Y>w`. Prove, in the same `P_minor^0` family and with
the same masks, dyadic shell, W-residue conventions, kernel, and limiting
order:

```text
1. Finite-side control:
     the Module 335 weighted CRT/mask and composite-modulus range rows hold
     for all cover families with primes <=Y(N,w).

2. Tail-side control:
     TailUniformityRows_336 holds uniformly for Z>=Y(N,w).

3. Low-high coupling:
     the factor (1+Def_Y) does not amplify Def_{Y,Z} beyond the tail budget.

4. Exact-zero diagonal control:
     exact integer equalities Delta_{ij}=0 that survive for all high primes
     are either already removed by the local model convention or bounded by
     the structural diagonal/collision rows in the same weighted average.

5. Limit order:
     all estimates survive N -> infinity first at fixed w, then w -> infinity.
```

Classification:

```text
CutoffWindowCriterion_336:
  CONDITIONAL.
```

If the criterion is proved, then the finite cutoff in
`KernelWeightedMobiusMomentCriterion_330` can be removed for the model-side
cover moment. The criterion is not proved here.

### F. Current closure verdict

The current ledger now has:

```text
finite cutoff difference algebra,
a precise tail functional,
a tuple-level divisor ceiling for nonzero lifted differences,
and a conditional cutoff-window criterion.
```

It does not have:

```text
weighted high-prime tail uniformity,
low-high cover coupling,
exact-zero diagonal control in this tail row,
finite-side CRT/mask closure for all p<=Y(N,w),
or a proved cutoff window Y(N,w).
```

Therefore:

```text
CurrentFinitePrimeTailClosure_336:
  FALSE / BLOCKED.
```

The next useful target is to audit whether the tuple-level high-prime divisor
ceiling can be promoted to a same-family weighted row with a compatible cutoff
window.

## 6. Edge cases and exclusions

- `Def_Z-Def_Y` is multiplied by `1+Def_Y`; high-prime tail control is not
  independent of the low-prime product.
- Exact zero differences `Delta_{ij}=0` are not controlled by
  `sum_{p>Y,p|Delta_{ij}} 1/p`; every prime divides zero.
- The divisor ceiling requires a declared integer lift and a bound for
  `M(z)`. Cyclic congruence statements alone do not give it.
- Choosing `Y` large helps divisor tails but may break the finite CRT/mask
  range through large composite moduli.
- Choosing `Y` small helps the finite CRT range but leaves more high-prime
  tail to control.
- Pointwise powers in `mu_p(T)` are not weighted averages.
- A one-prime high-block tail can be low order in `1/p` if many labels
  collide in one block; its usefulness depends on counting rarity.
- Absolute values remove signed cancellation between low and high factors.
- The masks `U,V` and the kernel remain data-dependent.
- The model selector is not the actual sharp moving selector.
- The local W-cyclic prime-only model is not the original full-gap problem.
- A finite cutoff identity is not an analytic proof.

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
  -> FinitePrimeTailCoverAudit_336
  -> HighPrimeDivisorWindowAudit_337.
```

It is still inside the local model `P_minor^0`. It does not prove
`AntiDiagonalTwoShiftKernelGain_312`, `PhaseKernelBound_273^0`,
`NarrowMinorArc_3^B`, `ResCube_3^sharp`, or the original selected-average
problem.

## 8. What remains open

The next smaller targets are:

```text
1. HighPrimeDivisorWindowAudit_337(P_minor^0):
     decide whether the tuple-level divisor ceiling can be averaged with the
     same absolute kernel, masks, dyadic ranges, W-residue conventions, and
     cutoff order.

2. LowHighCoverCouplingRows_336:
     prove or reject control of (1+Def_Y) times the high-prime defect inside
     the same weighted cover row.

3. ExactZeroDiagonalRows_336:
     decide which exact-zero high-prime strata are already covered by
     structural diagonal/collision rows and which remain endpoint-strength.

4. CutoffWindowCriterion_336:
     find or reject a range for Y(N,w) compatible with both finite CRT/mask
     estimates and high-prime tail estimates.

5. FinitePrimeTailRows_330:
     prove or reject tail control above the cutoff in the Module 330 cover
     moment.
```

The current cadence after completing this module is:

```text
Latest completed module: 336
Post-Reflective_1 solving count: 155
Long-term-plan count: 149

149 is not divisible by 9, so no plan update is due in this module.
149 is not divisible by 15, so no plan challenge is due in this module.
Next reflective log remains expected around Module 341.
```

## 9. Forbidden upgrades

This module does not prove:

```text
TailUniformityRows_336,
LowHighCoverCouplingRows_336,
CutoffWindowCriterion_336 as an estimate,
FinitePrimeTailRows_330,
MultiPrimeCoverMomentRows_330,
WeightedCRTMaskCriterion_335 as an estimate,
MaskCRTUniformityRows_335,
KernelCRTUniformityRows_335,
CompositeModulusRangeCriterion_335 as an estimate,
ExactWeightedPartitionRows_334,
CoarseningWeightedUniformityRows_334,
WeightedDyadicProjectionRow_333,
MaskedDyadicResidueUniformity_333,
KernelResidueMassCriterion_332 as an estimate,
AbsoluteMinorKernelResidueUniformity_332,
KernelWeightedPartitionClassCounting_331,
MaskResidueUniformity_331,
PartitionClassCountingRows_330,
StructuralRankUniformityRows_330,
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

Do not cite `TuplePrimeDivisorCeiling_336` as a weighted tail theorem. It is a
pointwise nonzero-divisor diagnostic only.
