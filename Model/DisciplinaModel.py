from DAO.DAO import DAOCrud

class ManipulaBanco():
    def cadastraDisciplina(disciplina):
        try:
            sessao = DAOCrud.getSession()
            DAOCrud.insere(sessao, disciplina)
            sessao.commit()
            sessao.close()
            return True
        except:
            return False

    def deletaDisciplina(id):
        try:
            sessao = DAOCrud.getSession()
            DAOCrud.deletaDisciplina(sessao, id)
            sessao.commit()
            sessao.close()
            return True
        except:
            return False
    
    def listaDisciplinas():
        try:
            sessao = DAOCrud.getSession()
            sessao.expire_on_commit = False
            disciplinas = DAOCrud.listaDisciplinas(sessao)
            sessao.commit()
            sessao.close()
            return disciplinas
        except :
            return False

    def consultaDisciplina(id):
        try:
            sessao = DAOCrud.getSession()
            sessao.expire_on_commit = False
            disciplina = DAOCrud.consultaDisciplina(sessao, id)
            sessao.commit()
            sessao.close()
            return disciplina
        except :
            return False

    def atualizaDisciplina(id, nomeDisc, chDisc):
        try:
            sessao = DAOCrud.getSession()
            disciplina = DAOCrud.consultaDisciplina(sessao, id)
            DAOCrud.atualizaDisciplina(disciplina, nomeDisc, chDisc)
            sessao.commit()
            sessao.close()
            return True
        except :
            return False