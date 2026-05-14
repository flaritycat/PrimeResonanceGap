# Module 315: Zero-mode product audit inside `P_minor^0`

## 1. Precise theorem / claim being advanced

This module audits the zero-mode product row isolated in Module 314.

Define:

```text
ZeroModeProductAudit_315(P_minor^0).
```

The row is:

```text
ZeroModeProductRow_314
  =
  D^(-1) sum_{d_1 != d_2}
    |beta_0(d_1,0)|^2 |beta_0(d_2,0)|^2.
```

The question is whether this row is killed by the local convention,
controlled by an available estimate, or should be rerouted by an exact
centered rewrite.

Verdict:

```text
ZeroModeProductAudit_315(P_minor^0):
  STRUCTURAL / EXTRACTION.

ZeroModeKilledByMinorConvention_315:
  FALSE / BLOCKED.

ZeroModeProductIdentity_315:
  STRUCTURAL / EXTRACTION.

CenteredRewriteRemovesExplicitZeroRow_315:
  STRUCTURAL / EXTRACTION.

CurrentZeroModeProductControl_315:
  FALSE / BLOCKED.

ZeroModeProductControl_314(P_minor^0):
  OPEN as a standalone estimate.

CenteredFullAntiDiagonalAudit_316(P_minor^0):
  OPEN next target.
```

The zero mode is not automatically zero in the uncentered split. However,
because the minor projection excludes zero frequency, the weighted minor row
can be rewritten exactly using centered products. This removes the explicit
zero row from the algebra but does not prove any anti-diagonal gain.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This module gives identities and a proof-route decision. It proves no
weighted pair estimate, no column-barrier smallness, no threshold closure, no
adaptive-shell gain, no minor-arc endpoint, and no selector transfer.

## 3. Definitions and variables

Work inside:

```text
P_minor^0,
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d|<=2D.
```

Use:

```text
f_0(n)=nu_0(n)-1,
B_d^0(n)=f_0(n+d)conj(f_0(n)),
beta_0(d,xi)=widehat{B_d^0}(xi).
```

Define the zero coefficient:

```text
Z_d
  =
  beta_0(d,0)
  =
  E_{n in G_N} B_d^0(n)
  =
  E_n f_0(n+d)conj(f_0(n)).
```

Define the centered residual-pair product:

```text
B_d^{0,circ}(n)
  =
  B_d^0(n)-Z_d.
```

Then:

```text
widehat{B_d^{0,circ}}(0)=0,
widehat{B_d^{0,circ}}(xi)=beta_0(d,xi) for xi != 0.
```

Define its cyclic autocorrelation:

```text
A_d^{circ}(h)
  =
  E_n B_d^{0,circ}(n)conj(B_d^{0,circ}(n+h)).
```

The original uncentered autocorrelation is:

```text
A_d(h)=E_n B_d^0(n)conj(B_d^0(n+h)).
```

They satisfy:

```text
A_d^{circ}(h)=A_d(h)-|Z_d|^2.
```

## 4. Assumptions

This module assumes the active status ledger and Modules 278, 284, 297, 308,
309, 310, 311, 312, 313, and 314.

It uses only:

```text
the finite cyclic Fourier normalization,
the fact that Minor_0(R,eta) excludes xi=0,
the Module 314 row split,
and finite algebra.
```

It does not assume:

```text
ZeroModeProductControl_314(P_minor^0),
CenteredFullAntiDiagonalAudit_316(P_minor^0),
FullAntiDiagonalControl_314(P_minor^0),
MajorKernelCorrectionControl_314(P_minor^0),
SignedMinorKernelCombinationTarget_314(P_minor^0),
AntiDiagonalTwoShiftKernelGain_312(P_minor^0),
WeightedColumnSecondMomentTarget_311(P_minor^0),
WeightedColumnPairEnergyTarget_310(P_minor^0),
OffDiagonalSameFrequencyPair_310(lambda_j),
ColumnTailGainTarget_309(r),
ColumnMultiplicityGainTarget_308(r),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ThresholdBudgetP0Closure_284(q,r),
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
selector transfer,
the original selected-average problem,
the all-alpha theorem,
or the unconditional finite-type theorem.
```

## 5. Proof / disproof / reduction

### A. The zero mode is not killed by the minor convention

