# Routine: Dreaming Pass (The Learning Loop)

Schedule: weekly, Friday 16:00 ET

This routine refines memory only. It does not publish and does not rewrite the brand canon.

---

Run the BrokerBot dreaming pass.

1. Read every package in companies/brokerbot/review/ from the past 7 days, including any
   human edits or lines beginning with NOTES:, plus memory/run-log.md.
2. Extract patterns: voice corrections that recur, angles approved vs killed, stats that
   got flagged, and formats that performed if performance notes are present.
3. Write a dated PROPOSED update to memory/brokerbot-memory-proposed.md. Keep it
   operational: preferences, do and don't refinements, angle-rotation notes, sourcing
   reminders. This is memory, not brand law.
4. Do NOT edit core/marketing-core.md, companies/brokerbot/brand.md, or the editorial law.
   If a pattern implies a brand-canon change, list it under "For human decision" instead
   of applying it.
5. Self-grade: score the week's drafts against the core QA gate and the BrokerBot
   Pre-Flight, and note any recurring failure for the human.

A human reviews brokerbot-memory-proposed.md and merges approved items into
brokerbot-memory.md. Nothing in proposed memory takes effect until merged.

Do not publish.

---

## Note on Managed Agents / native Dreams

Native Dreams is a Managed Agents research-preview feature (Opus 4.7 and Sonnet 4.6 only)
not available inside Claude Code today. This dreaming pass implements the same pattern as
a scheduled Routine with human review on memory updates. If you later move the worker onto
Managed Agents, swap this Routine for native Dreams and keep the same human review step on
brokerbot-memory-proposed.md.
