# Module 218: Major/minor selector-transfer compatibility audit

## 1. Precise theorem / claim being advanced

This module audits whether the major-arc and minor-arc selector-transfer
packages are compatible enough to be combined into a full nonzero residual
fourth-moment transfer.

Define:

```text
MajorMinorSelCompat_3(P_adm).
```

Conditional claim:

```text
MinorArcTransfer_3^B
  + MajorSelectorTransfer_3^P
  + MajorMinorSelCompat_3(P_adm)
    => FullNonzeroSelectorTransfer_3.
```

The implication is only a compatibility reduction. It does not prove the
minor-arc estimate, the major-arc estimate, any selector-transfer row, or the
residual cube endpoint.

The main warning is:

```text
major transfer + minor transfer != full transfer
```

unless the boundary between the major and minor projections is controlled in
the same residual fourth-moment normalization.

## 2. Status label

`CONDITIONAL`

The triangle-inequality composition is formal after the compatibility rows are
assumed. The smallness of those rows is open.

## 3. Definitions and variables

Let `s` be a selector or model class:

```text
fs, bern, sm, fr, mv, W, cyc, int, model.
```

For that class define:

```text
nu_s,
f_s=nu_s-1,
B_{d,s}(n)=f_s(n+d)conj(f_s(n)).
```

If centered products are used:

```text
c_{d,s}=E_n B_{d,s}(n),
B_{d,s}^circ=B_{d,s}-c_{d,s}.
```

The target actual selector is:

```text
mv: chi_alpha(p)=1_{||alpha p||<1/log p}.
```

For an adjacent selector edge:

```text
a -> b,
```

write:

```text
Delta B_d(a->b)=B_{d,b}-T_{a->b}B_{d,a},
```

with `T_{a->b}` omitted when both objects live on the same interval and
frequency space.

Let:

```text
P_M^s
```

be the major-arc projection used in selector class `s`, with multiplier
`m_M^s`, denominator range `R_M^s`, arc width `eta_M^s`, and zero-mode
convention inherited from Modules 206 and 209.

Let:

```text
Pi_minor^s
```

be the minor-arc projection used in selector class `s`, with denominator range
`R_m^s` and arc width `eta_m^s`.

The full nonzero transfer norm is:

```text
FullSelErr_4(a->b;D)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi != 0} |widehat{Delta B_d(a->b)}(xi)|^4.
```

The major projected transfer norm is:

```text
MajorSelErr_4^P(a->b;N,w;rho)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi != 0}
        |m_M^b(xi)|^4 |widehat{Delta B_d(a->b)}(xi)|^4.
```

The minor transfer norm is:

```text
MinorSelErr_4(a->b;D;R,eta)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in Minor(R,eta)}
        |widehat{Delta B_d(a->b)}(xi)|^4.
```

If the minor projection is smoothed, replace the indicator by the multiplier
`m_minor` and use `|m_minor(xi)|^4`.

## 4. Assumptions: compatibility rows

`MajorMinorSelCompat_3(P_adm)` consists of the following rows.

### A. Common dyadic and W-limit conventions

The major and minor packages must use the same dyadic shift range:

```text
D<|d|<=2D,
D in D_range(N,Hcal).
```

All W-dependent rows must use:

```text
lim_{w->infinity} limsup_{N->infinity}
```

with `w` fixed during the `N -> infinity` limit.

The compatibility error is:

```text
RangeWCompatErr(a->b;N,w)=o_W(1).
```

This row is structural if the ranges and W-limit order are literally the
same. Otherwise it must be estimated.

### B. Projection partition compatibility

For sharp disjoint projections one wants:

```text
{xi != 0}
  = Major(R,eta) disjoint_union Minor(R,eta).
```

For smoothed or buffered projections one needs a fourth-moment partition
defect. Define:

```text
PartDef(xi)
  = |1_{xi != 0}
      - |m_M(xi)|^4
      - |m_minor(xi)|^4 |.
```

Then:

```text
PartBdSel_4(a->b)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi != 0} PartDef(xi)
        |widehat{Delta B_d(a->b)}(xi)|^4.
```

The package requires:

```text
PartBdSel_4(a->b)=o(1)
```

