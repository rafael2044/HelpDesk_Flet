from models.usuario import Usuario


def adicionar_usuario(nome_usuario:str, login_usuario:str, senha:str, id_privilegio:int):
    usuario_existe = Usuario.filter(Usuario.nome_usuario == nome_usuario,
                                    Usuario.login_usuario == login_usuario)

    if not usuario_existe:
        if len(senha) > 2:
            if len(nome_usuario) > 10:
                novo_usuario = Usuario(nome_usuario = nome_usuario, login_usuario=login_usuario,
                                   senha_usuario = senha, privilegio_usuario = id_privilegio)
                novo_usuario.save()
                return {'mensagem':'Usuario cadastrado com sucesso','tipo':'sucesso'}
            else: return {'mensagem':'O nome precisa ter 10 ou mais caracteres!','tipo':'info'}
                
        else: return {'mensagem':'A senha precisa ter 3 ou mais caracteres!','tipo':'info'}
            
    else:
        return {'mensagem':'O usuario ou o login ja existe!','tipo':'aviso'}
    
def selecionar_todos_usuarios():
    usuarios = [usuario for usuario in Usuario.select()]
    
    return usuarios

def quantidade_usuarios():
    return len(Usuario.select())

def selecionar_usuario_login(login):
    usuario_existe = Usuario.get(Usuario.login_usuario == login)
    if usuario_existe:
        return usuario_existe
    else:
        return False
