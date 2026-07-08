## Why

Gisele's Virtuologia practice involves **patient-related content** (Google Meet transcriptions, session notes). D-019 and D-023 block clinical indexing until privacy is designed. P1 spec needs locked **LGPD posture**, workspace isolation rules, and a gated path (or explicit exclusion) before production.

## What Changes

- Grilling on issue **#16 — [Grill] P1 — Privacy, LGPD & sensitive content**
- Resolve clinical/sensitive content policy, Gisele workspace privacy, Meet transcription handling
- Record in `DECISIONS.md`, `open-questions.md`, issue **#16** comments
- Update planning canon for spec input

No runtime code. Documentation and decision capture only.

## Capabilities

### New Capabilities

- `privacy-lgpd-sensitive`: LGPD posture, sensitive content classes, Gisele clinical path, isolation guarantees, consent/retention principles

### Modified Capabilities

- _(none)_

## Impact

- **Docs:** `DECISIONS.md`, `docs/planning/open-questions.md`, privacy sections of future `docs/spec/requirements.md`
- **Downstream:** unblocks or gates Gisele Meet transcription indexing; informs **#17** MVP scope
- **Board:** **#16** → Done on close
