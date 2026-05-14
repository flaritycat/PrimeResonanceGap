# Module 189: Exponential-moment criterion for beta-load sums

## 1. Precise theorem / claim being advanced

This module gives a sufficient criterion for the uniform exponential
integrability required in Module 188. It replaces the vague request:

```text
E_abs exp(lambda B_w) = O(1)
```

by a concrete joint divisor target for the projected pair-difference forms.

Let:

```text
B_w(d,h,k;t) = sum_{j=1}^J beta_w(L_j(d,h,k;t)),
beta_w(m) = sum_{p>w, p|m} 1/p.
```

After structural zero strata and boundary regions are removed, define:

```text
X_p(d,h,k;t) = 1_{exists j with p | L_j(d,h,k;t)}.
```

Since at most `J` forms can be divisible by one prime:

```text
B_w <= J sum_{w<p<=B_*(N)} X_p/p.
```

The criterion is:

if the weighted joint union-divisibility estimate

```text
E_abs prod_{p in P} X_p
  <= C_0 prod_{p in P} (K_0/p) + Err(P)
```

holds for every finite set `P` of primes `p>w`, with the weighted error
summable in the exponential expansion, then for every fixed `lambda>0`:

```text
E_abs exp(lambda B_w) = O_{lambda,J,K_0,C_0}(1).
```

In fact, after the project limit order and if the expansion error vanishes:

```text
E_abs exp(lambda B_w)
  <= C_0 exp(O_{lambda,J,K_0}(sum_{p>w} 1/p^2)) + o(1).
```

This supplies the exact type of input needed by Module 188 with
`lambda=C+epsilon`.

## 2. Status label

`CONDITIONAL`

The exponential-moment bound is proved conditionally from the stated joint
divisor criterion. This module does not prove that the actual projected
major-arc kernel satisfies that criterion.

## 3. Definitions and variables

Let the active nonstructural pair-difference forms be:

```text
L_1, ..., L_J,
J <= 28.
```

They are functions of:

```text
(d,h,k;t0,t1,t2,t3).
```

Let:

```text
E_abs F
  = (1/D) sum_{D<|d|<=2D} E_{h,k} E_t |W_M(t)| F(d,h,k;t),
```

where:

```text
W_M(t)=K_M(t0) conj(K_M(t1)) conj(K_M(t2)) K_M(t3).
```

Assume:

```text
A_M = E_abs 1 = O(1).
```

Let `B_*(N)` be a finite magnitude envelope such that, away from removed
regions,

```text
0 < |L_j(d,h,k;t)| <= B_*(N).
```

Then primes `p>B_*(N)` do not divide active nonzero `L_j`, and:

```text
B_w = sum_{j=1}^J sum_{w<p<=B_*(N), p|L_j} 1/p.
```

For each prime `p>w`, set:

```text
C_p = sum_{j=1}^J 1_{p|L_j},
X_p = 1_{C_p>0}.
```

Thus:

```text
C_p <= J X_p,
B_w = sum_{w<p<=B_*(N)} C_p/p
    <= J sum_{w<p<=B_*(N)} X_p/p.
```

## 4. Assumptions

Assume:

- structural zero strata `L_j=0` have been removed or bounded separately;
- boundary regions where `|L_j|` lacks the envelope `B_*(N)` are included in a
  separate error;
- the kernel absolute mass satisfies `A_M=O(1)`;
- for every finite set `P` of primes `p>w`, the joint union-divisibility bound
  holds:

```text
E_abs prod_{p in P} X_p
  <= C_0 prod_{p in P} (K_0/p) + Err(P);
```

- for the chosen fixed `lambda`, the exponential-expansion error is summable:

```text
Err_exp(lambda)
  = sum_{P finite}
      prod_{p in P} (exp(lambda J/p)-1) Err(P)
  = o(1)
```

in the project limit order.

The constants `C_0,K_0` may depend on the finite cube complexity and on fixed
kernel-shape parameters, but not on `N,D,h,k,w`, or the finite prime set `P`.
Module 190 audits the kernel absolute-mass and finite-range hypotheses needed
to verify this assumption for a concrete major-arc projection.

## 5. Proof / disproof / reduction

Since:

```text
B_w <= J sum_p X_p/p,
```

