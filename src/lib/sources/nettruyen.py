import requests
from bs4 import BeautifulSoup
from .base import ComicSource
from typing import Any, Dict

class NettruyenSource(ComicSource):
    def fetch_page(self, url: str) -> str:
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.text

    def parse_comic_info(self, html: str) -> Dict[str, Any]:
        soup = BeautifulSoup(html, 'html.parser')
        # Example: parse title and author
        title = soup.select_one('.title-detail').text.strip() if soup.select_one('.title-detail') else ''
        author = soup.select_one('.author').text.strip() if soup.select_one('.author') else ''
        return {'title': title, 'author': author}

    def parse_chapters(self, html: str) -> list:
        soup = BeautifulSoup(html, 'html.parser')
        chapters = [a['href'] for a in soup.select('.list-chapter a')]
        return chapters

    def parse_chapter_content(self, html: str) -> Dict[str, Any]:
        soup = BeautifulSoup(html, 'html.parser')
        images = [img['src'] for img in soup.select('.page-chapter img')]
        return {'images': images}
