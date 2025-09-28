from celery import Celery
import os
from dotenv import load_dotenv
from src.lib.crawl_service import CrawlService
from src.lib.source_factory import SourceFactory

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '../../.env'))

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')

celery_app = Celery(
    'crawler',
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)

celery_app.conf.update(
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    timezone='UTC',
    enable_utc=True,
)

# Example task
def register_tasks():
    @celery_app.task
    def crawl_site(site_url):
        # Placeholder for crawling logic
        return f"Crawled {site_url}"

register_tasks()
