#!/usr/bin/env python3
"""
Token Sync Script — merge_tokens.py
------------------------------------
Compares a "production" token file (from engineers/Storybook)
against the Design Team file (Tokens Studio / Figma).

Outputs:
  1. A merged JSON — DesignTeam file + all missing tokens from production
  2. A Markdown diff report — missing tokens + changed values
     (description-field differences are ignored)

Ignore list:
  tokens/sync-ignore.json — token paths to exclude from the changed-values
  report (e.g. font-family tokens that intentionally differ between Figma
  and production). The design team value is always kept regardless.

Usage:
  python scripts/merge_tokens.py \
    --design   tokens/design-team.json \
    --prod     tokens/production.json \
    --output   tokens/design-team-merged.json \
    --report   tokens/diff-report.md \
    --ignore   tokens/sync-ignore.json   # optional, defaults to this path
"""

import argparse
import copy
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


# ─── helpers ────────────────────────────────────────────────────────────────

def flatten_tokens(obj, prefix="", result=None):
    """Recursively flatten a token tree into dot-path → token-object pairs."""
    if result is None:
        result = {}
    if isinstance(obj, dict):
        if "value" in obj:
            result[prefix] = obj
        else:
            for k, v in obj.items():
                if k.startswith("$"):
                    continue
                new_prefix = f"{prefix}.{k}" if prefix else k
                flatten_tokens(v, new_prefix, result)
    return result


def set_nested(d, keys, value):
    """Write a value into a nested dict following a list of keys."""
    for k in keys[:-1]:
        d = d.setdefault(k, {})
    d[keys[-1]] = value


def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_ignore_list(path: Path) -> set:
    """
    Load token paths to ignore from sync-ignore.json.
    Returns a set of dot-path strings. Silently returns empty set
    if the file doesn't exist (so the ignore file is always optional).
    """
    if not path.exists():
        return set()
    data = load_json(path)
    entries = data.get("ignore_changes", [])
    paths = {e["path"] for e in entries if "path" in e}
    if paths:
        print(f"\u2139\ufe0f   Ignore list loaded ({len(paths)} entries) from {path}")
    return paths


def clean_token(token: dict) -> dict:
    """
    Return a copy of the token with the 'description' field removed
    when it is empty, None, or not present — so it never ends up
    cluttering the merged file.
    """
    t = copy.deepcopy(token)
    desc = t.get("description")
    if desc is None or (isinstance(desc, str) and desc.strip() == ""):
        t.pop("description", None)
    return t


def values_differ(a: dict, b: dict) -> bool:
    """True when two tokens have meaningfully different values."""
    return str(a.get("value", "")).strip() != str(b.get("value", "")).strip()


# ─── core logic ─────────────────────────────────────────────────────────────

