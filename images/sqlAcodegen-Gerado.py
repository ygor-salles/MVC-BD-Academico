# coding: utf-8
from sqlalchemy import Boolean, CheckConstraint, Column, Float, ForeignKey, ForeignKeyConstraint, Integer, SmallInteger, String, Table, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Curso(Base):
    __tablename__ = 'cursos'

    nome = Column(String(30), primary_key=True)


class Disciplina(Base):
    __tablename__ = 'disciplinas'

    codigo = Column(String(10), primary_key=True)
    nome = Column(String(50))
    carga_horaria = Column(SmallInteger)
    ativo = Column(Boolean, server_default=text("true"))

    grades = relationship('Grade', secondary='grade_disciplina')


class Aluno(Base):
    __tablename__ = 'alunos'

    nro_matric = Column(Integer, primary_key=True)
    nome = Column(String(50))
    curso_id = Column(ForeignKey('cursos.nome', ondelete='SET NULL', onupdate='CASCADE'))

    curso = relationship('Curso')


class Grade(Base):
    __tablename__ = 'grades'

    ano = Column(SmallInteger, primary_key=True, nullable=False)
    curso_id = Column(ForeignKey('cursos.nome', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, unique=True)

    curso = relationship('Curso', uselist=False)


t_grade_disciplina = Table(
    'grade_disciplina', metadata,
    Column('grade_id_ano', SmallInteger, primary_key=True, nullable=False),
    Column('grade_id_curso', String(30), primary_key=True, nullable=False),
    Column('disciplina_id', ForeignKey('disciplinas.codigo', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False),
    ForeignKeyConstraint(['grade_id_curso', 'grade_id_ano'], ['grades.curso_id', 'grades.ano'], ondelete='CASCADE', onupdate='CASCADE')
)


class Historico(Base):
    __tablename__ = 'historicos'
    __table_args__ = (
        CheckConstraint('(semestre = 1) OR (semestre = 2)'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('historicos_id_seq'::regclass)"))
    nro_matric = Column(ForeignKey('alunos.nro_matric', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    semestre = Column(SmallInteger)
    ano = Column(SmallInteger)

    aluno = relationship('Aluno')


class HistoricoDisciplina(Base):
    __tablename__ = 'historico_disciplina'
    __table_args__ = (
        CheckConstraint("((status)::text = 'APROVADO'::text) OR ((status)::text = 'REPROVADO'::text)"),
    )

    historico_id = Column(ForeignKey('historicos.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    disciplina_id = Column(ForeignKey('disciplinas.codigo'), primary_key=True, nullable=False)
    nota_disciplina = Column(Float(53))
    status = Column(String(10))
    obrigatorio = Column(Boolean)

    disciplina = relationship('Disciplina')
    historico = relationship('Historico')
