# Module 296: Low-level counting-barrier audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

This module performs the narrow audit selected by Module 295.

Define:

```text
LowLevelCountingBarrierAudit_296(P_minor^0).
```

The claim advanced is a classification of the low-level counting route:

```text
Pure counting of all below-lambda_min minor frequencies does not close the
low-level row from the current P_minor^0 definitions.
```

The useful extraction is that the exact fourth-moment reconstruction inherited
from Module 203 is sharper than pure counting:

```text
M_low,0(D;R,eta)
  <= lambda_min^2 E2_minor^0(D;R,eta).
```

Thus the next honest low-level target is not another counting argument, but
a same-family energy-tail audit.

Verdict:

```text
LowLevelCountingBarrierAudit_296(P_minor^0):
  STRUCTURAL / EXTRACTION.

PureCountingLowLevelClosure_296:
  FALSE / BLOCKED with the current P_minor^0 data.

LowLevelEnergyTailCriterion_296:
  STRUCTURAL / EXTRACTION.

LowLevelEnergyTailTarget_296(P_minor^0):
  OPEN.

LowLevelBudgetP0_284:
  OPEN.
```

This module proves no low-level smallness.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is an audit of one proposed route. It does not prove
`LowLevelBudgetP0_284`, `LowLevelCutoffP0_283`,
`ThresholdBudgetP0Closure_284(q,r)`, `SidePkg_291`,
`PhaseKernelBound_273^0`, or any endpoint theorem.

## 3. Definitions and variables

Work inside `P_minor^0`:

```text
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
N^{delta_D}<=D<=N^{1-delta_D},
2D<=N/16.
```

Use:

```text
f_0(n)=nu_0(n)-1,
B_d^0(n)=f_0(n+d)conj(f_0(n)),
beta_0(d,xi)=widehat{B_d^0}(xi),
A_N^0=sup_{d,xi}|beta_0(d,xi)|,
m_minor^0=#Minor_0(R,eta),
C_D=D^(-1)# { d:D<|d|<=2D },
lambda_min=A_N^0 N^{-kappa_lambda}.
```

Define the low-level set:

```text
Low_0(lambda_min)
  =
  { (d,xi):
      D<|d|<=2D,
      xi in Minor_0(R,eta),
      |beta_0(d,xi)|<lambda_min }.
```

Define the actual low-level fourth-moment piece:

```text
M_low,0(D;R,eta)
  =
  D^(-1) sum_{(d,xi) in Low_0(lambda_min)}
    |beta_0(d,xi)|^4.
```

Define the full local minor-arc second energy:

```text
E2_minor^0(D;R,eta)
  =
  D^(-1) sum_{D<|d|<=2D}
    sum_{xi in Minor_0(R,eta)}
      |beta_0(d,xi)|^2.
```

Also define:

```text
LowEng_0
  =
  D^(-1) sum_{(d,xi) in Low_0(lambda_min)}
    |beta_0(d,xi)|^2.
```

Then:

```text
LowEng_0 <= E2_minor^0(D;R,eta).
```

## 4. Assumptions

This module assumes only Modules 203 and 278-295 plus the active status
ledger.

It does not assume:

```text
LowLevelEnergyTailTarget_296,
LowLevelCountingBarrier_294,
LowLevelBudgetP0_284,
LowLevelCutoffP0_283,
LowLevelCountingBarrierAudit_296,
ThresholdBudgetP0_283,
ThresholdBudgetP0Closure_284(q,r),
SideRowsP0Ready_283,
SidePkg_291,
SidePkgReady_293,
DegRowsP0Small_282,
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
PhaseKernelBound_273,
TransverseGateProofPkg_276,
TransIncBound_269,
MinorArcTransfer_3^B,
NarrowMinorArc_3^B,
selector transfer,
ProjectedModelNeutrality_3^major,
WProjectedLocalMatch_3^major,
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the original selected-average problem,
the all-alpha theorem,
or the unconditional finite-type theorem.
```

## 5. Proof / disproof / reduction

### A. Exact low-level reconstruction inherited from Module 203

Module 203 states the low-level row in the form:

```text
lambda_0^2 E2_minor(D)=o(1),
```

where `lambda_0` is the low threshold of the dyadic decomposition.

In `P_minor^0`, the low threshold is:

```text
lambda_min=A_N^0 N^{-kappa_lambda}.
```

Therefore the direct local translation is:

```text
LowLevelEnergyTailTarget_296(P_minor^0):
  lambda_min^2 E2_minor^0(D;R,eta)=o_W(1)
```

with all `P_minor^0` uniformity and limiting-order conventions included.

This translation also corrects a possible notation trap:

```text
Module 203 uses lambda_0 as the lower threshold.
Module 278 uses lambda_j=2^{-j}A_N^0 and lambda_min for the lower cutoff.
```

The local row must use `lambda_min`, not the top shell `lambda_0=A_N^0` from
the Module 278 indexing convention.

### B. Energy-tail inequality

On `Low_0(lambda_min)`:

```text
|beta_0(d,xi)|<lambda_min.
```

Hence:

```text
|beta_0(d,xi)|^4
  <=
  lambda_min^2 |beta_0(d,xi)|^2.
```

Summing gives:

```text
M_low,0(D;R,eta)
  <=
  lambda_min^2 LowEng_0
  <=
  lambda_min^2 E2_minor^0(D;R,eta).
```

