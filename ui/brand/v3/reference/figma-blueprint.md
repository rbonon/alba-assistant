# Alba — Rising Halo Simplified
## Step 3: Figma Rebuild Blueprint v0.1

**Purpose:** Convert the approved Alba “Rising Halo — Simplified” production spec into a practical Figma construction manual.

**Important principle:** The PNG concept boards are visual references, not production source files. In Figma, rebuild the boards with real vectors, real text, reusable components, and design tokens.

---

## 1. Figma File Structure

Create a Figma file named:

**Alba — Rising Halo Simplified — Production Rebuild**

Recommended pages:

1. **00 — References**
2. **01 — Foundations**
3. **02 — Logo System**
4. **03 — Components**
5. **04 — Desktop Brand Board**
6. **05 — Mobile UI Board**
7. **06 — Export Frames**
8. **99 — Scratch**

---

## 2. Reference Setup

### 2.1 Import reference PNGs

Place the approved PNG references on page **00 — References**:

- Desktop / brand concept board
- Mobile UI concept board

Create two frames:

| Frame | Size |
|---|---:|
| Reference — Desktop Board | 1448 × 1086 px |
| Reference — Mobile Board | 1448 × 1086 px |

Lock both reference images.

### 2.2 Production rebuild scale

Use a clean production board size:

| Production Frame | Size | Ratio |
|---|---:|---:|
| Desktop Brand Board | 1920 × 1440 px | 4:3 |
| Mobile UI Board | 1920 × 1440 px | 4:3 |

Why this size:

- Clean 4:3 ratio.
- Better grid math than 1448 × 1086.
- Exports cleanly to 7680 × 5760 at 4×.
- Easy to downscale for decks, PDFs, and previews.

---

## 3. Figma Variables and Styles

Create Figma variables or styles with the following names.

### 3.1 Color variables

| Name | Hex |
|---|---:|
| Alba / Deep Navy | `#0F172A` |
| Alba / Cloud White | `#F8FAFC` |
| Alba / Paper | `#FFFDF9` |
| Alba / Dawn Peach | `#FFD6B3` |
| Alba / Sunrise Gold | `#FFB45C` |
| Alba / Soft Lavender | `#C8B7FF` |
| Alba / Sky Blue | `#A7C7FF` |
| Alba / Warm Gray | `#6B7280` |
| Alba / Border Soft | `#E5E7EB` |
| Alba / Card White | `#FFFFFF` |
| Product / Docs | `#FFB45C` |
| Product / Photos | `#8E6DE5` |
| Product / Expenses | `#35A66F` |
| Product / Virtuo | `#5F8FEF` |
| Semantic / Success | `#35A66F` |
| Semantic / Warning | `#F59E0B` |
| Semantic / Error | `#E85D75` |
| Semantic / Info | `#5F8FEF` |

### 3.2 Typography styles

Use open-source fonts only:

- **Playfair Display**
- **Inter**

Create these text styles:

| Style | Font | Size | Weight | Line height |
|---|---|---:|---:|---:|
| Display / Hero | Playfair Display | 84 | SemiBold | 88 |
| Display / Page Title | Playfair Display | 58 | SemiBold | 64 |
| Display / Section Title | Playfair Display | 40 | SemiBold | 46 |
| UI / H1 | Inter | 32 | 700 | 40 |
| UI / H2 | Inter | 24 | 700 | 32 |
| UI / H3 | Inter | 20 | 600 | 28 |
| UI / Body Large | Inter | 18 | 400 | 30 |
| UI / Body | Inter | 16 | 400 | 24 |
| UI / Body Small | Inter | 14 | 400 | 21 |
| UI / Label | Inter | 13 | 600 | 16 |
| UI / Caption | Inter | 12 | 500 | 16 |
| UI / Micro | Inter | 10 | 600 | 12 |
| UI / Button | Inter | 15 | 600 | 18 |

### 3.3 Effects

Create these effect styles:

| Style | Value |
|---|---|
| Shadow / Card | `0, 12, 30, rgba(15, 23, 42, 0.08)` |
| Shadow / Panel | `0, 24, 70, rgba(15, 23, 42, 0.12)` |
| Shadow / Phone | `0, 24, 60, rgba(15, 23, 42, 0.16)` |
| Border / Soft | 1 px `#E5E7EB` |

### 3.4 Radius tokens

| Token | Value |
|---|---:|
| Radius / XS | 6 |
| Radius / SM | 10 |
| Radius / MD | 16 |
| Radius / LG | 24 |
| Radius / XL | 32 |
| Radius / XXL | 40 |
| Radius / Full | 999 |

