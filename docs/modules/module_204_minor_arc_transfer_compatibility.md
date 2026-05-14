# Module 204: Boundary, W-range, and selector compatibility for minor arcs

## 1. Precise theorem / claim being advanced

Module 203 defined the conditional minor-arc package:

```text
NarrowMinorArc_3^B(D;R,eta).
```

This module asks whether that package can be used in the actual project
environment rather than only inside a cyclic Fourier model.

Define a transfer package:

```text
MinorArcTransfer_3^B(D;R,eta;w).
```

Conditional claim:

```text
NarrowMinorArc_3^B_model(D;R,eta;w)
  + MinorArcTransfer_3^B(D;R,eta;w)
    => M_minor^target(D;R,eta)=o(1).
```

Here `target` may be an interval model, a W-tricked prime model, a frozen
sharp selector, or the actual sharp moving selector, depending on which
transfer hypotheses have been supplied.

This implication is only a compatibility reduction. It does not prove the
minor-arc estimate, the transfer package, the residual cube endpoint, or any
global theorem.

## 2. Status label

`CONDITIONAL`

The deterministic implication is valid once the named transfer errors are
assumed small. The smallness of those transfer errors is open.

## 3. Definitions and variables

For a selector or model class `s`, write:

```text
f_s=nu_s-1,
B_{d,s}(n)=f_s(n+d)conj(f_s(n)).
```

Examples of `s` include:

```text
cyc        finite cyclic Fourier model,
int        interval model without cyclic wraparound,
W          W-tricked prime model,
frozen     frozen sharp dyadic selector,
smooth     smoothed finite-band selector,
sharp      actual sharp moving selector.
```

Let:

```text
Pi_minor^s=Fourier projection to Minor(R,eta) in model s.
```

In a common finite cyclic group, define:

```text
M_minor^s(D;R,eta)
  = (1/D) sum_{D<|d|<=2D}
      || Pi_minor^s B_{d,s} ||_{U^2}^4

  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)}
        |widehat{B_{d,s}}(xi)|^4.
```

When two models do not live on the same group, insert a transport map
`T_{a->b}` between their frequency spaces and define the adjacent transfer
error by:

```text
Err_4^minor(a->b;D;R,eta)
  = (1/D) sum_{D<|d|<=2D}
      || Pi_minor^b B_{d,b}
          - T_{a->b}(Pi_minor^a B_{d,a}) ||_{U^2}^4.
```

In the simpler common-group case this is:

```text
Err_4^minor(a->b;D;R,eta)
  = (1/D) sum_{D<|d|<=2D}
      || Pi_minor(B_{d,b}-B_{d,a}) ||_{U^2}^4.
```

The package must also track the zero frequency separately:

```text
xi=0 is excluded from M_minor.
```

Any zero-frequency correction belongs either to the mean term or to the
major-arc analysis, not to the nonzero minor-arc fourth moment.

## 4. Transfer assumptions

`MinorArcTransfer_3^B(D;R,eta;w)` consists of the following requirements.

### A. Adjacent model transfer in fourth-moment norm

For every adjacent transition in the intended chain:

```text
cyc -> int -> W -> smooth/frozen -> sharp,
```

one must prove:

```text
Err_4^minor(a->b;D;R,eta)=o(1)
```

in the same normalization as `M_minor`.

It is not enough to have a first moment estimate, a mean Hardy-Littlewood
estimate, or a pair-correlation estimate for a different object. The transfer
must control the projected derivative product:

```text
B_d(n)=f(n+d)conj(f(n)).
```

### B. Arc-boundary stability

Major and minor arcs must be separated with a buffer. Define an arc boundary
set:

```text
ArcBd(R,eta,eta')
  = Major(R,eta') \ Major(R,eta)
```

for a slightly enlarged parameter `eta'>eta`, or the analogous buffered
partition in the project convention.

The boundary contribution must satisfy:

```text
ArcBd_4(D;R,eta,eta')
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in ArcBd(R,eta,eta')}
        |widehat{B_d}(xi)|^4
    = o(1).
```

Without this term, small changes in the frequency model may move mass across
the major/minor boundary.

### C. W-limit order and W-admissibility

For every error term in this module, the required form is:

```text
lim_{w->infty} limsup_{N->infty}
  sup_{D,R,eta in range}
    Err(N,w;D,R,eta)=0.
```

The fixed-`w` limit must come before the `w->infty` limit. A diagonal choice
`w=w(N)` is allowed only after this two-stage estimate has been proved.

All auxiliary parameters from Module 203 must also be W-admissible:

```text
lambda_0,
Lambda,
mu(lambda),
K(lambda),
A_N,
Gamma_trans(lambda;D,R,eta,w).
```

