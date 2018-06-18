from tfs import TFSAPI
from tfsrep.lib.session import Session
from pprint import pprint


class TFSData:

    def __init__(self, config, logger):
        self.session = Session(config, logger).client
        self.logger = logger
        self.config = config

        self.logger.info('TFSData Started')

        self.get_epics()

    def get_epics(self):
        self.logger.info('Get Epics')
        query = """SELECT
            [System.Id]
        FROM workitems
        WHERE
            [System.WorkItemType] = 'Epic'
        ORDER BY [System.ChangedDate]"""

        return self.run_query(query)



    def run_query(self, query):
        result = self.session.run_wiql(query)

        ids = result.workitem_ids
        raw = result.result
        items = result.workitems
        count = len(result.workitems)
        return {"ids":ids,"raw":raw,"items":items,"count":count}
