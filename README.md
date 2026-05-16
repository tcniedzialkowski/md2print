# md2print

md2print converts Markdown into dense, readable, print-ready HTML for technical documents.

It is intentionally small: run one command and get one self-contained HTML file. Open it in a browser, print it, annotate it, and keep moving.

## Install

```bash
pipx install md2print
```

For local development from this repository:

```bash
pipx install --force .
```

## Quickstart

```bash
md2print report.md
md2print report.md --output print.html
md2print report.md --meta
```

By default, `md2print input.md` writes `input.html`. Existing files are left untouched unless you pass `--force`.

For duplex 3-ring binder printing:

```bash
md2print report.md --preset compact-3ring
```

## CLI Reference

```bash
md2print [options] input.md
```

Options:

- `-o, --output PATH`: write to a specific HTML file instead of deriving one from the input filename.
- `-p, --preset NAME`: choose a print preset. Defaults to `compact`.
- `--meta`: include a small print metadata banner in the generated document.
- `--force`: overwrite the output file if it already exists.
- `--list-presets`: print available presets and exit.
- `--version`: print the installed version and exit.

## Presets

`compact` is the default compact layout: 9.5pt body text, tight spacing, visible table borders, light print-friendly code blocks, and 0.5-inch margins.

`compact-3ring` uses the same density with a 0.9-inch alternating inside margin for duplex pages that will be hole-punched for a 3-ring binder.

## Why HTML Instead Of PDF?

The browser print dialog is good at the final mile: duplex, page ranges, scaling, destination printers, and Save as PDF. md2print focuses on producing clean single-file HTML with print CSS and lets the browser handle device-specific printing.

There is no Chromium dependency, hosted service, or bundled PDF renderer.

## Privacy And Security

md2print runs locally. It does not make network calls, collect telemetry, upload documents, or load external CSS, JavaScript, fonts, or images.

Treat generated HTML files like the Markdown files they came from. If the source document is sensitive, the output is sensitive too.

## When Not To Use md2print

Use Pandoc or a typesetting system if you need citations, EPUB, Word export, complex academic layout, or precise PDF production.

Use a static site generator if you are publishing a website.

Use a slide tool if you are making presentations.

md2print is for dense technical documents you want to print, read, and mark up.

## Roadmap

- Polish the first release from real printed output.
- Add release automation after the manual release path is proven.
- Consider additional Markdown features and print presets only after the core CLI proves useful in daily use.
- Consider Rust or Typst only if distribution or low-level safety becomes a stronger reason to move beyond Python.
