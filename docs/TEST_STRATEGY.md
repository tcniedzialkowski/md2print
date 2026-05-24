# Test Strategy

md2print is focused on compact, page-efficient printing of technical files, with strong
representation for inline code, fenced code blocks, tables, and other technical matter. The test
strategy should protect that product direction: the CLI should be predictable, generated HTML
should be self-contained and print-oriented, and layout choices should stay intentional as the tool
evolves.

## What The Automated Tests Cover

The automated suite currently has 25 pytest tests across four areas:

- CLI behavior in `tests/test_cli.py`
- Markdown conversion and shared CSS behavior in `tests/test_convert.py`
- Output-quality fixture coverage in `tests/test_convert.py` using `tests/fixtures/output_quality.md`
- Preset definitions and preset lookup behavior in `tests/test_presets.py`

These tests are intentionally small and direct. They mostly exercise public behavior rather than
private implementation details, which makes them useful as both regression protection and readable
documentation for future contributors.

## CLI Tests

### `test_cli_writes_default_output_file`

Why the test exists: verifies the default user workflow. A Markdown input should produce an HTML
file beside it without extra flags.

How it works: creates a temporary `input.md`, runs `main([input_path])`, and checks that
`input.html` exists with a zero exit code.

### `test_cli_refuses_to_overwrite_default_output`

Why the test exists: protects user files from accidental overwrite.

How it works: creates both `input.md` and an existing `input.html`, runs the default command, and
checks for exit code `1`, preserved file contents, and an error message.

### `test_cli_force_overwrites_default_output`

Why the test exists: verifies that overwrite protection has an explicit escape hatch.

How it works: creates an existing default output file, runs with `--force`, and confirms the old
content was replaced.

### `test_cli_writes_compact_3ring_output_file`

Why the test exists: documents the filename behavior for non-default presets.

How it works: runs with `--preset compact-3ring` and checks for `input_compact-3ring.html`.

### `test_cli_refuses_to_overwrite_explicit_output`

Why the test exists: applies overwrite protection to `--output`, not only derived filenames.

How it works: creates an explicit `print.html`, runs with `--output print.html`, and verifies the
file is preserved with an error.

### `test_cli_force_overwrites_explicit_output`

Why the test exists: verifies that `--force` also works with explicit output paths.

How it works: runs with `--output` and `--force`, then checks that previous output content is gone.

### `test_cli_rejects_missing_input`

Why the test exists: keeps the command interface honest. Input Markdown is required.

How it works: calls `main([])` and checks that argparse exits with code `2`.

### `test_cli_help_shows_input_as_required`

Why the test exists: prevents the help text from implying that the input file is optional.

How it works: renders parser help and checks that `input` appears as a required positional
argument, not `[input]`.

### `test_cli_list_presets_exits_zero`

Why the test exists: ensures users can discover available print layouts from the CLI.

How it works: runs `--list-presets`, checks exit code `0`, and confirms both launch presets are
listed.

### `test_cli_returns_error_for_nonexistent_input`

Why the test exists: verifies a clear failure path for missing files.

How it works: runs the CLI with a path that does not exist and checks for exit code `1`.

### `test_cli_rejects_all_as_invalid_preset`

Why the test exists: protects the public preset surface. `all` is not a real print preset.

How it works: runs with `--preset all` and checks that argparse exits with code `2`.

## Conversion And CSS Tests

### `test_basic_markdown_conversion_returns_full_document`

Why the test exists: verifies the core conversion promise from Markdown to complete HTML.

How it works: converts a small Markdown document and checks for a doctype, heading, body text, and
rendered strong text.

### `test_title_is_extracted_from_first_h1`

Why the test exists: gives generated documents useful browser titles without requiring a separate
title flag.

How it works: converts a document with an H1 and checks that the HTML `<title>` matches it.

### `test_metadata_is_absent_by_default`

Why the test exists: keeps default output clean and focused on the document itself.

How it works: converts without `include_meta` and checks that the print metadata banner is absent.

### `test_metadata_is_present_when_requested`

Why the test exists: verifies the optional provenance banner for users who want print metadata.

How it works: converts with `include_meta=True` and checks for the banner text and class.

### `test_table_css_allows_table_splitting_but_keeps_rows_intact`

Why the test exists: protects a key print behavior for technical tables. Long tables should be able
to continue across pages while rows remain intact.

How it works: checks shared CSS for table pagination rules: tables may split, table headers repeat,
and rows avoid internal page breaks.

