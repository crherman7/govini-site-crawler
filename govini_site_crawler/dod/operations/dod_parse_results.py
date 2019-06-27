from govini_site_crawler.common.operations.parse_results import ParseResults
from govini_site_crawler.dod.models.dod_result import DoDResult
from govini_site_crawler.dod.models.constants import RESULTS_CLASS_NAME

from selenium import webdriver


class DoDParseResults(ParseResults):

    def __init__(self, browser):
        self.browser = browser

        self.dod_results = list()

    def get_elements(self):
        elements = self.browser.find_elements_by_class_name(name=RESULTS_CLASS_NAME)

        return elements

    def assign_results(self, elements):
        for element in elements:
            program_title, \
            agency, \
            fiscal_year, \
            budget_title, \
            program_number, \
            appropriation_number, \
            file_name \
                = element.text.split("\n")[:7]
            dod_result = DoDResult(program_title=program_title,
                                   agency=agency,
                                   fiscal_year=fiscal_year,
                                   budget_title=budget_title,
                                   program_number=program_number,
                                   appropriation_number=appropriation_number,
                                   file_name=file_name)
            self.dod_results.append(dod_result)

    def print_results(self):
        for dod_result in self.dod_results:
            print(dod_result.__dict__)
