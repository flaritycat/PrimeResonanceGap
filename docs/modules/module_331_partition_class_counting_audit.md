# Module 331: Partition-class counting audit and sixteenth plan update

## 1. Precise theorem / claim being advanced

Module 330 isolated the kernel-weighted Mobius cover-moment criterion. The
first missing input is the ability to count one prime partition class in the
same row.

Define:

```text
PartitionClassCountingAudit_331(P_minor^0).
```

Verdict:

```text
PartitionClassCountingAudit_331(P_minor^0):
  STRUCTURAL / EXTRACTION.

EqualityConstraintMatrix_331:
  STRUCTURAL / EXTRACTION.

KernelFiberRankDecomposition_331:
  STRUCTURAL / EXTRACTION.

ExactPartitionUpperEnvelope_331:
  STRUCTURAL / EXTRACTION.

KernelWeightedPartitionClassCounting_331:
  OPEN.

DyadicResidueUniformity_331:
  OPEN.

KernelResidueMassRows_331:
  OPEN.

MaskResidueUniformity_331:
  OPEN.

CurrentPartitionClassCountingClosure_331:
  FALSE / BLOCKED.

PlanUpdate_16_331:
  STRUCTURAL / EXTRACTION.

KernelFiberPartitionAudit_332(P_minor^0):
  OPEN next target.
```

This module gives the linear-algebra normal form for one partition class. It
does not prove the kernel-weighted partition count needed by Module 330.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The rank decomposition is exact finite linear algebra over one prime. The
analytic counting row remains open because the target average is weighted by
the same data-dependent kernel, threshold masks, dyadic shift ranges, and
W-residue conventions as the minor row.

This module proves no kernel-weighted Mobius-cover smallness, no partition
counting estimate, no CRT product estimate, no finite-prime tail removal, no
signed local-model insertion, no threshold closure, no `PhaseKernelBound_273^0`,
no residual cube endpoint, no selector transfer, and no statement about the
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

Use the eight slots:

```text
Lambda_8={1,2,3,4,5,6,7,8},

L_1=x+d_1,      L_2=x,
L_3=x+h+d_1,    L_4=x+h,
L_5=y+d_2,      L_6=y,
L_7=y+k+d_2,    L_8=y+k.
```

Set:

```text
r=x-y,
t=h+k.
```

After quotienting by the common translation `y`, the slots become:

```text
L_1=r+d_1,      L_2=r,
L_3=r+h+d_1,    L_4=r+h,
L_5=d_2,        L_6=0,
L_7=t-h+d_2,    L_8=t-h.
```

For one prime `p>w`, all ranks below are over `F_p`. Since the active
W-limit eventually has `w>8`, the small-prime degeneracies `p<=8` are not
used as closure inputs.

Write the coefficient vectors in variables:

```text
z=(r,h,t,d_1,d_2)
```

as:

```text
v_1=(1, 0, 0, 1, 0)
v_2=(1, 0, 0, 0, 0)
v_3=(1, 1, 0, 1, 0)
v_4=(1, 1, 0, 0, 0)
v_5=(0, 0, 0, 0, 1)
v_6=(0, 0, 0, 0, 0)
v_7=(0,-1, 1, 0, 1)
v_8=(0,-1, 1, 0, 0).
```

For a partition `pi` of a subset `T subset Lambda_8`, let `E(pi)` be any
spanning-tree edge set inside each block of `pi`. The equality closure of
`pi` is:

```text
L_i=L_j mod p for every edge (i,j) in E(pi).
```

Let `A_pi` be the matrix with rows:

```text
v_i-v_j,  (i,j) in E(pi).
```

Split variables as:

```text
u=(r,h),
b=(t,d_1,d_2).
```

Write:

```text
A_pi = [ A_u(pi) | A_b(pi) ],

rho_u(pi)=rank A_u(pi),
rho(pi)=rank A_pi,
rho_b(pi)=rho(pi)-rho_u(pi).
```

Define the single-prime weighted partition row:

```text
C_pi^{331}(p;U,V)
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      |K_{U,V}^0(d_1,d_2;h+k)|
      1_{Pi_p|_T = pi}.
```

The target needed by Module 330 is a bound for this row, or for a finite
collection of such rows, in the exact same family.

## 4. Assumptions

This module assumes only:

```text
the active status ledger,
Modules 323-330,
finite linear algebra over F_p,
and the exact eight-slot forms above.
```

It does not assume:

