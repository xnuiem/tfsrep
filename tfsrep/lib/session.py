from tfs import TFSAPI
from cassandra.cluster import Cluster

class Session:

    def __init__(self, config, logger):
        logger.info('Created TFS Session')
        self.client = TFSAPI(config.api_host, project=config.api_collection + '/' + config.api_project, user='',
                             password=config.api_key)



class DataSession:

    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        cluster = Cluster(self.config.cassandra_cluster)
        self.session = cluster.connect(self.config.cassandra_keyspace)