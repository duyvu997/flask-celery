"""
Pluggable Comic Source Crawler
=============================

This module demonstrates how to add new comic sources using the pluggable design pattern.

Example usage:

from src.lib.crawl_service import CrawlService

service = CrawlService('nettruyen')
result = service.crawl_comic('https://nettruyen3qb.com/truyen/some-comic')
print(result['info'])
print(result['chapters'])

To add a new source:
- Create a new class in src/lib/sources/ that inherits from ComicSource
- Register it in SourceFactory._sources
- Use its key in CrawlService
"""
