# Flask Celery Crawler MVP

A minimal Flask server integrated with Celery for crawling comics and novels from multiple sites, storing metadata in PostgreSQL, and saving images/text in folders. Includes Swagger API docs, SQLAlchemy ORM, Alembic migrations, and .env config.

## Features
- Flask REST API with Swagger docs (Flasgger)
- Celery worker for async crawling
- BeautifulSoup for HTML parsing
- PostgreSQL for metadata (SQLAlchemy ORM)
- Alembic for DB migrations
- File storage for images/text
- Configurable via `.env`
- Basic authentication for endpoints

## Quickstart

### 1. Install dependencies
```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure environment
Edit `.env` with your DB and broker settings:
```
DB_USER=youruser
DB_PASS=yourpass
DB_HOST=localhost
DB_PORT=5432
DB_NAME=yourdb
DATABASE_URL=postgresql://user:pass@host:port/dbname
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
BASIC_AUTH_USER=admin
BASIC_AUTH_PASS=password
```

### 3. Run DB migrations
```sh
alembic upgrade head
```

### 4. Start services
- **Flask app:**
  ```sh
  python -m src.app
  # or
  export FLASK_APP=src.app
  flask run
  ```
- **Celery worker:**
  ```sh
  celery -A src.services.celery_worker.celery_app worker --loglevel=info
  ```

### 5. Access API docs
Open [http://localhost:5000/apidocs](http://localhost:5000/apidocs) in your browser.

## Project Structure
```
src/
  app.py                # Flask app entrypoint
  models/               # SQLAlchemy models
  services/             # Celery, Postgres, storage, config
  cli/                  # API blueprints, auth
  lib/                  # Parsers (BeautifulSoup)
alembic/                 # DB migrations
.env                     # Environment config
requirements.txt         # Python dependencies
```

## Endpoints
- `GET /` — Welcome message
- `POST /crawl` — Trigger crawl (JSON: `{ "site_url": "..." }`)
- `GET /crawl/<task_id>` — Check crawl status/result

## Development
- Lint: `flake8 src/`
- Format: `black src/`
- Migrations: `alembic revision --autogenerate -m "msg"`

## License
MIT
