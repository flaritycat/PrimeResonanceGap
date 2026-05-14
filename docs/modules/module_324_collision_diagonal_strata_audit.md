# Module 324: Collision and diagonal strata audit for the eight-slot minor row

## 1. Precise theorem / claim being advanced

Module 323 expanded the centered minor-kernel row into the exact eight-slot
residual top face. This module classifies the collision and diagonal strata
of that top face before any generic local-model or cancellation claim is
made.

Define:

```text
CollisionDiagonalStrataAudit_324(P_minor^0).
```

Verdict:

```text
CollisionDiagonalStrataAudit_324(P_minor^0):
  STRUCTURAL / EXTRACTION.

SlotDifferenceCatalog_324:
  STRUCTURAL / EXTRACTION.

StructuralDiagonalCatalog_324:
  STRUCTURAL / EXTRACTION.

FinitePrimeCollisionLoad_324:
  STRUCTURAL / EXTRACTION.

KernelAntiDiagonalStratum_324:
  STRUCTURAL / EXTRACTION.

CurrentCollisionStrataClosure_324:
  FALSE / BLOCKED.

GenericCollisionLocalModelSplit_325(P_minor^0):
  OPEN next target.
```

The audit shows that the off-diagonal condition `d_1 != d_2` removes only
one integer diagonal. It does not remove internal autocorrelation diagonals,
cross-block slot collisions, finite-prime collisions, or the full-frequency
anti-diagonal diagnostic `h+k=0`. None of these strata is proved small here.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module proves no collision smallness, no generic local-model estimate,
no residual eight-slot cancellation, no admissible `Phi`, no threshold
closure, no column barrier, no residual cube endpoint, and no selector
transfer.

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d_i|<=2D,
d_1 != d_2.
```

Use the eight slots from Module 323:

```text
L_1=x+d_1,      L_2=x,
L_3=x+h+d_1,    L_4=x+h,
L_5=y+d_2,      L_6=y,
L_7=y+k+d_2,    L_8=y+k.
```

The top-face residual product is:

```text
F_8(d_1,d_2;x,y,h,k)
  =
  f_0(L_1)conj(f_0(L_2))
  conj(f_0(L_3))f_0(L_4)
  f_0(L_5)conj(f_0(L_6))
  conj(f_0(L_7))f_0(L_8).
```

For threshold-localized masks `U,V`, the Module 323 row is:

```text
WOff_{U,V}
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      F_8(d_1,d_2;x,y,h,k)
      K_{U,V}^0(d_1,d_2;h+k),
```

where:

```text
K_{U,V}^0(d_1,d_2;t)
  =
  sum_{xi in Minor_0(R,eta)}
    U(d_1,xi)V(d_2,xi)e_N(xi t).
```

For the raw unlocalized row, `U=V=1` and `K_{U,V}^0=K_minor^0`.

For labels `1<=i<j<=8`, define the slot difference:

```text
Delta_{ij}=L_i-L_j.
```

## 4. Assumptions

This module assumes the active status ledger and Modules 278, 284, 297,
308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322,
and 323.

It uses only:

```text
the exact eight-slot expansion from Module 323,
finite affine algebra in G_N,
the off-diagonal shift condition d_1 != d_2,
and the nonzero-frequency minor-kernel convention.
```

It does not assume:

```text
GenericCollisionLocalModelSplit_325(P_minor^0),
CollisionStrataSmallness_324(P_minor^0),
FinitePrimeCollisionLoadSmall_324(P_minor^0),
ResidualEightSlotMinorCancellation_319(P_minor^0),
FiberOverlapGainTarget_321(P_minor^0),
AdmissiblePhiGain_320(P_minor^0),
DirectSignedMinorKernelTheorem_319(P_minor^0),
DataDependentLargeSpectrumGain_319(P_minor^0),
SignedMinorKernelGain_318(P_minor^0),
MajorLocalModelTransfer_317(P_minor^0),
CenteredFullAntiDiagonalControl_316(P_minor^0),
CenteredFullColumnSecondMomentTarget_316(P_minor^0),
MajorKernelCorrectionControl_314(P_minor^0),
AntiDiagonalTwoShiftKernelGain_312(P_minor^0),
WeightedColumnSecondMomentTarget_311(P_minor^0),
WeightedColumnPairEnergyTarget_310(P_minor^0),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
RowBarrierP0_284(q)=o_W(1),
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
ProjectedMajorTarget_3^B,
WProjectedLocalMatch_3^major,
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

### A. Slot-difference catalog

The first four slots form the `d_1,h` block:

```text
L_1=x+d_1, L_2=x, L_3=x+h+d_1, L_4=x+h.
```