---

## 4. Simplified Logo Geometry

Build the logo mark as vector geometry in Figma.

### 4.1 Mark construction frame

Create component:

**Logo / Mark / Simplified**

Base frame:

- Width: 512 px
- Height: 512 px
- Fill: none

### 4.2 Core geometry

Use these elements:

#### Halo arc

- Shape: arc/path
- Start point: x 146, y 226
- End point: x 366, y 226
- Arc: upward semicircular / elliptical arc
- Stroke: Sunrise Gold
- Stroke width: 32
- Stroke cap: round

SVG equivalent:

```svg
<path d="M146 226 A110 88 0 0 1 366 226" />
```

#### Stylized A

- Shape: path
- Stroke: Deep Navy
- Stroke width: 42
- Stroke cap: round
- Stroke join: round

SVG equivalent:

```svg
<path d="M190 342 L256 164 L322 342" />
```

#### A crossbar

- Shape: horizontal line/path
- Stroke: Deep Navy
- Stroke width: 30
- Stroke cap: round

SVG equivalent:

```svg
<path d="M222 275 L290 275" />
```

#### Horizon line

- Shape: curved path
- Stroke: Sunrise Gold
- Stroke width: 20
- Stroke cap: round

SVG equivalent:

```svg
<path d="M166 360 C208 340 304 340 346 360" />
```

### 4.3 Logo variants to create

Create these Figma components:

- `Logo / Mark / Light`
- `Logo / Mark / Dark`
- `Logo / Mark / Mono`
- `Logo / Horizontal / Light`
- `Logo / Horizontal / Dark`
- `Logo / Stacked / Light`
- `Logo / Stacked / Dark`
- `Logo / App Icon / Light`
- `Logo / App Icon / Dark`
- `Logo / App Icon / Mono`

### 4.4 Wordmark

Start with:

- Text: Alba
- Font: Playfair Display SemiBold
- Size: 96 px for stacked logo
- Size: 64 px for horizontal logo
- Fill: Deep Navy on light; Cloud White on dark
- Letter spacing: -2%

Descriptor:

- Text: AI ASSISTANT SUITE
- Font: Inter SemiBold
- Size: 15–18 px
- Letter spacing: 18–22%
- Fill: Sunrise Gold

### 4.5 Logo clear space

Use clear space equal to:

- 0.25× mark width around icon-only mark
- 0.5× mark height around full lockups

Do not let other elements enter this area.

---

## 5. Core Components

Create all components on page **03 — Components**.

### 5.1 Buttons

#### Button / Primary

- Height: 48 px
- Padding: 20 px horizontal
- Radius: Full
- Fill: Deep Navy
- Text: white, Inter SemiBold 15
- Optional icon: 18 px

#### Button / Secondary

- Height: 48 px
- Padding: 20 px horizontal
- Radius: Full
- Fill: white
- Stroke: Border Soft, 1 px
- Text: Deep Navy, Inter SemiBold 15

### 5.2 Chips

#### Chip / Active

- Height: 34 px
- Padding: 14 px horizontal
- Radius: Full
- Fill: Deep Navy
- Text: white, Inter Medium 13

#### Chip / Inactive

- Height: 34 px
- Padding: 14 px horizontal
- Radius: Full
- Fill: Cloud White or white
- Stroke: Border Soft 1 px
- Text: Warm Gray, Inter Medium 13

### 5.3 Cards

#### Card / Base

- Fill: white
- Radius: 24
- Stroke: Border Soft 1 px or Shadow / Card
- Padding: 24

#### Card / Dark Feature

- Fill: Deep Navy
- Radius: 28
- Text: Cloud White
- Accent: Sunrise Gold

#### Card / Product Tile

- Fill: white
- Radius: 20
- Padding: 18
- Icon container: 44 × 44 px, radius 14
- Title: Inter SemiBold 15–16
- Body: Inter Regular 12–13

### 5.4 List rows

#### Row / File

- Height: 68 px
- Icon container: 40 × 40 px
- Title: Inter SemiBold 14
- Metadata: Inter Regular 12, Warm Gray
- Right action: More icon 20 px

#### Row / Priority

- Height: 58 px
- Checkbox: 20 px
- Title: Inter Medium 14
- Time: Inter Regular 12, Warm Gray

#### Row / Expense

- Height: 64 px
- Category icon: 40 × 40
- Title: Inter SemiBold 14
- Metadata: Inter Regular 12
- Amount: Inter SemiBold 14

### 5.5 Mobile navigation

Component:

**Navigation / Mobile Bottom**

