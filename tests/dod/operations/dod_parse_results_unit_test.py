import unittest
from mock.mock import Mock, patch, call

from govini_site_crawler.dod.operations.dod_parse_results import DoDParseResults
from govini_site_crawler.common.operations.web_crawler import WebCrawler

from selenium.webdriver.remote.webelement import WebElement

from selenium.common.exceptions import NoSuchElementException


class DoDParseResultsUnitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = WebCrawler.retrieve_browser()

        cls.parse_results = DoDParseResults(browser=browser)

    @patch('govini_site_crawler.dod.operations.dod_parse_results.DoDParseResults.assign_results')
    @patch('govini_site_crawler.common.operations.web_crawler.webdriver.Chrome.find_elements_by_class_name')
    def test_get_element_list(self, mock_find_elements_by_class_name, mock_assign_results):
        mock_find_elements_by_class_name.return_value = Mock()
        mock_assign_results.return_value = Mock()

        self.parse_results.get_element_list()

        self.assertTrue(mock_find_elements_by_class_name.called)
        self.assertTrue(mock_assign_results.called)

    @patch('govini_site_crawler.common.operations.web_crawler.webdriver.remote.webelement.WebElement.click')
    @patch('govini_site_crawler.common.operations.web_crawler.webdriver.Chrome.find_element_by_link_text')
    def test_iterate_next_page(self, mock_find_element_by_link_text, mock_click):
        mock_find_element_by_link_text.side_effect = NoSuchElementException
        mock_click.return_value = Mock()

        self.parse_results.iterate_next_page()

        self.assertTrue(mock_find_element_by_link_text.called)
        self.assertFalse(mock_click.called)

    def test_assign_results(self):
        obj2 = Mock(spec=WebElement)
        obj2.text = "Program Element Title: Manufacturing Technology Program\nAgency: Air Force\nFiscal " \
                    "Year: 2020\nBudget Activity Title: Advanced Technology Development (ATD)\nProgram " \
                    "Element Number: 0603680F\nAppropriation Number: 3600\nFile Name: " \
                    "U_0603680F_3_PB_2020\nView PDF version | View XML version"

        self.parse_results.assign_results([obj2])

        self.assertTrue(self.parse_results.dod_results.__len__() > 0)

    @patch('__builtin__.print')
    def test_print_results(self, mock_print):
        self.parse_results.print_results()

        mock_print.assert_has_calls([
            call("=========="),
            call("RESULTS"),
            call("=========="),
            call(self.parse_results.dod_results[0].__dict__)
        ])

    @classmethod
    def tearDownClass(cls):
        cls.parse_results = None
