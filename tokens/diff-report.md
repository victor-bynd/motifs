# Token Diff Report

**Generated:** 2026-08-12 21:40 UTC  
**Design dir:** `tokens`  
**Production file:** `Motifs-Storybook/Figma Tokens - Motif.2026-08-12T21_33_33.227Z.json`

---

## Summary

| | Count |
|---|---|
| 🆕 Missing tokens (added to set files) | **40** |
| ⚠️ Changed values (review needed) | **5** |
| 🚫 Ignored changes (sync-ignore.json) | **0** |
| 🔵 Design-only tokens (not in production) | **24** |

---

## 🆕 Missing Tokens — added to set files (40)

These tokens exist in the production file but were absent from the design files.  
They have been automatically added to the corresponding set file.

### `Snap Motif/Primary`

#### Autocomplete

| Token | Type | Value |
|---|---|---|
| `--autocomplete-input-border-radius` | borderRadius | `{Root.--border-radius-l}` |
| `--autocomplete-input-height` | sizing | `52px` |
| `--autocomplete-list-border-radius` | borderRadius | `{Root.--spacing-s}` |

#### Bar Chart

| Token | Type | Value |
|---|---|---|
| `--bar-chart-border-radius` | borderRadius | `40px` |
| `--bar-chart-filter-border-radius` | borderRadius | `{Root.--border-radius-s}` |
| `--bar-chart-tooltip-border-color` | color | `transparent` |
| `--bar-chart-tooltip-border-radius` | borderRadius | `{Root.--border-radius-s}` |
| `--bar-chart-tooltip-box-shadow` | boxShadow | `{'type': 'dropShadow', 'x': '0', 'y': '1px', 'blur': '2px', 'spread': '0', 'color': 'rgba(83, 87, 91, 1)'}` |

#### Carousel

| Token | Type | Value |
|---|---|---|
| `--carousel-card-body-color` | color | `{Neutral.--neutral-v700}` |
| `--carousel-dot-border-radius` | borderRadius | `100px` |
| `--carousel-text-item-bg-color` | color | `{Neutral.--neutral-v0}` |
| `--carousel-text-item-box-shadow` | boxShadow | `{'type': 'dropShadow', 'x': '0', 'y': '0', 'blur': '32px', 'spread': '0', 'color': 'rgba(0, 0, 0, 0.12)'}` |
| `--carousel-text-item-sub-text-color` | color | `{Neutral.--neutral-v700}` |

#### Chart Skeleton

| Token | Type | Value |
|---|---|---|
| `--chart-skeleton-border-radius` | borderRadius | `{Root.--border-radius-xl}` |

#### Footnote

| Token | Type | Value |
|---|---|---|
| `--footnote-icon-hover-bg-color` | color | `{Neutral.--neutral-v200}` |

#### Icon Button

| Token | Type | Value |
|---|---|---|
| `--icon-button-box-shadow` | boxShadow | `{Root.--box-shadow-xs}` |

#### Multi Select

| Token | Type | Value |
|---|---|---|
| `--multi-select-border-color` | color | `transparent` |
| `--multi-select-border-radius` | borderRadius | `0 0 {Root.--border-radius-s} {Root.--border-radius-s}` |
| `--multi-select-box-shadow` | boxShadow | `{Root.--box-shadow-l}` |
| `--multi-select-chip-border-radius` | borderRadius | `11px` |
| `--multi-select-chip-fg-color` | color | `{Neutral.--neutral-v700}` |
| `--multi-select-chip-margin` | spacing | `5px` |
| `--multi-select-min-height` | sizing | `50px` |
| `--multi-select-option-border-radius` | borderRadius | `5px` |
| `--multi-select-option-padding` | spacing | `10px {Root.--spacing-m}` |
| `--multi-select-padding` | spacing | `0 {Root.--spacing-xxl} 0 {Root.--spacing-xs}` |

#### Quote

| Token | Type | Value |
|---|---|---|
| `--quote-card-desktop-padding` | spacing | `{Root.--spacing-xl}` |
| `--quote-card-mobile-padding` | spacing | `{Root.--spacing-l}` |
| `--quote-desktop-gap` | spacing | `0px` |
| `--quote-media-border-radius` | borderRadius | `{Root.--border-radius-xl}` |
| `--quote-media-desktop-translate-x` | spacing | `8px` |
| `--quote-media-mobile-translate-y` | spacing | `16px` |
| `--quote-mobile-gap` | spacing | `0px` |

