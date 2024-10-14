""" BANCO DE DADOS 
    - SQL (LINGUAGEM DE CONSULTA ESTRUTURADA)
    - EXEMPLO: 
        - SELECT * FROM CLIENTE;
        - IRÁ CONSULTAR O BANDO DE DADOS NA TABELA CLIENTES.

        - SGBD: (Sisitema Gerenciador de Banco de dados.)
            - GERENCIAR PERMISSÕES DE ACESSO
            - ADMINISTRADOR DE BANCO DE DADOS (DBA)
            - CRIAR CONSULTAS PERSONALIZADAS
            - SELECT * FROM CLIENTE;
        - ORM: MAPEAMENTO OBJETO RELACIONAL
            - USAR A LINGUAGEM DE PROGRAMAÇÃO PARA 
              MANIPULAR O BANCO DE DADOS.
        - INSTALANDO ORM PARA PYTHON: 
            - pip install sqlalchemy
"""


import os 
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados. 
MEU_BANCO2 = create_engine("sqlite:///meubanco_alunos.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=MEU_BANCO2)
session = Session()

# Criando tabela.

Base = declarative_base()

class Alunos(Base): 
    __tablename__ = "alunos"

    # Definindo campos da tabela.
    ra = Column("ra", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    sobrenome = Column("sobrenome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classe.
    def __init__(self, nome: str, sobrenome: str, email: str, senha: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha



# Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO2)

# CRUD.
# Create - Insert - Salvar.
def solicitando_alunos():
    os.system("cls || clear")
    print("Solicitando dados para o usúario. ")
    inserir_nome = input("Digite seu nome: ")
    inserir_sobrenome = input("Digite seu sobrenome: ")
    inserir_email = input("Digite seu e-mail: ")
    inserir_senha = input("Digite sua senha: ")

    aluno = Alunos(nome=inserir_nome, sobrenome=inserir_sobrenome, email=inserir_email, senha=inserir_senha)
    session.add(aluno)
    session.commit()

# Read - Select - Consulta
def exibindo_alunos():
    print("\nExibindo dados de todos os alunos. ")
    lista_alunos = session.query(Alunos).all()

    for aluno in lista_alunos:
        print(f"{aluno.ra} - {aluno.sobrenome} - {aluno.nome} - {aluno.email} - {aluno.senha}")


# U - Update - UPDATE - Atualizar
def atualizando_alunos():
    print("\nAtualizando dados do aluno.")
    email_aluno = input("Digite o e-mail do aluno que será atualizado: ") 

    aluno = session.query(Alunos).filter_by(email = email_aluno).first()

    if aluno:
        aluno.nome = input("Digite seu nome: ")
        aluno.sobrenome = input("Digite seu sobrenome: ")
        aluno.email = input("Digite seu e-mail: ")
        aluno.senha = input("Digite sua senha: ")

        session.commit()
    else: 
        print("Aluno não encontrado.")

# R - Read - SELECT -Consulta
def exibindo_alunos():
    print("\nExibindo dados de todos os alunos. ")
    lista_alunos = session.query(Alunos).all()

    for aluno in lista_alunos:
        print(f"{aluno.ra} - {aluno.sobrenome} - {aluno.nome} - {aluno.email} - {aluno.senha}")

# D - Delete - DELETE - Excluir 
def excluindo_alunos():
    print("\nExcluindo os dados de um aluno. ")
    email_aluno = input("Digite o e-mail do aluno que será excluído: ")

    aluno = session.query(Alunos).filter_by(email = email_aluno).first()

    if aluno:
        session.delete(aluno)
        session.commit()
        print(f"Aluno {aluno.nome} excluido com sucesso!")
    else:
        print("Aluno não encontrado.")

# R - Read - SELECT - Consulta
def exibindo_todos():
    print("\nExibindo dados de todos os alunos. ")
    lista_alunos = session.query(Alunos).all()

    for aluno in lista_alunos:
        print(f"{aluno.ra} - {aluno.sobrenome} - {aluno.nome} - {aluno.email} - {aluno.senha}")

# R - Read - SELECT - Consulta
def consultando_apenas_um():
    print("\nConsultando os dados de apenas um aluno. ")
    email_aluno = input("Digite o e-mail do aluno:  ")

    aluno = session.query(Alunos).filter_by(email = email_aluno).first()

    if aluno:
        print(f"{aluno.ra} - {aluno.sobrenome} - {aluno.nome} - {aluno.email} - {aluno.senha}")
    else:
        print("Aluno não encontrado.")


# Fechando conexão.
session.close()

