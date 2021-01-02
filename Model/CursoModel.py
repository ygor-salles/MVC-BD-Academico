from config.DAO import DAOCrud

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
            curso = DAOCrud.consultaCurso(sessao, id)
            DAOCrud.deleta(sessao, curso)
            sessao.commit()
            sessao.close()
            return True
        except:
            return False
    
    def listaCursos():
        try:
            sessao = DAOCrud.getSession()
            cursos = DAOCrud.listaCursos(sessao)
            sessao.commit()
            return cursos
        except :
            return False

    def consultaCurso(id):
        try:
            sessao = DAOCrud.getSession()
            sessao.expire_on_commit = False
            curso = DAOCrud.consultaCurso(sessao, id)
            sessao.commit()
            sessao.close()
            return curso
        except :
            return False

    def atualizaCurso(id, nomeCurso):
        try:
            sessao = DAOCrud.getSession()
            curso = DAOCrud.consultaCurso(sessao, id)
            DAOCrud.atualizaCurso(curso, nomeCurso)
            sessao.commit()
            sessao.close()
            return True
        except :
            return False