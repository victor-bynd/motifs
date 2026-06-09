# Token Diff Report

**Generated:** 2026-06-08 23:53 UTC  
**Design dir:** `tokens`  
**Production file:** `production.json`

---

## Summary

| | Count |
|---|---|
| 🆕 Missing tokens (added to set files) | **7** |
| ⚠️ Changed values (review needed) | **2** |
| 🚫 Ignored changes (sync-ignore.json) | **0** |
| 🔵 Design-only tokens (not in production) | **4** |

---

## 🆕 Missing Tokens — added to set files (7)

These tokens exist in the production file but were absent from the design files.  
They have been automatically added to the corresponding set file.

### `Snap Motif/Primary`

#### Accordion

| Token | Type | Value |
|---|---|---|
| `--accordion-header-divider-border-color` | color | `{Neutral.--neutral-v500}` |
| `--accordion-item-icon-color` | color | `{Neutral.--neutral-v700}` |
| `--accordion-item-icon-inset` | spacing | `{Root.--spacing-m}` |

### `Snap Motif/Quaternary`

#### Accordion

| Token | Type | Value |
|---|---|---|
| `--accordion-header-divider-border-color` | color | `{Neutral.--neutral-v300}` |

### `Snap Motif/Secondary`

#### Accordion

| Token | Type | Value |
|---|---|---|
| `--accordion-header-divider-border-color` | color | `{Neutral.--neutral-v300}` |
| `--accordion-item-icon-color` | color | `{Neutral.--neutral-v0}` |

### `Snap Motif/Tertiary`

#### Accordion

| Token | Type | Value |
|---|---|---|
| `--accordion-header-divider-border-color` | color | `{Neutral.--neutral-v250}` |

---

## ⚠️ Changed Values — review required (2)

These tokens exist in both files but the production value differs from the design file.  
**The design file value is kept.** Review each one and update manually if needed.

### `Snap Motif/Global`

| Token | Type | Design value | Production value |
|---|---|---|---|
| `Root.--h1-font-family` | fontFamilies | `Program Nar OT, Helvetica, Tahoma, Arial, sans-serif` | `Program OT, Helvetica Heading, Tahoma Heading, Arial, sans-serif` |
| `Root.--h2-font-family` | fontFamilies | `Program Nar OT, Helvetica, Tahoma, Arial, sans-serif` | `Program OT, Helvetica Heading, Tahoma Heading, Arial, sans-serif` |

---

## 🔵 Design-only Tokens — not in production (4)

These tokens exist only in the design files (e.g. custom Figma helpers).  
They are untouched.

| Token | Type | Value |
|---|---|---|
| `Snap Motif/Global.Root.--border-radius-none` | borderRadius | `0px` |
| `Snap Motif/Global.Root.--spacing-none` | spacing | `0px` |
| `Snap Motif/Primary.Root.bg-gradient-transparent` | color | `rgba( {Root.--bg-color}, 0)` |
| `Snap Motif/Primary.Root.gradient-transparency` | color | `linear-gradient(270deg, {Root.--bg-color} 0%, {Root.bg-gradient-transparent} 100%)` |
