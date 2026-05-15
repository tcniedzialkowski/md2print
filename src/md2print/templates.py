"""HTML template rendering for md2print."""

from __future__ import annotations

from html import escape

from md2print.presets import Preset
from md2print.styles import SHARED_CSS


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title><!--TITLE--></title>
<style>
/* Preset: <!--PRESET_LABEL--> */
/* <!--PRESET_SUBTITLE--> */
<!--PRESET_VARS-->
<!--SHARED_CSS-->

.print-meta {
    font-size: 8pt;
    color: #888;
    border-bottom: 0.5pt solid #ccc;
    padding-bottom: 3pt;
    margin-bottom: 8pt;
    display: flex;
    justify-content: space-between;
}

.print-meta span { font-family: var(--code-font); }

@media screen {
    body {
        max-width: 8.5in;
        margin: 0 auto;
        padding:
            var(--page-margin-top, var(--page-margin))
            var(--page-margin-outside, var(--page-margin))
            var(--page-margin-bottom, var(--page-margin))
            var(--page-margin-inside, var(--page-margin));
        background: #fff;
        box-shadow: 0 0 20px rgba(0,0,0,0.08);
    }
}
</style>
</head>
<body>
<!--META_HTML-->
<!--CONTENT-->
</body>
</html>
"""


def render_html_document(
    *,
    title: str,
    content: str,
    preset: Preset,
    include_meta: bool = False,
) -> str:
    """Render converted Markdown content inside the md2print HTML shell."""

    meta_html = ""
    if include_meta:
        meta_html = (
            f'\n<div class="print-meta">'
            f"\n    <span>{escape(preset.label)}</span>"
            f"\n    <span>Printed from md2print</span>"
            f"\n</div>"
        )

    return (
        HTML_TEMPLATE
        .replace("<!--TITLE-->", escape(title))
        .replace("<!--PRESET_LABEL-->", escape(preset.label))
        .replace("<!--PRESET_SUBTITLE-->", escape(preset.subtitle))
        .replace("<!--PRESET_VARS-->", preset.css_vars)
        .replace("<!--SHARED_CSS-->", SHARED_CSS)
        .replace("<!--META_HTML-->", meta_html)
        .replace("<!--CONTENT-->", content)
    )
