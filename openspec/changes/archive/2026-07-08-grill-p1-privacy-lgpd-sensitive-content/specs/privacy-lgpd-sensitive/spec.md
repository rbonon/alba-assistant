## ADDED Requirements

### Requirement: Sensitive content classes are defined

The product SHALL classify content types (clinical/patient, family personal, shared casa, technical) with indexing and access rules per class.

#### Scenario: Classification locked

- **WHEN** grilling on issue **#16** completes
- **THEN** `DECISIONS.md` lists sensitive classes and default handling

### Requirement: Gisele workspace isolation is specified

The product SHALL document that Ricardo MUST NOT access Gisele `gisele` workspace private content, including any future clinical index.

#### Scenario: Cross-user isolation

- **WHEN** multi-user retrieval is specified
- **THEN** rules state Ricardo cannot read Gisele private or clinical-indexed content (D-016 baseline)

### Requirement: Clinical Meet transcription path is decided

The product SHALL document whether patient Meet transcriptions may enter Alba, and under what controls if yes.

#### Scenario: Transcription policy

- **WHEN** grilling resolves Meet transcription question
- **THEN** decision records allow/deny/gated-post-MVP with required controls listed

### Requirement: LGPD posture is stated for family product

The product SHALL document data-minimization, purpose limitation, and retention principles for Brazilian LGPD context.

#### Scenario: LGPD principles recorded

- **WHEN** grilling completes
- **THEN** planning canon includes LGPD posture summary for spec writers
