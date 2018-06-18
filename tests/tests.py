import unittest
import sys
import inspect
import os
import xmlrunner
from ddt import ddt, data
from customassertions import CustomAssertions
import mockconfig

from tfsrep import TFSReports

cmd_folder = os.path.abspath(os.path.join(os.path.split(inspect.getfile(
    inspect.currentframe()))[0], ".."))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


@ddt
class TFSReportsUnitTest(unittest.TestCase, CustomAssertions):

    def setUp(self):
        self.config = self.setup_config()

    def tearDown(self):
        del self.config

    def get_data(self):
        return TFSReports(self.config)


    @staticmethod
    def setup_config():
        config = mockconfig
        config.api_key = os.getenv('API_KEY', None)
        config.api_host = os.getenv('API_HOST', None)
        config.api_collection = os.getenv('API_COLLECTION', 'DefaultCollection')
        config.api_project = os.getenv('API_PROJECT', None)
        config.cassandra_nodes = os.getenv('CASSANDRA_NODES', None )
        config.cassandra_keyspace = os.getenv('CASSANDRA_KEYSPACE', 'tfsrep')

        return config

    def test_data_close_logger(self):
        """Data Close Logger"""
        data = self.get_data().close()
        self.assertAttrNotExists(data, "logger")

