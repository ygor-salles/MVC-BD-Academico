from flask import Flask
from flask_mongoalchemy import MongoAlchemy
app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'academico'
db = MongoAlchemy(app)

class Disciplina(db.Document):
    # codigo_index = db.Index().ascending('codigo').unique()
    codigo = db.StringField()
    nome = db.StringField()
    cargaHoraria = db.IntField()

    def __repr__(self):
        return f'Disciplina(codigo{self.codigo}, nome={self.nome}, cargaHoraria={self.cargaHoraria})'

class Aluno(db.Document):
    # matricula_index = db.Index().ascending('matricula').unique()
    matricula = db.IntField()
    nome = db.StringField()
    curso = db.StringField()

    def __repr__(self):
        return f'Disciplina(matricula{self.matricula}, nome={self.nome}, curso={self.curso})'