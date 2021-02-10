from DAO.DAO import DAOCrud

class ManipulaBanco():
    def cadastraGrade(obj):
        try:
            DAOCrud.insere(obj)
            return True
        except:
            return False
    
    def listaGrade():
        try:
            return DAOCrud.listaGrades()
        except:
            return False

    def consultaGrade(anoCurso):
        try:
            return DAOCrud.buscaGrade(anoCurso)
        except:
            return False

    def deletaGrade(anoCurso):
        try:
            DAOCrud.removeGrade(anoCurso)
            return True
        except:
            return False

    def atualizaGrade(anoCurso, listaDisciplinas):
        try:
            DAOCrud.atualizaGrade(anoCurso, listaDisciplinas)
            return True
        except:
            return False