from .source_factory import SourceFactory

class CrawlService:
    def __init__(self, source_key: str):
        self.source = SourceFactory.get_source(source_key)

    def crawl_comic(self, url: str):
        html = self.source.fetch_page(url)
        info = self.source.parse_comic_info(html)
        chapters = self.source.parse_chapters(html)
        return {'info': info, 'chapters': chapters}

    def crawl_chapter(self, url: str):
        html = self.source.fetch_page(url)
        content = self.source.parse_chapter_content(html)
        return content
