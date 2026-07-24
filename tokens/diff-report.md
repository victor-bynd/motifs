# Token Diff Report

**Generated:** 2026-07-24 19:56 UTC  
**Design dir:** `tokens`  
**Production file:** `Motifs-Storybook/figmaTokens.default-motif.2026-07-24T18_04_52.732Z.json`

---

## Summary

| | Count |
|---|---|
| 🆕 Missing tokens (added to set files) | **8** |
| ⚠️ Changed values (review needed) | **2** |
| 🚫 Ignored changes (sync-ignore.json) | **0** |
| 🔵 Design-only tokens (not in production) | **12** |

---

## 🆕 Missing Tokens — added to set files (8)

These tokens exist in the production file but were absent from the design files.  
They have been automatically added to the corresponding set file.

### `Snap Motif/Primary`

#### Code

| Token | Type | Value |
|---|---|---|
| `--code-border-radius` | borderRadius | `{Root.--border-radius-l}` |

#### Content

| Token | Type | Value |
|---|---|---|
| `--content-border-radius` | borderRadius | `{Root.--border-radius-l}` |

#### Definition

| Token | Type | Value |
|---|---|---|
| `--definition-border-radius` | borderRadius | `{Root.--border-radius-s}` |

#### Icon Button

| Token | Type | Value |
|---|---|---|
| `--icon-button-border-radius` | borderRadius | `50%` |

#### Quote

| Token | Type | Value |
|---|---|---|
| `--quote-border-radius` | borderRadius | `{Root.--border-radius-l}` |
| `--quote-media-rotate` | number | `2` |

#### Side Overlay

| Token | Type | Value |
|---|---|---|
| `--side-overlay-desktop-border-radius` | borderRadius | `{Root.--border-radius-l}` |
| `--side-overlay-mobile-border-radius` | borderRadius | `{Root.--border-radius-l} {Root.--border-radius-l} 0 0` |

---

## ⚠️ Changed Values — review required (2)

These tokens exist in both files but the **value and/or type** differs between production and design.  
**The design file value/type is kept.** Review each one and update manually if needed.

The **Changed** column shows whether it's the `value`, the `type`, or both that differ.

### `Snap Motif/Global`

| Token | Changed | Design value | Production value | Design type | Production type |
|---|---|---|---|---|---|
| `Root.--h1-font-family` | value | `Program Nar OT, Helvetica, Tahoma, Arial, sans-serif` | `Program OT, Helvetica Heading, Tahoma Heading, Arial, sans-serif` | `fontFamilies` | `fontFamilies` |
| `Root.--h2-font-family` | value | `Program Nar OT, Helvetica, Tahoma, Arial, sans-serif` | `Program OT, Helvetica Heading, Tahoma Heading, Arial, sans-serif` | `fontFamilies` | `fontFamilies` |

---

## 🔵 Design-only Tokens — not in production (12)

These tokens exist only in the design files (e.g. custom Figma helpers).  
They are untouched.

| Token | Type | Value |
|---|---|---|
| `Snap Motif/Global.Root.--border-radius-none` | borderRadius | `0px` |
| `Snap Motif/Global.Root.--spacing-none` | spacing | `0px` |
| `Snap Motif/Primary.Animated Accordion.--animated-accordion-progress-indicator-color` | color | `{Root.--fg-color}` |
| `Snap Motif/Primary.Dropdown Menu.--dropdown-menu-divider-color` | color | `transparent` |
| `Snap Motif/Primary.Dropdown Menu.--dropdown-menu-divider-width` | sizing | `0` |
| `Snap Motif/Primary.Quote.--quote-icon-color` | color | `{Neutral.--neutral-v700}` |
| `Snap Motif/Primary.Root.bg-gradient-transparent` | color | `rgba( {Root.--bg-color}, 0)` |
| `Snap Motif/Primary.Root.gradient-transparency` | color | `linear-gradient(270deg, {Root.--bg-color} 0%, {Root.bg-gradient-transparent} 100%)` |
| `Snap Motif/Primary.Tooltip.--tooltip-line-height` | sizing | `22px` |
| `Snap Motif/Secondary.Animated Accordion.--animated-accordion-progress-indicator-color` | color | `{Primary.--primary-v100}` |
| `Snap Motif/Secondary.Quote.--quote-icon-color` | color | `{Primary.--primary-v100}` |
| `Snap Motif/Tertiary.Quote.--quote-icon-color` | color | `{Primary.--primary-v100}` |
