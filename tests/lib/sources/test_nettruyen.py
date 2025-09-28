from src.lib.sources.nettruyen import NettruyenSource

def test_nettruyen_fetch(monkeypatch):
    class DummyResp:
        text = '<html><div class="title-detail">Title</div><div class="author">Author</div></html>'
        def raise_for_status(self): pass
    monkeypatch.setattr('requests.get', lambda url: DummyResp())
    src = NettruyenSource()
    html = src.fetch_page('dummy')
    info = src.parse_comic_info(html)
    assert info['title'] == 'Title'
    assert info['author'] == 'Author'
