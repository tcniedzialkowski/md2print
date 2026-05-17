# Security Policy

## Supported Versions

md2print is pre-1.0 software. Security fixes are expected to land on the current default branch and the next published release, without long-term support for older versions.

## Privacy Posture

md2print runs locally on files you provide. It does not make network calls, collect telemetry, upload documents, or load external CSS, JavaScript, fonts, or images into generated HTML.

Generated HTML should be handled with the same care as the source Markdown. If the input contains sensitive information, the output does too.

## Input Sanitization

md2print converts Markdown to HTML using Python-Markdown with a standard extension set. Raw HTML embedded in Markdown source, including `<script>` tags, passes through to the generated output. This is intentional: md2print treats the source document as trusted input, consistent with tools like Pandoc and most static site generators.

Generated HTML is opened locally via `file://` with no cookies, sessions, or credentials in scope, which limits the practical impact of embedded scripts. Users processing untrusted Markdown should review or sanitize input before conversion.

A `--safe` mode that strips raw HTML is tracked for a future release.

## Reporting A Vulnerability

Please report suspected vulnerabilities through the repository's issue tracker:

https://github.com/tcniedzialkowski/md2print/issues

Include the affected version or commit, a clear description of the behavior, and a minimal reproduction when possible. Please avoid sharing sensitive source documents in public reports.
