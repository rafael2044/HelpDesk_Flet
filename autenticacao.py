from models.usuario import Usuario
from models.sessao import Sessao
from datetime import datetime, timedelta
from crud import usuarioCRUD
import uuid

def criar_sessao(usuario: Usuario, expiracao: datetime) -> str:
    token = str(uuid.uuid4())  # Gera um token único
    Sessao.create(usuario=usuario, token=token, expiracao=expiracao)
    return token

def autenticar_usuario(username: str, senha: str) -> str:
    try:
        usuario = usuarioCRUD.selecionar_usuario_login(username)
        if usuario:
            if senha == usuario.senha:
                expiracao = datetime.now() + timedelta(minutes=1)  # Token expira em 1 hora
                return criar_sessao(usuario, expiracao)
        else:
            return False
    except Usuario.DoesNotExist:
        return None
    
    
def verificar_sessao(token: str):
    try:
        sessao = Sessao.get(Sessao.token == token, Sessao.ativo == True)
        if sessao.expiracao > datetime.now():
            return sessao.usuario
        else:
            sessao.ativo = False
            sessao.save()
            return None
    except Sessao.DoesNotExist:
        return None
    
       
def desativar_sessao(token: str):
    try:
        sessao = Sessao.get(Sessao.token == token)
        sessao.ativo = False
        sessao.save()
    except Sessao.DoesNotExist:
        pass