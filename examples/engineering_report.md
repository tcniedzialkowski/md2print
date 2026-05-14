# Engineering Report Sample

## Decision

Adopt a small CLI package layout before publishing the first release.

## Rationale

The package should be easy to install, test, and explain. A `src/` layout keeps import behavior honest during development.

## Risks

| Risk | Mitigation |
| --- | --- |
| Scope creep | Keep v0.1 HTML-only |
| Print regressions | Add focused CSS tests and manual print checks |
