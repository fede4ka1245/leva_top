from peewee import *
from database import database

class IndexedTable(Model):
    index = PrimaryKeyField()
    num = BigIntegerField()
    mp2 = TextField()
    emb = TextField()
    pin = DoubleField()
    e13 = BigIntegerField()

    class Meta:
        database = database
        table_name = '100000000'