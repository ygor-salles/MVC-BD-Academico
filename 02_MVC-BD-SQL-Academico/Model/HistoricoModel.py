from DAO.DAO import DAOCrud
from DAO.Mapeamento import Historico, HistoricoDisciplina
from sqlalchemy.orm.exc import StaleDataError

class ManipulaBanco():
    # insere ---------------------
    def cadastraHistorico(historico: Historico):
        try:
            sessao = DAOCrud.getSession()
            DAOCrud.insere(sessao, historico)
            sessao.commit()
            sessao.close()
            return True
        except:
            return False

    # retorna id SERIAL inserido ------------------
    def retornaByIdHistorico():
        try:
            sessao = DAOCrud.getSession()
            sessao.expire_on_commit = False
            id = DAOCrud.retornaIdInserido(sessao)
            sessao.commit()
            # sessao.close()
            return id
        except:
            return False

    # insere varias disciplinas no historico ------------
    def cadastraListaDiscHistorico(listaRelacionamento: HistoricoDisciplina):
        try:
            sessao = DAOCrud.getSession()
            DAOCrud.insereLista(sessao, listaRelacionamento)
            sessao.commit()
            sessao.close()
            return True
        except:
            return False

    # deleta historico -----------------------------------------
    def deletaHistorico(matric):
        try:
            sessao = DAOCrud.getSession()
            DAOCrud.deletaHistorico(sessao, matric)
            sessao.commit()
            sessao.close()
            return True
        except:
            return False
    
    # listar historicos -----------------------------------------
    def listaHistoricos():
        try:
            sessao = DAOCrud.getSession()
            sessao.expire_on_commit = False
            historicos = DAOCrud.listaHistorico(sessao)
            sessao.commit()
            # sessao.close()
            return historicos
        except :
            return False

    # consulta historico por nro_matric(FK) ---------------------------
    def consultaHistorico(matric):
        try:
            sessao = DAOCrud.getSession()
            sessao.expire_on_commit = False
            historico = DAOCrud.consultaHistorico(sessao, matric)
            sessao.commit()
            #sessao.close()
            return historico
        except:
            return False

    # insere uma disciplina na grade ----------------------------
    def inserirDisciplinaNoHistorico(historicoDisciplina: HistoricoDisciplina):
        try:
            sessao = DAOCrud.getSession()
            DAOCrud.insere(sessao, historicoDisciplina)
            sessao.commit()
            sessao.close()
            return True
        except:
            return False        
    
    # remove uma disciplina na grade ----------------------
    def removerDisciplinaDoHistorico(id_historico, id_disciplina):
        try:
            sessao = DAOCrud.getSession()
            DAOCrud.deletaHistoricoDisciplina(sessao, id_historico, id_disciplina)
            sessao.commit()
            sessao.close()
            return True
        except:
            return False

    # consulta GradeDisciplina para verificar disciplina é obrigatória para o Aluno ou não
    def consultaGradeDisc(gradeAno, gradeCurso, idDisc):
        try:
            sessao = DAOCrud.getSession()
            sessao.expire_on_commit = False
            grade = DAOCrud.consultaGradeDisciplina(sessao, gradeAno, gradeCurso, idDisc)
            sessao.commit()
            # sessao.close()
            return grade
        except StaleDataError as error:
            return False