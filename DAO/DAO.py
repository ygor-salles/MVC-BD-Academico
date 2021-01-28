from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from DAO.Mapeamento import Base, Aluno, Curso, Disciplina, Grade, GradeDisciplina, Historico, HistoricoDisciplina

class DAOCrud():
    # MÉTODOS GERAIS ------------------------------
    def getSession():
        # engine = create_engine('postgresql+psycopg2://postgres:123456@localhost:5432/academico', echo=False)
        engine = create_engine('sqlite:///teste.db', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        Base.metadata.create_all(engine)
        return session

    def insere(sessao, obj):
        sessao.add(obj)

    def insereLista(sessao, listaObj):
        sessao.add_all(listaObj)

    def retornaIdInserido(sessao):
        idHistorico = None
        consultaSelect = sessao.query(func.max(Historico.id)).first()
        for i in consultaSelect: idHistorico = i
        return idHistorico

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

    # O delete de disciplina não irá excluir definitivamente do banco, só ficará invisível para a aplicação
    def deletaDisciplina(disciplina: Disciplina):
        disciplina.ativo = False

    def atualizaDisciplina(disciplina: Disciplina, nomeDisc, chDisc):
        disciplina.nome = nomeDisc
        disciplina.carga_horaria = chDisc

    # caso o usuário insira novamente a disciplina que ja foi deletada, basta atualizar para ativo e os campos 
    def atualizaDisciplinaParaAtivo(disciplina: Disciplina, nomeDisc, chDisc):
        disciplina.ativo = True
        disciplina.nome = nomeDisc
        disciplina.carga_horaria = chDisc

    # MÉTODOS GRADEDISCIPLINA -------------------------------------------------------
    def deletaGradeDisciplina(sessao, gradeAno, gradeCurso, disciplinaCod):
        sessao.query(GradeDisciplina).filter(GradeDisciplina.grade_id_ano==gradeAno,
            GradeDisciplina.grade_id_curso==gradeCurso, GradeDisciplina.disciplina_id==disciplinaCod).delete()

    def consultaGradeDisciplina(sessao, gradeAno, gradeCurso, disciplinaCod):
        return sessao.query(GradeDisciplina).filter(GradeDisciplina.grade_id_ano==gradeAno,
            GradeDisciplina.grade_id_curso==gradeCurso, GradeDisciplina.disciplina_id==disciplinaCod).first()

    # MÉTODOS HISTORICO -------------------------------------------------
    def consultaHistorico(sessao, matric):
        return sessao.query(Historico).filter(Historico.nro_matric == matric)
    
    def listaHistorico(sessao):
        return sessao.query(Historico).all()

    def deletaHistorico(sessao, matric):
        sessao.query(Historico).filter(Historico.nro_matric == matric).delete()
    
    def atualizarHistorico(historico: Historico, semestre, ano):
        historico.semestre = semestre
        historico.ano = ano

    # MÉTODO HISTORICODISCIPLINA ----------------------------------------
    def deletaHistoricoDisciplina(sessao, id_historico, id_disciplina):
        sessao.query(HistoricoDisciplina).filter(HistoricoDisciplina.disciplina_id==id_disciplina, 
            HistoricoDisciplina.historico_id==id_historico).delete()