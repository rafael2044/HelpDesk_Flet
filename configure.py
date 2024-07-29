from connect import db
from models.setor import Setor
from models.prioridade import Prioridade
from models.status import Status
from models.privilegio import Privilegio
from models.usuario import Usuario
from models.categoria import Categoria
from models.chamado import Chamado
from models.atendimento import Atendimento
from models.sessao import Sessao

PRIORIDADES = ('Baixa', 'Media', 'Alta')
STATUS = ('Pendente', 'Concluido')
PRIVILEGIOS = ('Padrao', 'Suporte', 'Administrador')
CATEGORIAS = ("Sistema", 'Equipamento', 'Software', 'Internet')
USUARIO_ADM = [('---', 'sar', 'sist', 3)]

def inserir_dados_padroes():
    try:
        if not Prioridade.select().execute():
            for p in PRIORIDADES:
                prioridade = Prioridade(nome = p)
                prioridade.save()
        
        if not Status.select().execute():
            for s in STATUS:
                status = Status(nome = s)
                status.save()
        
        if not Privilegio.select().execute():
            for pri in PRIVILEGIOS:
                privilegio = Privilegio(nome = pri)
                privilegio.save()
                
        if not Categoria.select().execute():
            for cat in CATEGORIAS:
                categoria = Categoria(nome = cat)
                categoria.save()
        if not Usuario.select().execute():
            for usuario in USUARIO_ADM:
                new_usuario = Usuario(nome_completo = usuario[0], usuario = usuario[1], senha = usuario[2],
                                  privilegio = usuario[3])
                new_usuario.save()
    except Exception as e:
        print(f"Erro ao inserir dados padrões:{e}")
    
def criar_database(db):
    
    def criar_trigger():
        with db.connection_context():
            db.execute_sql('''
                CREATE TRIGGER IF NOT EXISTS atualizar_status_chamado
                AFTER INSERT ON atendimento
                FOR EACH ROW
                BEGIN
                    UPDATE chamado
                    SET id_status = 2
                    WHERE id = NEW.chamado_id;
                END;
            ''')
    
    try:
        
        db.create_tables([Setor, Prioridade, Status, Privilegio, Usuario,
                          Categoria, Chamado, Atendimento, Sessao])
        inserir_dados_padroes()
        criar_trigger()
    except Exception as e:
        print(f"Erro ao inicializar tabelas: {e}")
criar_database(db)
    
