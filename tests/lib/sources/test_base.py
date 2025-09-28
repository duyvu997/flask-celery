import pytest
from src.lib.sources.base import ComicSource

class DummySource(ComicSource):
    def fetch_page(self, url):
        return '<html></html>'
    def parse_comic_info(self, html):
        return {'title': 'Test', 'author': 'Tester'}
    def parse_chapters(self, html):
        return ['chapter1', 'chapter2']
    def parse_chapter_content(self, html):
        return {'images': ['img1.jpg', 'img2.jpg']}

def test_base_methods():
    src = DummySource()
    assert src.fetch_page('url') == '<html></html>'
    assert src.parse_comic_info('') == {'title': 'Test', 'author': 'Tester'}
    assert src.parse_chapters('') == ['chapter1', 'chapter2']
    assert src.parse_chapter_content('') == {'images': ['img1.jpg', 'img2.jpg']}
