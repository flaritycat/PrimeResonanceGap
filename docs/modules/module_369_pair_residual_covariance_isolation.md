# Module 369: Pair-residual covariance isolation

## 1. Target claim

Chosen attack mode:

```text
E. Residual obstruction route.
```

Best-module selection:

```text
The best current module is PairResidualCovarianceIsolation_369(P_minor^0).
```

Reason:

```text
Module 368 classified the pair-residual Fourier energy as the missing
same-family variance input. The next smaller attack is not another
pair-model coefficient estimate; it is to isolate the exact four-point
covariance, degenerate rectangle strata, weighted residual cross term, and
model-defect rows inside that variance.
```

Define:

```text
PairResidualCovarianceIsolation_369(P_minor^0).
```

Verdict:

```text
PairResidualCovarianceIsolation_369(P_minor^0):
  STRUCTURAL / EXTRACTION.

PairResidualCovarianceDecomposition_369:
  PROVEN.

NondegenerateRectangleCovarianceObject_369:
  STRUCTURAL / EXTRACTION.

DegenerateRectangleStrataCatalog_369:
  STRUCTURAL / EXTRACTION.

WeightedPairResidualCorrelationTarget_369:
  OPEN.

RectangleDiagonalModelDefectTarget_369:
  OPEN.

FirstMomentRectangleHLShortcut_369:
  FALSE / BLOCKED.

SameFamilyPairBDHVarianceTarget_368:
  OPEN.
```

Module status label:

```text
STRUCTURAL / EXTRACTION.
```

The useful outcome is that `SameFamilyPairBDHVarianceTarget_368` is split
into exact rows. The main analytic row is a same-shift four-point covariance
over rectangles:

```text
E_{a,q,r}
  nu_0(r)nu_0(r+a)nu_0(r+q)nu_0(r+q+a)
  -
  Theta_model^0(a,q),
```

together with degenerate rectangle strata, a weighted pair-residual
correlation, and a rectangle-diagonal model-defect row. Current first-moment
rectangle language does not close all of these rows.

## 2. Why this would advance the main theorem

The current large-value route needs:

```text
D^(-1)K_UK_V
  E_a |P_nu^0(a)-kappa_model^0(a)|^2
  =
  o_W(1).
```

Module 368 showed that this is a variance theorem, not a zero-mode pair
calibration theorem. This module identifies the exact covariance objects
inside the variance. That gives the next proof run a smaller target:

```text
prove the nondegenerate same-shift rectangle covariance and route the
degenerate/model-defect/weighted-cross rows in the same family.
```

It also prevents a false shortcut. A first-moment rectangle statement for
generic rectangles is not enough unless it includes the same diagonal
conventions, degenerate strata, model defect, weighted pair-residual cross
term, W-residue, cyclic range, and limit order.

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ.
```

The physical pair correlation is:

```text
P_nu^0(a)
  =
  E_{r in G_N} nu_0(r)nu_0(r+a).
```

Let:

```text
kappa_model^0(a)
```

be the pair model used in the residual, with the same diagonal/off-diagonal
convention as Modules 363-368. Define:

```text
E_pair,model^0(a)
  =
  P_nu^0(a)-kappa_model^0(a),

Energy_pair^0(model)
  =
  E_a |E_pair,model^0(a)|^2.
```

Define the physical same-shift rectangle count:

```text
Rect_nu^0(a,q)
  =
  E_{r in G_N}
    nu_0(r)nu_0(r+a)nu_0(r+q)nu_0(r+q+a).
