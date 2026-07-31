# Token Diff Report

**Generated:** 2026-07-30 21:54 UTC  
**Design dir:** `tokens`  
**Production file:** `Motifs-Storybook/Figma Tokens - Motif.2026-07-30T18_26_14.691Z.json`

---

## Summary

| | Count |
|---|---|
| 🆕 Missing tokens (added to set files) | **12** |
| ⚠️ Changed values (review needed) | **5** |
| 🚫 Ignored changes (sync-ignore.json) | **0** |
| 🔵 Design-only tokens (not in production) | **14** |

---

## 🆕 Missing Tokens — added to set files (12)

These tokens exist in the production file but were absent from the design files.  
They have been automatically added to the corresponding set file.

### `Snap Motif/Primary`

#### Accordion

| Token | Type | Value |
|---|---|---|
| `--accordion-item-body-link-color` | color | `{Root.--action-text-default-color}` |
| `--accordion-item-body-link-font-weight` | fontWeights | `{Root.--action-desktop-font-weight}` |
| `--accordion-item-body-link-hover-color` | color | `{Root.--action-text-hover-color}` |

#### Dropdown Menu

| Token | Type | Value |
|---|---|---|
| `--dropdown-button-padding` | spacing | `{Root.--spacing-s} {Root.--spacing-m}` |
| `--dropdown-desktop-font-line-height` | lineHeights | `{Root.--action-desktop-font-line-height}` |
| `--dropdown-desktop-font-size` | fontSizes | `{Root.--action-desktop-font-size}` |
| `--dropdown-mobile-font-line-height` | lineHeights | `{Root.--action-mobile-font-line-height}` |
| `--dropdown-mobile-font-size` | fontSizes | `{Root.--action-mobile-font-size}` |

#### Form

| Token | Type | Value |
|---|---|---|
| `--form-input-height` | sizing | `52px` |
| `--form-input-selection-control-active-color` | color | `{Palette.Plain.--palette-plain-white}` |
| `--form-input-selection-control-border-width` | borderWidth | `2px` |

#### Modal

| Token | Type | Value |
|---|---|---|
| `--modal-border-radius` | borderRadius | `{Root.--border-radius-l}` |

---

## ⚠️ Changed Values — review required (5)

These tokens exist in both files but the **value and/or type** differs between production and design.  
**The design file value/type is kept.** Review each one and update manually if needed.

The **Changed** column shows whether it's the `value`, the `type`, or both that differ.

### `Snap Motif/Global`

| Token | Changed | Design value | Production value | Design type | Production type |
|---|---|---|---|---|---|
| `Root.--h1-font-family` | value | `Program Nar OT, Helvetica, Tahoma, Arial, sans-serif` | `Program OT, Helvetica Heading, Tahoma Heading, Arial, sans-serif` | `fontFamilies` | `fontFamilies` |
| `Root.--h2-font-family` | value | `Program Nar OT, Helvetica, Tahoma, Arial, sans-serif` | `Program OT, Helvetica Heading, Tahoma Heading, Arial, sans-serif` | `fontFamilies` | `fontFamilies` |

### `Snap Motif/Primary`

| Token | Changed | Design value | Production value | Design type | Production type |
|---|---|---|---|---|---|
| `Dropdown Menu.--dropdown-item-padding` | value | `{Root.--spacing-m}` | `{Root.--spacing-xs} {Root.--spacing-m}` | `spacing` | `spacing` |
| `Form.--form-input-desktop-font-line-height` | value | `normal` | `20px` | `lineHeights` | `lineHeights` |

### `Snap Motif/Secondary`

| Token | Changed | Design value | Production value | Design type | Production type |
|---|---|---|---|---|---|
| `Dropdown Menu.--dropdown-menu-border-color` | value | `{Neutral.--neutral-v0}` | `{Neutral.--neutral-v500}` | `color` | `color` |

---

## 🔵 Design-only Tokens — not in production (14)

These tokens exist only in the design files (e.g. custom Figma helpers).  
They are untouched.

| Token | Type | Value |
|---|---|---|
| `Snap Motif/Global.Root.--border-radius-none` | borderRadius | `0px` |
| `Snap Motif/Global.Root.--spacing-none` | spacing | `0px` |
| `Snap Motif/Primary.Dropdown Menu.--dropdown-menu-divider-color` | color | `transparent` |
| `Snap Motif/Primary.Dropdown Menu.--dropdown-menu-divider-width` | sizing | `0` |
| `Snap Motif/Primary.Modal.--modal-close-bg-color` | color | `{Neutral.--neutral-v700}` |
| `Snap Motif/Primary.Modal.--modal-close-fg-color` | color | `{Neutral.--neutral-v0}` |
| `Snap Motif/Primary.Quote.--quote-icon-color` | color | `{Neutral.--neutral-v700}` |
| `Snap Motif/Primary.Root.bg-gradient-transparent` | color | `rgba( {Root.--bg-color}, 0)` |
| `Snap Motif/Primary.Root.gradient-transparency` | color | `linear-gradient(270deg, {Root.--bg-color} 0%, {Root.bg-gradient-transparent} 100%)` |
| `Snap Motif/Secondary.Animated Accordion.--animated-accordion-progress-indicator-color` | color | `{Primary.--primary-v100}` |
| `Snap Motif/Secondary.Modal.--modal-close-bg-color` | color | `{Neutral.--neutral-v0}` |
| `Snap Motif/Secondary.Modal.--modal-close-fg-color` | color | `{Neutral.--neutral-v700}` |
| `Snap Motif/Secondary.Quote.--quote-icon-color` | color | `{Primary.--primary-v100}` |
| `Snap Motif/Tertiary.Quote.--quote-icon-color` | color | `{Primary.--primary-v100}` |
