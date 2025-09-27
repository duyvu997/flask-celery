# Tasks: MVP Flask Server with Celery Crawler

**Input**: Design documents from `/specs/001-build-a-mvp/`
**Prerequisites**: plan.md (required)

## Execution Flow (main)

### Phase 3.1: Setup
- [X] T001 Create project structure in `src/` per plan.md
  - Created: src/, src/models/, src/services/, src/cli/, src/lib/, src/__init__.py
- [X] T002 Initialize Python project with Flask, Celery, BeautifulSoup, and PostgreSQL dependencies
  - Added requirements.txt and installed all dependencies in venv
- [X] T003 [P] Configure linting and formatting tools (e.g., flake8, black)
  - Added .flake8 config
- [X] T004 [P] Setup Swagger/OpenAPI documentation for Flask API (e.g., use flask-swagger or flasgger)
  - Created src/app.py with Swagger enabled

### Phase 3.3: Core Implementation
- [ ] T008 [P] Comic model in src/models/comic.py
- [ ] T009 [P] Novel model in src/models/novel.py
- [ ] T010 [P] CrawlTask model in src/models/crawl_task.py
- [ ] T011 [P] Celery worker setup in src/services/celery_worker.py
- [ ] T012 [P] Flask API: trigger crawl endpoint in src/cli/crawl_api.py
- [ ] T013 [P] Flask API: crawl status/result endpoint in src/cli/crawl_api.py
- [ ] T014 [P] BeautifulSoup site parser for https://nettruyen3qb.com/ in src/lib/nettruyen_parser.py
- [ ] T015 [P] Postgres integration for metadata in src/services/pg_service.py
- [ ] T016 [P] File storage for images/text in src/services/storage_service.py
- [ ] T017 [P] Configurable RAM usage/concurrency in src/services/worker_config.py
- [ ] T018 [P] Basic authentication in src/cli/auth.py

## Parallel Execution Examples
- T003 can run in parallel
- T008, T009, T010 can run in parallel
- T011, T014, T015, T016, T017, T018 can run in parallel after models

## Dependency Notes
- Setup (T001-T003) before everything
- Models (T008-T010) before services/endpoints
- Services before endpoints
- Core before integration