The structural differences inside this block are:

```text
d_1,
h,
h+d_1,
h-d_1
```

up to sign. Thus internal first-block collisions occur on:

```text
p | d_1,
p | h,
p | h+d_1,
p | h-d_1
```

or, as exact structural diagonals in `G_N`, on:

```text
h=0, h=-d_1, h=d_1,
```

with `d_1=0` excluded by the active dyadic shift range except for separate
range/wrap defects.

The second block similarly gives:

```text
d_2,
k,
k+d_2,
k-d_2.
```

For cross-block differences, set:

```text
r=x-y.
```

Each cross difference has the form:

```text
Delta_{ij}
  =
  r + a d_1 + b h - c d_2 - e k,
```

where:

```text
(a,b) in {(1,0),(0,0),(1,1),(0,1)},
(c,e) in {(1,0),(0,0),(1,1),(0,1)}.
```

There are sixteen such cross forms. Their exact structural diagonals are:

```text
r = -a d_1 - b h + c d_2 + e k.
```

Classification:

```text
SlotDifferenceCatalog_324:
  STRUCTURAL / EXTRACTION.
```

This catalog only names where collisions can occur. It is not a smallness
estimate.

### B. Structural diagonal catalog

Define the structural diagonal set:

```text
Z_struct^8
  =
  union_{i<j} { Delta_{ij}=0 in G_N }.
```

It includes:

```text
h=0, h=d_1, h=-d_1,
k=0, k=d_2, k=-d_2,
```

and the sixteen cross-block equations:

```text
x-y = -a d_1 - b h + c d_2 + e k.
```

The excluded shift diagonal:

```text
d_1=d_2
```

is not the same object. It is already removed in `WOff_{U,V}`, but the
cross-block equations can still hold when `d_1 != d_2`.

Classification:

```text
StructuralDiagonalCatalog_324:
  STRUCTURAL / EXTRACTION.
```

A codimension-one description does not prove the weighted residual
contribution is small. The weights are residual prime weights, the kernel may
be large on some increments, and the threshold masks may be data-dependent.

### C. Finite-prime collision load

On the complement of `Z_struct^8`, every `Delta_{ij}` is nonzero in the
structural sense. A future generic-versus-collision comparison may need a
finite-prime collision load. Define the diagnostic load:

```text
B_{w,8}^{minor}
  =
  sum_{1<=i<j<=8}
    sum_{p>w, p | Delta_{ij}} 1/p,
```

formed only after structural zero forms have been removed or separately
modeled.

Equivalently, for each prime `p>w`, let `G_p^8` be the graph on
`{1,...,8}` with edge `i-j` when:

```text
L_i = L_j mod p.
```

The load records how far the residue pattern of the eight slots is from a
generic eight-distinct pattern.

Classification:

```text
FinitePrimeCollisionLoad_324:
  STRUCTURAL / EXTRACTION.
```

This is not an estimate. It is also not a substitute for the exact local
factor. A future module must decide whether the exact residual local model
can be split into a generic factor plus controlled collision defects in this
same `P_minor^0` family.

### D. Kernel anti-diagonal stratum

The full-frequency diagnostic in Module 312 would impose:

```text
h+k=0.
```

The actual minor row does not impose this equation. Instead it carries:

```text
K_{U,V}^0(d_1,d_2;h+k).
```

Define:

```text
Z_kernel^8={h+k=0}.
```

Classification:

```text
KernelAntiDiagonalStratum_324:
  STRUCTURAL / EXTRACTION.
```

This stratum is useful for orientation because it explains the
anti-diagonal geometry of the full-frequency row. It is not a support
condition for the actual minor row. Replacing the minor kernel by the
condition `h+k=0` would lose the zero and major corrections already audited
in Modules 314-318.

### E. Why current closure is blocked

The current ledger does not prove:

```text
weighted smallness on Z_struct^8,
small average finite-prime collision load B_{w,8}^{minor},
overflow control for large B_{w,8}^{minor},
uniform estimates for data-dependent K_{U,V}^0,
or generic residual local-model matching on the complement.
```

Counting a structural diagonal as codimension one is insufficient by itself.
The row is weighted by residual prime products and by a minor/localized
kernel. Similarly, bounding `B_{w,8}^{minor}` requires averaging over the
same dyadic shifts, W-residue convention, threshold masks, and limiting order
used in `P_minor^0`.

Therefore:

```text
CurrentCollisionStrataClosure_324:
  FALSE / BLOCKED.
```

This blocks only the current shortcut from classification to smallness. It
does not rule out a future collision/generic theorem.

### F. Extracted next target

