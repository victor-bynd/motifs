# Token Diff Report

**Generated:** 2026-08-14 22:37 UTC  
**Design dir:** `tokens`  
**Production file:** `Motifs-Storybook/Figma Tokens - Motif.2026-08-14T22_33_58.141Z.json`

---

## Summary

| | Count |
|---|---|
| 🆕 Missing tokens (added to set files) | **12** |
| ⚠️ Changed values (review needed) | **4** |
| 🚫 Ignored changes (sync-ignore.json) | **0** |
| 🔵 Design-only tokens (not in production) | **23** |

---

## 🆕 Missing Tokens — added to set files (12)

These tokens exist in the production file but were absent from the design files.  
They have been automatically added to the corresponding set file.

### `Snap Motif/Primary`

#### Editorial Gallery Card

| Token | Type | Value |
|---|---|---|
| `--editorial-gallery-card-media-border-radius` | borderRadius | `{Root.--border-radius-l}` |
| `--editorial-gallery-card-media-hover-box-shadow` | boxShadow | `{'type': 'dropShadow', 'x': '0', 'y': '4px', 'blur': '8px', 'spread': '0', 'color': 'rgba(0, 0, 0, 0.12)'}` |
| `--editorial-gallery-card-title-desktop-font-line-height` | lineHeights | `{Root.--h5-desktop-font-line-height}` |
| `--editorial-gallery-card-title-desktop-font-size` | fontSizes | `{Root.--h5-desktop-font-size}` |
| `--editorial-gallery-card-title-desktop-font-weight` | fontWeights | `{Root.--h5-desktop-font-weight}` |
| `--editorial-gallery-card-title-mobile-font-line-height` | lineHeights | `{Root.--h5-mobile-font-line-height}` |
| `--editorial-gallery-card-title-mobile-font-size` | fontSizes | `{Root.--h5-mobile-font-size}` |
| `--editorial-gallery-card-title-mobile-font-weight` | fontWeights | `{Root.--h5-mobile-font-weight}` |

#### Multi Value Prop Block

| Token | Type | Value |
|---|---|---|
| `--multi-value-prop-block-stat-desktop-font-line-height` | lineHeights | `{Root.--h3-desktop-font-line-height}` |
| `--multi-value-prop-block-stat-desktop-font-size` | fontSizes | `{Root.--h3-desktop-font-size}` |
| `--multi-value-prop-block-stat-mobile-font-line-height` | lineHeights | `{Root.--h3-mobile-font-line-height}` |
| `--multi-value-prop-block-stat-mobile-font-size` | fontSizes | `{Root.--h3-mobile-font-size}` |

---

## ⚠️ Changed Values — review required (4)

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
| `Form.--form-input-desktop-font-line-height` | value | `normal` | `20px` | `lineHeights` | `lineHeights` |

### `Snap Motif/Secondary`

| Token | Changed | Design value | Production value | Design type | Production type |
|---|---|---|---|---|---|
| `Dropdown Menu.--dropdown-menu-border-color` | value | `{Neutral.--neutral-v0}` | `{Neutral.--neutral-v500}` | `color` | `color` |

---

## 🔵 Design-only Tokens — not in production (23)

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
