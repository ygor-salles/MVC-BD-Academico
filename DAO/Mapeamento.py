from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, SmallInteger, ForeignKeyConstraint, Float, CheckConstraint, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text

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
    grade = relationship('Grade', uselist=False, cascade="all, delete", passive_deletes=True)
    def __repr__(self):
        return f'Curso(nome={self.nome}, alunos={self.alunos}, grade={self.grade})'

class Disciplina(Base):
    __tablename__ = 'disciplinas'
    codigo = Column(String(10), primary_key=True)
    nome = Column(String(50))
    carga_horaria = Column(SmallInteger)
    ativo = Column(Boolean, server_default=text('true'))

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

class Historico(Base):
    __tablename__ = 'historicos'
    __table_args__ = (
        CheckConstraint('(semestre = 1) OR (semestre = 2)'),
    )
    id = Column(Integer, primary_key=True)
    nro_matric = Column(ForeignKey('alunos.nro_matric', ondelete='CASCADE', onupdate='CASCADE'))
    semestre = Column(SmallInteger)
    ano = Column(SmallInteger)
    
    aluno = relationship('Aluno', uselist=False)
    disciplinas = relationship('HistoricoDisciplina')
    def __repr__(self):
        return f'Historico(id={self.id}, nro_matric={self.nro_matric}, semestre={self.semestre}, ano={self.ano}, aluno={self.aluno}, disciplinas={self.disciplinas})'

class HistoricoDisciplina(Base):
    __tablename__ = 'historico_disciplina'
    __table_args__ = (
        CheckConstraint("((status)::text = 'APROVADO'::text) OR ((status)::text = 'REPROVADO'::text)"),
    )
    historico_id = Column(ForeignKey('historicos.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    disciplina_id = Column(ForeignKey('disciplinas.codigo'), primary_key=True)
    nota_disciplina = Column(Float(53))
    status = Column(String(10))
    obrigatorio = Column(Boolean)

    disciplinas = relationship('Disciplina')
    def __repr__(self):
        return f'HistoricoDisciplina(historico_id={self.historico_id}, disciplina_id={self.disciplina_id}, nota_disciplina={self.nota_disciplina}, status={self.status}, obrigatorio={self.obrigatorio})'