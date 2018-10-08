"""
Crawling and scraping.
"""

from newspaper import Article
import newspaper
import feedparser
import urllib.request
import nltk
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


def build_source(source_url):
    """Extract article urls from news source

    Parameters
    ----------
    source_url : str
        News source url.

    Return
    ------
    Source list : list
    """
    paper = newspaper.build(source_url)

    article_urls = []
    for article in paper.articles:
        article_urls.append(article.url)

    return article_urls


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
    summary : text
    text : str
    top_image: str(url)
    movies : list
    keywords : list
    """
    article = Article(url)
    article.download()
    article.parse()

    title = article.title
    text = article.text
    author = article.authors
    publish_date = article.publish_date
    top_image = article.top_image
    movies = article.movies
    
    nltk.download('punkt')
    article.nlp()
    keywords = article.keywords
    summary = article.summary

    return {
        "title": title,
        "summary": summary, 
        "text": text, 
        "link": url,
        "author": author, 
        "publish_date": publish_date, 
        "top_image": top_image, 
        "movies": movies, 
        "keywords": keywords,
    }

def batch_extract_content(source_url, article_num=10, logging=True):
    article_urls = build_source(source_url)
    
    contents = []
    for idx, url in enumerate(article_urls):
        if logging is True:
            pp.pprint(url)
            
        content = extract_content(url)
        contents.append(content)
        if (idx + 1) == article_num:
            break

    return contents