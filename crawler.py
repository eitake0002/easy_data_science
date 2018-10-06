"""
Crawling and scraping.
"""

import feedparser
import urllib.request
from bs4 import BeautifulSoup
import pprint
pp = pprint.PrettyPrinter(indent=4)


def get_main_text(url):
    f = urllib.request.urlopen(url)
    soup = BeautifulSoup(f.read(), "html.parser")
    #soup = BeautifulSoup("aaa bbb ccc", "html.parser")
    #text = soup.get_text()
    return soup.get_text()


def feed_rss(rss_url, description=False):
    """Crawl rss

    Parameters
    ----------
    rss_url : str
        target rss url

    Return
    ------
    RSS data : list
        title, link, description

    """
    d = feedparser.parse(rss_url)

    entry_list = []
    if description is True:
        for e in d["entries"]:
            entry_data = (e["title"], e["link"], e["description"])
            entry_list.append(entry_data)

    else:
        for e in d["entries"]:
            entry_data = (e["title"], e["link"])
            entry_list.append(entry_data)

    return entry_list


def feed_rss_list(rss_list_file):

    with open(rss_list_file) as f:
        rss_list = f.readlines()

    rss_all_list = []
    for i in rss_list:
        rss_data = feed_rss(i)
        rss_all_list.append(rss_data)

    return rss_all_list


if __name__ == '__main__':
    res = feed_rss_list("rss_list.csv")
    pp.pprint(res)
