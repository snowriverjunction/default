---
name: clearing-brand
description: Clearing company pack for the portfolio marketing system. Brand, audience, sources, channels, playbooks, and cron schedule for Clearing, trust accounting and automated bookkeeping software for short-term rental property managers. Load alongside marketing-core for any Clearing marketing deliverable: LinkedIn posts, blog and SEO content, email, social cards, interactive tools, decks. Also trigger on trust accounting, STR bookkeeping, owner statements, reconciliation, property-manager finances, or any Clearing voice, colour, audience, or messaging question. Deeper product, pricing, integration, and glossary detail lives in clearing-context.
---

# Company Brand Pack: Clearing

This pack configures the marketing-core engine for Clearing. Clearing is a US-market fintech that handles other people's money, so accuracy, trust, and the banking disclosure are central.

## How to use this pack

1. Load this pack with `marketing-core` for any Clearing task.
2. For product modules, pricing, integrations, competitors, and the glossary, pull from `clearing-context`. This pack stays lean and points there.
3. Inherited rules from marketing-core always apply: no em dashes, no fabricated statistics, humanized prose, the QA gate, the output contract. Clearing adds its own Pre-Flight below, including a non-negotiable banking disclosure.

## Company identity

- Name: Clearing. Web: getclearing.co.
- One line: trust accounting and automated bookkeeping software tailored for short-term rental property managers.
- What it is: a financial operating system for STR property managers. It sits between the property management software and the bank, and between the manager and their homeowners. It is not a property management software, and you do not need one to use it.
- Compliance status: Clearing is a financial technology company, not a bank. Deposit accounts are issued by Evolve Bank & Trust, Member FDIC, with balances insured up to $250,000. VRMA member.
- Market: United States. Use US spelling and US regulatory context (state trust-accounting rules, FDIC). Do not state or imply ownership by any other company; Clearing integrates with several PMS platforms, which is an integration, not a parent relationship.

## Brand kit

Building from scratch. Fill every value from your Claude Design system and the live site, then replace this section.

- Primary colour: [confirm]
- Secondary and accent: [confirm]
- Type: [confirm display and body faces]
- Logo: [confirm files and clear-space rule]
- Action: pull the palette and type from getclearing.co and your Claude Design system, lock them here, and wire the components before the agent renders any card.

## Voice delta

Start from the marketing-core baseline, then shift for Clearing:

- Calm and relief-oriented. The promise is "take vacation from managing your property finances" and "say hello to automation, goodbye to hours in spreadsheets." Lead with relief from a hated chore.
- Trustworthy and precise. Clearing handles funds, so the voice is exact with numbers and never loose with compliance language.
- Benefit-led and plain. Speak to a busy professional operator, not an accountant, but stay credible to the accountant who reviews the books.
- Warm, not hype. No vendor cliches, no overpromising. Confidence comes from accuracy.

## Audience and personas

1. Professional STR property managers (primary). 10 to 200+ units across multiple owners. Pain: bookkeeping and trust accounting eat hours, spreadsheets and generic tools do not fit multi-owner STR, owners want transparency. Angle: automate the books, pay homeowners cleanly, stay compliant.
2. Smaller and growing operators (entry). On spreadsheets or QuickBooks, feeling the strain as they scale. Angle: get off spreadsheets before they break.
3. Accountants and bookkeepers (partner channel). Serve STR property managers. Angle: a purpose-built ledger that makes their work faster and cleaner; an accountant partner program.
4. Real estate investors (secondary). Track cashflow across properties.
Homeowners are the end beneficiaries of transparency, the relationship Clearing helps managers protect, not the buyer.

## Positioning and key messages

- Core: the financial operating system for STR property managers. Trust accounting is the primary product, not a bolt-on feature of a PMS.
- Pillar 1, Trust accounting made easy: collect funds and pay homeowners with per-owner sub-balances, set up correctly.
- Pillar 2, Automation over spreadsheets: transactions from Stripe, Airbnb, banks, and cards in one place, enriched and reconciled, closing the books faster.
- Pillar 3, Owner satisfaction: real-time transparency and clean owner statements build trust and retention.
- Pillar 4, Compliance: as state trust-accounting rules tighten, purpose-built trust accounting reduces risk.
- Proof points exist (hours saved per month, dollars saved, named customer stories). Confirm each is current and that named customers have given permission before external use.

## Banned and preferred terms

- Always: "Clearing." Describe it as trust accounting and bookkeeping software, or a financial operating system for STR property managers.
- Never: call Clearing a bank, or imply it holds deposits itself; call Clearing a PMS; use em dashes; overstate compliance or insurance.
- Banking disclosure (non-negotiable): any claim about holding funds, deposits, balances, or insurance must carry the disclosure that Clearing is a financial technology company and not a bank, that deposit accounts are issued by Evolve Bank & Trust, Member FDIC, and that balances are insured up to $250,000. Credit the banking partner; never claim the insurance without it.

## Approved source library and stats integrity

Every number on a finished asset traces to one of these, named where external.

- Tier 1, Clearing proprietary and customer (present as Clearing's own, confirm current and permissioned): hours saved per month, dollars saved per year, named customer stories and their unit counts. Do not reuse an old figure without confirming it still holds, and do not name a customer without permission.
- Tier 2, external authorities (name the source on use): VRMA, state trust-accounting regulations, STR market data (for example AirDNA, Skift, VRMA research), QuickBooks facts for comparisons, and the banking-partner facts (Evolve Bank & Trust, FDIC).
- Tier 3, flagged: market-size figures, "category leader" or "first" claims, and specific state-regulation details, until tied to a named source. Until then, the QA gate flags it.

When a run needs a figure it cannot source, it stops and flags for the human. It never invents one, and it never invents a regulatory or insurance detail.

## Channels and accounts

- LinkedIn (primary): the Clearing company page, where finance-operations education and compliance content live.
- Blog and SEO: getclearing.co, the engine for trust-accounting and STR-bookkeeping search demand.
- Email and newsletter: confirm the sending tool.
- Accountant partner program: co-marketing with bookkeepers and accountants.
- Interactive tools: a bookkeeping-hours calculator and a trust-accounting readiness quiz are strong owned assets for this audience. Confirm handles and the publishing path.

## Playbooks

| Playbook | Cadence | Output | Channel |
|---|---|---|---|
| STR finance education post | Mon 09:00 ET | Short LinkedIn post | LinkedIn |
| Trust-accounting and compliance post | Wed 09:00 ET | Post or 1:1 card | LinkedIn, social |
| Tool or seasonal spotlight | 1st of month | Post or card | LinkedIn, social, blog |

Playbooks 1 and 2 are specced below. The others follow the same block format when you are ready.

### Playbook block: STR finance education post

```
Playbook:  STR finance education post (weekly LinkedIn)
Goal:      Take one bookkeeping or financial-operations pain point a STR property manager
           feels, explain it plainly, and show the relief Clearing provides. Build authority
           and reach with operators and the accountants who serve them.
Input:     This week's pain point or teaching angle (for example reconciling across Stripe
           and Airbnb, closing the books faster, clean owner statements). Check memory for
           recent topics and avoid repeats.
Steps:     1. Pick the angle. If it uses a figure, pull it from the source library and
              confirm it is current.
           2. Draft: name the chore and the hours it eats, teach one useful thing, show the
              automated way, close with a calm, benefit-led CTA. Relief, not hype.
           3. If banking, deposits, or insurance comes up, include the required disclosure.
           4. Run the core QA gate, then the Clearing Pre-Flight.
Output:    LinkedIn post text, hook before the fold, in the output-contract header. Sources
           line cites any stat. Status NEEDS REVIEW.
Route:     Clearing LinkedIn company page once APPROVED.
Cadence:   Weekly, Monday 09:00 ET (confirm the time for the US audience).
```

### Playbook block: Trust-accounting and compliance post

```
Playbook:  Trust-accounting and compliance post (weekly)
Goal:      Use Clearing's durable edge, that trust accounting is the primary product, to
           teach a compliance or trust-accounting concept STR managers worry about. Build
           credibility as the category authority.
Input:     This week's concept or development (for example per-owner sub-balances,
           commingling risk, a state trust-accounting requirement). For regulation, pull the
           specifics from a Tier 2 source and record them and the date.
Steps:     1. Pick the concept. If it cites a regulation, source it and do not overstate it.
           2. Explain the risk or rule plainly, then show how purpose-built trust accounting
              addresses it, without promising legal outcomes.
           3. Include the banking disclosure if funds, deposits, or insurance are mentioned.
           4. If a card is used, build it in the locked brand kit with a source credit line.
           5. Run the core QA gate, then the Clearing Pre-Flight.
Output:    Post text (and card if used), in the output-contract header. Sources line names
           any source and date. Status NEEDS REVIEW.
Route:     Clearing LinkedIn and social once APPROVED.
Cadence:   Weekly, Wednesday 09:00 ET (confirm the time).
```

## Clearing Pre-Flight (runs on top of the core QA gate)

1. Brand name correct; Clearing is never called a bank or a PMS.
2. Banking disclosure present wherever funds, deposits, balances, or insurance are mentioned (financial technology company, not a bank; deposit accounts issued by Evolve Bank & Trust, Member FDIC; insured up to $250,000).
3. ROI and customer stats sourced, current, and permissioned; no named customer without permission.
4. Trust-accounting and regulation references accurate and not overstated; no promise of legal or compliance outcomes.
5. Voice is calm, precise, and benefit-led; relief framing, not hype.
6. US-market context correct; locked brand kit observed.

## Cron schedule

Each run loads marketing-core plus this pack plus the playbook, runs on Anthropic infrastructure, and stops at NEEDS REVIEW. A human approves before anything publishes. Confirm posting times against the US audience.

- MON 09:00 ET, STR finance education post, NEEDS REVIEW
- WED 09:00 ET, Trust-accounting and compliance post, NEEDS REVIEW
- 01 / MONTH 09:00 ET, Tool or seasonal spotlight, NEEDS REVIEW

## Deploy note

To install as a skill: place this file in a folder named `clearing-brand`, rename it to `SKILL.md`, and keep `clearing-context.md` in a `references/` subfolder. To use in a Project, add this pack plus clearing-context as project knowledge alongside `marketing-core`.
