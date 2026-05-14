# Module 190: Kernel absolute-mass and range audit for major projection

## 1. Precise theorem / claim being advanced

This module audits the kernel and range hypotheses used in Modules 183-189.
It records that the major-arc collision package needs more than formal
projected local factors. It needs:

```text
absolute kernel mass control
  + kernel-tail truncation control
  + finite-range congruence control for large CRT moduli.
```

The main conditional claim is:

if the major-arc projection kernel satisfies an absolute-mass/tail package and
the active pair-difference forms satisfy a finite-range CRT package, then the
joint union-divisibility criterion from Module 189 holds with a summable
error term.

This module is deliberately an audit. It does not prove that the actual sharp
major-arc projection has the required absolute-mass behavior. In particular,
the bound:

```text
E_t |W_M(t)| = O(1)
```

must not be treated as automatic.

## 2. Status label

`CONDITIONAL`

The reduction from kernel/range hypotheses to the Module 189 criterion is
conditional. The actual verification of those hypotheses for the chosen
major-arc projection remains open.

## 3. Definitions and variables

Let `P_M` be the nonzero major-arc Fourier projection with multiplier `m_M`.
Let its inverse kernel be:

```text
P_M F(x)=E_t K_M(t) F(x-t).
```

Define the one-kernel absolute mass:

```text
A_1(M)=E_t |K_M(t)|.
```

For the four projected cube slots:

```text
W_M(t0,t1,t2,t3)
  = K_M(t0) conj(K_M(t1)) conj(K_M(t2)) K_M(t3),
```

and:

```text
A_W(M)=E_{t0,t1,t2,t3} |W_M(t0,t1,t2,t3)|.
```

When the four `t` variables are averaged independently with the same
normalization:

```text
A_W(M)=A_1(M)^4.
```

For a truncation parameter `T`, define:

```text
tau_M(T)=E_{|t|>T} |K_M(t)|.
```

The four-fold tail is bounded by:

```text
Tail_W(T) <= 4 A_1(M)^3 tau_M(T)
```

up to harmless normalization conventions.

Let the active nonstructural pair-difference forms be:

```text
L_1(d,h,k;t), ..., L_J(d,h,k;t),
J <= 28.
```

On the truncated kernel range `|t_i|<=T`, with:

```text
D<|d|<=2D,
h in I_H, |I_H|=H,
k in I_K, |I_K|=K,
```

set a deterministic magnitude envelope:

```text
B_*(N,T) = C_*(D+H+K+T+1)
```

so that, away from structural and boundary regions:

```text
0 < |L_j(d,h,k;t)| <= B_*(N,T).
```

For a finite prime set `P`, define:

```text
Q(P)=prod_{p in P} p.
```

For Module 189:

```text
X_p(d,h,k;t)=1_{exists j with p|L_j(d,h,k;t)}.
```

## 4. Assumptions

Assume the following kernel-range package.

Kernel absolute mass:

```text
A_W(M)=O(1)
```

or, more generally, all later savings are strong enough after multiplying by
`A_W(M)`.

Kernel tail:

for some truncation `T=T(N,M)`,

```text
Tail_W(T)=o(1)
```

in the project limit order, and, for each fixed `lambda` needed later,

```text
Tail_exp(lambda,T)
  = Tail_W(T)
    prod_{w<p<=B_*(N,T)}
      (1 + J (exp(lambda J/p)-1))
  = o(1).
```

Equivalently, one may prove the direct weighted tail bound:

```text
E_abs exp(lambda B_w) 1_{max_i |t_i|>T}=o(1).
```

Magnitude envelope:

on `|t_i|<=T`, every active nonzero form satisfies:

```text
0<|L_j|<=B_*(N,T).
```

Finite-range CRT package:

for every finite prime set `P` and every assignment

```text
phi:P -> {1,...,J},
```

the simultaneous congruence event

```text
p | L_{phi(p)}(d,h,k;t) for every p in P
```

satisfies, uniformly for truncated `t`,

```text
E_{d,h,k} prod_{p in P} 1_{p|L_{phi(p)}}
  <= C_CRT / Q(P) + RangeErr(P,phi;N,T).
```

The range errors must satisfy the exponential summability condition:

```text
Err_range(lambda)
  = A_W(M)
    sum_{P finite, p in (w,B_*(N,T)]}
      prod_{p in P} (exp(lambda J/p)-1)
      sum_{phi:P->{1,...,J}} RangeErr(P,phi;N,T)
  = o(1).
```

Structural zero strata and boundary regions are removed before these estimates
are applied.

## 5. Proof / disproof / reduction

On the truncated kernel range, expand:

```text
prod_{p in P} X_p
  <= sum_{phi:P->{1,...,J}}
      prod_{p in P} 1_{p|L_{phi(p)}}.
```

Multiplying by `|W_M(t)|`, averaging in `t`, and using the finite-range CRT
package gives:

```text
E_abs prod_{p in P} X_p
  <= A_W(M) J^{|P|} C_CRT / Q(P)
     + Err_range(P)
     + Tail_W(T),
```

where:

```text
Err_range(P)
  = E_{|t_i|<=T} |W_M(t)|
      sum_phi RangeErr(P,phi;N,T).
```

Since:

```text
Q(P)=prod_{p in P} p,
```

the main term has the Module 189 shape:

```text
C_0 prod_{p in P} (K_0/p)
```

with, for example:

```text
C_0 = C_CRT A_W(M),
K_0 = J,
```

provided `A_W(M)=O(1)`.

The exponential-expansion error in Module 189 is controlled by
`Err_range(lambda)` plus the summable kernel-tail contribution
`Tail_exp(lambda,T)`. Module 191 records the W-limit uniformity needed for the
generic `p^{-2}` product tails. Thus, under the assumptions in Section 4:

```text
E_abs prod_{p in P} X_p
  <= C_0 prod_{p in P} (K_0/p) + Err(P)
```

with summable `Err(P)`. Module 189 then gives:

```text
E_abs exp(lambda B_w)=O(1)
```

for fixed `lambda`, including `lambda=C+epsilon` from Module 188.

### Why this audit is necessary

For a single congruence over an interval of length `L`, one often has:

```text
E 1_{q|L(x)} <= 1/q + O(1/L).
```

In an exponential expansion, the `O(1/L)` terms are multiplied by many possible
prime sets and form assignments. A crude bound can produce an error of the
shape:

```text
A_W(M) L^{-1}
  prod_{w<p<=B_*(N,T)}
    (1 + J (exp(lambda J/p)-1)).
```

This is roughly a power of:

```text
log B_*(N,T) / log w
```

divided by `L`, not merely `1/L`. Therefore range losses must be tracked in
the same expansion that proves exponential integrability.

## 6. Edge cases

- Sharp major-arc cutoffs can have large physical-space `L^1` kernels. A
  smoothed projection may be needed, but smoothing changes the model and must
  be recorded.
- Kernel cancellation is unavailable after passing to `|W_M|`.
- If `A_W(M)` grows, every structural-stratum and divisor-counting saving must
  beat that growth.
- If `T` is too small, the kernel tail is not negligible in the exponential
  expansion. If `T` is too large, the magnitude envelope `B_*(N,T)` grows and
  worsens the prime expansion.
- If `Q(P)` is larger than the effective averaging range, the main term
  `1/Q(P)` may be dominated by range errors.
- Pure `d` forms require the dyadic `d` average to be part of the CRT package.
- Horizontal, vertical, and diagonal forms can become dependent for some
  assignments `phi`; those dependencies must either be harmless modulo `Q(P)`
  or included in structural/boundary errors.
- The audit is performed for the projected model side. Transferring it to the
  actual sharp moving selector requires separate transfer hypotheses.

## 7. Where it fits in the project map

Modules 187-189 created the following conditional chain:

```text
local factor envelope
  -> overflow criterion
  -> exponential moment
  -> joint union-divisibility estimates.
```

Module 190 audits the analytic infrastructure under that chain:

```text
major-arc kernel K_M
  -> absolute mass and tail
  -> finite range for projected pair differences
  -> CRT errors over many primes
  -> Module 189 criterion.
```

This module therefore sits between the formal collision-load reductions and
any attempted proof of the actual major-arc collision package.
Module 191 is the next bookkeeping layer: it identifies which tails are
genuinely generic W-tails and which remain arithmetic range errors.

## 8. What remains open

This module does not prove:

- bounded absolute mass for the actual major-arc projection kernel;
- a tail truncation compatible with the required local model;
- exponential summability of the kernel-tail contribution;
- the finite-range CRT package for all projected pair-difference assignments;
- summability of range errors in the Module 189 exponential expansion;
- the W-admissibility checks isolated in Module 191;
- projected local-model matching;
- minor-arc large-spectrum decay;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem or the all-alpha theorem.

## Red flags / forbidden upgrades

- Do not assume `E_t |W_M(t)|=O(1)` without proving it for the chosen
  projection.
- Do not hide range errors from large CRT moduli in a generic boundary term.
- Do not use cancellation from `W_M` after the absolute value has been taken.
- Do not switch from a sharp projection to a smoothed projection without
  updating the projected local model.
- Do not treat this kernel/range audit as projected local-model matching.
- Do not transfer this model estimate to actual sharp moving selectors without
  the full transfer package.
