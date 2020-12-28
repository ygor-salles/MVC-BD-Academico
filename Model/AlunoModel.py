from config.DAO import DAOCrud
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
Base = declarative_base()

class Aluno(Base):
    __tablename__ = 'alunos'

    nromatric = Column(Integer, primary_key=True)
    nome = Column(String(50))
    curso_id = Column(ForeignKey('public.cursos.nome'))
    curso = relationship('Curso')

    def getNroMatric(self):
        return self.__nroMatric
    
    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome