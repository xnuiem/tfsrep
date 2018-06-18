import logging, os

from pprint import pprint

from tfsrep.lib.tfs_link import TFSData
from tfsrep.lib.error import InvalidUsage


class TFSReports:

    def __init__(self, config):
        self.config = config

        logging.basicConfig(level=self.config.logging_level)
        logger = logging.getLogger(__name__)

        if config.logging_file:
            handler = logging.FileHandler(self.config.logging_file)
            handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S")
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        self.logger = logger
        self.setup_config()
        self.logger.info('Starting')
        self.logger.debug('===========================')
        self.logger.debug('Configuration')
        self.logger.debug('LOGGING level:%s, file:%s', self.config.logging_level, self.config.logging_file)
        self.logger.debug('API host:%s, collection:%s, project:%s ', self.config.api_host, self.config.api_collection,
                          self.config.api_project)
        self.logger.debug('===========================')

    def setup_config(self):
        """
        Populates the config object with environment variables
        :return: None
        """
        self.config.api_key = os.getenv('API_KEY', None)
        self.config.api_host = os.getenv('API_HOST', None)
        self.config.api_collection = os.getenv('API_COLLECTION', 'DefaultCollection')
        self.config.api_project = os.getenv('API_PROJECT', None)
        self.config.cassandra_keyspace = os.getenv('CASSANDRA_KEYSPACE', 'tfsrep')

        nodes = os.getenv('CASSANDRA_NODES', None)
        if nodes is None:
            self.logger.exception('Cassandra Nodes')
            exit(1)
        else:
            self.config.cassandra_nodes = []
            for i in nodes.split(','):
                self.config.cassandra_nodes.append(i.strip())

        if self.config.api_key is None:
            self.logger.exception('Missing API Key')
            exit(1)

        if self.config.api_host is None:
            self.logger.exception('Missing API Host')
            exit(1)


    def close_handler(self):
        for handler in self.logger.handlers:
            handler.close()
            self.logger.removeHandler(handler)

    def get_data(self):
        tfs_data_obj = TFSData(self.config, self.logger)
        epics = tfs_data_obj.get_epics()
        pprint(epics)

    def close(self):
        self.close_handler()

