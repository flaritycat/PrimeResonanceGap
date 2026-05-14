# Module 203: Refined conditional minor-arc criterion after the challenge

## 1. Precise theorem / claim being advanced

This module turns the Module 201 obstruction tree into a named conditional
minor-arc package. The package is deliberately narrow: it proves the
minor-arc fourth-moment target only if low-level leakage, bad-shift energy,
persistent-frequency energy, and transverse incidence energy are all controlled
in quantified forms.

Define the package:

```text
NarrowMinorArc_3^B(D;R,eta)
```

for the residual derivative products:

```text
B_d(n)=f(n+d)conj(f(n)),   f=nu-1.
```

Conditional claim:

```text
NarrowMinorArc_3^B(D;R,eta)
  => M_minor(D)=o(1),
```

where:

```text
M_minor(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)} |widehat{B_d}(xi)|^4.
```

Challenge response:

```text
The package is useful only if at least one of its inputs is supplied by a
checkable moment, multiplicity, or incidence estimate that is smaller than
M_minor(D)=o(1).
```

The shift and frequency inputs below are stated in checkable moment forms. The
transverse incidence input remains the dangerous part: if it is supplied only
by restating `M_minor(D)=o(1)`, the package has no analytic value.

## 2. Status label

`CONDITIONAL`

The dyadic implication is deterministic once the named hypotheses are assumed.
The hypotheses themselves are open analytic inputs.

## 3. Definitions and variables

Use the finite cyclic Fourier model or a transferred interval model. Let:

```text
f=nu-1
B_d(n)=f(n+d)conj(f(n))
widehat{B_d}(xi)=E_n B_d(n)e(-xi n)
Minor(R,eta)={xi != 0}\Major(R,eta)
```

For `lambda>0`:

```text
Spec_d^minor(lambda)
  = { xi in Minor(R,eta) : |widehat{B_d}(xi)| >= lambda }.
```

Define:

```text
E2_minor(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)} |widehat{B_d}(xi)|^2,

E_d(lambda)
  = sum_{xi in Spec_d^minor(lambda)} |widehat{B_d}(xi)|^2,

N_xi(lambda)
  = # { d : D<|d|<=2D, xi in Spec_d^minor(lambda) }.
```

Let:

```text
I_lambda
  = { (d,xi) : D<|d|<=2D, xi in Spec_d^minor(lambda) }.
```

For an incidence set `I subset I_lambda`, define its averaged energy:

```text
Eng(I)
  = (1/D) sum_{(d,xi) in I} |widehat{B_d}(xi)|^2.
```

Fix a low threshold `lambda_0`, an upper envelope `A_N`, and a dyadic grid:

```text
Lambda = { lambda_j : lambda_0 <= lambda_j <= A_N }.
```

For each `lambda in Lambda`, choose thresholds:

```text
mu(lambda) > 0,
K(lambda) >= 1.
```

Define bad shifts:

```text
BadShift(lambda)
  = { d : E_d(lambda) > mu(lambda) }.
```

Define persistent minor frequencies:

```text
BadFreq(lambda)
  = { xi in Minor(R,eta) : N_xi(lambda) > K(lambda) }.
```

Decompose incidences disjointly:

```text
I_shift(lambda)
  = { (d,xi) in I_lambda : d in BadShift(lambda) },

I_freq(lambda)
  = { (d,xi) in I_lambda :
        d notin BadShift(lambda), xi in BadFreq(lambda) },

I_trans(lambda)
  = I_lambda \ (I_shift(lambda) union I_freq(lambda)).
```

The transverse set is the region where no single shift and no single minor
frequency is carrying the obstruction by itself.

## 4. Assumptions

`NarrowMinorArc_3^B(D;R,eta)` consists of the following assumptions.

### A. Low-level leakage control

```text
lambda_0^2 E2_minor(D)=o(1).
```

### B. Bad-shift energy control

```text
sum_{lambda in Lambda}
  lambda^2 Eng(I_shift(lambda)) = o(1).
```

A checkable sufficient form is: for some `q>1`,

```text
ShiftMoment_q(lambda)
  = (1/D) sum_{D<|d|<=2D} E_d(lambda)^q
```

satisfies:

```text
sum_{lambda in Lambda}
  lambda^2 mu(lambda)^(1-q) ShiftMoment_q(lambda)
  = o(1).
```

This is smaller than the endpoint if `ShiftMoment_q` is estimated by a
separate shift-energy moment theorem rather than by `M_minor(D)`.

### C. Persistent-frequency energy control

```text
sum_{lambda in Lambda}
  lambda^2 Eng(I_freq(lambda)) = o(1).
```

A checkable sufficient form is: for some `r>1`, with:

```text
MultMoment_r(lambda)
  = (1/D) sum_{xi in Minor(R,eta)} N_xi(lambda)^r,
```

and with the Fourier envelope:

```text
|widehat{B_d}(xi)| <= A_N,
```

one has:

```text
sum_{lambda in Lambda}
  lambda^2 A_N^2 K(lambda)^(1-r) MultMoment_r(lambda)
  = o(1).
```

This is smaller than the endpoint if `MultMoment_r` is supplied by a
minor-frequency multiplicity estimate.

### D. Transverse incidence control

```text
sum_{lambda in Lambda}
  lambda^2 Eng(I_trans(lambda)) = o(1).
```

A non-tautological transverse input must give a bound:

```text
Eng(I_trans(lambda)) <= Gamma_trans(lambda;D,R,eta,w)
```

such that:

```text
sum_{lambda in Lambda}
  lambda^2 Gamma_trans(lambda;D,R,eta,w)=o(1),
```

and `Gamma_trans` is obtained without using `M_minor(D)=o(1)` or an
equivalent endpoint statement. This is the part most likely to be
endpoint-strength if it is not made more explicit.

## 5. Proof / disproof / reduction

By the Module 197 energy-tail decomposition:

```text
M_minor(D)
  <= lambda_0^2 E2_minor(D)
     + C sum_{lambda in Lambda}
          lambda^2 E_minor(>=lambda;D),
```

where:

```text
E_minor(>=lambda;D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Spec_d^minor(lambda)}
        |widehat{B_d}(xi)|^2.
```

Equivalently:

```text
E_minor(>=lambda;D)=Eng(I_lambda).
```

For each `lambda`, the incidence decomposition is disjoint:

```text
I_lambda
  = I_shift(lambda)
    disjoint union I_freq(lambda)
    disjoint union I_trans(lambda).
```

Hence:

```text
Eng(I_lambda)
  = Eng(I_shift(lambda))
    + Eng(I_freq(lambda))
    + Eng(I_trans(lambda)).
```

The assumed low-level, shift, frequency, and transverse estimates therefore
give:

```text
M_minor(D)=o(1).
```

### Checkable shift moment reduction

On `BadShift(lambda)`:

```text
E_d(lambda) > mu(lambda).
```

For `q>1`:

```text
E_d(lambda) 1_{E_d(lambda)>mu(lambda)}
  <= mu(lambda)^(1-q) E_d(lambda)^q.
```

Therefore:

```text
Eng(I_shift(lambda))
  = (1/D) sum_{d in BadShift(lambda)} E_d(lambda)
  <= mu(lambda)^(1-q) ShiftMoment_q(lambda).
```

This proves the stated sufficient form for bad-shift energy.

### Checkable persistent-frequency reduction

Using `|widehat{B_d}(xi)| <= A_N`:

```text
Eng(I_freq(lambda))
  <= (A_N^2/D)
     sum_{xi in BadFreq(lambda)} N_xi(lambda).
```

For `r>1`:

```text
N_xi(lambda) 1_{N_xi(lambda)>K(lambda)}
  <= K(lambda)^(1-r) N_xi(lambda)^r.
```

Thus:

```text
Eng(I_freq(lambda))
  <= A_N^2 K(lambda)^(1-r) MultMoment_r(lambda).
```

This proves the stated sufficient form for persistent-frequency energy.

### Why the transverse input is not automatically useful

For `I_trans(lambda)`, both:

```text
E_d(lambda) <= mu(lambda),
N_xi(lambda) <= K(lambda)
```

hold on the relevant shifts and frequencies. These two facts alone do not
force the total energy to be small. A broad incidence cloud can have many
moderate coefficients.

Therefore the transverse hypothesis is the critical analytic input. It must
come from a new incidence, restriction, inverse, or correlation theorem. If it
is proved only by:

```text
Eng(I_trans(lambda)) <= E_minor(>=lambda;D)
```

or by assuming `M_minor(D)=o(1)`, then the package is circular.

## 6. Edge cases

- The dyadic grid size must be budgeted. Logarithmic losses in
  `A_N/lambda_0` cannot be hidden.
- `A_N` may be large for W-tricked prime weights; the persistent-frequency
  sufficient form is useful only if the multiplicity moment beats this
  envelope.
- Choosing `mu(lambda)` too small makes the bad-shift term hard; choosing it
  too large leaves too much transverse energy.
- Choosing `K(lambda)` too small makes many frequencies persistent; choosing
  it too large weakens the multiplicity gain.
- Bad-shift and persistent-frequency decompositions depend on the cyclic
  Fourier model and must be rechecked after interval transfer.
- The transverse input must not be smuggled in through endpoint-equivalent
  language such as full `AU^3`, full `ResCube_3^sharp`, or endpoint-grade
  `RBDH_pair_short`.
- Major-arc leakage, zero frequency, collision hyperplanes, prime powers, and
  selector transfer remain outside this package.

## 7. Where it fits in the project map

Module 203 answers the Module 202 challenge:

```text
Module 201
  -> obstruction tree
Module 202
  -> plan challenge: narrow Phase B
Module 203
  -> named conditional package with checkable shift/frequency moment forms
     and an explicit transverse-risk input.
```

The next module must test whether this package survives the actual project
environment:

```text
Module 204
  -> boundary, W-range, and selector compatibility for minor arcs.
```

## 8. What remains open

This module does not prove:

- low-level `L^2` control;
- the shift moment estimates `ShiftMoment_q(lambda)`;
- the multiplicity estimates `MultMoment_r(lambda)`;
- a non-tautological transverse incidence bound `Gamma_trans`;
- the boundary, W-range, prime-power, or selector transfer of this package;
- any major-arc estimate using `Omega_w`;
- `ProjectedLocalMatch_3^major`;
- minor-arc fourth-moment decay unconditionally;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not cite `NarrowMinorArc_3^B` without all four input classes.
- Do not treat the transverse input as checkable unless a genuine incidence,
  restriction, inverse, or correlation theorem supplies `Gamma_trans`.
- Do not estimate `Gamma_trans` by assuming the endpoint.
- Do not forget the low-level `L^2` term.
- Do not hide W-trick size in `A_N`.
- Do not transfer cyclic, smoothed, frozen, projected, or model estimates to
  the actual sharp moving selector without the full transfer package.
