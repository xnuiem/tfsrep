from tfsrep.lib.tfs_link import TFSLink
from tfsrep.lib.info import TFSInfo, CreateJSON


class ReportResults:

    def __init__(self, config, logger):
        logger.debug('Report - Fetching Raw')
        raw_epics = TFSLink(config, logger).get_items('Epic')
        raw_stories = TFSLink(config, logger).get_items('User Story')
        raw_features = TFSLink(config, logger).get_items('Feature')

        logger.debug('Report - Create Info')
        self.stories = TFSInfo(config, logger, raw_stories).create_info()
        self.features = TFSInfo(config, logger, raw_features).create_info()
        self.epics = TFSInfo(config, logger, raw_epics).create_info()

        if config.write_info_to_file == 1:
            logger.info('Writing to Files')
            with open("tests/mock-epics.txt", 'w') as file:
                file.write(CreateJSON(self.epics).to_json())
                file.close()

            with open("tests/mock-stories.txt", 'w') as file:
                file.write(CreateJSON(self.stories).to_json())
                file.close()

            with open("tests/mock-features.txt", 'w') as file:
                file.write(CreateJSON(self.features).to_json())
                file.close()
