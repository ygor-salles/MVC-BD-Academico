from DAO.Mapeamento import Aluno, Curso, Disciplina, Grade

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
    def listaGrades():
        return Grade.objects()

    def buscaGrade(anoCurso):
        return Grade.objects(anoCurso=anoCurso).first()

    def removeGrade(anoCurso):
        Grade.objects(anoCurso=anoCurso).delete()

    def atualizaGrade(anoCurso, listaDisciplinas):
        Grade.objects(anoCurso=anoCurso).update(disciplinas=listaDisciplinas)

    # Métodos cursos ---------------------------------------
    def listaCursos():
        return Curso.objects()

    def buscaCurso(nomeCurso):
        return Curso.objects(nome=nomeCurso).first()

    def removeCurso(nomeCurso):
        Curso.objects(nome=nomeCurso).delete()

    def atualizaCurso(nomeCurso, listaAlunos, grade):
        Curso.objects(nome=nomeCurso).update(alunos=listaAlunos, grade=grade)
