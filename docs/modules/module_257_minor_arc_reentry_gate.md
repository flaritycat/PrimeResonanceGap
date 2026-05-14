# Module 257: Minor-arc reentry gate

## 1. Precise theorem / claim being advanced

This module compares the fixed-support boundary obstruction from Modules
242-256 with the residual derivative cube minor-arc packages from Modules 203
and 204.

The boundary branch currently has:

```text
FixedRowFeasGate_255
  => FixedRowOnePointPkg_249
  => OnePointBIHL_242,

TwoPointEscGate_256
  => TwoPointBIHL_256.
```

Both are conditional. Neither proves a local boundary theorem outside exact
model conventions.

The minor-arc branch has:

```text
NarrowMinorArc_3^B(D;R,eta)
  => M_minor(D;R,eta)=o(1),

NarrowMinorArc_3^B_model
  + MinorArcTransfer_3^B
    => M_minor^target(D;R,eta)=o(1).
```

Define:

```text
BoundaryMinorReentry_257(s0,D0,rho0;D,R,eta)
```

to be the routing ledger deciding whether a boundary gate is:

```text
local compared with the minor-arc package,
mixed with minor-arc transfer,
endpoint-strength through the minor-arc endpoint,
or false / blocked as a shortcut.
```

The structural claim is:

```text
NarrowMinorArc_3^B + MinorArcTransfer_3^B
```

does not automatically prove the fixed-support boundary gates. It controls a
spectral minor-arc fourth moment for `B_d`, while the boundary gates are
`|W_M|`-weighted interval/cutoff/residue tuple estimates in the fixed
projected-major cyclic-to-interval row. A proof that routes boundary gates
through the full minor-arc fourth moment is endpoint-strength unless it
isolates a genuinely localized minor-boundary transfer row.

The branch verdict is:

```text
Do not continue blind boundary tuple expansion. Reenter the endpoint map by
comparing the boundary obstruction first with the minor-arc package here, then
with the projected-major package in Module 258, before the Module 259 plan
update chooses the next branch.
```

This module does not prove `NarrowMinorArc_3^B`, `MinorArcTransfer_3^B`, any
boundary gate, or the residual cube endpoint.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The module is a routing and comparison audit. It classifies possible
interactions between boundary gates and minor-arc packages but supplies no
new analytic estimate.

## 3. Definitions and variables

Use the fixed boundary row:

```text
rho0=(D0,R0,eta0,P_M,H0,K0,T0,s0,cutoff0),
s0 in {model, W, sm, fr},
BdPrefRow_224^P(s0,D0;N,w,rho0),
Pi=P_M,
edge=cyc_s0 -> int_s0,
D0<|d|<=2D0,
w fixed, N -> infinity, then w -> infinity.
```

The boundary branch objects are:

```text
OnePointBIHL_242,
FixedRowFeasGate_255,
TwoPointBIHL_256,
TwoPointEscGate_256,
FixedSupportTupleHL_238.
```

The one-point active form is:

```text
m0(n,t)=n-t0.
```

The same-slot two-point diagnostic forms are:

```text
m0(n,t)=n-t0,
m1(n,d,t)=n-t0+d,
Theta_{w,{(00,0),(00,1)}}^proj=kappa_w(d).
```

The minor-arc branch uses:

```text
f_s=nu_s-1,
B_{d,s}(n)=f_s(n+d)conj(f_s(n)),
Pi_minor^s=projection to Minor(R,eta),
```

and:

```text
M_minor^s(D;R,eta)
  = (1/D) sum_{D<|d|<=2D}
      ||Pi_minor^s B_{d,s}||_{U^2}^4

  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)}
        |widehat{B_{d,s}}(xi)|^4.
```

Module 203 defined:

```text
NarrowMinorArc_3^B(D;R,eta)
```

as the package:

```text
low-level L^2 leakage control,
bad-shift moment control,
persistent-frequency multiplicity control,
non-tautological transverse incidence control.
```

Module 204 defined:

```text
MinorArcTransfer_3^B(D;R,eta;w)
```

as the package:

```text
adjacent fourth-moment transfer,
arc-boundary stability,
W-limit and W-growth control,
dyadic D-range uniformity,
cyclic-to-interval boundary transfer,
prime-power and small-prime transfer,
selector transfer,
threshold stability.
```

The analytic side-package audit of Module 229 names their combination:

```text
MinorAnalyticPkg_229
  = NarrowMinorArc_3^B + MinorArcTransfer_3^B
    + threshold, W, range, prime-power, selector, and transfer rows.
```

## 4. Assumptions

This module assumes only the definitions above and the status ledger:

```text
Boundary gates are conditional or open.
NarrowMinorArc_3^B is conditional/open.
MinorArcTransfer_3^B is conditional/open.
ResCube_3^sharp is open.
```

No comparison may change:

```text
selector class s0,
projection P_M or Pi_minor without a named projection-transfer row,
dyadic shell,
W-residue convention,
boundary intervals,
cutoff0,
fixed-w then N -> infinity then w -> infinity limit order.
```

The module does not assume:

```text
FixedRowFeasGate_255,
TwoPointEscGate_256,
FixedSupportTupleHL_238,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
MinorTarget_3^B,
ProjectedMajorTarget_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3.
```

## 5. Proof / disproof / reduction

### A. Object comparison

The boundary gates are physical-space, boundary-supported, kernel-weighted
rows. Typical targets are:

```text
E_K sum_r |E_n 1_{J_r}(n)(mu_s0(m0(n,t))-1)|,

E_K sum_r |E_n 1_{J_r}(n)
  mu_s0(m0(n,t))mu_s0(m1(n,d,t))
  - ell_r kappa_w(d)|.
```

The minor-arc target is:

```text
M_minor^s(D;R,eta)
  = (1/D) sum_d ||Pi_minor^s B_{d,s}||_{U^2}^4.
```

These are not the same object:

```text
boundary rows:
  localized in n near interval endpoints,
  weighted by |W_M(t)|,
  tied to cyclic-to-interval or fixed-support tuple transfer;

minor-arc row:
  spectral nonzero-frequency fourth moment on Minor(R,eta),
  tied to large-spectrum incidence and selector transfer.
```

Therefore:

```text
NarrowMinorArc_3^B + MinorArcTransfer_3^B
  => FixedRowFeasGate_255
```

is not a valid implication without an additional localized
minor-boundary-transfer theorem.

### B. When minor arcs can help a boundary gate

A minor-arc estimate may support a boundary gate only through a named
localized row such as:

```text
MinorBoundaryTrace_257:
  fixed-support boundary/cutoff contribution of Pi_minor B_d
  is o_W(1)
```

or:

```text
MinorSideTransfer_257:
  minor-frequency selector transfer controls the exact boundary-side defect
  appearing in Modules 254-256.
```

Such a row must specify:

```text
the boundary support,
the projection used,
the selector class,
the |W_M| weighting,
the dyadic shell,
the W-limit order,
the prime-power and W-residue side rows.
```

If the proof instead bounds a boundary row by the full:

```text
M_minor(D;R,eta)=o(1)
```

or by an endpoint-equivalent residual fourth moment, then the boundary row is
not local. It is endpoint-strength.

### C. When boundary gates can help minor arcs

Boundary gates can enter `MinorArcTransfer_3^B` only as transfer components,
for example:

```text
cyclic-to-interval boundary transfer,
cutoff transfer,
range transfer,
W-residue transfer,
prime-power boundary transfer.
```

They do not prove:

```text
low-level leakage,
bad-shift moments,
persistent-frequency multiplicity moments,
transverse incidence control.
```

Thus:

```text
FixedRowFeasGate_255 + TwoPointEscGate_256
  => NarrowMinorArc_3^B
```

is false / blocked as a shortcut.

At most, a successful boundary package could contribute to:

```text
MinorArcTransfer_3^B
```

by reducing cyclic/interval or selector-edge boundary errors. The analytic
minor-arc cancellation itself remains a separate package.

### D. Comparison table

| Proposed use | Classification | Reason |
|---|---|---|
| Boundary gates proved by fixed physical support estimates | local if fixed-row | Smaller than endpoint if no full residual fourth moment is used. |
| Boundary gates proved by full `M_minor=o(1)` | endpoint-strength | Uses a spectral endpoint-side estimate to close a local row. |
| Boundary gates proved by `NarrowMinorArc_3^B` plus a named localized trace row | conditional / mixed | Depends on whether the trace row is fixed-row local or changes projection/selector. |
| `NarrowMinorArc_3^B` proved by boundary volume or one-point gates | false / blocked | Minor-arc large-spectrum incidence is not boundary volume. |
| `MinorArcTransfer_3^B` using boundary gates for cyclic-to-interval errors | conditional / mixed | Valid only for transfer rows, not analytic cancellation. |
| Boundary tuple expansion after Module 256 | conditional diagnostic only | Adds complexity before proving local gates. |
| Reentering minor arcs after Module 256 | structurally justified | Tests a distinct endpoint-side obstruction already named in Modules 203-204. |

### E. Branch decision

The boundary branch has clarified:

```text
one-point mean gates,
kernel gates,
short-interval W range gates,
side convention gates,
same-slot pair local factor kappa_w(d).
```

But it has not supplied a proved local theorem. Continuing blindly to more
tuple rows risks building a larger taxonomy around the same missing estimates.

The minor-arc branch remains open, but it is a different obstruction:

```text
large-spectrum density,
shift moments,
frequency multiplicity,
transverse incidence,
minor selector transfer.
```

The project should therefore pause further boundary tuple expansion and
reenter the endpoint map:

```text
Module 257:
  compare boundary with minor arcs;

Module 258:
  compare boundary with projected major arcs;

Module 259:
  plan update and branch decision.
```

This is not an abandonment of the boundary branch. It is a check against
turning localized bookkeeping into a maze.

### F. Conditional routing statement

The valid routing statement is:

```text
BoundaryMinorReentry_257:

1. If a boundary gate is proved by fixed support, exact local model, and
   fixed-row weighted estimates, classify it as local.

2. If a boundary gate is proved through a named minor-boundary trace row,
   classify it according to that trace row: local if fixed-row, mixed if it
   changes projection/selector, endpoint-strength if it uses full residual
   fourth moments.

3. If a boundary gate is proved by assuming `NarrowMinorArc_3^B`,
   `MinorTarget_3^B`, or `ResCube_3^sharp` without localization, classify it
   as endpoint-strength.

4. If a minor-arc package is claimed from boundary volume, one-point gates,
   pair local factors, ordinary pair-BDH, or first-moment HL, classify it as
   false / blocked.
```

This routing statement is structural. It proves no estimate.

## 6. Edge cases

- Major/minor recomposition requires an exact or compatible partition; boundary
  gates do not supply `MajorMinorSelCompat_3(P_adm)`.
- The fixed boundary row uses `P_M`; minor arcs use `Pi_minor`. Moving between
  them requires projection compatibility.
- A minor estimate for cyclic `B_d` does not transfer to interval, W,
  smoothed, frozen, or actual moving selectors without `MinorArcTransfer_3^B`.
- A boundary estimate for one dyadic shell does not give uniform minor-arc
  control over the endpoint dyadic range.
- The two-point local factor `kappa_w(d)` is a pair model; it is not a
  minor-arc large-spectrum estimate.
- Boundary rows use `|W_M|`; signed kernel cancellation in a minor-arc proof
  cannot be imported without a named absolute-weight transfer.
- Threshold stability in `NarrowMinorArc_3^B` does not follow from physical
  boundary support estimates.
- Prime powers and W-residue errors appear on both branches, but the norms are
  different: boundary weighted mass versus projected fourth moment.
- Using `AU^3`, `CPC_3^sharp`, `RBDH_pair_short`, or `ResCube_3^sharp` to
  close minor or boundary subrows is endpoint-strength unless circularity is
  explicitly broken.

## 7. Where it fits in the project map

The Phase G boundary diagnostics now stand at:

```text
Module 251:
  BoundaryLengthGate_251.

Module 252:
  KernelHolderGate_252.

Module 253:
  WShortRangeGate_253.

Module 254:
  SideConventionGate_254.

Module 255:
  FixedRowFeasGate_255.

Module 256:
  TwoPointEscGate_256.

Module 257:
  minor-arc reentry comparison.
```

The minor-arc side remains:

```text
NarrowMinorArc_3^B
  + MinorArcTransfer_3^B
    => MinorTarget_3^B
```

only conditionally.

The next module should perform the analogous comparison with projected major
arcs:

```text
Module 258:
  projected-major reentry gate, comparing the boundary obstruction with
  ProjectedMajorTarget_3^B and WProjectedLocalMatch_3^major.
```

## 8. What remains open

This module does not prove:

- `BoundaryMinorReentry_257` as an analytic estimate;
- `MinorBoundaryTrace_257`;
- `MinorSideTransfer_257`;
- `FixedRowFeasGate_255`;
- `TwoPointEscGate_256`;
- `OnePointBIHL_242`;
- `TwoPointBIHL_256`;
- `FixedSupportTupleHL_238`;
- `NarrowMinorArc_3^B`;
- `MinorArcTransfer_3^B`;
- `MinorTarget_3^B`;
- `MinorAnalyticPkg_229`;
- `MajorMinorSelCompat_3(P_adm)`;
- `ProjectedMajorTarget_3^B`;
- `ResCube_3^sharp`;
- `RBDH_pair_short`;
- `CPC_3^sharp`;
- `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not use `NarrowMinorArc_3^B` as a boundary theorem.
- Do not use boundary volume, one-point gates, or the pair local factor
  `kappa_w(d)` as minor-arc cancellation.
- Do not close boundary gates by full `M_minor=o(1)` and still call them
  local.
- Do not treat `MinorArcTransfer_3^B` as analytic minor-arc cancellation; it
  is a transfer package.
- Do not move between `P_M` and `Pi_minor` without a named compatibility row.
- Do not transfer model, cyclic, W, smoothed, frozen, or boundary estimates to
  the actual moving selector without the required selector-transfer norm.
- Do not cite ordinary pair-BDH, rectangle-BDH, or first-moment HL as
  `NarrowMinorArc_3^B`.
- Do not close this comparison by assuming `ProjectedMajorTarget_3^B`,
  `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`.
- Do not claim the original problem, all-alpha theorem, unconditional
  finite-type theorem, or endpoint class is proved.
