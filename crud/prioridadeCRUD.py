from models.prioridade import Prioridade

def seleciona_nome_prioridades():
    prioridades = [prioridade.nome_prioridade for prioridade in Prioridade.select()]
    return prioridades

def selecionar_id_prioridade_por_nome(nome_prioridade):
    id_prioridade = Prioridade.get(Prioridade.nome_prioridade==nome_prioridade).id
    
    return id_prioridade