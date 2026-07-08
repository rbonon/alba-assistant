# Alba — Rising Halo Simplified
## Detailed Production Specification

**Document status:** Production specification v0.1  
**Purpose:** Translate the approved visual direction into a deterministic design system that can be rebuilt in Figma, implemented on web/mobile, and exported as production assets.  
**Scope:** Brand identity, simplified logo system, typography, color palette, sub-brand system, desktop/web UI direction, mobile UI direction, and export requirements.  
**Next step:** Figma Rebuild Blueprint.

---

## 1. Approved Design Direction

### 1.1 Direction name

**Rising Halo — Simplified**

This direction is a simplified evolution of the original Rising Halo concept. It keeps the warmth, elegance, and premium feeling of the selected Alba designs, while reducing logo complexity so the identity can be rebuilt as clean vector artwork.

### 1.2 Core brand idea

**Alba is a calm, human-centered AI assistant suite that brings clarity at the start of every task.**

The brand should feel like the first light of the day: warm, clear, structured, reassuring, and intelligent.

### 1.3 Brand attributes

Alba should consistently express:

- Calm
- Intelligent
- Human
- Friendly
- Trustworthy
- Premium
- Organized
- Luminous, but not flashy
- Modern, but not cold

### 1.4 Design metaphor

The visual metaphor is:

**A rising halo of clarity over an organized structure.**

In practical terms, this becomes:

- a simplified halo / dawn arch
- a clean stylized “A”
- a minimal horizon line
- warm sunrise color accents
- deep navy for trust and structure
- soft backgrounds and rounded UI components

---

## 2. Production Principle

### 2.1 Critical rule

The production system must not depend on image-generation artifacts.

The PNG concept boards are visual references only. The final design must be rebuilt using deterministic assets:

- vector logo
- real font files from open-source sources
- defined color tokens
- reusable UI components
- documented spacing, radius, and shadow rules

### 2.2 Why the logo was simplified

The original Rising Halo logo was visually beautiful but too complex for reliable production because it used:

- glow effects
- radial rays
- fine lighting details
- painterly gradients
- raster-dependent rendering

The simplified version keeps the emotional value of the original while becoming:

- easier to draw as SVG
- easier to recreate consistently
- stronger at small sizes
- easier for LLM/image systems to describe and regenerate
- more practical for app icons, favicons, embroidery, print, and web UI

---

## 3. Logo System

### 3.1 Master logo concept

The Alba mark is composed of three simple elements:

1. **Halo arch**  
   A warm rounded arc above the letterform, representing dawn, guidance, and clarity.

2. **Stylized A**  
   A clean geometric “A” built from simple strokes or filled geometric shapes, representing Alba as the master brand.

3. **Horizon line**  
   A small curved line beneath the A, representing organization, emergence, and a new day.

### 3.2 Logo construction rules

The production logo should be created as vector geometry.

Recommended construction:

- Artboard base: square ratio for mark construction.
- Halo: single stroked arc with rounded caps.
- A-shape: two diagonal strokes plus optional crossbar.
- Horizon: single shallow curve below the A.
- No embedded glow in the core mark.
- No rays in the core mark.
- No complex gradients in the core mark.
- Gradients may be used only in app icons, backgrounds, hero graphics, and decorative environments.

### 3.3 Logo variants

The final production set should include:

1. **Primary horizontal logo**
   - Mark left
   - “Alba” wordmark right
   - Optional descriptor: “AI Assistant Suite”

2. **Primary stacked logo**
   - Mark above
   - “Alba” below
   - Descriptor below wordmark

3. **Icon-only mark**
   - Halo + A + horizon
   - Used for app icons, favicon, small UI marks

4. **Monochrome mark**
   - One-color version for print, embroidery, engraving, stamps, and restricted environments

5. **Dark-mode logo**
   - Mark in warm accent and white/off-white
   - Wordmark in white or Cloud White
   - Descriptor in Sunrise Gold

