# Module 367: Pair-model minor top-mass verdict

## 1. Target claim

Chosen attack mode:

```text
F. Counter-route with a steering verdict.
```

Best-module selection:

```text
The best current module is PairModelMinorTopMassVerdict_367(P_minor^0).
```

Reason:

```text
Modules 362-366 have now extracted everything currently available from the
pair-model coefficient branch. Continuing to refine the pair-model side would
not address the remaining same-family pair-residual energy obstruction. The
right move is to assemble the pair-model conclusions, classify the branch,
perform the due plan update/challenge at long-term-plan count 180, and pivot
to PairResidualFourierEnergyTarget_361.
```

Define:

```text
PairModelMinorTopMassVerdict_367(P_minor^0).
```

Verdict:

```text
PairModelMinorTopMassVerdict_367(P_minor^0):
  STRUCTURAL / EXTRACTION.

MixedRowAssemblyLemma_367:
  PROVEN.

PolynomialRSubfamilyModelCoefficientCriterion_367:
  CONDITIONAL.

FullPminorPairModelTopMassClosure_367:
  FALSE / BLOCKED.

PairModelBranchAsNextPrimaryAttack_367:
  FALSE / BLOCKED.

PairResidualFourierEnergyTarget_361:
  OPEN.
  Next primary attack.

PlanUpdate_20_367:
  STRUCTURAL / EXTRACTION.

PlanChallenge_12_367:
  STRUCTURAL / EXTRACTION.
```

Module status label:

```text
STRUCTURAL / EXTRACTION.
```

The useful outcome is a clean verdict. The pair-model coefficient branch has
produced a conditional polynomial-R subfamily estimate, not a full `P_minor^0`
theorem. The next best analytic target is the pair-residual Fourier energy
itself.

## 2. Why this would advance the main theorem

The active no-twist branch contains:

```text
PairResidualLargeValueStress_361
  -> pair-residual square row
  -> pair-residual times model row
  -> CoefficientTopMassProfileCriterion_356
  -> NoTwistColumnProfileCorrelation_356
  -> SignedLocalModelInsertion_326.
```

Modules 362-366 have tested the deterministic model coefficient side of the
mixed row. They show:

```text
full P_minor^0 pair-model top-mass is not closed,
but a polynomial-R off-diagonal model subfamily is conditionally controlled.
```

This means the project should stop treating the model coefficient as a black
box and should not spend the next step trying to squeeze full `P_minor^0`
out of a family that allows bounded `R`. The remaining high-value attack is
the same-family pair-residual energy:

```text
E_a |P_nu^0(a)-kappa_w^0(a)|^2.
```

That is the object which can feed both the square pair-residual row and the
mixed row once model coefficient hypotheses are fixed.

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
Minor_0(R,eta) subset G_N \ {0}.
```

Recall:

```text
P_nu^0(a)
  =
  E_{r in G_N} nu_0(r)nu_0(r+a),

E_pair^0(a)
  =
  P_nu^0(a)-kappa_w^0(a),

E_+^0(xi)
  =
  E_{a in G_N} E_pair^0(a)e_N(xi a),

K_+^0(xi)
  =
  E_{a in G_N} kappa_w^0(a)e_N(xi a).
