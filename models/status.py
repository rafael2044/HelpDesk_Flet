from peewee import Model, CharField
from connect import db

class Status(Model):
    nome = CharField(max_length=20)
    class Meta:
        database=db