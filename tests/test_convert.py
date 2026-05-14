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
