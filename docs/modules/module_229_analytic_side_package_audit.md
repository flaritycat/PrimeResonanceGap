# Module 229: Analytic side-package arrow audit

## 1. Precise theorem / claim being advanced

This module audits the endpoint arrows that Module 228 deliberately excluded
from the structural bucket.

Define:

```text
AnalyticArrowAudit_229.
```

Claim:

```text
AnalyticArrowAudit_229
```

is a side-package ledger for the non-structural arrows:

```text
ResCube_3^sharp <-> CPC_3^sharp,
CPC_3^sharp <-> SPAC_2^sharp,
CPC_3^sharp <-> RBDH_pair_short,
ProjectedMajorTarget_3^B,
MinorTarget_3^B.
```

The audit identifies the exact analytic and transfer inputs needed before any
of these arrows may be used as endpoint-strength statements. It does not prove
any of the inputs and does not upgrade any endpoint object.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The module is an audit of conditional arrows. Each analytic arrow below is
classified as `CONDITIONAL` unless explicitly blocked as an underspecified
shortcut. No arrow is classified as `PROVEN`.

## 3. Definitions and variables

Use:

```text
f=nu-1,
B_d(n)=f(n+d)conj(f(n)),
c_d=E_n B_d(n),
B_d^circ(n)=B_d(n)-c_d.
```

The residual cube quantity is:

```text
ResFour_B(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi != 0} |widehat{B_d}(xi)|^4.
```

The pair product, pair residual, and linear margin are:

```text
P_d(n)=nu(n+d)conj(nu(n)),
R_d(n)=P_d(n)-kappa_w(d),
L_d(n)=f(n+d)+conj(f(n)).
```

Since `nu=1+f`:

```text
P_d(n)=1+L_d(n)+B_d(n),
R_d(n)=B_d(n)+L_d(n)+(1-kappa_w(d)).
```

For nonzero frequencies:

```text
widehat{R_d}(xi)=widehat{B_d}(xi)+widehat{L_d}(xi),
widehat{B_d}(xi)=widehat{R_d}(xi)-widehat{L_d}(xi).
```

Define:

```text
ResFour_R(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi != 0} |widehat{R_d}(xi)|^4,

LinFour_L(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi != 0} |widehat{L_d}(xi)|^4.
```

The exact local models are:

```text
kappa_w(d)
  = prod_{p>w} (1-1/p)^(-2)
      (1 - #{0,-d mod p}/p),

Sigma_w(d,h)
  = prod_{p>w} (1-1/p)^(-4)
      (1 - #{0,-d,-h,-h-d mod p}/p),

Omega_w(d,h,k)
  = sum_{S subset V(d,h,k;0)}
      (-1)^(8-|S|) Theta_{w,S}(d,h,k),
```

where `V(d,h,k;0)` is the unprojected eight-vertex residual cube. In projected
major-arc form this becomes:

```text
Omega_w^proj(d,h,k;t)
  = sum_{S subset V(d,h,k;t)}
      (-1)^(8-|S|) Theta_{w,S}^proj(d,h,k;t).
```

The local residual covariance model for the centered pair residual is:

```text
Cov_w(d,h)=Sigma_w(d,h)-|kappa_w(d)|^2.
```

This is a model difference, not the forbidden pointwise replacement
`Sigma_w(d,h)=kappa_w(d)^2`.

For major and minor arcs write:

```text
ResFour_B(D)=M_major(D)+M_minor(D)
```

only when the nonzero Fourier partition is exact and sharp. In smoothed or
buffered settings, use the Module 218 compatibility rows.

## 4. Assumptions

The audit assumes:

- normalized Fourier conventions in a fixed cyclic model, or an interval
  model already transferred to that convention;
- the same dyadic shell `D<|d|<=2D`;
- zero frequency is excluded from `ResFour_B` and `ResFour_R`;
- the exact W-limit order is fixed `w`, then `N -> infinity`, then
  `w -> infinity`;
- the selector class is declared before any arrow is used;
- prime powers, small-prime residues, boundary terms, projection terms, and
  range restrictions are not hidden inside local-model notation.

No ordinary pair-BDH, ordinary rectangle-BDH, first-moment Hardy-Littlewood,
or generic finite-complexity tuple theorem is assumed to include the side
packages below unless those packages are explicitly part of its statement.

## 5. Analytic side-package audit

### A. `ResCube_3^sharp <-> CPC_3^sharp`

The deterministic nonzero-frequency inequalities are:

```text
ResFour_B(D) <= 8 ResFour_R(D) + 8 LinFour_L(D),
ResFour_R(D) <= 8 ResFour_B(D) + 8 LinFour_L(D).
```

Thus a pair-residual fourth-moment estimate for `R_d` transfers to the
residual derivative cube for `B_d` only with:

```text
LinearU2Margin_229:
  LinFour_L(D)=o(1)
```

in the same dyadic range, W-limit order, selector class, and domain.

The analytic arrow requires the package:

```text
PairResidualTransfer_229
  = LinearU2Margin_229
    + zero-mode compatibility
    + kappa_w(d) centering
    + boundary transfer
    + W-limit compatibility
    + prime-power transfer
    + range coverage
    + selector transfer.
```

Audit verdict:

```text
ResCube_3^sharp <-> CPC_3^sharp
  is CONDITIONAL on PairResidualTransfer_229.
```

Blocked shortcut:

```text
ordinary pair-BDH alone
```

does not supply this arrow. It controls, at best, the pair object `R_d`; it
does not remove the linear margin `L_d`, move selector class, or transfer
cyclic estimates to the endpoint environment.

### B. `CPC_3^sharp <-> SPAC_2^sharp`

For one fixed centered pair residual `R_d` in one fixed cyclic model, Module
228 recorded the structural identity:

```text
E_h |E_n R_d(n+h)conj(R_d(n))|^2
  = sum_xi |widehat{R_d}(xi)|^4.
```

The endpoint arrow between `CPC_3^sharp` and `SPAC_2^sharp` is analytic
because project statements may start from uncentered rectangles or from a
different model. The required package is:

```text
CPCSPACAlign_229
  = exact R_d=P_d-kappa_w(d) centering
    + covariance calibration by Cov_w(d,h)
    + interval/cyclic boundary transfer
    + cutoff and smoothing compatibility
    + range coverage in d and h
    + W-limit compatibility
    + prime-power transfer
    + selector transfer.
```

The covariance calibration row is:

```text
CovCal_229(D)
  = (1/D) sum_{D<|d|<=2D}
      E_h |Cov_w(d,h)|^2
  = o_W(1),
```

or the corresponding cutoff-weighted version required by the chosen
`SPAC_2^sharp` statement.

Audit verdict:

```text
CPC_3^sharp <-> SPAC_2^sharp
  is structural only after CPCSPACAlign_229 has put both sides
  on the same centered pair residual R_d.
```

Until then, the endpoint arrow is `CONDITIONAL`.

Blocked shortcut:

```text
forbidden pointwise replacement:
  Sigma_w(d,h) by kappa_w(d)^2
```

is forbidden. The arrow may use averaged covariance calibration for
`Sigma_w(d,h)-|kappa_w(d)|^2`; it may not erase that difference pointwise.

### C. `CPC_3^sharp <-> RBDH_pair_short`

The rectangle-BDH representative estimates:

```text
E_n P_d(n+h)conj(P_d(n)) - Sigma_w(d,h)
```

in an averaged square. The pair-residual autocorrelation is:

```text
E_n R_d(n+h)conj(R_d(n))
  = E_n P_d(n+h)conj(P_d(n))
    - conj(kappa_w(d)) E_n P_d(n+h)
    - kappa_w(d) E_n conj(P_d(n))
    + |kappa_w(d)|^2.
```

Therefore the bridge between rectangle-BDH and CPC requires:

```text
RBDHCPCBridge_229
  = exact rectangle model Sigma_w(d,h)
    + pair mean calibration E_n P_d(n) ~ kappa_w(d)
    + covariance calibration Cov_w(d,h)
    + cutoff and smoothing transfer
    + pair-margin absorption
    + boundary transfer
    + W-limit order
    + prime-power transfer
    + range coverage
    + selector transfer.
```

