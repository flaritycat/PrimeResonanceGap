#!/usr/bin/env python3
"""Build a lightweight markdown index of docs and source texts."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / 'docs' / 'modules' / 'generated_file_index.md'
out.parent.mkdir(parents=True, exist_ok=True)

rows = []
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.suffix in {'.md', '.txt', '.json', '.yml', '.yaml', '.cff'}:
        rows.append((str(p.relative_to(ROOT)), p.stat().st_size))

with out.open('w', encoding='utf-8') as f:
    f.write('# Generated file index\n\n')
    f.write('| File | Bytes |\n|---|---:|\n')
    for rel, size in rows:
        f.write(f'| `{rel}` | {size} |\n')
print(f'Wrote {out.relative_to(ROOT)} with {len(rows)} files.')
