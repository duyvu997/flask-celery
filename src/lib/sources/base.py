from abc import ABC, abstractmethod
from typing import Any, Dict

class ComicSource(ABC):
    """
    Abstract base class for comic sources.
    """
    @abstractmethod
    def fetch_page(self, url: str) -> str:
        """Fetch raw HTML for a given page URL."""
        pass

    @abstractmethod
    def parse_comic_info(self, html: str) -> Dict[str, Any]:
        """Parse comic metadata from HTML."""
        pass

    @abstractmethod
    def parse_chapters(self, html: str) -> list:
        """Parse chapter list from HTML."""
        pass

    @abstractmethod
    def parse_chapter_content(self, html: str) -> Dict[str, Any]:
        """Parse content (images/text) from a chapter HTML."""
        pass
