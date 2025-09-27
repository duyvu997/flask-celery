from src.models import db, Comic, Novel, CrawlTask

class PGService:
    @staticmethod
    def add_comic(**kwargs):
        comic = Comic(**kwargs)
        db.session.add(comic)
        db.session.commit()
        return comic

    @staticmethod
    def add_novel(**kwargs):
        novel = Novel(**kwargs)
        db.session.add(novel)
        db.session.commit()
        return novel

    @staticmethod
    def add_crawl_task(**kwargs):
        task = CrawlTask(**kwargs)
        db.session.add(task)
        db.session.commit()
        return task
