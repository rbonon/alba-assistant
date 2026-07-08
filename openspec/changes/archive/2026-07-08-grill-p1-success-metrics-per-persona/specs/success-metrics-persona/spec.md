## ADDED Requirements

### Requirement: Core MVP success metrics are defined

The product SHALL document measurable criteria for P6–P7 go-live that apply to all MVP users.

#### Scenario: Core metrics locked

- **WHEN** grilling on issue **#18** completes core bundle
- **THEN** `DECISIONS.md` lists core metrics (search quality, isolation, availability, staging gate)

### Requirement: Persona-specific MVP metrics are defined or explicitly deferred

The product SHALL document success metrics per persona (Ricardo/Alba Dev, Gisele/Alba Texto, Casa/Alba Casa) with deferrals for post-MVP capabilities.

#### Scenario: Persona metrics documented

- **WHEN** grilling completes
- **THEN** each persona has MVP metrics or explicit "deferred post-MVP" with reason

### Requirement: Metrics align with MVP scope

MVP success metrics MUST NOT require capabilities listed MVP OUT in D-031.

#### Scenario: No metric scope creep

- **WHEN** metrics are reviewed against D-031
- **THEN** no metric requires clinical slice, integrations, voice, or writes at MVP
