import abc

ABC = abc.ABCMeta('ABC', (object,), {})


class ParseResults(ABC):

    @staticmethod
    def print_results(json_object):
        print(json_object)
