from DAO.Mapeamento import Aluno, Curso, Disciplina

class DAOCrud():
    
    # Métodos gerais -----------------------------------------
    def insere(obj):
        obj.save()

    # Métodos disciplinas ------------------------------------
    def listaDisciplinas():
        return Disciplina.objects()

    def buscaDisciplina(codigo):
        return Disciplina.objects(codigo=codigo).first()

    def removeDisciplina(codigo):
        Disciplina.objects(codigo=codigo).delete()

    def atualizaDisciplina(codigo, nome, cargaHoraria):
        Disciplina.objects(codigo=codigo).update(nome=nome, cargaHoraria=cargaHoraria)

    # Métodos alunos ------------------------------------
    def listaAlunos():
        return Aluno.objects()

    def buscaAluno(matricula):
        return Aluno.objects(matricula=matricula).first()

    def removeAluno(matricula):
        Aluno.objects(matricula=matricula).delete()

    def atualizaAluno(matricula, nome, curso):
        Aluno.objects(matricula=matricula).update(nome=nome, curso=curso)

    # Métodos cursos ---------------------------------------
    def listaCursos():
        return Curso.objects()

    def buscaCurso(nome):
        return Curso.objects(nome=nome).first()

    def removeCurso(nome):
        Curso.objects(nome=nome).delete()

    def atualizaCurso(nome, grade):
        Curso.objects(nome=nome).update(nome=nome, grade=grade)