Schematic conditional implication:

```text
RBDH_pair_short
  + RBDHCPCBridge_229
    => CPC_3^sharp.
```

Conversely:

```text
CPC_3^sharp
  + RBDHCPCBridge_229
    => RBDH_pair_short
```

only if the uncentered rectangle residual is reconstructed with the same
weighted cutoffs and local models.

Audit verdict:

```text
CPC_3^sharp <-> RBDH_pair_short
  is CONDITIONAL on RBDHCPCBridge_229.
```

Blocked shortcuts:

```text
first-moment Hardy-Littlewood => RBDH_pair_short,
ordinary rectangle-BDH => endpoint CPC,
Sigma_w(d,h)=kappa_w(d)^2 pointwise.
```

All three remain forbidden or underspecified.

### D. Major-arc model matching

The projected major-arc arrow is:

```text
WProjectedLocalMatch_3^major(P_adm)
  + ProjectedModelNeutrality_3^major(P_adm)
    => ProjectedMajorTarget_3^B(P_adm).
```

The analytic side package is:

```text
MajorAnalyticPkg_229
  = exact projected local model Omega_w^proj(d,h,k;t)
    + residual subset-HL matching for all S subset V
    + structural collision synchronization
    + collision-defect control if a generic model is used
    + kernel absolute-mass and kernel-tail control
    + cyclic-to-interval boundary transfer
    + projection-boundary transfer
    + W-residue compatibility
    + prime-power transfer
    + denominator and CRT range admissibility
    + model-neutrality after inclusion-exclusion
    + selector transfer.
```

`LocalBdPkg_226` enters only as:

```text
LocalBdPkg_226
  => one fixed projected-major boundary/prefix row
```

inside the larger boundary-transfer package. It is not full
`CycIntTransfer_3^major`, not full selector transfer, and not the major-arc
endpoint.

Audit verdict:

```text
ProjectedMajorTarget_3^B
  is CONDITIONAL on MajorAnalyticPkg_229.
```

Blocked shortcuts:

```text
first-moment tuple HL,
full eight-form Theta_w^proj without residual inclusion-exclusion,
unprojected Omega_w when kernel shifts t are active,
collision-free generic factors without CollDef control.
```

### E. Minor-arc large-spectrum control

The minor-arc route is:

```text
NarrowMinorArc_3^B
  + MinorArcTransfer_3^B
    => MinorTarget_3^B.
```

The analytic side package is:

```text
MinorAnalyticPkg_229
  = low-level L^2 leakage control
    + bad-shift moment control
    + persistent-frequency multiplicity control
    + non-tautological transverse incidence control
    + threshold stability
    + adaptive residual restriction for B_d
    + arc-boundary stability
    + interval/cyclic boundary transfer
    + W-limit order and W-growth control
    + prime-power transfer
    + dyadic range coverage
    + selector transfer.
```

The transverse row must be supplied as an estimate smaller than the endpoint:

```text
Eng(I_trans(lambda))
  <= Gamma_trans(lambda;D,R,eta,w),
```

with:

```text
sum_lambda lambda^2 Gamma_trans(lambda;D,R,eta,w)=o(1).
```

Audit verdict:

```text
MinorTarget_3^B
  is CONDITIONAL on MinorAnalyticPkg_229.
```

Blocked shortcuts:

```text
ordinary pair-BDH,
ordinary rectangle-BDH,
first-moment Hardy-Littlewood,
Gamma_trans approximately M_minor(D),
full AU^3/CPC/RBDH used as the transverse estimate.
```

The last line is circular: it assumes an endpoint-strength object to prove the
minor side of the endpoint.

## 6. Combined endpoint dependency table

| Arrow / target | Status in this audit | Required side package |
|---|---|---|
| `ResCube_3^sharp <-> CPC_3^sharp` | `CONDITIONAL` | `PairResidualTransfer_229` |
| `CPC_3^sharp <-> SPAC_2^sharp` | `CONDITIONAL` before alignment, structural after alignment | `CPCSPACAlign_229` |
| `CPC_3^sharp <-> RBDH_pair_short` | `CONDITIONAL` | `RBDHCPCBridge_229` |
| `ProjectedMajorTarget_3^B` | `CONDITIONAL` | `MajorAnalyticPkg_229` |
| `MinorTarget_3^B` | `CONDITIONAL` | `MinorAnalyticPkg_229` |
| full nonzero recomposition | `CONDITIONAL` outside exact sharp partition | `MajorMinorSelCompat_3(P_adm)` |

