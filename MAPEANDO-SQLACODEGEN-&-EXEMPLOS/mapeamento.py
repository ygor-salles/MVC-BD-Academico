# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Curso(Base):
    __tablename__ = 'cursos'
    __table_args__ = {'schema': 'public'}

    nome = Column(String(30), primary_key=True)


class Aluno(Base):
    __tablename__ = 'alunos'
    __table_args__ = {'schema': 'public'}

    nromatric = Column(Integer, primary_key=True)
    nome = Column(String(50))
    curso = Column(ForeignKey('public.cursos.nome'))

    curso1 = relationship('Curso')


class Historico(Aluno):
    __tablename__ = 'historicos'
    __table_args__ = {'schema': 'public'}

    aluno = Column(ForeignKey('public.alunos.nromatric'), primary_key=True)
    semestre = Column(Integer)
    ano = Column(Integer)


class Grade(Base):
    __tablename__ = 'grades'
    __table_args__ = {'schema': 'public'}

    anocurso = Column(String(10), primary_key=True)
    curso = Column(ForeignKey('public.cursos.nome'), unique=True)

    curso1 = relationship('Curso', uselist=False)


class Disciplina(Base):
    __tablename__ = 'disciplinas'
    __table_args__ = {'schema': 'public'}

    codigo = Column(String(10), primary_key=True)
    nome = Column(String(50))
    cargahoraria = Column(Integer)
    grade = Column(ForeignKey('public.grades.anocurso'))
    historico = Column(ForeignKey('public.historicos.aluno'))

    grade1 = relationship('Grade')
    historico1 = relationship('Historico')


t_notadisc = Table(
    'notadisc', metadata,
    Column('disciplina', String(10)),
    Column('nota', Float(53)),
    Column('historico', ForeignKey('public.historicos.aluno')),
    schema='public'
)
