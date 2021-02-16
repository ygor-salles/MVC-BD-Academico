from DAO.DAO import DAOCrud

class ManipulaBanco():
    def cadastraHistorico(obj):
        try:
            DAOCrud.insere(obj)
            return True
        except:
            return False

    def consultaHistorico(matricula):
        try:
            return DAOCrud.buscaHistorico(matricula)
        except:
            return False

    def deletaHistorico(matricula):
        try:
            DAOCrud.removeHistorico(matricula)
            return True
        except:
            return False