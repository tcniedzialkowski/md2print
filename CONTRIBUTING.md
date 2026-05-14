# Contributing

md2print is in early v0.1 development. The project is intentionally narrow: dense, readable Markdown printing for technical work.

## Development

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -U pip
.venv/bin/python -m pip install -e '.[dev]'
.venv/bin/ruff check .
.venv/bin/pytest
```

## Scope

Good early contributions improve the CLI, packaging, tests, documentation, or print CSS for the existing HTML output.

Please keep contributions focused on the current Python CLI unless a broader phase has been deliberately opened.
