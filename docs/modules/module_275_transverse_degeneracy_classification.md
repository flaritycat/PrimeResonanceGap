# Module 275: Degeneracy routing inside the transverse phase equations

## 1. Precise theorem / claim being advanced

This module classifies the low-dimensional degeneracies that can occur in the
transverse phase-kernel objects from Modules 271-274.

Define:

```text
TransDegeneracyAudit_275(P_minor).
```

The audit asks whether degenerate transverse configurations reduce to already
named rows:

```text
bad-shift rows,
persistent-frequency rows,
major-arc leakage rows,
arc-boundary rows,
prime-power/W-residue rows,
cutoff/boundary rows,
selector-transfer rows.
```

Verdict:

```text
Degeneracy routing is structural only.
```

Some degeneracies have natural destinations in existing open packages, but no
listed destination row is automatically proved. After these classes are
removed, the genuinely transverse remainder still requires a same-family
phase-kernel theorem.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module classifies and routes cases. It does not prove
`PhaseKernelBound_273`, `TransGateSideRows_274`, `TransIncBound_269`, or
`NarrowMinorArc_3^B`.

## 3. Definitions and variables

Use the notation of Modules 269-274:

```text
f_s=nu_s-1
F_{d,s}(n)=f_s(n+d)conj(f_s(n))
beta_s(d,xi)=E_n F_{d,s}(n)e(-xi n)
```

The transverse graph is:

```text
I_trans_s(lambda)
  = { (d,xi) :
        D<|d|<=2D,
        xi in Minor(R,eta),
        |beta_s(d,xi)|>=lambda,
        E_{d,s}(lambda)<=mu(lambda),
        N_{xi,s}(lambda)<=K(lambda) }.
```

For dyadic `sigma>=lambda`:

```text
J_trans_s(lambda;sigma)
  = { (d,xi) in I_trans_s(lambda) :
        sigma <= |beta_s(d,xi)| < 2sigma }.
```

The oriented rectangle product is:

```text
R_s(d1,d2;xi1,xi2)
  =
  beta_s(d1,xi1)
  conj(beta_s(d2,xi1))
  conj(beta_s(d1,xi2))
  beta_s(d2,xi2).
```

The graph-restriction functional from Module 273 is:

```text
Xi_273(lambda;sigma;s)
  =
  sup_{|omega_{d,xi}|<=1}
    | sum_{(d,xi) in J_trans_s(lambda;sigma)}
        omega_{d,xi} beta_s(d,xi) |.
```

## 4. Assumptions

This module assumes only the definitions above and the existing status ledger.

It does not assume:

```text
DegFreePhaseGate_275,
PhaseKernelBound_273,
TransGateSideRows_274,
TransverseIncidenceGate_273,
TransIncBound_269,
ThresholdOnlyClosure_270,
PhaseIncidenceGate_271,
AvailableToolClosure_272,
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

### A. Shift-diagonal degeneracy

The shift-diagonal rectangle has:

```text
d1=d2.
```

Then:

```text
R_s(d,d;xi1,xi2)
  =
  |beta_s(d,xi1)|^2 |beta_s(d,xi2)|^2.
```

This is not genuinely transverse between two shifts. It is a row-diagonal
object and should be routed to:

```text
BadShift_s(lambda),
ShiftMoment_{q,s},
row-energy ceiling E_{d,s}(lambda)<=mu(lambda).
```

Routing verdict:

```text
ShiftDiag_275 -> bad-shift / shift-moment row.
```

It is harmless only if the corresponding row estimate is proved. The row
ceiling inside `I_trans_s(lambda)` is a diagnostic, not a full endpoint
estimate.

### B. Frequency-diagonal degeneracy

The frequency-diagonal rectangle has:

```text
xi1=xi2.
```

Then:

```text
R_s(d1,d2;xi,xi)
  =
  |beta_s(d1,xi)|^2 |beta_s(d2,xi)|^2.
```

This is not genuinely transverse between two frequencies. It is a column
object and should be routed to:

```text
BadFreq_s(lambda),
MultMoment_{r,s},
column-multiplicity ceiling N_{xi,s}(lambda)<=K(lambda).
```

Routing verdict:

```text
FreqDiag_275 -> persistent-frequency / multiplicity row.
```

It is harmless only if the corresponding multiplicity estimate is proved.

### C. Repeated-edge degeneracy

The repeated-edge case has:

```text
(d1,xi1)=(d2,xi2).
```

It lies in both the shift-diagonal and frequency-diagonal classes and is
controlled only to the extent that the row and column packages are controlled.
It must not be counted as new transverse cancellation.

Routing verdict:

```text
RepeatEdge_275 -> ShiftDiag_275 + FreqDiag_275.
```

### D. Major-difference and arc-boundary degeneracy

Even when each frequency lies in `Minor(R,eta)`, phase products can contain
frequency combinations such as:

```text
xi1-xi2,
xi1+xi2,
or more general signed sums from K_{Xi,epsilon}.
```

If one of these combinations lies in a major region or in a buffered boundary
set:

```text
Major(R',eta') or ArcBd(R',eta',eta''),
```

then the corresponding phase kernel is not safely minor-arc transverse. It
must be routed to:

```text
major-arc leakage,
ArcBoundaryCompat_274,
WProjectedLocalMatch_3^major if the object is projected-major,
or a named mixed major/minor transfer row.
```

Routing verdict:

```text
MajorDiff_275 -> major-arc leakage / arc-boundary row.
```

This routing does not prove the leakage row. It only prevents a major-like
frequency relation from being hidden inside the transverse remainder.

### E. Physical diagonal degeneracy

The same-frequency pair expansion contains:

```text
E_{n,m}
  F_{d1,s}(n)conj(F_{d2,s}(m))K_S(n-m).