6. **Light-mode logo**
   - Mark in Sunrise Gold + Deep Navy
   - Wordmark in Deep Navy
   - Descriptor in Sunrise Gold

### 3.4 Logo clear space

Minimum clear space around the logo should equal:

- **1× the height of the horizon line area** for compact UI usage
- **0.5× mark width** for brand/marketing usage
- **1× the capital A stroke width** as the minimum emergency spacing

No text, icon, or container edge should enter this protected space.

### 3.5 Minimum sizes

Recommended minimums:

- Full horizontal logo: **160 px wide**
- Stacked logo: **120 px wide**
- Icon-only mark: **24 px**
- Favicon simplified mark: **16 px**
- Embroidery mark: test at **25 mm wide minimum**

At very small sizes, remove the descriptor and use the icon-only mark.

### 3.6 Logo misuse

Avoid:

- adding rays to the production mark
- adding uncontrolled glow to the production mark
- stretching the mark
- changing the A geometry independently from the halo
- using low-contrast accent colors on light backgrounds
- using the full logo below minimum size
- placing the mark over noisy photography without a protective container

---

## 4. Typography

### 4.1 Font principle

The brand uses only open-source, freely available typefaces.

### 4.2 Primary heading font

**Playfair Display**

Use for:

- brand headlines
- landing page hero titles
- concept board titles
- major section headings
- selected marketing moments
- Alba wordmark exploration, if appropriate

Recommended weights:

- Regular
- Medium
- SemiBold
- Bold

Style guidance:

- Use sparingly.
- Use for emotional, high-level hierarchy.
- Avoid long paragraphs in Playfair Display.
- Keep letter spacing normal or slightly tightened for large sizes.

### 4.3 Primary body and UI font

**Inter**

Use for:

- web UI
- mobile UI
- navigation
- buttons
- labels
- cards
- tables
- captions
- product dashboards
- body copy

Recommended weights:

- Regular 400
- Medium 500
- SemiBold 600
- Bold 700

Style guidance:

- Use Inter as the default interface typeface.
- Prefer medium weight for labels and navigation.
- Prefer regular weight for body copy.
- Use semibold for buttons and section labels.

### 4.4 Type hierarchy

Recommended starting hierarchy:

| Role | Font | Size | Weight | Line height |
|---|---:|---:|---:|---:|
| Hero headline | Playfair Display | 64–88 px desktop / 38–48 px mobile | 600 | 0.95–1.05 |
| Page title | Playfair Display | 40–56 px desktop / 30–36 px mobile | 600 | 1.05–1.15 |
| Section title | Inter | 14–18 px | 700 | 1.2 |
| Card title | Inter | 16–22 px | 600 | 1.25 |
| Body text | Inter | 15–18 px | 400 | 1.45–1.65 |
| Caption | Inter | 11–13 px | 500 | 1.3 |
| Button | Inter | 14–16 px | 600 | 1.1 |

### 4.5 Wordmark note

The Alba wordmark may use Playfair Display as a starting point, but the final wordmark should ideally be converted to outlines and lightly customized for uniqueness. Do not over-customize before the master logo is locked.

---

## 5. Color System

### 5.1 Canonical palette

The following palette is the production baseline.

| Token | Hex | Role |
|---|---:|---|
| Deep Navy | `#0F172A` | Primary text, dark panels, brand authority |
| Cloud White | `#F8FAFC` | Light surfaces, UI backgrounds |
| Paper | `#FFFDF9` | Warm off-white brand background |
| Dawn Peach | `#FFD6B3` | Soft warmth, backgrounds, gradients |
| Sunrise Gold | `#FFB45C` | Primary accent, halo, CTA warmth |
| Soft Lavender | `#C8B7FF` | Secondary accent, photos/soft AI moments |
| Sky Blue | `#A7C7FF` | Support accent, guidance, calm states |
| Warm Gray | `#6B7280` | Secondary text, captions, neutral UI |

### 5.2 Extended semantic accents

