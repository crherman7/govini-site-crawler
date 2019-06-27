import abc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from govini_site_crawler.dod.models.constants import ENVIRONMENT

ABC = abc.ABCMeta('ABC', (object,), {})


class WebCrawler(ABC):

    @staticmethod
    def retrieve_browser():
        if ENVIRONMENT == "development":
            return webdriver.Chrome()
        else:
            options = Options()
            options.add_argument('--headless')
            return webdriver.Chrome(chrome_options=options)

    @abc.abstractmethod
    def retrieve_website(self):
        pass

    @abc.abstractmethod
    def retrieve_element(self, identifier):
        pass

    @abc.abstractmethod
    def element_interaction(self, **kwargs):
        pass

    @abc.abstractmethod
    def close_browser(self):
        pass
