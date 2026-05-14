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
<title>{title}</title>
<style>
/* Preset: {preset_label} */
/* {preset_subtitle} */
{preset_vars}
{shared_css}

.print-meta {{
    font-size: 8pt;
    color: #888;
    border-bottom: 0.5pt solid #ccc;
    padding-bottom: 3pt;
    margin-bottom: 8pt;
    display: flex;
    justify-content: space-between;
}}

.print-meta span {{ font-family: var(--code-font); }}

@media screen {{
    body {{
        max-width: 8.5in;
        margin: 0 auto;
        padding:
            var(--page-margin-top, var(--page-margin))
            var(--page-margin-outside, var(--page-margin))
            var(--page-margin-bottom, var(--page-margin))
            var(--page-margin-inside, var(--page-margin));
        background: #fff;
        box-shadow: 0 0 20px rgba(0,0,0,0.08);
    }}
}}
</style>
</head>
<body>
{meta_html}
{content}
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
        meta_html = f"""
<div class="print-meta">
    <span>{escape(preset.label)}</span>
    <span>Printed from md2print</span>
</div>"""

    return HTML_TEMPLATE.format(
        title=escape(title),
        preset_label=escape(preset.label),
        preset_subtitle=escape(preset.subtitle),
        preset_vars=preset.css_vars,
        shared_css=SHARED_CSS,
        meta_html=meta_html,
        content=content,
    )
