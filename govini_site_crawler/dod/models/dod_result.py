class DoDResult(object):

    def __init__(self, **kwargs):
        self.program_title = kwargs.get('program_title', None)
        self.agency = kwargs.get('agency', None)
        self.fiscal_year = kwargs.get('fiscal_year', None)
        self.budget_title = kwargs.get('budget_title', None)
        self.program_number = kwargs.get('program_number', None)
        self.appropriation_number = kwargs.get('appropriation_number', None)
        self.file_name = kwargs.get('file_name', None)
