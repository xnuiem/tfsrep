from tfsrep.lib.session import Session


class TFSData:

    def __init__(self, config, logger):
        self.session = Session(config, logger).client
        self.logger = logger
        self.config = config
        self.logger.info('TFSData Started')

    def get_items(self, item_type):
        self.logger.info('Get ' + item_type)
        query = """SELECT
            [System.Id]
        FROM workitems
        WHERE
            [System.WorkItemType] = '""" + item_type + """'
        ORDER BY [System.ChangedDate]"""
        self.run_query(query)
        self.close()
        return self

    def close(self):
        self.logger.info('Closing')
        del self.config
        del self.logger
        del self.session

    def run_query(self, query):
        self.logger.info('Running Query')
        self.logger.debug(query)
        self.result = self.session.run_wiql(query)
