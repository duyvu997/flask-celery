from src.lib.source_factory import SourceFactory

def test_factory_returns_nettruyen():
    src = SourceFactory.get_source('nettruyen')
    assert src.__class__.__name__ == 'NettruyenSource'
