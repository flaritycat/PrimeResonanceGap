# Module 270: Threshold-removal audit for the transverse incidence core

## 1. Precise theorem / claim being advanced

This module audits what can be obtained from the bad-shift and
persistent-frequency removals in `NarrowMinorArc_3^B` after Module 269.

Define:

```text
ThresholdRemovalAudit_270(s;D,R,eta,w).
```

The audit asks whether the row-energy ceiling:

```text
E_{d,s}(lambda) <= mu(lambda)
```

and the column-multiplicity ceiling:

```text
N_{xi,s}(lambda) <= K(lambda)
```

can make the transverse contribution small without a new incidence theorem.

The verdict is:

```text
Threshold-only closure is not established by the current ledger.
```

The ceilings are useful diagnostics, but they close the transverse term only
under additional quantitative moment estimates and a compatible threshold
window. Those estimates are not proved here and are not already available in
the active project ledger.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module derives a deterministic threshold audit. It does not prove
`TransIncBound_269`, `NarrowMinorArc_3^B`, or any endpoint estimate.

## 3. Definitions and variables

Use the notation of Modules 203 and 269. For the declared selector/model class
`s`:

```text
f_s=nu_s-1
B_{d,s}(n)=f_s(n+d)conj(f_s(n))
widehat{B_{d,s}}(xi)=E_n B_{d,s}(n)e(-xi n)
Minor(R,eta)={xi != 0}\Major(R,eta)
```

For `lambda in Lambda`:

```text
Spec_{d,s}^minor(lambda)
  = { xi in Minor(R,eta) :
        |widehat{B_{d,s}}(xi)| >= lambda },

I_lambda(s)
  = { (d,xi) :
        D<|d|<=2D,
        xi in Spec_{d,s}^minor(lambda) }.
```

The row energy and column multiplicity are:

```text
E_{d,s}(lambda)
  = sum_{xi in Spec_{d,s}^minor(lambda)}
      |widehat{B_{d,s}}(xi)|^2,

N_{xi,s}(lambda)
  = # { d : D<|d|<=2D,
             xi in Spec_{d,s}^minor(lambda) }.
```

For thresholds `mu(lambda)>0` and `K(lambda)>=1`:

```text
BadShift_s(lambda)
  = { d : E_{d,s}(lambda)>mu(lambda) },

BadFreq_s(lambda)
  = { xi in Minor(R,eta) :
        N_{xi,s}(lambda)>K(lambda) }.
```

The ordered decomposition is:

```text
I_lambda(s)
  = I_shift_s(lambda)
    disjoint union I_freq_s(lambda)
    disjoint union I_trans_s(lambda),
```

where bad shifts are removed before persistent frequencies.

Let:

```text
C_D = D^(-1) # { d : D<|d|<=2D },
m_minor(R,eta)=#Minor(R,eta),
A_N = sup_{d,xi} |widehat{B_{d,s}}(xi)|.
```

For `q>1` and `r>1`, define the moment diagnostics:

```text
ShiftMoment_{q,s}(lambda)
  = (1/D) sum_{D<|d|<=2D} E_{d,s}(lambda)^q,

MultMoment_{r,s}(lambda)
  = (1/D) sum_{xi in Minor(R,eta)} N_{xi,s}(lambda)^r.
```

## 4. Assumptions

This module assumes:

- the finite Fourier model or a named transferred interval model;
- the same selector/model class `s` throughout;
- the same dyadic shift range `D<|d|<=2D`;
- zero frequency excluded before forming `Minor(R,eta)`;
- the ordered bad-shift then bad-frequency decomposition of Module 269.

It does not assume:

```text
ShiftMoment_{q,s} smallness,
MultMoment_{r,s} smallness,
TransIncBound_269,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
selector transfer,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
ProjectedMajorTarget_3^B,
WProjectedLocalMatch_3^major,
ProjectedModelNeutrality_3^major,
the original selected-average problem,
the all-alpha theorem,
or the unconditional finite-type theorem.
```

## 5. Proof / disproof / reduction

### A. The threshold audit functional

Define the threshold-only upper envelope:

```text
Theta_270(lambda;mu,K,q,r,s)
  =
    mu(lambda)^(1-q) ShiftMoment_{q,s}(lambda)
    + A_N^2 K(lambda)^(1-r) MultMoment_{r,s}(lambda)
    + min(
        C_D mu(lambda),
        A_N^2 K(lambda) m_minor(R,eta) / D
      ).
```

The associated conditional target is:

```text
ThresholdOnlyClosure_270:
  lambda_0^2 E2_minor(D)
    + C sum_{lambda in Lambda}
        lambda^2 Theta_270(lambda;mu,K,q,r,s)
    = o(1).
```

If this target were proved by external estimates for the declared class `s`,
then the large-spectrum part of `NarrowMinorArc_3^B` would be controlled by
threshold removals and trivial transverse ceilings. This is a conditional
criterion, not an established result.

### B. Bad-shift removal

On `BadShift_s(lambda)`:

```text
E_{d,s}(lambda)>mu(lambda).
```

For `q>1`:

```text
E_{d,s}(lambda) 1_{E_{d,s}(lambda)>mu(lambda)}
  <= mu(lambda)^(1-q) E_{d,s}(lambda)^q.
```

Therefore:

```text
Eng_s(I_shift_s(lambda))
  <= mu(lambda)^(1-q) ShiftMoment_{q,s}(lambda).
```