- Height: 78 px
- Fill: white
- Top border: Border Soft
- Items: 5
- Icon: 22 px
- Label: Inter Medium 10
- Active: Sunrise Gold or Deep Navy
- Inactive: Warm Gray

### 5.6 Phone frame

Component:

**Device / Phone Frame**

- Outer size: 280 × 608 px
- Corner radius: 42
- Fill: Deep Navy or black frame
- Inner screen: 260 × 584 px
- Inner corner radius: 34
- Shadow: Shadow / Phone

For board mockups, keep a clean simplified device frame. Do not over-render realistic hardware.

---

## 6. Desktop Brand Board Rebuild

Page:

**04 — Desktop Brand Board**

Frame:

**Board / Desktop Brand / 1920×1440**

### 6.1 Canvas

- Size: 1920 × 1440 px
- Fill: Paper `#FFFDF9`
- Layout grid:
  - Columns: 12
  - Margin: 72 px
  - Gutter: 24 px
  - Column width: 126 px
- Base spacing: 8 px

### 6.2 Section layout

Use this approximate section map:

| Section | X | Y | W | H |
|---|---:|---:|---:|---:|
| Concept Intro | 72 | 64 | 480 | 360 |
| Master Logo Light | 600 | 64 | 560 | 360 |
| Master Logo Dark | 1208 | 64 | 640 | 360 |
| App Icon Variations | 72 | 456 | 520 | 220 |
| Color Palette | 624 | 456 | 640 | 220 |
| Typography | 1296 | 456 | 552 | 220 |
| Sub-brand System | 72 | 708 | 1230 | 240 |
| Why This Works | 1334 | 708 | 514 | 240 |
| Web Preview | 72 | 980 | 760 | 300 |
| Dashboard Preview | 856 | 980 | 600 | 300 |
| Brand Applications | 1480 | 980 | 368 | 300 |
| Values Strip | 72 | 1312 | 1776 | 88 |

### 6.3 Desktop section details

#### Concept Intro

Content:

- Label: CONCEPT
- Title: Rising Halo — Simplified
- Subtitle: A CLEANER, VECTOR-FRIENDLY EVOLUTION OF ALBA.
- Paragraph:
  “This simplified mark preserves the feeling of dawn, clarity, and trust—using simple geometry that is easy to produce as SVG, recognizable at any size, and consistent across digital and physical experiences.”
- Value list:
  - Dawn of clarity
  - Intelligent & luminous
  - Human & friendly
  - Trustworthy & secure
  - Premium by design

#### Master Logo Light

- White or Paper panel
- Label: 2. MASTER LOGO — LIGHT
- Stacked logo centered
- Mark width: 150–180 px
- Wordmark: 92–104 px
- Descriptor: 15–18 px

#### Master Logo Dark

- Deep Navy panel
- Radius: 24
- Label: 3. MASTER LOGO — DARK
- Stacked dark logo centered
- Optional very subtle radial glow behind logo, but do not include glow inside logo component

#### App Icon Variations

Create four icon cards:

- Light
- Dark
- Monochrome
- Shortcut

Each icon:

- 76 × 76 px
- Radius: 20
- Shadow: soft
- Caption below

#### Color Palette

Swatches:

- 56 px circles
- Name below, 2 lines max
- Hex below in Inter Micro

#### Typography

Display:

- Playfair Display
- Label: HEADINGS / Open-source
- Inter
- Label: BODY & INTERFACE / Open-source

#### Sub-brand System

Four tiles:

- Alba Docs
- Alba Photos
- Alba Expenses
- Alba Virtuo

Each tile:

- Icon container 52 × 52
- Title 22–26 px
- Descriptor 13–14 px
- Accent on product name and icon

#### Why This Works

Four compact points:

- Simple geometry
- Easy SVG tracing
- Strong at small sizes
- Consistent across AI image generation

#### Web Preview

Mini landing page:

- Header with logo, nav, Get Started
- Hero headline: “Clarity at dawn. Productivity all day.”
- Body copy
- CTA buttons
- Dawn gradient or simple landscape abstraction

#### Dashboard Preview

Mini app shell:

- Deep Navy sidebar
- Logo at top
- Navigation list
- Dashboard content with greeting, Today card, Recent card

#### Brand Applications

Two mockups:

- Mug
- Hat

For production rebuild, these can be simplified vector mockups instead of photorealistic images.

#### Values Strip

Items:

- One assistant. Many capabilities.
- Built to grow—beautifully, consistently, and with purpose.
- Unified experience
- Secure by default
- Made for people
- Smart by design

---

## 7. Mobile UI Board Rebuild

Page:

**05 — Mobile UI Board**

Frame:

