from __future__ import print_function

from webcrawler import WebCrawler
from loggers import *
import html_helper
import unittest

test_case_html = """
<!DOCTYPE html>
<html>
  <body>
    <h1>Test Case 1</h1>

    <p>I am a paragraph! <a href="javascript:doThing">blah</a></p>

    <p>Sometimes I am <a href="./cynical.html">overly cynical</a>, but sometimes I am
      <a href="./page2.html">overly na&#xEFve.</a></p>
  </body>
</html>
"""

class HtmlHelperTests(unittest.TestCase):
    def test_clean_up_href(self):
        self.assertEqual(
            html_helper.clean_up_href("http://www.example.com/space url"),
            "http://www.example.com/space%20url")

    def test_absolutize_path(self):
        base_path = '/base/path/'

        absolutize_path = html_helper.absolutize_path

        self.assertEqual(absolutize_path("/hello", base_path), "/hello")

        self.assertEqual(absolutize_path("hello/what", base_path), base_path + "hello/what")

        self.assertEqual(absolutize_path("./hello/what", base_path), base_path + "hello/what")

        self.assertEqual(absolutize_path("../hello/what", base_path), "/base/hello/what")

        self.assertEqual(absolutize_path("../../hello/what", base_path), "/hello/what")

        other_base_path = "/base/path"

        self.assertEqual(absolutize_path("/hello", other_base_path), "/hello")

        self.assertEqual(absolutize_path("hello/what", other_base_path), "/base/hello/what")

        self.assertEqual(absolutize_path("./hello/what", other_base_path), "/base/hello/what")

        self.assertEqual(absolutize_path("../hello/what", other_base_path), "/hello/what")

    def test_get_paths(self):
        result = html_helper.get_url_strings_from_doc(test_case_html)

        self.assertEqual(result, ["javascript:doThing", "./cynical.html", "./page2.html"])

class CrawlerTests(unittest.TestCase):
    def test_crawling_triplebyte(self):
        crawler = WebCrawler(100, SilentCrawlerLogger)
        crawler.crawl("https://www.triplebyte.com", None, True)

        self.assertIn("https://www.triplebyte.com", crawler.graph.nodes)

        self.assertIn(
            "https://triplebyte.com/careers",
            crawler
                .graph
                .nodes)

        self.assertEqual(
            crawler
                .graph
                .nodes["http://www.olark.com?welcome"]
                .request_type,
            "head")

if __name__ == '__main__':
    unittest.main()
