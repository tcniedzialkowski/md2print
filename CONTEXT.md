# md2print

md2print is a Python CLI that converts one Markdown source document into one self-contained, print-ready HTML file.
The browser print dialog handles duplex printing, page ranges, scaling, printer selection, and Save-as-PDF.
md2print produces only HTML.

## Language

**Preset**:
A named bundle of layout CSS variables and rendering options that controls the print output.
Selected on the CLI with `--preset <name>` and listed with `--list-presets`.
_Avoid_: theme, style, profile, mode

**Compact**:
The default preset. It favors dense technical reading: small body text, tight spacing, visible table borders, light print-friendly code blocks, and compact margins.
_Avoid_: small, dense, tight

**Compact-3ring**:
A preset variant of compact with a wider alternating inside margin for duplex pages destined for a 3-ring binder.
_Avoid_: binder mode, hole-punch preset

**Meta banner**:
The optional header block at the top of the generated HTML containing source metadata.
Off by default and enabled with `--meta`.
_Avoid_: header, frontmatter, banner

**Self-contained HTML**:
The output file format. CSS and syntax-highlighting styles live inside the single `.html` file.
No external CSS, JavaScript, fonts, images, or network resources.
_Avoid_: standalone HTML, single-file HTML, inlined HTML

**Final mile**:
The browser-side print workflow: duplex, page-range selection, scaling, destination printer, and Save-as-PDF.
md2print produces input to the final mile but does not own it.
_Avoid_: printing, output stage, finishing

**Source document**:
The input Markdown file the user passes on the command line.
Treat it as potentially sensitive; the generated HTML inherits the same sensitivity.
_Avoid_: input file, markdown file, doc

## Relationships

- A source document plus a preset produces one self-contained HTML file.
- A preset may include a meta banner when `--meta` is set.
- Compact-3ring is a structural variant of compact; do not derive it with fragile string replacement.
- The final mile consumes one self-contained HTML file and produces the physical printout or PDF artifact.

## Product Boundaries

- Do not add network calls, telemetry, remote assets, CDN links, or hosted services.
- Do not add a PDF rendering backend such as Chromium, Playwright, WeasyPrint, or wkhtmltopdf.
- Keep the project focused on the current Python CLI unless a broader phase is deliberately opened.
- Prefer standard-library tools and small dependencies.
- Preserve the dense, print-oriented output philosophy.

## Ambiguities

- Use **preset**, not theme or style, for named output configurations.
- Use **source document** for the input Markdown and **self-contained HTML** for the generated output.
- Disambiguate print-ready HTML from the browser's final-mile print workflow.