In particular, the Fourier envelope `A_N` may not absorb W-growth so large
that the persistent-frequency condition becomes vacuous.

### D. Dyadic D-range uniformity

The estimate must be uniform over the dyadic shift range used in the endpoint
branch:

```text
D < |d| <= 2D,
D in D_range(N,Hcal).
```

At minimum, one needs:

```text
sup_{D in D_range(N,Hcal)} M_minor^target(D;R,eta)=o(1).
```

If the argument only works for one fixed `D`, it does not yet feed the
endpoint machinery.

### E. Interval boundary and cyclic wraparound

The cyclic model contains wraparound pairs. The interval model contains
boundary losses from:

```text
n <= |d|,
n+d outside the interval,
prefix and tail cutoffs,
moving dyadic endpoints.
```

The boundary transfer must control:

```text
BdInt_4(D)
  = (1/D) sum_{D<|d|<=2D}
      || Pi_minor(B_{d,cyc}-B_{d,int}) ||_{U^2}^4
    = o(1).
```

This condition is especially sensitive when `D` is close to the allowed upper
range.

### F. Prime-power and small-prime artifacts

The W-tricked model must separate the contribution of prime powers and small
prime artifacts. Define:

```text
PPErr_4(D)
  = (1/D) sum_{D<|d|<=2D}
      || Pi_minor(B_{d,W}-B_{d,W}^{prime-only}) ||_{U^2}^4.
```

The package requires:

```text
PPErr_4(D)=o(1)
```

with the W-limit order from part C.

### G. Selector transfer to the actual sharp moving window

The actual selector is:

```text
chi_alpha(p)=1_{||alpha p|| < 1/log p}.
```

Any route from smoothed, finite-band, or frozen selectors to this selector must
include the full selector-transfer line:

```text
boundary transfer,
moving-window transition control,
prefix safety,
denominator control,
tail control,
sharp-window transfer,
recursive-engine compatibility.
```

At the residual-product level the required error is:

```text
SelErr_4^minor(D)
  = (1/D) sum_{D<|d|<=2D}
      || Pi_minor(B_{d,sharp}-B_{d,model}) ||_{U^2}^4
    = o(1).
```

A selector approximation for `f` in a weak average norm is not sufficient
unless it is explicitly propagated through:

```text
B_d(n)=f(n+d)conj(f(n)).
```

### H. Threshold stability for large-spectrum inputs

Module 203 used sets of the form:

```text
Spec_d^minor(lambda)
  = { xi in Minor(R,eta) :
        |widehat{B_d}(xi)| >= lambda }.
```

These sets are unstable under small perturbations near the threshold. Therefore
one of the following must be supplied:

```text
1. transfer of the final fourth-moment quantity M_minor itself;
2. buffered threshold inclusions such as
     Spec_target(lambda)
       subset Spec_model(lambda/2) union ErrSpec(lambda);
3. a direct energy-transfer statement for Eng(I_shift),
   Eng(I_freq), and Eng(I_trans).
```

Without one of these, a model estimate for `ShiftMoment_q(lambda)`,
`MultMoment_r(lambda)`, or `Gamma_trans(lambda;D,R,eta,w)` does not
automatically transfer to the target selector.

### I. Non-tautological transverse input survives transfer

The Module 203 transverse input:

```text
Eng(I_trans(lambda)) <= Gamma_trans(lambda;D,R,eta,w)
```

must be proved in the same model as the minor-arc target, or transferred by one
of the admissible mechanisms above. It must not be replaced by:

```text
Gamma_trans approx M_minor(D),
```

or by an endpoint-strength assumption such as full `AU^3`, full
`CPC_3^sharp`, full `RBDH_pair_short`, or `ResCube_3^sharp`.

## 5. Proof / reduction

Assume first that two adjacent models `a` and `b` live on compatible frequency
spaces. Let:

```text
X_{d,a}=Pi_minor^a B_{d,a},
X_{d,b}=Pi_minor^b B_{d,b}.
```

By the triangle inequality in the Fourier `L^4` norm:

```text
||X_{d,b}||_{U^2}^4
  <= 8 ||X_{d,a}||_{U^2}^4
     + 8 ||X_{d,b}-T_{a->b}X_{d,a}||_{U^2}^4.
```

Averaging over `D<|d|<=2D` gives:

```text
M_minor^b(D;R,eta)
  <= 8 M_minor^a(D;R,eta)
     + 8 Err_4^minor(a->b;D;R,eta),
```

up to the arc-boundary term if the two minor-arc projections differ.

Iterating over a chain:

```text
s_0 -> s_1 -> ... -> s_k
```

gives:

```text
M_minor^{s_k}(D;R,eta)
  <= C_k M_minor^{s_0}(D;R,eta)
     + C_k sum_{j<k} Err_4^minor(s_j->s_{j+1};D;R,eta)
     + C_k ArcBd_4(D;R,eta,eta').
```

Therefore, if:

```text
M_minor^{s_0}(D;R,eta)=o(1)
```

and every transfer and arc-boundary error is `o(1)` uniformly in the required
range, then:

```text
M_minor^{s_k}(D;R,eta)=o(1).
```

Now take `s_0` to be the model where `NarrowMinorArc_3^B_model` has been
proved. Module 203 gives:

```text
NarrowMinorArc_3^B_model(D;R,eta;w)
  => M_minor^{s_0}(D;R,eta)=o(1).
```

The transfer inequality above then gives the conditional claim:

```text
NarrowMinorArc_3^B_model
  + MinorArcTransfer_3^B
    => M_minor^target(D;R,eta)=o(1).
```

No part of this proof estimates the transfer errors. They are new open inputs.

## 6. Review of Module 203 under this audit

Module 203 remains useful, but its inputs must be interpreted carefully.

The shift-moment and multiplicity-moment sufficient conditions are
model-dependent:

```text
ShiftMoment_q(lambda),
MultMoment_r(lambda).
```

If these are proved only in a cyclic or smoothed model, they do not
automatically apply to the sharp moving selector. The large-spectrum sets may
change under perturbation, and the changes can occur exactly at the thresholds
where the dyadic decomposition is trying to gain power.

The safer path is:

```text
prove the model NarrowMinorArc package,
then transfer the final M_minor fourth moment.
```

The more delicate path is:

```text
transfer each large-spectrum input with threshold buffers.
```

Either path is acceptable if written explicitly. Neither path is currently
proved.

This is the main correction to keep in view: the refined criterion narrowed
the obstruction, but it did not remove the selector-transfer burden.

## 7. Edge cases

- Negative shifts `d` must be included with the same boundary bookkeeping as
  positive shifts.
- If `D` approaches the interval length, cyclic wraparound can dominate unless
  excluded by the project range.
- Frequencies close to major-arc boundaries may move across the partition
  under denominator changes or W-trick normalization.
- The zero frequency is excluded from the minor-arc target; it must not be
  reintroduced through a transport map.
- Prime powers may be negligible in first moment but still need projected
  fourth-moment control for the residual product.
- W-growth hidden inside `A_N` can destroy the persistent-frequency gain from
  Module 203.
- Threshold sets `Spec_d^minor(lambda)` are not stable unless buffered.
- Selector errors for `f` may amplify after forming
  `f(n+d)conj(f(n))`, especially if the weights are unbounded.
- Bounds for one dyadic `D` do not automatically sum or take suprema over the
  endpoint dyadic range.

## 8. Where it fits in the project map

The current branch is:

```text
Module 197
  -> density/energy criterion
Module 201
  -> obstruction tree
Module 203
  -> narrowed conditional large-spectrum package
Module 204
  -> transfer compatibility audit for that package.
```

The module shows that Phase B has two distinct open parts:

```text
analytic minor-arc cancellation,
model-to-target transfer.
```

The next scheduled iteration is:

```text
Module 205: second 9-iteration plan update.
```

That update should decide whether Phase B has become a useful checkable route
or whether the project should pivot back to major-arc local-model matching or
selector-transfer foundations.

## 9. What remains open

This module does not prove:

- `NarrowMinorArc_3^B` in any model;
- low-level minor-arc leakage control;
- `ShiftMoment_q(lambda)`;
- `MultMoment_r(lambda)`;
- a non-tautological `Gamma_trans`;
- arc-boundary fourth-moment stability;
- interval boundary transfer;
- W-admissible minor-arc transfer;
- prime-power fourth-moment removal;
- sharp moving-selector transfer;
- threshold stability for large-spectrum sets;
- `ProjectedLocalMatch_3^major`;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not use a cyclic or smoothed `NarrowMinorArc_3^B` estimate as an actual
  sharp moving-selector estimate without `MinorArcTransfer_3^B`.
- Do not hide W-growth in `A_N` or in an unnamed `o(1)`.
- Do not choose a diagonal `w(N)` before proving fixed-`w` estimates followed
  by the `w->infty` limit.
- Do not transfer large-spectrum sets by name without threshold stability.
- Do not replace `Gamma_trans` with the endpoint target.
- Do not use ordinary pair-BDH, first-moment Hardy-Littlewood, or mean
  rectangle estimates as substitutes for projected residual fourth-moment
  transfer.
- Do not claim the residual cube endpoint, the original problem, the all-alpha
  theorem, the unconditional finite-type theorem, `RBDH_pair_short`,
  `CPC_3^sharp`, or `AU^3`.
