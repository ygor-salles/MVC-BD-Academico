from config.DAO import DAOCrud

class ManipulaBanco():
    def cadastraGrade(grade):
        try:
            sessao = DAOCrud.getSession()
            DAOCrud.insere(sessao, grade)
            sessao.commit()
            sessao.close()
            return True
        except:
            return False

    def deletaGrade(id):
        try:
            sessao = DAOCrud.getSession()
            grade = DAOCrud.consultaGrade(sessao, id)
            DAOCrud.deleta(sessao, grade)
            sessao.commit()
            sessao.close()
            return True
        except:
            return False
    
    def listaGrades():
        try:
            sessao = DAOCrud.getSession()
            grades = DAOCrud.listaGrades(sessao)
            return grades
        except :
            return False

    def consultaGrade(id):
        try:
            sessao = DAOCrud.getSession()
            sessao.expire_on_commit = False
            grade = DAOCrud.consultaGrade(sessao, id)
            sessao.commit()
            sessao.close()
            return grade
        except :
            return False

    def atualizaGrade(id, nomeGrade):
        try:
            sessao = DAOCrud.getSession()
            grade = DAOCrud.consultaGrade(sessao, id)
            DAOCrud.atualizaGrade(grade, nomeGrade)
            sessao.commit()
            sessao.close()
            return True
        except :
            return False