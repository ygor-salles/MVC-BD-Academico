from config.DAO import DAOCrud

class ManipulaBanco():
    def cadastraAluno(aluno):
        try:
            sessao = DAOCrud.getSession()
            DAOCrud.insere(sessao, aluno)
            sessao.commit()
            sessao.close()
            return True
        except:
            return False

    def deletaAluno(id):
        try:
            sessao = DAOCrud.getSession()
            aluno = DAOCrud.consultaAluno(sessao, id)
            DAOCrud.deleta(sessao, aluno)
            sessao.commit()
            sessao.close()
            return True
        except:
            return False
    
    def listaAlunos():
        try:
            sessao = DAOCrud.getSession()
            alunos = DAOCrud.listaAluno(sessao)
            sessao.commit()
            return alunos
        except :
            return False

    def consultaAluno(id):
        try:
            sessao = DAOCrud.getSession()
            sessao.expire_on_commit = False
            aluno = DAOCrud.consultaAluno(sessao, id)
            sessao.commit()
            sessao.close()
            return aluno
        except :
            return False

    def atualizaAluno(id, nomeAluno):
        try:
            sessao = DAOCrud.getSession()
            aluno = DAOCrud.consultaAluno(sessao, id)
            DAOCrud.atualizaAluno(aluno, nomeAluno)
            sessao.commit()
            sessao.close()
            return True
        except :
            return False