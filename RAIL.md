# Research rail v0.1

Purpose: let a researcher point an agent at this cache and continue the work without confusing internal validation, public evidence, and hypotheses.

## Access boundary

This is a private cache. The following are forbidden without explicit approval:

- publishing cache files or excerpts;
- copying unpublished notes into public issues, posts, or pull requests;
- sending messages to Matthew Wright, @enuminous, or any third party;
- adding credentials, private conversations, personal data, or secrets;
- treating repository access as permission to change the public review repository;
- changing a claim from conditional/not-established to supported without a new receipt.

Private means access-controlled, not magically verified. Every claim still needs an evidence class.

## Evidence classes

- `source_observation`: directly observed in a public source; cite URL and retrieval context.
- `our_reproduction`: independently implemented/run by us; include command, result, and artifact path.
- `author_report`: reported by the author but not independently reproduced.
- `inference`: our interpretation from sources or runs; never present as direct observation.
- `proposal`: a test design, not a result.

## Claim states

- `supported`: the narrow statement survived the stated validation.
- `conditional`: mathematically or operationally valid only under explicit assumptions.
- `not_established`: evidence inspected but does not establish the broader claim.
- `blocked`: the proposed test could not run because a prerequisite was missing.
- `unresolved`: insufficient evidence; do not fill the gap with confidence.

## Agent workflow

### Read

1. Load `README.md`, this file, and `data/claims.jsonl`.
2. Search by `claim_id`, `mechanism`, or `status`.
3. Read every `evidence` pointer attached to a candidate claim.
4. Check `receipt.promise`, `receipt.result`, and `falsifier` separately.

### Analyze

1. State the narrow claim, not the attractive generalization.
2. Name the assumptions doing the work.
3. Compare against a boring baseline.
4. Identify the observation that would falsify the claim.
5. If the result depends on a toy choice, mark it as toy evidence.

### Contribute

Contributions must be append-only JSONL records or new files. Each new record requires:

- stable `claim_id`;
- one-sentence claim;
- evidence class and state;
- source or artifact pointer;
- exact command or protocol when executable;
- promise/result receipt;
- falsifier;
- author/agent and timestamp;
- privacy classification.

Run:

```bash
python3 scripts/validate_cache.py
python3 -m unittest discover -s tests -v
```

A passing validator proves schema and receipt consistency only. It does not prove the research claim. The universe remains disappointingly outside the unit test.

## Promotion rule

A claim may move from `proposal` to `conditional` only when its assumptions and executable test are explicit. It may move to `supported` only after an independent run produces a receipt and the stated falsifier was not triggered within the tested scope. Broad physical or consciousness claims remain `not_established` until they have discriminating evidence against credible alternatives.

## Public-release rail

To move material from this cache into the public review repository:

1. Create a public-safe derivative file.
2. Remove unpublished synthesis and private provenance.
3. Preserve exact source URLs and evidence class.
4. Run the privacy scan and validator.
5. Obtain explicit operator approval for the external write.
6. Push one commit and read back the public tree.

No automatic sync. No surprise leaks. No “it was only a cache” autopsy.
