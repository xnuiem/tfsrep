from tfsrep.lib.tfs_link import TFSData
from tfsrep.lib.info import TFSInfo
from tfsrep.lib.error import InvalidUsage
from pprint import pprint

class ReportResults:

    def __init__(self, config, logger):
        raw_epics = TFSData(config, logger).get_items('Epic')
        raw_stories = TFSData(config, logger).get_items('User Story')
        raw_features = TFSData(config, logger).get_items('Feature')

        stories = TFSInfo(config, logger, raw_stories).create_info()
        features = TFSInfo(config, logger, raw_features).create_info()
        epics = TFSInfo(config, logger, raw_epics).create_info()

        pprint(vars(stories))



