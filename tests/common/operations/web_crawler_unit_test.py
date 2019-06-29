import unittest
from mock.mock import patch

from nose.tools import assert_true


from govini_site_crawler.common.operations.web_crawler import WebCrawler


class WebCrawlerUnitTest(unittest.TestCase):

    @staticmethod
    @patch('govini_site_crawler.common.operations.web_crawler.webdriver.Chrome')
    def test_retrieve_browser(mock_webdriver):
        mock_webdriver.return_value = True

        response_driver = WebCrawler.retrieve_browser()

        assert_true(response_driver)