The useful next move is not to declare the collision strata harmless. It is
to formulate the generic-versus-collision split that would be needed for the
exact eight-slot minor row.

Define:

```text
GenericCollisionLocalModelSplit_325(P_minor^0):
  split the exact eight-slot minor local model into a generic noncollision
  part, structural diagonal rows, finite-prime collision-load rows, overflow
  rows, kernel anti-diagonal diagnostics, and data-dependent kernel-selection
  rows, all in the same P_minor^0 conventions.
```

Status:

```text
GenericCollisionLocalModelSplit_325(P_minor^0):
  OPEN next target.
```

## 6. Edge cases

If `h=0`, the pairs `(L_1,L_3)` and `(L_2,L_4)` collide. This is an internal
autocorrelation diagonal, not a proof of saving.

If `h=d_1` or `h=-d_1`, cross-pairs inside the first block collide. The
analogous statements hold for `k=d_2` and `k=-d_2`.

If `x-y` satisfies one of the sixteen cross-block equations, slots from the
two derivative blocks collide even though `d_1 != d_2`.

If `p|d_1`, then `L_1` and `L_2`, and also `L_3` and `L_4`, collide modulo
`p`; the dyadic condition excludes `d_1=0` as an integer but not small-prime
divisibility.

If `d_1=d_2 mod p`, cross-block collision load may increase even though the
off-diagonal row has `d_1 != d_2`.

If `h+k=0`, the full-frequency anti-diagonal diagnostic is visible, but the
actual minor kernel remains an oscillatory nonzero-frequency kernel.

If `U,V` are data-dependent shell masks, the collision strata and kernel
selection are coupled; counting unweighted forms is not enough.

Nothing here transfers from `P_minor^0` to the actual sharp moving selector.

## 7. Project-map location

The Phase K column branch now reads:

```text
Module 323:
  extracts the exact eight-slot residual top face.

Module 324:
  classifies internal diagonals, cross-block diagonals, finite-prime
  collision load, and the kernel anti-diagonal diagnostic.
```

The selected next target is:

```text
GenericCollisionLocalModelSplit_325(P_minor^0).
```

## 8. What remains open

Still open:

```text
GenericCollisionLocalModelSplit_325(P_minor^0),
CollisionStrataSmallness_324(P_minor^0),
FinitePrimeCollisionLoadSmall_324(P_minor^0),
ResidualEightSlotMinorCancellation_319(P_minor^0),
FiberOverlapGainTarget_321(P_minor^0),
AdmissiblePhiGain_320(P_minor^0),
SizeSensitiveMinorKernelCriterion_320 as an estimate,
DirectSignedMinorKernelTheorem_319(P_minor^0),
DataDependentLargeSpectrumGain_319(P_minor^0),
SignedMinorKernelGain_318(P_minor^0),
MajorLocalModelTransfer_317(P_minor^0),
CenteredFullAntiDiagonalControl_316(P_minor^0),
CenteredFullColumnSecondMomentTarget_316(P_minor^0),
MajorKernelCorrectionControl_314(P_minor^0),
AntiDiagonalTwoShiftKernelGain_312(P_minor^0),
WeightedColumnSecondMomentTarget_311(P_minor^0),
WeightedColumnPairEnergyTarget_310(P_minor^0),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
RowBarrierP0_284(q)=o_W(1),
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
ProjectedMajorTarget_3^B,
WProjectedLocalMatch_3^major,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the original selected-average problem.
```

## 9. Forbidden upgrades

Do not cite `CollisionDiagonalStrataAudit_324(P_minor^0)` as collision
smallness.

Do not cite `StructuralDiagonalCatalog_324` as a bound for structural
diagonal rows.

Do not cite `FinitePrimeCollisionLoad_324` as a proof that the collision load
is small.

Do not replace the exact eight-slot residual local factor by a generic
eight-distinct factor without proving the collision and overflow rows.

Do not replace the minor kernel by the full-frequency anti-diagonal condition
`h+k=0`.

Do not treat data-dependent threshold masks as fixed external test functions.

Do not use endpoint objects, projected-major targets, column-barrier closure,
selector transfer, residual cube estimates, or an assumed admissible `Phi` to
prove the rows classified here.

Do not move this local `P_minor^0` classification to the actual sharp moving
selector without transfer rows.

## 10. Next target

The next target is:

```text
Module 325:
  GenericCollisionLocalModelSplit_325(P_minor^0).
```

It should formulate the exact generic-versus-collision local-model split for
the eight-slot minor row, including structural diagonals, finite-prime
collision load, overflow, data-dependent kernel selection, and the W-limit
order, without claiming any of those rows are already small.
