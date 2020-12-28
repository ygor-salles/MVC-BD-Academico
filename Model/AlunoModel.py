from config.DAO import DAOCrud
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import StaleDataError
Base = declarative_base()

class Aluno(Base):
    __tablename__ = 'alunos'

    nromatric = Column(Integer, primary_key=True)
    nome = Column(String(50))
    #curso_id = Column(ForeignKey('public.cursos.nome'))
    #curso = relationship('Curso')

    def getNroMatric(self):
        return self.__nroMatric
    
    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

class manipulaBanco():
    def cadastraAluno(aluno):
        try:
            sessao = DAOCrud.getSession()
            DAOCrud.insere(sessao, aluno)
            sessao.commit()
            sessao.close()
            return 1
        except:
            return -1

    def deletaAluno(id):
        try:
            sessao = DAOCrud.getSession()
            aluno = DAOCrud.consultaAluno(sessao, id)
            DAOCrud.deleta(sessao, aluno)
            sessao.commit()
            sessao.close()
            return 1
        except:
            return -1

    def consultaAluno(id):
        try:
            sessao = DAOCrud.getSession()
            sessao.expire_on_commit = False
            aluno = DAOCrud.consultaAluno(sessao, id)
            sessao.commit()
            sessao.close()
            return aluno
        except :
            return -1
