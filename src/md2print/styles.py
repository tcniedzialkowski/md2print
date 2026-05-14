"""Shared CSS for generated md2print HTML."""

SHARED_CSS = """
/* Reset and base */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

@page {
    size: letter;
    margin:
        var(--page-margin-top, var(--page-margin))
        var(--page-margin-outside, var(--page-margin))
        var(--page-margin-bottom, var(--page-margin))
        var(--page-margin-inside, var(--page-margin));
}

@page :left {
    margin-left: var(--page-margin-outside, var(--page-margin));
    margin-right: var(--page-margin-inside, var(--page-margin));
}

@page :right {
    margin-left: var(--page-margin-inside, var(--page-margin));
    margin-right: var(--page-margin-outside, var(--page-margin));
}

@media print {
    body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
    h1, h2, h3, h4 { break-after: avoid; }
    figure, pre { break-inside: avoid; }
    table { break-inside: auto; }
    thead { display: table-header-group; }
    tr { break-inside: avoid; }
}

body {
    font-family: var(--body-font);
    font-size: var(--body-size);
    line-height: var(--body-lh);
    color: var(--text-color);
    max-width: 100%;
    padding: 0;
}

h1 {
    font-size: var(--h1-size);
    font-weight: 700;
    line-height: 1.15;
    margin: 0 0 var(--heading-gap) 0;
    color: var(--heading-color);
    border-bottom: var(--h1-border);
    padding-bottom: var(--h1-pad-bottom);
}

h2 {
    font-size: var(--h2-size);
    font-weight: 600;
    line-height: 1.2;
    margin: var(--section-gap) 0 var(--heading-gap) 0;
    color: var(--heading-color);
    border-bottom: var(--h2-border);
    padding-bottom: var(--h2-pad-bottom);
}

h3 {
    font-size: var(--h3-size);
    font-weight: 600;
    line-height: 1.25;
    margin: var(--subsection-gap) 0 var(--heading-gap) 0;
    color: var(--heading-color);
}

h4 {
    font-size: var(--h4-size);
    font-weight: 600;
    line-height: 1.3;
    margin: var(--subsection-gap) 0 calc(var(--heading-gap) * 0.7) 0;
    color: var(--heading-color);
}

p { margin: 0 0 var(--para-gap) 0; }
strong { font-weight: 600; }
em { font-style: italic; }

a { color: var(--text-color); text-decoration: underline; }
@media print { a { text-decoration: none; } }

code {
    font-family: var(--code-font);
    font-size: var(--code-size);
    background: var(--code-bg);
    color: var(--code-color);
    border: var(--code-border);
    border-radius: var(--code-radius);
    padding: var(--code-pad);
    word-break: break-all;
}

h1 code, h2 code, h3 code, h4 code {
    font-family: inherit;
    background: #eeeeee;
    border: 1px solid #d0d0d0;
    border-radius: 3px;
    padding: 0 3px;
    font-size: inherit;
    font-weight: inherit;
}

pre {
    background: var(--pre-bg);
    border: var(--pre-border);
    border-radius: var(--pre-radius);
    padding: var(--pre-pad);
    margin: 0 0 var(--para-gap) 0;
    overflow-x: auto;
    line-height: var(--pre-lh);
}

pre code {
    background: none;
    border: none;
    padding: 0;
    font-size: var(--pre-code-size);
    color: var(--pre-color);
    border-radius: 0;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 0 0 var(--para-gap) 0;
    font-size: var(--table-size);
    line-height: var(--table-lh);
}

th, td {
    border: var(--table-border);
    padding: var(--table-cell-pad);
    text-align: left;
    vertical-align: top;
}

th {
    background: var(--table-header-bg);
    font-weight: 600;
    color: var(--heading-color);
}

tr:nth-child(even) td { background: var(--table-stripe); }

ul, ol {
    margin: 0 0 var(--para-gap) 0;
    padding-left: var(--list-indent);
}

li { margin-bottom: var(--list-item-gap); }

li > ul, li > ol {
    margin-top: var(--list-item-gap);
    margin-bottom: 0;
}

hr {
    border: none;
    border-top: 1px solid var(--hr-color);
    margin: var(--section-gap) 0;
}

blockquote {
    border-left: 3px solid var(--blockquote-border);
    padding-left: 0.6em;
    margin: 0 0 var(--para-gap) 0;
    color: var(--blockquote-color);
}

body > h1:first-child { margin-top: 0; }
"""
