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

Behavior:
  - New tokens found only in production are ADDED to the design files.
  - Tokens with a different value and/or type are OVERWRITTEN with
    production's value/type — production always wins. The design file
    stays in sync with code; nothing is left for manual merging.

Ignore list:
  tokens/sync-ignore.json — informational only. A path listed here still
  gets synced from production like everything else; it's just flagged with
  its reason in the diff report, in case you want to revisit it later.

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


def deep_merge(base: dict, overlay: dict):
    """Recursively merge overlay into base, in place."""
    for k, v in overlay.items():
        if k in base and isinstance(base[k], dict) and isinstance(v, dict):
            deep_merge(base[k], v)
        else:
            base[k] = v


def load_ignore_map(path: Path) -> dict:
    """
    Load tokens/sync-ignore.json as { path: reason }.
    Supports both the full "Set/Name.Root.token" format and the
    local "Root.token" format (set-prefix stripped), same as before.
    This is informational only — it no longer blocks auto-apply.
    """
    if not path or not path.exists():
        return {}
    data = load_json(path)
    entries = data.get("ignore_changes", [])
    reasons = {}
    for e in entries:
        p = e.get("path", "")
        reason = e.get("reason", "—")
        if "/" in p:
            local = p.split(".", 1)[1] if "." in p else p
            reasons[local] = reason
        reasons[p] = reason
    if reasons:
        print(f"ℹ️   sync-ignore.json loaded ({len(set(reasons.values()))} reasons) from {path} "
              f"— informational only, does not block auto-apply")
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
    ignore_map  = load_ignore_map(ignore_path)  # informational only now

    # ── 1. Missing: in prod but not in design ────────────────────────────────
    missing: dict[str, dict] = {
        k: v for k, v in prod_flat.items() if k not in design_flat
    }

    # ── 2. Changed: exist in both but value and/or type differs ─────────────
    # NOTE: production always wins here — these get written back into the
    # design set files below, even if the path matches sync-ignore.json.
    # The ignore list is kept purely so the report can flag "this one was on
    # your ignore list, applied anyway" for visibility.
    changed: dict[str, dict] = {}
    ignored_but_applied: list[str] = []

    for path, prod_token in prod_flat.items():
        if path not in design_flat:
            continue
        reasons = token_diff_reasons(design_flat[path], prod_token)
        if not reasons:
            continue
        local_path = path.split(".", 1)[1] if "." in path else path
        ignore_reason = ignore_map.get(path) or ignore_map.get(local_path)
        if ignore_reason is not None:
            ignored_but_applied.append(path)
        changed[path] = {
            "design_value":  design_flat[path].get("value"),
            "prod_value":    prod_token.get("value"),
            "design_type":   design_flat[path].get("type", ""),
            "prod_type":     prod_token.get("type", ""),
            "reasons":       reasons,
            "ignore_reason": ignore_reason,  # None unless it matched sync-ignore.json
        }

    # ── 3. Design-only: in design but not in prod ────────────────────────────
    design_only: dict[str, dict] = {
        k: v for k, v in design_flat.items() if k not in prod_flat
    }

    # ── Apply missing additions + changed overwrites, then write files ───────
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

    sets_to_save: set = set()

    # 3a. Merge in brand-new tokens
    for set_name in TOKEN_SETS:
        additions = missing_by_set.get(set_name, {})
        if additions:
            deep_merge(design_sets[set_name], additions)
            sets_to_save.add(set_name)

    # 3b. Overwrite value/type on existing tokens with production's values
    for full_path, info in changed.items():
        set_name = next((s for s in TOKEN_SETS if full_path.startswith(s + ".")), None)
        if set_name is None:
            print(f"⚠️  Could not match set for changed path: {full_path} — skipping apply")
            continue
        local_keys = full_path[len(set_name) + 1:].split(".")
        try:
            node = design_sets[set_name]
            for k in local_keys[:-1]:
                node = node[k]
            node[local_keys[-1]]["value"] = info["prod_value"]
            node[local_keys[-1]]["type"]  = info["prod_type"]
        except (KeyError, TypeError):
            print(f"⚠️  Could not apply change for path: {full_path} — structure mismatch, skipping")
            continue
        sets_to_save.add(set_name)

    # 3c. Clean + save every touched set file
    files_written = []
    for set_name in TOKEN_SETS:
        if set_name not in sets_to_save:
            continue

        file_path = design_dir / f"{set_name}.json"
        set_data  = design_sets[set_name]

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
        f"| 🔄 Values/types synced from production | **{len(changed)}** |",
        f"| 🚫 Synced despite matching sync-ignore.json | **{len(ignored_but_applied)}** |",
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

    # Section 2 — Changed (now auto-applied)
    lines += [
        f"## 🔄 Values & Types Synced from Production ({len(changed)})",
        "",
        "These tokens existed in both files but the **value and/or type** differed.  ",
        "**Production's value/type has been applied to the design file automatically** — "
        "no manual action needed. The columns below show what changed, for your records.",
        "",
        "The **Changed** column shows whether it was the `value`, the `type`, or both. "
        "The **Note** column flags entries that matched `sync-ignore.json` — these were "
        "**still synced**; the ignore list is informational only and no longer blocks syncing.",
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
            lines.append("| Token | Changed | Previous (design) value | New (production) value | Previous (design) type | New (production) type | Note |")
            lines.append("|---|---|---|---|---|---|---|")
            for path, info in sorted(tokens):
                token_name = path[len(set_name) + 1:]
                dv  = str(info["design_value"]).replace("|", "\\|").replace("\n", " ")
                pv  = str(info["prod_value"]).replace("|", "\\|").replace("\n", " ")
                dt  = info["design_type"] or "—"
                pt  = info["prod_type"] or "—"
                changed_label = " + ".join(info["reasons"])
                note = f"⚠️ matched sync-ignore.json: {info['ignore_reason']}" if info.get("ignore_reason") else "—"
                note = note.replace("|", "\\|")
                lines.append(f"| `{token_name}` | {changed_label} | `{dv}` | `{pv}` | `{dt}` | `{pt}` | {note} |")
            lines.append("")
    else:
        lines += ["_No value or type changes detected._", ""]

    lines += ["---", ""]

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
    print(f"   🆕 Missing tokens added      : {len(missing)}")
    print(f"   🔄 Values/types synced       : {len(changed)}")
    if ignored_but_applied:
        print(f"   🚫 (of those) on ignore list : {len(ignored_but_applied)} — synced anyway, see report")
    print(f"   🔵 Design-only tokens        : {len(design_only)}")

    if changed:
        print(f"\n🔄  Values/types synced from production — see {report_path}")

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
