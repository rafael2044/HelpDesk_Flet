from peewee import Model, CharField, ForeignKeyField, DateTimeField, TextField
from models.setor import Setor
from models.prioridade import Prioridade
from models.status import Status
from models.usuario import Usuario
from models.categoria import Categoria
from connect import db
import datetime

class Chamado(Model):
    solicitante = ForeignKeyField(Usuario, backref='chamados')
    titulo = CharField()
    setor = ForeignKeyField(Setor, backref='chamados')
    categoria = ForeignKeyField(Categoria, backref='chamados')
    prioridade = ForeignKeyField(Prioridade, backref='chamados')
    status = ForeignKeyField(Status, backref='chamados')
    detalhes = TextField()
    data_abertura = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database=db