---
name: Enterprise Corporate System
colors:
  surface: '#faf8ff'
  surface-dim: '#dad9e1'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3fa'
  surface-container: '#eeedf4'
  surface-container-high: '#e9e7ef'
  surface-container-highest: '#e3e1e9'
  on-surface: '#1a1b21'
  on-surface-variant: '#444651'
  inverse-surface: '#2f3036'
  inverse-on-surface: '#f1f0f7'
  outline: '#757682'
  outline-variant: '#c5c5d3'
  surface-tint: '#4059aa'
  primary: '#00236f'
  on-primary: '#ffffff'
  primary-container: '#1e3a8a'
  on-primary-container: '#90a8ff'
  inverse-primary: '#b6c4ff'
  secondary: '#505f76'
  on-secondary: '#ffffff'
  secondary-container: '#d0e1fb'
  on-secondary-container: '#54647a'
  tertiary: '#4b1c00'
  on-tertiary: '#ffffff'
  tertiary-container: '#6e2c00'
  on-tertiary-container: '#f39461'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dce1ff'
  primary-fixed-dim: '#b6c4ff'
  on-primary-fixed: '#00164e'
  on-primary-fixed-variant: '#264191'
  secondary-fixed: '#d3e4fe'
  secondary-fixed-dim: '#b7c8e1'
  on-secondary-fixed: '#0b1c30'
  on-secondary-fixed-variant: '#38485d'
  tertiary-fixed: '#ffdbcb'
  tertiary-fixed-dim: '#ffb691'
  on-tertiary-fixed: '#341100'
  on-tertiary-fixed-variant: '#773205'
  background: '#faf8ff'
  on-background: '#1a1b21'
  surface-variant: '#e3e1e9'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  headline-sm:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 14px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 32px
---

## Brand & Style

The design system is engineered for **Myan Corp**, focusing on high-density data management and professional reliability. The brand personality is **Trustworthy, Professional, and Systematic**. It targets enterprise users who require a high degree of clarity and efficiency in their daily CRM workflows.

The design style follows a **Modern Corporate** aesthetic with a lean toward **Minimalism**. It prioritizes functional hierarchy over decorative elements, using a structured grid and a restrained color palette to reduce cognitive load. Visual depth is achieved through subtle tonal layering rather than heavy shadows, ensuring the interface feels light, fast, and stable.

## Colors

The palette is anchored by **Deep Blue (#1E3A8A)**, representing stability and authority. This is used exclusively for primary actions and active states. 

- **Backgrounds:** A soft **Light Gray (#F8FAFC)** is used for the application canvas to provide a clean contrast against white surface elements.
- **Surfaces:** Pure **White (#FFFFFF)** is used for cards, tables, and containers to signify interactive or content-rich areas.
- **Borders:** A two-tier system is used. **Soft Gray (#E2E8F0)** for layout partitions and **#CBD5E1** for interactive element boundaries (inputs) to ensure WCAG-compliant visibility.
- **Status:** Standard semantic colors for Success and Error are muted to integrate with the professional tone while maintaining high legibility.

## Typography

The design system utilizes **Inter** for all roles. Inter’s tall x-height and geometric clarity make it ideal for high-density enterprise data.

- **Headlines:** Use Semi-Bold (600) or Bold (700) weights with slight negative letter spacing to maintain a compact, professional look.
- **Body:** The default reading size is **14px (body-md)**. This allows for more information density without sacrificing readability.
- **Labels:** Small, uppercase labels with increased letter spacing are used for table headers and category descriptors to differentiate them from actionable text.
- **Mobile:** For screens smaller than 768px, `display-lg` should scale down to 28px and `headline-lg` to 24px.

## Layout & Spacing

This design system employs a **12-column fluid grid** for the main content area with a fixed-width sidebar (240px or 280px). 

- **The 4px Rule:** All spacing increments are multiples of 4px.
- **Internal Spacing:** Use `md (16px)` for standard padding within cards and `sm (8px)` for spacing between related elements like labels and inputs.
- **External Spacing:** Use `lg (24px)` or `xl (32px)` for margins between major layout sections.
- **Adaptivity:** On mobile, margins reduce to 16px and the grid collapses to a single column. On large desktops (1440px+), the main container can be capped at 1280px to prevent excessively long line lengths in text-heavy CRM views.

## Elevation & Depth

To maintain a "Modern Corporate" feel, depth is communicated through **Tonal Layers** and **Low-Contrast Outlines** rather than heavy shadows.

- **Level 0 (Base):** Background color (#F8FAFC). Used for the canvas behind all components.
- **Level 1 (Surface):** White (#FFFFFF) with a 1px border (#E2E8F0). Used for primary cards and content containers.
- **Level 2 (Popovers):** White (#FFFFFF) with a very soft, diffused shadow: `0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)`. Used for dropdowns and tooltips.
- **Level 3 (Modals):** Same shadow as Level 2 but with an increased blur radius and a backdrop overlay (Deep Blue at 20% opacity).

## Shapes

The design system uses a **Rounded** shape language to soften the corporate rigidity while remaining professional.

- **Global Radius:** A standard 8px (0.5rem) radius is applied to all buttons, inputs, and cards.
- **Small Elements:** Chips and tags use a smaller 4px radius or a full pill shape depending on the context.
- **Visual Consistency:** Borders should always be 1px wide. Avoid using "thick" borders to keep the UI looking precise and clean.

## Components

### Buttons
- **Primary:** Deep Blue (#1E3A8A) background, White text. High emphasis.
- **Secondary:** White background, Soft Gray (#E2E8F0) border, Deep Blue text.
- **Tertiary/Ghost:** No background or border, Deep Blue text. Used for less frequent actions.

### Input Fields
- **Default State:** White background, #CBD5E1 border, 14px text.
- **Focus State:** 1px solid Deep Blue (#1E3A8A) border with a 3px soft blue outer glow (ring).
- **Validation:** Use #EF4444 for error borders and helper text.

### Data Tables
- **Header:** Light Gray (#F8FAFC) background, Uppercase labels, 1px bottom border.
- **Rows:** White background, subtle hover state (#F1F5F9).
- **Density:** Provide a "Compact" mode with reduced vertical padding (8px) for power users managing large datasets.

### Chips & Badges
- Used for status (Active, Pending, Closed). Use low-saturation background tints with high-saturation text of the same hue for maximum professional clarity.

### Cards
- White surface, 1px #E2E8F0 border, 8px corner radius. No shadow unless the card is being dragged or is a temporary pop-over.