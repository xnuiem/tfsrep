from tfsrep.lib.tfs_link import TFSData
from tfsrep.lib.info import TFSInfo


class ReportResults:

    def __init__(self, config, logger):
        raw_epics = TFSData(config, logger).get_items('Epic')
        raw_stories = TFSData(config, logger).get_items('User Story')
        raw_features = TFSData(config, logger).get_items('Feature')

        self.stories = TFSInfo(config, logger, raw_stories).create_info()
        self.features = TFSInfo(config, logger, raw_features).create_info()
        self.epics = TFSInfo(config, logger, raw_epics).create_info()





