# Module 274: Compatibility audit for the candidate transverse gate

## 1. Precise theorem / claim being advanced

This module audits whether the candidate transverse gate from Module 273 can
be used in the active minor-arc environment.

Define:

```text
TransGateCompatAudit_274(P_minor).
```

The audit introduces the side package:

```text
TransGateSideRows_274(P_minor)
  =
  WLimitCompat_274
  + ThresholdBufferCompat_274
  + ArcBoundaryCompat_274
  + PrimePowerResidueCompat_274
  + CutoffTruncCompat_274
  + SelectorTransferCompat_274
  + DyadicUniformityCompat_274.
```

Verdict:

```text
TransGateSideRows_274(P_minor) is not proved by the current ledger.
```

Thus `TransverseIncidenceGate_273` remains a candidate structural gate, not a
usable proof input for `NarrowMinorArc_3^B`.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module defines compatibility requirements. It does not prove
`PhaseKernelBound_273`, `TransverseIncidenceGate_273`, `TransIncBound_269`,
`MinorArcTransfer_3^B`, or `NarrowMinorArc_3^B`.

## 3. Definitions and variables

Use the Module 273 base-tail shell notation:

```text
I_trans_s(lambda)
  = { (d,xi) :
        D<|d|<=2D,
        xi in Minor(R,eta),
        |beta_s(d,xi)|>=lambda,
        E_{d,s}(lambda)<=mu(lambda),
        N_{xi,s}(lambda)<=K(lambda) },

J_trans_s(lambda;sigma)
  = { (d,xi) in I_trans_s(lambda) :
        sigma <= |beta_s(d,xi)| < 2sigma },

Xi_273(lambda;sigma;s)
  =
  sup_{|omega_{d,xi}|<=1}
    | sum_{(d,xi) in J_trans_s(lambda;sigma)}
        omega_{d,xi} beta_s(d,xi) |.
```

The candidate shell majorant is:

```text
Gamma_shell^273(lambda;sigma;D,R,eta,w;s)
  =
  min(
    C_D mu(lambda),
    A_N^2 K(lambda) m_minor(R,eta) / D,
    2sigma X_273(lambda;sigma;D,R,eta,w;s) / D
  ).
```

The candidate tail majorant is:

```text
Gamma_trans^273(lambda_j;D,R,eta,w;s)
  =
  sum_{k>=j}
    Gamma_shell^273(lambda_j;lambda_k;D,R,eta,w;s).
```

The desired lambda-summed target is:

```text
S_273(P_minor;s)
  =
  sum_{lambda_j in Lambda}
    lambda_j^2 Gamma_trans^273(lambda_j;D,R,eta,w;s)
  = o(1).
```

## 4. Assumptions

This module assumes only the definitions of Modules 269-273 and the transfer
warnings of Modules 204 and 257.

It does not assume:

```text
TransGateSideRows_274,
WLimitCompat_274,
ThresholdBufferCompat_274,
ArcBoundaryCompat_274,
PrimePowerResidueCompat_274,
CutoffTruncCompat_274,
SelectorTransferCompat_274,
DyadicUniformityCompat_274,
PhaseKernelBound_273,
TransverseIncidenceGate_273,
TransIncBound_269,
MinorArcTransfer_3^B,
NarrowMinorArc_3^B,
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

### A. W-limit compatibility

`WLimitCompat_274` requires the same two-stage limit order throughout:

```text
lim_{w->infty} limsup_{N->infty}
  sup_{(D,R,eta,Lambda,mu,K) in P_minor(w,N)}
    S_273(P_minor;s)
  = 0.
```

The estimate for `X_273` must also be uniform in the same range:

```text
Xi_273(lambda;sigma;s)
  <= X_273(lambda;sigma;D,R,eta,w;s)