```

When the diagonal/off-diagonal convention from Modules 363 and 366 is used,
write:

```text
K_model^0(xi)
```

for the model coefficient actually used in the mixed row. It may be:

```text
K_{w,+}^{0,off}(xi),
```

or that off-diagonal coefficient plus an explicitly retained finite diagonal
row. The convention must be fixed before the residual is defined.

For a nonnegative coefficient `c(xi)`:

```text
A_star,c(m)
  =
  sup_{E subset Minor_0(R,eta), #E<=m}
    sum_{xi in E} c(xi).
```

The active top-mass scale is:

```text
m_{U,V}=ceil(min(I_U/K_U,I_V/K_V)).
```

## 4. Assumptions

This module assumes:

```text
Modules 361-366,
finite cyclic Fourier algebra,
and the active status ledger.
```

For the conditional subfamily criterion it additionally assumes:

```text
PolyR_rho,
a fixed off-diagonal/diagonal convention,
the model coefficient bound supplied by Module 366,
and the diagonal row from Module 363 when a finite diagonal atom is retained.
```

It does not assume:

```text
PairResidualFourierEnergyTarget_361,
PairResidualLargeValueTarget_359,
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
PolyR_rho is automatic in full P_minor^0,
off-diagonal model control absorbs the physical diagonal,
model coefficient control proves pair-residual energy,
conditional subfamily control closes the full parent theorem.
```

## 5. Proof / disproof / reduction

### A. Mixed row assembly lemma

Let `K_model^0` be any model coefficient on `Minor_0(R,eta)` satisfying:

```text
sup_{xi in Minor_0(R,eta)} |K_model^0(xi)| <= eps_K.
```

Then for every `E subset Minor_0(R,eta)` with `#E<=m`:

```text
sum_{xi in E} |E_+^0(xi)K_model^0(xi)|
  <=
  eps_K m^(1/2)
  (
    sum_{xi in G_N} |E_+^0(xi)|^2
  )^(1/2).
```

By normalized Parseval:

```text
sum_{xi in G_N} |E_+^0(xi)|^2
  =
  E_{a in G_N} |E_pair^0(a)|^2.
```

Therefore:

```text
A_star,|E_+^0K_model^0|(m)
  <=
  eps_K m^(1/2)
  (
    E_a |E_pair^0(a)|^2
  )^(1/2).
```

Classification:

```text
MixedRowAssemblyLemma_367:
  PROVEN.
```

This is a finite Fourier/Cauchy inequality. It estimates no prime
distribution object.

### B. Conditional polynomial-R model coefficient criterion

Module 366 proves, in the polynomial-R subfamily and after the off-diagonal
convention is fixed:

```text
sup_{xi in Minor_0(R,eta)}
  |K_{w,+}^{0,off}(xi)|
  =
  o(1).
```

If the finite diagonal atom is removed or separately satisfies the Module 363
absorption row, then the mixed row is reduced by part A to:

```text
D^(-1)K_UK_V
  eps_K
  m_{U,V}^{1/2}
  (
    E_a |E_pair^0(a)|^2
  )^(1/2)
  =
  o_W(1),
```

with the residual and model convention matched.

Classification:

```text
PolynomialRSubfamilyModelCoefficientCriterion_367:
  CONDITIONAL.
```

The condition is genuine: it includes the polynomial-R subfamily, diagonal
routing, threshold-scale compatibility, and pair-residual energy. It is not a
full `P_minor^0` theorem.

### C. Full P_minor0 pair-model closure remains blocked

Full `P_minor^0` permits:

```text
2 <= R <= N^delta_R
```

without any lower growth assumption. Module 366 showed that if `R` is bounded
or grows too slowly, the choice:

```text
z_N proportional to log N
```

need not satisfy:

```text
P(w,z_N)<=R.
```

The current proof cannot simultaneously:

```text
put all Ramanujan denominators inside the major-denominator cutoff,
approximate the infinite off-diagonal Euler product uniformly,
and route the diagonal row.
```

Therefore:

```text
FullPminorPairModelTopMassClosure_367:
  FALSE / BLOCKED.
```

This is a proof-route verdict, not a counterexample to the target.

### D. Best next attack

The pair-model branch has now delivered:

```text
1. exact low-denominator leakage,
2. diagonal divergence and finite diagonal leakage,
3. exact finite Ramanujan expansion,
4. finite-cyclic tail and range criteria,
5. conditional polynomial-R off-diagonal model smallness.
```

The remaining mixed-row obstruction is no longer primarily the deterministic
model coefficient. It is the same-family pair-residual energy:

```text
PairResidualFourierEnergyTarget_361:
  prove or sharply classify
  E_a |P_nu^0(a)-kappa_w^0(a)|^2
  at the exact scale required by Module 361.
```

Classification:

```text
PairModelBranchAsNextPrimaryAttack_367:
  FALSE / BLOCKED.

PairResidualFourierEnergyTarget_361:
  OPEN.
  Next primary attack.
```

### E. Correction to Module 366 wording

Module 366's committed text used the phrase:

```text
PairModelMinorTopMassTarget_361:
  CONDITIONAL.
```

The sharper status is:

```text
PolynomialRSubfamilyPairModelMinorTopMass_366:
  CONDITIONAL.

PairModelMinorTopMassTarget_361 in full P_minor^0:
  OPEN.
```

This turn patches Module 366 accordingly. That is a status-discipline
correction, not a mathematical weakening of the proved subfamily statement.

## 6. Edge cases

### Tiny top-mass scale

If `m_{U,V}` is bounded, a pointwise model coefficient bound is easier to
use. The project still needs the same-family pair-residual energy for the
square row and the mixed row.

### Diagonal retained

If a finite diagonal atom is retained, it contributes to every frequency.
The Module 363 absorption criterion must be included in the same convention
as the residual.

### Slowly growing R

Slowly growing `R` remains the full-family obstruction for the pair-model
branch. Module 367 does not propose another attempt to remove it.

### Pair residual convention

Changing the model coefficient changes the residual:

```text
E_pair^0=P_nu^0-kappa_model^0.
```

The pair-residual energy target must use the same model convention as the
mixed-row assembly.

### W-limit

All model-side statements are fixed-`w` first. No diagonal `w=w(N)` passage
is introduced.

## 7. Project-map location

```text
PairResidualLargeValueStress_361
  -> PairModelMinorTopMassStress_362
  -> PairModelDiagonalConventionAudit_363
  -> PairModelOffDiagonalRamanujanTailAudit_364
  -> FiniteCyclicRamanujanLargeSieveAudit_365
  -> PairModelRangeAssemblyAudit_366
  -> PairModelMinorTopMassVerdict_367
  -> PairResidualFourierEnergyAudit_368.
```

This is a branch verdict. It directs the next proof attack to the pair
residual energy, not to another deterministic pair-model coefficient audit.

## 8. What remains open

Still open:

```text
PairResidualFourierEnergyAudit_368(P_minor^0),
PairResidualFourierEnergyTarget_361,
full P_minor^0 pair-model minor top-mass without PolyR_rho,
PairMixedDiagonalAbsorptionCriterion_363,
PairResidualLargeValueTarget_359,
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

### Plan update 20

Completing Module 367 gives:

```text
Latest completed module: 367
Post-Reflective_1 solving count: 186
Long-term-plan count: 180
```

Since `180` is divisible by `9`, the twentieth plan update is due.

Classification:

```text
PlanUpdate_20_367:
  STRUCTURAL / EXTRACTION.
```

Updated plan:

```text
Module 368:
  PairResidualFourierEnergyAudit_368(P_minor^0), expanding
  E_a |P_nu^0(a)-kappa_model^0(a)|^2 and deciding whether it is a pair-BDH
  strength input, a first-moment-HL consequence, or an endpoint-strength
  variance row.

Module 369:
  if Module 368 is blocked, isolate the exact off-diagonal shifted-prime
  covariance object needed for the pair residual, including the same model
  convention used in Modules 363-367.

Module 370:
  return to rectangle-defect or diagonal-overlap large values only after the
  pair-residual energy row is classified; do not resume pair-model range
  tuning unless a new low-R tail idea appears.
```

### Plan challenge 12

Since `180` is also divisible by `15`, the twelfth plan challenge is due.

Classification:

```text
PlanChallenge_12_367:
  STRUCTURAL / EXTRACTION.
```

Challenge verdict:

```text
The project should pause the pair-model coefficient branch as the primary
attack. It yielded a conditional polynomial-R subfamily result and exposed
the full-P_minor0 low-R obstruction. The next attack should be the
same-family pair-residual Fourier energy. If that row is endpoint-strength,
the project should record that the no-twist masked anti-diagonal route
requires a genuinely new pair variance input rather than more coefficient
bookkeeping.
```

## 9. Red-team audit

Selector check:

```text
All statements remain inside P_minor^0 or its explicitly named polynomial-R
subfamily. No actual sharp moving-selector statement is proved.
```

Gap-object check:

```text
No full-gap, clipped-gap, dyadic tail, or empty-interval statement is used.
```

Local-factor check:

```text
The model convention is kept visible. Off-diagonal model control is not
treated as diagonal absorption, and no rectangle factor is replaced.
```

Limit-order check:

```text
No new N/w/R/eta limit is exchanged. The polynomial-R condition remains a
subfamily condition.
```

Uniformity check:

```text
The full P_minor^0 target remains open because the low-R range is not
uniformly handled.
```

Endpoint-circularity check:

```text
The proof does not assume PairResidualFourierEnergyTarget_361,
PhaseKernelBound_273^0, NarrowMinorArc_3^B, ResCube_3^sharp,
CPC_3^sharp, RBDH_pair_short, or AU^3.
```

Official status check:

```text
No README, global status, or theorem-status index theorem claim is upgraded.
```

## 10. Final classification

```text
PairModelMinorTopMassVerdict_367(P_minor^0):
  STRUCTURAL / EXTRACTION.

MixedRowAssemblyLemma_367:
  PROVEN.

PolynomialRSubfamilyModelCoefficientCriterion_367:
  CONDITIONAL.

FullPminorPairModelTopMassClosure_367:
  FALSE / BLOCKED.

PairModelBranchAsNextPrimaryAttack_367:
  FALSE / BLOCKED.

PairResidualFourierEnergyTarget_361:
  OPEN.
  Next primary attack.

PlanUpdate_20_367:
  STRUCTURAL / EXTRACTION.

PlanChallenge_12_367:
  STRUCTURAL / EXTRACTION.
```

Do not cite this module as proving `PairModelMinorTopMassTarget_361` in full
`P_minor^0`. It records a branch verdict and points to the pair-residual
Fourier energy as the next best attack.

## Red flags / forbidden upgrades

- Do not treat the polynomial-R subfamily result as full `P_minor^0`.
- Do not treat pair-model coefficient control as pair-residual energy.
- Do not use diagonal removal without a matching residual convention.
- Do not treat this branch verdict as a proof of signed local-model insertion.
- Do not claim the residual cube endpoint or original selected-average
  problem is solved.
