#!/usr/bin/env python3
"""Lightweight status/overclaim audit for PrimeResonanceGap active docs."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTS = {".md", ".txt"}

ACTIVE_PREFIXES = (
    Path("docs/modules"),
    Path("docs/status"),
    Path("papers"),
)
ACTIVE_FILES = {
    Path("README.md"),
}
ARCHIVAL_PREFIXES = (
    Path("source_texts"),
    Path("docs/paper"),
    Path("docs/ledger"),
)
INTENTIONAL_FILES = {
    Path("AGENTS.md"),
    Path("docs/status/forbidden_upgrades.md"),
    Path("docs/codex/continuation_protocol.md"),
    Path("docs/codex/SHORT_CODEX_PROMPT.md"),
}
GENERATED_PREFIXES = ("generated_",)


def is_under(path: Path, prefix: Path) -> bool:
    try:
        path.relative_to(ROOT / prefix)
        return True
    except ValueError:
        return False


def is_archival(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    return any(is_under(path, prefix) for prefix in ARCHIVAL_PREFIXES) or (
        rel.name.startswith(GENERATED_PREFIXES)
    )


def is_active(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    return rel in ACTIVE_FILES or any(is_under(path, prefix) for prefix in ACTIVE_PREFIXES)


def is_intentional(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    name = rel.name.lower()
    return (
        rel in INTENTIONAL_FILES
        or "forbidden" in name
        or "audit" in name
        or "prompt" in name
    )


SAFE_CONTEXT = re.compile(
    r"\b("
    r"do not|never|not|without|forbidden|blocked|false|red flag|"
    r"remains open|open|conditional|not proved|does not prove|"
    r"does not claim|must not|endpoint-strength|guardrail"
    r")\b",
    re.I,
)

FORBIDDEN_PATTERNS = [
    (
        re.compile(
            r"(therefore\s+)?(the\s+)?original (selected-average|positive existence) "
            r"(problem\s+)?(is\s+)?(solved|proved|closed)",
            re.I,
        ),
        "original selected-average problem overclaim",
    ),
    (
        re.compile(r"all[- ]alpha .* (proved|solved|closed)", re.I),
        "all-alpha overclaim",
    ),
    (
        re.compile(r"\bunconditional proof\b|\bunconditional finite[- ]type theorem\b.*\bproved\b", re.I),
        "unconditional proof/theorem overclaim",
    ),
    (
        re.compile(r"\bendpoint (is )?(closed|proved|solved)\b", re.I),
        "endpoint closure overclaim",
    ),
    (
        re.compile(r"selector transfer (is )?automatic", re.I),
        "automatic selector-transfer overclaim",
    ),
    (
        re.compile(r"Pair[- ]BDH.*implies.*CPC", re.I),
        "Pair-BDH=>CPC forbidden shortcut",
    ),
    (
        re.compile(r"first[- ]moment.*implies.*RBDH", re.I),
        "first-moment=>RBDH forbidden shortcut",
    ),
    (
        re.compile(r"mean rectangle[- ]HL.*implies.*rectangle[- ]BDH", re.I),
        "mean rectangle-HL=>rectangle-BDH forbidden shortcut",
    ),
    (
        re.compile(r"Sigma_w\(d,h\)\s*=\s*kappa_w\(d\)\^2", re.I),
        "Sigma=kappa^2 pointwise model error",
    ),
]

PROTECTED_OBJECTS = [
    re.compile(r"ProjectedModelNeutralityGate_260", re.I),
    re.compile(r"CollNeutral_260", re.I),
    re.compile(r"WProjectedLocalMatch_3\^major", re.I),
    re.compile(r"ProjectedMajorTarget_3\^B", re.I),
    re.compile(r"ResCube_3\^sharp", re.I),
    re.compile(r"original (selected-average|positive existence) problem", re.I),
]

STATUS_PROVEN = re.compile(r"## 2\. Status label\s+`PROVEN`", re.I | re.S)


def safe_line(line: str) -> bool:
    return bool(SAFE_CONTEXT.search(line))


errors = []
warnings = []
checked = 0
skipped = 0

for path in ROOT.rglob("*"):
    if path.suffix not in TEXT_EXTS or ".git" in path.parts:
        continue
    if is_archival(path) or not is_active(path) or is_intentional(path):
        skipped += 1
        continue

    checked += 1
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8", errors="ignore")

    if STATUS_PROVEN.search(text) and any(obj.search(text) for obj in PROTECTED_OBJECTS):
        errors.append((rel, "protected endpoint/original object appears in a PROVEN module"))

    for line_no, line in enumerate(text.splitlines(), start=1):
        for pat, msg in FORBIDDEN_PATTERNS:
            if pat.search(line):
                item = (rel, line_no, msg)
                if safe_line(line):
                    warnings.append(item)
                else:
                    errors.append(item)

        if re.search(r"\bPROVEN\b", line):
            for obj in PROTECTED_OBJECTS:
                if obj.search(line) and not safe_line(line):
                    errors.append((rel, line_no, "protected object marked or implied PROVEN"))

if errors:
    print("Status audit failed:")
    for item in errors[:25]:
        if len(item) == 3:
            path, line_no, msg = item
            print(f"- {path}:{line_no}: {msg}")
        else:
            path, msg = item
            print(f"- {path}: {msg}")
    if len(errors) > 25:
        print(f"... {len(errors) - 25} more error(s)")
    print(f"Checked {checked} active file(s); skipped {skipped} archival/generated/intentional file(s).")
    sys.exit(1)

if warnings:
    print("Status audit warnings:")
    for path, line_no, msg in warnings[:10]:
        print(f"- {path}:{line_no}: {msg}")
    if len(warnings) > 10:
        print(f"... {len(warnings) - 10} more warning(s)")

print(
    "Status audit passed. "
    f"Checked {checked} active file(s); "
    f"skipped {skipped} archival/generated/intentional file(s); "
    f"{len(warnings)} warning(s)."
)
