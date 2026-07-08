# Reminder — after P1 gate (#30)

> **Invoke once P1 leaves #14–#30 are done** and **[Gate] P1 — Approve spec v1** (#30) is closed.
> Do **not** run during P1 grilling or spec work — it would compete with open leaves.

---

## Trigger

All of the following are true:

- [ ] Issues **#14–#29** closed (grills + spec docs + OpenSpec proposal)
- [ ] **[Gate] P1 — Approve spec v1** (#30) closed — spec v1 human-approved
- [ ] Epic **#2 — [Epic] P1 — Requirements & spec v1** ready to close

---

## What to run

Paste in a new session:

```text
rbo-product-bootstrap — brownfield on alba-assistant
Read docs/planning/reminder-after-p1-gate.md and run Step 1 only (inventory, no mutations).
Compare Alba P0–P14 phase map vs rbo-product-bootstrap phase-template.md.
Recommend: keep current map, partial adopt, or full realign — then stop for my OK.
```

---

## Expected outcome

1. **Brownfield inventory** (bootstrap Step 1) — board, canon, phase completion, no edits
2. **Gap report** — Alba compressed map (P2=arch, P5=impl gate) vs suite map (P2=UI, P10=impl gate)
3. **One recommendation** — keep / partial / full realign
4. **Stop at approval gate** — no issue recreation, no board churn, until you explicitly OK a plan

If you approve realignment, that becomes its **own epic + change** — not a side effect of bootstrap.

---

## References

| Doc | Role |
|-----|------|
| [`phases.md`](./phases.md) | Current Alba P0–P14 map |
| [`DECISIONS.md`](../../DECISIONS.md) | Deferred realignment note (2026-07-08) |
| `ai-skills/skills/rbo-product-bootstrap/phase-template.md` | Suite default P0–Pn map |
| `ai-skills/docs/rbo-product-skills.md` | Suite guide |

---

## Do not

- Run full bootstrap before #30 closes
- Auto-restructure the board without explicit approval
- Block P2 work if you choose **keep current map** — proceed with **#3 — [Epic] P2 — Architecture v1** on Alba numbering
