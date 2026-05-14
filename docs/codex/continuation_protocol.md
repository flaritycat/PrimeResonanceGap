# Continuation protocol

When continuing the project:

1. Start from the latest module number.
2. Use exactly one allowed status label.
3. Never upgrade an endpoint unless the proof is supplied.
4. Preserve selector taxonomy.
5. Preserve gap-object taxonomy.
6. Preserve exact local models.
7. If an analytic endpoint is open, state it as open.
8. End every module with edge cases, project-map location, what remains open, and red flags.
9. Read and follow `docs/status/long_term_plan.md` before choosing the next
   module.
10. Update the long-term plan every 9th solving iteration after its adoption.
11. Question the long-term plan every 15th solving iteration after its adoption.

## Required module format

```text
# Module NNN: Title

## 1. Precise theorem / claim being advanced
## 2. Status label
## 3. Definitions and variables
## 4. Assumptions
## 5. Proof / disproof / reduction
## 6. Edge cases
## 7. Where it fits in the project map
## 8. What remains open
## Red flags / forbidden upgrades
```

## Long-term planning cadence

The active long-term plan is:

```text
docs/status/long_term_plan.md
```

It defines:

- the current module anchor;
- the post-reflection solving count;
- the plan-update count;
- the 9-iteration plan update cadence;
- the 15-iteration plan challenge cadence;
- the 40-iteration reflective-log cadence.

When multiple cadences are due in the same solving iteration, perform all due
actions. The plan is allowed to change, but any change must preserve the global
status ledger and forbidden-upgrade discipline.

## Continuation pointer

Historical first continuation task after the handoff:

```text
Fourier major/minor decomposition for the residual derivative cube endpoint.
```

After Module 187 and the adoption of the long-term plan, continue from the
latest module and the immediate next action named in
`docs/status/long_term_plan.md`.

Do not prove the endpoint unless an actual proof is supplied. A major/minor
split is structural unless estimates close both parts in the required range.
