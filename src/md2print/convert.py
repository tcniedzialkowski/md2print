"""Markdown conversion for md2print."""

from __future__ import annotations

import re

import markdown

from md2print.presets import DEFAULT_PRESET, get_preset
from md2print.templates import render_html_document

TAG_RE = re.compile(r"<[^>]+>")
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.DOTALL)


def extract_title(html_content: str) -> str:
    """Extract the document title from the first H1 in converted HTML."""

    h1_match = H1_RE.search(html_content)
    if not h1_match:
        return "Document"
    return TAG_RE.sub("", h1_match.group(1)).strip() or "Document"


def markdown_to_body_html(markdown_text: str) -> str:
    """Convert Markdown text to body HTML using the supported v0.1 extensions."""

    md = markdown.Markdown(
        extensions=[
            "tables",
            "fenced_code",
            "codehilite",
            "toc",
            "smarty",
            "attr_list",
        ],
        extension_configs={
            "codehilite": {"css_class": "highlight", "guess_lang": False},
        },
    )
    return md.convert(markdown_text)


def convert_markdown_to_html(
    markdown_text: str,
    *,
    preset: str = DEFAULT_PRESET,
    title: str | None = None,
    include_meta: bool = False,
) -> str:
    """Convert Markdown text into a complete print-optimized HTML document."""

    preset_config = get_preset(preset)
    body_html = markdown_to_body_html(markdown_text)
    document_title = title or extract_title(body_html)
    return render_html_document(
        title=document_title,
        content=body_html,
        preset=preset_config,
        include_meta=include_meta,
    )
