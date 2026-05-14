# Module 187: Local-factor collision envelope for projected singular models

## 1. Precise theorem / claim being advanced

This module examines the local Euler-factor step behind the collision-defect
template in Module 183. It gives the correct envelope for the difference
between projected singular models and their generic collision-free models.

The important correction is that a strictly linear pointwise envelope:

```text
|Delta_w^{coll}| <= C sum_{i<j} beta_w(L_{ij})
```

is not automatic without a small-collision-load hypothesis. Under the local
Euler-product model assumed in this module, the available envelope has the form:

```text
|Delta_w^{coll}|
  <= C exp(C B_w) B_w + tail_w,
```

where:

```text
B_w(d,h,k;t) = sum_{i<j} beta_w(L_{ij}(d,h,k;t)),
beta_w(m) = sum_{p>w, p|m} 1/p.
```

The linear envelope used in Module 183 is valid after restricting to the
region `B_w <= 1`, or after proving an additional overflow estimate on
`B_w > 1`.

## 2. Status label

`CONDITIONAL`

This is a conditional local-factor envelope. It depends on the exact singular
series product formula and does not prove projected local-model matching or
the endpoint.

## 3. Definitions and variables

For a subset `S` of the eight projected vertices from Module 181, let:

```text
s = |S|.
```

For a prime `p>w`, let:

```text
r_p(S) = number of distinct residue classes mod p occupied by S.
```

The projected local factor is:

```text
theta_{p,S}^{proj}
  = (1 - 1/p)^(-s) (1 - r_p(S)/p).
```

The generic factor is:

```text
theta_{p,S}^{gen}
  = (1 - 1/p)^(-s) (1 - s/p).
```

The projected and generic singular models are:

```text
Theta_{w,S}^{proj} = prod_{p>w} theta_{p,S}^{proj},
Theta_{w,S}^{gen}  = prod_{p>w} theta_{p,S}^{gen}.
```

For pair-difference forms `L_{ij}` among projected vertices, define:

```text
B_w = sum_{i<j} beta_w(L_{ij}),
beta_w(m)=sum_{p>w,p|m} 1/p.
```

Structural zero strata `L_{ij}=0` are excluded or treated separately as in
Modules 184-185.

## 4. Assumptions

Assume:

- the exact local factors have the form above for all subsets `S`;
- `w` is large enough that `p>w` exceeds the fixed complexity bound `s <= 8`;
- local obstructions other than collisions among projected vertices have been
  separated;
- structural zero strata are removed before applying `beta_w`;
- Euler products are interpreted with the projective/W-limit order.

To recover the linear envelope from Module 183, additionally assume either:

```text
B_w(d,h,k;t) <= 1
```

on the active range, or prove a separate overflow estimate:

```text
E_{d,h,k,t} |W_M(t)| exp(C B_w) B_w 1_{B_w>1} = o(1).
```

## 5. Proof / disproof / reduction

For fixed `S` and prime `p>w`, write:

```text
delta_p(S) = s - r_p(S).
```

If no two forms in `S` collide modulo `p`, then `delta_p(S)=0` and:

```text
theta_{p,S}^{proj} = theta_{p,S}^{gen}.
```

If collisions occur, then:

```text
0 <= delta_p(S)
  <= sum_{i<j, i,j in S} 1_{p | L_{ij}}.
```

For `p>w` sufficiently large:

```text
theta_{p,S}^{proj} - theta_{p,S}^{gen}
  = (1 - 1/p)^(-s) delta_p(S)/p,
```

and:

```text
|theta_{p,S}^{proj}/theta_{p,S}^{gen} - 1|
  <= C_s delta_p(S)/p.
```

Multiplying over primes gives:

```text
|Theta_{w,S}^{proj} - Theta_{w,S}^{gen}|
  <= C_s exp(C_s B_w(S)) B_w(S) + tail_w,
```

where:

```text
B_w(S)=sum_{i<j, i,j in S} beta_w(L_{ij})
```

and `tail_w` covers the generic `sum_{p>w} 1/p^2` errors.

Since there are only finitely many subsets `S` of the eight vertices,
inclusion-exclusion gives:

```text
|Omega_w^{proj} - Omega_w^{gen}|
  <= C exp(C B_w) B_w + tail_w.
```

On the region `B_w <= 1`, this reduces to:

```text
|Omega_w^{proj} - Omega_w^{gen}|
  <= C B_w + tail_w.
```

This is the linear collision-envelope template used in Module 183, now with
its missing hypothesis made explicit.

## 6. Edge cases

- Structural zero strata make `beta_w(L)` ill-defined or too large and must be
  removed first.
- Multiple collisions at the same prime can increase `delta_p(S)`, but only
  by a bounded amount because the cube has eight vertices.
- The generic `sum_{p>w} 1/p^2` tail is harmless only after the W-limit order
  is respected.
- If `B_w` has a heavy tail, the exponential envelope cannot be replaced by a
  linear one.
- Local obstructions not caused by pair collisions must be listed separately;
  they are not controlled by pair-difference beta sums.
- The projected kernel weights do not enter the local factor calculation, but
  they enter every averaged use of the envelope.

## 7. Where it fits in the project map

Modules 183 and 186 used a linear collision-envelope template. Module 187
supplies the local-factor justification and correction:

```text
local projected singular factors
  -> collision load B_w
  -> exponential envelope
  -> linear envelope only on B_w <= 1 or with overflow control.
```

Module 188 supplies a conditional overflow criterion for the region `B_w>1`.
Module 189 reduces one exponential-integrability route to a joint
union-divisibility criterion. The remaining work is to verify that criterion
for the actual projected kernel.

## 8. What remains open

This module does not prove:

- verification of the Module 189 joint-divisibility criterion behind the
  Module 188 overflow hypotheses for `B_w>1`;
- the averaged collision-defect bound under the exponential envelope;
- projected local-model matching for the actual major-arc cube;
- minor-arc large-spectrum decay;
- `ResCube_3^sharp`, `CPC_3^sharp`, `RBDH_pair_short`, or `AU^3`;
- any actual sharp moving-selector theorem.

## Red flags / forbidden upgrades

- Do not use the linear envelope without a small-load or overflow hypothesis.
- Do not apply `beta_w(L)` on structural zero strata.
- Do not treat local-factor collision control as projected local-model
  matching.
- Do not use this module as an endpoint proof.
- Do not transfer this model calculation to actual sharp moving selectors
  without all transfer packages.