Substituting the cutoff:

```text
lambda_min^2 E2_minor^0(D;R,eta)
  =
  (A_N^0)^2 N^{-2 kappa_lambda}
    E2_minor^0(D;R,eta).
```

Thus:

```text
LowLevelEnergyTailCriterion_296:
  if
    (A_N^0)^2 N^{-2 kappa_lambda} E2_minor^0(D;R,eta)=o_W(1)
  uniformly over P_minor^0,
  then the fourth-moment low-level piece M_low,0 is o_W(1).
```

This is a criterion only. The required second-energy bound is not proved in
this module.

### C. Pure counting barrier

Module 294 recorded the pure counting estimate:

```text
M_low,0(D;R,eta)
  <=
  C_D m_minor^0 (A_N^0)^4 N^{-4 kappa_lambda}.
```

This is valid but too crude to close from the current declarations alone.

The declared family permits:

```text
m_minor^0 as large as essentially the whole nonzero frequency set,
kappa_lambda<1/100,
and no smallness assumption on A_N^0.
```

Therefore the pure counting route would need an extra size input such as:

```text
C_D m_minor^0 (A_N^0)^4 N^{-4 kappa_lambda}=o_W(1).
```

That input is not a consequence of the definitions of `P_minor^0`.

Classification:

```text
PureCountingLowLevelClosure_296:
  FALSE / BLOCKED with the current P_minor^0 data.
```

The point is not that the inequality is false. The point is that the
inequality is only a barrier, and the barrier is not known to be small.

### D. Why this is better than another counting pass

The energy-tail criterion is strictly better aligned with the original
fourth-moment decomposition:

```text
below threshold:
  |beta|^4 <= lambda_min^2 |beta|^2.
```

Pure counting discards all second-energy information and pays the full minor
frequency count:

```text
#Minor_0(R,eta).
```

Since `Minor_0(R,eta)` can be large, another pure counting audit would only
repeat the same blockage. The next useful question is whether
`E2_minor^0(D;R,eta)` has a same-family bound strong enough after multiplying
by `lambda_min^2`.

### E. What an acceptable future proof would need

To close the low-level row through this route, a future module must prove:

```text
(A_N^0)^2 N^{-2 kappa_lambda} E2_minor^0(D;R,eta)=o_W(1)
```

uniformly over:

```text
N,w,b,D,R,eta,
both signs of d,
the declared W-residue convention,
the declared Fourier normalization,
the declared major/minor arc boundary convention,
and the final limiting order.
```

It must not use:

```text
M_minor(D)=o(1),
NarrowMinorArc_3^B,
PhaseKernelBound_273^0,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
or selector transfer
```

as an input.

## 6. Edge cases

If:

```text
A_N^0=0,
```

then `Lambda_0` is empty and `M_low,0=0`. This degenerate tuple is not a
uniform proof of the row.

If:

```text
m_minor^0=0,
```

then the low-level minor-arc set is empty. This is also degenerate.

If a future estimate proves:

```text
E2_minor^0(D;R,eta)=O_W(1)
and
A_N^0=O_W(1),
```

then the factor `N^{-2 kappa_lambda}` would make the energy-tail target
small. Those bounds are not asserted in the current ledger.

If `A_N^0` grows with the W-tricked prime weight or if `E2_minor^0` has
unpaid logarithmic, W, dyadic, or residue losses, the energy-tail route may
still fail.

## 7. Project-map location

The local map after this audit is:

```text
LowLevelEnergyTailTarget_296
  -> LowLevelBudgetP0_284
  -> ThresholdBudgetP0Closure_284(q,r)
  -> SideRowsP0Ready_283 / SidePkg_291
  -> PhaseKernelBound_273^0
  -> NarrowMinorArc_3^B
  -> ResCube_3^sharp
  -> original selected-average problem.
```

This module advances only the first label by identifying the correct target.
It does not prove the target.

## 8. What remains open

The open low-level row is now sharper:

```text
LowLevelEnergyTailTarget_296(P_minor^0):
  (A_N^0)^2 N^{-2 kappa_lambda} E2_minor^0(D;R,eta)=o_W(1).
```

Still open:

```text
LowLevelBudgetP0_284,
LowLevelCutoffP0_283,
ThresholdBudgetP0Closure_284(q,r),
SidePkg_291,
SidePkgReady_293,
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the original selected-average problem.
```

## 9. Forbidden upgrades

Do not treat:

```text
M_low,0 <= lambda_min^2 E2_minor^0
```

as low-level smallness. It is only a reduction.

Do not treat pure counting as a proof unless the displayed counting barrier is
proved `o_W(1)` in the same parameter family.

Do not transfer this local W-cyclic model statement to the actual sharp
moving selector. Do not replace a full-gap statement by a clipped or tail
statement. Do not replace `Sigma_w(d,h)` by `kappa_w(d)^2` pointwise.

## 10. Next target

The next target should remain inside the low-level branch:

```text
Module 297:
  E2MinorEnergyTailAudit_297(P_minor^0).
```

It should test whether known same-family second-energy tools can prove,
or fail to prove,

```text
(A_N^0)^2 N^{-2 kappa_lambda} E2_minor^0(D;R,eta)=o_W(1).
```

If that audit blocks, the project should leave the low-level branch and move
to the shift/frequency removal budgets named in Module 284.
