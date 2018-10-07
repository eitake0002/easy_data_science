"""
Crawling and scraping.
"""

from newspaper import Article
import feedparser
import urllib.request
from bs4 import BeautifulSoup
import pprint
pp = pprint.PrettyPrinter(indent=4)


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
    """Feed from csv file

    Parameters
    ----------
    rss_list_file : str
        CSV file to load. 

    Return
    ------
    list
        RSS data from all site in CSV file.
    """

    with open(rss_list_file) as f:
        rss_list = f.readlines()

    rss_all_list = []
    for i in rss_list:
        rss_data = feed_rss(i)
        rss_all_list.append(rss_data)

    return rss_all_list


def extract_content(url):
    """Extract content

    Parameters
    ----------
    url : str
        Aritlce URL to extract content. 

    Return
    ------
    author : str
    publish_date : datetime
    text : str
    top_image: str(url)
    movies : list
    """
    article = Article(url)
    article.download()
    article.parse()

    author = article.authors
    publish_date = article.publish_date
    text = article.text
    top_image = article.top_image
    movies = article.movies

    return author, publish_date, text, top_image, movies
