"""
Crawling and scraping.
"""

import urllib.request
from bs4 import BeautifulSoup

def get_main_text(url):
    f = urllib.request.urlopen(url)
    soup = BeautifulSoup(f.read(), "html.parser")
    #soup = BeautifulSoup("aaa bbb ccc", "html.parser")
    #text = soup.get_text()
    return soup.get_text()


if __name__ == '__main__':
    url = "http://stackoverflow.com/questions/2023893/python-3-get-http-page"
    url = "http://qiita.com/FGtatsuro/items/f45c349e06d6df95839b"
    print(get_main_text(url))
    