```text
KernelWeightedPartitionClassCounting_331,
DyadicResidueUniformity_331,
KernelResidueMassRows_331,
MaskResidueUniformity_331,
KernelFiberPartitionAudit_332,
PartitionClassCountingRows_330,
StructuralRankUniformityRows_330,
MultiPrimeCoverMomentRows_330,
FinitePrimeTailRows_330,
KernelWeightedMobiusMomentCriterion_330 as a proved estimate,
SharpCoverSmallness_328,
FullCoverLoadSmallness_327,
FullCoverRankUniformity_327,
KernelWeightedCoverRows_327,
FullCoverCollisionRows_326,
StratifiedGenericRemainderRows_326,
SignedLocalModelInsertion_326,
StructuralDiagonalRows_325,
FinitePrimeCollisionLoadRows_325,
OverflowRows_325,
DataDependentKernelSelectionRows_325,
GenericNoncollisionRow_325,
LocalModelInsertion_325,
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

### A. Translation reduction

Every equality `L_i=L_j mod p` is unchanged by adding the same residue to
`x` and `y`. The kernel in the local row depends on `h+k=t`, not on the
common translation. Hence the partition indicator is a function of:

```text
(r,h,t,d_1,d_2).
```

The common translation contributes one free normalized average. This gives
the coefficient vectors above.

Classification:

```text
EqualityConstraintMatrix_331:
  STRUCTURAL / EXTRACTION.
```

### B. Equality-class rank over full residues

If `(r,h,t,d_1,d_2)` were averaged uniformly over all residues modulo `p`,
then the equality closure of `pi` would have residue density:

```text
p^(-rho(pi)).
```

This is only the full-residue linear algebra benchmark. It is not the target
row, because the actual average has:

```text
dyadic restrictions on d_1,d_2,
the kernel weight |K_{U,V}^0(d_1,d_2;t)|,
threshold-localized masks U,V,
W-residue conventions,
and finite-cyclic wrap constraints.
```

### C. Kernel-fiber rank decomposition

For fixed base variables:

```text
b=(t,d_1,d_2),
```

the equality system has the form:

```text
A_u(pi) u = -A_b(pi)b.
```

For a fixed compatible base `b`, the number of residue solutions in
`u=(r,h)` is:

```text
p^(2-rho_u(pi)).
```

The compatible set of base residues has codimension:

```text
rho_b(pi)=rho(pi)-rho_u(pi).
```

Thus the rank splits into:

```text
rho_u(pi): loss inside the free variables r,h,
rho_b(pi): compatibility loss in the weighted variables t,d_1,d_2.
```

Classification:

```text
KernelFiberRankDecomposition_331:
  STRUCTURAL / EXTRACTION.
```

This is the key obstruction exposed by the audit. The `rho_b` part cannot be
used unless the project controls residue classes of `t` under the kernel and
residue classes of `d_1,d_2` under the dyadic shift average and masks.

### D. Exact partition versus equality envelope

The exact event `Pi_p|_T=pi` requires:

```text
equalities inside each block of pi,
and inequalities between distinct blocks of pi.
```

For upper bounds:

```text
1_{Pi_p|_T=pi}
  <=
  1_{equality closure of pi}.
```

Exact counting can be expressed by inclusion-exclusion over coarsenings of
`pi`, but that would require the same kernel-weighted rows for all coarser
partitions. The upper envelope is structural; exact asymptotics are not
proved here.

Classification:

```text
ExactPartitionUpperEnvelope_331:
  STRUCTURAL / EXTRACTION.
```

### E. Diagnostic examples

For the pair block `{1,2}`:

```text
L_1=L_2 mod p  iff  d_1=0 mod p.
```

Therefore:

```text
rho_u=0,
rho_b=1.
```

This is not a free `p^(-1)` saving unless the dyadic `d_1` residues are
controlled in the relevant range.

For the pair block `{1,3}`:

```text
L_1=L_3 mod p  iff  h=0 mod p.
```

Therefore:

```text
rho_u=1,
rho_b=0.
```

This is an internal fiber loss in `h`; it does not by itself give kernel
residue savings in `t`.

For the cross pair `{1,5}`:

```text
L_1=L_5 mod p  iff  r+d_1-d_2=0 mod p.
```

Therefore:

```text
rho_u=1,
rho_b=0.
```

For the cross pair `{3,8}`:

```text
L_3=L_8 mod p  iff  r+2h-t+d_1=0 mod p.
```

For `p>2`:

```text
rho_u=1,
rho_b=0.
```

For the first autocorrelation block `{1,2,3,4}`:

```text
L_1=L_2=L_3=L_4 mod p
```

forces:

```text
d_1=0 mod p,
h=0 mod p,
```

so:

```text
rho_u=1,
rho_b=1.
```

For the one-prime full block `Lambda_8`:

```text
L_1=...=L_8 mod p
```

forces:

```text
r=0,
h=0,
t=0,
d_1=0,
d_2=0             mod p.
```

For `p>2`:

```text
rho_u=2,
rho_b=3,
rho=5.
```

These examples explain why Module 329's pointwise powers cannot be converted
into averages by a single rank slogan. Some losses live in unweighted
fiber variables, while others live in the kernel and dyadic shift variables.

### F. Current closure verdict

The current ledger now has:

```text
an equality matrix for each one-prime partition class,
a split between free-fiber rank and kernel/base compatibility rank,
and an upper envelope for exact partition events.
```

It does not have:

```text
kernel residue-mass estimates for t,
dyadic residue uniformity for d_1,d_2,
mask uniformity across d-residue classes,
exact coarsening inclusion-exclusion estimates,
multi-prime CRT combination after weights,
or finite-prime tail removal.
```

Therefore:

```text
CurrentPartitionClassCountingClosure_331:
  FALSE / BLOCKED.