#### Stats

| Token | Type | Value |
|---|---|---|
| `--stats-color` | color | `{Root.--fg-color}` |

### `Snap Motif/Secondary`

#### Carousel

| Token | Type | Value |
|---|---|---|
| `--carousel-card-body-color` | color | `{Neutral.--neutral-v0}` |
| `--carousel-text-item-bg-color` | color | `{Neutral.--neutral-v625}` |
| `--carousel-text-item-sub-text-color` | color | `{Neutral.--neutral-v0}` |

#### Footnote

| Token | Type | Value |
|---|---|---|
| `--footnote-icon-hover-bg-color` | color | `{Neutral.--neutral-v600}` |

#### Multi Select

| Token | Type | Value |
|---|---|---|
| `--multi-select-chip-fg-color` | color | `{Neutral.--neutral-v0}` |

#### Stats

| Token | Type | Value |
|---|---|---|
| `--stats-color` | color | `{Primary.--primary-v100}` |

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

## 🔵 Design-only Tokens — not in production (24)

These tokens exist only in the design files (e.g. custom Figma helpers).  
They are untouched.

| Token | Type | Value |
|---|---|---|
| `Snap Motif/Global.Root.--border-radius-none` | borderRadius | `0px` |
| `Snap Motif/Global.Root.--spacing-none` | spacing | `0px` |
| `Snap Motif/Primary.Dropdown Menu.--dropdown-menu-divider-color` | color | `transparent` |
| `Snap Motif/Primary.Dropdown Menu.--dropdown-menu-divider-width` | sizing | `0` |
| `Snap Motif/Primary.Footnote.--footnote-hover-icon-bg-color` | color | `{Neutral.--neutral-v200}` |
| `Snap Motif/Primary.Modal.--modal-close-bg-color` | color | `{Neutral.--neutral-v700}` |
| `Snap Motif/Primary.Modal.--modal-close-fg-color` | color | `{Neutral.--neutral-v0}` |
| `Snap Motif/Primary.Quote.--quote-card-left-right-padding` | spacing | `{Root.--spacing-xl}` |
| `Snap Motif/Primary.Quote.--quote-icon-color` | color | `{Neutral.--neutral-v700}` |
| `Snap Motif/Primary.Root.bg-gradient-transparent` | color | `rgba( {Root.--bg-color}, 0)` |
| `Snap Motif/Primary.Root.gradient-transparency` | color | `linear-gradient(270deg, {Root.--bg-color} 0%, {Root.bg-gradient-transparent} 100%)` |
| `Snap Motif/Primary.Stats.--stats-stat-color` | color | `{Root.--fg-color}` |
| `Snap Motif/Primary.Stats.--stats-stat-font-line-height` | lineHeights | `{Root.--stats-font-line-height}` |
| `Snap Motif/Primary.Stats.--stats-stat-font-size` | fontSizes | `{Root.--stats-font-size}` |
| `Snap Motif/Primary.Stats.--stats-stat-font-weight` | fontWeights | `{Root.--stats-font-weight}` |
| `Snap Motif/Primary.Stats.--stats-stat-supplementary-text-font-size` | fontSizes | `{Root.--stats-supplementary-text-font-size}` |
| `Snap Motif/Primary.Stats.--stats-stat-supplementary-text-font-weight` | fontWeights | `{Root.--stats-supplementary-text-font-weight}` |
| `Snap Motif/Secondary.Animated Accordion.--animated-accordion-progress-indicator-color` | color | `{Primary.--primary-v100}` |
| `Snap Motif/Secondary.Footnote.--footnote-hover-icon-bg-color` | color | `{Neutral.--neutral-v600}` |
| `Snap Motif/Secondary.Modal.--modal-close-bg-color` | color | `{Neutral.--neutral-v0}` |
| `Snap Motif/Secondary.Modal.--modal-close-fg-color` | color | `{Neutral.--neutral-v700}` |
| `Snap Motif/Secondary.Quote.--quote-icon-color` | color | `{Primary.--primary-v100}` |
| `Snap Motif/Secondary.Stats.--stats-stat-color` | color | `{Primary.--primary-v100}` |
| `Snap Motif/Tertiary.Quote.--quote-icon-color` | color | `{Primary.--primary-v100}` |
