# FundMore Assets

Drop brand files here before running the worker:

- `fundmore-logo.png` -- logo for embedding in card HTML (will be base64-encoded)
- `brand-kit.html` -- optional: a reference HTML page showing colours, fonts, and card templates

The worker embeds the logo from this folder into any `.html` card it produces. Without the
logo file, cards will render without it and the Pre-Flight will flag the gap.

## Logo usage notes (from brand.md)

- Embed as base64 in card HTML -- do not link to an external URL
- Minimum width: 120px
- Use on FundMore Blue (`#0A2463`) or white backgrounds only
- Never stretch, skew, or recolour the logo
