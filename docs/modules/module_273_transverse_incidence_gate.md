# Module 273: Non-tautological transverse incidence gate

## 1. Precise theorem / claim being advanced

This module formulates a candidate transverse incidence gate for the exact
object extracted in Modules 269-272.

Define:

```text
TransverseIncidenceGate_273(P_minor,X_273).
```

The gate proposes a candidate:

```text
Gamma_trans^273(lambda;D,R,eta,w;s)
```

for the open bound:

```text
Eng_trans_269(lambda;s,D,R,eta,w)
  <= Gamma_trans(lambda;D,R,eta,w;s).
```

The gate is non-tautological only if the input `X_273` is proved from exact
phase-kernel estimates for the active selector/model class, not from
`Eng_trans_269`, `M_minor=o(1)`, `NarrowMinorArc_3^B`, or any endpoint
equivalent.

This module does not prove `X_273`; it records the exact kind of estimate
that would be sufficient.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The module defines a conditional gate and candidate majorant. It does not
prove `TransIncBound_269`, `PhaseIncidenceGate_271`,
`AvailableToolClosure_272`, or `NarrowMinorArc_3^B`.

## 3. Definitions and variables

Use the notation of Modules 269-272:

```text
f_s=nu_s-1
F_{d,s}(n)=f_s(n+d)conj(f_s(n))
beta_s(d,xi)=widehat{B_{d,s}}(xi)
            = E_n F_{d,s}(n)e(-xi n)
```

For `lambda in Lambda`:

```text
I_trans_s(lambda)
  = { (d,xi) :
        D<|d|<=2D,
        xi in Minor(R,eta),
        |beta_s(d,xi)|>=lambda,
        E_{d,s}(lambda)<=mu(lambda),
        N_{xi,s}(lambda)<=K(lambda) }.
```

Define dyadic base-tail transverse shells. For dyadic `sigma>=lambda`:

```text
J_trans_s(lambda;sigma)
  = { (d,xi) in I_trans_s(lambda) :
        sigma <= |beta_s(d,xi)| < 2sigma }.
```

The base threshold `lambda` and shell height `sigma` are deliberately kept
separate. The sets `I_trans_s(lambda)` need not be nested in `lambda`, because
the thresholds `mu(lambda)` and `K(lambda)` may change.

With the usual terminal convention at the top of the dyadic grid:

```text
I_trans_s(lambda_j)
  subset union_{k>=j} J_trans_s(lambda_j;lambda_k).
```

For a shell `J=J_trans_s(lambda;sigma)`, define the graph-restriction
functional:

```text
Xi_273(lambda;sigma;s)
  =
  sup_{|omega_{d,xi}|<=1}
    | sum_{(d,xi) in J_trans_s(lambda;sigma)}
        omega_{d,xi} beta_s(d,xi) |.
```

The proposed external phase-kernel input is:

```text
PhaseKernelBound_273(X_273):
  Xi_273(lambda;sigma;s)
    <= X_273(lambda;sigma;D,R,eta,w;s)
```

uniformly over the declared parameter family `P_minor`.

## 4. Assumptions

This module assumes only:

- the finite Fourier model or a named transferred interval model;
- the fixed selector/model class `s`;
- the Module 269 transverse incidence definition;
- the Module 270 threshold notation;
- the Module 271 phase-kernel expansions;
- the Module 272 compatibility audit.

It does not assume:

```text
PhaseKernelBound_273,
TransverseIncidenceGate_273,
TransIncBound_269,
ThresholdOnlyClosure_270,
PhaseIncidenceGate_271,
AvailableToolClosure_272,
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

### A. Shell conversion from graph restriction to energy

On `J_trans_s(lambda;sigma)`:

```text
sigma <= |beta_s(d,xi)| < 2sigma.
```

Therefore:

```text
sum_{(d,xi) in J_trans_s(lambda;sigma)} |beta_s(d,xi)|^2
  <= 2sigma
     sum_{(d,xi) in J_trans_s(lambda;sigma)} |beta_s(d,xi)|.
```

By choosing phases:

```text
sum_{(d,xi) in J_trans_s(lambda;sigma)} |beta_s(d,xi)|
  =
  sup_{|omega_{d,xi}|<=1}
    | sum_{(d,xi) in J_trans_s(lambda;sigma)}
        omega_{d,xi} beta_s(d,xi) |.
```

Hence:

```text
Eng_s(J_trans_s(lambda;sigma))
  <= (2sigma/D) Xi_273(lambda;sigma;s).
```

If `PhaseKernelBound_273(X_273)` is proved, then:

```text
Eng_s(J_trans_s(lambda;sigma))
  <= (2sigma/D) X_273(lambda;sigma;D,R,eta,w;s).
```

This is the phase-kernel route. It is useful only if `X_273` is obtained from
the exact shifted `f_s` kernels of Module 271.

### B. Candidate shell majorant

The trivial row and column ceilings from Module 270 also apply to a shell:

```text
Eng_s(J_trans_s(lambda;sigma))
  <= C_D mu(lambda),

Eng_s(J_trans_s(lambda;sigma))
  <= A_N^2 K(lambda) m_minor(R,eta) / D.
