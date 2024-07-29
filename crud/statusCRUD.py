from models.status import Status

def seleciona_nome_status():
    status = [st.nome for st in Status.select()]
    return status

def selecionar_id_status_por_nome(nome_status):
    id_status = Status.get(Status.nome==nome_status).id
    
    return id_status