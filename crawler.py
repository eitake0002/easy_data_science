"""
Crawling and scraping.
"""

from newspaper import Article
import newspaper
from multiprocessing import Pool, Process
import feedparser
import urllib.request
import nltk
from boilerpipe.extract import Extractor
import sys
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
    try:
        paper = newspaper.build(source_url)
    except Exception as e:
        print(e)
        return False

    if paper.size() == 0:
        pp.pprint("Warning: No articles found in the source.")
        pp.pprint(source_url)

    article_urls = []
    for article in paper.articles:
        article_urls.append(article.url)

    return article_urls


def extract_content_jp(url):
    """Extract content from Japanese article."""
    extractor = Extractor(extractor='ArticleExtractor', url=url)
    content = extractor.getText()
    return content


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
    try:
        article = Article(url)
        article.download()
        article.parse()

    except Exception as e:
        pp.pprint(e)
        pp.pprint("ERROR : something wrong with url")
        return False

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
    """Extract content from multiple articles in source

    Parameters
    ----------
    source_url : str
        Source url to extract article contents. 

    article_num : int
        Number of articles to extract. 

    logging : bool
        Logging

    Return
    ------
    contents : list
    """
    article_urls = build_source(source_url)

    contents = []
    for idx, url in enumerate(article_urls):
        if logging is True:
            pp.pprint(url)

        try:
            content = extract_content(url)
            contents.append(content)

        except Exception as e:
            print(e)

        if (idx + 1) == article_num:
            break

    return contents


def batch_extract_content_parallel(source_url, article_num=10, parallel_num=4):
    """Extract content from multiple articles in source parallely.

    Parameters
    ----------
    source_url : str
        Source url to extract article contents. 

    article_num : int
        Number of articles to extract. 

    Return
    ------
    contents : list
    """
    article_urls = build_source(source_url)
    article_urls_slice = article_urls[0:article_num]

    p = Pool(parallel_num)
    contents = p.map(extract_content, article_urls_slice)
    return contents


if __name__ == '__main__':

    args = sys.argv
    if args[1] == '-h' or args[1] == '--help':
        help_doc = """
            python crawler.py [crawling_type] [url]
            
            Ex)
            [Get all articles in the site]
            python crawler.py batch http://www.yahoo.com/news
            
            [Get all articles in the site with parallel processing]
            python crawler.py pbatch https://www.yahoo.com/news
            
            [Get content from single article]
            python crawler.py single http://www.yahoo.com/news/article
            """
        print(help_doc)
        sys.exit()

    elif len(args) == 2:
        print("Arg is not defined")
        sys.exit()

    if sys.argv[1] == 'batch':
        contents = batch_extract_content(sys.argv[2])
        pp.pprint(contents)

    elif sys.argv[1] == 'pbatch':
        contents = batch_extract_content_parallel(sys.argv[2])
        pp.pprint(contents)

    elif sys.argv[1] == 'single':
        contents = extract_content(sys.argv[2])
        pp.pprint(contents)
