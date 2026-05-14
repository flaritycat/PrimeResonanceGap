#!/usr/bin/env python3
"""Lightweight status/overclaim audit for PrimeResonanceGap docs."""
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTS = {'.md', '.txt'}

FORBIDDEN_PATTERNS = [
    (re.compile(r'original positive (existence )?(problem )?(is )?(solved|proved|closed)', re.I), 'original positive problem overclaim'),
    (re.compile(r'all[- ]alpha .* (proved|solved|closed)', re.I), 'all-alpha overclaim'),
    (re.compile(r'finite[- ]type theorem (is )?proved', re.I), 'unconditional finite-type overclaim'),
    (re.compile(r'Pair[- ]BDH.*implies.*CPC', re.I), 'Pair-BDH=>CPC forbidden shortcut'),
    (re.compile(r'first[- ]moment.*implies.*RBDH', re.I), 'first-moment=>RBDH forbidden shortcut'),
    (re.compile(r'Sigma_w\(d,h\)\s*=\s*kappa_w\(d\)\^2', re.I), 'Sigma=kappa^2 pointwise model error'),
]

errors = []
for path in ROOT.rglob('*'):
    if path.suffix not in TEXT_EXTS or '.git' in path.parts:
        continue
    rel_parts = set(path.relative_to(ROOT).parts)
    # Skip archival source texts and instruction files that intentionally list forbidden claims.
    if {'source_texts'} & rel_parts or ('docs' in rel_parts and ('paper' in rel_parts or 'ledger' in rel_parts)):
        continue
    if 'codex' in rel_parts or '.github' in rel_parts:
        continue
    text = path.read_text(encoding='utf-8', errors='ignore')
    for pat, msg in FORBIDDEN_PATTERNS:
        if pat.search(text):
            # allowed if explicitly in forbidden docs or prompts
            if 'forbidden' in str(path).lower() or 'audit' in str(path).lower() or 'AGENTS.md' in str(path):
                continue
            errors.append((path, msg))

if errors:
    print('Status audit failed:')
    for path, msg in errors:
        print(f'- {path.relative_to(ROOT)}: {msg}')
    sys.exit(1)

print('Status audit passed. No obvious forbidden overclaims found.')
