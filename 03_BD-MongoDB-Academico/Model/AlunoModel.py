from DAO.DAO import DAOCrud

class ManipulaBanco():
    def cadastraAluno(obj):
        try:
            DAOCrud.insere(obj)
            return True
        except:
            return False
    
    def listaAluno():
        try:
            return DAOCrud.listaAlunos()
        except:
            return False

    def consultaAluno(matricula):
        try:
            return DAOCrud.buscaAluno(matricula)
        except:
            return False

    def deletaAluno(matricula):
        try:
            DAOCrud.removeAluno(matricula)
            return True
        except:
            return False

    def atualizaAluno(matricula, nome, curso):
        try:
            DAOCrud.atualizaAluno(matricula, nome, curso)
            return True
        except:
            return False