This term wants `mu(lambda)` large.

### C. Persistent-frequency removal

Using `|widehat{B_{d,s}}(xi)|<=A_N`:

```text
Eng_s(I_freq_s(lambda))
  <= A_N^2 K(lambda)^(1-r) MultMoment_{r,s}(lambda).
```

This term wants `K(lambda)` large.

### D. Trivial transverse ceilings

On `I_trans_s(lambda)`:

```text
E_{d,s}(lambda)<=mu(lambda),
N_{xi,s}(lambda)<=K(lambda).
```

The row ceiling gives:

```text
Eng_s(I_trans_s(lambda)) <= C_D mu(lambda).
```

The column ceiling gives:

```text
Eng_s(I_trans_s(lambda))
  <= A_N^2 K(lambda) m_minor(R,eta) / D.
```

Hence:

```text
Eng_s(I_trans_s(lambda))
  <= min(
       C_D mu(lambda),
       A_N^2 K(lambda) m_minor(R,eta) / D
     ).
```

These terms want `mu(lambda)` and `K(lambda)` small. This is the basic
threshold tension: the removals need large thresholds, while the trivial
transverse ceilings need small thresholds.

### E. Optimized diagnostic barriers

If one tries to close the transverse term with the row ceiling alone, the
lambda-level expression:

```text
ShiftMoment_{q,s}(lambda) mu^(1-q) + C_D mu
```

is minimized, up to constants depending on `q`, at:

```text
mu^q approx ShiftMoment_{q,s}(lambda) / C_D.
```

The resulting barrier is:

```text
C_q C_D^((q-1)/q) ShiftMoment_{q,s}(lambda)^(1/q).
```

Thus a row-only threshold route would require:

```text
sum_{lambda in Lambda}
  lambda^2 C_D^((q-1)/q)
  ShiftMoment_{q,s}(lambda)^(1/q)
  = o(1),
```

in addition to the low-level term and selector/transfer side rows.

Similarly, a column-only threshold route would require, up to constants
depending on `r`:

```text
sum_{lambda in Lambda}
  lambda^2 A_N^2
  (m_minor(R,eta)/D)^((r-1)/r)
  MultMoment_{r,s}(lambda)^(1/r)
  = o(1).
```

Neither diagnostic barrier is proved in the current ledger. They are useful
because they show exactly what a threshold-only closure would have to beat.

### F. What remains after the audit

The audit leaves two possible future routes:

```text
Route 1:
  prove ThresholdOnlyClosure_270 from genuine shift and multiplicity moment
  estimates smaller than the endpoint.

Route 2:
  prove a new transverse incidence/restriction/correlation theorem improving
  the trivial term
    min(C_D mu, A_N^2 K m_minor/D)
  for the exact weighted graph I_trans_s(lambda).
```

Route 1 is not available without new moment estimates. Route 2 is the reason
Module 271 should expand the large Fourier coefficient and record the exact
phase equations behind multiple transverse incidences.

## 6. Edge cases

- `K(lambda)` is integer-valued; continuous optimization is only a diagnostic.
- The grid size `#Lambda` must be paid for in the final lambda-sum.
- If `A_N` grows with W-tricked weights, the column route can be unusable even
  when multiplicities look sparse.
- If `m_minor(R,eta)` is essentially the whole nonzero frequency set, the
  column ceiling has little strength unless `D` is very large.
- If `q` or `r` is close to `1`, the moment gain can disappear into threshold
  losses.
- `N_{xi,s}(lambda)` is the total multiplicity before removing bad shifts;
  redefining it after bad-shift removal changes the package.
- The low-level term `lambda_0^2 E2_minor(D)` is still required.
- Major/minor boundary leakage, prime powers, W-residue restrictions,
  truncation tails, and selector transfer remain outside this threshold audit.

## 7. Where it fits in the project map

```text
Module 203
  -> NarrowMinorArc_3^B with low-level, shift, frequency, transverse rows

Module 269
  -> TransIncCore_269, the exact weighted transverse graph

Module 270
  -> ThresholdRemovalAudit_270, the threshold-only feasibility test
```

The next useful step is:

```text
Module 271:
  expand a transverse large Fourier coefficient of B_{d,s} into shifted
  f_s-correlations and record the exact phase equations generated by multiple
  transverse incidences.
```

## 8. What remains open

This module does not prove:

- `ThresholdOnlyClosure_270`;
- `ShiftMoment_{q,s}` or `MultMoment_{r,s}` estimates;
- `TransIncBound_269`;
- transverse energy smallness;
- `NarrowMinorArc_3^B`;
- `MinorArcTransfer_3^B`;
- selector transfer to the actual sharp moving selector;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- `ProjectedMajorTarget_3^B`, `WProjectedLocalMatch_3^major`,
  or `ProjectedModelNeutrality_3^major`;
- the original selected-average problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not cite row and column ceilings as a proof of transverse smallness.
- Do not treat optimized threshold barriers as estimates.
- Do not choose `mu(lambda)` and `K(lambda)` separately for different rows
  after the decomposition has been fixed.
- Do not estimate `ShiftMoment` or `MultMoment` by assuming the minor-arc
  endpoint.
- Do not move between selector/model classes without a named transfer theorem.
- Do not use `ThresholdOnlyClosure_270` as an input to prove itself or the
  endpoint it would imply.
