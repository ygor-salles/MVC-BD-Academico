from DAO.DAO import DAOCrud

class ManipulaBanco():
    def cadastraCurso(obj):
        try:
            DAOCrud.insere(obj)
            return True
        except:
            return False
    
    def listaCurso():
        try:
            return DAOCrud.listaCursos()
        except:
            return False

    def consultaCurso(nome):
        try:
            return DAOCrud.buscaCurso(nome)
        except:
            return False

    def deletaCurso(nome):
        try:
            DAOCrud.removeCurso(nome)
            return True
        except:
            return False

    def atualizaCurso(nome, grade):
        try:
            DAOCrud.atualizaCurso(nome, grade)
            return True
        except:
            return False