we have:

```text
exp(lambda B_w)
  <= prod_{w<p<=B_*(N)} exp(lambda J X_p/p).
```

Because `X_p` is an indicator:

```text
exp(lambda J X_p/p)
  = 1 + a_p X_p,
a_p = exp(lambda J/p)-1.
```

Therefore:

```text
exp(lambda B_w)
  <= prod_{w<p<=B_*(N)} (1+a_p X_p).
```

Expanding the finite product gives:

```text
E_abs exp(lambda B_w)
  <= sum_{P subset {w<p<=B_*(N)}}
      prod_{p in P} a_p
      E_abs prod_{p in P} X_p.
```

Insert the joint union-divisibility estimate:

```text
E_abs exp(lambda B_w)
  <= C_0 sum_P prod_{p in P} (a_p K_0/p)
     + Err_exp(lambda).
```

The main term factors:

```text
sum_P prod_{p in P} (a_p K_0/p)
  = prod_{w<p<=B_*(N)} (1 + a_p K_0/p).
```

For `w` large relative to `lambda J`:

```text
a_p = exp(lambda J/p)-1 <= C_{lambda,J}/p.
```

Thus:

```text
sum_p a_p K_0/p
  <= C_{lambda,J,K_0} sum_{p>w} 1/p^2
  = o_w(1),
```

and:

```text
prod_{w<p<=B_*(N)} (1 + a_p K_0/p)
  <= exp(C_{lambda,J,K_0} sum_{p>w} 1/p^2)
  = O(1).
```

If `Err_exp(lambda)=o(1)`, this proves:

```text
E_abs exp(lambda B_w) = O(1).
```

Taking:

```text
lambda = C + epsilon
```

matches the uniform exponential-integrability hypothesis in Module 188.

## 6. Edge cases

- Individual estimates `E_abs X_p <= O(1/p)` are not enough unless their joint
  versions are also controlled. Exponential moments expand over many primes.
- If the same pair-difference form is responsible for many primes, the
  criterion still allows it, but the CRT/divisibility count must handle
  products of primes rather than only one prime at a time.
- If a form is structurally zero on a stratum, then `X_p=1` for every `p` on
  that stratum and the product estimate fails. This is why Modules 184-185 are
  logically prior.
- If `prod_{p in P} p` exceeds the effective averaging volume, naive
  equidistribution can fail; the excess must be included in `Err(P)`.
- Absolute kernel weights are essential. Cancellation in `W_M` cannot be used
  inside `E_abs`.
- The finite magnitude envelope `B_*(N)` must be stated before expanding the
  product. Otherwise the prime product has no finite truncation at fixed `N`.
- The criterion is insensitive to the precise value `J<=28`, but every
  constant worsens with `J`.

## 7. Where it fits in the project map

Module 188 showed that overflow control follows from uniform exponential
integrability of `B_w`. Module 189 turns that integrability into a precise
arithmetic target:

```text
projected pair-difference forms
  -> union divisibility indicators X_p
  -> joint product estimates over finite prime sets
  -> exponential moment for B_w
  -> overflow hypothesis of Module 188.
```

This is still a major-arc collision-control package, not projected local-model
matching and not a minor-arc estimate.
Module 190 is the next infrastructure check: it asks whether the absolute
kernel and CRT range errors are strong enough to support the displayed joint
criterion.

## 8. What remains open

This module does not prove:

- the Module 190 kernel/range package needed for the joint
  union-divisibility estimate for the actual projected kernel;
- summability of `Err_exp(lambda)` in the true parameter ranges;
- kernel absolute-mass bounds for the major-arc projection;
- structural and boundary negligibility in the sharp interval model;
- projected local-model matching;
- minor-arc large-spectrum decay;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- the original positive existence problem or the all-alpha theorem.

## Red flags / forbidden upgrades

- Do not replace the joint product estimate by separate first-moment bounds.
- Do not use kernel cancellation after passing to `|W_M|`.
- Do not hide large-modulus or short-range losses in `O(1)` constants.
- Do not apply the criterion on structural zero strata.
- Do not treat exponential integrability of the collision load as projected
  local-model matching.
- Do not transfer this model estimate to actual sharp moving selectors without
  the full transfer package.
