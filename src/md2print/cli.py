"""Command line interface for md2print."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from md2print import __version__
from md2print.convert import convert_markdown_to_html
from md2print.presets import DEFAULT_PRESET, PRESETS


def build_parser() -> argparse.ArgumentParser:
    """Build the public v0.1 command line parser."""

    parser = argparse.ArgumentParser(
        prog="md2print",
        description="Convert Markdown to dense, readable, print-ready HTML.",
    )
    parser.add_argument("input", nargs="?", help="Input Markdown file")
    parser.add_argument("-o", "--output", help="Output HTML path")
    parser.add_argument(
        "-p",
        "--preset",
        choices=PRESETS.keys(),
        default=DEFAULT_PRESET,
        help="Preset to use (default: compact)",
    )
    parser.add_argument("--meta", action="store_true", help="Include a print metadata banner")
    parser.add_argument("--list-presets", action="store_true", help="List available presets")
    parser.add_argument("--version", action="version", version=f"md2print {__version__}")
    return parser


def output_path_for(input_path: Path, preset: str, *, explicit_output: str | None = None) -> Path:
    """Return the output path when generating one HTML file."""

    if explicit_output:
        return Path(explicit_output)
    if preset == DEFAULT_PRESET:
        return input_path.with_suffix(".html")
    return input_path.with_name(f"{input_path.stem}_{preset}.html")


def list_presets() -> None:
    """Print the available print presets."""

    for preset in PRESETS.values():
        print(f"{preset.name}: {preset.subtitle}")


def main(argv: list[str] | None = None) -> int:
    """Run the md2print CLI."""

    parser = build_parser()
    args = parser.parse_args(argv)

    if args.list_presets:
        list_presets()
        return 0

    if not args.input:
        parser.error("the following arguments are required: input")

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: {input_path} not found", file=sys.stderr)
        return 1

    try:
        markdown_text = input_path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"Error: could not read {input_path}: {exc}", file=sys.stderr)
        return 2

    html = convert_markdown_to_html(markdown_text, preset=args.preset, include_meta=args.meta)
    output_path = output_path_for(input_path, args.preset, explicit_output=args.output)

    try:
        output_path.write_text(html, encoding="utf-8")
    except OSError as exc:
        print(f"Error: could not write {output_path}: {exc}", file=sys.stderr)
        return 2

    print(f"Wrote {output_path} ({PRESETS[args.preset].label})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
