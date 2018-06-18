from tfsrep.lib.session import DataSession

class dataSource:

    def __init__(self, config, logger):
        self.session = DataSession(config, logger)
        self.config = config
        self.logger = logger


    def select(self, query):
        rows = self.session.execute(query)




