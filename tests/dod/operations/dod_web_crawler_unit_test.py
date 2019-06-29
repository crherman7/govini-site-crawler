import unittest
from mock.mock import Mock, patch

from govini_site_crawler.dod.operations.dod_web_crawler import DoDWebCrawler


class DoDWebCrawlerUnitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.crawler = DoDWebCrawler()

    @patch('govini_site_crawler.common.operations.web_crawler.webdriver.Chrome.get')
    def test_retrieve_website(self, mock_get):
        mock_get.return_value = Mock()

        self.crawler.retrieve_website()

        self.assertTrue(mock_get.called)

    @patch('govini_site_crawler.common.operations.web_crawler.webdriver.Chrome.find_element_by_id')
    def test_retrieve_element(self, mock_call):
        mock_call.return_value = Mock()

        self.crawler.retrieve_element("fake_id")

        self.assertTrue(mock_call.called)

    @patch('govini_site_crawler.common.operations.web_crawler.webdriver.remote.webelement.WebElement.click')
    @patch('govini_site_crawler.common.operations.web_crawler.webdriver.remote.webelement.WebElement.send_keys')
    def test_element_interaction(self, mock_call_a, mock_call_b):
        mock_call_a.return_value = Mock()
        mock_call_b.return_value = Mock()

        obj1 = Mock()
        obj2 = Mock()

        DoDWebCrawler.element_interaction(obj1, obj2)

        obj1.send_keys.assert_called()
        obj2.click.assert_called()

    @patch('govini_site_crawler.common.operations.web_crawler.webdriver.Chrome.close')
    def test_close_browser(self, mock_call):
        mock_call.return_value = Mock()

        self.crawler.close_browser()

        self.assertTrue(mock_call.called)