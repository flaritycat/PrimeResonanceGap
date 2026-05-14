# Module 323: Residual eight-slot minor expansion inside `P_minor^0`

## 1. Precise theorem / claim being advanced

Module 322 selected an extraction-only test: expand the centered
minor-kernel row into exact residual slots before making any new analytic
claim.

Define:

```text
ResidualEightSlotMinorExpansion_323(P_minor^0).
```

Verdict:

```text
ResidualEightSlotMinorExpansion_323(P_minor^0):
  STRUCTURAL / EXTRACTION.

RawEightSlotTopFaceIdentity_323:
  STRUCTURAL / EXTRACTION.

ThresholdLocalizedKernelIdentity_323(U,V):
  STRUCTURAL / EXTRACTION.

ZeroMeanLowerFaceIdentity_323:
  STRUCTURAL / EXTRACTION.

FixedKernelInterpretation_323(U,V):
  FALSE / BLOCKED for data-dependent threshold-localized rows.

EightSlotExpansionClosesMinorGain_323:
  FALSE / BLOCKED.

CollisionDiagonalStrataAudit_324(P_minor^0):
  OPEN next target.
```

The expansion gives an exact eight-residual-slot top face. The centered lower
faces vanish in aggregate because the minor kernel contains only nonzero
frequencies. This is an identity, not cancellation at the needed scale. For
the threshold-localized rows used by the Module 320 `Phi` criterion, the
kernel is data-dependent through the large-spectrum masks, so the expansion
does not become a fixed local-model theorem for free.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module proves no residual eight-slot cancellation, no admissible `Phi`,
no column barrier, no threshold closure, no signed minor-kernel gain, no
phase-kernel bound, no residual cube endpoint, and no selector transfer.

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
f_0(n)=nu_0(n)-1,
B_d^0(n)=f_0(n+d)conj(f_0(n)),
Z_d=E_n B_d^0(n),
B_d^{0,circ}(n)=B_d^0(n)-Z_d,
gamma_0(d,xi)=widehat{B_d^{0,circ}}(xi).
```

Then:

```text
gamma_0(d,0)=0,
gamma_0(d,xi)=beta_0(d,xi) for xi != 0.
```

The centered autocorrelation is:

```text
A_d^{circ}(h)
  =
  E_x B_d^{0,circ}(x)conj(B_d^{0,circ}(x+h)).
```

The uncentered autocorrelation is:

```text
A_d(h)
  =
  E_x B_d^0(x)conj(B_d^0(x+h)).
```

They satisfy:

```text
A_d^{circ}(h)=A_d(h)-|Z_d|^2.
```

The raw centered minor row is:

```text
M_minor^{circ}
  =
  WOff_311
  =
  D^(-1) sum_{d_1 != d_2}
    sum_{xi in Minor_0(R,eta)}
      |gamma_0(d_1,xi)|^2 |gamma_0(d_2,xi)|^2.
```

For threshold-localized rows, let `U,V` be masks on the shift-frequency
incidence set, for example:

```text
U=1_{J_{j,k}},
V=1_{J_{j,l}}.
```

Define:

```text
WOff_{U,V}
  =
  D^(-1) sum_{d_1 != d_2}
    sum_{xi in Minor_0(R,eta)}
      U(d_1,xi)V(d_2,xi)
      |gamma_0(d_1,xi)|^2 |gamma_0(d_2,xi)|^2.
```

The associated localized kernel is:

```text
K_{U,V}^0(d_1,d_2;t)
  =
  sum_{xi in Minor_0(R,eta)}
    U(d_1,xi)V(d_2,xi)e_N(xi t).
```

For `U=V=1` on the full minor set this is the raw minor kernel
`K_minor^0(t)`.

## 4. Assumptions

This module assumes the active status ledger and Modules 278, 284, 297,
308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, and
322.

It uses:

```text
finite cyclic Fourier algebra,
the exact centered identity from Module 315,
the nonzero-frequency minor convention,
the Module 312 autocorrelation identity,
and the Module 320 threshold-localized cross-shell notation.
```

It does not assume:

```text
CollisionDiagonalStrataAudit_324(P_minor^0),
ResidualEightSlotMinorCancellation_319(P_minor^0),
FiberOverlapGainTarget_321(P_minor^0),
AdmissiblePhiGain_320(P_minor^0),
PhiCriterion_320(Phi) with a proved Phi,
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
ThresholdBudgetP0Closure_284(q,r),
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

### A. Threshold-localized autocorrelation identity

For every nonzero frequency:

```text
|gamma_0(d,xi)|^2
  =
  E_h A_d^{circ}(h)e_N(xi h).
```

Therefore, for any masks `U,V` supported on minor frequencies:

