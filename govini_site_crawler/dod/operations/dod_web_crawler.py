"""DoD specific web crawler.
"""

from govini_site_crawler.common.operations.web_crawler import WebCrawler
from govini_site_crawler.dod.models.constants import URL, SEARCH_VALUE, SEARCH_ELEMENT_ID, BUTTON_ELEMENT_ID
from govini_site_crawler.app_logging import logger
from retry import retry


class DoDWebCrawler(WebCrawler):

    def __init__(self):
        """Crawls the DoD Investment Budget website to find results from a specific program element number.
        """
        self.browser = super(DoDWebCrawler, self).retrieve_browser()

    def retrieve_website(self):
        """Retrieves the webdriver object for a specific website.
        """
        logger.info("Retrieving website: {}".format(URL))
        self.browser.get(URL)

    @retry(Exception, tries=20, delay=3)
    def retrieve_element(self, identifier):
        """Finds an element on an html source utilizing an element id.

        Args:
            identifier: html element id

        Returns:
            WebElement: Found html element

        """
        logger.info("Attempting to retrieve element by id: {}".format(identifier))
        element = self.browser.find_element_by_id(identifier)

        return element

    @staticmethod
    def element_interaction(search_element, button_element):
        """Interacts with website elements.

        Args:
            search_element: WebElement that key words are entered into
            button_element: WebElement that is clicked

        """
        logger.info("Interacting with search element id: {} and button element id: {}"
                    .format(SEARCH_ELEMENT_ID, BUTTON_ELEMENT_ID))
        search_element.send_keys(SEARCH_VALUE)
        button_element.click()

    def close_browser(self):
        """Closes the ChromeDriver session.
        """
        logger.info("Closing Chrome WebDriver session")
        self.browser.close()
