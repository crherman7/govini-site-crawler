from govini_site_crawler.common.operations.web_crawler import WebCrawler
from govini_site_crawler.dod.models.constants import URL, SEARCH_VALUE, SEARCH_ELEMENT_ID, BUTTON_ELEMENT_ID
from govini_site_crawler.app_logging import logger
from retry import retry


class DoDWebCrawler(WebCrawler):

    def __init__(self):
        self.browser = super(DoDWebCrawler, self).retrieve_browser()

    def retrieve_website(self):
        logger.info("Retrieving website: {}".format(URL))
        self.browser.get(URL)

    @retry(Exception, tries=20, delay=3)
    def retrieve_element(self, identifier):
        logger.info("Attempting to retrieve element by id: {}".format(identifier))
        element = self.browser.find_element_by_id(identifier)

        return element

    def element_interaction(self, search_element, button_element):
        logger.info("Interacting with search element id: {} and button element id: {}"
                    .format(SEARCH_ELEMENT_ID, BUTTON_ELEMENT_ID))
        search_element.send_keys(SEARCH_VALUE)
        button_element.click()

    def close_browser(self):
        logger.info("Closing Chrome WebDriver session")
        self.browser.close()
