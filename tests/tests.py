import unittest, logging, json
import sys, os, re, inspect
from pprint import pprint
from ddt import ddt, data, file_data, unpack
from customassertions import CustomAssertions
import mockconfig

from tfsrep import TFSReports
from tfsrep.lib.info import TFSInfo

cmd_folder = os.path.abspath(os.path.join(os.path.split(inspect.getfile(
    inspect.currentframe()))[0], ".."))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


@ddt
class TFSReportsUnitTest(unittest.TestCase, CustomAssertions):

    def setUp(self):
        self.config = self.setup_config()
        self.logger = self.setup_logger()
        self.file_list = []

    def tearDown(self):
        for x in self.file_list:
            if os.path.isfile(x):
                os.remove(x)
        del self.config

    def get_reports(self):
        return TFSReports(self.config)

    @staticmethod
    def setup_config():
        config = mockconfig
        config.api_key = os.getenv('API_KEY', None)
        config.api_host = os.getenv('API_HOST', None)
        config.api_collection = os.getenv('API_COLLECTION', 'DefaultCollection')
        config.api_project = os.getenv('API_PROJECT', None)
        config.cassandra_nodes = os.getenv('CASSANDRA_NODES', None)
        config.cassandra_keyspace = os.getenv('CASSANDRA_KEYSPACE', 'tfsrep')
        config.template_file = os.getenv('TEMPLATE_FILE', 'index.html')
        config.write_info_to_file = int(os.getenv('WRITE_INFO_TO_FILE', 0))

        return config

    @staticmethod
    def setup_logger():
        logging.basicConfig(level='DEBUG')
        logger = logging.getLogger(__name__)
        logger.debug('Starting Logger in Unit Test')
        return logger

    @staticmethod
    def get_file_data(file_name):
        with open(file_name, 'r') as file:
            d = file.read()
            file.close()
        return json.loads(d)


    def test_data_close_logger(self):
        """Data Close Logger"""
        data = self.get_reports().close()
        self.assertAttrNotExists(data, "logger")

    def test_data_close_config(self):
        """Data Close Config"""
        data = self.get_reports().close()
        self.assertAttrNotExists(data, "config")

    @data('test-created.log')
    def test_logging_file_created(self, file_name):
        """Test Logging File"""
        self.config.logging_file = file_name
        self.file_list.append(file_name)
        self.get_reports().close()
        self.assertTrue(os.path.isfile(self.config.logging_file))

    @data('test-content.log')
    def test_logging_file_content(self, file_name):
        """Test Logging File Content"""
        self.config.logging_file = file_name
        self.file_list.append(file_name)
        self.get_reports().close()
        if os.path.isfile(self.config.logging_file):
            with open(self.config.logging_file, 'r') as myfile:
                match = re.match(
                    '20[0-9]{2}-[0-1]{1}[0-9]{1}-[1-3]{1}[0-9]{1} [0-1]{1}[0-2]{1}:[0-5]{1}[0-9]{1}:[0-5]{1}[0-9]{1} - tfsrep - INFO - Starting',
                    myfile.read())
                self.assertIsNotNone(match, "Test Logging File Content did not match")

    @data('mock-epics.txt')
    def test_epic_count(self, file_name):
        data = self.get_file_data(file_name)
        #infoObj = TFSInfo(self.config, self.logger, data)

