# Token Diff Report

**Generated:** 2026-06-03 23:26 UTC  
**Design dir:** `tokens`  
**Production file:** `production.json`

---

## Summary

| | Count |
|---|---|
| 🆕 Missing tokens (added to set files) | **1** |
| ⚠️ Changed values (review needed) | **8** |
| 🚫 Ignored changes (sync-ignore.json) | **0** |
| 🔵 Design-only tokens (not in production) | **4** |

---

## 🆕 Missing Tokens — added to set files (1)

These tokens exist in the production file but were absent from the design files.  
They have been automatically added to the corresponding set file.

### `Snap Motif/Primary`

#### Header

| Token | Type | Value |
|---|---|---|
| `--global-header-menu-featured-item-border-radius` | borderRadius | `{Root.--border-radius-m}` |

---

## ⚠️ Changed Values — review required (8)

These tokens exist in both files but the production value differs from the design file.  
**The design file value is kept.** Review each one and update manually if needed.

### `Snap Motif/Global`

| Token | Type | Design value | Production value |
|---|---|---|---|
| `Root.--h1-desktop-font-line-height-compact` | sizing | `95px` | `108%` |
| `Root.--h1-font-family` | fontFamilies | `Program Nar OT, Helvetica, Tahoma, Arial, sans-serif` | `Program OT, Helvetica Heading, Tahoma Heading, Arial, sans-serif` |
| `Root.--h2-font-family` | fontFamilies | `Program Nar OT, Helvetica, Tahoma, Arial, sans-serif` | `Program OT, Helvetica Heading, Tahoma Heading, Arial, sans-serif` |

### `Snap Motif/Primary`

| Token | Type | Design value | Production value |
|---|---|---|---|
| `Banner.--banner-bg-color` | color | `{Root.--bg-color}` | `{Primary.--primary-v100}` |
| `Footer.--footer-bar-bg-color` | color | `{Root.--bg-color}` | `{Primary.--primary-v100}` |
| `Footer.--footer-bg-color` | color | `{Root.--bg-color}` | `{Primary.--primary-v100}` |
| `Header.--global-header-bg-color` | color | `{Root.--bg-color}` | `{Primary.--primary-v100}` |
| `Quote.--quote-icon-color` | color | `{Primary.--primary-v100}` | `{Neutral.--neutral-v700}` |

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
