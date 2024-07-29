from models.categoria import Categoria

def seleciona_nome_categorias():
    categorias = [ categoria.nome_categoria for categoria in Categoria.select()]
    return categorias

def selecionar_id_categoria_por_nome(nome_categoria):
    id_categoria = Categoria.get(Categoria.nome_categoria==nome_categoria).id
    
    return id_categoria