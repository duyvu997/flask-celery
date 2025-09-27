from src.models import db

class CrawlTask(db.Model):
    __tablename__ = 'crawl_tasks'
    id = db.Column(db.Integer, primary_key=True)
    target_type = db.Column(db.String(32), nullable=False)  # 'comic' or 'novel'
    target_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(32), nullable=False, default='pending')
    result = db.Column(db.JSON)
    started_at = db.Column(db.DateTime)
    finished_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