The convention:

```text
Minor_0(R,eta) subset {xi != 0}
```

means the minor sum does not include `xi=0`. It does not imply:

```text
beta_0(d,0)=0.
```

Indeed:

```text
beta_0(d,0)=E_n f_0(n+d)conj(f_0(n)),
```

which is a two-point residual covariance of the local W-cyclic prime model.
It is not the mean of `f_0`.

Therefore:

```text
ZeroModeKilledByMinorConvention_315:
  FALSE / BLOCKED.
```

### B. Exact covariance expansion

Write:

```text
m_0=E_n nu_0(n),
P_2^0(d)=E_n nu_0(n+d)nu_0(n).
```

Since the average is cyclic:

```text
E_n nu_0(n+d)=m_0.
```

For the real prime weight in `P_minor^0`:

```text
Z_d
  =
  P_2^0(d)-2m_0+1.
```

Equivalently:

```text
Z_d
  =
  (P_2^0(d)-m_0^2)+(m_0-1)^2.
```

If a future convention or theorem proves `m_0=1+o(1)` and
`P_2^0(d)` has the required pair local model, then `Z_d` may be routed to a
pair-covariance row. This module does not supply such a theorem.

Classification:

```text
ZeroModeProductIdentity_315:
  STRUCTURAL / EXTRACTION.
```

### C. Exact product-row formula

Using `Z_d=beta_0(d,0)`:

```text
ZeroModeProductRow_314
  =
  D^(-1) sum_{d_1 != d_2}|Z_{d_1}|^2|Z_{d_2}|^2.
```

Equivalently:

```text
ZeroModeProductRow_314
  =
  D^(-1)
  [
    (sum_d |Z_d|^2)^2
    -
    sum_d |Z_d|^4
  ].
```

Thus a standalone zero-mode route would need a same-family second-moment
bound for:

```text
Z2_315
  =
  D^(-1) sum_{D<|d|<=2D}|Z_d|^2.
```

The elementary ceiling is:

```text
ZeroModeProductRow_314 <= D (Z2_315)^2,
```

up to the two-sided shell-count constant already tracked by `C_D`.

This is only a criterion. The current ledger has no estimate making
`D(Z2_315)^2` small enough after Module 310 threshold conversion and Module
284 column-barrier weights.

### D. Centered rewrite

Define:

```text
B_d^{0,circ}=B_d^0-Z_d.
```

For every nonzero frequency:

```text
widehat{B_d^{0,circ}}(xi)=beta_0(d,xi).
```

Since:

```text
Minor_0(R,eta) subset {xi != 0},
```

we have the exact identity:

```text
WPair(d_1,d_2)
  =
  sum_{xi in Minor_0(R,eta)}
    |widehat{B_{d_1}^{0,circ}}(xi)|^2
    |widehat{B_{d_2}^{0,circ}}(xi)|^2.
```

Using the centered full and major kernels:

```text
FullPair_circ_315(d_1,d_2)
  =
  sum_{xi in G_N}
    |widehat{B_{d_1}^{0,circ}}(xi)|^2
    |widehat{B_{d_2}^{0,circ}}(xi)|^2,

MajorPair_circ_315(d_1,d_2)
  =
  sum_{xi in Major_0(R,eta)}
    |beta_0(d_1,xi)|^2 |beta_0(d_2,xi)|^2,
```

the minor row becomes:

```text
WPair(d_1,d_2)
  =
  FullPair_circ_315(d_1,d_2)
  -
  MajorPair_circ_315(d_1,d_2).
```

Thus the explicit zero row can be removed by changing the full row to the
centered full row.

Classification:

```text
CenteredRewriteRemovesExplicitZeroRow_315:
  STRUCTURAL / EXTRACTION.
```

This is an exact rewrite. It is not a proof that the centered full row or the
major row is small.

### E. Why current zero-mode control is still unavailable

There are three tempting shortcuts.

First:

```text
E_n f_0(n)=0
```

would not imply `Z_d=0`; `Z_d` is a correlation of two shifted residual
weights.

Second, replacing `B_d^0` by `B_d^{0,circ}` is valid for nonzero frequencies,
but it changes the full-frequency row. It removes an explicit correction; it
does not create cancellation.

