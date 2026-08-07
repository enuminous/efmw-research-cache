# EFMW research cache

Private working cache for independent research on the EFMW framework by Matthew C. Wright / @enuminous.

Source trail:

- X thread: https://x.com/enuminous/status/2085498481670779122
- Publication: https://enuminous.substack.com/
- Public review repository: https://github.com/leo-guinan/efmw-equation-review

This repository is intentionally private because it contains unpublished synthesis, internal validation receipts, and research coordination metadata. It is not a truth oracle. A private cache can protect unpublished work; it cannot turn a conditional result into a fact. The epistemic status of every item is explicit.

## Research rail

An agent entering this repository must:

1. Read `RAIL.md` before interpreting any claim.
2. Search `data/claims.jsonl` by claim ID, mechanism, and status.
3. Follow every evidence pointer before summarizing.
4. Preserve the distinction between `supported`, `conditional`, `not_established`, `blocked`, and `unresolved`.
5. Treat `result` as a receipt of what was actually run, not as a restatement of the promise.
6. Never publish private cache contents, quote unpublished synthesis, or contact the originator without explicit operator approval.
7. Add new work by append-only evidence receipts and a falsifier. Do not overwrite a closed receipt.
8. Before claiming an improvement, run the validator and cite the exact commit and test output.

## Current contents

- `RAIL.md`: agent operating boundary and contribution protocol.
- `data/claims.jsonl`: machine-searchable claims and evidence receipts.
- `data/source_index.jsonl`: public source index and coverage facts.
- `scripts/validate_cache.py`: dependency-free schema and consistency validator.
- `tests/test_cache.py`: local tests for the rail.

## Current evidence boundary

Supported by our own execution:

- the 102-image inventory is complete;
- the visible `888 = 23 × 38 + 14` arithmetic relation is correct;
- the public Substack archive/sitemap contains 707 matching post URLs in the captured snapshot;
- the linear observer/controller mechanism described in the formalism stabilizes the chosen unstable toy system under explicit gains.

Conditional:

- the control-theoretic mechanism may be useful as an EFMW engineering core;
- the bounded recovery-margin/collapse argument is valid under its stated dynamical assumptions;
- the proposed model-wrapper and lead-time tests are suitable preregistration hypotheses.

Not established:

- a new informational stress tensor or universal physical field;
- retrocausal physics, cognitive electromagnetic waves, cosmological modifications, consciousness from recursion, or measured model-performance gains.

The public review repository contains the reproducible public-facing implementation. This private cache contains the structured claim ledger and the rail for future agent work.