```

Define:

```text
Gamma_shell^273(lambda;sigma;D,R,eta,w;s)
  =
  min(
    C_D mu(lambda),
    A_N^2 K(lambda) m_minor(R,eta) / D,
    2sigma X_273(lambda;sigma;D,R,eta,w;s) / D
  ).
```

This shell majorant is conditional on the external input
`PhaseKernelBound_273(X_273)`.

### C. Candidate tail majorant

For dyadic `lambda_j`, define:

```text
Gamma_trans^273(lambda_j;D,R,eta,w;s)
  =
  sum_{k>=j}
    Gamma_shell^273(lambda_j;lambda_k;D,R,eta,w;s).
```

Then:

```text
Eng_trans_269(lambda_j;s,D,R,eta,w)
  <= Gamma_trans^273(lambda_j;D,R,eta,w;s).
```

Thus the sufficient lambda-summed target is:

```text
sum_{lambda_j in Lambda}
  lambda_j^2 Gamma_trans^273(lambda_j;D,R,eta,w;s)
  = o(1).
```

It is enough to prove the double shell sum:

```text
sum_{lambda_j in Lambda}
  lambda_j^2
  sum_{k>=j}
    Gamma_shell^273(lambda_j;lambda_k;D,R,eta,w;s)
  = o(1).
```

This is the proposed candidate for `TransIncBound_269`.

### D. Non-endpoint criteria

`TransverseIncidenceGate_273(P_minor,X_273)` is admissible only if all of the
following are verified:

```text
G1  X_273 is proved for the same selector/model class s.
G2  The proof uses restricted minor-arc or large-spectrum kernels, not a
    replacement by full-frequency diagonal equations.
G3  The proof controls weighted residual coefficients beta_s(d,xi), not only
    unweighted graph counts.
G4  The dyadic shift range D<|d|<=2D is preserved.
G5  W-residue, prime-power, cutoff, truncation, and boundary terms are included
    in the same parameter family.
G6  The lambda-summed base-tail shell majorant is o(1).
G7  No endpoint object is assumed: not NarrowMinorArc_3^B, M_minor=o(1),
    TransIncBound_269, ResCube_3^sharp, CPC_3^sharp, RBDH_pair_short, or AU^3.
G8  No selector transfer is used unless a named transfer theorem supplies it.
```

If any of these fail, the proposed `Gamma_trans^273` is only a notation for an
open route, not an input to the proof ledger.

### E. Why this is not a proof

The displayed inequalities are deterministic. The difficult term is:

```text
X_273(lambda;D,R,eta,w;s).
```

Bounding `X_273` requires the exact phase-kernel theorem that Module 272
showed is not supplied by the listed off-the-shelf tools. In particular, one
must not set:

```text
X_273(lambda;sigma) = (D/sigma) Eng_trans_269(lambda)
```

or estimate `X_273` by assuming the minor-arc endpoint.

## 6. Edge cases

- Shells use the upper bound `|beta|<2sigma`; the top shell must be handled
  with the declared Fourier envelope `A_N`.
- The base threshold `lambda` and shell height `sigma` must not be collapsed
  unless monotonicity of `mu(lambda)`, `K(lambda)`, and the transverse sets is
  proved.
- Tail bounds inherit a dyadic summation loss; the final lambda-sum must pay
  for it.
- The phase choice in `Xi_273` is adversarial. A proof of `X_273` must handle
  arbitrary unit coefficients on the transverse shell.
- A bound only for fixed frequency sets does not handle data-dependent
  large-spectrum shells unless selection uniformity is proved.
- Row and column ceilings remain available but do not by themselves supply a
  phase-kernel gain.
- The same `mu(lambda)` and `K(lambda)` must be used consistently across bad
  shifts, persistent frequencies, and the transverse shell.
- If `X_273` is proved in a smoothed, frozen, projected, or W-model class, it
  stays there until transfer rows are supplied.

## 7. Where it fits in the project map

```text
Module 269
  -> TransIncCore_269

Module 270
  -> ThresholdRemovalAudit_270

Module 271
  -> TransPhaseExpansion_271

Module 272
  -> PhaseToolCompatAudit_272

Module 273
  -> TransverseIncidenceGate_273 with candidate Gamma_trans^273
```

The next useful step is:

```text
Module 274:
  audit W-limit, threshold-buffer, prime-power, major/minor arc-boundary, and
  selector-transfer compatibility for the candidate transverse gate.
```

## 8. What remains open

This module does not prove:

- `PhaseKernelBound_273`;
- `TransverseIncidenceGate_273`;
- `Gamma_trans^273=o(1)` in the lambda-summed sense;
- `AvailableToolClosure_272`;
- `PhaseIncidenceGate_271`;
- `ThresholdOnlyClosure_270`;
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

- Do not set `X_273` equal to the quantity it is meant to bound.
- Do not use the minor-arc endpoint to prove the graph-restriction input.
- Do not replace restricted kernels by full-frequency diagonal kernels.
- Do not use unweighted incidence counts as weighted residual cancellation.
- Do not use a selector/model estimate outside its declared family.
- Do not cite `TransverseIncidenceGate_273` without `PhaseKernelBound_273`
  and the lambda-summed `Gamma_trans^273` estimate.