| Product / Function | Recommended Accent | Hex |
|---|---:|---:|
| Alba Docs | Sunrise Gold | `#FFB45C` |
| Alba Photos | Lavender | `#8E6DE5` |
| Alba Expenses | Green | `#35A66F` |
| Alba Virtuo | Blue | `#5F8FEF` |
| Success | Green | `#35A66F` |
| Warning | Amber | `#F59E0B` |
| Error | Soft Red | `#E85D75` |
| Info | Sky Blue | `#5F8FEF` |

### 5.3 Color usage ratio

Recommended ratio for Alba interfaces:

- 60–70% light neutral surfaces
- 15–20% Deep Navy text / structure
- 10–15% warm dawn accents
- 5–10% product-specific accents

### 5.4 Gradients

Gradients should be used as environmental atmosphere, not as core logo dependencies.

Recommended dawn gradient:

```css
linear-gradient(135deg, #FFD6B3 0%, #F8FAFC 38%, #C8B7FF 72%, #A7C7FF 100%)
```

Recommended hero glow:

```css
radial-gradient(circle at 70% 70%, rgba(255,180,92,0.75), rgba(255,214,179,0.15) 35%, transparent 60%)
```

### 5.5 Accessibility note

Use Deep Navy text on light surfaces for primary readability. Sunrise Gold and Dawn Peach should not be used for small text on light backgrounds unless contrast is verified.

---

## 6. Iconography

### 6.1 Icon style

Icons should be:

- simple line icons
- rounded caps and joins
- 1.75–2 px stroke at 24 px size
- minimal internal detail
- geometric but friendly
- consistent across products

### 6.2 Icon categories

Core icons:

- Home
- Document
- Photo / image
- Receipt / expense
- Spark / assistant
- Search
- Filter
- Bell
- User
- Shield
- Calendar
- Check
- Camera
- Folder
- More / overflow

### 6.3 Product icons

Recommended product metaphors:

| Product | Icon |
|---|---|
| Alba Docs | Document page with 2–3 horizontal lines |
| Alba Photos | Photo frame with mountain/sun shape |
| Alba Expenses | Receipt or card with currency cue |
| Alba Virtuo | Spark / small guiding star |

Avoid overly detailed product icons. Each product icon should work inside a 32 px or 40 px rounded square.

---

## 7. Sub-brand System

### 7.1 Naming

The product family uses the structure:

**Alba + Product Name**

Current approved examples:

- Alba Docs
- Alba Photos
- Alba Expenses
- Alba Virtuo

Future names should follow the same structure.

### 7.2 Sub-brand lockup

Each sub-brand lockup should include:

- product icon
- “Alba” in primary brand style
- product name in product accent color
- optional one-line descriptor

### 7.3 Sub-brand tone

Sub-brands should not look like separate companies. They are functional expressions of Alba.

The master brand remains dominant. Product accents should help orientation, not create competing identities.

### 7.4 Product descriptors

Recommended descriptor language:

| Product | Descriptor |
|---|---|
| Alba Docs | Documents organized and clear. |
| Alba Photos | Memories beautifully organized. |
| Alba Expenses | Track, understand, stay in control. |
| Alba Virtuo | Guided processing and clarity. |

---

## 8. UI Design System

### 8.1 Overall UI feel

The UI should feel:

- calm
- organized
- readable
- rounded
- premium
- useful without being visually heavy

Avoid highly futuristic, cybernetic, or robot-like aesthetics.

### 8.2 Surfaces

Recommended surfaces:

- main background: Paper or Cloud White
- cards: white or near-white
- dark feature panels: Deep Navy
- product tiles: white with subtle accent icon containers
- modals: white with soft shadow

### 8.3 Corner radius

Recommended radius scale:

| Token | Value | Usage |
|---|---:|---|
| Radius XS | 6 px | small tags, badges |
| Radius SM | 10 px | chips, inputs |
| Radius MD | 16 px | cards, list containers |
| Radius LG | 24 px | major feature cards |
| Radius XL | 32 px | hero panels, phone mockup cards |
| Radius Full | 999 px | pills, circular controls |

