from peewee import Model, CharField, ForeignKeyField
from models.privilegio import Privilegio
from connect import db

class Usuario(Model):
    nome_completo = CharField(unique=True)
    usuario = CharField(unique=True)
    senha = CharField()
    privilegio = ForeignKeyField(Privilegio)
    class Meta:
        database=db