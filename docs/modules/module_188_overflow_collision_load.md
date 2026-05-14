# Module 188: Overflow estimate for large collision load

## 1. Precise theorem / claim being advanced

This module isolates the exact extra estimate needed after Module 187. The
local-factor collision envelope has the form:

```text
|Delta_w^{coll}| <= C exp(C B_w) B_w + tail_w.
```

The earlier linear envelope is available only if the large-load contribution

```text
Ov_w(C)
  = (1/D) sum_{D<|d|<=2D}
      E_{h,k} E_t |W_M(t)|
        exp(C B_w(d,h,k;t)) B_w(d,h,k;t)
        1_{B_w(d,h,k;t)>1}
```

is `o(1)` in the project limit order.

The claim advanced here is a conditional reduction:

```text
small first moment of B_w
  + uniform exponential integrability beyond C
  => Ov_w(C)=o(1).
```

Equivalently, with a deterministic cap on `B_w`, a sufficiently strong
high-moment estimate also implies `Ov_w(C)=o(1)`.

This module does not prove the required exponential integrability. It records
the exact missing target and explains why Module 186's first-moment divisor
averages are not enough by themselves.

## 2. Status label

`CONDITIONAL`

The reduction is analytic and conditional on weighted uniform integrability or
on a high-moment divisor package. It does not prove the major-arc theorem, the
residual cube endpoint, or any sharp moving-selector statement.

## 3. Definitions and variables

Let the active projected pair-difference forms after structural-stratum removal
be:

```text
L_1(d,h,k;t), ..., L_J(d,h,k;t),
```

where `J <= 28`. Define:

```text
beta_w(m) = sum_{p>w, p|m} 1/p
```

for `m != 0`, and:

```text
B_w(d,h,k;t) = sum_{j=1}^J beta_w(L_j(d,h,k;t)).
```

The absolute major-arc projection weight is:

```text
W_M(t)=K_M(t0) conj(K_M(t1)) conj(K_M(t2)) K_M(t3).
```

For an integrable quantity `F`, write:

```text
E_abs F
  = (1/D) sum_{D<|d|<=2D} E_{h,k} E_t |W_M(t)| F(d,h,k;t).
```

Let:

```text
A_M = E_abs 1.
```

The first moment and overflow functional are:

```text
M_1(w) = E_abs B_w,
Ov_w(C) = E_abs exp(C B_w) B_w 1_{B_w>1}.
```

When a finite magnitude envelope is available, write:

```text
0 < |L_j(d,h,k;t)| <= B_*(N)
```

off boundary and structural errors, and:

```text
R_w(N)
  = J sup_{0<|m|<=B_*(N)} beta_w(m).
```

A crude deterministic cap is:

```text
R_w(N)
  <= J min(
       sum_{w<p<=B_*(N)} 1/p,
       (log B_*(N))/(w log w)
     )
```

up to harmless endpoint conventions for small `w`.

## 4. Assumptions

Assume:

- all structural zero strata `L_j=0` have been removed or placed in a separate
  error term;
- the weighted absolute mass satisfies:

```text
A_M = O(1);
```

- the first collision-load moment satisfies:

```text
M_1(w)=o(1);
```

- one of the following two strengthening hypotheses holds.

Uniform exponential integrability:

there exists `epsilon>0` such that:

```text
E_abs exp((C+epsilon) B_w) = O(1).
```

High-moment with cap:

there is an integer `q>=1` and a deterministic cap `B_w <= R_w(N)` such that:

```text
exp(C R_w(N)) E_abs B_w^q = o(1).
```

The high-moment version is useful only when the cap and the moment estimate are
tracked in the same limit order.

## 5. Proof / disproof / reduction

### Exponential-integrability route

Choose `r>1` so close to `1` that:

```text
r C < C + epsilon.
```

For a constant depending only on `r,C,epsilon`:

```text
(exp(C x) x)^r <= C_{r,C,epsilon} exp((C+epsilon)x)
```

for all `x>=0`. Hence:

```text
E_abs (exp(C B_w) B_w)^r = O(1).
```

Let:

```text
mu_abs(E)=E_abs 1_E.
```

By Markov:

```text
mu_abs(B_w>1) <= E_abs B_w = M_1(w)=o(1).
```

Holder gives:

```text
Ov_w(C)
  <= (E_abs (exp(C B_w) B_w)^r)^{1/r}
     mu_abs(B_w>1)^{1-1/r}
  = o(1).
```

Thus a small first moment plus uniform exponential integrability beyond the
Euler-product constant `C` controls the overflow.

### High-moment route

If `B_w <= R_w(N)` and `q>=1`, then on `B_w>1`:

```text
exp(C B_w) B_w <= exp(C R_w(N)) B_w^q.
```

Therefore:

```text
Ov_w(C)
  <= exp(C R_w(N)) E_abs B_w^q.
```

The displayed high-moment condition gives `Ov_w(C)=o(1)`.

### Divisor-moment expansion

The high moments expand into weighted joint divisibility sums:

```text
E_abs B_w^q
  = sum_{j_1,...,j_q}
    sum_{p_1,...,p_q>w}
      (1/(p_1...p_q))
      E_abs prod_{a=1}^q 1_{p_a | L_{j_a}}.
```

This is the exact arithmetic target behind the overflow estimate. Module 189
packages it as a joint union-divisibility criterion for exponential moments.
Any claimed overflow proof must control these joint congruence probabilities
with the actual projected kernel weights and with structural strata removed.

## 6. Edge cases

- First-moment control `M_1(w)=o(1)` alone only gives
  `mu_abs(B_w>1)=o(1)`. It does not control the size of
  `exp(C B_w) B_w` on that rare set.
- If `R_w(N)` grows too quickly, the capped high-moment route may require
  moments of order or strength not supplied by finite congruence counting.
- If the kernel absolute mass grows with `N`, the Markov and Holder bounds
  inherit that growth.
- Repeated primes in the divisor-moment expansion are not a problem by
  themselves, but repeated or dependent forms can create structural
  congruence clusters that must be removed first.
- Pure `d` pair-difference forms require averaging over the dyadic `d` block;
  they cannot be handled only by `h,k` interval equidistribution.
- Boundary regions where `|L_j|` is not bounded below must be separated before
  applying `beta_w`.
- The constant `C` comes from the local Euler-product envelope. Changing the
  local model changes the integrability threshold.

## 7. Where it fits in the project map

Modules 183 and 186 gave first-moment divisor control for the linear collision
template. Module 187 corrected the local-factor envelope to an exponential
collision-load bound. Module 188 supplies the missing bridge:

```text
first-moment divisor averages
  -> small measure of B_w>1
  -> need uniform integrability or high moments
  -> overflow estimate
  -> licensed return to the linear envelope.
```

This keeps the major-arc branch conditional but better specified. Module 189
gives a sufficient joint-divisibility criterion for the required exponential
integrability.

## 8. What remains open

This module does not prove:

- verification of the Module 189 joint-divisibility criterion for `B_w`;
- the high-moment divisor estimates needed when `R_w(N)` grows;
- kernel absolute-mass bounds for the actual major-arc projection;
- negligibility of all structural and boundary regions;
- projected local-model matching;
- minor-arc large-spectrum decay;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem or the all-alpha theorem.

## Red flags / forbidden upgrades

- Do not replace the overflow estimate by first-moment divisor control alone.
- Do not ignore the exponential constant inherited from the local factors.
- Do not use the capped high-moment route without tracking `R_w(N)`.
- Do not apply the divisor-moment expansion before structural zero strata are
  removed.
- Do not treat this conditional overflow criterion as projected local-model
  matching.
- Do not transfer this model estimate to actual sharp moving selectors without
  the full transfer package.
