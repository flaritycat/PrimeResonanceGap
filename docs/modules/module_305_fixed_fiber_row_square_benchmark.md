# Module 305: Fixed-fiber row-square benchmark inside `P_minor^0`

## 1. Precise theorem / claim being advanced

This module performs the benchmark selected by Module 304.

Define:

```text
FixedFiberRowSquareBenchmark_305(P_minor^0).
```

The benchmark replaces the data-dependent large-spectrum fibers:

```text
S_{d,j}
  =
  { xi in Minor_0(R,eta):
      |beta_0(d,xi)|>=lambda_j }
```

by a prescribed family:

```text
U=(U_d)_d,
U_d subset Minor_0(R,eta),
```

chosen independently of the coefficients `beta_0(d,xi)`.

Verdict:

```text
FixedFiberRowSquareBenchmark_305(P_minor^0):
  STRUCTURAL / EXTRACTION.

FixedFiberKernelIdentity_305(U):
  STRUCTURAL / EXTRACTION.

FixedFiberParsevalCeiling_305(U):
  STRUCTURAL / EXTRACTION.

FixedFiberSizeCriterion_305(U):
  STRUCTURAL / EXTRACTION.

CurrentToolsFixedFiberGain_305:
  FALSE / BLOCKED.

FullFrequencyFixedFiberDiagnostic_305:
  FALSE / BLOCKED as a proof route.

FixedFiberRowSquareGain_305(P_minor^0):
  OPEN.
```

Thus prescribed fibers remove the selection issue, but they do not by
themselves produce the q=2 row-square gain from the current toolkit. A new
fixed-fiber same-shift estimate, or a size criterion with genuinely summable
losses, would still be needed before selection transfer becomes the next
missing input.

## 2. Status label

`STRUCTURAL / EXTRACTION`

This is a benchmark and route classification. It proves no row-square
smallness, no row-barrier smallness, no threshold closure, no minor-arc
endpoint, and no selector transfer.

## 3. Definitions and variables

Work inside the Module 278 family:

```text
P_minor^0.
```

Use:

```text
rho_0=(N,w,b,D,R,eta,Lambda_0,mu_0,K_0),
G_N=Z/NZ,
D<|d|<=2D,
N^{delta_D}<=D<=N^{1-delta_D},
2D<=N/16.
```

The residual derivative coefficients are:

```text
f_0(n)=nu_0(n)-1,
B_d^0(n)=f_0(n+d)conj(f_0(n)),
beta_0(d,xi)=widehat{B_d^0}(xi)
             = E_{n in G_N} B_d^0(n)e_N(-xi n).
```

Fix a prescribed family:

```text
U=(U_d)_d,
U_d subset Minor_0(R,eta),
```

with `U_d` chosen before the coefficients `beta_0(d,xi)` are inspected.

Define:

```text
E_d^U
  =
  sum_{xi in U_d}|beta_0(d,xi)|^2,

RowSq^U
  =
  D^(-1) sum_{D<|d|<=2D} (E_d^U)^2.
```

Also define:

```text
K_{U_d}(t)
  =
  sum_{xi in U_d} e_N(xi t),

M_U=max_{D<|d|<=2D} #U_d,

E2_U
  =
  D^(-1) sum_{D<|d|<=2D} E_d^U.
```

The full minor row energy remains:

```text
E_{d,0}^minor
  =
  sum_{xi in Minor_0(R,eta)} |beta_0(d,xi)|^2,

E2_minor^0(D;R,eta)
  =
  D^(-1) sum_{D<|d|<=2D} E_{d,0}^minor.
```

Use the Module 297 envelope:

```text
|beta_0(d,xi)| <= L_{N,w}^2,
E_{d,0}^minor <= L_{N,w}^4,
E2_minor^0(D;R,eta) <= C_D L_{N,w}^4,
```

where:

```text
L_{N,w}=1+log(WN+b),
C_D=D^(-1)# { d:D<|d|<=2D }.
```

## 4. Assumptions

This module assumes Modules 278, 281, 297, 300, 302, 303, and 304, plus the
active status ledger.

It uses only:

```text
finite cyclic Fourier normalization,
the prescribed-fiber condition for U,
Parseval/Bessel diagnostics,
the pointwise logarithmic envelope,
and the Module 297 local second-energy bound.
```

It does not assume:

```text
FixedFiberRowSquareGain_305(P_minor^0),
SameShiftSquareKernelGain_303(P_minor^0),
OffDiagonalSameShiftRow_303(lambda_j),
RowSquareMomentTarget_302,
RowTailGainTarget_302(q),
RowMomentGainTarget_300(q),
RowBarrierP0_284(q)=o_W(1),
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ThresholdBudgetP0Closure_284(q,r),
LargeSieveBesselClosure_281,
AdaptiveBesselGain_281,
PhaseKernelBound_273^0,
PhaseKernelBound_273,
DirectShellCrossTermGain_287,
SelectionTransfer_280,
UniformFiberBound_280,
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

### A. Exact fixed-fiber identity

By definition:

```text
RowSq^U
  =
  D^(-1) sum_d
    sum_{xi_1,xi_2 in U_d}
      |beta_0(d,xi_1)|^2 |beta_0(d,xi_2)|^2.
