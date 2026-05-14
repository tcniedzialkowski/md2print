# Architecture

md2print is an opinionated Markdown-to-HTML CLI for printed technical documents.

## Code Layout

The package is split by responsibility:

- `cli.py` parses arguments, validates files, chooses output names, and writes HTML.
- `convert.py` converts Markdown to body HTML and extracts the document title.
- `presets.py` stores named product choices as CSS variable bundles.
- `styles.py` stores shared print CSS.
- `templates.py` renders the final single-file HTML document.

This keeps the public command small while making the implementation easy to test.

## HTML Only

The first release emits HTML, not PDF. That is deliberate. Browser print dialogs already handle printer selection, duplex mode, page ranges, scaling, and Save as PDF.

The generated file is self-contained and does not load external assets.

## No Chromium Dependency

md2print does not bundle or invoke Chromium. The tool should stay lightweight and install cleanly with `pipx`.
