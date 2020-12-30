from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from config.Mapeamento import Aluno, Base

class DAOCrud():
    def getSession():
        engine = create_engine('postgresql+psycopg2://postgres:123456@localhost:5432/academico', echo=False)
        Session = sessionmaker(bind=engine)
        session = Session()
        Base.metadata.create_all(engine)
        return session

    def insere(sessao, obj):
        sessao.add(obj)

    def deleta(session, obj):
        session.delete(obj)

    def consultaAluno(sessao, id):
        aluno = sessao.query(Aluno).filter(Aluno.nromatric == id).first()
        return aluno
    
    def listaAluno(sessao):
        alunos = sessao.query(Aluno).all()
        return alunos
    