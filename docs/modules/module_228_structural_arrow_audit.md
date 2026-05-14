# Module 228: Structural endpoint-arrow audit

## 1. Precise theorem / claim being advanced

This module audits the arrows from Module 227 that are exact algebra or
structural extraction arrows once the same object, domain, projection,
centering, and selector convention have been fixed.

Define:

```text
StructuralArrowAudit_228.
```

Claim:

```text
StructuralArrowAudit_228
```

separates the endpoint map into:

```text
structural identities of quantities
```

and:

```text
analytic estimates / transfer theorems.
```

The structural identities do not prove the endpoint estimates. They only say
that, inside one fixed model, two displayed quantities are the same quantity
or are obtained from each other by a deterministic reindexing.

## 2. Status label

`STRUCTURAL / EXTRACTION`

No endpoint estimate is established. No endpoint arrow is upgraded to
`PROVEN`.

## 3. Definitions and variables

For the derivative residual:

```text
f=nu-1,
B_d(n)=f(n+d)conj(f(n)),
c_d=E_n B_d(n),
B_d^circ(n)=B_d(n)-c_d.
```

The normalized Fourier transform is:

```text
widehat{F}(xi)=E_n F(n)e(-xi n).
```

The derivative `U^2` quantity is:

```text
DDU2(D)
  = (1/D) sum_{D<|d|<=2D} ||B_d^circ||_{U^2}^4.
```

The residual Fourier quantity is:

```text
ResFour(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi != 0} |widehat{B_d}(xi)|^4.
```

The anisotropic eight-vertex box quantity is:

```text
AUBox(D)
  = (1/D) sum_{D<|d|<=2D}
      E_{n,h,k}
        B_d(n) conj(B_d(n+h)) conj(B_d(n+k)) B_d(n+h+k)
      - mean contribution,
```

where the mean contribution is exactly the zero-frequency term required by
the chosen centering convention.

For pair residuals, define:

```text
P_d(n)=nu(n+d)conj(nu(n)),
R_d(n)=P_d(n)-kappa_w(d).
```

The pair autocorrelation quantity is:

```text
SPACQty(D)
  = (1/D) sum_{D<|d|<=2D}
      E_h | E_n R_d(n+h)conj(R_d(n)) |^2,
```

with whatever smoothing or interval cutoff is fixed before the identity is
used.

The pair `U^2` quantity is:

```text
SU2PairQty(D)
  = (1/D) sum_{D<|d|<=2D} ||R_d||_{U^2}^4.
```

For a major/minor split, let:

```text
Major(R,eta) subset {xi != 0},
Minor(R,eta)={xi != 0}\Major(R,eta),
```

or let `m_M`, `m_minor` be a declared smoothed partition.

## 4. Assumptions

Every structural arrow below assumes:

- one fixed finite cyclic Fourier model, or an interval model already
  transferred to that Fourier model;
- normalized averaging conventions are identical on both sides;
- the same dyadic shell `D<|d|<=2D`;
- the same W-tricked residue convention;
- the same selector class;
- no movement between model, W, cyclic, interval, smoothed, frozen,
  Bernoulli, finite-stage, and actual moving selectors;
- zero frequency is handled identically on both sides;
- if a projection appears, it is applied to the same object on both sides.

If any of these assumptions fails, the arrow is no longer a pure structural
identity. It becomes a conditional transfer statement and belongs to Module
229 or Module 230.

## 5. Proof / disproof / reduction

### A. `ResCube_3^sharp <-> DyadicDerivativeU^2`

Structural identity:

```text
DDU2(D)=ResFour(D).
```

Indeed:

```text
||B_d^circ||_{U^2}^4
  = sum_xi |widehat{B_d^circ}(xi)|^4
  = sum_{xi != 0} |widehat{B_d}(xi)|^4,
```

because:

```text
widehat{B_d}(0)=c_d,
B_d^circ=B_d-c_d.
```

This is an identity of quantities. The estimate:

```text
DDU2(D)=o(1)
```

is exactly the open residual cube endpoint in derivative language.

Audit verdict:

```text
structural both directions,
no analytic estimate,
no selector transfer,
no interval transfer.
```

### B. `DyadicDerivativeU^2 <-> AU^3`

Structural reindexing:

```text
||B_d^circ||_{U^2}^4
```

expands to the centered version of:

```text
E_{n,h,k}
  B_d(n) conj(B_d(n+h)) conj(B_d(n+k)) B_d(n+h+k).
```

After substituting:

```text
B_d(x)=f(x+d)conj(f(x)),
```

the eight vertices are:

```text
n, n+d,
n+h, n+h+d,
n+k, n+k+d,
n+h+k, n+h+k+d.
```

This is the anisotropic `AU^3` / box arrangement in the derivative direction.

Audit verdict:

```text
structural reindexing of the same eight vertices,
but only after the centering convention and domain are fixed.
```

Not structural for free:

```text
projected AU^3 <-> projected derivative U^2
```

unless the same projection is applied to `Delta_d f=B_d` in the same Fourier
model. Moving a projection from `B_d` to `f` is not an algebraic identity.

### C. `SPAC_2^sharp <-> SU2Pair_2^sharp`

For a fixed pair residual `R_d`, the `U^2` identity gives:

```text
||R_d||_{U^2}^4
  = E_{n,h,k}
      R_d(n) conj(R_d(n+h)) conj(R_d(n+k)) R_d(n+h+k).
```

