# Alba — Design System v3 (reconciled)

**Status:** canonical design-token source of truth.
**Supersedes:** `../v1`, `../v2` (kept frozen as historical concepts — never edit them).

## What v3 is

v3 merges two things that had drifted apart:

1. **Shipped** — the design that is actually live in production: `app/globals.css` plus the approved mock `ui/mockups/staging-layout-v75.html`. Validated, in production.
2. **v2 GPT design system** — a richer, more structured design-system spec (logo system, type hierarchy, iconography, sub-brand/product accents, asset exports, voice) that was generated but **never implemented**.

The decision: **shipped wins every value conflict.** v3 keeps v2's *structure* (the things shipped never documented) and overwrites v2's *values* wherever they disagree with what ships.

## Files

| File | Role |
|---|---|
| `alba-design-tokens.json` | **Canonical tokens** — colors (light+dark), type scale, semantic colors, product accents, radii, shadows, spacing. Machine-readable source of truth. |
| `alba-tokens.css` | The same tokens as CSS custom properties. The `:root`/`.dark` color blocks are 1:1 with `app/globals.css`; the radius/shadow/product/spacing scales are new (formalize what's currently hardcoded inline). This is the bridge artifact for adopting the system in code. |
| `reference/production-spec.md` | v2 GPT production spec — kept for its **structural** value (logo system, typography hierarchy, iconography, sub-brand system, asset exports, voice). Where it states colors/radii/shadows, the reconciliation table below overrides it. |
| `reference/figma-blueprint.md`, `figma-rebuild-checklist.md`, `figma-layout-tokens.json` | Figma rebuild kit (reference). Layout tokens had their accent/canvas/ink values adjusted to shipped. |
| `reference/component-inventory.csv` | Component inventory — useful checklist when documenting primitives. |
| `reference/alba-mark.svg` | Simplified logo mark starter (accent/ink adjusted to shipped `#E8950A` / `#101828`). |

## Reconciliation — where shipped overrides v2/GPT

| Token | v2 / GPT | **Shipped wins (v3)** |
|---|---|---|
| Docs accent | `#FFB45C` sunrise-gold | `#E8950A` (light) / `#F0A52E` (dark) |
| Main canvas | `#FFFDF9` paper / `#F8FAFC` | `#F0EDE8` warm beige (light) / `#1B1916` (dark) |
| Ink / primary text | `#0F172A` | `#101828` |
| Success green | `#35A66F` | `#4CB783` |
| Radius scale | 6 / 10 / 16 / 24 / 32 | 4 / 6 / 8 / 10 / 12 / 50 (actual usage) |
| Shadows | soft `0 12px 30px` / `0 24px 70px` | tighter `0 1px 3px` → `0 16px 48px` |
| Type sizes | 64 / 40 / 16 px (marketing) | 38 / 22 / 17 / 12 px (compact UI) |
| Dark theme | *(none in GPT spec)* | full warm-dark scale — **shipped adds what GPT lacks** |

## What v3 keeps from v2/GPT (no conflict)

- **Logo system** — variants, clear space, minimum sizes, misuse rules
- **Type hierarchy** — role structure (the sizes are reconciled, the roles kept)
- **Iconography** — line-icon style (shipped already uses Tabler icons, consistent)
- **Sub-brand / product accents** — the docs/photos/expenses/virtuo accent system, needed by the `app-auth` skills selector. Docs reconciled to shipped; others are placeholders until those skills ship.
- **Asset export requirements**, **voice & content**, **Figma rebuild kit**

## Per-skill provenance (the `shipped` flag)

The concept boards (`alba_ai_*_upscaled.png`) are **reference and completeness only** — their exact hex values follow the v2 concept, not shipped. Each skill's design follows a provenance ladder:

1. **Shipped wins where it exists.** Today that is **Docs** only — its accent (`#E8950A`/`#F0A52E`) and UI come from the live app and override the concept boards.
2. **Concept fills the gaps.** **Photos / Expenses / Virtuo** have no shipped UI yet, so their accents, lockups, and screens are taken from the concept boards as a *starting reference* (the placeholder values in `alba-design-tokens.json → products`).
3. **Shipped overrides on build.** When a skill is actually built, its shipped design replaces the concept placeholder — the same path Docs already walked.

This is encoded by `"shipped": true|false` on each product in `alba-design-tokens.json`. `true` = locked to the live app; `false` = concept placeholder, open to revision.

**Sub-brand & suite-shell reference:** both concept boards carry the sub-brand system. The brand/desktop board is the most relevant for the future `app-auth` change — its **§7 (sub-brand lockups)** and **§9 (desktop landing page + suite sidebar with all four skills)** are the design reference for the login landing page and skills selector. Colors there are superseded by the reconciled tokens; structure is canonical.

## How to adopt it (not done yet)

Authoring v3 is housekeeping. *Wiring it into the app* is a separate change that should run the full OpenSpec cycle (`/opsx:explore → propose → apply → archive`):

1. Import `alba-tokens.css` into `app/globals.css` (or generate globals.css from `alba-design-tokens.json`) so there is one token source.
2. Replace hardcoded radii/shadows in components and the mock with the token vars.
3. Optionally build a `/design` living style-guide route that renders every token + component, so it can never drift from the app.

Until then, **`app/globals.css` remains the operative source for the running app** — v3 documents and extends it; it does not yet replace it.
