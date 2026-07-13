#!/usr/bin/env python3
"""
Token Sync Script — merge_tokens.py
------------------------------------
Compares a "production" token file (from engineers/Storybook — one big JSON)
against the Design Team files (Tokens Studio / GitHub — split into individual
JSON files per token set, plus $metadata.json and $themes.json).

Reads:
  tokens/Snap Motif/Global.json
  tokens/Snap Motif/Primary.json
  tokens/Snap Motif/Secondary.json
  tokens/Snap Motif/Tertiary.json
  tokens/Snap Motif/Quaternary.json
  tokens/$metadata.json
  tokens/$themes.json

Writes (same split structure — safe to commit & re-import in Tokens Studio):
  tokens/Snap Motif/Global.json       ← updated in place
  tokens/Snap Motif/Primary.json      ← updated in place
  ... (only files that actually changed)
  tokens/diff-report.md               ← diff report

Ignore list:
  tokens/sync-ignore.json — token paths to exclude from the changed-values
  report. The design team value/type is always kept regardless.

Usage:
  python scripts/merge_tokens.py \
    --design-dir  tokens \
    --prod        production.json \
    --ignore      tokens/sync-ignore.json

NOTE: production.json must live at the REPO ROOT (not inside tokens/).
Tokens Studio treats every .json inside tokens/ as a token set — keeping
production.json outside that folder prevents it from showing up as a set.
"""

import argparse
import copy
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


# ── Token set names → file paths (relative to design-dir) ───────────────────
# Order matches $metadata.tokenSetOrder
TOKEN_SETS = [
    "Snap Motif/Global",
    "Snap Motif/Primary",
    "Snap Motif/Secondary",
    "Snap Motif/Tertiary",
    "Snap Motif/Quaternary",
]


# ─── helpers ────────────────────────────────────────────────────────────────

def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")   # trailing newline — consistent with Tokens Studio output


def load_ignore_list(path: Path) -> set:
    """
    Load token paths to ignore from sync-ignore.json.
    Paths here use the full dot-path WITHOUT the set-name prefix,
    e.g. "Root.--h1-font-family" (not "Snap Motif/Global.Root.--h1-font-family")
    because inside each split file there is no set-name prefix.
    Returns a set of such strings.
    """
    if not path or not path.exists():
        return set()
    data = load_json(path)
    entries = data.get("ignore_changes", [])
    # Strip the set-name prefix if present (support both formats)
    paths = set()
    for e in entries:
        p = e.get("path", "")
        # If path contains "/" it has a set prefix like "Snap Motif/Global.Root.--h1-..."
        # Strip everything up to and including the first "."  after the "/"
        if "/" in p:
            p = p.split(".", 1)[1] if "." in p else p
        paths.add(p)
    if paths:
        print(f"ℹ️   Ignore list loaded ({len(paths)} entries) from {path}")
    return paths


def flatten_tokens(obj, prefix="", result=None):
    """Flatten a token tree into dot-path → token-object pairs."""
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


def clean_token(token: dict) -> dict:
    """Remove 'description' when it is empty or absent."""
    t = copy.deepcopy(token)
    desc = t.get("description")
    if desc is None or (isinstance(desc, str) and desc.strip() == ""):
        t.pop("description", None)
    return t


def token_diff_reasons(design_tok: dict, prod_tok: dict) -> list[str]:
    """
    Compare a design-side token and a production-side token.
    Returns a list of field names that differ, e.g. ["value"], ["type"],
    or ["value", "type"]. Empty list means no relevant difference.
    """
    reasons = []
    if str(design_tok.get("value", "")).strip() != str(prod_tok.get("value", "")).strip():
        reasons.append("value")
    if str(design_tok.get("type", "")).strip() != str(prod_tok.get("type", "")).strip():
        reasons.append("type")
    return reasons


# ─── load design-side split files ───────────────────────────────────────────