Equivalently, by Fourier:

```text
||R_d||_{U^2}^4
  = sum_xi |widehat{R_d}(xi)|^4.
```

The shifted-pair autocorrelation form satisfies:

```text
E_h |E_n R_d(n+h)conj(R_d(n))|^2
  = sum_xi |widehat{R_d}(xi)|^4
```

in the fixed cyclic model. Thus:

```text
SPACQty(D)=SU2PairQty(D)
```

after averaging over the same dyadic `d` shell.

Audit verdict:

```text
structural both directions for the same R_d.
```

Not structural for free:

```text
P_d -> R_d,
R_d -> B_d,
cyclic -> interval,
model selector -> actual moving selector.
```

Those are centering, margin, boundary, or selector-transfer operations.

### D. `ResCube_3^sharp <-> major/minor Fourier split`

In a sharp exact partition of the nonzero frequencies:

```text
{xi != 0}=Major(R,eta) disjoint_union Minor(R,eta),
```

one has:

```text
ResFour(D)=M_major(D)+M_minor(D),
```

where:

```text
M_major(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Major(R,eta)} |widehat{B_d}(xi)|^4,

M_minor(D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)} |widehat{B_d}(xi)|^4.
```

Therefore, inside the exact sharp partition:

```text
M_major(D)=o(1) and M_minor(D)=o(1)
  => ResFour(D)=o(1),
```

and:

```text
ResFour(D)=o(1)
  => M_major(D)=o(1), M_minor(D)=o(1),
```

because both summands are nonnegative.

Audit verdict:

```text
structural only for a fixed exact partition of the same nonzero frequency
space.
```

If the project uses smoothed multipliers, buffered arcs, different denominator
grids, or different selector chains on the major and minor sides, recomposition
requires the Module 218 compatibility rows:

```text
PartBdSel_4,
ArcBdSel_4,
DenMMErr,
ZeroMMErr,
ChainMMErr,
BdMMErr,
PPWMMErr.
```

In that setting the recomposition is conditional, not pure algebra.

### E. Arrows deliberately excluded from the structural audit

The following are not structural arrows in the present ledger:

```text
ResCube_3^sharp <-> CPC_3^sharp,
CPC_3^sharp <-> SPAC_2^sharp,
CPC_3^sharp <-> RBDH_pair_short.
```

They require analytic or transfer side packages:

```text
pair-margin absorption,
linear U^2 control,
local covariance calibration,
exact rectangle model Sigma_w(d,h),
boundary transfer,
selector transfer,
prime-power transfer,
W-limit order,
range coverage.
```

They are deferred to Module 229.

## 6. Edge cases

- If the zero frequency is not removed, the derivative/residual identity
  gains the `|c_d|^4` term.
- If `B_d` is replaced by `P_d` or `R_d`, the structural identity changes
  object and no longer represents the same residual statement.
- If the domain changes from cyclic to interval, boundary transfer is needed.
- If a smoothed projection is used, the Fourier weight is `|m(xi)|^4`, not a
  sharp indicator.
- If the major and minor denominator grids differ, the partition identity is
  no longer exact.
- If the selector class changes, selector transfer is needed before comparing
  endpoint statements.
- If centering is performed before projection on one side and after interval
  truncation on the other, zero-mode leakage must be controlled.
- If `AU^3` is cited without the same eight-vertex derivative arrangement,
  the reindexing may refer to a different box norm.
- If `SPAC` is formed from `P_d` but `SU2Pair` is formed from `R_d`, the
  identity is false as stated.

## 7. Where it fits in the project map

Module 227 inventoried all endpoint arrows. Module 228 now identifies the
arrows that are genuinely structural:

```text
ResCube_3^sharp <-> DyadicDerivativeU^2,
DyadicDerivativeU^2 <-> AU^3,
SPAC_2^sharp <-> SU2Pair_2^sharp,
ResCube_3^sharp <-> exact major/minor Fourier split.
```

The remaining arrows move to the analytic side-package audit:

```text
Module 229:
  ResCube/CPC,
  CPC/SPAC,
  CPC/RBDH,
  major-arc model matching,
  minor-arc large-spectrum control,
  boundary and range packages.
```

## 8. What remains open

This module does not prove:

- `ResCube_3^sharp`;
- `DyadicDerivativeU^2=o(1)`;
- `AU^3`;
- `SPAC_2^sharp`;
- `SU2Pair_2^sharp`;
- `CPC_3^sharp`;
- `RBDH_pair_short`;
- major-arc cancellation;
- minor-arc cancellation;
- `ProjectedMajorTarget_3^B`;
- `NarrowMinorArc_3^B`;
- exact interval transfer;
- smoothed/sharp projection transfer;
- selector transfer to the actual sharp moving selector;
- `LocalBdPkg_226`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not confuse an identity of quantities with an estimate for that quantity.
- Do not cite `DyadicDerivativeU^2` or `AU^3` as proved analytic inputs.
- Do not move projections from `B_d` to `f` without a lemma.
- Do not merge `B_d`, `R_d`, and `P_d`.
- Do not treat a smoothed major/minor partition as an exact sharp partition.
- Do not use cyclic Fourier identities as interval estimates without boundary
  transfer.
- Do not transfer model, smoothed, frozen, Bernoulli, or finite-stage
  statements to the actual sharp moving selector without selector transfer.
- Do not replace `Sigma_w(d,h)` pointwise by `kappa_w(d)^2`.
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem,
  `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`.