```

Expanding the coefficients as in Module 303 gives:

```text
RowSq^U
  =
  D^(-1) sum_d
  E_{n_1,m_1,n_2,m_2}
    B_d^0(n_1)conj(B_d^0(m_1))
    B_d^0(n_2)conj(B_d^0(m_2))
    K_{U_d}(m_1-n_1)
    K_{U_d}(m_2-n_2).
```

This is the same-shift row-square kernel with `K_{d,j}` replaced by the
prescribed kernel `K_{U_d}`.

Classification:

```text
FixedFiberKernelIdentity_305(U):
  STRUCTURAL / EXTRACTION.
```

The identity removes the data-dependent selection issue. It does not estimate
the same-shift residual kernel.

### B. Parseval ceiling

Since:

```text
U_d subset Minor_0(R,eta),
```

one has:

```text
0 <= E_d^U <= E_{d,0}^minor <= L_{N,w}^4.
```

Therefore:

```text
(E_d^U)^2 <= L_{N,w}^4 E_d^U.
```

Averaging over the dyadic shift shell:

```text
RowSq^U
  <=
  L_{N,w}^4 E2_U
  <=
  L_{N,w}^4 E2_minor^0(D;R,eta)
  <=
  C_D L_{N,w}^8.
```

Thus:

```text
(RowSq^U)^(1/2)
  <=
  C_D^(1/2)L_{N,w}^4.
```

Inserted into the q=2 row-barrier shape:

```text
sum_j lambda_j^2 (L_j C_D)^(1/2) (RowSq^U)^(1/2),
```

this gives the same polylogarithmic ceiling scale as Modules 300 and 302,
after the standard lambda-grid summation.

Classification:

```text
FixedFiberParsevalCeiling_305(U):
  STRUCTURAL / EXTRACTION.
```

It is a valid ceiling, not `o_W(1)` row-barrier smallness.

### C. Size-sensitive criterion

The prescribed family has an additional size parameter:

```text
M_U=max_d #U_d.
```

The pointwise envelope gives:

```text
E_d^U
  <=
  M_U (A_N^0)^2
  <=
  M_U L_{N,w}^4.
```

Hence:

```text
RowSq^U
  <=
  M_U (A_N^0)^2 E2_U
  <=
  M_U L_{N,w}^4 E2_minor^0(D;R,eta)
  <=
  M_U C_D L_{N,w}^8.
```

This improves the Parseval ceiling only if `M_U` is better than the trivial
row envelope in the relevant regime. It still does not imply:

```text
sum_j lambda_j^2 (L_j C_D)^(1/2)(RowSq^U)^(1/2)=o_W(1)
```

unless the allowed fiber sizes and lambda losses are strong enough after the
full row-barrier summation.

So Module 305 extracts only the conditional size test:

```text
FixedFiberSizeCriterion_305(U):
  find size and energy hypotheses on U such that

  sum_j lambda_j^2 (L_j C_D)^(1/2)
    [D^(-1)sum_d(E_d^U)^2]^(1/2)
  =
  o_W(1).
```

Classification:

```text
FixedFiberSizeCriterion_305(U):
  STRUCTURAL / EXTRACTION.
```

The criterion is not currently verified for any family that can replace
`S_{d,j}`.

### D. Full-frequency diagnostic

If:

```text
U_d=G_N
```

then cyclic Parseval gives:

```text
E_d^U
  =
  E_{n in G_N}|B_d^0(n)|^2.
```

Consequently:

```text
RowSq^U
  =
  D^(-1)sum_d
    (E_n |B_d^0(n)|^2)^2.
```

This is a same-shift fourth moment of the derivative products. The current
ledger has no estimate making this lambda-summed row-barrier-small. It is
also not the restricted minor-arc fixed-fiber problem, since it uses the full
frequency group.

Classification:

```text
FullFrequencyFixedFiberDiagnostic_305:
  FALSE / BLOCKED as a proof route.
```

It is useful for checking normalization only.

### E. Large-sieve/Bessel benchmark

Module 281 already records that available non-endpoint large-sieve/Bessel
tools produce row/column ceilings or fixed-set diagnostics for the shell
functional. In the present positive q=2 row-square object, a Bessel step gives
at most:

```text
E_d^U <= E_{d,0}^minor,
```

and hence the Parseval ceiling above.

A linear fixed-set large-sieve estimate for:

```text
sum_d sum_{xi in U_d} omega_{d,xi} beta_0(d,xi)
```

does not by itself estimate:

```text
D^(-1)sum_d (sum_{xi in U_d}|beta_0(d,xi)|^2)^2
```

with the needed lambda-summed saving. The row-square object is positive and
same-shift; it needs a quadratic row-energy estimate, not merely a linear
dual estimate with favorable cancellation.

Thus:

```text
CurrentToolsFixedFiberGain_305:
  FALSE / BLOCKED.
