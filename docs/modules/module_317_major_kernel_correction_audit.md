# Module 317: Major-kernel correction audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

Module 316 rewrote the minor row as a centered full row minus a major
correction row:

```text
WOff_311
  =
  FullAntiDiag_circ_316
  -
  MajorKernelCorrectionRow_circ_316.
```

This module audits the major correction row. The word "correction" is
dangerous here: the row is a positive same-frequency pair energy over the
major arcs, not an error term known to be small.

Define:

```text
MajorKernelCorrectionAudit_317(P_minor^0).
```

Verdict:

```text
MajorKernelCorrectionAudit_317(P_minor^0):
  STRUCTURAL / EXTRACTION.

MajorKernelCorrectionIdentity_317:
  STRUCTURAL / EXTRACTION.

MajorArcEightSlotModelRequirement_317:
  STRUCTURAL / EXTRACTION.

CurrentMajorCorrectionToolsClose_317:
  FALSE / BLOCKED.

MajorKernelCorrectionControl_314(P_minor^0):
  OPEN.

MajorLocalModelTransfer_317(P_minor^0):
  OPEN.

SignedMinorKernelCombinationVerdict_318(P_minor^0):
  OPEN next target.
```

The module extracts the exact row and the exact kind of local model that
would be needed. It does not prove the major row small and does not prove the
signed full-minus-major minor row.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is an identity and route-classification module. It proves no major-arc
cancellation, no weighted column-pair gain, no threshold closure, no
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
beta_0(d,xi)=widehat{B_d^0}(xi).
```

From Module 315:

```text
B_d^{0,circ}(n)=B_d^0(n)-Z_d,
gamma_0(d,xi)=widehat{B_d^{0,circ}}(xi),
gamma_0(d,0)=0,
gamma_0(d,xi)=beta_0(d,xi) for xi != 0.
```

The active major/minor convention from Module 278 is:

```text
Major_0(R,eta)
  =
  { xi in widehat{G_N} :
      xi != 0 and
      exists 1<=q<=R, exists (a,q)=1,
      || xi/N - a/q ||_{R/Z} <= eta/q },

Minor_0(R,eta)
  =
  { xi in widehat{G_N} : xi != 0 } \ Major_0(R,eta).
```

Zero is removed before the major/minor split. Boundary frequencies use the
displayed non-strict inequality.

Define:

```text
K_major^0(t)
  =
  sum_{xi in Major_0(R,eta)} e_N(xi t).
```

For the centered product define:

```text
A_d^{circ}(h)
  =
  E_n B_d^{0,circ}(n)conj(B_d^{0,circ}(n+h)).
```

The centered major pair is:

```text
MajorPair_circ_317(d_1,d_2)
  =
  sum_{xi in Major_0(R,eta)}
    |gamma_0(d_1,xi)|^2 |gamma_0(d_2,xi)|^2.
```

Since `Major_0(R,eta)` excludes zero:

```text
MajorPair_circ_317(d_1,d_2)
  =
  sum_{xi in Major_0(R,eta)}
    |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2.
```

The off-diagonal row is:

```text
MajorKernelCorrectionRow_circ_317
  =
  D^(-1) sum_{d_1 != d_2}
    MajorPair_circ_317(d_1,d_2).
```

## 4. Assumptions

This module assumes the active status ledger and Modules 278, 284, 297, 308,
309, 310, 311, 312, 313, 314, 315, and 316.

It uses:

```text
finite cyclic Fourier algebra,
the active Major_0/Minor_0 convention,
the centered rewrite from Module 315,
and the Module 316 full-minus-major identity.
```

It does not assume:

```text
MajorKernelCorrectionControl_314(P_minor^0),
MajorLocalModelTransfer_317(P_minor^0),
SignedMinorKernelCombinationTarget_314(P_minor^0),
CenteredFullAntiDiagonalControl_316(P_minor^0),
CenteredFullColumnSecondMomentTarget_316(P_minor^0),
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

### A. Exact major-row identity

By the same Fourier calculation used in Module 312:

```text
|gamma_0(d,xi)|^2
  =
  E_h A_d^{circ}(h)e_N(xi h).
```

Therefore:

```text
MajorPair_circ_317(d_1,d_2)
  =
  E_{h,k}
    A_{d_1}^{circ}(h)A_{d_2}^{circ}(k)K_major^0(h+k).
```

