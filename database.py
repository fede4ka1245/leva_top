from configparser import ConfigParser
from peewee import *

config = ConfigParser()

config.read('settings.ini')
database_config = config['database']

database = PostgresqlDatabase(
    database_config['dbname'],
    user=database_config['user'],
    password=database_config['password'],
    host=database_config['host']
)

database.connect()