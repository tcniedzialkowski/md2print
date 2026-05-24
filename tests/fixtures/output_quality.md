# Output Quality Fixture

This source document represents dense technical content for md2print output-quality tests. It includes **strong text**, *emphasis*, and inline code such as `--preset compact`.

## Technical Content

- Convert one source document into one self-contained HTML file.
- Keep code, tables, paths, logs, and configuration values readable.
- Preserve technical strings without treating them as template placeholders.

```bash
md2print docs/source.md --preset compact --output print.html
export MD2PRINT_OUTPUT_PRESET=compact-3ring
```

### Operational Notes

| Kind | Example value | Expected handling |
| --- | --- | --- |
| Path | `/Users/example/projects/md2print/tests/fixtures/output_quality.md` | stays readable |
| URL | `https://example.invalid/docs/md2print/output-quality-reference` | remains literal source content |
| Config | `MD2PRINT_OUTPUT_PRESET=compact-3ring` | remains readable in a dense table |
| Log | `2026-05-23T12:34:56Z INFO render completed source=fixture.md` | keeps log text intact |
| Identifier | `sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` | does not disappear during conversion |

> This blockquote checks quoted technical notes without introducing a separate admonition feature.
