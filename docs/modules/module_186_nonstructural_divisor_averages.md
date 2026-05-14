# Module 186: Nonstructural divisor averages for projected pair-difference forms

## 1. Precise theorem / claim being advanced

This module supplies the elementary counting estimate needed after Modules
184-185 remove the structural zero strata. It treats the nonstructural
divisor averages:

```text
E beta_w(L(d,h,k;t)),
beta_w(m)=sum_{p>w, p|m} 1/p,
```

for active projected pair-difference forms `L` that have at least one `h` or
`k` coefficient equal to `+/-1`.

The claim is conditional on a finite magnitude envelope for `L`, a bounded
kernel absolute mass, and removal of the structural zero set. Under those
hypotheses:

```text
E beta_w(L)
  <= O(sum_{p>w} 1/p^2)
     + O((log log B(N))/H_L)
     + boundary_error,
```

where `B(N)` bounds `|L|` and `H_L` is the effective averaging length in a
variable on which `L` has coefficient `+/-1`.

Thus the nonstructural divisor averages are small if:

```text
w -> infinity
```

and:

```text
(log log B(N))/H_L -> 0
```

in the relevant limit order.

## 2. Status label

`CONDITIONAL`

The congruence counting estimate is elementary under the stated range and
kernel hypotheses. It does not prove the endpoint or the projected local-model
matching theorem.

## 3. Definitions and variables

Let:

```text
L(d,h,k;t)
  = alpha h + beta k + gamma d - tau(t),
```

where:

```text
alpha,beta,gamma in {-1,0,1},
```

and at least one of `alpha,beta` is nonzero. This excludes the pure same-slot
form `+/-d`, already handled in Module 184.

Let:

```text
h in I_H, |I_H|=H,
k in I_K, |I_K|=K.
```

Let `B(N)` be a deterministic envelope such that outside boundary errors:

```text
0 < |L(d,h,k;t)| <= B(N).
```

Let:

```text
H_L =
  H              if alpha != 0 and beta = 0,
  K              if alpha = 0 and beta != 0,
  min(H,K)       if alpha != 0 and beta != 0.
```

## 4. Assumptions

Assume:

- the structural zero stratum `L=0` has been removed or bounded separately;
- `|L| <= B(N)` on the remaining range;
- the kernel weight has bounded absolute mass:

```text
A_M = E_t |W_M(t)| <= C_M;
```

- interval boundary errors are recorded explicitly;
- `H_L -> infinity` fast enough that:

```text
(log log B(N))/H_L = o(1).
```

## 5. Proof / disproof / reduction

For a prime `p`, if `alpha != 0` and `beta=0`, then for fixed `d,k,t`:

```text
L = +/- h + constant.
```

In an interval of length `H`:

```text
E_h 1_{p|L} <= 1/p + O(1/H).
```

If `alpha=0` and `beta != 0`, the same argument gives:

```text
E_k 1_{p|L} <= 1/p + O(1/K).
```

If both `alpha` and `beta` are nonzero, then for each fixed `h` there is one
residue class of `k mod p`, and for each fixed `k` there is one residue class
of `h mod p`. Hence:

```text
E_{h,k} 1_{p|L} <= 1/p + O(1/min(H,K)).
```

All three cases are summarized as:

```text
E_{h,k} 1_{p|L} <= 1/p + O(1/H_L) + boundary_error_p.
```

Since `|L| <= B(N)`, only primes `p <= B(N)` can divide a nonzero `L`.
Therefore:

```text
E beta_w(L)
  = sum_{w<p<=B(N)} (1/p) E 1_{p|L}
```

and hence:

```text
E beta_w(L)
  <= sum_{p>w} 1/p^2
     + O((1/H_L) sum_{w<p<=B(N)} 1/p)
     + boundary_error.
```

Using:

```text
sum_{p>w} 1/p^2 = o_w(1),
sum_{p<=B(N)} 1/p = O(log log B(N)),
```

we obtain:

```text
E beta_w(L)
  <= o_w(1)
     + O((log log B(N))/H_L)
     + boundary_error.
```

After multiplying by `|W_M(t)|` and averaging in `t`, the same bound acquires
the factor `A_M`. Under the assumptions in Section 4, this is `o(1)`.

## 6. Edge cases

- The estimate is invalid on the structural zero set `L=0`.
- If `B(N)` is too large relative to `H_L`, the `log log B(N)` term may not be
  negligible.
- If the kernel absolute mass grows, the small divisor average can be lost.
- If the `h,k` windows are sparse sets rather than intervals, the congruence
  count must be replaced.
- Prime moduli larger than the averaging window are handled by the `1/H_L`
  term; this is exactly why the logarithmic loss appears.
- Pure `d` forms require dyadic `d` averaging and are not part of this module.

## 7. Where it fits in the project map

Modules 184 and 185 handle structural collision strata. Module 186 handles the
remaining nonstructural divisor averages:

```text
collision defects
  -> structural zero strata
  -> nonstructural beta_w(L)
  -> finite-interval congruence counting.
```

This advances the projected model-neutrality branch, subject to the still-open
local-factor collision envelope and projected local-model matching theorem.

## 8. What remains open

This module does not prove:

- the local-factor collision-envelope bound from Module 183;
- the kernel absolute-mass bound for the actual major-arc projection;
- the boundary transfer for the sharp interval model;
- projected local-model matching;
- minor-arc large-spectrum decay;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- any actual sharp moving-selector theorem.

## Red flags / forbidden upgrades

- Do not apply this estimate on structural zero strata.
- Do not ignore the `log log B(N)` loss.
- Do not drop the kernel absolute-mass factor.
- Do not treat this divisor estimate as projected local-model matching.
- Do not use this conditional counting lemma as an endpoint proof.
- Do not transfer it to actual sharp moving selectors without all transfer
  packages.
