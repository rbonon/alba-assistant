## ADDED Requirements

### Requirement: MVP capability bundle is enumerated

The product SHALL document which capabilities ship at P6–P7 production go-live vs deferred.

#### Scenario: MVP IN list locked

- **WHEN** grilling on issue **#17** completes
- **THEN** planning canon lists MVP IN capabilities with reference to prior decisions (D-015–D-030)

### Requirement: Post-MVP capabilities are categorized

The product SHALL group deferred capabilities (writes, integrations, clinical slice, voice) with rough phase ordering.

#### Scenario: MVP OUT list locked

- **WHEN** grilling completes
- **THEN** MVP OUT items are explicit non-goals for P6–P7

### Requirement: MVP aligns with indexed sources decision

MVP capabilities MUST NOT require sources outside D-019 (Obsidian + Git) unless grilling explicitly expands MVP.

#### Scenario: No scope creep

- **WHEN** MVP boundary is reviewed
- **THEN** Calendar/Tasks/Drive/clinical indexing remain post-MVP unless user explicitly moves them in
