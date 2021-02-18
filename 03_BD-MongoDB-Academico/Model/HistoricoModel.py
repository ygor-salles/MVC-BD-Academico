from DAO.DAO import DAOCrud

class ManipulaBanco():
    def cadastraHistorico(obj):
        try:
            DAOCrud.insere(obj)
            return True
        except:
            return False

    def consultaHistorico(aluno):
        try:
            return DAOCrud.buscaHistorico(aluno)
        except:
            return False

    def deletaHistorico(aluno):
        try:
            DAOCrud.removeHistorico(aluno)
            return True
        except:
            return False