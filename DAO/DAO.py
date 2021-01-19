from tkinter.constants import TRUE
from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from DAO.Mapeamento import Base, Aluno, Curso, Disciplina, Grade, GradeDisciplina

class DAOCrud():
    # MÉTODOS GERAIS ------------------------------
    def getSession():
        engine = create_engine('postgresql+psycopg2://postgres:123456@localhost:5432/academico', echo=False)
        Session = sessionmaker(bind=engine)
        session = Session()
        Base.metadata.create_all(engine)
        return session

    def insere(sessao, obj):
        sessao.add(obj)

    def insereLista(sessao, listaObj):
        sessao.add_all(listaObj)

    # MÉTODOS ALUNOS ------------------------------
    def consultaAluno(sessao, id):
        return sessao.query(Aluno).filter(Aluno.nro_matric == id).first()
    
    def listaAluno(sessao):
        return sessao.query(Aluno).all()

    def deletaAluno(session, id):
        session.query(Aluno).filter(Aluno.nro_matric==id).delete()

    def atualizaAluno(aluno: Aluno, nomeAluno, curso):
        aluno.nome = nomeAluno
        aluno.curso_id = curso
        
    # MÉTODOS CURSOS ------------------------------
    def consultaCurso(sessao, id):
        return sessao.query(Curso).filter(Curso.nome == id).first()

    def listaCursos(sessao):
        return sessao.query(Curso).all()

    def deletaCurso(sessao, id):
        sessao.query(Curso).filter(Curso.nome == id).delete()

    # MÉTODOS GRADE ----------------------------------
    def consultaGrade(sessao, id_ano, id_curso):
        return sessao.query(Grade).filter(Grade.ano == id_ano, Grade.curso_id == id_curso).first()

    def listaGrades(sessao):
        return sessao.query(Grade).all()

    def deletaGrade(sessao, id_ano, id_curso):
        sessao.query(Grade).filter(Grade.ano==id_ano, Grade.curso_id==id_curso).delete()

    # MÉTODOS DISCIPLINA ----------------------------------
    def consultaDisciplina(sessao, id):
        return sessao.query(Disciplina).filter(Disciplina.codigo == id).first()

    def listaDisciplinas(sessao):
        return sessao.query(Disciplina).all()

    def deletaDisciplina(sessao, id):
        sessao.query(Disciplina).filter(Disciplina.codigo == id).delete()

    def atualizaDisciplina(disciplina: Disciplina, nomeDisc, chDisc):
        disciplina.nome = nomeDisc
        disciplina.carga_horaria = chDisc

    # MÉTODOS GRADEDISCIPLINA -------------------------------------------------------
    def deletaGradeDisciplina(sessao, gradeAno, gradeCurso, disciplinaCod):
        sessao.query(GradeDisciplina).filter(GradeDisciplina.grade_id_ano==gradeAno,
            GradeDisciplina.grade_id_curso==gradeCurso, GradeDisciplina.disciplina_id==disciplinaCod).delete()