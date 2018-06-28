from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.connection import setup


setup(config.cassServers, config.tableName)

class Resp(Model):
    __keyspace__ = config.keyspace
    __table_name__ = config.tableName
    user = columns.Text(primary_key=True)
    user_pretty_name = columns.Text()
    stat_name = columns.Text(index=True)
    stat_value = columns.Text()

if config.syncModel is True:
    from cassandra.cqlengine.management import sync_table
    sync_table( Resp )
    exit()