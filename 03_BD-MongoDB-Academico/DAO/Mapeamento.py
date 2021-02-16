from enum import Enum, IntEnum
from mongoengine import *
from mongoengine.connection import connect
from mongoengine.document import Document
from mongoengine.fields import EnumField, FloatField, IntField, ListField, ReferenceField, StringField
from mongoengine.queryset.base import CASCADE
connect('academico')

class Disciplina(Document):
    codigo = StringField(unique=True)
    nome = StringField()
    cargaHoraria = IntField()

class Aluno(Document):
    matricula = IntField(unique=True)
    nome = StringField()

class Grade(Document):
    anoCurso = StringField(unique=True)
    disciplinas = ListField()

class Curso(Document):
    nome = StringField(unique=True)
    grade = ReferenceField(Grade)
    alunos = ListField(ReferenceField(Aluno))

class Historico(Document):
    aluno = ReferenceField(Aluno)
    ano = IntField()
    semestre = IntField()
    discNotaStatus = ListField()

