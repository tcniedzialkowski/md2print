# Contributing

md2print is in early v0.1 development. The project is intentionally narrow: dense, readable Markdown printing for technical work.

## Development

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -U pip
.venv/bin/python -m pip install -e '.[dev]'
.venv/bin/pytest
.venv/bin/ruff check .
.venv/bin/mypy src/
.venv/bin/python -m build
.venv/bin/python -m twine check dist/*
```

Print layout changes also need manual visual checks. See `docs/TESTING.md` for known regression
cases, including large preformatted code blocks and long table values that can overrun cell
borders.

See `docs/TEST_STRATEGY.md` for the current automated test inventory, testing rationale, and
portfolio-oriented engineering notes.

## Scope

Good early contributions improve the CLI, packaging, tests, documentation, or print CSS for the existing HTML output.

Please keep contributions focused on the current Python CLI unless a broader phase has been deliberately opened.