or the W-admissible projected analogue. If the partition is sharp and exact,
this row is zero.

### C. Arc-boundary stability

If major and minor arcs are separated with a buffer, define:

```text
ArcBd(R,eta,eta')
  = Major(R,eta') \ Major(R,eta),
```

or the equivalent boundary band between the major and minor conventions.

The required row is:

```text
ArcBdSel_4(a->b)
  = (1/D) sum_{D<|d|<=2D}
      sum_{xi in ArcBd(R,eta,eta')}
        |widehat{Delta B_d(a->b)}(xi)|^4
  = o(1).
```

This row prevents selector transfer from moving mass across the major/minor
cut in a way neither package sees.

### D. Denominator compatibility

The major package may use:

```text
DenAdm(N,w;R_M,eta_M,P_M),
```

while the minor package may use:

```text
Minor(R_m,eta_m).
```

Define:

```text
DenMMErr(a->b;N,w)
```

for failures of the two denominator conventions to form one frequency
partition with bounded overlap, compatible CRT moduli, and the same W-limit
order.

The package requires:

```text
DenMMErr(a->b;N,w)=o_W(1).
```

This includes denominator changes caused by smoothing, finite-band selectors,
Bernoulli lifts, W-tricks, and buffered arcs.

### E. Zero-mode and centering compatibility

The minor package excludes:

```text
xi=0.
```

The major package also uses:

```text
m_M(0)=0
```

for the nonzero residual target. If either package keeps a mean term or uses
centered products, define:

```text
ZeroMMErr(a->b)
  = (1/D) sum_{D<|d|<=2D}
      |c_{d,b}-c_{d,a}|^4
```

plus any zero-mode leakage caused by interval truncation, kernel truncation,
or smoothing.

The package requires:

```text
ZeroMMErr(a->b)=o(1)
```

in the same limit order as the relevant branch.

### F. Selector-chain compatibility

The major and minor packages must transfer along the same selector edge:

```text
a -> b.
```

If the minor package uses:

```text
cyc -> int -> W -> smooth/frozen -> sharp,
```

and the major package uses:

```text
fs -> bern -> sm -> fr -> mv,
```

then the proof must define a common refinement of these chains. The
compatibility row is:

```text
ChainMMErr(a->b)=o(1),
```

meaning every edge is represented in both major and minor accounting or is
explicitly declared irrelevant to one side.

### G. Boundary accounting compatibility

Major-arc boundary rows include:

```text
CycIntTransfer_3^major,
SelBd_major^P,
ProjSel_major^P.
```

Minor-arc boundary rows include:

```text
BdInt_4,
ArcBd_4,
threshold stability,
dyadic D-range uniformity.
```

Define:

```text
BdMMErr(a->b)
```

for overlap, gaps, or double counting between these boundary conventions.

The package requires:

```text
BdMMErr(a->b)=o(1).
```

The proof may instead choose a disjoint accounting convention, but it must be
stated before the estimates are used.

### H. Prime-power and W-residue compatibility

The major package has:

```text
PPSPTransfer_3^major,
WResSel_major^P.
```

The minor package has:

```text
PPErr_4,
W-admissible minor transfer.
```

Define:

```text
PPWMMErr(a->b)
```

for mismatches in which a prime-power or W-residue failure is removed from one
side of the major/minor split but not the other.

The package requires:

```text
PPWMMErr(a->b)=o_W(1).
```

## 5. Conditional proof / reduction

Assume first the ideal sharp partition:

```text
{xi != 0}=Major disjoint_union Minor.
```

Then for each `d`:

```text
sum_{xi != 0} |widehat{Delta B_d}(xi)|^4
  = sum_{xi in Major} |widehat{Delta B_d}(xi)|^4
    + sum_{xi in Minor} |widehat{Delta B_d}(xi)|^4.
```

Averaging over `D<|d|<=2D` gives:

```text
FullSelErr_4(a->b)
  = MajorSelErr_4^P(a->b)
    + MinorSelErr_4(a->b).
```

For smoothed, buffered, transported, or model-dependent projections, insert
the compatibility rows:

```text
FullSelErr_4(a->b)
  <= C MajorSelErr_4^P(a->b)
     + C MinorSelErr_4(a->b)
     + C PartBdSel_4(a->b)
     + C ArcBdSel_4(a->b)
     + C DenMMErr(a->b)
     + C ZeroMMErr(a->b)
     + C ChainMMErr(a->b)
     + C BdMMErr(a->b)
     + C PPWMMErr(a->b).
```

Therefore, if:

```text
MinorArcTransfer_3^B,
MajorSelectorTransfer_3^P,
MajorMinorSelCompat_3(P_adm)
```

all hold in the required ranges and limit order, then:

```text
FullNonzeroSelectorTransfer_3
```

holds for the same selector edge.

No row in this proof is estimated.

## 6. Compatibility diagnosis

The audit gives a narrow verdict:

```text
Major and minor selector-transfer packages are composable only after an
explicit projection-boundary package.
```

The most dangerous gap is:

```text
PartBdSel_4 + ArcBdSel_4.
```

If those rows are not small, then mass can move between major and minor arcs
under selector changes, smoothing, W-normalization, or denominator changes.
In that case proving a major transfer and a minor transfer separately does
not prove a full selector transfer.

This is not a rejection of the major/minor split. It is a requirement that the
split be part of the selector-transfer object, not an afterthought.

## 7. Edge cases

- If the major projection is smoothed and the minor projection is sharp, then
  `|m_M|^4+1_{minor}` may overlap or leave gaps.
- If major and minor arcs use different denominator bounds, a frequency may
  change side after transport.
- If the zero frequency is excluded in one package but centered in another,
  mean leakage can be double counted or missed.
- If the selector chain differs between major and minor arcs, the adjacent
  transfer errors do not refer to the same `Delta B_d`.
- If a W-residue or prime-power term is removed only in the major package, the
  minor complement may still contain it.
- If the major arc uses a buffered projection and the minor arc uses threshold
  large-spectrum sets, both buffer and threshold stability are needed.
- If `D` varies over the endpoint dyadic range, partition compatibility must
  be uniform in `D`.
- If the proof chooses a disjoint boundary convention, it must declare it
  before estimating any row.

## 8. Where it fits in the project map

The Phase D chain now has:

```text
Module 214
  -> third 9-iteration plan update
Module 215
  -> selector inventory
Module 216
  -> global selector-transfer matrix
Module 217
  -> narrowed plan challenge
Module 218
  -> major/minor selector-transfer compatibility.
```

The next scheduled module is the frozen-to-moving dyadic threshold transfer
obstruction in residual fourth-moment normalization.

## 9. What remains open

This module does not prove:

- `MajorMinorSelCompat_3(P_adm)`;
- `PartBdSel_4=o(1)`;
- `ArcBdSel_4=o(1)`;
- `DenMMErr=o_W(1)`;
- `ZeroMMErr=o(1)`;
- `ChainMMErr=o(1)`;
- `BdMMErr=o(1)`;
- `PPWMMErr=o_W(1)`;
- `MinorArcTransfer_3^B`;
- `MajorSelectorTransfer_3^P`;
- `SharpSelectorTransfer_3`;
- `WProjectedLocalMatch_3^major`;
- `ProjectedMajorTarget_3^B`;
- `NarrowMinorArc_3^B`;
- `ResCube_3^sharp`;
- `RBDH_pair_short`, `CPC_3^sharp`, or `AU^3`;
- the original positive existence problem;
- the all-alpha no-positive-limit theorem;
- the unconditional finite-type theorem.

## Red flags / forbidden upgrades

- Do not combine major and minor selector-transfer estimates without
  `MajorMinorSelCompat_3`.
- Do not assume a smoothed major projection and a sharp minor projection form
  an exact fourth-moment partition.
- Do not ignore frequencies in the major/minor boundary band.
- Do not use different selector-chain edges in the major and minor packages
  and then add the errors as if they were the same transfer.
- Do not hide zero-mode, denominator, W-residue, prime-power, boundary, or
  projection errors inside the phrase "major/minor split".
- Do not claim the residual cube endpoint, the original problem, the
  all-alpha theorem, the unconditional finite-type theorem, `RBDH_pair_short`,
  `CPC_3^sharp`, or `AU^3`.