def run(design_path: Path, prod_path: Path, output_path: Path, report_path: Path, ignore_path: Path = None):

    design_raw  = load_json(design_path)
    prod_raw    = load_json(prod_path)
    ignore_list = load_ignore_list(ignore_path) if ignore_path else set()

    # Flatten both files (skip $themes / $metadata)
    design_flat: dict = {}
    for k, v in design_raw.items():
        if not k.startswith("$"):
            flatten_tokens(v, k, design_flat)

    prod_flat: dict = {}
    for k, v in prod_raw.items():
        if not k.startswith("$"):
            flatten_tokens(v, k, prod_flat)

    # ── 1. tokens in production but missing from design ──────────────────────
    missing: dict[str, dict] = {
        k: v for k, v in prod_flat.items() if k not in design_flat
    }

    # ── 2. tokens that exist in both but whose VALUE changed ─────────────────
    changed: dict[str, dict] = {}   # path → {design_value, prod_value}
    ignored_changes: list[str] = []  # paths skipped due to ignore list
    for path, prod_token in prod_flat.items():
        if path in design_flat and values_differ(design_flat[path], prod_token):
            if path in ignore_list:
                ignored_changes.append(path)
                continue
            changed[path] = {
                "design_value": design_flat[path].get("value"),
                "prod_value":   prod_token.get("value"),
                "type":         prod_token.get("type", ""),
            }

    # ── 3. tokens only in design (not in production) — informational ─────────
    design_only: dict[str, dict] = {
        k: v for k, v in design_flat.items() if k not in prod_flat
    }

    # ─── Build merged file ───────────────────────────────────────────────────
    merged = copy.deepcopy(design_raw)

    for full_path, token in missing.items():
        parts    = full_path.split(".")
        set_key  = parts[0]
        tok_path = parts[1:]
        if set_key not in merged:
            merged[set_key] = {}
        set_nested(merged[set_key], tok_path, clean_token(token))

    # Clean description from ALL tokens in the merged file
    merged_clean = copy.deepcopy(merged)
    for set_key, set_val in merged_clean.items():
        if set_key.startswith("$"):
            continue
        flat_set: dict = {}
        flatten_tokens(set_val, set_key, flat_set)
        for path, tok in flat_set.items():
            parts    = path.split(".")
            tok_path = parts[1:]
            if tok_path:
                set_nested(merged_clean[set_key], tok_path, clean_token(tok))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(merged_clean, f, indent=2, ensure_ascii=False)

    # ─── Build Markdown report ───────────────────────────────────────────────
    now    = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines  = []

    lines += [
        f"# Token Diff Report",
        f"",
        f"**Generated:** {now}  ",
        f"**Design file:** `{design_path}`  ",
        f"**Production file:** `{prod_path}`",
        f"",
        f"---",
        f"",
        f"## Summary",
        f"",
        f"| | Count |",
        f"|---|---|",
        f"| 🆕 Missing tokens (added to merged file) | **{len(missing)}** |",
        f"| ⚠️ Changed values (review needed) | **{len(changed)}** |",
        f"| 🚫 Ignored changes (sync-ignore.json) | **{len(ignored_changes)}** |",
        f"| 🔵 Design-only tokens (not in production) | **{len(design_only)}** |",
        f"",
        f"---",
        f"",
    ]

    # ── Section 1: Missing tokens ─────────────────────────────────────────────
    lines += [
        f"## 🆕 Missing Tokens — added to merged file ({len(missing)})",
        f"",
        f"These tokens exist in the production file but were absent from the design file.  ",
        f"They have been automatically added to the merged output.",
        f"",
    ]

    if missing:
        # Group by token set
        by_set: dict[str, list] = {}
        for path, tok in sorted(missing.items()):
            set_key = path.split(".")[0]
            by_set.setdefault(set_key, []).append((path, tok))

        for set_name, tokens in sorted(by_set.items()):
            # Group by component within the set
            by_component: dict[str, list] = {}
            for path, tok in tokens:
                parts     = path.split(".")
                component = parts[1] if len(parts) > 1 else "Root"
                by_component.setdefault(component, []).append((path, tok))

            lines.append(f"### `{set_name}`")
            lines.append(f"")

            for component, comp_tokens in sorted(by_component.items()):
                lines.append(f"#### {component}")
                lines.append(f"")
                lines.append(f"| Token | Type | Value |")
                lines.append(f"|---|---|---|")
                for path, tok in sorted(comp_tokens):
                    token_name = ".".join(path.split(".")[2:]) if len(path.split(".")) > 2 else path.split(".")[-1]
                    val  = str(tok.get("value", "")).replace("|", "\\|").replace("\n", " ")
                    typ  = tok.get("type", "—")
                    lines.append(f"| `{token_name}` | {typ} | `{val}` |")
                lines.append(f"")
    else:
        lines += ["_No missing tokens._", ""]

    lines += ["---", ""]

    # ── Section 2: Changed values ─────────────────────────────────────────────
    lines += [
        f"## ⚠️ Changed Values — review required ({len(changed)})",
        f"",
        f"These tokens exist in both files but the production value differs from the design file.  ",
        f"**The merged file keeps the design team value.** Review each one and update manually if needed.",
        f"",
    ]

    if changed:
        by_set_c: dict[str, list] = {}
        for path, info in sorted(changed.items()):
            set_key = path.split(".")[0]
            by_set_c.setdefault(set_key, []).append((path, info))

        for set_name, tokens in sorted(by_set_c.items()):
            lines.append(f"### `{set_name}`")
            lines.append(f"")
            lines.append(f"| Token | Type | Design value | Production value |")
            lines.append(f"|---|---|---|---|")
            for path, info in sorted(tokens):
                token_name  = ".".join(path.split(".")[1:])
                dv = str(info["design_value"]).replace("|", "\\|").replace("\n", " ")
                pv = str(info["prod_value"]).replace("|", "\\|").replace("\n", " ")
                typ = info["type"] or "—"
                lines.append(f"| `{token_name}` | {typ} | `{dv}` | `{pv}` |")
            lines.append(f"")
    else:
        lines += ["_No value changes detected._", ""]

    lines += ["---", ""]

    # ── Section 2b: Ignored changes ──────────────────────────────────────────
    if ignored_changes:
        lines += [
            f"## 🚫 Ignored Changes — silenced by sync-ignore.json ({len(ignored_changes)})",
            f"",
            f"These value differences are intentional and have been suppressed.  ",
            f"Edit `tokens/sync-ignore.json` to manage this list.",
            f"",
            f"| Token | Reason |",
            f"|---|---|",
        ]
        ignore_data = load_json(ignore_path) if ignore_path and ignore_path.exists() else {}
        ignore_map = {e["path"]: e.get("reason", "—") for e in ignore_data.get("ignore_changes", [])}
        for p in sorted(ignored_changes):
            reason = ignore_map.get(p, "—").replace("|", "\\|")
            lines.append(f"| `{p}` | {reason} |")
        lines += ["", "---", ""]

    # ── Section 3: Design-only tokens ────────────────────────────────────────
    lines += [
        f"## 🔵 Design-only Tokens — not in production ({len(design_only)})",
        f"",
        f"These tokens exist only in the design file (e.g. custom Figma helpers).  ",
        f"They are preserved in the merged file as-is.",
        f"",
    ]

    if design_only:
        lines.append(f"| Token | Type | Value |")
        lines.append(f"|---|---|---|")
        for path, tok in sorted(design_only.items()):
            val = str(tok.get("value", "")).replace("|", "\\|").replace("\n", " ")
            typ = tok.get("type", "—")
            lines.append(f"| `{path}` | {typ} | `{val}` |")
        lines.append(f"")
    else:
        lines += ["_No design-only tokens._", ""]

    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # ─── Console summary ─────────────────────────────────────────────────────
    print(f"✅  Merged file   → {output_path}  ({len(design_flat) + len(missing)} tokens)")
    print(f"📄  Diff report   → {report_path}")
    print(f"")
    print(f"   🆕 Missing tokens added : {len(missing)}")
    print(f"   ⚠️  Changed values found : {len(changed)}")
    if ignored_changes:
        print(f"   🚫 Changes ignored       : {len(ignored_changes)}")
    print(f"   🔵 Design-only tokens   : {len(design_only)}")

    if changed:
        print(f"\n⚠️  Changed values detected — see the diff report for details.")

    return len(missing), len(changed)


# ─── CLI ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Merge & diff design token files.")
    parser.add_argument("--design",  required=True, help="Path to the Design Team token JSON")
    parser.add_argument("--prod",    required=True, help="Path to the production token JSON")
    parser.add_argument("--output",  required=True, help="Path for the merged output JSON")
    parser.add_argument("--report",  required=True, help="Path for the Markdown diff report")
    parser.add_argument("--ignore",  default="tokens/sync-ignore.json",
                        help="Path to sync-ignore.json (default: tokens/sync-ignore.json)")
    args = parser.parse_args()

    missing_count, changed_count = run(
        design_path = Path(args.design),
        prod_path   = Path(args.prod),
        output_path = Path(args.output),
        report_path = Path(args.report),
        ignore_path = Path(args.ignore),
    )

    # Exit code 2 if there are changed values (so CI can flag it clearly)
    if changed_count > 0:
        sys.exit(2)


if __name__ == "__main__":
    main()
