from peewee import Model, ForeignKeyField, TextField, DateTimeField
from connect import db
from models.chamado import Chamado
from models.usuario import Usuario
import datetime

class Atendimento(Model):
    chamado = ForeignKeyField(Chamado)
    suporte = ForeignKeyField(Usuario, backref='atendimentos')
    detalhes = TextField()
    data_abertura = DateTimeField(default=datetime.datetime.now)
    
    
    class Meta:
        database=db