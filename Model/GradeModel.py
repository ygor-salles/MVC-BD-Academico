from DAO.Mapeamento import Grade, GradeDisciplina
from DAO.DAO import DAOCrud

class ManipulaBanco():
    # insere ---------------------------
    def cadastraGrade(grade: Grade):
        try:
            sessao = DAOCrud.getSession()
            DAOCrud.insere(sessao, grade)
            sessao.commit()
            sessao.close()
            return True
        except:
            return False

    # insere varias disciplinas na grade ------------
    def cadastraGradeDisciplina(listaRelacionamento: GradeDisciplina):
        try:
            sessao = DAOCrud.getSession()
            DAOCrud.insereLista(sessao, listaRelacionamento)
            sessao.commit()
            sessao.close()
            return True
        except:
            return False

    # deleta grade -----------------------------------------
    def deletaGrade(ano_id, curso_id):
        try:
            sessao = DAOCrud.getSession()
            grade = DAOCrud.consultaGrade(sessao, ano_id, curso_id)
            DAOCrud.deleta(sessao, grade)
            sessao.commit()
            sessao.close()
            return True
        except:
            return False
    
    # listar grades -----------------------------------------
    def listaGrades():
        try:
            sessao = DAOCrud.getSession()
            grades = DAOCrud.listaGrades(sessao)
            sessao.commit()
            return grades
        except :
            return False

    # consulta grade por FK(id) ---------------------------
    def consultaGrade(id_ano, id_curso):
        try:
            sessao = DAOCrud.getSession()
            sessao.expire_on_commit = False
            grade = DAOCrud.consultaGrade(sessao, id_ano, id_curso)
            sessao.commit()
            #sessao.close()
            return grade
        except :
            return False

    # insere uma disciplina na grade ----------------------------
    def inserirDisciplinaNaGrade(gradeDisciplina: GradeDisciplina):
        try:
            sessao = DAOCrud.getSession()
            DAOCrud.insere(sessao, gradeDisciplina)
            sessao.commit()
            sessao.close()
            return True
        except:
            return False        
    
    # remove uma disciplina na grade ----------------------
    def removerDisciplinaDaGrade(gradeAno, gradeCurso, disciplinaCod):
        try:
            sessao = DAOCrud.getSession()
            gradeDisciplina = DAOCrud.consultaGradeDisciplina(sessao, gradeAno, gradeCurso, disciplinaCod)
            DAOCrud.deleta(sessao, gradeDisciplina)
            sessao.commit()
            sessao.close()
            return True
        except:
            return False