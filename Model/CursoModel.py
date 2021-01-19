from DAO.DAO import DAOCrud

class ManipulaBanco():
    def cadastraCurso(curso):
        try:
            sessao = DAOCrud.getSession()
            DAOCrud.insere(sessao, curso)
            sessao.commit()
            sessao.close()
            return True
        except:
            return False

    def deletaCurso(id):
        try:
            sessao = DAOCrud.getSession()
            DAOCrud.deletaCurso(sessao, id)
            sessao.commit()
            # sessao.close()
            return True
        except:
            return False
    
    def listaCursos():
        try:
            sessao = DAOCrud.getSession()
            sessao.expire_on_commit = False
            cursos = DAOCrud.listaCursos(sessao)
            sessao.commit()
            # sessao.close()
            return cursos
        except :
            return False

    def consultaCurso(id):
        try:
            sessao = DAOCrud.getSession()
            sessao.expire_on_commit = False
            curso = DAOCrud.consultaCurso(sessao, id)
            sessao.commit()
            # sessao.close()
            return curso
        except :
            return False