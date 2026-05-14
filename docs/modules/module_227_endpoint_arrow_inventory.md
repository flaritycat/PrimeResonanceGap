# Module 227: Endpoint-equivalence arrow inventory

## 1. Precise theorem / claim being advanced

This module builds an inventory of the endpoint-equivalence arrows surrounding
the residual derivative cube branch.

The objects inventoried are:

```text
ResCube_3^sharp,
RBDH_pair_short,
CPC_3^sharp,
SPAC_2^sharp,
SU2Pair_2^sharp,
DyadicDerivativeU^2,
AU^3.
```

Claim:

```text
EndpointArrowInventory_227
```

is the current structural map of arrows between these objects, with side
packages, selector class, and boundary-transfer location recorded.

This module does not prove any endpoint arrow. It records where later audits
must decide whether an arrow is exact algebra, structural extraction,
conditional analytic implication, or open.

## 2. Status label

`STRUCTURAL / EXTRACTION`

The module is a dependency inventory. It adds no estimate and does not upgrade
the endpoint class.

## 3. Definitions and variables

The residual derivative object is:

```text
f=nu-1,
B_d(n)=f(n+d)conj(f(n)),
c_d=E_n B_d(n),
B_d^circ(n)=B_d(n)-c_d.
```

The residual cube endpoint is:

```text
ResCube_3^sharp(Hcal):
  (1/D) sum_{D<|d|<=2D}
    sum_{xi != 0} |widehat{B_d}(xi)|^4=o(1)
```

uniformly in the required dyadic short-shift range `D<=Hcal(N)`, with the
project W-limit order and the correct selector-transfer line.

The pair product and pair-centered object are:

```text
P_d(n)=nu(n+d)conj(nu(n)),
R_d(n)=P_d(n)-kappa_w(d).
```

The exact pair and rectangle local models are:

```text
kappa_w(d),
Sigma_w(d,h).
```

The residual cube local model is:

```text
Omega_w(d,h,k)
  = sum_{S subset {0,1}^3} (-1)^(8-|S|) Theta_{w,S}(d,h,k).
```

In projected major-arc form, use:

```text
Omega_w^proj(d,h,k;t),
P_M,
LocalBdPkg_226.
```

The representative endpoint objects are:

```text
RBDH_pair_short(Hcal):
  rectangle-BDH strength for P_d/R_d against Sigma_w(d,h),
  with exact local models, pair margins, W-limit, boundary, selector, and
  range packages included.

CPC_3^sharp(Hcal):
  sharp correlation/covariance cancellation for the pair-centered object
  R_d, in the project endpoint normalization.

SPAC_2^sharp:
  sharp shifted-pair autocorrelation package for the pair residual, with
  exact pair and rectangle local models.

SU2Pair_2^sharp:
  shifted-pair U^2 package for the pair residual.

DyadicDerivativeU^2:
  averaged U^2 control of Delta_d f=B_d, equivalently the nonzero Fourier
  fourth moment after centering.

AU^3:
  anisotropic U^3 / eight-vertex box formulation of the same derivative cube,
  modulo the endpoint side packages.
```

Selector class convention:

```text
mv = actual sharp moving selector
```

is required for the actual endpoint. Any statement first proved in:

```text
model, W, cyc, int, sm, fr, bern, fs
```

must pass through the relevant selector-transfer graph before it can be used
as an `mv` endpoint statement.

## 4. Assumptions

This inventory assumes only the project ledger:

```text
the endpoint class is OPEN;
ResCube_3^sharp is OPEN;
RBDH_pair_short is OPEN;
CPC_3^sharp is OPEN;
AU^3 is OPEN;
ordinary pair-BDH alone does not imply CPC_3^sharp;
first-moment Hardy-Littlewood does not imply RBDH;
Sigma_w(d,h) is not pointwise kappa_w(d)^2.
```

The inventory also keeps the local-row verdict from Module 226:

```text
LocalBdPkg_226
  => BdPrefRow_224^P=o_W(1)
```

only for one fixed projected-major cyclic-to-interval boundary/prefix row.
It is not a full `CycIntTransfer_3^major(P_adm)` theorem.

## 5. Arrow inventory / reduction map

The arrows below are a map, not a closure proof.

### A. Fourier and derivative arrows

