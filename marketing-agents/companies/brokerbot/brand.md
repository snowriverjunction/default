# BrokerBot Brand Canon

This file is read-only for the worker. Only a human may edit it.

---

## What BrokerBot is

BrokerBot is a white-label AI assistant that mortgage brokers embed in their client experience. It handles pre-qualification questions, renewal reminders, and document checklists so brokers spend time on relationships, not repetition.

---

## Positioning

BrokerBot helps Canadian mortgage brokers keep clients between transactions so they stop losing renewals to the banks.

One line: "Your clients. Your brand. Between every transaction."

---

## Ideal customer profiles (ICPs) -- rotate, brokers most often

1. Independent mortgage brokers (volume 25-100 deals/year)
2. Small brokerage principals (2-10 agents)
3. Mortgage agents newly licensed, building a book
4. Credit union mortgage advisors
5. Real estate agents who co-refer mortgage clients

---

## Voice

- Direct and practitioner-level. Write to someone who has closed 200 deals, not a first-time buyer.
- Canadian specificity is a competitive advantage. Name the context (OSFI B-20, renewal cliff, Big Six, stress test). Do not generalize to "North America."
- Loss aversion over feature lists. Lead with what brokers stand to lose, then show the fix.
- Short sentences. One idea per sentence. No throat-clearing.
- Warmth without softness. Acknowledge the broker's expertise; do not condescend.

---

## BrokerBot Pre-Flight checklist

Run after the core QA gate. Fix every fail.

| # | Check | Pass condition |
|---|-------|----------------|
| 1 | Canadian context | At least one Canada-specific reference (institution, regulation, or market condition) |
| 2 | ICP match | Content is addressed to one named ICP, not a generic "advisor" |
| 3 | Loss-aversion hook | Lead surfaces a cost, risk, or missed opportunity -- not a feature |
| 4 | No Tier 3 figures | Confirmed: zero unsourced Tier 3 stats |
| 5 | Source credit visible | Stat source named inline or in a visible credit line |
| 6 | No AI tells | Zero phrases from the core AI tell list |
| 7 | CTA is direct | CTA names an action ("Book a Demo", "Reply to this post"), not a vague invitation |

---

## Output contract

Every deliverable written to review/ must open with this header block:

```
---
playbook: <name>
date: <YYYY-MM-DD>
status: NEEDS REVIEW
stat_used: <figure and source>
angle: <one-line description>
---
```

---

## Brand colours

- Pink: #FC0A7E
- Purple: #86308B
- Dark: #0B1818
- White: #FFFFFF

## Typography (web/card)

- Headlines: Gothic A1 (Google Fonts)
- Body: Mulish (Google Fonts)
- Data/code callouts: JetBrains Mono (Google Fonts)

## Logo

File: companies/brokerbot/assets/brokerbot_logo_icon_400x100.png
Embed as base64 in HTML cards. Do not hotlink.

---

## What the worker must never do

- Edit this file.
- Edit core/marketing-core.md.
- Publish or set Status APPROVED.
- Use Tier 3 figures without a named source.
- Invent statistics.
- Use em dashes.
