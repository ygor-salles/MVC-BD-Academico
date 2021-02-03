from DAO.DAO import DAOCrud

class ManipulaBanco():
    def cadastraDisciplina(obj):
        try:
            DAOCrud.insere(obj)
            return True
        except:
            return False
    
    def listaDisciplina():
        try:
            return DAOCrud.listaDisciplinas()
        except:
            return False

    def consultaDisciplina(codigo):
        try:
            return DAOCrud.buscaDisciplina(codigo)
        except:
            return False

    def deletaDisciplina(codigo):
        try:
            DAOCrud.removeDisciplina(codigo)
            return True
        except:
            return False

    def atualizaDisciplina(codigo, nome, cargaHoraria):
        try:
            DAOCrud.atualizaDisciplina(codigo, nome, cargaHoraria)
            return True
        except:
            return False