### `test_preset_css_variables_are_included`

Why the test exists: verifies that selected preset variables actually reach the generated HTML.

How it works: converts with `compact-3ring` and checks for the wider inside-margin CSS variable.

### `test_curly_braces_in_markdown_do_not_raise`

Why the test exists: protects a regression where template formatting treated Markdown braces as
format placeholders.

How it works: converts Markdown containing `{HOST}` and `${PORT}` and checks that literal braces
survive.

## Output-Quality Fixture Test

### `test_output_quality_fixture_preserves_technical_print_content`

Why the test exists: protects md2print's dense technical print-output promise without relying on a
broad HTML snapshot or browser-rendered visual diff.

How it works: converts `tests/fixtures/output_quality.md`, a stable source document containing
headings, prose, emphasis, inline code, fenced code, a list, a blockquote, a table, and long
technical values such as paths, URLs, config values, log lines, and identifier-like strings. The
assertions check that the generated HTML is complete, self-contained, uses the default compact
preset, omits the meta banner by default, and preserves representative technical content.

This test does not prove browser pagination or final-mile print quality. Browser-rendered CI is
intentionally deferred until a specific repeatable visual regression justifies the added dependency
and maintenance cost. Manual visual risks remain tracked in `docs/TESTING.md`.

## Preset Tests

### `test_launch_presets_exist`

Why the test exists: locks in the public launch presets.

How it works: checks that `compact` and `compact-3ring` exist in `PRESETS`.

### `test_all_is_not_a_public_preset`

Why the test exists: prevents internal or convenience concepts from becoming accidental user-facing
presets.

How it works: checks that `all` is absent from `PRESETS`.

### `test_compact_3ring_uses_wider_inside_margin`

Why the test exists: protects the binder-printing purpose of `compact-3ring`.

How it works: checks that the preset includes a `0.9in` inside margin.

### `test_compact_3ring_does_not_mutate_compact_margin`

Why the test exists: protects preset independence. A specialized preset should not change the
default preset.

How it works: checks that `compact` keeps its own `0.5in` inside margin.

### `test_compact_uses_footer_safe_vertical_margins`

Why the test exists: supports page-efficient printing while leaving enough room for browser
headers and footers when users need page numbers.

How it works: checks that the default preset uses the expected top and bottom page margins.

### `test_get_preset_error_lists_valid_names`

Why the test exists: makes invalid preset errors useful for users and contributors.

How it works: calls `get_preset("badname")`, checks for a `KeyError`, and confirms the message
names valid presets.

## Manual Visual Tests

Some print problems cannot be fully protected by unit tests because pagination is decided by the
browser after md2print emits HTML. Manual regression cases are tracked in `docs/TESTING.md`.

Current priority visual risks:

- Large preformatted code blocks can be pushed to a later page and leave excessive blank space.
- Long unbroken table values can overrun cell borders or page boundaries.

These cases matter because md2print's product value is not merely "Markdown becomes HTML." Its
value is compact, readable, technical print output.

## Engineering Best Practices

Recommended practices for this project:

- Keep tests close to public behavior: CLI return codes, output files, generated HTML, and public
  preset names.
- Add a regression test whenever a bug is fixed, especially for escaping, output safety, or CSS
  rules that protect print readability.
- Treat visual print cases as first-class manual tests until a browser rendering workflow is added.
- Prefer small focused assertions over broad snapshots, because generated HTML can change in
  harmless ways.
- Keep test names descriptive. The current names read like a behavior checklist, which is useful
  for maintenance and portfolio review.
- When adding CSS for code blocks, inline code, tables, or pagination, include both a focused unit
  assertion and a manual print case when the behavior depends on browser rendering.

## Portfolio And Resume Positioning

This project can be presented as a compact technical publishing tool with an engineering-quality
test strategy. Strong resume points include:

- Built a Python CLI that converts Markdown into self-contained, print-ready HTML.
- Designed print presets for dense technical documents, including 3-ring binder-bound output.
- Added automated tests for CLI safety, conversion behavior, preset contracts, and regression
  cases.
- Documented manual visual regression cases for browser-owned print behavior.
- Balanced lightweight tooling with practical constraints: no bundled Chromium, no network calls,
  and browser print used for the final mile.

As a portfolio piece, md2print should continue emphasizing the same product thesis: compact,
page-efficient printing for technical material, especially documents with code, code blocks,
tables, paths, logs, and configuration values.
