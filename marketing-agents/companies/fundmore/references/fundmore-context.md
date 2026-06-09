# FundMore Context Reference

This file is the canonical source of record for FundMore company facts, product details,
and approved statistics. The worker reads this file on every run. Do not use any fact,
figure, or product detail that contradicts or extends what is here without flagging it for
human review.

---

## Company overview

FundMore is a Canadian AI-powered mortgage and lending technology company. It builds
infrastructure for lenders -- banks, credit unions, and mortgage companies -- to automate
and accelerate loan origination decisions.

Core value proposition: faster, more consistent, more defensible lending decisions through
AI and automation, with full audit trails for compliance.

Primary markets: Canada (established), United States (expansion stage).

---

## Products

### Fathom
AI decisioning engine. Automates underwriting logic, surfaces risk signals, and produces
explainable decisions. Designed for OSFI and B-20 compliance environments.

### FundMore IQ
Intelligence and analytics layer. Provides lenders with portfolio-level insight, performance
benchmarking, and decisioning analytics.

### FundMore AI
The overarching AI platform brand. Used when referring to the full suite or the AI
capability as a whole.

### US Headless LOS
A headless loan origination system built for the US market. "Headless" means it exposes
APIs that integrate into lenders' existing front-end systems rather than replacing them.

---

## Statistics and metrics

**IMPORTANT -- WORKER INSTRUCTION**: The canonical processed-volume figure is **NOT YET
CONFIRMED** for this version of the context file. Do not publish any processed-volume dollar
figure in any deliverable until a human has updated this file with a confirmed, sourced
number and removed this notice. Flag the gap in the Pre-Flight output if the routine
requires a volume stat.

All other statistics used in deliverables must be sourced at run time via web search from
Tier 1 or Tier 2 approved sources (see below) or from a human-confirmed entry in this file.

---

## Approved source tiers

**Tier 1 (primary, preferred)**
- OSFI (Office of the Superintendent of Financial Institutions)
- Bank of Canada
- FINTRAC
- CMHC (Canada Mortgage and Housing Corporation)

**Tier 2 (acceptable with attribution)**
- Canadian Mortgage Trends (CMT)
- Canadian Mortgage Professional (CMP)
- Mortgage Professionals Canada
- Major Canadian financial press (Globe and Mail, Financial Post, BNN Bloomberg)

**Not acceptable**: unnamed "industry reports," paywalled sources that cannot be linked,
or statistics the worker cannot verify via web search this run.

---

## Regulatory context (Canada)

- **B-20**: OSFI's residential mortgage underwriting guideline. Requires stress testing
  (qualifying rate), LTV limits, and documentation standards. Key compliance driver for
  FundMore's lender customers.
- **OSFI**: Regulator for federally regulated financial institutions.
- **FINTRAC**: Canada's financial intelligence unit. Anti-money-laundering and
  terrorist-financing compliance.
- **Stress test rate**: Set by OSFI; check current rate via web search at run time --
  do not hard-code a rate that may be outdated.

---

## Personas (thought-leadership rotation)

Rotate in this order; track in memory/fundmore-memory.md to avoid repeats:
1. CRO / Chief Risk Officer
2. CIO / Chief Information Officer (or CTO)
3. Lending Executive (VP Lending, Head of Originations, etc.)

---

## Topics and angles (rotation seed list)

- Explainability and B-20 audit readiness
- Decision speed and cost-to-close reduction
- Consistency and bias reduction in underwriting
- AI and OSFI regulatory alignment
- US market expansion and headless LOS opportunity
- Portfolio intelligence and early-warning signals

Track angles used in memory/fundmore-memory.md to avoid repeats.
