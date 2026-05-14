# Module 278: Minimal transverse family for the phase-kernel test

## 1. Precise theorem / claim being advanced

This module defines the smallest declared environment in which Phase J will
test the transverse phase-kernel input from Module 273.

Define:

```text
MinimalTransverseFamily_278(P_minor^0).
```

The claim is structural:

```text
Future Phase J tests of PhaseKernelBound_273 must first be formulated inside
P_minor^0, or explicitly state which transfer row moves them out of it.
```

This module fixes the selector/model class, Fourier group, W-order, dyadic
shift range, major/minor arc convention, lambda grid, row/column thresholds,
Fourier envelope, shell convention, W-residue convention, cutoff convention,
and limiting order.

It does not prove `PhaseKernelBound_273`, `TransIncBound_269`,
`NarrowMinorArc_3^B`, or any endpoint estimate.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The module defines a local/model-side parameter family. It is a convention
package and a guardrail, not an analytic estimate.

## 3. Definitions and variables

### A. Fixed constants and W-data

Fix once and for all small positive constants:

```text
c0=(delta_D,delta_R,delta_eta,kappa_lambda),
0<delta_D,delta_R,delta_eta,kappa_lambda<1/100.
```

The exact numerical values are not optimized in this module. They are part of
the declared minimal family and may not change inside a proof of the same
row.

For `w>=2`, write:

```text
W=W(w)=prod_{p<=w} p.
```

Choose one reduced W-residue:

```text
b=b(w), 1<=b<=W, (b,W)=1.
```

No averaging over W-residues is included in `P_minor^0`. If a future proof
needs residue averaging or a different residue convention, that is a transfer
step.

### B. Model selector / weight class

The selector/model class is:

```text
s0 = W-cyclic prime-only model in the residue b mod W.
```

Work on representatives `0<=n<N` and define the periodized W-prime weight:

```text
nu_0(n)
  = (phi(W)/W) log(Wn+b) 1_{Wn+b is prime},

f_0(n)=nu_0(n)-1,
```

viewed as functions on the cyclic group below. Prime powers are not included
in `nu_0`. This is not the actual sharp moving selector
`1_{||alpha p||<1/log p}`.

### C. Fourier group and normalization

For fixed `w`, let `N -> infinity` through integers satisfying:

```text
(N,W)=1.
```

Set:

```text
G_N=Z/NZ,
widehat{G_N}=Z/NZ,
e_N(t)=exp(2 pi i t/N).
```

For `F:G_N -> C`, use the normalized Fourier transform:

```text
widehat{F}(xi)=E_{n in G_N} F(n)e_N(-xi n).
```

The residual derivative coefficient is:

```text
B_d^0(n)=f_0(n+d)conj(f_0(n)),
beta_0(d,xi)=widehat{B_d^0}(xi).
```

All shifts are cyclic shifts in `G_N`.

### D. Dyadic shift range

The dyadic shift shell is:

```text
D<|d|<=2D,
d in Z,
d != 0,
N^{delta_D} <= D <= N^{1-delta_D},
2D <= N/16.
```

Both positive and negative `d` are included. The normalization remains `1/D`,
so constants from counting the two-sided shell must still be tracked.

### E. Major/minor arc convention

For integers `R` and real `eta`, require:

```text
2 <= R <= N^{delta_R},
N^{-1+delta_eta} <= eta <= (100 R^2)^(-1).
```

For `xi in widehat{G_N}`, identify `xi/N` with a point of `R/Z` and define:

```text
Major_0(R,eta)
  =
  { xi in widehat{G_N} :
      xi != 0 and
      exists 1<=q<=R, exists (a,q)=1,
      || xi/N - a/q ||_{R/Z} <= eta/q },

Minor_0(R,eta)
  =
  { xi in widehat{G_N} : xi != 0 } \ Major_0(R,eta).
```

The zero frequency is removed before the major/minor split. Boundary
frequencies are assigned by the displayed non-strict inequality; any alternate
buffered convention is a separate arc-boundary row.

Write:

```text
m_minor^0(R,eta)=#Minor_0(R,eta).
```

### F. Fourier envelope and lambda grid

For the declared tuple `(N,w,b,D,R,eta)`, define the actual deterministic
envelope:

```text
A_N^0
  =
  sup_{D<|d|<=2D, xi in widehat{G_N}}
    |beta_0(d,xi)|.
```

No smallness of `A_N^0` is asserted.

If `A_N^0=0`, set `Lambda_0=emptyset`. Otherwise let:

```text
lambda_min=A_N^0 N^{-kappa_lambda},

Lambda_0
  =
  { lambda_j=2^{-j}A_N^0 :
      j=0,1,...,J,
      lambda_j >= lambda_min,
      lambda_{J+1}<lambda_min }.
```

