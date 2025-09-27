<!--
Sync Impact Report
- Version change: [TEMPLATE] → 1.0.0
- Modified principles: All placeholders replaced with concrete principles (Code Quality, Quick Development, Performance)
- Added sections: None
- Removed sections: None
- Templates requiring updates: 
  - .specify/templates/plan-template.md ✅ updated
  - .specify/templates/spec-template.md ✅ updated
  - .specify/templates/tasks-template.md ✅ updated
  - .specify/templates/agent-file-template.md ✅ updated
- Follow-up TODOs:
  - TODO(RATIFICATION_DATE): original adoption date unknown
-->

# Flask Celery Project Constitution

## Core Principles

### I. Code Quality
All code MUST pass automated linting, code review, and maintainability checks before merge. Code must be readable, well-documented, and follow project style guides. No code with unresolved warnings or failing tests may be merged.

### II. Quick Development
Rapid prototyping and short feedback cycles are prioritized. Minimal process overhead is enforced: contributors may submit work-in-progress for early review, and blockers must be surfaced immediately. Time-to-merge is a tracked metric.

### III. Performance
All code MUST meet defined performance benchmarks. Avoid unnecessary resource usage. Performance regressions are treated as critical bugs and must be resolved before release.

## Additional Constraints

- All dependencies must be justified and reviewed for security and performance impact.
- Technology choices must support rapid iteration and maintainability.

## Development Workflow

- Code review is mandatory for all merges.
- Automated tests and performance checks must pass before deployment.
- Task breakdowns should reflect code quality, speed, and performance priorities.

## Governance

- This constitution supersedes all other practices.
- Amendments require documentation, approval, and a migration plan.
- All PRs/reviews must verify compliance with these principles.
- Versioning follows semantic rules: MAJOR for breaking changes, MINOR for new principles, PATCH for clarifications.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): original adoption date unknown | **Last Amended**: 2025-09-27