# Testing Notes

md2print has normal unit tests for conversion and CLI behavior, but print layout quality also
needs manual visual regression checks. These cases document known use and abuse patterns that
should be re-tested whenever shared CSS, presets, Markdown extensions, or browser print guidance
changes.

## Manual Print Regression Cases

### Large Preformatted Code Blocks

Example: the "two repo plan" print output has a large fenced code block containing
preformatted text.

Risk:

- A wide or tall `pre` block can reserve more vertical space than the current page has left.
- Because md2print currently avoids breaking `pre` blocks across pages, the browser may push the
  whole block to the next page and leave a large blank area on the previous page.
- Dense technical documents can look sparse or broken even though no content is missing.

What to test:

- Render a document with a long fenced code block containing preformatted text, such as an ASCII
  diagram, repository tree, command output, log excerpt, config dump, or generated plan.
- Print or Save as PDF from Chrome, Safari, and Firefox when practical.
- Check whether the previous page has excessive whitespace before the block.
- Check whether the block is still readable and whether horizontal overflow is handled acceptably.
- Re-test both `compact` and `compact-3ring`, with browser headers and footers enabled and
  disabled when possible.

Current expectation:

- Content should remain readable and should not clip.
- Some whitespace before oversized `pre` blocks is accepted in v0.1 because pagination is owned by
  the browser, but repeated or severe blank space should stay visible in the backlog.

### Long Table Values Overrunning Cell Borders

Example: a table with a very long unbroken value, token, path, URL, identifier, or config string.

Risk:

- A long value in a table cell can continue past the cell or table border.
- The printed page can clip the value, overlap adjacent content, or make the table border no longer
  describe the visible content.
- This is especially likely in dense presets because table columns are narrow.

What to test:

- Render a Markdown table with at least one long unbroken value in a narrow column.
- Include representative values such as long paths, URLs, hashes, environment variable values, and
  generated identifiers.
- Print or Save as PDF from Chrome, Safari, and Firefox when practical.
- Check that the value wraps, breaks, or otherwise stays visually contained within the table.
- Check that table borders still align with visible cell content.

Current expectation:

- Table content should not visually escape the table or page.
- If wrapping makes rows tall, that is preferable to clipped or border-overrunning content.