```

This is not a statement that all fixed-fiber theorems are impossible. It says
only that the currently recorded tools do not provide the needed q=2 gain.

### F. What a genuine fixed-fiber theorem would need

Define the open target:

```text
FixedFiberRowSquareGain_305(P_minor^0):
  for prescribed fibers U_d subset Minor_0(R,eta),
  independent of beta_0,
  prove a same-family bound

    D^(-1)sum_d (E_d^U)^2 <= V(U;rho_0)^2

  such that the lambda-summed row-barrier expression with V(U;rho_0)
  is o_W(1), with losses compatible with the fixed N->infinity then
  w->infinity order.
```

Status:

```text
FixedFiberRowSquareGain_305(P_minor^0):
  OPEN.
```

If such a theorem is later supplied, the next obstruction would be a
selection-transfer theorem from prescribed fibers `U_d` to the actual
large-spectrum fibers `S_{d,j}`. Since no such fixed-fiber gain is currently
available, selection transfer is not yet the first missing input.

## 6. Edge cases

If:

```text
U_d=emptyset
```

for every shift, then `RowSq^U=0`. This is vacuous and says nothing about
nonempty fibers or `S_{d,j}`.

If `U_d` is allowed to depend on `beta_0`, this benchmark no longer applies.
The object has returned to the data-dependent Module 303 setting.

If `U_d=G_N`, full-frequency orthogonality can be used for diagnostics, but
the resulting object is not a restricted minor-arc row-square estimate.

If `M_U` is small for one fixed row family, the gain must still survive the
lambda-summed barrier weights. A pointwise or single-family smallness claim is
not enough.

Nothing here transfers from `P_minor^0` to the actual sharp moving selector.

## 7. Project-map location

The q=2 row branch now reads:

```text
Module 303:
  data-dependent row-square kernel extracted.

Module 304:
  selected fixed-fiber benchmark before selection transfer.

Module 305:
  fixed-fiber benchmark returns only ceilings from current tools;
  fixed-fiber row-square gain remains open.
```

Therefore the immediate branch should not proceed to selection transfer as if
a fixed-fiber theorem were available.

The local map is:

```text
FixedFiberRowSquareGain_305
  + SelectionTransferForRowSquare
  => SameShiftSquareKernelGain_303
  => RowSquareMomentTarget_302
  => possible RowBarrierP0_284(2)=o_W(1).
```

Every nonstructural input in this chain remains open.

## 8. What remains open

Still open:

```text
FixedFiberRowSquareGain_305(P_minor^0),
FixedFiberRowSquareBenchmark_305 as a source of gain,
SameShiftSquareKernelGain_303(P_minor^0),
OffDiagonalSameShiftRow_303(lambda_j),
RowSquareMomentTarget_302,
RowTailGainTarget_302(q),
RowMomentGainTarget_300(q),
RowBarrierP0_284(q)=o_W(1),
ThresholdWindowClosure_299(q,r),
BarrierSmallnessPackage_299(q,r),
ColumnBarrierP0_284(r)=o_W(1),
SigmaColumnBarrierP0_284(r)=o_W(1),
ThresholdBudgetP0Closure_284(q,r),
SideRowsP0Ready_283,
SidePkg_291,
SidePkgReady_293,
AdaptiveShellGainP0_285,
PhaseKernelBound_273^0,
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
the original selected-average problem.
```

## 9. Forbidden upgrades

Do not cite `FixedFiberKernelIdentity_305(U)` as a bound.

Do not cite `FixedFiberParsevalCeiling_305(U)` as row-barrier smallness.

Do not treat a fixed-fiber benchmark as a data-dependent large-spectrum
estimate for `S_{d,j}`.

Do not proceed to selection transfer as though `FixedFiberRowSquareGain_305`
were proved.

Do not prove the fixed-fiber or data-dependent row-square target by assuming:

```text
NarrowMinorArc_3^B,
ResCube_3^sharp,
CPC_3^sharp,
RBDH_pair_short,
AU^3,
PhaseKernelBound_273^0,
selector transfer,
or the original selected-average problem.
```

Do not move this local fixed-fiber benchmark to the actual sharp moving
selector without transfer rows.

## 10. Next target

The next target should record the blocked consequence before the scheduled
plan challenge:

```text
Module 306:
  FixedFiberBlockedVerdict_306(P_minor^0).
```

That module should decide whether to pause the row-square branch until a new
same-shift theorem appears, or whether a smaller size-sensitive fixed-fiber
criterion is worth isolating before `PlanChallenge_8_307`.
