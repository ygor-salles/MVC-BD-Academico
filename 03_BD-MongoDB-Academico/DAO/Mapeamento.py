from flask import Flask
from flask_mongoalchemy import MongoAlchemy
app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'academico'
db = MongoAlchemy(app)

class Disciplina(db.Document):
    codigo = db.StringField()
    nome = db.StringField()
    cargaHoraria = db.IntField()

class Aluno():
    def __init__(self, nroMatric, nome, curso):
        self.__nroMatric = nroMatric
        self.__nome = nome
        self.__curso = curso

    def getNroMatric(self):
        return self.__nroMatric
    
    def getNome(self):
        return self.__nome

    def getCurso(self):
        return self.__curso