from peewee import Model, CharField
from connect import db

class Privilegio(Model):
    nome = CharField(max_length=50)
    class Meta:
        database=db