def load_design_sets(design_dir: Path) -> dict[str, dict]:
    """
    Returns { "Snap Motif/Global": { ...tokens... }, ... }
    Reads each set file. Missing files are loaded as empty dicts (won't crash).
    """
    sets = {}
    for set_name in TOKEN_SETS:
        # "Snap Motif/Global" → "Snap Motif/Global.json"
        file_path = design_dir / f"{set_name}.json"
        if file_path.exists():
            sets[set_name] = load_json(file_path)
        else:
            print(f"⚠️  Set file not found: {file_path} — treating as empty")
            sets[set_name] = {}
    return sets


def flatten_all_sets(sets: dict[str, dict]) -> dict[str, dict]:
    """
    Flatten all sets into one dict keyed by FULL path:
      "Snap Motif/Global.Root.--h1-font-family" → token object
    (The set name is prepended so we can compare across the full token space.)
    """
    result = {}
    for set_name, set_data in sets.items():
        flatten_tokens(set_data, set_name, result)
    return result


# ─── load production file ────────────────────────────────────────────────────

def load_prod_flat(prod_path: Path) -> dict[str, dict]:
    """
    The production file is one big JSON keyed by set name at the top level.
    e.g. { "Snap Motif/Global": { "Root": { ... } }, "Snap Motif/Primary": ... }
    Flatten it the same way as design sets.
    """
    prod_raw = load_json(prod_path)
    result = {}
    for k, v in prod_raw.items():
        if not k.startswith("$"):
            flatten_tokens(v, k, result)
    return result


# ─── core ────────────────────────────────────────────────────────────────────

