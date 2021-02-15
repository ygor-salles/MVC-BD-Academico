from mongoengine import *
from mongoengine.connection import connect
from mongoengine.document import Document, EmbeddedDocument
from mongoengine.fields import EmbeddedDocumentField, FloatField, IntField, ListField, ReferenceField, StringField
from mongoengine.queryset.base import CASCADE
connect('academico')

class Disciplina(Document):
    codigo = StringField(unique=True)
    nome = StringField()
    cargaHoraria = IntField()

    def __repr__(self):
        return f'Disciplina(codigo{self.codigo}, nome={self.nome}, cargaHoraria={self.cargaHoraria})'

class Aluno(Document):
    matricula = IntField(unique=True)
    nome = StringField()
    curso = StringField()

    def __repr__(self):
        return f'Disciplina(matricula{self.matricula}, nome={self.nome}, curso={self.curso})'

class Grade(Document):
    anoCurso = StringField(unique=True)
    disciplinas = ListField()

    def __repr__(self):
        return f'Grade(anoCurso={self.anoCurso}, disciplinas={self.disciplinas})'

class Curso(Document):
    nome = StringField(unique=True)
    grade = ReferenceField(Grade)
    alunos = ListField(ReferenceField(Aluno))

    def __repr__(self):
        return f'Curso(nome={self.nome}, grade=(anoCurso={self.grade.ano}), alunos={self.alunos})'