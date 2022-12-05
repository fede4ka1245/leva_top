from peewee import *
from database import database

class Data(Model):
    id = PrimaryKeyField()
    path = TextField()
    class Meta:
        database = database
        table_name = "Data"