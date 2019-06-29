"""Abstract class for parsing results.
"""

import abc

ABC = abc.ABCMeta('ABC', (object,), {})


class ParseResults(ABC):

    @abc.abstractmethod
    def get_elements(self):
        """Abstract method for retrieving elements for a webdriver page.
        """
        pass

    @abc.abstractmethod
    def print_results(self):
        """Abstract method for printing results to std.out.
        """
        pass
