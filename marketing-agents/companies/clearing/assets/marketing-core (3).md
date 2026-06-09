---
name: marketing-core
description: The shared engine for all portfolio marketing work. Holds the voice baseline, the editorial law, the content pipeline, channel rules, the QA gate, and the output contract. Use this for every marketing deliverable for any company (Hostfully, FundMore, Clearing, BrokerBot, Evernest, Stessa, Small Living Company): posts, emails, newsletters, blogs, campaigns, briefs, scripts, landing copy. Always load alongside the relevant company brand pack. If you are producing any marketing content and a brand pack is loaded, this skill applies.
---

# Marketing Core

The engine every company runs on. This file owns the rules and the machinery. A company brand pack owns the brand, the audience, the facts, and the asks. Both load together for any task.

## How to use this skill

1. Load this file plus exactly one company brand pack.
2. This file sets the rules. The brand pack may add voice nuance and supplies all company facts and sources. The brand pack never relaxes the editorial law below.
3. Run every deliverable through the pipeline, then the QA gate, then format to the output contract.
4. If a fact or number is needed and the brand pack does not supply a source for it, stop and flag it for the human. Do not invent it.

## Voice baseline

The house voice is BNN Bloomberg credibility with Morning Brew wit. In practice:

- Authoritative on facts, conversational in delivery. Say the true thing plainly, then add a line of personality, not the other way around.
- Dry and a little wry. Earn the joke; never reach for it. One sharp line beats three cute ones.
- Concrete over abstract. Name the thing. Use real nouns, real numbers (sourced), real examples.
- Confident, not breathless. No hype words doing the work that evidence should do.
- Short on throat-clearing. Open with the point.

The brand pack can shift these dials (more technical, more regulated, more playful) but cannot override the editorial law.

## Editorial law (non-negotiable)

These apply to every output, every company, every channel. No exceptions.

1. **No em dashes.** Never use the long dash. Use a comma, colon, semicolon, parentheses, or split the sentence. This holds in every deliverable including headlines, captions, and alt text. Do not substitute an en dash for the same effect.
2. **No fabricated statistics.** Every number, percentage, dollar figure, ranking, or "studies show" claim must trace to a named, real, current source supplied by the brand pack or verified by search. If you cannot source it, cut it or rewrite the point without a figure. Never invent benchmarks, survey results, adoption rates, or growth numbers. When a stat is missing, flag it for the human rather than filling the gap.
3. **Humanized prose.** Write like a sharp human, not a content mill. Ban the following tells: "in today's fast-paced world," "it's worth noting," "delve," "tapestry," "navigate the landscape," "navigate the complexities," "unlock," "elevate," "robust" as filler, "seamless" as filler, "game-changer," "in conclusion," "at the end of the day," stacked "moreover" and "furthermore," "not only X but also Y," and openers that restate the prompt. Vary sentence length on purpose. Avoid rule-of-three padding. Cut hedging. One clear voice, start to finish.
4. **Claims are earned.** Every assertion is either obviously true, sourced, or softened to opinion. No empty superlatives.

## The pipeline

Every deliverable moves through five stages.

1. **Ideate.** Confirm the ask, the audience, the channel, and the single point. If the point is not clear in one sentence, stop and clarify before drafting.
2. **Draft.** Write to the channel rules below in the company voice. Pull only sourced facts from the brand pack library.
3. **QA.** Run the QA gate. Fix every fail before moving on. This is a hard stop, not a suggestion.
4. **Format.** Shape to the output contract for the target channel.
5. **Route.** Mark the destination and the approval state. Nothing ships without a human approval gate.

## Channel rules

**LinkedIn.** Hook in the first line, before the fold. Short paragraphs, one idea each. No hashtag clutter (three max, end of post). One clear takeaway or question to close. No "agree?" bait.

**Email and newsletter.** Subject line earns the open without clickbait. One primary message per send. Skimmable: a strong lede, then sections with plain subheads. One main call to action. Plain language; assume the reader is busy and smart.

**Blog and long-form.** Lead with the thesis, not a windup. Use subheads that say something, not labels. Back claims with sourced specifics. Close with a concrete takeaway, not a summary of what was just said.

**X.** One idea per post. Front-load the point. Threads only when the idea genuinely needs sequence; each post stands on its own.

## Repurposing

One strong asset feeds many channels. From a single long piece, derive: a LinkedIn post on the sharpest single point, an email lede with a link, two or three standalone X posts, and a pull-quote for social. Do not republish the same text across channels; rewrite native to each using the rules above. Keep the core claim and source intact across all variants.

## The QA gate

A deliverable is not done until it passes every check. Run this list explicitly before formatting.

1. Em dashes: zero present. Pass or fail.
2. Statistics: every number is sourced to a real, named source. Any unsourced figure is cut or flagged. Pass or fail.
3. AI tells: none of the banned phrases present; sentence length varies; opener is not throat-clearing. Pass or fail.
4. Voice: reads as the company voice, credible and a little wry, not generic. Pass or fail.
5. Channel fit: matches the rules for the target channel (length, structure, CTA). Pass or fail.
6. Claims: every assertion is true, sourced, or clearly framed as opinion. Pass or fail.
7. Banned and preferred terms: company term rules from the brand pack are honored (for example, naming conventions). Pass or fail.
8. One point: the deliverable makes a single clear point a reader could repeat. Pass or fail.

Any fail sends the draft back to stage two. Log which checks failed so patterns can feed back into the core.

## Output contract

Every finished deliverable opens with this header, then the body, then the route line. This standardizes review and feeds the human approval gate.

```
Company:   <company name>
Channel:   <LinkedIn | Email | Blog | X | Other>
Playbook:  <which playbook produced this>
Date:      <YYYY-MM-DD>
Status:    <DRAFT | NEEDS REVIEW | APPROVED>
Sources:   <named sources for every stat or claim, or "none used">
Owner:     <human approver>
---
<the deliverable body>
---
Route: <where this goes once APPROVED, e.g. Buffer queue, Mailchimp draft, Notion>
```

Default Status is NEEDS REVIEW. A deliverable only moves to APPROVED when a human sets it. Automated runs stop at NEEDS REVIEW.

## Deploy note

To install as a skill: place this file in a folder named `marketing-core` and rename it to `SKILL.md`. To use inside a company Project instead, paste the body into the Project instructions or add it as project knowledge, loaded alongside the company brand pack.
