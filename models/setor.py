from peewee import Model, CharField
from connect import db

class Setor(Model):
    nome = CharField(max_length=50, unique=True)
    class Meta:
        database=db