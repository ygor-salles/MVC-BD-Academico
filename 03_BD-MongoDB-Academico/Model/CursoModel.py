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

    def consultaCurso(nomeCurso):
        try:
            return DAOCrud.buscaCurso(nomeCurso)
        except:
            return False

    def deletaCurso(nomeCurso):
        try:
            DAOCrud.removeCurso(nomeCurso)
            return True
        except:
            return False

    def atualizaCurso(nomeCurso, listaAlunos):
        try:
            DAOCrud.atualizaCurso(nomeCurso, listaAlunos)
            return True
        except:
            return False