This table is not a proof graph. It is a list of toll gates that must be
passed before the endpoint equivalence chain can be used.

## 7. Edge cases

- If `LinFour_L(D)` is not controlled, pair residual control for `R_d` does
  not control the derivative residual `B_d`.
- If zero frequency is kept on one side and removed on another, mean terms
  such as `c_d` and `1-kappa_w(d)` leak into the comparison.
- If rectangle cutoffs differ from pair autocorrelation cutoffs, the
  `RBDHCPCBridge_229` reconstruction is not the same statement.
- If `Sigma_w(d,h)-|kappa_w(d)|^2` is large on an averaged square scale,
  centered pair autocorrelations are not negligible.
- If major and minor projections are smoothed or buffered differently,
  recomposition requires Module 218, not the exact sharp split.
- If `LocalBdPkg_226` is cited beyond its fixed row, the boundary claim is
  too strong.
- If collision strata are included in the exact model on one side and removed
  on the other, structural synchronization is missing.
- If W-limit estimates are proved only on a diagonal `w=w(N)`, the project
  double-limit order has not been supplied.
- If selector class changes, Module 230 must attach the correct selector
  transfer requirements before the arrow is endpoint-ready.
- Negative shifts must remain in the same dyadic and boundary accounting as
  positive shifts.

## 8. Where it fits in the project map

Module 227 inventoried all endpoint arrows. Module 228 separated the genuinely
structural identities. Module 229 now records the analytic toll gates for the
remaining arrows:

```text
Module 227
  -> endpoint arrow inventory
Module 228
  -> structural arrow audit
Module 229
  -> analytic side-package audit
Module 230
  -> selector-transfer requirements attached to each arrow.
```

The most important correction is:

```text
endpoint equivalence is not a single theorem in the current ledger;
it is a chain of structural identities plus conditional analytic bridges.
```

## 9. What remains open

This module does not prove:

- `PairResidualTransfer_229`;
- `LinearU2Margin_229`;
- `CPCSPACAlign_229`;
- `CovCal_229`;
- `RBDHCPCBridge_229`;
- `MajorAnalyticPkg_229`;
- `MinorAnalyticPkg_229`;
- `MajorMinorSelCompat_3(P_adm)`;
- `LocalBdPkg_226`;
- `WProjectedLocalMatch_3^major`;
- `ProjectedModelNeutrality_3^major`;
- `NarrowMinorArc_3^B`;
- `MinorArcTransfer_3^B`;
- `ProjectedMajorTarget_3^B`;
- `MinorTarget_3^B`;
- `ResCube_3^sharp`;
- `RBDH_pair_short`;
- `CPC_3^sharp`;
- `SPAC_2^sharp`;
- `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not treat this audit as a proof of any analytic side package.
- Do not cite ordinary pair-BDH as `PairResidualTransfer_229`.
- Do not cite ordinary rectangle-BDH as `RBDHCPCBridge_229`.
- Do not cite first-moment Hardy-Littlewood as variance-strength residual
  control.
- Do not replace `Sigma_w(d,h)` pointwise by `kappa_w(d)^2`.
- Do not replace `Omega_w^proj` by `Theta_w^proj`, by `Omega_w`, or by a
  collision-free generic model without the matching compatibility row.
- Do not use `LocalBdPkg_226` as full boundary transfer.
- Do not use `AU^3`, `CPC_3^sharp`, `RBDH_pair_short`, or `ResCube_3^sharp`
  as an input to prove one side of the same endpoint unless the circularity is
  explicitly broken.
- Do not transfer model, cyclic, smoothed, frozen, Bernoulli, finite-stage, or
  W-tricked estimates to the actual sharp moving selector without Module 230's
  selector-transfer ledger.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem,
  `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
