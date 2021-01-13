from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship, sessionmaker

Base = declarative_base()

class Aluno(Base):
    __tablename__ = 'alunos'
    nromatric = Column(Integer, primary_key=True)
    nome = Column(String(50))
    curso_id = Column(ForeignKey('cursos.nome'))

    def __repr__(self):
        return f'Aluno(nromatric={self.nromatric}, nome={self.nome}, curso_id={self.curso_id})'

class Grade(Base):
    __tablename__ = 'grades'
    anocurso = Column(String(10), primary_key=True)
    curso_id = Column(ForeignKey('cursos.nome', ondelete='CASCADE'), unique=True)
    curso = relationship('Curso', backref='grades')
    disciplinas = relationship('Disciplina', secondary='grade_disciplina') 
    
    def __repr__(self):
        return f'Grade(anocurso={self.anocurso}, curso_id={self.curso_id}, disciplinas={self.disciplinas})'

class Curso(Base):
    __tablename__ = 'cursos'
    nome = Column(String(30), primary_key=True)
    alunos = relationship('Aluno')
    grade = relationship('Grade', uselist=False, backref='cursos', cascade="all, delete", passive_deletes=True)
    
    def __repr__(self):
        return f'Curso(nome={self.nome}, alunos={self.alunos}, grade={self.grade})'

class Disciplina(Base):
    __tablename__ = 'disciplinas'
    codigo = Column(String(10), primary_key=True)
    nome = Column(String(50))
    cargahoraria = Column(Integer)

    def __repr__(self):
        return f'Disciplina(codigo={self.codigo}, nome={self.nome}, cargahoraria={self.cargahoraria})'

class GradeDisciplina(Base):
    __tablename__ = 'grade_disciplina'
    grade_id = Column(String(10), ForeignKey('grades.anocurso'), primary_key=True)
    disciplina_id = Column(String(10), ForeignKey('disciplinas.codigo'), primary_key=True)

    def __repr__(self):
        return f'GradeDisciplina(grade_id={self.grade_id}, disciplina_id={self.disciplina_id})'