import abc

ABC = abc.ABCMeta('ABC', (object,), {})


class ParseResults(ABC):

    @abc.abstractmethod
    def print_results(self):
        pass
