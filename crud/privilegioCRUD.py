from models.privilegio import Privilegio

def seleciona_nome_privilegio():
    privilegios = [priv.nome for priv in Privilegio.select()]
    return privilegios

def selecionar_id_status_por_nome(nome_privilegio):
    id_privilegio = Privilegio.get(Privilegio.nome==nome_privilegio).id
    
    return id_privilegio