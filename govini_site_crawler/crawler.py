"""Main web crawler runner.
"""

from govini_site_crawler.dod.operations.dod_web_crawler import DoDWebCrawler
from govini_site_crawler.dod.models.constants import SEARCH_ELEMENT_ID, BUTTON_ELEMENT_ID
from govini_site_crawler.dod.operations.dod_parse_results import DoDParseResults


def main():
    """Combines the steps from the created library to run the script.
    """
    crawler = DoDWebCrawler()
    crawler.retrieve_website()
    search_element, button_element = crawler.retrieve_element(SEARCH_ELEMENT_ID), \
                                     crawler.retrieve_element(BUTTON_ELEMENT_ID)
    crawler.element_interaction(search_element=search_element, button_element=button_element)
    crawler.browser.implicitly_wait(5)
    dod_parse_results = DoDParseResults(crawler.browser)
    dod_parse_results.get_element_list()
    dod_parse_results.iterate_next_page()
    dod_parse_results.print_results()


if __name__ == "__main__":
    main()
