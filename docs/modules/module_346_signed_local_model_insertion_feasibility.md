# Module 346: Signed local-model insertion feasibility

## 1. Precise theorem / claim being advanced

Module 345 selected the signed local-model insertion row as the next honest
test after pausing the absolute cover route. This module classifies that row.

The target is not to prove:

```text
F_8 = Omega_{w,8}^{minor}
```

pointwise. The target is to decide what same-family averaged theorem would be
needed to replace the physical signed eight-slot row by the
collision-sensitive local model under the threshold-localized minor kernel.

Define:

```text
SignedLocalModelInsertionFeasibility_346(P_minor^0).
```

Verdict:

```text
SignedLocalModelInsertionFeasibility_346(P_minor^0):
  STRUCTURAL / EXTRACTION.

SignedInsertionErrorIdentity_346:
  STRUCTURAL / EXTRACTION.

WeightedSubsetModelDiscrepancyCriterion_346:
  CONDITIONAL.

NaiveHLInsertionShortcut_346:
  FALSE / BLOCKED.

ProperSupportInsertionShortcut_346:
  FALSE / BLOCKED.

CurrentSignedLocalModelInsertionClosure_346:
  FALSE / BLOCKED.

SubsetModelDiscrepancyAudit_347(P_minor^0):
  OPEN next target.
```

The useful extraction is an exact identity:

```text
signed insertion error
  =
  signed sum of weighted subset physical-minus-model discrepancies.
```

The current ledger supplies no estimate for those discrepancies in the same
`P_minor^0` family with data-dependent threshold masks.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module proves no `SignedLocalModelInsertion_326`, no
`LocalModelInsertion_325`, no `DataDependentKernelSelectionRows_325`, no
`GenericNoncollisionRow_325`, no `StructuralDiagonalRows_325`, no
`FullCoverCollisionRows_326`, no `StratifiedGenericRemainderRows_326`, no
`KernelWeightedMobiusMomentCriterion_330`, no `PhaseKernelBound_273^0`, no
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

The local prime-only weight is real in `P_minor^0`, so the conjugations in
the original autocorrelation product are harmless for the subset expansion.
Keep the Module 323 physical product:

```text
f_0(n)=nu_0(n)-1,

F_8(z)
  =
  f_0(L_1)conj(f_0(L_2))
  conj(f_0(L_3))f_0(L_4)
  f_0(L_5)conj(f_0(L_6))
  conj(f_0(L_7))f_0(L_8).
```

For `S subset Lambda_8`, define:

```text
Nu_S^{346}(z)
  =
  prod_{i in S} nu_0(L_i(z)),

Nu_emptyset^{346}(z)=1.
```

Then:

```text
F_8(z)
  =
  sum_{S subset Lambda_8}
    (-1)^(8-|S|) Nu_S^{346}(z).
```

For the local model, retain:

```text
Theta_{w,S}^{8,min}(z)
  =
  prod_{p>w}
    (1-1/p)^(-|S|)
    (1-r_p(S;z)/p),
```

where `r_p(S;z)` counts distinct residues among `{L_i(z): i in S}` modulo
`p`. The signed local factor is:

```text
Omega_{w,8}^{minor}(z)
  =
  sum_{S subset Lambda_8}
    (-1)^(8-|S|) Theta_{w,S}^{8,min}(z).
```

For threshold-localized masks `U,V`, define:

```text
K_{U,V}^0(d_1,d_2;t)
  =
  sum_{xi in Minor_0(R,eta)}
    U(d_1,xi)V(d_2,xi)e_N(xi t).
```

The physical subset row is:

```text
Phys_S^{346}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      K_{U,V}^0(d_1,d_2;h+k)
      Nu_S^{346}(z).
```

The model subset row is:

```text
Mod_S^{346}(U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      K_{U,V}^0(d_1,d_2;h+k)
      Theta_{w,S}^{8,min}(z).
```

The subset discrepancy is:

```text
Err_S^{346}(U,V)
  =
  Phys_S^{346}(U,V)-Mod_S^{346}(U,V).
```

The signed insertion error is:

```text
SLMIError_{U,V}^{346}
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      K_{U,V}^0(d_1,d_2;h+k)
      (F_8(z)-Omega_{w,8}^{minor}(z)).
```

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 323-345,
the exact residual eight-slot expansion from Module 323,
the generic/collision local-model split from Module 325,
the signed inclusion-exclusion audit from Module 326,
and the post-cover branch decision from Module 345.
```

It does not assume:

```text
SignedLocalModelInsertion_326,
LocalModelInsertion_325,
DataDependentKernelSelectionRows_325,
GenericNoncollisionRow_325,
StructuralDiagonalRows_325,
FinitePrimeCollisionLoadRows_325,
OverflowRows_325,
FullCoverCollisionRows_326,
StratifiedGenericRemainderRows_326,
SharpCoverSmallness_328,
KernelWeightedSharpCoverCriterion_328 as a proved estimate,
KernelWeightedMobiusMomentCriterion_330 as a proved estimate,
WeightedCRTMaskCriterion_335 as a proved estimate,
CutoffWindowCriterion_336 as a proved estimate,
KernelWeightedDivisorWindowCriterion_337 as a proved estimate,
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

### A. Exact signed insertion error identity

Insert the two signed subset expansions:

```text
F_8(z)
  =
  sum_{S subset Lambda_8}
    (-1)^(8-|S|) Nu_S^{346}(z),

Omega_{w,8}^{minor}(z)
  =
  sum_{S subset Lambda_8}
    (-1)^(8-|S|) Theta_{w,S}^{8,min}(z).
```

By finite linearity:

```text
SLMIError_{U,V}^{346}
  =
  sum_{S subset Lambda_8}
    (-1)^(8-|S|) Err_S^{346}(U,V).
```

Classification:

```text
SignedInsertionErrorIdentity_346:
  STRUCTURAL / EXTRACTION.
```

This is only an identity. It does not estimate any `Err_S^{346}`.

### B. Conditional subset-model discrepancy criterion

A sufficient same-family insertion theorem is:

```text
For every S subset Lambda_8 and every admissible threshold-localized mask
pair U,V,

lim_{w -> infinity} limsup_{N -> infinity}
  |Err_S^{346}(U,V)|
  =
  0,
```

with the same:

```text
W-residue convention,
dyadic shell,
minor-arc denominator convention,
threshold mask class,
cutoff order,
local lift convention,
and limiting order
```

as `P_minor^0`.

Then:

```text
lim_{w -> infinity} limsup_{N -> infinity}
  |SLMIError_{U,V}^{346}|
  =
  0
```

by the finite sum over `2^8` subset rows.

Classification:

```text
WeightedSubsetModelDiscrepancyCriterion_346:
  CONDITIONAL.
```

This criterion is intentionally stronger than a possible signed cancellation
theorem for the total error. It is useful because it names the exact
same-family physical-versus-model rows that would need proof. The module does
not prove them.

### C. Why first-moment local models do not insert the row

Ordinary first-moment Hardy-Littlewood information would concern unweighted
averages of products such as:

```text
E_{x,y,h,k} Nu_S^{346}(z).
```

The needed object is weighted by:

```text
K_{U,V}^0(d_1,d_2;h+k),
```

summed over:

```text
D<|d_i|<=2D,  d_1 != d_2,
```

and uses data-dependent masks `U,V`. It also has to preserve the W-limit,
cutoff, dyadic, minor-arc, and selector conventions.

Therefore:

```text
NaiveHLInsertionShortcut_346:
  FALSE / BLOCKED.
```

First-moment local density does not imply this weighted threshold-localized
eight-slot insertion row.

### D. Proper-support cancellation does not insert the physical product

Module 326 proves a signed algebra fact inside the model-side subset
operator: proper-support components can cancel in the exact same signed
average. That does not prove:

```text
Phys_S^{346}(U,V)=Mod_S^{346}(U,V)
```

for any subset `S`, nor does it prove smallness of the signed sum of
discrepancies. The cancellation begins after the local model has already been
inserted.

Therefore:

```text
ProperSupportInsertionShortcut_346:
  FALSE / BLOCKED.
```

Signed algebra is not a physical-to-model transfer theorem.

### E. Current closure verdict

The active ledger has:

```text
exact physical eight-slot expansion,
exact local-model signed subset expansion,
collision and diagonal catalogs,
cover and tail diagnostics,
and low-envelope/exact-zero obstruction tests.
```

It does not have:

```text
weighted subset physical-minus-model estimates,
data-dependent kernel-selection uniformity,
same-family W-limit and cutoff transfer for the insertion row,
structural diagonal physical-model control,
collision-load physical-model control,
or any theorem inserting Omega_{w,8}^{minor} into the physical row.
```

Thus:

```text
CurrentSignedLocalModelInsertionClosure_346:
  FALSE / BLOCKED.
```

The insertion target remains open. The current module only reduces it to the
subset discrepancy rows and blocks the two tempting shortcuts.

### F. Next smaller target

The next smaller target should audit the subset discrepancy rows themselves:

```text
SubsetModelDiscrepancyAudit_347(P_minor^0).
```

That audit should decide whether any nontrivial subset family is already
controlled by model convention, zero-frequency cancellation, W-cyclic
averaging, or existing local HL inputs, and where the first genuinely
unproved weighted row appears.

## 6. Edge cases and exclusions

### Empty subset

For `S=emptyset`:

```text
Nu_emptyset^{346}=Theta_{w,emptyset}^{8,min}=1,
```

so:

```text
Err_emptyset^{346}(U,V)=0.
```

This exact zero does not control any nonempty subset discrepancy.

### Singletons and lower-order subsets

Some lower-order subset rows may vanish in special full-average situations
because of nonzero-frequency cancellation. That cancellation is not automatic
after data-dependent masks, structural cuts, W-residue restrictions, cutoff
changes, or dyadic shell restrictions are inserted.

### Structural diagonals

When lifted slots coincide, the physical product may contain repeated local
weights on the same point. The local factor `Theta_{w,S}^{8,min}` records
residue occupancy, but using it for the physical product still requires a
same-family insertion theorem or a separate structural diagonal row.

### Collision-sensitive model versus generic model

This module keeps `Theta_{w,S}^{8,min}` and `Omega_{w,8}^{minor}`. It does
not replace them by the generic size-only factors `Theta_{w,|S|}^{gen}` or
`Omega_w^{gen}`.

### Complex conjugation bookkeeping

The prime-only local weight `nu_0` is real in the current model. If a future
variant introduces a genuinely complex weight, the subset expansion must carry
the conjugation signature explicitly.

### Selector and endpoint transfer

This module stays inside `P_minor^0`. It does not transfer to the actual
sharp moving selector, full gap averages, the residual cube endpoint, or the
original selected-average problem.

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
  -> SignedLocalModelInsertionFeasibility_346.
```

The module returns to the missing physical-to-model insertion row named in
Modules 325-326. It does not prove `AntiDiagonalTwoShiftKernelGain_312`,
`PhaseKernelBound_273^0`, `NarrowMinorArc_3^B`, `ResCube_3^sharp`, or the
original selected-average problem.

## 8. What remains open

Still open:

```text
SubsetModelDiscrepancyAudit_347(P_minor^0),
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
the all-alpha theorem,
the finite-type theorem unconditionally,
and the original selected-average problem.
```

Next target:

```text
SubsetModelDiscrepancyAudit_347(P_minor^0).
```

## Red flags / forbidden upgrades

Do not cite `SignedInsertionErrorIdentity_346` as an insertion theorem.

Do not cite `WeightedSubsetModelDiscrepancyCriterion_346` unless the subset
discrepancy estimates have actually been proved.

Do not use first-moment Hardy-Littlewood, pair-BDH, or generic local density
as a substitute for weighted threshold-localized eight-slot insertion.

Do not use proper-support signed cancellation as physical-to-model transfer.

Do not treat data-dependent threshold masks as fixed external kernels.

Do not replace `Omega_{w,8}^{minor}` by `Omega_w^{gen}` without collision,
finite-prime load, overflow, and structural diagonal control.

Do not use `SignedLocalModelInsertion_326`, `LocalModelInsertion_325`,
`PhaseKernelBound_273^0`, `ResCube_3^sharp`, `CPC_3^sharp`,
`RBDH_pair_short`, or `AU^3` as assumptions.

Do not transfer this local model statement to the actual sharp moving
selector or to the original selected-average problem.