```

with constants that do not destroy the final `w -> infinity` limit.

Failure mode:

```text
An estimate proved only for fixed w, fixed D, or fixed thresholds is not an
endpoint-ready transverse input.
```

### B. Threshold-buffer compatibility

The shell sets depend on inequalities:

```text
|beta_s(d,xi)| >= lambda,
sigma <= |beta_s(d,xi)| < 2sigma,
E_{d,s}(lambda)<=mu(lambda),
N_{xi,s}(lambda)<=K(lambda).
```

Small model-transfer errors can move edges across these boundaries. Define a
buffered bad shell boundary, schematically:

```text
ShellBd_274(lambda;sigma;tau)
  =
  { (d,xi) :
      ||beta_s(d,xi)|-lambda| <= tau
      or ||beta_s(d,xi)|-sigma| <= tau
      or ||beta_s(d,xi)|-2sigma| <= tau
      or |E_{d,s}(lambda)-mu(lambda)| <= tau
      or |N_{xi,s}(lambda)-K(lambda)| <= 1 }.
```

`ThresholdBufferCompat_274` requires either:

```text
1. direct transfer of Eng_s(J_trans_s(lambda;sigma));
2. direct transfer of Xi_273(lambda;sigma;s);
3. or a buffered inclusion whose ShellBd_274 contribution is small in the
   lambda-summed target.
```

Without this row, a model-side shell estimate does not transfer to a target
large-spectrum shell.

### C. Arc-boundary compatibility

The phase kernels are built over:

```text
Minor(R,eta)={xi != 0}\Major(R,eta).
```

Changing model, denominator range, or projection convention can move
frequencies across the major/minor boundary. With a buffered boundary:

```text
ArcBd(R,eta,eta')=Major(R,eta')\Major(R,eta),
```

`ArcBoundaryCompat_274` requires a shell-level or graph-restriction-level
bound for the boundary contribution:

```text
Xi_ArcBd_274(lambda;sigma)
  =
  sup_{|omega_{d,xi}|<=1}
    | sum_{(d,xi) in J_trans_s(lambda;sigma), xi in ArcBd}
        omega_{d,xi} beta_s(d,xi) |
```

whose contribution to the double shell sum is `o(1)`.

This row is stronger than merely saying the full fourth moment has a small
arc boundary term, because the gate uses data-dependent shells and adversarial
phases.

### D. Prime-power and W-residue compatibility

Let `beta_s^prime(d,xi)` denote the coefficient after removing prime powers
and small-prime artifacts in the chosen W-model convention.

`PrimePowerResidueCompat_274` requires:

```text
Xi_PP_274(lambda;sigma)
  =
  sup_{|omega_{d,xi}|<=1}
    | sum_{(d,xi) in J_trans_s(lambda;sigma)}
        omega_{d,xi}
        (beta_s(d,xi)-beta_s^prime(d,xi)) |
```

to have lambda-summed contribution `o(1)`, together with fixed W-residue
conventions for:

```text
d,
n,
n+d,
the Fourier group,
and the allowed residue classes.
```

A first-moment prime-power estimate is not enough unless it propagates through
the residual product and the adversarial shell functional.

### E. Cutoff and truncation compatibility

The phase gate is sensitive to:

```text
cyclic wraparound,
interval endpoints,
dyadic cutoffs,
truncation of f_s,
top shell A_N,
prefix and tail windows.
```

`CutoffTruncCompat_274` requires the graph-restriction error:

```text
Xi_Cut_274(lambda;sigma)
```

from replacing one cutoff/truncation convention by another to be small in the
same double shell sum. It also requires the top shell to be controlled by the
declared Fourier envelope `A_N`, not by an unstated pointwise bound.

### F. Selector-transfer compatibility

If `X_273` is proved in a model class:

```text
s in {cyc,int,W,smooth,frozen},
```

then `SelectorTransferCompat_274` is needed before it can be used for the
actual sharp moving selector. The required transfer must apply to:

```text
beta_s(d,xi),
I_trans_s(lambda),
J_trans_s(lambda;sigma),
Xi_273(lambda;sigma;s),
Gamma_shell^273,
Gamma_trans^273,
and the final double lambda-shell sum.
```

It is not enough to approximate `f_s` in a weak average norm. The transfer
must pass through:

```text
B_{d,s}(n)=f_s(n+d)conj(f_s(n))
```

and through the large-spectrum shell selection.

### G. Dyadic uniformity compatibility

`DyadicUniformityCompat_274` requires the gate to be uniform over:

```text
D<|d|<=2D,
D in D_range(N,Hcal),
lambda_j in Lambda,
sigma=lambda_k>=lambda_j,
R, eta,
w,
and the declared selector/model class.
```

The double shell sum:

```text
sum_{lambda_j}
  lambda_j^2 sum_{k>=j}
    Gamma_shell^273(lambda_j;lambda_k;D,R,eta,w;s)