**Board / Mobile UI / 1920×1440**

### 7.1 Canvas

- Size: 1920 × 1440 px
- Fill: Paper
- Layout grid:
  - Columns: 12
  - Margin: 72 px
  - Gutter: 24 px
- Base spacing: 8 px

### 7.2 Section layout

| Section | X | Y | W | H |
|---|---:|---:|---:|---:|
| Brand Lockup | 72 | 56 | 360 | 180 |
| Mobile Title Block | 480 | 56 | 520 | 180 |
| Feature Row | 1040 | 56 | 808 | 180 |
| Phone 1 Area | 72 | 280 | 336 | 780 |
| Phone 2 Area | 432 | 280 | 336 | 780 |
| Phone 3 Area | 792 | 280 | 336 | 780 |
| Phone 4 Area | 1152 | 280 | 336 | 780 |
| Phone 5 Area | 1512 | 280 | 336 | 780 |
| Components Strip | 72 | 1100 | 420 | 280 |
| Color Palette Strip | 516 | 1100 | 420 | 280 |
| Typography Strip | 960 | 1100 | 360 | 280 |
| Iconography + Logo Note | 1344 | 1100 | 504 | 280 |

### 7.3 Phone frame sizing

For each phone area:

- Phone frame: 280 × 608 px
- Label above: 36 px high
- Center phone horizontally within each 336 px area
- Phone top Y: 344
- Phone X positions:
  - Phone 1: 100
  - Phone 2: 460
  - Phone 3: 820
  - Phone 4: 1180
  - Phone 5: 1540

### 7.4 Phone screen content

#### Screen 1 — Welcome / Onboarding

- Soft dawn gradient background
- Alba mark and wordmark
- Headline: “Clarity at dawn.”
- Body:
  “Alba helps you organize, create, and accomplish more—with the power of AI.”
- Primary button: Get Started
- Secondary button: Watch Demo
- Pagination dots

#### Screen 2 — Home Dashboard

- Greeting: “Good morning, Sam”
- Subtext: “Here’s what’s on your plate today.”
- Top icons: menu, bell, avatar
- Four product tiles:
  - Alba Docs
  - Alba Photos
  - Alba Expenses
  - Alba Virtuo
- Today’s Priorities card
- Recent Activity card
- Bottom navigation

#### Screen 3 — Alba Docs

- Top bar: back, title, overflow
- Search bar
- Filter icon
- Chips: All, Work, Personal, Finance, Projects
- Recent file list:
  - Brand strategy.docx
  - Q2 Planning Deck.pptx
  - Client Proposal.pdf
  - Project Brief.pdf
- Categories:
  - Work
  - Personal
  - Finance
  - Projects
- Bottom navigation, Docs active

#### Screen 4 — Alba Expenses

- Top bar
- Dark summary card
- Total Spent: `$2,842.75`
- Trend: `8% vs last month`
- Simple donut chart
- Stats:
  - 128 Transactions
  - 4 Categories
  - 2 Budgets
  - 98% On Track
- Buttons:
  - Add Expense
  - Capture Receipt
- Spending by Category list
- Recent Expenses
- Bottom navigation, Expenses active

#### Screen 5 — Alba Virtuo

- Top bar
- Spark / assistant emblem
- Headline:
  “I’m here to help you find clarity.”
- Body:
  “Share what’s on your mind, and we’ll work through it together.”
- Suggested prompts:
  - I feel overwhelmed. Help me focus.
  - Help me reflect on my day.
  - What should I prioritize today?
  - I need motivation and a plan.
- Message input:
  “Message Alba Virtuo...”
- Privacy reassurance:
  “Alba respects your privacy. Conversations are private and secure.”
- Bottom navigation, Virtuo active

### 7.5 Bottom system strip

#### Components

Include:

- Primary button
- Secondary button
- Active chip
- Inactive chip
- Checked checkbox
- Unchecked checkbox
- Simple card example

#### Color Palette

Use the canonical swatches.

#### Typography

Show:

- Playfair Display
- Inter
- Label both as open-source fonts

#### Iconography + Logo Note

Show:

- 10–15 simple line icons
- Mini simplified logo mark
- Note:
  “Vector-friendly, consistent, and easy to reproduce at any size.”

---

## 8. Component Naming Convention

Use this naming pattern:

```text
Category / Component / Variant / State
```

Examples:

```text
Button / Primary / Default
Button / Primary / Hover
Button / Secondary / Default
Card / Product Tile / Docs
Card / Product Tile / Photos
Navigation / Mobile Bottom / Home Active
Logo / Mark / Light
Logo / Mark / Dark
Logo / Horizontal / Light
Phone Screen / Home Dashboard
```