Levels below `lambda_min` are not part of the Phase J shell test; their
contribution belongs to the low-level leakage row of `NarrowMinorArc_3^B`.

### G. Threshold schedules

A tuple in `P_minor^0` includes deterministic threshold schedules:

```text
mu_0:Lambda_0 -> (0,infinity),
K_0:Lambda_0 -> {1,2,...,# {d:D<|d|<=2D}}.
```

The schedules may depend on `(N,w,b,D,R,eta,A_N^0,c0)` and on the grid value
`lambda`, but they are fixed before forming the sets
`Spec_d^minor(lambda)`, `BadShift(lambda)`, `BadFreq(lambda)`, and
`I_trans(lambda)`. They may not be reselected after seeing a particular
large-spectrum graph.

For `lambda in Lambda_0`, define:

```text
Spec_{d,0}^minor(lambda)
  =
  { xi in Minor_0(R,eta) :
      |beta_0(d,xi)| >= lambda },

E_{d,0}(lambda)
  =
  sum_{xi in Spec_{d,0}^minor(lambda)}
    |beta_0(d,xi)|^2,

N_{xi,0}(lambda)
  =
  # { d : D<|d|<=2D,
          xi in Spec_{d,0}^minor(lambda) }.
```

The ordered bad sets are:

```text
BadShift_0(lambda)
  =
  { d : E_{d,0}(lambda)>mu_0(lambda) },

BadFreq_0(lambda)
  =
  { xi in Minor_0(R,eta) :
      N_{xi,0}(lambda)>K_0(lambda) }.
```

Then:

```text
I_trans_0(lambda)
  =
  { (d,xi) :
      D<|d|<=2D,
      xi in Minor_0(R,eta),
      |beta_0(d,xi)| >= lambda,
      E_{d,0}(lambda) <= mu_0(lambda),
      N_{xi,0}(lambda) <= K_0(lambda),
      d notin BadShift_0(lambda),
      xi notin BadFreq_0(lambda) }.
```

The last two conditions are redundant after the non-strict inequalities, but
they record the ordered-removal convention of Module 269.

### H. Shell convention

For `lambda_j in Lambda_0` and `sigma=lambda_k in Lambda_0` with `k<=j`
under the decreasing grid, equivalently `sigma>=lambda_j`, define:

```text
J_trans_0(lambda_j;sigma)
  =
  { (d,xi) in I_trans_0(lambda_j) :
      sigma <= |beta_0(d,xi)| < 2sigma }.
```

The base threshold `lambda_j` and the shell height `sigma` remain separate.
No nesting of the sets `I_trans_0(lambda_j)` is assumed.

The graph-restriction functional inside the minimal family is:

```text
Xi_273^0(lambda_j;sigma)
  =
  sup_{|omega_{d,xi}|<=1}
    | sum_{(d,xi) in J_trans_0(lambda_j;sigma)}
        omega_{d,xi} beta_0(d,xi) |.
```

The corresponding open input is:

```text
PhaseKernelBound_273^0(X_273^0):
  Xi_273^0(lambda_j;sigma)
    <= X_273^0(lambda_j;sigma;N,w,b,D,R,eta,mu_0,K_0).
```

This row remains open.

### I. Cutoff and limiting convention

The cutoff convention in `P_minor^0` is:

```text
full cyclic average over G_N,
no interval cutoff,
no moving alpha-window,
no smoothed selector,
no frozen selector,
no Bernoulli lift,
no projection change after Minor_0(R,eta) is fixed.
```

For any future error term `Err(N,w;rho_0)` over
`rho_0 in P_minor^0(N,w)`, the project meaning of:

```text
Err=o_W(1) over P_minor^0
```

is:

```text
lim_{w->infinity} limsup_{N->infinity}
  sup_{rho_0 in P_minor^0(N,w)}
    |Err(N,w;rho_0)| = 0.
```

The order is fixed: first `N -> infinity` at fixed `w`, then
`w -> infinity`.

## 4. Assumptions

This module assumes only the definitions and status ledger through
Module 277.

It does not assume:

```text
PhaseKernelBound_273^0,
PhaseKernelBound_273,
TransverseGateProofPkg_276,
TransGateSideRows_274,
DegFreePhaseGate_275,
TransIncBound_269,
ThresholdOnlyClosure_270,
PhaseIncidenceGate_271,
AvailableToolClosure_272,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
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

### A. What is gained

The gain is not smallness. The gain is that the next analytic question now
has a fixed ambient family:

```text
P_minor^0
  =
  W-cyclic prime-only model
  + fixed W-residue b
  + normalized cyclic Fourier group
  + two-sided interior dyadic D-shell
  + declared Major_0/Minor_0 arcs
  + declared lambda grid
  + declared threshold schedules
  + declared base-tail shell convention
  + two-stage W-limit.
