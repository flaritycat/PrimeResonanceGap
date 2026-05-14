#!/usr/bin/env python3
"""Extract PAGE/MODULE-like headings from a text file into a markdown index."""
from pathlib import Path
import re, sys

if len(sys.argv) != 3:
    print('Usage: extract_modules.py INPUT.txt OUTPUT.md')
    sys.exit(2)

inp = Path(sys.argv[1])
out = Path(sys.argv[2])
text = inp.read_text(encoding='utf-8', errors='ignore').splitlines()

page_re = re.compile(r'^PAGE\s+(\d+)\s+OF\s+(\d+)', re.I)
title_re = re.compile(r'^TITLE:\s*(.*)$', re.I)
status_re = re.compile(r'^STATUS:\s*(.*)$', re.I)

items = []
current = {}
for line in text:
    m = page_re.match(line)
    if m:
        if current:
            items.append(current)
        current = {'page': m.group(1), 'of': m.group(2), 'title': '', 'status': ''}
        continue
    if current:
        mt = title_re.match(line)
        if mt:
            current['title'] = mt.group(1).strip()
        ms = status_re.match(line)
        if ms:
            current['status'] = ms.group(1).strip()
if current:
    items.append(current)

out.parent.mkdir(parents=True, exist_ok=True)
with out.open('w', encoding='utf-8') as f:
    f.write(f'# Extracted index for `{inp.name}`\n\n')
    f.write('| Page | Title | Status |\n|---:|---|---|\n')
    for it in items:
        f.write(f"| {it.get('page','')} | {it.get('title','')} | {it.get('status','')} |\n")
print(f'Extracted {len(items)} page entries to {out}')