---

## 9. Auto Layout Guidance

Use Auto Layout wherever possible.

### 9.1 Cards

- Direction: vertical
- Padding: 20–24 px
- Gap: 10–16 px
- Hug contents vertically
- Fixed width when used in board

### 9.2 Button

- Direction: horizontal
- Padding: 20 px left/right
- Gap: 8 px
- Height: 48 px
- Center align

### 9.3 Mobile screen

Use nested Auto Layout:

- Screen frame: vertical
- Top bar
- Scrollable content group
- Bottom navigation

For the presentation board, the screen can be static; still build it with components.

---

## 10. Export Frames

Create page **06 — Export Frames**.

### 10.1 Board exports

| Export | Figma Frame | Format | Scale |
|---|---|---|---:|
| Desktop Board Preview | Board / Desktop Brand / 1920×1440 | PNG | 1× |
| Desktop Board Hi-Res | Board / Desktop Brand / 1920×1440 | PNG | 4× |
| Desktop Board PDF | Board / Desktop Brand / 1920×1440 | PDF | 1× |
| Mobile Board Preview | Board / Mobile UI / 1920×1440 | PNG | 1× |
| Mobile Board Hi-Res | Board / Mobile UI / 1920×1440 | PNG | 4× |
| Mobile Board PDF | Board / Mobile UI / 1920×1440 | PDF | 1× |

4× export size from 1920 × 1440:

**7680 × 5760 px**

### 10.2 Logo exports

| Asset | Format |
|---|---|
| Alba horizontal light | SVG, PNG |
| Alba horizontal dark | SVG, PNG |
| Alba stacked light | SVG, PNG |
| Alba stacked dark | SVG, PNG |
| Alba mark light | SVG, PNG |
| Alba mark dark | SVG, PNG |
| Alba mark mono | SVG, PNG |
| App icon light | PNG |
| App icon dark | PNG |
| Favicon | SVG, ICO, PNG |

### 10.3 App icon sizes

Export:

- 1024 × 1024
- 512 × 512
- 256 × 256
- 192 × 192
- 180 × 180
- 152 × 152
- 120 × 120
- 76 × 76
- 32 × 32
- 16 × 16

---

## 11. Rebuild Checklist

Use this checklist to validate the Figma rebuild.

### Foundations

- [ ] Colors created as variables/styles
- [ ] Typography styles created
- [ ] Radius tokens represented
- [ ] Shadow styles created
- [ ] Icon stroke style standardized

### Logo

- [ ] Simplified mark built with vector paths
- [ ] Light mark component created
- [ ] Dark mark component created
- [ ] Monochrome mark component created
- [ ] Horizontal lockup created
- [ ] Stacked lockup created
- [ ] App icon variants created
- [ ] Small-size test at 16, 24, 32 px completed

### Desktop board

- [ ] Board frame created at 1920 × 1440
- [ ] 12-column grid applied
- [ ] All sections rebuilt with live text
- [ ] Web preview rebuilt as vector/UI elements
- [ ] Dashboard preview rebuilt as vector/UI elements
- [ ] Values strip rebuilt
- [ ] Export tested at 1× and 4×

### Mobile board

- [ ] Board frame created at 1920 × 1440
- [ ] Five phone screens rebuilt
- [ ] Phone frame component used
- [ ] Bottom navigation component used
- [ ] Product tile components used
- [ ] Bottom system strip rebuilt
- [ ] Export tested at 1× and 4×

### Production readiness

- [ ] No flattened screenshots except the locked reference page
- [ ] All text remains editable
- [ ] All logos are vector
- [ ] All UI elements are componentized
- [ ] Exports are clean at high resolution
- [ ] File naming is consistent

---

## 12. Practical Build Sequence

Recommended order:

1. Create Figma pages.
2. Add reference PNGs and lock them.
3. Create color variables.
4. Create text styles.
5. Build simplified logo mark.
6. Create logo variants.
7. Create core UI components.
8. Rebuild desktop brand board.
9. Rebuild mobile UI board.
10. Create export frames.
11. Export SVG logo pack.
12. Export PNG/PDF concept boards.
13. Review consistency against reference PNGs.
14. Adjust spacing and typography.
15. Freeze v1.0.

---

## 13. Expected Fidelity

The goal is not pixel-perfect duplication of the AI PNGs.

The goal is:

- same visual direction
- same hierarchy
- same mood
- same brand system
- cleaner typography
- cleaner vectors
- production-ready exports

Expected fidelity target:

**85–95% visual match, with higher production quality than the PNGs.**

