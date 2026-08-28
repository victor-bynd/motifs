# Token Diff Report

**Generated:** 2026-08-28 15:51 UTC  
**Design dir:** `tokens`  
**Production file:** `Motifs-Storybook/Figma Tokens - Motif.2026-08-28T15_48_26.201Z.json`

---

## Summary

| | Count |
|---|---|
| 🆕 Missing tokens (added to set files) | **0** |
| ⚠️ Changed values (review needed) | **9** |
| 🚫 Ignored changes (sync-ignore.json) | **0** |
| 🔵 Design-only tokens (not in production) | **12** |

---

## 🆕 Missing Tokens — added to set files (0)

These tokens exist in the production file but were absent from the design files.  
They have been automatically added to the corresponding set file.

_No missing tokens._

---

## ⚠️ Changed Values — review required (9)

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
| `Autocomplete.--autocomplete-list-border-radius` | value | `{Root.--spacing-s}` | `{Root.--border-radius-s}` | `borderRadius` | `borderRadius` |
| `Carousel.--carousel-card-bg-color` | value | `{Palette.Plain.--palette-plain-transparent}` | `transparent` | `color` | `color` |
| `Carousel.--carousel-card-desktop-text-padding` | value | `{Root.--spacing-m} 0px` | `{Root.--spacing-m} 0` | `spacing` | `spacing` |
| `Carousel.--carousel-card-hover-bg-color` | value | `{Palette.Plain.--palette-plain-transparent}` | `transparent` | `color` | `color` |
| `Carousel.--carousel-card-mobile-text-padding` | value | `{Root.--spacing-m} 0px` | `{Root.--spacing-m} 0` | `spacing` | `spacing` |
| `Form.--form-input-desktop-font-line-height` | value | `normal` | `20px` | `lineHeights` | `lineHeights` |

### `Snap Motif/Secondary`

| Token | Changed | Design value | Production value | Design type | Production type |
|---|---|---|---|---|---|
| `Dropdown Menu.--dropdown-menu-border-color` | value | `{Neutral.--neutral-v0}` | `{Neutral.--neutral-v500}` | `color` | `color` |

---

## 🔵 Design-only Tokens — not in production (12)

These tokens exist only in the design files (e.g. custom Figma helpers).  
They are untouched.

| Token | Type | Value |
|---|---|---|
| `Snap Motif/Global.Root.--border-radius-none` | borderRadius | `0px` |
| `Snap Motif/Global.Root.--spacing-none` | spacing | `0px` |
| `Snap Motif/Primary.Quote.--quote-card-left-right-padding` | spacing | `{Root.--spacing-xl}` |
| `Snap Motif/Primary.Quote.--quote-icon-color` | color | `{Neutral.--neutral-v700}` |
| `Snap Motif/Primary.Root.bg-gradient-transparent` | color | `rgba( {Root.--bg-color}, 0)` |
| `Snap Motif/Primary.Root.gradient-transparency` | color | `linear-gradient(270deg, {Root.--bg-color} 0%, {Root.bg-gradient-transparent} 100%)` |
| `Snap Motif/Primary.Stats.--stats-stat-font-line-height` | lineHeights | `{Root.--stats-font-line-height}` |
| `Snap Motif/Primary.Stats.--stats-stat-font-size` | fontSizes | `{Root.--stats-font-size}` |
| `Snap Motif/Primary.Stats.--stats-stat-font-weight` | fontWeights | `{Root.--stats-font-weight}` |
| `Snap Motif/Secondary.Quote.--quote-icon-color` | color | `{Primary.--primary-v100}` |
| `Snap Motif/Secondary.Stats.--stats-stat-color` | color | `{Primary.--primary-v100}` |
| `Snap Motif/Tertiary.Quote.--quote-icon-color` | color | `{Primary.--primary-v100}` |
