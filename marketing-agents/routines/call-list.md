# Routine: The Call List

Schedule: weekly, Monday 08:00 ET

---

Run the BrokerBot playbook "The Call List".

1. Using web search, find this week's most relevant Canadian housing or credit figure
   from an approved Tier 2 source (Equifax, CMHC, Bank of Canada, CREA, Statistics Canada,
   OSFI, CMP, CMT). Record the exact number, the named source, and the release date. If
   nothing fresh this week, use the most recent release and label the period.
2. Reframe it into a concrete broker action for the week (the call-list angle).
3. Build the 1:1 card as an HTML file: white background; Gothic A1 and Mulish and JetBrains
   Mono via Google Fonts; pink (#FC0A7E) and purple (#86308B) stats; dark (#0B1818) punch
   strip; the logo from companies/brokerbot/assets embedded as base64; a visible source
   credit line. Match the structure of the most recent approved card in review/ if one
   exists.
4. Write the caption: lead with the number, name the source, one practitioner action, a
   soft "Book a Demo" CTA, loss-aversion framing.
5. Run the core QA gate, then the BrokerBot Pre-Flight.
6. Write review/call-list-<date>.md (contract header + caption) and
   review/call-list-<date>.html (card). Status NEEDS REVIEW. Log the run.

Do not publish.