### 8.4 Shadow style

Shadows should be soft and low contrast.

Recommended card shadow:

```css
0 12px 30px rgba(15, 23, 42, 0.08)
```

Recommended elevated panel shadow:

```css
0 24px 70px rgba(15, 23, 42, 0.12)
```

Avoid harsh shadows and black-heavy elevation.

### 8.5 Buttons

Primary button:

- background: Deep Navy
- text: white
- radius: full / pill
- font: Inter Semibold
- height: 44–52 px

Secondary button:

- background: white or transparent
- border: 1 px light gray
- text: Deep Navy
- radius: full / pill

Accent CTA:

- use Sunrise Gold sparingly
- best for onboarding or highlight actions
- verify contrast before using with white text

### 8.6 Cards

Cards should use:

- white background
- 1 px subtle border or soft shadow
- 16–24 px internal padding
- rounded corners
- clear hierarchy
- small product icon in colored container

### 8.7 Chips

Chips should be used for filters and categories.

Active chip:

- Deep Navy background
- white text

Inactive chip:

- white or Cloud White background
- Warm Gray or Deep Navy text
- subtle border

### 8.8 Navigation

Bottom mobile navigation:

- 5 items maximum
- active state uses Sunrise Gold or Deep Navy
- inactive state uses Warm Gray
- icons should be simple line icons

Desktop/sidebar navigation:

- dark sidebar allowed
- active item can use a darker navy or soft accent background
- use product accent dots/icons for orientation

---

## 9. Desktop / Web Direction

### 9.1 Primary desktop use cases

The web system should support:

- marketing website
- product suite landing page
- dashboard shell
- document/expense/photo management screens
- assistant/chat panels

### 9.2 Landing page hero

Hero structure:

- Alba logo in header
- navigation: Product, Solutions, Pricing, Resources
- primary CTA: Get Started
- headline: “Clarity at dawn. Productivity all day.”
- supportive body copy
- optional secondary CTA: Watch Demo
- soft dawn background or abstract sunrise panel

### 9.3 Dashboard shell

Recommended desktop shell:

- left sidebar for suite navigation
- main content area with cards
- top greeting or page title
- recent activity block
- task/priority cards
- product entry points

### 9.4 Web page rhythm

Use generous spacing:

- outer page margin: 64–96 px desktop
- section gap: 64–120 px
- card gap: 16–24 px
- card padding: 24–32 px

---

## 10. Mobile Direction

### 10.1 Mobile app structure

Initial mobile flow contains:

1. Welcome / onboarding
2. Home dashboard
3. Alba Docs
4. Alba Expenses
5. Alba Virtuo assistant

Alba Photos can be present as a home tile and become a dedicated screen later.

### 10.2 Mobile onboarding

Should include:

- simplified Alba logo
- dawn gradient or soft sunrise illustration
- headline: “Clarity at dawn.”
- short product statement
- primary CTA: Get Started
- secondary CTA: Watch Demo or Learn More
- simple pagination dots

### 10.3 Home dashboard

Should include:

- personalized greeting
- four suite tiles:
  - Alba Docs
  - Alba Photos
  - Alba Expenses
  - Alba Virtuo
- Today’s Priorities
- Recent Activity
- bottom navigation

### 10.4 Alba Docs screen

Should include:

- title
- search bar
- filter control
- category chips
- recent document list
- categories section
- bottom navigation

### 10.5 Alba Expenses screen

Should include:

- monthly summary card
- total spent
- trend indicator
- simple chart
- add expense / capture receipt action
- spending categories
- recent expenses

### 10.6 Alba Virtuo screen

Should include:

- calm assistant greeting
- suggested prompts
- message input
- privacy reassurance
- minimal distraction
- softer accent colors, preferably blue/lavender

### 10.7 Mobile spacing

Recommended mobile spacing:

- screen horizontal padding: 20–24 px
- card padding: 16–20 px
- section gap: 24–32 px
- list row height: 56–72 px
- bottom navigation height: 72–84 px

