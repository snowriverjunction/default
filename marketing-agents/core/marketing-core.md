# Marketing Core

Universal editorial standards, QA gate, and output contract for all marketing workers in this
repo. Company-specific brand files and routines layer on top of this.

---

## Editorial law

- No em dashes. Use a comma, a colon, or a new sentence.
- No fabricated statistics. Every number traces to a named, verifiable source.
- No hype superlatives (revolutionary, game-changing, best-in-class) without a sourced claim.
- Active voice as the default.
- US spelling throughout.

---

## Core QA gate

Run before writing any deliverable. Every item must pass.

1. **Source check** -- every statistic, percentage, and named figure has a named source
   recorded in the deliverable or the run log.
2. **Claim check** -- no promise of legal, compliance, tax, or investment outcomes.
3. **Voice check** -- calm, precise, benefit-led. No hype. No em dashes.
4. **Disclosure check** -- any mention of funds, deposits, balances, or insurance triggers
   the required company-level banking disclosure (see each company's brand.md).
5. **Brand check** -- no visual production if the brand kit is unlocked; text only with a
   flag.
6. **Repeat check** -- topic not covered in the last four runs (check run-log.md).

---

## Output contract

Every deliverable file begins with this header block:

```
---
Status: NEEDS REVIEW
Playbook: <playbook name>
Date: <YYYY-MM-DD>
Topic: <one-line description>
Sources: <comma-separated list of sources used>
---
```

Body follows immediately after the header.

The worker never sets Status: APPROVED and never publishes.

---

## Learning loop

The Friday dreaming pass (see routines/dreaming-pass.md per company) writes proposed memory
updates to memory/memory-proposed.md. A human reviews and merges approved items into
memory/memory.md. No learning takes effect until merged.

If the same lesson appears across multiple companies, a human (not the worker) moves it into
this core file so all workers benefit.
