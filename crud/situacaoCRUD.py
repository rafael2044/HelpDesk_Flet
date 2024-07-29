from models.situacao import Situacao

def seleciona_nome_situacoes():
    situacoes = [situacao.nome_situacao for situacao in Situacao.select()]
    return situacoes

def selecionar_id_situacao_por_nome(nome_situacao):
    id_situacao = Situacao.get(Situacao.nome_situacao==nome_situacao).id
    
    return id_situacao