| Arrow | Source | Target | Type | Status | Side packages / warnings |
|---|---|---|---|---|---|
| A1 | `ResCube_3^sharp` | `DyadicDerivativeU^2` | Fourier `U^2` identity for `B_d^circ` | `STRUCTURAL / EXTRACTION` | zero mode removed; same dyadic `D`; interval/cyclic transfer explicit |
| A2 | `DyadicDerivativeU^2` | `ResCube_3^sharp` | same identity reversed | `STRUCTURAL / EXTRACTION` | no analytic estimate supplied |
| A3 | `DyadicDerivativeU^2` | `AU^3` | eight-vertex box reindexing | `STRUCTURAL / EXTRACTION` | boundary, W-limit, selector, prime-power, and range packages still external |
| A4 | `AU^3` | `DyadicDerivativeU^2` | box-to-derivative reindexing | `STRUCTURAL / EXTRACTION` | projected versions need projection compatibility |

These arrows explain why derivative and anisotropic-box language are useful.
They do not make the averaged fourth moment small.

### B. Residual cube to CPC arrows

| Arrow | Source | Target | Type | Status | Side packages / warnings |
|---|---|---|---|---|---|
| B1 | `ResCube_3^sharp` | `CPC_3^sharp` | residual-to-pair covariance transfer | `CONDITIONAL` | pair decomposition `P_d=1+f(n+d)+conj(f(n))+B_d`; linear-margin absorption; zero-mode convention; exact `kappa_w(d)`; selector transfer |
| B2 | `CPC_3^sharp` | `ResCube_3^sharp` | pair covariance back to residual derivative cube | `CONDITIONAL` | requires controlling the linear margin and constant terms rather than assuming pair control is residual control |

The direct obstruction from Module 198 applies here:

```text
ordinary pair-BDH alone is not B1.
```

It controls the wrong object unless the residual decomposition and linear
margin rows are included.

### C. CPC, SPAC, and shifted-pair U2 arrows

| Arrow | Source | Target | Type | Status | Side packages / warnings |
|---|---|---|---|---|---|
| C1 | `CPC_3^sharp` | `SPAC_2^sharp` | covariance-to-shifted-pair autocorrelation extraction | `CONDITIONAL` | exact pair model, centering by `kappa_w(d)`, range coverage |
| C2 | `SPAC_2^sharp` | `CPC_3^sharp` | autocorrelation-to-covariance reconstruction | `CONDITIONAL` | same model and centering conventions required |
| C3 | `SPAC_2^sharp` | `SU2Pair_2^sharp` | Fourier/autocorrelation `U^2` identity for the pair residual | `STRUCTURAL / EXTRACTION` | exact selector and boundary conventions must match |
| C4 | `SU2Pair_2^sharp` | `SPAC_2^sharp` | reverse `U^2` identity | `STRUCTURAL / EXTRACTION` | no analytic estimate supplied |

The structural arrows C3-C4 are identities only after the same object, same
centering, same selector class, and same domain are fixed.

### D. CPC and RBDH arrows

| Arrow | Source | Target | Type | Status | Side packages / warnings |
|---|---|---|---|---|---|
| D1 | `CPC_3^sharp` | `RBDH_pair_short` | covariance package to rectangle variance package | `CONDITIONAL` | rectangle local model `Sigma_w(d,h)`, pair-margin absorption, smoothing/cutoff transfer, W-limit order, range coverage |
| D2 | `RBDH_pair_short` | `CPC_3^sharp` | rectangle variance package to covariance package | `CONDITIONAL` | endpoint-grade RBDH only; first-moment HL and ordinary rectangle-BDH are insufficient |

The Module 199 warning attaches here:

```text
mean rectangle-HL does not imply RBDH,
ordinary rectangle-BDH is not enough unless upgraded to the residual,
adaptive, variance-strength endpoint package.
```

### E. Major/minor decomposition arrows for ResCube

| Arrow | Source | Target | Type | Status | Side packages / warnings |
|---|---|---|---|---|---|
| E1 | `ResCube_3^sharp` | `ProjectedMajorTarget_3^B + MinorTarget_3^B` | Fourier major/minor split | `STRUCTURAL / EXTRACTION` | zero mode excluded; denominator partition compatibility |
| E2 | `ProjectedMajorTarget_3^B + MinorTarget_3^B` | `ResCube_3^sharp` | recomposition of nonzero frequencies | `CONDITIONAL` | requires `MajorMinorSelCompat_3(P_adm)`, boundary/arc partition rows, and same selector chain |

On the major side:

```text
ProjectedMajorTarget_3^B
```

requires:

```text
WProjectedLocalMatch_3^major,
ProjectedModelNeutrality_3^major,
LocalModelCompat_3^major,
CycIntTransfer_3^major,
PPSPTransfer_3^major,
selector transfer.
```

The new local-row verdict enters only as:

```text
LocalBdPkg_226
  -> one fixed boundary/prefix row inside CycIntTransfer_3^major.
```

It does not supply full boundary transfer, full selector transfer, or the
endpoint.

On the minor side:

```text
MinorTarget_3^B
```

requires:

```text
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
adaptive residual minor-arc restriction,
large-spectrum control.
```

## 6. Selector and boundary locations

The endpoint arrows should be read in selector class `mv` only after selector
transfer has been supplied. Current structural work often lives first in:

```text
model, W, cyc, int, sm, fr.
```

The selector-transfer dependencies are:

```text
SelectorTransferGraph_3^consol,
MajorSelectorTransfer_3^P,
MinorArcTransfer_3^B,
MajorMinorSelCompat_3(P_adm),
FrozenMovingObstruction_3^Pi,
DetExtract_3^Pi(s -> mv).
```

Boundary transfer enters at multiple places:

```text
cyclic-to-interval projected major transfer,
interval cutoff transfer,
kernel-tail transfer,
zero-mode leakage after truncation,
W-residue boundary compatibility,
prime-power/boundary overlap,
dyadic prefix safety.
```

`LocalBdPkg_226` handles only the first local test row in this list. It should
be carried forward as evidence that a truly local row can be formulated, not
as evidence that all boundary transfer is solved.

## 7. Edge cases

- If an arrow changes selector class, it is not just an endpoint-equivalence
  arrow; it also requires selector transfer.
- If an arrow changes cyclic/interval domain, it requires boundary transfer.
- If an arrow changes smoothed/sharp projection, it requires projection
  boundary control.
- If the zero frequency is treated differently, the centering row must be
  named.
- If `Sigma_w(d,h)` is replaced by `kappa_w(d)^2`, the RBDH/CPC arrow is
  invalid.
- If pair-BDH is cited without linear-margin absorption, the `ResCube` to
  `CPC` route is not justified.
- If first-moment HL is cited as variance strength, the `RBDH` arrow is not
  justified.
- If major and minor arcs use different denominator grids, recomposition needs
  the Module 218 compatibility rows.
- If `LocalBdPkg_226` is used outside its fixed row, the citation is too
  strong.

## 8. Where it fits in the project map

Phase E now has:

```text
Module 224
  -> fixed local boundary/prefix row
Module 225
  -> expanded row into boundary-marked tuple envelopes
Module 226
  -> classified row as conditional local under LocalBdPkg_226
Module 227
  -> inventories endpoint-equivalence arrows and side-package locations.
```

The next two modules should refine this inventory:

```text
Module 228:
  audit exact algebra and structural extraction arrows.

Module 229:
  audit analytic side-package arrows.
```

Module 230 should then attach selector-transfer requirements to every arrow.

## 9. What remains open

This module does not prove:

- any arrow in the endpoint class;
- `ResCube_3^sharp`;
- `RBDH_pair_short`;
- `CPC_3^sharp`;
- `SPAC_2^sharp`;
- `SU2Pair_2^sharp`;
- `DyadicDerivativeU^2` as an estimate;
- `AU^3`;
- `ProjectedMajorTarget_3^B`;
- `NarrowMinorArc_3^B`;
- `WProjectedLocalMatch_3^major`;
- `CycIntTransfer_3^major(P_adm)`;
- `LocalBdPkg_226`;
- `MajorMinorSelCompat_3(P_adm)`;
- selector transfer to the actual sharp moving selector;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not read an inventory arrow as a proved theorem.
- Do not label any endpoint arrow `PROVEN` unless a later ledger entry
  supplies the proof.
- Do not cite ordinary pair-BDH as `CPC_3^sharp`.
- Do not cite first-moment Hardy-Littlewood as `RBDH_pair_short`.
- Do not replace `Sigma_w(d,h)` pointwise by `kappa_w(d)^2`.
- Do not treat `LocalBdPkg_226` as full boundary transfer.
- Do not transfer model, cyclic, smoothed, frozen, Bernoulli, or finite-stage
  statements to the actual sharp moving selector without the selector-transfer
  packages.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem,
  `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
