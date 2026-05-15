# Security Policy

## Supported Versions

md2print is pre-1.0 software. Security fixes are expected to land on the current default branch and the next published release, without long-term support for older versions.

## Privacy Posture

md2print runs locally on files you provide. It does not make network calls, collect telemetry, upload documents, or load external CSS, JavaScript, fonts, or images into generated HTML.

Generated HTML should be handled with the same care as the source Markdown. If the input contains sensitive information, the output does too.

## Reporting A Vulnerability

Please report suspected vulnerabilities through the repository's issue tracker:

https://github.com/tcniedzialkowski/md2print/issues

Include the affected version or commit, a clear description of the behavior, and a minimal reproduction when possible. Please avoid sharing sensitive source documents in public reports.
