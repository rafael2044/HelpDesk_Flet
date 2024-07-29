from models.chamado import Chamado

def adicionar_chamado(id_usuario:int, titulo:str,id_setor:int, id_categoria:int, id_prioridade:int,
                      detalhes:str, id_situacao=1, id_suporte=1):
    
    if len(titulo)>10:
        if len(detalhes) > 10:
            novo_chamado = Chamado(usuario_solicitante=id_usuario, titulo=titulo,
                                   setor=id_setor, categoria=id_categoria,
                                   prioridade=id_prioridade, detalhes=detalhes, 
                                   situacao=id_situacao, suporte_atendimento=id_suporte)
            novo_chamado.save()
            return {'mensagem':f'O chamado foi aberto! Num. {novo_chamado.id}', 'tipo':'sucesso'}
        else: return {'mensagem':'Os detalhes precisam ter 10 ou mais caracteres!', 'tipo':'info'}
    else: return {'mensagem':'O titulo precisa ter 10 ou mais caracteres!', 'tipo':'info'}
 
def selecionar_todos_chamados():
    chamados = [chamado for chamado in Chamado.select()]
    return chamados
   
def selecionar_chamado_solitado_por(id_usuario):
    chamados = [chamado for chamado in Chamado.select().filter(Chamado.usuario_solicitante == id_usuario)]
    return chamados
    
def selecionar_chamado_atendido_por(id_suporte):
    chamados = [chamado for chamado in Chamado.select().filter(Chamado.suporte_atendimento == id_suporte)]
    return chamados

def atender_chamado_id(id_chamado, descricao_atendimento, id_suporte, data_atendimento):
    chamado = Chamado.get_by_id(id_chamado)
    
    if len(descricao_atendimento) > 9:
        
        chamado.descricao_atendimento=descricao_atendimento
        chamado.suporte_atendimento = id_suporte
        chamado.data_fechamento = data_atendimento
        chamado.situacao = 2
        chamado.save()
        return {"mensagem":"Chamado atendido com sucesso!", 'tipo':'sucesso'}
    else:
        return {"mensagem":"A descricao do atendimento precisa ter 10 ou mais caracteres", 'tipo':'info'}