from models.usuario import Usuario


def adicionar_usuario(nomeCompleto:str, usuario:str, senha:str, privilegio:int):
    usuario_existe = Usuario.filter(Usuario.nome_completo == nomeCompleto,
                                    Usuario.usuario == usuario)

    if not usuario_existe:
        novo_usuario = Usuario(nome_completo = nomeCompleto, usuario=usuario,
                                   senha = senha, privilegio = privilegio)
        novo_usuario.save()
        return novo_usuario
    return False
            
    
def selecionar_todos_usuarios():
    usuarios = [usuario for usuario in Usuario.select()]
    
    return usuarios

def quantidade_usuarios():
    return len(Usuario.select())

def selecionar_usuario_login(login):
    try:
        usuario = Usuario.get(Usuario.usuario == login)
        return usuario
    except Usuario.DoesNotExist as e:
        return None