```

Therefore Module 279 can expand `Xi_273^0` without moving between cyclic,
interval, W-residue, smoothed, frozen, or sharp selector worlds.

### B. What is deliberately excluded

`P_minor^0` is not the actual target family. It excludes:

```text
actual sharp moving alpha selector,
interval boundary and prefix effects,
smoothed/frozen selector transfer,
Bernoulli or finite-stage extraction,
W-residue averaging,
prime-power restoration,
major/minor arc boundary transfer,
dyadic endpoint ranges outside N^{delta_D}<=D<=N^{1-delta_D},
levels below lambda_min.
```

These exclusions are not proofs that the excluded errors are small. They are
the point of the minimal family: first test whether the core phase-kernel
problem is already blocked before spending more ledger on transfer rows.

### C. The local Phase J target

Inside `P_minor^0`, the next non-tautological input is:

```text
PhaseKernelBound_273^0(X_273^0).
```

It is admissible only if `X_273^0` is proved from estimates for the exact
restricted shell functional `Xi_273^0`, with arbitrary unit coefficients
`omega_{d,xi}`, in the same family.

It is not admissible if it is obtained by assuming:

```text
Eng_trans_269 small,
M_minor=o(1),
NarrowMinorArc_3^B,
TransIncBound_269,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
or selector transfer to the actual sharp moving selector.
```

### D. Classification

The definition of `P_minor^0` has status:

```text
STRUCTURAL / EXTRACTION.
```

The row:

```text
PhaseKernelBound_273^0(X_273^0)
```

has status:

```text
OPEN.
```

If a future proof stays wholly inside `P_minor^0`, it is a local/model-side
statement. If it exits to interval, smoothed, frozen, W-residue-averaged, or
sharp selector objects, it becomes mixed until the relevant transfer row is
proved. If it uses endpoint objects, it is endpoint-strength and cannot serve
as a proof input.

## 6. Edge cases

- If `A_N^0=0`, the lambda grid is empty and the Phase J shell target is
  vacuous for that tuple; this does not prove any uniform endpoint estimate.
- The top shell is controlled only by the declared envelope `A_N^0`.
- The lower cutoff `lambda_min` leaves a low-level contribution outside this
  module.
- The family includes both signs of `d`; dropping one sign is a new family.
- Cyclic wraparound is part of the model. It is not an interval estimate.
- The W-residue `b` is fixed. Averaging over `b` or changing residue
  conventions is a transfer step.
- Boundary frequencies in `Major_0(R,eta)` use the displayed non-strict
  inequality. Buffered major/minor partitions are different objects.
- Threshold schedules must be chosen before the large-spectrum graph is
  formed.
- Data-dependent shells remain data-dependent even in `P_minor^0`; a theorem
  for fixed frequency sets does not automatically apply.

## 7. Where it fits in the project map

```text
Module 273
  -> TransverseIncidenceGate_273 and Xi_273

Module 276
  -> TransverseGateProofPkg_276 remains open

Module 277
  -> Phase J selected:
     minimal transverse proof-package feasibility

Module 278
  -> MinimalTransverseFamily_278(P_minor^0)
```

The next useful step is:

```text
Module 279:
  derive the exact dual/phase expansion of Xi_273^0 inside P_minor^0 and
  mark every data-dependent set.
```

## 8. What remains open

This module does not prove:

- `PhaseKernelBound_273^0`;
- `PhaseKernelBound_273`;
- `TransverseGateProofPkg_276`;
- `TransGateSideRows_274`;
- `DegFreePhaseGate_275`;
- `TransIncBound_269`;
- `ThresholdOnlyClosure_270`;
- `PhaseIncidenceGate_271`;
- `AvailableToolClosure_272`;
- `MinorArcTransfer_3^B`;
- `NarrowMinorArc_3^B`;
- selector transfer to the actual sharp moving selector;
- `ProjectedModelNeutrality_3^major`;
- `WProjectedLocalMatch_3^major`;
- `ProjectedMajorTarget_3^B`;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original selected-average problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not treat the definition of `P_minor^0` as a phase-kernel estimate.
- Do not cite `P_minor^0` as a sharp moving-selector family.
- Do not move from cyclic to interval averages without a boundary row.
- Do not move from fixed W-residue to residue-averaged statements for free.
- Do not collapse the base threshold `lambda` and shell height `sigma`.
- Do not replace data-dependent shells by fixed frequency sets without a
  selection theorem.
- Do not use endpoint-strength assumptions to prove `PhaseKernelBound_273^0`.
