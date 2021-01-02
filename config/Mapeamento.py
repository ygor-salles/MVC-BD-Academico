from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship, sessionmaker

Base = declarative_base()

class Aluno(Base):
    __tablename__ = 'alunos'
    nromatric = Column(Integer, primary_key=True)
    nome = Column(String(50))
    curso_id = Column(ForeignKey('cursos.nome'))
    curso = relationship('Curso')

    def __repr__(self):
        return f'Aluno(nromatric={self.nromatric}, nome={self.nome}, curso_id={self.curso_id})'

class Grade(Base):
    __tablename__ = 'grades'
    anocurso = Column(String(10), primary_key=True)
    # curso = Column(ForeignKey('cursos.nome'), unique=True)
    # curso = relationship('Curso')
    # disciplina = relationship('Disciplina') 
    
    def __repr__(self):
        return f'Curso(anocurso={self.anocurso})'

class Curso(Base):
    __tablename__ = 'cursos'
    nome = Column(String(30), primary_key=True)
    alunos = relationship(Aluno, backref='cursos')
    # grade = relationship(Grade, backref='cursos')
    
    def __repr__(self):
        return f'Curso(nome={self.nome}, alunos={self.alunos})'

class Disciplina(Base):
    __tablename__ = 'disciplinas'
    codigo = Column(String(10), primary_key=True)
    nome = Column(String(50))
    cargahoraria = Column(Integer)
    # grade_id = Column(ForeignKey('grades.anocurso'))
    # historico_id = Column(ForeignKey('historicos.aluno'))
    # grade = relationship('Grade')
    # historico = relationship('Historico')

    def __repr__(self):
        return f'Disciplina(codigo={self.codigo}, nome={self.nome}, cargahoraria={self.cargahoraria})'
