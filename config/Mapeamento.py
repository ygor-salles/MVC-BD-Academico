from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Aluno(Base):
    __tablename__ = 'alunos'
    nromatric = Column(Integer, primary_key=True)
    nome = Column(String(50))
    #curso_id = Column(ForeignKey('public.cursos.nome'))
    #curso = relationship('Curso')

    def __repr__(self):
        return f'Aluno(nromatric={self.nromatric}, nome={self.nome})'

class Curso(Base):
    __tablename__ = 'cursos'
    nome = Column(String(30), primary_key=True)
    
    def __repr__(self):
        return f'Curso(nome={self.nome})'