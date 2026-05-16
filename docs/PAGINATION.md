# Pagination Research

md2print v0.1 emits self-contained HTML and lets the browser handle printing. That keeps the tool lightweight, but it means pagination is decided after md2print has finished rendering.

## Current Direction

The default presets should be safe with browser headers and footers enabled, because browser page numbers are the practical v0.1 workaround for long printed drafts.

For clean output, users can disable browser-generated headers and footers in the print dialog. For page order on long drafts, users can enable them.

## Known Tradeoffs

- Browser headers and footers provide page numbers, title, date, and source path.
- They are visually inconsistent and outside md2print's control.
- They consume top and bottom page space, which can crowd dense layouts.
- md2print does not know final page numbers before the browser paginates the document.

## Research Backlog

- Test `@page` margin boxes and `counter(page)` / `counter(pages)` in Chrome, Safari, and Firefox.
- Determine whether md2print can provide reliable title and page-number footers in plain browser-printed HTML.
- If browser support is not reliable, evaluate Paged.js, WeasyPrint, Typst, or another paged-media path for a later phase.
- Explore `compact-tight` and `compact-3ring-tight` presets for users who disable browser headers and footers.
- Revisit long `pre` block pagination so oversized code/tree blocks do not leave mostly blank previous pages.