```

The next useful target is to isolate the kernel-fiber row: what can actually
be said about the `t`-residue mass of `|K_{U,V}^0(d_1,d_2;t)|` after the
threshold masks and dyadic shift ranges are present?

### G. Sixteenth plan update

The current cadence after completing this module is:

```text
Latest completed module: 331
Post-Reflective_1 solving count: 150
Long-term-plan count: 144

144 is divisible by 9, so the sixteenth plan update is due and completed here.
144 is not divisible by 15, so no plan challenge is due here.
Next reflective log remains expected around Module 341.
```

Plan update:

```text
PlanUpdate_16_331:
  STRUCTURAL / EXTRACTION.
```

The previous nine-iteration window moved the branch from a broad column and
fiber obstruction into exact eight-slot collision/Mobius bookkeeping:

```text
Module 323: exact eight-slot minor expansion,
Module 324: collision and diagonal strata audit,
Module 325: generic/collision split,
Module 326: signed inclusion-exclusion support audit,
Module 327: full-cover cluster catalog,
Module 328: sharp Mobius-cover criterion,
Module 329: prime-local Mobius powers,
Module 330: cover-moment criterion,
Module 331: partition-class rank audit.
```

The branch became sharper, but it did not close any endpoint row. The next
window should stay narrow:

```text
Module 332:
  KernelFiberPartitionAudit_332(P_minor^0).

Module 333:
  DyadicResidueUniformityAudit_333(P_minor^0).

Module 334:
  ExactPartitionCoarseningAudit_334(P_minor^0).

Module 335:
  MultiPrimeCRTMaskAudit_335(P_minor^0).

Module 336:
  FinitePrimeTailCoverAudit_336(P_minor^0).

Module 337:
  SignedLocalModelInsertionGate_337(P_minor^0), unless an earlier row blocks
  the route more decisively.

Module 338:
  CoverMomentRouteVerdict_338(P_minor^0).

Module 339:
  PhaseKBranchDecision_339.

Module 340:
  prepare the next reflection boundary without upgrading any open row.
```

Decision:

```text
Continue Phase K only through the kernel-fiber and residue-uniformity
micro-rows. If those rows reproduce row/column barriers or require endpoint
strength, stop treating the Mobius-cover route as a promising closure route
and redirect the next challenge toward signed local-model insertion or a
return to PhaseKernelBound_273^0.
```

## 6. Edge cases and exclusions

- A full-residue rank is not a kernel-weighted partition count.
- The compatibility rank `rho_b` is useful only with residue control for
  `t,d_1,d_2` in the same family.
- Ignoring inequalities between partition blocks gives only an upper envelope.
- Exact partition counting by coarsening inclusion-exclusion still needs the
  same kernel-weighted rows for coarser partitions.
- Pair blocks such as `{1,2}` may ask for `p|d_1`; this is a dyadic shift row,
  not an `h`-fiber saving.
- Cross blocks may consume `r` and leave the kernel variable untouched.
- Blocks involving both sides can impose conditions on `t`; those require
  kernel residue-mass estimates.
- The data-dependent masks `U,V` remain part of the target row.
- The model selector is not the actual sharp moving selector.
- The local W-cyclic prime-only model is not the original full-gap problem.
- A structural rank extraction is not an analytic proof.
- A conditional theorem is not a theorem.

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
  -> KernelFiberPartitionAudit_332.
```

It is still inside the local model `P_minor^0`. It does not prove
`AntiDiagonalTwoShiftKernelGain_312`, `PhaseKernelBound_273^0`,
`NarrowMinorArc_3^B`, `ResCube_3^sharp`, or the original selected-average
problem.

## 8. What remains open

The next smaller targets are:

```text
1. KernelFiberPartitionAudit_332(P_minor^0):
     decide what residue-mass statements are available for
     |K_{U,V}^0(d_1,d_2;t)| on the compatibility classes forced by pi.

2. DyadicResidueUniformity_331:
     prove or reject the residue distribution needed for d_1,d_2 over the
     active dyadic ranges.

3. MaskResidueUniformity_331:
     prove or reject uniformity after threshold masks U,V are present.

4. ExactPartitionCoarseningAudit_334:
     decide whether exact partition events can be handled by coarsening
     inclusion-exclusion without losing the same-family row.

5. MultiPrimeCoverMomentRows_330:
     prove or reject CRT/uniformity for products of one-prime partition rows.
```

## 9. Forbidden upgrades

This module does not prove:

```text
KernelWeightedPartitionClassCounting_331,
DyadicResidueUniformity_331,
KernelResidueMassRows_331,
MaskResidueUniformity_331,
KernelFiberPartitionAudit_332,
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

Do not cite `PartitionClassCountingAudit_331` as a partition-counting
estimate. It is a rank and obstruction audit only.
