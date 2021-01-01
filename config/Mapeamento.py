from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship, sessionmaker

Base = declarative_base()

class Aluno(Base):
    __tablename__ = 'alunos'
    nromatric = Column(Integer, primary_key=True)
    nome = Column(String(50))
    #curso_id = Column(ForeignKey('public.cursos.nome'))
    #curso = relationship('Curso')

    def __repr__(self):
        return f'Aluno(nromatric={self.nromatric}, nome={self.nome})'

class Grade(Base):
    __tablename__ = 'grades'
    anocurso = Column(String(10), primary_key=True)
    # curso = Column(ForeignKey('public.cursos.nome'), unique=True)
    # curso = relationship('Curso')
    
    def __repr__(self):
        return f'Curso(anocurso={self.anocurso})'

class Curso(Base):
    __tablename__ = 'cursos'
    nome = Column(String(30), primary_key=True)
    # grade = relationship(Grade, backref='cursos')
    # alunos = relationship(Aluno, backref='cursos')
    
    def __repr__(self):
        return f'Curso(nome={self.nome})'

