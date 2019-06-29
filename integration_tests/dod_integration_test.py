import unittest

from govini_site_crawler.dod.operations.dod_web_crawler import DoDWebCrawler
from govini_site_crawler.dod.models.constants import SEARCH_ELEMENT_ID, BUTTON_ELEMENT_ID
from govini_site_crawler.dod.operations.dod_parse_results import DoDParseResults

EXPECTED_LENGTH = 12


class DoDIntegrationTest(unittest.TestCase):

    def setUp(self):
        self.crawler = DoDWebCrawler()
        self.crawler.retrieve_website()
        search_element, button_element = self.crawler.retrieve_element(SEARCH_ELEMENT_ID), \
                                         self.crawler.retrieve_element(BUTTON_ELEMENT_ID)
        self.crawler.element_interaction(search_element=search_element, button_element=button_element)
        self.crawler.browser.implicitly_wait(5)
        self.dod_parse_results = DoDParseResults(self.crawler.browser)
        self.dod_parse_results.get_elements()

    def test_data_parsing(self):
        results = self.dod_parse_results.dod_results
        none_results = False

        for dod_result in results:
            none_results = None in dod_result.__dict__.values()

        self.assertEqual(EXPECTED_LENGTH, results.__len__())
        self.assertFalse(none_results)

    def tearDown(self):
        self.crawler.close_browser()