```

If a full-frequency kernel were present, the diagonal `n=m` would appear. For
restricted minor-arc kernels, this diagonal is not automatic. When a proof
isolates a physical diagonal contribution, it becomes a shifted local
correlation:

```text
F_{d1,s}(n)conj(F_{d2,s}(n))
  =
  f_s(n+d1)conj(f_s(n+d2)) |f_s(n)|^2.
```

This should be routed to a local shifted-correlation row only if such a row is
explicitly declared in the same selector/model family.

Routing verdict:

```text
PhysDiag_275 -> local shifted-correlation row, if supplied;
otherwise remains open.
```

It is not a license to replace restricted kernels by diagonal equations.

### F. Boundary and cutoff degeneracy

If any shifted coordinate leaves the active interval or cutoff support:

```text
n,
n+d,
n+d1,
n+d2,
```

then the configuration belongs to the cyclic-to-interval, cutoff, or
truncation side rows:

```text
CutoffTruncCompat_274,
MinorArcTransfer_3^B,
boundary/cyclic-wrap rows.
```

Routing verdict:

```text
BoundaryDeg_275 -> cutoff/truncation/boundary transfer rows.
```

It is not part of the generic transverse phase theorem unless the proof works
inside a model where these boundary terms have already been removed.

### G. W-residue and prime-power degeneracy

If the forms in:

```text
n,
n+d1,
n+d2,
```

collide modulo primes dividing `W`, hit excluded residue classes, or include
prime-power artifacts, the configuration belongs to:

```text
PrimePowerResidueCompat_274,
W-residue side rows,
small-prime artifact rows.
```

Routing verdict:

```text
WPPDeg_275 -> prime-power / W-residue rows.
```

A first-moment small-prime estimate is not enough unless it controls the
weighted residual phase functional.

### H. Selector degeneracy

If a degeneracy is created or removed by changing:

```text
cyc -> int -> W -> smooth/frozen -> sharp,
```

or by moving from a model selector to the actual sharp moving selector, then
the row belongs to:

```text
SelectorTransferCompat_274,
MinorArcTransfer_3^B.
```

Routing verdict:

```text
SelectorDeg_275 -> selector-transfer row.
```

No model-side degeneracy classification automatically transfers to the sharp
moving selector.

### I. Generic transverse remainder

After removing the routed classes:

```text
ShiftDiag_275,
FreqDiag_275,
RepeatEdge_275,
MajorDiff_275,
PhysDiag_275,
BoundaryDeg_275,
WPPDeg_275,
SelectorDeg_275,
```

the remaining contribution is the genuine transverse phase problem.

Define the future remainder gate:

```text
DegFreePhaseGate_275(P_minor):
  a same-family bound for Xi_273 restricted to the complement of the routed
  degeneracy classes, strong enough for the lambda-summed
  Gamma_trans^273 target.
```

This gate is open.

### J. Conditional decomposition

The classification gives only a conditional route:

```text
routed degeneracy rows
  + DegFreePhaseGate_275
  + TransGateSideRows_274
    => PhaseKernelBound_273
```

where the routed degeneracy rows are:

```text
ShiftDiag_275 small,
FreqDiag_275 small,
MajorDiff_275 small,
PhysDiag_275 controlled,
BoundaryDeg_275 small,
WPPDeg_275 small,
SelectorDeg_275 transferred.
```

None of these rows is proved in this module.

## 6. Edge cases

- A row diagonal is not transverse cancellation; it is a shift-moment issue.
- A column diagonal is not transverse cancellation; it is a multiplicity issue.
- A minor frequency can create a major-like difference with another minor
  frequency.
- Full-frequency physical diagonals are diagnostics only; restricted kernels
  do not collapse automatically.
- Boundary and cutoff degeneracies depend on the model and cannot be removed
  after selector transfer as an afterthought.
- W-residue collisions must be tested in the same W-limit order as the gate.
- Degeneracy classes may overlap. The routing must be disjointened before any
  lambda-summed estimate is claimed.
- Removing degenerate cases cannot use the endpoint estimate that the
  transverse gate is meant to help prove.

## 7. Where it fits in the project map

```text
Module 271
  -> phase equations and kernels

Module 273
  -> candidate Gamma_trans^273

Module 274
  -> compatibility side rows

Module 275
  -> degeneracy routing and DegFreePhaseGate_275
```

The next useful step is:

```text
Module 276:
  give a proof-or-blocked verdict for the transverse incidence gate:
  local/model-side, mixed, endpoint-strength, or false / blocked as a
  shortcut.
```

## 8. What remains open

This module does not prove:

- `DegFreePhaseGate_275`;
- smallness of any routed degeneracy row;
- `PhaseKernelBound_273`;
- `TransGateSideRows_274`;
- `TransverseIncidenceGate_273`;
- `TransIncBound_269`;
- `ThresholdOnlyClosure_270`;
- `PhaseIncidenceGate_271`;
- `AvailableToolClosure_272`;
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

- Do not treat degeneracy classification as degeneracy smallness.
- Do not call a row or column diagonal a transverse estimate.
- Do not replace restricted minor-arc kernels by physical diagonals.
- Do not classify major-difference terms as minor without an arc-boundary row.
- Do not transfer model-side degeneracy routing to the sharp selector without
  selector-transfer estimates.
- Do not use endpoint-strength estimates to remove degenerate cases.
