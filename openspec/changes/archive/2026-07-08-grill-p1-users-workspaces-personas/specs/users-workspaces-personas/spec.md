## ADDED Requirements

### Requirement: MVP primary user scope is defined

The product SHALL document which human user(s) are in scope for MVP production go-live before P1 spec writing completes.

#### Scenario: Q-001 resolved

- **WHEN** grilling on issue **#14** completes Q-001
- **THEN** `DECISIONS.md` states whether MVP production is Ricardo-only or Ricardo + Gisele from day one

### Requirement: Workspace model is documented

The product SHALL define the four workspaces (`ricardo`, `gisele`, `casa`, `compartilhado`) with primary users and intended content boundaries.

#### Scenario: Workspace table locked

- **WHEN** grilling on issue **#14** completes
- **THEN** planning canon lists each workspace with primary user(s) and purpose (not vision-only suggestions)

### Requirement: Persona mapping is documented

The product SHALL map each active MVP workspace to a persona (Alba Dev, Alba Texto, Alba Casa) or explicitly defer persona for out-of-MVP workspaces.

#### Scenario: Persona assignment recorded

- **WHEN** grilling resolves persona scope for MVP
- **THEN** `DECISIONS.md` or approved planning doc states persona per in-scope workspace

### Requirement: Cross-workspace read rules are defined for MVP

The product SHALL document which workspaces an MVP user may read (e.g. `ricardo` + `compartilhado`) and that private workspace isolation is a hard rule for future multi-user production.

#### Scenario: MVP read paths documented

- **WHEN** MVP user scope is Ricardo-only
- **THEN** canon states Ricardo's allowed read workspaces and that `gisele` private content is out of MVP production scope