```

must absorb all logarithmic losses from the dyadic grid. A single fixed
`lambda` or fixed `D` estimate is not a transverse endpoint input.

### H. Conditional use statement

The usable conditional implication is:

```text
PhaseKernelBound_273(X_273)
  + TransGateSideRows_274(P_minor)
  + lambda-summed Gamma_trans^273=o(1)
    => TransIncBound_269
```

inside the declared selector/model class.

If the target is the actual sharp moving selector, then one also needs the
appropriate part of:

```text
MinorArcTransfer_3^B.
```

None of these rows is proved here.

## 6. Edge cases

- The base threshold `lambda` and shell height `sigma` are separate; transfer
  must preserve the base-tail shell structure.
- The strict and non-strict inequalities defining bad shifts, persistent
  frequencies, and shells can change under perturbation.
- Integer-valued `N_{xi,s}(lambda)` makes threshold buffering asymmetric.
- Arc-boundary leakage can be small in total fourth moment but large for an
  adversarial graph-restriction functional.
- Prime-power errors must be controlled after multiplication in `B_{d,s}`,
  not only at the level of `nu_s`.
- A W-model estimate with uncontrolled W-growth can fail after the
  `w -> infinity` limit.
- A smoothed or frozen selector estimate is not a sharp moving-selector
  estimate.
- Full-frequency diagonal identities remain diagnostics only; they do not
  provide restricted minor-arc kernel transfer.

## 7. Where it fits in the project map

```text
Module 273
  -> TransverseIncidenceGate_273 and candidate Gamma_trans^273

Module 274
  -> TransGateCompatAudit_274 and TransGateSideRows_274
```

The next useful step is:

```text
Module 275:
  test whether low-dimensional degeneracies in the transverse equations
  reduce to bad-shift, persistent-frequency, major-arc leakage, or boundary
  rows already named.
```

## 8. What remains open

This module does not prove:

- `TransGateSideRows_274`;
- `WLimitCompat_274`;
- `ThresholdBufferCompat_274`;
- `ArcBoundaryCompat_274`;
- `PrimePowerResidueCompat_274`;
- `CutoffTruncCompat_274`;
- `SelectorTransferCompat_274`;
- `DyadicUniformityCompat_274`;
- `PhaseKernelBound_273`;
- `TransverseIncidenceGate_273`;
- `TransIncBound_269`;
- `MinorArcTransfer_3^B`;
- `NarrowMinorArc_3^B`;
- selector transfer to the actual sharp moving selector;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- `ProjectedMajorTarget_3^B`, `WProjectedLocalMatch_3^major`,
  or `ProjectedModelNeutrality_3^major`;
- the original selected-average problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not use a model-side `X_273` estimate for the sharp selector without
  shell-level selector transfer.
- Do not treat threshold-buffer, arc-boundary, prime-power, or cutoff errors
  as automatic.
- Do not collapse base threshold `lambda` and shell height `sigma` without a
  monotonicity or buffering proof.
- Do not replace graph-restriction transfer by a first-moment transfer.
- Do not assume `MinorArcTransfer_3^B` inside a module meant to supply its
  missing transverse input.
- Do not cite `TransverseIncidenceGate_273` as usable unless
  `TransGateSideRows_274` and the lambda-summed `Gamma_trans^273` estimate
  are both supplied.