```text
WOff_{U,V}
  =
  D^(-1) sum_{d_1 != d_2}
    E_{h,k}
      A_{d_1}^{circ}(h)A_{d_2}^{circ}(k)
      K_{U,V}^0(d_1,d_2;h+k).
```

Classification:

```text
ThresholdLocalizedKernelIdentity_323(U,V):
  STRUCTURAL / EXTRACTION.
```

This identity keeps the Module 320 threshold localization visible. It also
shows a warning: when `U,V` are data-dependent shell masks such as
`J_{j,k},J_{j,l}`, the kernel `K_{U,V}^0` is not a fixed external kernel.
It depends on the same Fourier coefficients being estimated.

### B. Zero-mean lower-face identity

Because `Minor_0(R,eta)` excludes zero:

```text
E_h K_{U,V}^0(d_1,d_2;h+k)=0,
E_k K_{U,V}^0(d_1,d_2;h+k)=0
```

for every fixed `d_1,d_2,k,h`, and also:

```text
E_{h,k} K_{U,V}^0(d_1,d_2;h+k)=0.
```

Using:

```text
A_d^{circ}(h)=A_d(h)-|Z_d|^2,
```

we get:

```text
E_{h,k}
  A_{d_1}^{circ}(h)A_{d_2}^{circ}(k)
  K_{U,V}^0(d_1,d_2;h+k)

=

E_{h,k}
  A_{d_1}(h)A_{d_2}(k)
  K_{U,V}^0(d_1,d_2;h+k).
```

The lower faces created by centering vanish exactly after the nonzero
minor-frequency kernel is applied.

Classification:

```text
ZeroMeanLowerFaceIdentity_323:
  STRUCTURAL / EXTRACTION.
```

This is zero-mode bookkeeping. It is not a minor-arc saving, and it does not
control any collision stratum of the top eight-slot row.

### C. Exact eight residual slots

Substitute:

```text
B_d^0(x)=f_0(x+d)conj(f_0(x))
```

into the uncentered autocorrelation product. For variables
`x,y,h,k in G_N`, define eight affine slots:

```text
L_1=x+d_1,      L_2=x,
L_3=x+h+d_1,    L_4=x+h,
L_5=y+d_2,      L_6=y,
L_7=y+k+d_2,    L_8=y+k.
```

Define the signed-conjugated eight-slot residual product:

```text
F_8(d_1,d_2;x,y,h,k)
  =
  f_0(L_1)conj(f_0(L_2))
  conj(f_0(L_3))f_0(L_4)
  f_0(L_5)conj(f_0(L_6))
  conj(f_0(L_7))f_0(L_8).
```

Then the threshold-localized row has the exact physical expansion:

```text
WOff_{U,V}
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      F_8(d_1,d_2;x,y,h,k)
      K_{U,V}^0(d_1,d_2;h+k).
```

In particular:

```text
M_minor^{circ}
  =
  D^(-1) sum_{d_1 != d_2}
    E_{x,y,h,k}
      F_8(d_1,d_2;x,y,h,k)
      K_minor^0(h+k).
```

Classification:

```text
RawEightSlotTopFaceIdentity_323:
  STRUCTURAL / EXTRACTION.
```

The displayed identity is the exact residual eight-slot top face. It is not
a proof that the top face is small.

### D. What the expansion does and does not expose

The expansion exposes four kinds of structure.

First, it displays the two derivative shifts:

```text
L_1-L_2=L_3-L_4=d_1,
L_5-L_6=L_7-L_8=d_2.
```

Second, it displays the two autocorrelation increments:

```text
L_3-L_1=L_4-L_2=h,
L_7-L_5=L_8-L_6=k.
```

Third, it displays the same-frequency minor projection through:

```text
K_{U,V}^0(d_1,d_2;h+k).
```

For the full-frequency diagnostic this would become a hard condition
`h+k=0`. For the actual minor row it is an oscillatory nonzero-frequency
kernel, not a physical equality.

Fourth, it displays many possible collision strata among:

```text
L_1,...,L_8
```

modulo finite primes, including internal collisions such as `h=0` or
`h=-d_1`, cross-shift collisions relating `x-y` to combinations of
`d_1,d_2,h,k`, and modular coincidences such as `d_1=d_2 mod p` even when
`d_1 != d_2` as integers.

The expansion does not yet say which collision strata are harmless, which
are structural diagonals, and which carry endpoint-strength load.

### E. Why fixed-kernel interpretation is blocked for localized rows

For the raw row, `K_minor^0(t)` is a fixed kernel after `R,eta,N` are fixed.
For the Module 320 cross-shell rows, however:

```text
K_{U,V}^0(d_1,d_2;t)
  =
  sum_xi U(d_1,xi)V(d_2,xi)e_N(xi t)
```

with `U,V` usually determined by shell conditions on:

```text
|gamma_0(d,xi)|.
```

Thus the kernel records the data-dependent large spectrum. Treating it as a
fixed deterministic test function would hide the selection problem already
exposed in Modules 280, 288, 303, 305, and 321.

Classification:

```text
FixedKernelInterpretation_323(U,V):
  FALSE / BLOCKED for data-dependent threshold-localized rows.
```

A future fixed-kernel theorem could be useful only if accompanied by a
selection-transfer, uniform-fiber, or direct adaptive-kernel theorem in the
same `P_minor^0` family.

### F. Closure verdict

The exact expansion gives:

```text
centered minor row
  =
eight residual top face with the minor/localized kernel.
```

It does not give:

```text
an admissible Phi,
a column-multiplicity gain,
a weighted column-pair gain,
a collision-neutrality theorem,
or residual cube control.
```

Therefore:

```text
EightSlotExpansionClosesMinorGain_323:
  FALSE / BLOCKED.
```

The expansion is still useful because it gives the next smaller object to
audit: the collision and diagonal strata of the top eight-slot row.

Define:

```text
CollisionDiagonalStrataAudit_324(P_minor^0):
  classify the collision and diagonal strata of L_1,...,L_8 in the exact
  residual eight-slot minor row, separating structural diagonals, finite-prime
  collision loads, full-frequency diagnostics, and genuinely oscillatory
  minor-kernel rows.
```

Status:

```text
CollisionDiagonalStrataAudit_324(P_minor^0):
  OPEN next target.
```

## 6. Edge cases

If `U` or `V` is empty, the localized kernel is zero and the row vanishes.
This is local vacuity, not a uniform estimate.

If `U,V` are fixed masks independent of `gamma_0`, the localized kernel is a
fixed nonzero-frequency kernel. This removes the selection issue but still
does not prove any eight-slot cancellation.

If `U,V` are shell masks such as `J_{j,k},J_{j,l}`, the kernel is adaptive
and must not be treated as independent of the residual slots.

If zero frequency enters a future minor convention, the zero-mean lower-face
identity must be rederived. The current convention excludes zero.

If `h+k=0`, the full-frequency diagnostic is visible, but the actual minor
kernel remains `K_minor^0(0)` or its localized analogue. The major and zero
pieces have not disappeared.

If `h=0`, `k=0`, `h=-d_1`, or `k=-d_2`, some internal slots collide. These
are strata for Module 324, not automatic savings.

If `d_1=d_2 mod p` for small primes, cross-shift collision load may increase
even though the off-diagonal integer condition `d_1 != d_2` holds.

Nothing in this module transfers from `P_minor^0` to the actual sharp moving
selector.

## 7. Project-map location

The Phase K column branch now reads:

```text
Module 312:
  weighted pair energy expands to a minor-kernel anti-diagonal row.

Modules 314-318:
  full/zero/major splitting is diagnostic; the centered full-minus-major row
  is exactly WOff_311.

Modules 319-321:
  candidate inputs are filtered; a Phi criterion is formulated; current
  fiber caps do not force the needed Phi.

Module 322:
  direct cap-only/fiber-only continuation is paused.

Module 323:
  the centered minor row is expanded into the exact eight-slot residual top
  face, with lower centered faces removed only by the nonzero minor-kernel
  identity.
```

The selected next target is:

```text
CollisionDiagonalStrataAudit_324(P_minor^0).
```

## 8. What remains open

Still open:

```text
CollisionDiagonalStrataAudit_324(P_minor^0),
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
ThresholdBudgetP0Closure_284(q,r),
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

Do not cite `ResidualEightSlotMinorExpansion_323(P_minor^0)` as residual
eight-slot cancellation.

Do not cite `ZeroMeanLowerFaceIdentity_323` as analytic saving. It is exact
zero-frequency bookkeeping.

Do not treat `K_{U,V}^0` as fixed when `U,V` are data-dependent shell masks.

Do not claim the eight-slot top face is controlled because it has been
written down.

Do not use endpoint objects, projected-major targets, column-barrier closure,
selector transfer, residual cube estimates, or an assumed admissible `Phi` to
prove the rows extracted here.

Do not replace the actual sharp moving selector by a model, frozen, smoothed,
or finite-stage selector without a named transfer theorem.

Do not replace the full gap by a clipped gap or tail without a named gap/tail
transfer theorem.

Do not replace exact local collision factors by averaged substitutes.

## 10. Next target

The next target is:

```text
Module 324:
  CollisionDiagonalStrataAudit_324(P_minor^0).
```

It should classify the collision and diagonal strata of the exact eight-slot
minor row and decide whether a smaller non-endpoint collision/generic split
survives, or whether the expansion has simply restated the signed
minor-kernel obstruction in physical variables.
