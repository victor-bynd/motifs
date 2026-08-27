# Token Diff Report

**Generated:** 2026-08-27 16:53 UTC  
**Design dir:** `tokens`  
**Production file:** `Motifs-Storybook/Figma Tokens - Motif.2026-08-27T16_51_46.970Z.json`

---

## Summary

| | Count |
|---|---|
| 🆕 Missing tokens (added to set files) | **6** |
| ⚠️ Changed values (review needed) | **13** |
| 🚫 Ignored changes (sync-ignore.json) | **0** |
| 🔵 Design-only tokens (not in production) | **37** |

---

## 🆕 Missing Tokens — added to set files (6)

These tokens exist in the production file but were absent from the design files.  
They have been automatically added to the corresponding set file.

### `Snap Motif/Primary`

#### Button

| Token | Type | Value |
|---|---|---|
| `--persistent-cta-button-border-radius` | borderRadius | `{Root.--border-radius-s}` |

#### Carousel

| Token | Type | Value |
|---|---|---|
| `--carousel-card-single-view-landscape-max-width` | sizing | `480px` |
| `--carousel-card-single-view-portrait-max-width` | sizing | `256px` |
| `--carousel-text-item-border-radius` | borderRadius | `16px` |
| `--carousel-text-item-desktop-max-width` | sizing | `700px` |
| `--carousel-text-item-mobile-max-width` | sizing | `480px` |

---

## ⚠️ Changed Values — review required (13)

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
| `Carousel.--carousel-card-bg-color` | value | `{Neutral.--neutral-v0}` | `transparent` | `color` | `color` |
| `Carousel.--carousel-card-desktop-grid-gap` | value | `64px` | `{Root.--spacing-xl}` | `spacing` | `spacing` |
| `Carousel.--carousel-card-desktop-text-padding` | value | `{Root.--spacing-m}` | `{Root.--spacing-m} 0` | `spacing` | `spacing` |
| `Carousel.--carousel-card-hover-bg-color` | value | `{Neutral.--neutral-v0}` | `transparent` | `color` | `color` |
| `Carousel.--carousel-card-landscape-square-desktop-width` | value | `364px` | `396px` | `sizing` | `sizing` |
| `Carousel.--carousel-card-mobile-grid-gap` | value | `16px` | `{Root.--spacing-m}` | `spacing` | `spacing` |
| `Carousel.--carousel-card-mobile-text-padding` | value | `{Root.--spacing-m}` | `{Root.--spacing-m} 0` | `spacing` | `spacing` |
| `Carousel.--carousel-card-portrait-desktop-width` | value | `257px` | `288px` | `sizing` | `sizing` |
| `Carousel.--carousel-card-portrait-mobile-width` | value | `257px` | `311px` | `sizing` | `sizing` |
| `Form.--form-input-desktop-font-line-height` | value | `normal` | `20px` | `lineHeights` | `lineHeights` |

### `Snap Motif/Secondary`

| Token | Changed | Design value | Production value | Design type | Production type |
|---|---|---|---|---|---|
| `Dropdown Menu.--dropdown-menu-border-color` | value | `{Neutral.--neutral-v0}` | `{Neutral.--neutral-v500}` | `color` | `color` |

---

## 🔵 Design-only Tokens — not in production (37)

These tokens exist only in the design files (e.g. custom Figma helpers).  
They are untouched.

| Token | Type | Value |
|---|---|---|
| `Snap Motif/Global.Root.--border-radius-none` | borderRadius | `0px` |
| `Snap Motif/Global.Root.--spacing-none` | spacing | `0px` |
| `Snap Motif/Primary.Carousel.--carousel-card-border-radius` | borderRadius | `{Root.--border-radius-l}` |
| `Snap Motif/Primary.Carousel.--carousel-card-box-shadow` | boxShadow | `{Root.--box-shadow-s}` |
| `Snap Motif/Primary.Carousel.--carousel-card-desktop-text-height` | sizing | `120px` |
| `Snap Motif/Primary.Carousel.--carousel-card-desktop-text-min-height` | sizing | `120px` |
| `Snap Motif/Primary.Carousel.--carousel-card-hover-box-shadow` | boxShadow | `{Root.--box-shadow-l}` |
| `Snap Motif/Primary.Carousel.--carousel-card-landscape-square-small-mobile-width` | sizing | `288px` |
| `Snap Motif/Primary.Carousel.--carousel-card-mobile-text-height` | sizing | `120px` |
| `Snap Motif/Primary.Carousel.--carousel-card-mobile-text-min-height` | sizing | `120px` |
| `Snap Motif/Primary.Carousel.--carousel-card-text-position` | other | `absolute` |
| `Snap Motif/Primary.Carousel.--carousel-text-item-box-shadow` | boxShadow | `{'type': 'dropShadow', 'x': '0', 'y': '0', 'blur': '32px', 'spread': '0', 'color': 'rgba(0, 0, 0, 0.12)'}` |
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
| `Snap Motif/Secondary.Carousel.--carousel-card-bg-color` | color | `{Neutral.--neutral-v625}` |
| `Snap Motif/Secondary.Carousel.--carousel-card-box-shadow` | boxShadow | `{'type': 'dropShadow', 'x': '0px', 'y': '0px', 'blur': '0px', 'spread': '0', 'color': 'rgba(0, 0, 0, 0)'}` |
| `Snap Motif/Secondary.Carousel.--carousel-card-hover-bg-color` | color | `{Neutral.--neutral-v625}` |
| `Snap Motif/Secondary.Carousel.--carousel-card-hover-box-shadow` | boxShadow | `{'type': 'dropShadow', 'x': '0px', 'y': '0px', 'blur': '0px', 'spread': '0', 'color': 'rgba(0, 0, 0, 0)'}` |
| `Snap Motif/Secondary.Footnote.--footnote-hover-icon-bg-color` | color | `{Neutral.--neutral-v600}` |
| `Snap Motif/Secondary.Modal.--modal-close-bg-color` | color | `{Neutral.--neutral-v0}` |
| `Snap Motif/Secondary.Modal.--modal-close-fg-color` | color | `{Neutral.--neutral-v700}` |
| `Snap Motif/Secondary.Quote.--quote-icon-color` | color | `{Primary.--primary-v100}` |
| `Snap Motif/Secondary.Stats.--stats-stat-color` | color | `{Primary.--primary-v100}` |
| `Snap Motif/Tertiary.Quote.--quote-icon-color` | color | `{Primary.--primary-v100}` |
