from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, SmallInteger, ForeignKeyConstraint
from sqlalchemy.orm import relationship

Base = declarative_base()

class Aluno(Base):
    __tablename__ = 'alunos'
    nro_matric = Column(Integer, primary_key=True)
    nome = Column(String(50))
    curso_id = Column(String(30), ForeignKey('cursos.nome', ondelete='SET NULL', onupdate='CASCADE'))

    def __repr__(self):
        return f'Aluno(nro_matric={self.nro_matric}, nome={self.nome}, curso_id={self.curso_id})'

class Grade(Base):
    __tablename__ = 'grades'
    ano = Column(SmallInteger, primary_key=True)
    curso_id = Column(String(30), ForeignKey('cursos.nome', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, unique=True)
    disciplinas = relationship('Disciplina', secondary='grade_disciplina') 
    
    def __repr__(self):
        return f'Grade(ano={self.ano}, curso_id={self.curso_id}, disciplinas={self.disciplinas})'

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
    carga_horaria = Column(SmallInteger)

    def __repr__(self):
        return f'Disciplina(codigo={self.codigo}, nome={self.nome}, carga_horaria={self.carga_horaria})'

class GradeDisciplina(Base):
    __tablename__ = 'grade_disciplina'
    grade_id_ano = Column(SmallInteger, primary_key=True)
    grade_id_curso = Column(String(30), primary_key=True)
    disciplina_id = Column(String(10), ForeignKey('disciplinas.codigo', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    __table_args__ = (ForeignKeyConstraint([grade_id_ano, grade_id_curso],
                                           [Grade.ano, Grade.curso_id], ondelete='CASCADE', onupdate='CASCADE'), {})

    def __repr__(self):
        return f'GradeDisciplina(grade_id_ano={self.grade_id_ano}, grade_id_curso={self.grade_id_curso}, disciplina_id={self.disciplina_id})'