```

Let:

```text
Theta_model^0(a,q)
```

be the rectangle local model used with the same convention as the pair model.
On the nondegenerate stratum it is the exact four-point local factor:

```text
Theta_w^4(a,a;q)
  =
  prod_{p>w}
    (1-1/p)^(-4)
    (1-#({0,a,q,q+a} mod p)/p).
```

On degenerate strata it must be supplied by the declared collision/diagonal
convention. This module does not invent that convention.

Define:

```text
Delta_rect^0(a,q)
  =
  Rect_nu^0(a,q)-Theta_model^0(a,q),

R_diag,model^0(a)
  =
  E_{q in G_N} Theta_model^0(a,q),

Def_diag,model^0(a)
  =
  R_diag,model^0(a)-kappa_model^0(a)^2.
```

The nondegenerate rectangle stratum is:

```text
ND
  =
  { (a,q) in G_N^2 :
      a != 0,
      q != 0,
      q != -a }.
```

The degenerate stratum is:

```text
Deg=G_N^2 \ ND.
```

## 4. Assumptions

This module assumes:

```text
Modules 351, 361, and 368,
the model-convention discipline from Modules 363-367,
finite cyclic Fourier algebra,
and the active status ledger.
```

It does not assume:

```text
SameFamilyPairBDHVarianceTarget_368,
PairResidualFourierEnergyTarget_361,
PairResidualLargeValueTarget_359,
PairMixedDiagonalAbsorptionCriterion_363,
full P_minor^0 pair-model minor top-mass,
RectangleDefectLargeValueTarget_359,
AntiDiagonalRectangleVarianceTarget_360,
CoefficientTopMassProfileCriterion_356 as a proved estimate,
NoTwistColumnProfileCorrelation_356,
SignedLocalModelInsertion_326,
LocalModelInsertion_325,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
actual sharp moving-selector transfer,
full-gap transfer,
the all-alpha theorem,
the finite-type theorem unconditionally,
or the original selected-average problem.
```

Forbidden assumptions:

```text
generic rectangle HL controls degenerate rectangle strata,
Theta_model^0(a,q) may be replaced by kappa_model^0(a)^2,
the weighted pair-residual cross term is automatically small,
the pair model convention can differ between the covariance and residual.
```

## 5. Proof / disproof / reduction

### A. Exact covariance decomposition

By definition:

```text
Energy_pair^0(model)
  =
  E_a |P_nu^0(a)-kappa_model^0(a)|^2.
```

Using the finite identity from Module 368:

```text
|P_nu^0(a)-kappa_model^0(a)|^2
  =
  (P_nu^0(a)^2-R_diag,model^0(a))
  -2kappa_model^0(a)(P_nu^0(a)-kappa_model^0(a))
  +Def_diag,model^0(a).
```

Now:

```text
P_nu^0(a)^2
  =
  E_{r,s}
    nu_0(r)nu_0(r+a)nu_0(s)nu_0(s+a).
```

Writing:

```text
q=s-r
```

gives:

```text
P_nu^0(a)^2
  =
  E_{r,q}
    nu_0(r)nu_0(r+a)nu_0(r+q)nu_0(r+q+a)
  =
  E_q Rect_nu^0(a,q).
```

Therefore:

```text
E_a(P_nu^0(a)^2-R_diag,model^0(a))
  =
  E_{a,q} Delta_rect^0(a,q).
```

Combining:

```text
Energy_pair^0(model)
  =
  E_{a,q} Delta_rect^0(a,q)
  -2E_a kappa_model^0(a)E_pair,model^0(a)
  +E_a Def_diag,model^0(a).
```

Finally split:

```text
E_{a,q} Delta_rect^0(a,q)
  =
  E_{(a,q) in ND}^{norm} Delta_rect^0(a,q)
  +
  E_{(a,q) in Deg}^{norm} Delta_rect^0(a,q),
```

where the notation means the same global normalization `E_{a,q}` with the
indicator of the displayed set.

Classification:

```text
PairResidualCovarianceDecomposition_369:
  PROVEN.
```

This is exact algebra once the model conventions are fixed. It is not a
smallness theorem.

### B. Nondegenerate rectangle covariance object

On:

```text
ND={a != 0, q != 0, q != -a},
```

the four affine forms:

```text
r,
r+a,
r+q,
r+q+a
```

are pairwise distinct as cyclic shifts unless a further finite-cyclic wrap or
W-residue convention creates an additional collision. The required
nondegenerate covariance row is:

```text
NondegenerateRectangleCovarianceTarget_369:
  D^(-1)K_UK_V
  |
    E_{a,q} 1_ND(a,q)
      (
        Rect_nu^0(a,q)-Theta_w^4(a,a;q)
      )
  |
  =
  o_W(1),
```

with the same family, W-residue, cyclic range, and limit order.

Classification:

```text
NondegenerateRectangleCovarianceObject_369:
  STRUCTURAL / EXTRACTION.
```

This object is the main off-diagonal shifted-prime covariance. It is not
proved here.

### C. Degenerate rectangle strata catalog

The complement of `ND` consists of:

```text
a=0,
q=0,
q=-a.
```

These correspond respectively to:

```text
r=r+a and r+q=r+q+a,
r=s and r+a=s+a,
r+a=s and r=s+a.
```

On these strata the four-point local factor has collisions. A generic
four-distinct-forms Hardy-Littlewood statement does not apply without a
separate collision convention and estimate.

Classification:

```text
DegenerateRectangleStrataCatalog_369:
  STRUCTURAL / EXTRACTION.
```

The required degenerate target is:

```text
DegenerateRectangleCovarianceRows_369:
  OPEN.
```

This module does not mark it as closed.

### D. Weighted residual and model-defect rows

The covariance decomposition also contains:

```text
WeightedPairResidualCorrelation_369
  =
  E_a kappa_model^0(a)E_pair,model^0(a),
```

and:

```text
RectangleDiagonalModelDefect_369
  =
  E_a Def_diag,model^0(a)
  =
  E_a(R_diag,model^0(a)-kappa_model^0(a)^2).
```

These rows are not cosmetic. The first is a weighted pair-residual
correlation; the second is exactly the statement that the diagonal rectangle
model averages to the square of the pair model. Neither follows from the
nondegenerate rectangle covariance alone.

Classification:

```text
WeightedPairResidualCorrelationTarget_369:
  OPEN.

RectangleDiagonalModelDefectTarget_369:
  OPEN.
```

### E. Why first-moment rectangle HL is not enough

A first-moment rectangle theorem for generic nondegenerate quadruples could
at best address part of:

```text
E_{a,q} 1_ND(a,q) Delta_rect^0(a,q).
```

It does not automatically control:

```text
DegenerateRectangleCovarianceRows_369,
WeightedPairResidualCorrelationTarget_369,
RectangleDiagonalModelDefectTarget_369.
```

Nor does it automatically include the same:

```text
W-residue,
cyclic representative convention,
model diagonal convention,
fixed-w then N->infty limit order,
and threshold scale D^(-1)K_UK_V.
```

Therefore:

```text
FirstMomentRectangleHLShortcut_369:
  FALSE / BLOCKED.
```

The same-family variance target remains:

```text
SameFamilyPairBDHVarianceTarget_368:
  OPEN.
```

## 6. Edge cases

### Cyclic wrap

The conditions `a!=0`, `q!=0`, and `q!=-a` are cyclic conditions in `G_N`.
If a later argument changes representatives or imposes boundary windows, the
strata must be rechecked.

### Model convention

If `kappa_model^0` removes the pair diagonal, then `Theta_model^0` and
`R_diag,model^0` must use the compatible rectangle convention. Mismatched
model conventions change the defect row.

### Degenerate local factors

On degenerate strata, the four-form Euler product can behave like a lower
rank local factor. Treating it as the generic four-distinct local factor is a
forbidden upgrade.

### Weighted cross term

The weighted cross term can be bounded by Cauchy only using the same energy
one is trying to prove, so that route is circular unless a separate small
coefficient or absorption estimate is supplied.

### Threshold scale

All open targets must be strong enough after multiplication by
`D^(-1)K_UK_V`. Unscaled covariance statements are not automatically enough.

## 7. Project-map location

```text
PairResidualFourierEnergyAudit_368
  -> PairResidualCovarianceIsolation_369
  -> PairResidualVarianceInputVerdict_370.
```

This module isolates the exact rows inside the same-family pair variance.
It does not prove the variance.

## 8. What remains open

Still open:

```text
PairResidualVarianceInputVerdict_370(P_minor^0),
NondegenerateRectangleCovarianceTarget_369,
DegenerateRectangleCovarianceRows_369,
WeightedPairResidualCorrelationTarget_369,
RectangleDiagonalModelDefectTarget_369,
SameFamilyPairBDHVarianceTarget_368,
PairResidualFourierEnergyTarget_361,
PairResidualLargeValueTarget_359,
PairMixedDiagonalAbsorptionCriterion_363,
full P_minor^0 pair-model minor top-mass without PolyR_rho,
RectangleDefectLargeValueTarget_359,
AntiDiagonalRectangleVarianceTarget_360,
DiagonalOverlapLargeValueTarget_359,
CoefficientTopMassProfileCriterion_356 as an estimate,
NoTwistColumnProfileCorrelation_356(P_minor^0),
SignedLocalModelInsertion_326,
LocalModelInsertion_325,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
selector transfer,
full-gap transfer,
the all-alpha theorem,
and the original selected-average problem.
```

The current cadence after this module is:

```text
Latest completed module: 369
Post-Reflective_1 solving count: 188
Long-term-plan count: 182

182 is not divisible by 9, so no plan update is due in this module.
182 is not divisible by 15, so no plan challenge is due in this module.
The next reflective log is expected around Module 381.
```

## 9. Red-team audit

Selector check:

```text
All statements remain inside P_minor^0. No actual sharp moving-selector
statement is proved.
```

Gap-object check:

```text
No full-gap, clipped-gap, dyadic tail, or empty-interval statement is used.
```

Local-factor check:

```text
The rectangle model is kept as Theta_model^0(a,q). It is not replaced by
kappa_model^0(a)^2, and degenerate local factors are not treated as generic.
```

Limit-order check:

```text
All decompositions are finite cyclic decompositions. No fixed-w/N/W limit is
exchanged.
```

Uniformity check:

```text
The same-family variance rows are named but not proved.
```

Endpoint-circularity check:

```text
The proof does not assume SameFamilyPairBDHVarianceTarget_368,
PairResidualFourierEnergyTarget_361, PhaseKernelBound_273^0,
NarrowMinorArc_3^B, ResCube_3^sharp, CPC_3^sharp, RBDH_pair_short, or AU^3.
```

Official status check:

```text
No README, global status, or theorem-status index theorem claim is upgraded.
```

## 10. Final classification

```text
PairResidualCovarianceIsolation_369(P_minor^0):
  STRUCTURAL / EXTRACTION.

PairResidualCovarianceDecomposition_369:
  PROVEN.

NondegenerateRectangleCovarianceObject_369:
  STRUCTURAL / EXTRACTION.

DegenerateRectangleStrataCatalog_369:
  STRUCTURAL / EXTRACTION.

WeightedPairResidualCorrelationTarget_369:
  OPEN.

RectangleDiagonalModelDefectTarget_369:
  OPEN.

FirstMomentRectangleHLShortcut_369:
  FALSE / BLOCKED.

SameFamilyPairBDHVarianceTarget_368:
  OPEN.
```

Do not cite this module as a proof of pair-residual energy. It isolates the
covariance rows that a proof must control.

## Red flags / forbidden upgrades

- Do not treat generic rectangle HL as controlling degenerate strata.
- Do not replace `Theta_model^0(a,q)` by `kappa_model^0(a)^2`.
- Do not ignore the weighted pair-residual cross term.
- Do not change the model convention between pair and rectangle rows.
- Do not claim the residual cube endpoint or original selected-average
  problem is solved.
