from typing import Type, Dict
from .sources.base import ComicSource
from .sources.nettruyen import NettruyenSource

class SourceFactory:
    _sources: Dict[str, Type[ComicSource]] = {
        'nettruyen': NettruyenSource,
        # Add more sources here
    }

    @classmethod
    def get_source(cls, key: str) -> ComicSource:
        if key not in cls._sources:
            raise ValueError(f"Unknown source: {key}")
        return cls._sources[key]()
