from peewee import Model, CharField, ForeignKeyField, BooleanField, DateTimeField
from models.usuario import Usuario
from connect import db

class Sessao(Model):
    usuario = ForeignKeyField(Usuario, backref='sessoes')
    token = CharField(unique=True)
    ativo = BooleanField(default=True)
    expiracao = DateTimeField()
    
    class Meta:
        database=db
        
    