# Module 269: Exact transverse-incidence object in NarrowMinorArc_3^B

## 1. Precise theorem / claim being advanced

This module extracts the exact transverse-incidence object left open by
`NarrowMinorArc_3^B`.

Define:

```text
TransIncCore_269(s;lambda,D,R,eta,w).
```

Here `s` is the declared selector/model class. It may be cyclic, interval,
W-model, smoothed, frozen, or sharp only when the corresponding transfer rows
are explicitly supplied. This module does not move between those classes.

The object is the incidence-energy term:

```text
Eng_trans_269(lambda;s,D,R,eta,w)
  = Eng_s(I_trans_s(lambda)).
```

The future analytic target is not this definition, but a non-tautological
bound:

```text
TransIncBound_269(Gamma_trans;P_minor):
  Eng_trans_269(lambda;s,D,R,eta,w)
    <= Gamma_trans(lambda;D,R,eta,w;s)

  and

  sum_{lambda in Lambda}
    lambda^2 Gamma_trans(lambda;D,R,eta,w;s)=o(1),
```

over the declared minor-arc parameter family `P_minor`.

This module advances only the object definition and admissibility test for
such a bound. It does not prove the transverse estimate and does not prove
`NarrowMinorArc_3^B`.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The extraction is useful as proof steering. It is not an analytic estimate and
cannot be used as a substitute for `TransIncBound_269`.

## 3. Definitions and variables

For the declared class `s`, write:

```text
f_s = nu_s - 1
B_{d,s}(n)=f_s(n+d)conj(f_s(n))
widehat{B_{d,s}}(xi)=E_n B_{d,s}(n)e(-xi n)
Minor(R,eta)={xi != 0}\Major(R,eta)
```

For `lambda>0`:

```text
Spec_{d,s}^minor(lambda)
  = { xi in Minor(R,eta) :
        |widehat{B_{d,s}}(xi)| >= lambda }.
```

The large-spectrum incidence set is:

```text
I_lambda(s)
  = { (d,xi) :
        D<|d|<=2D,
        xi in Spec_{d,s}^minor(lambda) }.
```

For `I subset I_lambda(s)`, define:

```text
Eng_s(I)
  = (1/D) sum_{(d,xi) in I}
      |widehat{B_{d,s}}(xi)|^2.
```

The row and column diagnostics are:

```text
E_{d,s}(lambda)
  = sum_{xi in Spec_{d,s}^minor(lambda)}
      |widehat{B_{d,s}}(xi)|^2,

N_{xi,s}(lambda)
  = # { d : D<|d|<=2D,
             xi in Spec_{d,s}^minor(lambda) }.
```

Choose thresholds:

```text
mu(lambda)>0,
K(lambda)>=1.
```

Then:

```text
BadShift_s(lambda)
  = { d : E_{d,s}(lambda)>mu(lambda) },

BadFreq_s(lambda)
  = { xi in Minor(R,eta) :
        N_{xi,s}(lambda)>K(lambda) }.
```

The ordered decomposition is:

```text
I_shift_s(lambda)
  = { (d,xi) in I_lambda(s) :
        d in BadShift_s(lambda) },

I_freq_s(lambda)
  = { (d,xi) in I_lambda(s) :
        d notin BadShift_s(lambda),
        xi in BadFreq_s(lambda) },

I_trans_s(lambda)
  = I_lambda(s)
      \ (I_shift_s(lambda) union I_freq_s(lambda)).
```

Equivalently, `(d,xi) in I_trans_s(lambda)` exactly when:

```text
D<|d|<=2D,
xi in Minor(R,eta),
|widehat{B_{d,s}}(xi)| >= lambda,
E_{d,s}(lambda) <= mu(lambda),
N_{xi,s}(lambda) <= K(lambda).
```

Thus `I_trans_s(lambda)` is a weighted bipartite graph:

```text
left vertices:  shifts d with D<|d|<=2D,
right vertices: minor frequencies xi,
edge:           |widehat{B_{d,s}}(xi)| >= lambda,
edge weight:    a_{d,xi}=|widehat{B_{d,s}}(xi)|^2.
```

On the transverse graph:

```text
row-energy ceiling:
  sum_{xi:(d,xi) in I_trans_s(lambda)} a_{d,xi}
    <= mu(lambda),

column-multiplicity ceiling:
  # { d : (d,xi) in I_trans_s(lambda) }
    <= K(lambda).
```

The target term is:

```text
Eng_trans_269(lambda;s,D,R,eta,w)
  = (1/D) sum_{(d,xi) in I_trans_s(lambda)}
      a_{d,xi}.
```

## 4. Assumptions

This module assumes only the definitions and bookkeeping of Modules 197, 203,
204, 257, and 268.

It does not assume:

```text
NarrowMinorArc_3^B,
TransIncBound_269,
MinorArcTransfer_3^B,
ShiftMoment_q smallness,
MultMoment_r smallness,
ProjectedMajorTarget_3^B,
WProjectedLocalMatch_3^major,
ProjectedModelNeutrality_3^major,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
selector transfer,
the original positive existence result,
the all-alpha theorem,
or the unconditional finite-type theorem.
```

Every use of `s` must remain in the same selector/model class until a named
transfer theorem is supplied.

## 5. Proof / disproof / reduction

### A. What the extraction proves

The extraction proves only the identity of the remaining transverse object:

```text
NarrowMinorArc_3^B
  needs
    sum_{lambda in Lambda}
      lambda^2 Eng_trans_269(lambda;s,D,R,eta,w)=o(1)
```

after the low-level, bad-shift, and persistent-frequency rows are handled.

The object is not a theorem. It is a location where a theorem would have to be
inserted.

### B. Trivial ceilings

Let:

```text
C_D = D^(-1) # { d : D<|d|<=2D }.
```

The row-energy ceiling gives:

```text
Eng_trans_269(lambda;s,D,R,eta,w)
  <= C_D mu(lambda).
```

The column-multiplicity ceiling and a Fourier envelope
`|widehat{B_{d,s}}(xi)|<=A_N` give:

```text
Eng_trans_269(lambda;s,D,R,eta,w)
  <= (A_N^2/D) K(lambda) #Minor(R,eta).
```

The threshold condition gives only counting diagnostics such as:

```text
# I_trans_s(lambda)
  <= lambda^(-2) D Eng_trans_269(lambda;s,D,R,eta,w).
```

These ceilings are not enough by themselves. They become useful only if the
chosen `mu(lambda)`, `K(lambda)`, arc count, and envelope losses make the
lambda-sum small while the bad-shift and persistent-frequency removals remain
controlled.

### C. Non-tautological admissibility test

A proposed `Gamma_trans` is admissible only if it is proved by an input
strictly below the endpoint, such as a genuine incidence, restriction, inverse,
additive-energy, or residual-correlation theorem for the exact coefficients
`widehat{B_{d,s}}(xi)`.

It is not admissible if:

```text
Gamma_trans = Eng_trans_269,
Gamma_trans = Eng_s(I_lambda(s)),
Gamma_trans is obtained from M_minor=o(1),
Gamma_trans assumes NarrowMinorArc_3^B,
Gamma_trans assumes ResCube_3^sharp,
Gamma_trans assumes CPC_3^sharp or AU^3,
or Gamma_trans changes the selector/model class.
```

### D. Why ordinary inputs are insufficient

Ordinary pair-BDH type information controls pair variances or averaged
two-point errors. The transverse graph is a simultaneous shift-frequency
large-spectrum object for residual derivative products. It asks for a
weighted incidence estimate after both heavy rows and persistent columns have
been removed.

First-moment Hardy-Littlewood information controls mean local densities. It
does not control fourth moments, large Fourier spectra, row/column
multiplicity, or the residual signs and correlations in `B_{d,s}`.

Therefore ordinary pair-BDH and first-moment HL cannot be cited as
`TransIncBound_269` without an additional theorem that converts them into the
exact transverse incidence estimate above.

## 6. Edge cases

- The zero frequency `xi=0` is excluded before defining
  `Spec_{d,s}^minor(lambda)`.
- The decomposition is ordered: bad shifts are removed before persistent
  frequencies. Reversing this changes `I_freq_s(lambda)` and
  `I_trans_s(lambda)`.
- The inequalities are strict for bad sets and non-strict on the transverse
  complement.
- The normalization is `1/D`, while the shift range contains both positive
  and negative `d`; the harmless constant `C_D` must still be tracked.
- Dyadic threshold losses in `Lambda` cannot be hidden inside an `o(1)` term.
- Large `A_N`, growing `w`, and W-tricked prime weights can erase the
  column-multiplicity gain.
- Major/minor arc boundaries may move with `R` and `eta`; boundary leakage is
  not part of this extraction.
- Cyclic, interval, W-model, smoothed, frozen, and sharp selector estimates
  are different objects until transfer rows connect them.
- Prime powers, W-residue restrictions, and truncation tails remain side
  rows outside the transverse incidence definition.

## 7. Where it fits in the project map

```text
Module 197
  -> energy-tail decomposition

Module 203
  -> NarrowMinorArc_3^B and I_shift/I_freq/I_trans split

Module 204
  -> minor-arc transfer compatibility warnings

Module 257
  -> boundary/minor-arc reentry comparison

Module 268
  -> Phase I selected as transverse-incidence feasibility

Module 269
  -> TransIncCore_269 extracted as the exact remaining object
```

The next useful step is:

```text
Module 270:
  audit whether the bad-shift and persistent-frequency removals can be made
  compatible with any plausible row/column ceiling before asking for a new
  transverse theorem.
```

## 8. What remains open

This module does not prove:

- `TransIncBound_269`;
- `sum_lambda lambda^2 Eng_trans_269(lambda)=o(1)`;
- `NarrowMinorArc_3^B`;
- `MinorArcTransfer_3^B`;
- low-level leakage control;
- `ShiftMoment_q` or `MultMoment_r` estimates;
- any selector transfer from model/frozen/smoothed rows to the actual sharp
  moving selector;
- `ProjectedModelNeutralityGate_260`, `CollNeutral_260`,
  `WProjectedLocalMatch_3^major`, or `ProjectedMajorTarget_3^B`;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original selected-average problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not treat `TransIncCore_269` as a bound.
- Do not set `Gamma_trans` equal to the transverse energy being bounded.
- Do not use endpoint-strength assumptions in a module meant to prove the
  minor-arc endpoint.
- Do not use ordinary pair-BDH or first-moment HL as a transverse incidence
  theorem without an exact conversion theorem.
- Do not move between selector/model classes without a named transfer theorem.
- Do not replace a structural decomposition by an analytic proof.
