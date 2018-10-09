import unittest
from unittest.mock import patch
import crawler


class TestCrawler(unittest.TestCase):

    def test_build_source(self):
        url = "https://www.yahoo.com/news/"
        article_urls = crawler.build_source(url)

        # Data type check.
        self.assertEqual(type(article_urls), list)

        # Successfully get articles.
        self.assertNotEqual(len(article_urls), 0)

    def test_build_source_invalid(self):
        url = ""
        result_false = crawler.build_source(url)
        self.assertEqual(result_false, False)

    def test_build_source_none_articles_to_get(self):
        url = "http://"
        article_urls = crawler.build_source(url)
        self.assertEqual(len(article_urls), 0)

    def test_extract_content(self):
        url = "https://www.yahoo.com/news/"
        content = crawler.extract_content(url)
        self.assertEqual(type(content), dict)


if __name__ == '__main__':
    unittest.main()
