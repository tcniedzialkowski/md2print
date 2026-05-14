# Incident Postmortem Sample

## Summary

A scheduled maintenance task caused elevated error rates for an internal service.

## Timeline

| Time | Event |
| --- | --- |
| 09:00 | Maintenance began |
| 09:07 | Alerts fired |
| 09:12 | Rollback started |
| 09:20 | Error rate returned to baseline |

## Follow-Ups

- Add a preflight check.
- Update the runbook.
- Test rollback steps in staging.
