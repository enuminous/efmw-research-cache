#!/usr/bin/env python3
"""Validate the private evidence cache without external dependencies."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLAIMS = ROOT / 'data' / 'claims.jsonl'
SOURCES = ROOT / 'data' / 'source_index.jsonl'
ALLOWED_STATUS = {'supported','conditional','not_established','blocked','unresolved','proposal'}
ALLOWED_CLASSES = {'our_reproduction','our_analysis','proposal'}
REQUIRED = {'claim_id','claim','status','evidence_class','evidence','receipt','falsifier','privacy','actor','created_at'}


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def validate():
    claims = read_jsonl(CLAIMS)
    sources = read_jsonl(SOURCES)
    assert claims and sources
    ids = [c['claim_id'] for c in claims]
    assert len(ids) == len(set(ids)), 'duplicate claim_id'
    for c in claims:
        assert REQUIRED <= c.keys(), f'missing claim fields: {c}'
        assert c['status'] in ALLOWED_STATUS
        assert c['evidence_class'] in ALLOWED_CLASSES
        assert isinstance(c['evidence'], list) and c['evidence']
        assert c['receipt']['promise']
        assert 'result' in c['receipt']
        assert c['falsifier']
        assert c['privacy'] == 'public-safe'
        if c['status'] == 'supported':
            assert c['receipt']['result'] not in (None, '')
    for s in sources:
        assert {'source_id','title','url','role','access','reviewed','notes'} <= s.keys()
        assert s['access'] == 'public'
    return len(claims), len(sources)


def main():
    claims, sources = validate()
    print(f'claims: {claims}')
    print(f'sources: {sources}')
    print('cache_schema: PASS')


if __name__ == '__main__':
    main()
