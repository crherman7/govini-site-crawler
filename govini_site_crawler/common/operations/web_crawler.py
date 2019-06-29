"""Abstract class for web crawlers.
"""

import abc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from govini_site_crawler.dod.models.constants import ENVIRONMENT
from govini_site_crawler.app_logging import logger

ABC = abc.ABCMeta('ABC', (object,), {})


class WebCrawler(ABC):

    @staticmethod
    def retrieve_browser():
        """Initiates a ChromeDriver session in development mode (i.e. launches chrome) or headless mode.

        Returns:
            webdriver.Chrome: ChromeDriver object.

        """
        if ENVIRONMENT == "development":
            logger.info("Selenium Chrome WebDriver in development mode")
            return webdriver.Chrome()
        else:
            logger.info("Selenium Chrome WebDriver in production mode (i.e. --headless)")
            options = Options()
            options.add_argument('--headless')
            return webdriver.Chrome(chrome_options=options)

    @abc.abstractmethod
    def retrieve_website(self):
        """Abstract method for retrieving a website.
        """
        pass

    @abc.abstractmethod
    def retrieve_element(self, identifier):
        """Abstract method for retrieving an element on a website page.

        Args:
            identifier: Specific html identifier for retrieving an element.

        """
        pass

    @staticmethod
    @abc.abstractmethod
    def element_interaction(**kwargs):
        """Abstract method for interacting with the website.

        Args:
            **kwargs: Webdriver elements to interact with.

        """
        pass

    @abc.abstractmethod
    def close_browser(self):
        """Abstract method for closing the browser.
        """
        pass
