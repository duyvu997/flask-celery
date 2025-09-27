import requests
from bs4 import BeautifulSoup

def parse_nettruyen(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    # Example: extract comic titles
    titles = [a.text for a in soup.select('.item h3 a')]
    return titles
