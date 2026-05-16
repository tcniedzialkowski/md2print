"""Preset definitions for md2print."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Preset:
    """A coordinated set of print CSS variables."""

    name: str
    label: str
    subtitle: str
    css_vars: str


def compact_css_vars(*, page_margin_inside: str = "0.5in") -> str:
    """Return compact preset CSS variables with structural page options."""

    return f"""
:root {{
    /* Page */
    --page-margin: 0.5in;
    --page-margin-top: 0.6in;
    --page-margin-bottom: 0.7in;
    --page-margin-inside: {page_margin_inside};
    --page-margin-outside: 0.5in;

    /* Typography */
    --body-font: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    --body-size: 9.5pt;
    --body-lh: 1.28;
    --text-color: #111;
    --heading-color: #111;

    /* Heading sizes */
    --h1-size: 15pt;
    --h2-size: 12pt;
    --h3-size: 10.5pt;
    --h4-size: 9.5pt;

    /* Heading decoration */
    --h1-border: 1.5px solid #222;
    --h1-pad-bottom: 3pt;
    --h2-border: 1px solid #aaa;
    --h2-pad-bottom: 2pt;

    /* Spacing */
    --section-gap: 10pt;
    --subsection-gap: 7pt;
    --heading-gap: 3pt;
    --para-gap: 4pt;

    /* Inline code */
    --code-font: "SF Mono", "Cascadia Code", "JetBrains Mono", Menlo, Consolas, monospace;
    --code-size: 0.86em;
    --code-bg: #e5e5e5;
    --code-color: #111;
    --code-border: 1px solid #c0c0c0;
    --code-radius: 2px;
    --code-pad: 0.5px 3px;

    /* Code blocks */
    --pre-bg: #e5e5e5;
    --pre-border: 1px solid #b0b0b0;
    --pre-radius: 3px;
    --pre-pad: 4pt 6pt;
    --pre-lh: 1.25;
    --pre-code-size: 8.5pt;
    --pre-color: #111;

    /* Tables */
    --table-size: 8.5pt;
    --table-lh: 1.25;
    --table-border: 1px solid #999;
    --table-cell-pad: 2pt 4pt;
    --table-header-bg: #e0e0e0;
    --table-stripe: #f3f3f3;

    /* Lists */
    --list-indent: 1.2em;
    --list-item-gap: 1pt;

    /* Misc */
    --hr-color: #bbb;
    --blockquote-border: #999;
    --blockquote-color: #333;
}}
"""


COMPACT_CSS_VARS = compact_css_vars()
COMPACT_3RING_CSS_VARS = compact_css_vars(page_margin_inside="0.9in")

PRESETS: dict[str, Preset] = {
    "compact": Preset(
        name="compact",
        label="Compact",
        subtitle="Dense technical print layout with footer-safe vertical margins",
        css_vars=COMPACT_CSS_VARS,
    ),
    "compact-3ring": Preset(
        name="compact-3ring",
        label="Compact 3-Ring",
        subtitle="Compact with 0.9in alternating binder margin for 3-ring punched pages",
        css_vars=COMPACT_3RING_CSS_VARS,
    ),
}

DEFAULT_PRESET = "compact"


def get_preset(name: str) -> Preset:
    """Return a preset by name."""

    if name not in PRESETS:
        valid_presets = ", ".join(PRESETS)
        raise KeyError(f"Unknown preset {name!r}. Valid presets: {valid_presets}")
    return PRESETS[name]
