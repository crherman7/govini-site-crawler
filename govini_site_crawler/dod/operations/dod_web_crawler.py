from govini_site_crawler.common.operations.web_crawler import WebCrawler
from govini_site_crawler.dod.models.constants import URL, SEARCH_ELEMENT_ID, BUTTON_ELEMENT_ID, SEARCH_VALUE
from retry import retry


class DoDWebCrawler(WebCrawler):

    def __init__(self):
        self.browser = super(DoDWebCrawler, self).retrieve_browser()
        self.retrieve_website()

        search, button = self.retrieve_element(identifier=SEARCH_ELEMENT_ID), self.retrieve_element(
            identifier=BUTTON_ELEMENT_ID)
        self.element_interaction(search_element=search, button_element=button)

    def retrieve_website(self):
        self.browser.get(URL)

    @retry(Exception, tries=5, delay=3)
    def retrieve_element(self, identifier):
        element = self.browser.find_element_by_id(identifier)

        return element

    def element_interaction(self, search_element, button_element):
        search_element.send_keys(SEARCH_VALUE)
        button_element.click()

    def close_browser(self):
        self.browser.close()