Third, pair local-model heuristics suggest that `Z_d` should be related to a
pair covariance such as `kappa_w(d)-1` plus normalization errors, but the
current `P_minor^0` column branch has not proved the needed same-family,
W-uniform, dyadic average estimate.

Therefore:

```text
CurrentZeroModeProductControl_315:
  FALSE / BLOCKED.

ZeroModeProductControl_314(P_minor^0):
  OPEN as a standalone estimate.
```

The project should not try to close the column branch by declaring the zero
row negligible. The cleaner next move is to carry the centered rewrite into
the full anti-diagonal row.

### F. Next target

Define:

```text
CenteredFullAntiDiagonalAudit_316(P_minor^0):
  audit the full-frequency anti-diagonal row after replacing B_d^0 by
  B_d^{0,circ}, and decide whether current tools give anything beyond the
  Module 311 ceilings.
```

Status:

```text
CenteredFullAntiDiagonalAudit_316(P_minor^0):
  OPEN next target.
```

This target replaces the earlier uncentered full-row audit as the sharper
next step. The major correction row remains open and will still need its own
audit.

## 6. Edge cases

If `Z_d=0` for a specific shift, that shift contributes nothing to the
zero-mode product row. A uniform row statement cannot be inferred from
shift-by-shift accidents.

If `m_0=1` exactly, the identity reduces to:

```text
Z_d=P_2^0(d)-1.
```

This is still a pair-covariance row, not an automatic zero.

If the local model later uses a centered product `B_d^{0,circ}` from the
start, the explicit zero product row is absent, but the centered full row
must be audited in its place.

If zero is placed inside the major arcs by a future convention, the full /
zero / major partition from Module 314 must be rewritten to avoid double
counting.

Nothing in this module transfers from `P_minor^0` to the actual sharp moving
selector.

## 7. Project-map location

The column branch now reads:

```text
Module 312:
  weighted pair energy expands to a minor-kernel anti-diagonal form.

Module 314:
  the minor kernel splits into full-frequency, zero-mode, and major rows.

Module 315:
  the zero row is not killed by convention and is not controlled by current
  tools, but it can be absorbed exactly by a centered full-row rewrite.
```

The selected next target is:

```text
CenteredFullAntiDiagonalAudit_316(P_minor^0).
```

## 8. What remains open

Still open:

```text
CenteredFullAntiDiagonalAudit_316(P_minor^0),
ZeroModeProductControl_314(P_minor^0),
SignedMinorKernelCombinationTarget_314(P_minor^0),
FullAntiDiagonalControl_314(P_minor^0),
MajorKernelCorrectionControl_314(P_minor^0),
AntiDiagonalTwoShiftKernelGain_312(P_minor^0),
WeightedColumnSecondMomentTarget_311(P_minor^0),
WeightedColumnPairEnergyTarget_310(P_minor^0),
OffDiagonalSameFrequencyPair_310(lambda_j),
ColumnTailGainTarget_309(r),
ColumnMultiplicityGainTarget_308(r),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ThresholdBudgetP0Closure_284(q,r),
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
MinorArcTransfer_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the original selected-average problem.
```

## 9. Forbidden upgrades

Do not cite `ZeroModeProductAudit_315(P_minor^0)` as a zero-mode estimate.

Do not claim the minor convention proves `beta_0(d,0)=0`.

Do not claim `E f_0=0`, even if proved elsewhere, kills
`E f_0(n+d)conj(f_0(n))`.

Do not cite `CenteredRewriteRemovesExplicitZeroRow_315` as cancellation. It
is an exact rewrite that changes the full row to a centered full row.

Do not cite `ZeroModeProductControl_314(P_minor^0)` or
`CenteredFullAntiDiagonalAudit_316(P_minor^0)` as proved.

Do not prove the column barriers by assuming:

```text
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
PhaseKernelBound_273^0,
selector transfer,
or the original selected-average problem.
```

Do not move this local `P_minor^0` audit to the actual sharp moving selector
without transfer rows.

## 10. Next target

The next target is:

```text
Module 316:
  CenteredFullAntiDiagonalAudit_316(P_minor^0).
```

It should audit the full-frequency anti-diagonal row with
`B_d^{0,circ}` in place of `B_d^0`, compare current estimates to the Module
311 ceilings, and decide whether this centered full row is local, open, or
already endpoint-strength.
