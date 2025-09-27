from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .comic import Comic
from .novel import Novel
from .crawl_task import CrawlTask