def run(design_dir: Path, prod_path: Path, ignore_path: Path = None):

    design_sets = load_design_sets(design_dir)
    design_flat = flatten_all_sets(design_sets)
    prod_flat   = load_prod_flat(prod_path)
    ignore_list = load_ignore_list(ignore_path)

    # ── 1. Missing: in prod but not in design ────────────────────────────────
    missing: dict[str, dict] = {
        k: v for k, v in prod_flat.items() if k not in design_flat
    }

    # ── 2. Changed: exist in both but value and/or type differs ─────────────
    changed: dict[str, dict] = {}
    ignored_changes: list[str] = []

    for path, prod_token in prod_flat.items():
        if path not in design_flat:
            continue
        reasons = token_diff_reasons(design_flat[path], prod_token)
        if not reasons:
            continue
        # Strip set prefix for ignore-list lookup
        local_path = path.split(".", 1)[1] if "." in path else path
        if local_path in ignore_list or path in ignore_list:
            ignored_changes.append(path)
            continue
        changed[path] = {
            "design_value": design_flat[path].get("value"),
            "prod_value":   prod_token.get("value"),
            "design_type":  design_flat[path].get("type", ""),
            "prod_type":    prod_token.get("type", ""),
            "reasons":      reasons,
        }

    # ── 3. Design-only: in design but not in prod ────────────────────────────
    design_only: dict[str, dict] = {
        k: v for k, v in design_flat.items() if k not in prod_flat
    }

    # ── Write merged split files ─────────────────────────────────────────────
    # Group missing tokens by set name
    missing_by_set: dict[str, dict] = {s: {} for s in TOKEN_SETS}
    for full_path, token in missing.items():
        # full_path = "Snap Motif/Primary.Accordion.--accordion-item-color"
        # set_name  = "Snap Motif/Primary"
        # tok_path  = ["Accordion", "--accordion-item-color"]
        set_name = None
        for s in TOKEN_SETS:
            if full_path.startswith(s + "."):
                set_name = s
                break
        if set_name is None:
            print(f"⚠️  Could not match set for path: {full_path} — skipping")
            continue
        tok_path = full_path[len(set_name) + 1:].split(".")
        set_nested(missing_by_set[set_name], tok_path, clean_token(token))

    files_written = []
    for set_name in TOKEN_SETS:
        additions = missing_by_set.get(set_name, {})
        if not additions:
            continue   # nothing to add to this file

        file_path   = design_dir / f"{set_name}.json"
        set_data    = copy.deepcopy(design_sets[set_name])

        # Deep-merge additions into set_data
        def deep_merge(base, overlay):
            for k, v in overlay.items():
                if k in base and isinstance(base[k], dict) and isinstance(v, dict):
                    deep_merge(base[k], v)
                else:
                    base[k] = v

        deep_merge(set_data, additions)

        # Clean descriptions across the whole updated set
        flat_updated = {}
        flatten_tokens(set_data, "", flat_updated)
        for tok_path_str, tok in flat_updated.items():
            if tok_path_str:
                set_nested(set_data, tok_path_str.split("."), clean_token(tok))

        save_json(file_path, set_data)
        files_written.append(str(file_path))

    # ── Write diff report ────────────────────────────────────────────────────
    report_path = design_dir / "diff-report.md"
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# Token Diff Report",
        "",
        f"**Generated:** {now}  ",
        f"**Design dir:** `{design_dir}`  ",
        f"**Production file:** `{prod_path}`",
        "",
        "---",
        "",
        "## Summary",
        "",
        "| | Count |",
        "|---|---|",
        f"| 🆕 Missing tokens (added to set files) | **{len(missing)}** |",
        f"| ⚠️ Changed values (review needed) | **{len(changed)}** |",
        f"| 🚫 Ignored changes (sync-ignore.json) | **{len(ignored_changes)}** |",
        f"| 🔵 Design-only tokens (not in production) | **{len(design_only)}** |",
        "",
        "---",
        "",
    ]

    # Section 1 — Missing
    lines += [
        f"## 🆕 Missing Tokens — added to set files ({len(missing)})",
        "",
        "These tokens exist in the production file but were absent from the design files.  ",
        "They have been automatically added to the corresponding set file.",
        "",
    ]

    if missing:
        by_set: dict[str, list] = {}
        for path, tok in sorted(missing.items()):
            for s in TOKEN_SETS:
                if path.startswith(s + "."):
                    by_set.setdefault(s, []).append((path, tok))
                    break

        for set_name, tokens in sorted(by_set.items()):
            by_component: dict[str, list] = {}
            for path, tok in tokens:
                local = path[len(set_name) + 1:]
                component = local.split(".")[0] if "." in local else "Root"
                by_component.setdefault(component, []).append((path, tok))

            lines.append(f"### `{set_name}`")
            lines.append("")
            for component, comp_tokens in sorted(by_component.items()):
                lines.append(f"#### {component}")
                lines.append("")
                lines.append("| Token | Type | Value |")
                lines.append("|---|---|---|")
                for path, tok in sorted(comp_tokens):
                    local = path[len(set_name) + 1:]
                    token_name = ".".join(local.split(".")[1:]) or local
                    val = str(tok.get("value", "")).replace("|", "\\|").replace("\n", " ")
                    typ = tok.get("type", "—")
                    lines.append(f"| `{token_name}` | {typ} | `{val}` |")
                lines.append("")
    else:
        lines += ["_No missing tokens._", ""]

    lines += ["---", ""]

    # Section 2 — Changed
    lines += [
        f"## ⚠️ Changed Values — review required ({len(changed)})",
        "",
        "These tokens exist in both files but the **value and/or type** differs "
        "between production and design.  ",
        "**The design file value/type is kept.** Review each one and update manually if needed.",
        "",
        "The **Changed** column shows whether it's the `value`, the `type`, or both that differ.",
        "",
    ]

    if changed:
        by_set_c: dict[str, list] = {}
        for path, info in sorted(changed.items()):
            for s in TOKEN_SETS:
                if path.startswith(s + "."):
                    by_set_c.setdefault(s, []).append((path, info))
                    break

        for set_name, tokens in sorted(by_set_c.items()):
            lines.append(f"### `{set_name}`")
            lines.append("")
            lines.append("| Token | Changed | Design value | Production value | Design type | Production type |")
            lines.append("|---|---|---|---|---|---|")
            for path, info in sorted(tokens):
                token_name = path[len(set_name) + 1:]
                dv  = str(info["design_value"]).replace("|", "\\|").replace("\n", " ")
                pv  = str(info["prod_value"]).replace("|", "\\|").replace("\n", " ")
                dt  = info["design_type"] or "—"
                pt  = info["prod_type"] or "—"
                changed_label = " + ".join(info["reasons"])
                lines.append(f"| `{token_name}` | {changed_label} | `{dv}` | `{pv}` | `{dt}` | `{pt}` |")
            lines.append("")
    else:
        lines += ["_No value or type changes detected._", ""]

    lines += ["---", ""]

    # Section 2b — Ignored
    if ignored_changes:
        lines += [
            f"## 🚫 Ignored Changes — silenced by sync-ignore.json ({len(ignored_changes)})",
            "",
            "These value/type differences are intentional and have been suppressed.  ",
            "Edit `tokens/sync-ignore.json` to manage this list.",
            "",
            "| Token | Reason |",
            "|---|---|",
        ]
        ignore_data = load_json(ignore_path) if ignore_path and ignore_path.exists() else {}
        ignore_map  = {e["path"]: e.get("reason", "—") for e in ignore_data.get("ignore_changes", [])}
        for p in sorted(ignored_changes):
            local = p.split(".", 1)[1] if "." in p else p
            reason = (ignore_map.get(p) or ignore_map.get(local) or "—").replace("|", "\\|")
            lines.append(f"| `{p}` | {reason} |")
        lines += ["", "---", ""]

    # Section 3 — Design-only
    lines += [
        f"## 🔵 Design-only Tokens — not in production ({len(design_only)})",
        "",
        "These tokens exist only in the design files (e.g. custom Figma helpers).  ",
        "They are untouched.",
        "",
    ]

    if design_only:
        lines.append("| Token | Type | Value |")
        lines.append("|---|---|---|")
        for path, tok in sorted(design_only.items()):
            val = str(tok.get("value", "")).replace("|", "\\|").replace("\n", " ")
            typ = tok.get("type", "—")
            lines.append(f"| `{path}` | {typ} | `{val}` |")
        lines.append("")
    else:
        lines += ["_No design-only tokens._", ""]

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # ── Console summary ──────────────────────────────────────────────────────
    print(f"\n✅  Set files updated  : {files_written if files_written else 'none (already in sync)'}")
    print(f"📄  Diff report        → {report_path}")
    print(f"")
    print(f"   🆕 Missing tokens added : {len(missing)}")
    print(f"   ⚠️  Changed (value/type) : {len(changed)}")
    if ignored_changes:
        print(f"   🚫 Changes ignored       : {len(ignored_changes)}")
    print(f"   🔵 Design-only tokens   : {len(design_only)}")

    if changed:
        print(f"\n⚠️  Changed values/types detected — see {report_path}")

    return len(missing), len(changed)


# ─── CLI ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Merge & diff design token files (split format).")
    parser.add_argument("--design-dir", required=True,
                        help="Path to the tokens directory (contains set files + $metadata.json)")
    parser.add_argument("--prod",       required=True,
                        help="Path to the production token JSON (single file)")
    parser.add_argument("--ignore",     default="tokens/sync-ignore.json",
                        help="Path to sync-ignore.json (default: tokens/sync-ignore.json)")
    args = parser.parse_args()

    _, changed_count = run(
        design_dir  = Path(args.design_dir),
        prod_path   = Path(args.prod),
        ignore_path = Path(args.ignore),
    )

    if changed_count > 0:
        sys.exit(2)


if __name__ == "__main__":
    main()
