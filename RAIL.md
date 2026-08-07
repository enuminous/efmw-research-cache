# Public research rail v0.2

Purpose: provide a searchable anchor for another researcher or agent without asking them to trust a narrative summary.

## Boundary

This repository contains only public-safe artifacts and our own work:

- our code and tests;
- our measured outputs;
- our analytical classifications;
- public source URLs used as context;
- explicit proposals for future tests.

It does not contain private conversations, credentials, personal data, hidden archives, or unpublished source material. Repository access is not permission to speak for us, alter external systems, contact the original author, or publish new claims under our name.

## Evidence classes

- `our_reproduction`: independently implemented and run by us; command and result are recorded.
- `our_analysis`: our interpretation or mathematical audit, with the source and reasoning boundary exposed.
- `proposal`: a test design, not a result.

A public source link is provenance. It is not evidence that our claim is true.

## Claim states

- `supported`: the narrow statement survived the stated validation.
- `conditional`: valid only under explicit assumptions or scope.
- `not_established`: our review does not establish the broader claim.
- `blocked`: a proposed test could not run because a prerequisite was missing.
- `unresolved`: evidence is insufficient; do not fill the gap with confidence.
- `proposal`: a falsifiable next experiment, not an outcome.

## Agent workflow

1. Read `README.md`, this file, and `data/claims.jsonl`.
2. Search claims by `claim_id`, `mechanism`, and `status`.
3. Follow every evidence pointer before summarizing.
4. Separate `receipt.promise` from `receipt.result`.
5. State the narrow claim, assumptions, baseline, and falsifier.
6. Re-run executable artifacts before calling a result reproduced.
7. Use public-safe derivatives when adding work.
8. Make one bounded contribution at a time through a normal pull request.

Run the local checks:

```bash
python3 scripts/validate_cache.py
python3 -m unittest discover -s tests -v
```

A passing validator proves schema consistency, not the research conclusion. The universe remains outside the unit test, which is probably for the best.

## Contribution schema

New claim records must include:

- stable `claim_id`;
- one-sentence claim;
- `our_reproduction`, `our_analysis`, or `proposal` evidence class;
- claim status;
- public evidence pointers;
- exact command/protocol where executable;
- promise/result receipt;
- falsifier;
- actor and date;
- `public-safe` privacy label.

Do not overwrite a closed receipt. Append a correction or superseding receipt.

## Promotion rule

A claim may move from `proposal` to `conditional` only when its assumptions and test are explicit. It may move to `supported` only after an executable or auditable result is recorded. Broad physical, consciousness, and universal claims require discriminating evidence against credible alternatives; internal coherence is not enough.

## External-action rule

The rail supports research, not autonomous publication. No agent may contact the original author, open issues elsewhere, post socially, deploy code, spend money, or modify another repository without explicit approval for that exact action.