Equivalently:

```text
MajorPair_circ_317(d_1,d_2)
  =
  sum_{xi in Major_0(R,eta)}
    |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2.
```

Thus:

```text
MajorKernelCorrectionRow_circ_317
  =
  D^(-1) sum_{d_1 != d_2}
    sum_{xi in Major_0(R,eta)}
      |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2.
```

Classification:

```text
MajorKernelCorrectionIdentity_317:
  STRUCTURAL / EXTRACTION.
```

The row is positive. Its sign in:

```text
FullAntiDiag_circ_316 - MajorKernelCorrectionRow_circ_317
```

comes from the frequency partition, not from cancellation inside the major
row itself.

### B. Exact eight-slot object behind the major row

For each coefficient square:

```text
|beta_0(d,xi)|^2
  =
  E_{n,m}
    B_d^0(n)conj(B_d^0(m))e_N(xi(m-n)).
```

For two shifts `d_1,d_2`, the major row contains the eight residual slots:

```text
L_1=n_1+d_1,  L_2=n_1,
L_3=m_1+d_1,  L_4=m_1,
L_5=n_2+d_2,  L_6=n_2,
L_7=m_2+d_2,  L_8=m_2,
```

with oscillation:

```text
e_N(xi((m_1-n_1)+(m_2-n_2))).
```

Thus a major-arc local model for this row must be an exact residual
eight-slot model:

```text
Omega_{w}^{2x2}
  =
  sum_{S subset {1,...,8}} (-1)^(8-|S|)
    Theta_{w,S}^{2x2},
```

with the same collision conventions, W-residue `b`, cyclic variables,
dyadic shift shell, denominator ranges, cutoff, and limiting order as
`P_minor^0`.

It is not enough to supply:

```text
a first-moment Hardy-Littlewood count,
a pair covariance model,
a rectangle marginal,
the full non-residual eight-form model without inclusion-exclusion,
or a model in a different projected family.
```

Classification:

```text
MajorArcEightSlotModelRequirement_317:
  STRUCTURAL / EXTRACTION.
```

This requirement is a specification, not a proof that such a model exists or
that its signed residual contribution is small after summing `d_1 != d_2`.

### C. Rational-arc cover discipline

The major set is defined by the existence of a rational approximation
`a/q`. A route through rational arcs must decide how to handle:

```text
overlapping arcs,
boundary frequencies with equality ||xi/N-a/q||=eta/q,
the exclusion of xi=0,
summation over q<=R and (a,q)=1,
uniformity in eta and R,
and the same N -> infinity then w -> infinity order.
```

A cover estimate with multiplicity is not the same as an exact
major-projection identity. If a future proof decomposes:

```text
1_{Major_0(R,eta)}(xi)
```

into rational windows, it must either use an exact disjoint assignment or
carry the overlap/boundary error as a named row.

This is one reason the existing conditional major-projector ledgers cannot be
inserted here as a black box.

### D. Why current tools do not close the major correction row

The following shortcuts fail under the current ledger.

First, positivity gives only:

```text
0 <= MajorKernelCorrectionRow_circ_317
     <= FullAntiDiag_circ_316.
```

Module 316 records that the centered full row is open, so this bound does not
close the major row.

Second, the cardinality bound:

```text
|K_major^0(t)| <= #Major_0(R,eta)
```

returns an absolute-kernel ceiling. It does not use residual cancellation and
does not beat the weighted column-pair ceiling from Modules 311 and 312.

Third, ordinary pair-BDH or first-moment Hardy-Littlewood input controls
lower-order averages. The major row is a fourth moment of pair products, and
its physical expansion is the eight-slot residual object above. Pair or
first-moment information does not supply the needed nonzero-frequency
same-frequency pair estimate.

Fourth, `WProjectedLocalMatch_3^major` and
`ProjectedMajorTarget_3^B` are not available inputs. They are conditional or
open in the status ledger, and they concern a projected major endpoint with
its own transfer and model-neutrality packages. They cannot be used to prove
this local `P_minor^0` major correction row.

Therefore:

```text
CurrentMajorCorrectionToolsClose_317:
  FALSE / BLOCKED.

MajorKernelCorrectionControl_314(P_minor^0):
  OPEN.

MajorLocalModelTransfer_317(P_minor^0):
  OPEN.
```

This blocks only the current route. It does not prove that no major local
model route exists.

### E. Consequence for the centered full-minus-major route

After Modules 315-317 the split is:

```text
WOff_311
  =
  FullAntiDiag_circ_316
  -
  MajorKernelCorrectionRow_circ_317.
```

The first term is open by Module 316. The second term is open by the present
module. Proving them separately small remains unavailable.

The honest next question is whether the signed difference itself has
cancellation not visible in either positive component, or whether the
full-minus-major formulation merely restates the original minor-row target.

Define:

```text
SignedMinorKernelCombinationVerdict_318(P_minor^0):
  decide whether the centered full-minus-major formulation supplies a
  genuinely smaller proof route, or whether it is only a restatement of
  AntiDiagonalTwoShiftKernelGain_312(P_minor^0) under the current inputs.
```

Status:

```text
SignedMinorKernelCombinationVerdict_318(P_minor^0):
  OPEN next target.
```

## 6. Edge cases

If `Major_0(R,eta)` is empty, then the major correction row is zero. The
centered full row then equals the minor row, so Module 316 becomes the active
obstruction.

If `Major_0(R,eta)` contains every nonzero frequency, then the minor row is
empty and the centered full-minus-major identity is locally vacuous. This is
not the active major/minor regime.

If zero is included in a future major convention, the row must be rewritten.
The current convention removes zero before the major/minor split.

If rational arcs overlap, summing per-arc estimates may overcount. Exact
partition or overlap accounting is part of the model requirement.

If only fixed `q,a` estimates are supplied, they do not prove the row unless
they are summed uniformly over the declared major arcs with the exact
threshold, W-residue, dyadic, and limiting conventions.

If `d_1=d_2`, the row is diagonal and returns to fourth-power mass. The live
column-pair obstruction is the off-diagonal row `d_1 != d_2`.

Nothing in this module transfers from `P_minor^0` to the actual sharp moving
selector.

## 7. Project-map location

The Phase K column branch now reads:

```text
Module 312:
  weighted pair energy expands to a minor-kernel anti-diagonal form.

Module 314:
  the minor kernel splits into full-frequency, zero-mode, and major rows.

Module 315:
  the zero row is not killed by convention, but an exact centered rewrite
  removes it as an explicit correction.

Module 316:
  the centered full row is the full nonzero-frequency column second moment;
  current tools do not control it.

Module 317:
  the major correction row is a positive major-frequency pair-energy row;
  current tools do not control it either.
```

The selected next target is:

```text
SignedMinorKernelCombinationVerdict_318(P_minor^0).
```

## 8. What remains open

Still open:

```text
SignedMinorKernelCombinationVerdict_318(P_minor^0),
MajorKernelCorrectionControl_314(P_minor^0),
MajorLocalModelTransfer_317(P_minor^0),
CenteredFullAntiDiagonalControl_316(P_minor^0),
CenteredFullColumnSecondMomentTarget_316(P_minor^0),
SignedMinorKernelCombinationTarget_314(P_minor^0),
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

Do not cite `MajorKernelCorrectionAudit_317(P_minor^0)` as a major-row
estimate.

Do not cite `MajorKernelCorrectionIdentity_317` as smallness.

Do not call the major correction harmless because it is a "correction." It is
a positive major-frequency row.

Do not replace the exact residual eight-slot major model by pair-BDH,
first-moment Hardy-Littlewood, rectangle marginals, or the non-residual
eight-form model.

Do not use `WProjectedLocalMatch_3^major`, `ProjectedMajorTarget_3^B`, or
`ProjectedModelNeutralityGate_260` as inputs to prove this row. Their active
statuses are conditional or open, and they are not the same local
`P_minor^0` theorem.

Do not ignore rational-arc overlap, boundary frequencies, zero-frequency
conventions, W-residue conventions, denominator ranges, or limiting order.

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
Module 318:
  SignedMinorKernelCombinationVerdict_318(P_minor^0).
```

It should decide whether the centered full-minus-major expression is a
genuine smaller route with a named new estimate, or whether the row split has
now served its purpose and the project should return to the original
anti-diagonal minor-kernel target as the unresolved object.
