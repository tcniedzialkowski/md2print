from pathlib import Path

from md2print.convert import convert_markdown_to_html
from md2print.styles import SHARED_CSS


def test_basic_markdown_conversion_returns_full_document() -> None:
    html = convert_markdown_to_html("# Hello\n\nThis is **strong**.")

    assert html.startswith("<!DOCTYPE html>")
    assert "<h1" in html
    assert "Hello" in html
    assert "<strong>strong</strong>" in html


def test_title_is_extracted_from_first_h1() -> None:
    html = convert_markdown_to_html("# Print Guide\n\nBody")

    assert "<title>Print Guide</title>" in html


def test_metadata_is_absent_by_default() -> None:
    html = convert_markdown_to_html("# Doc")

    assert "Printed from md2print" not in html
    assert 'class="print-meta"' not in html


def test_metadata_is_present_when_requested() -> None:
    html = convert_markdown_to_html("# Doc", include_meta=True)

    assert "Printed from md2print" in html
    assert 'class="print-meta"' in html


def test_table_css_allows_table_splitting_but_keeps_rows_intact() -> None:
    assert "table { break-inside: auto; }" in SHARED_CSS
    assert "thead { display: table-header-group; }" in SHARED_CSS
    assert "tr { break-inside: avoid; }" in SHARED_CSS


def test_preset_css_variables_are_included() -> None:
    html = convert_markdown_to_html("# Doc", preset="compact-3ring")

    assert "--page-margin-inside: 0.9in;" in html


def test_curly_braces_in_markdown_do_not_raise() -> None:
    # Regression: str.format() would KeyError on {word} patterns in content
    html = convert_markdown_to_html("# Doc\n\nUse `{HOST}` and `${PORT}` to configure.")

    assert "{HOST}" in html


def test_output_quality_fixture_preserves_technical_print_content() -> None:
    fixture = Path("tests/fixtures/output_quality.md").read_text(encoding="utf-8")

    html = convert_markdown_to_html(fixture)

    assert html.startswith("<!DOCTYPE html>")
    assert "<style>" in html
    assert "--body-size: 9.5pt;" in html
    assert "Printed from md2print" not in html
    assert '<link' not in html
    assert '<script' not in html
    assert 'src="http://' not in html
    assert 'src="https://' not in html
    assert 'href="http://' not in html
    assert 'href="https://' not in html
    assert "<h1" in html
    assert "Output Quality Fixture" in html
    assert "<h2" in html
    assert "Technical Content" in html
    assert "<h3" in html
    assert "Operational Notes" in html
    assert "<strong>strong text</strong>" in html
    assert "<em>emphasis</em>" in html
    assert "--preset compact" in html
    assert "md2print" in html
    assert "docs/source.md" in html
    assert "--output" in html
    assert "print.html" in html
    assert "<table>" in html
    assert "/Users/example/projects/md2print/tests/fixtures/output_quality.md" in html
    assert "MD2PRINT_OUTPUT_PRESET=compact-3ring" in html
    assert "2026-05-23T12:34:56Z INFO render completed source=fixture.md" in html
    assert "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" in html
    assert "<blockquote>" in html
