# Tasks: Pluggable Comic Source Crawler

**Input**: Design documents from `/specs/002-pluggable-comic-source/`
**Prerequisites**: plan.md (required)

## Execution Flow (main)

### Phase 3.1: Setup
- [X] T001 Create source structure for pluggable comic sources in `src/lib/sources/` and supporting files
- [X] T002 Initialize Python dependencies for design pattern support (abc, typing)
- [X] T003 [P] Configure linting and formatting tools (e.g., flake8, black)

### Phase 3.2: Tests First (TDD)
- [X] T004 [P] Unit test for base ComicSource class in `tests/lib/sources/test_base.py`
- [X] T005 [P] Unit test for NettruyenSource in `tests/lib/sources/test_nettruyen.py`
- [X] T006 [P] Integration test for source factory/registry in `tests/lib/sources/test_factory.py`

### Phase 3.3: Core Implementation
- [X] T007 [P] Abstract base class ComicSource in `src/lib/sources/base.py`
- [X] T008 [P] NettruyenSource implementation in `src/lib/sources/nettruyen.py`
- [X] T009 [P] Source factory/registry in `src/lib/source_factory.py`
- [X] T010 [P] Crawl service using pluggable sources in `src/lib/crawl_service.py`

### Phase 3.4: Integration
- [X] T011 Integrate crawl service with Flask API in `src/api/crawl_api.py`
- [X] T012 Integrate crawl service with Celery worker in `src/services/celery_worker.py`

### Phase 3.5: Polish
- [X] T013 [P] Add docstrings and usage examples to all new modules
- [X] T014 [P] Update README with pluggable source usage

## Parallel Execution Examples
- T003, T004, T005, T006 can run in parallel
- T007, T008, T009, T010 can run in parallel after setup and tests
- T013, T014 can run in parallel after integration

## Dependency Notes
- Setup (T001-T003) before everything
- Tests (T004-T006) before core implementation
- Core (T007-T010) before integration
- Integration before polish