---

## 11. Content and Voice

### 11.1 Voice principles

Alba should sound:

- clear
- calm
- helpful
- human
- concise
- confident without hype

Avoid:

- “magical AI” exaggeration
- robotic terminology
- overly technical phrasing in user-facing UI
- therapy-like claims for Alba Virtuo unless legally and clinically reviewed

### 11.2 Sample language

Master tagline:

**Clarity at dawn. Productivity all day.**

Alternative tagline:

**One assistant. Many capabilities.**

Short brand description:

**Alba is a calm, intelligent AI assistant suite that helps you organize, create, and accomplish more with clarity.**

Alba Virtuo caution:

**Alba Virtuo may support reflection and organization of session material, but should not be positioned as a replacement for professional clinical judgment.**

---

## 12. Production Asset Requirements

### 12.1 Logo exports

Required exports:

- SVG: primary horizontal
- SVG: stacked
- SVG: icon-only
- SVG: monochrome
- SVG: dark version
- PNG: transparent logo at 1x, 2x, 4x
- PNG: app icon sizes
- PDF: print-safe logo sheet

### 12.2 App icon exports

Recommended app icon outputs:

- 1024 × 1024 PNG
- 512 × 512 PNG
- 256 × 256 PNG
- 192 × 192 PNG
- 180 × 180 PNG
- 152 × 152 PNG
- 120 × 120 PNG
- 76 × 76 PNG
- 32 × 32 PNG
- 16 × 16 PNG / ICO

### 12.3 Web assets

Required:

- favicon SVG
- favicon ICO
- web app manifest icons
- social preview image
- OG image
- header logo SVG
- footer logo SVG

### 12.4 Figma deliverables

The production Figma file should include:

- brand tokens
- logo components
- typography styles
- color styles
- icon components
- desktop UI components
- mobile UI components
- desktop concept board rebuilt
- mobile concept board rebuilt
- export-ready frames

---

## 13. Implementation Tokens

### 13.1 CSS variables

```css
:root {
  --alba-deep-navy: #0F172A;
  --alba-cloud-white: #F8FAFC;
  --alba-paper: #FFFDF9;
  --alba-dawn-peach: #FFD6B3;
  --alba-sunrise-gold: #FFB45C;
  --alba-soft-lavender: #C8B7FF;
  --alba-sky-blue: #A7C7FF;
  --alba-warm-gray: #6B7280;

  --alba-docs: #FFB45C;
  --alba-photos: #8E6DE5;
  --alba-expenses: #35A66F;
  --alba-virtuo: #5F8FEF;

  --radius-xs: 6px;
  --radius-sm: 10px;
  --radius-md: 16px;
  --radius-lg: 24px;
  --radius-xl: 32px;
  --radius-full: 999px;

  --shadow-card: 0 12px 30px rgba(15, 23, 42, 0.08);
  --shadow-panel: 0 24px 70px rgba(15, 23, 42, 0.12);
}
```

### 13.2 Font stack

```css
:root {
  --font-heading: "Playfair Display", Georgia, serif;
  --font-body: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
```

---

## 14. Acceptance Criteria

A production rebuild is acceptable when:

- the simplified logo exists as clean editable vector artwork
- the logo works in light, dark, monochrome, and icon-only forms
- typography uses open-source fonts only
- the color palette is tokenized
- the desktop and mobile boards can be exported at high resolution without raster degradation
- UI components are reusable, not flattened images
- app icons and favicons are readable at small sizes
- sub-brands feel like one coherent family
- the final system is implementable in web and mobile products

---

## 15. Open Decisions for Step 3

These items should be resolved in the Figma Rebuild Blueprint:

- exact frame size for rebuilt boards
- exact grid columns and margins
- exact logo geometry dimensions
- whether the final wordmark remains Playfair Display or becomes customized outlines
- exact mobile device frame size
- exact desktop dashboard preview dimensions
- final export naming convention
- whether to include Alba Photos as a full dedicated mobile screen in the first production flow
