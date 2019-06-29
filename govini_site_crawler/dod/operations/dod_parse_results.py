"""DoD specific class for parsing results.
"""

from govini_site_crawler.common.operations.parse_results import ParseResults
from govini_site_crawler.dod.models.dod_result import DoDResult
from govini_site_crawler.dod.models.constants import RESULTS_CLASS_NAME
from govini_site_crawler.app_logging import logger

from selenium.common.exceptions import NoSuchElementException

import time


class DoDParseResults(ParseResults):

    def __init__(self, browser):
        """Parses results from the DoD website after it has been interacted with.

        Args:
            browser: ChromeDriver selenium webdriver
        """
        self.browser = browser

        self.dod_results = list()

    def get_elements(self):
        """Retrieves all the result elements from the website and navigates to the next page if it exists
        to parse additional results.
        """
        logger.info("Attempting to retrieve list of elements by class name: {}".format(RESULTS_CLASS_NAME))
        elements = self.browser.find_elements_by_class_name(name=RESULTS_CLASS_NAME)

        self.assign_results(elements=elements)

        next_page = True
        page_value = 2
        while next_page:
            try:
                button = self.browser.find_element_by_link_text(str(page_value))
                button.click()
                time.sleep(5)
                next_elements = self.browser.find_elements_by_class_name(name=RESULTS_CLASS_NAME)
                self.assign_results(elements=next_elements)
                page_value += 1
            except NoSuchElementException:
                next_page = False

    def assign_results(self, elements):
        """Assigns results to a DoDResult model.

        Args:
            elements: List of ChromeDriver html elements

        """
        logger.info("Translating results into model")
        for element in elements:
            program_title, \
            agency, \
            fiscal_year, \
            budget_title, \
            program_number, \
            appropriation_number, \
            file_name \
                = element.text.split("\n")[:7]
            dod_result = DoDResult(program_title=program_title.split(':')[1],
                                   agency=agency.split(':')[1],
                                   fiscal_year=fiscal_year.split(':')[1],
                                   budget_title=budget_title.split(':')[1],
                                   program_number=program_number.split(':')[1],
                                   appropriation_number=appropriation_number.split(':')[1],
                                   file_name=file_name.split(':')[1])
            self.dod_results.append(dod_result)

    def print_results(self):
        """Prints DoD result items to the terminal.
        """
        print("==========")
        print("RESULTS")
        print("==========")
        for dod_result in self.dod_results:
            print(dod_result.__dict__)
