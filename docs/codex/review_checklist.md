# Review checklist

Use this for every PR, Codex-generated patch, or mathematical continuation.

## P0 issues

Flag as P0 if a patch:

- claims the original positive problem is solved;
- claims the all-alpha theorem is proved;
- claims the finite-type theorem is unconditional;
- claims `RBDH`, `CPC_3^sharp`, or `AU^3` is proved without a proof;
- replaces `Sigma_w(d,h)` with `kappa_w(d)^2` pointwise;
- uses first-moment HL as RBDH;
- upgrades smoothed/frozen/model selector to actual sharp moving selector without transfer.

## P1 issues

Flag as P1 if a patch:

- omits a status label;
- omits assumptions;
- omits edge cases;
- omits the range `D <= Hcal(N)`;
- omits boundary/collision/W/prime-power transfer;
- fails to say what remains open;
- conflates full gaps, clipped gaps, tails, thresholds, and tuple arrays.

## P2 issues

Flag as P2 if a patch:

- uses inconsistent notation;
- creates duplicate module numbers;
- fails to update indexes;
- adds raw theorem statements without dependencies.
