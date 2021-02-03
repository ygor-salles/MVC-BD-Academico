from DAO.Mapeamento import Aluno, Disciplina

class DAOCrud():
    
    # Métodos gerais -----------------------------------------
    def insere(obj):
        obj.save()

    # Métodos disciplinas ------------------------------------
    def listaDisciplinas():
        return Disciplina.query.all()

    def buscaDisciplina(codigo):
        return Disciplina.query.filter(Disciplina.codigo == codigo).first()

    def removeDisciplina(codigo):
        disc = Disciplina.query.filter(Disciplina.codigo == codigo).first()
        disc.remove()

    def atualizaDisciplina(codigo, nome, cargaHoraria):
        disciplina: Disciplina = Disciplina.query.filter(Disciplina.codigo == codigo).first()
        disciplina.nome = nome
        disciplina.cargaHoraria = cargaHoraria
        disciplina.save()

    # Métodos alunos ------------------------------------
    def listaAlunos():
        return Aluno.query.all()

    def buscaAluno(matricula):
        return Aluno.query.filter(Aluno.matricula == matricula).first()

    def removeAluno(matricula):
        disc = Aluno.query.filter(Aluno.matricula == matricula).first()
        disc.remove()

    def atualizaAluno(matricula, nome, curso):
        aluno: Aluno = Aluno.query.filter(Aluno.matricula == matricula).first()
        aluno.nome = nome
        aluno.curso = curso
        aluno.save()
