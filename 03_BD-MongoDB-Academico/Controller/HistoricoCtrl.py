from DAO.Mapeamento import Historico
from tkinter.constants import ACTIVE
from View.HistoricoView import LimiteConsultaHistorico, LimiteHistorico, LimiterRelatorioHistorico
from Model.HistoricoModel import ManipulaBanco

class ErroRequisicao(Exception): pass

class ConexaoBD(Exception): pass

class PreencherCampos(Exception): pass

class PreencherCampoId(Exception): pass

class ErroRequisicao(Exception): pass

class HistoricoNaoCadastrado(Exception): pass

class AlunoInexistente(Exception): pass

class CtrlHistorico():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaDiscNota = []

    # Função que serão chamadas da main, mostrar tela ------------------------------------
    
    def exibirTela(self, frame):
        listaDisciplinas = self.ctrlPrincipal.ctrlDisciplina.getListaDisciplinas()
        listaMatricAlunos = self.ctrlPrincipal.ctrlAluno.getListaMatricAluno()
        try:
            if listaDisciplinas==None or listaMatricAlunos==None: raise ErroRequisicao()
        except ErroRequisicao:
            self.limite.mostraMessagebox('ERROR', 'Houve erro na requisição', True)
        else:
            self.limite = LimiteHistorico(self, frame, listaMatricAlunos, listaDisciplinas)

    def exibirTelaConsulta(self, frame):
        listaMatricAlunos = self.ctrlPrincipal.ctrlAluno.getListaMatricAluno()
        try:
            if listaMatricAlunos==None: raise ErroRequisicao()
        except ErroRequisicao: self.limite.mostraMessagebox('ERROR', 'Houve erro na requisição', True)
        else:
            self.limiteConsulta = LimiteConsultaHistorico(self, frame, listaMatricAlunos)

    # Funções auxiliares -----------------------------------------------------------------

    def buscaGradeDoAluno(self, matric):
        todosCursos = self.ctrlPrincipal.ctrlCurso.getListaCursos()
        try:
            if todosCursos == False: raise ConexaoBD()
        except ConexaoBD: return None
        else:
            for curso in todosCursos:
                for aluno in curso.alunos:
                    if aluno.matricula == int(matric):
                        return curso.grade
            return None

    # Funções de CRUD dos buttons ----------------------------------------------------------
    
    def inserirHistorico(self):
        matric = self.limite.escolhaMatric.get()
        ano = self.limite.inputAno.get()
        semestre = self.limite.valorSemestre.get()
        codDisc = self.limite.listboxDisc.get(ACTIVE)
        nota = self.limite.inputNota.get()
        if float(nota) >= 6: status = 'APROVADO'
        else: status = 'REPROVADO'
        # verificar se a disciplina é obrigatória
        gradeDoAluno = self.buscaGradeDoAluno(matric) 
        try:
            if len(matric)==0 or len(ano)==0 or semestre==None or len(codDisc)==0 or len(nota)==0:
                raise PreencherCampos()
            if gradeDoAluno==None: raise ErroRequisicao()
        except PreencherCampos: self.limite.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        except ErroRequisicao: self.limite.mostraMessagebox('ERROR', 'Houve erro na requisição', True)
        else:
            obrigatorio = False
            for disc in gradeDoAluno.disciplinas:
                if disc['codigo'] == codDisc:
                    obrigatorio=True
                    break
            disciplina = self.limite.getDisciplinaByCode(codDisc)
            self.listaDiscNota.append({
                'codigoDisciplina': disciplina.codigo,
                'nomeDisciplina': disciplina.nome,
                'disciplinaCH': disciplina.cargaHoraria,
                'nota': float(nota),
                'status': status,
                'obrigatorio': obrigatorio
            })
            self.limite.mostraMessagebox('SUCESSO', 'Disciplina e nota inserida na lista', False)
            self.limite.limpaDiscNota()

    def cadastrarSemestre(self):
        matric = int(self.limite.escolhaMatric.get())
        ano = int(self.limite.inputAno.get())
        semestre = int(self.limite.valorSemestre.get())
        try:
            if matric==None or ano==None or semestre==None:
                raise PreencherCampos()
        except PreencherCampos: self.limite.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            aluno = self.ctrlPrincipal.ctrlAluno.getAlunoByCode(matric)
            try:
                if aluno==None: raise ErroRequisicao()
            except ErroRequisicao: self.limite.mostraMessagebox('ERROR', 'Houve erro na requisição', True)
            else:
                historico = Historico(aluno=aluno, ano=ano, semestre=semestre, discNotaStatus=self.listaDiscNota)
                statusBanco = ManipulaBanco.cadastraHistorico(historico)
                try:
                    if statusBanco==False: raise ConexaoBD()
                except ConexaoBD(): self.limite.mostraMessagebox('ERROR', 'Falha de conexão com o Banco de Dados', True)
                else:
                    self.limite.mostraMessagebox('SUCESSO', f'Historico de {aluno.nome} cadastrado com sucesso', False)

    def consultaHistorico(self, event, frame):
        try:
            matric = int(self.limiteConsulta.escolhaMatric.get())
            if matric==None: raise PreencherCampoId()
        except PreencherCampoId: self.limiteConsulta.mostraMessagebox('ALERTA', 'Campo matrícula deve ser preenchido', True)
        except ValueError: self.limiteConsulta.mostraMessagebox('ALERTA', 'A matrícula deve ser somente um dado número inteiro', True)
        else:
            aluno = self.ctrlPrincipal.ctrlAluno.getAlunoByCode(int(matric))
            historicosAluno = ManipulaBanco.consultaHistorico(aluno)
            try:
                if historicosAluno == False: raise ConexaoBD()
                if historicosAluno == None: raise HistoricoNaoCadastrado()
                if aluno == None: raise ErroRequisicao()
            except ConexaoBD: self.limiteConsulta.mostraMessagebox('ERROR', 'Falha de conexão com o Banco de Dados', True)
            except HistoricoNaoCadastrado: self.limiteConsulta.mostraMessagebox('ALERTA', 'Historico não cadastrada', True)
            except ErroRequisicao: self.limiteConsulta.mostraMessagebox('ERROR', 'Houve erro na requisição ou aluno inexitente', True)
            else:
                grade = self.buscaGradeDoAluno(matric)
                try:
                    if grade == None: raise AlunoInexistente()
                except AlunoInexistente: self.limiteConsulta.mostraMessagebox('ERROR', 'Aluno Inexistente', True)
                else:
                    LimiterRelatorioHistorico(frame, matric, aluno.nome, grade, historicosAluno)
            finally:
                self.limiteConsulta.limparConsulta()

    def deletarHistorico(self):
        try:
            matric = int(self.limiteConsulta.escolhaMatric.get())
            if matric==None: raise PreencherCampoId()
        except PreencherCampoId: self.limiteConsulta.mostraMessagebox('ALERTA', 'Campo matrícula deve ser preenchido', True)
        except ValueError: self.limiteConsulta.mostraMessagebox('ALERTA', 'A matrícula deve ser somente um dado número inteiro', True)
        else:
            aluno = self.ctrlPrincipal.ctrlAluno.getAlunoByCode(int(matric))
            status = ManipulaBanco.deletaHistorico(aluno)
            try:
                if status==False: raise ConexaoBD()
            except ConexaoBD: self.limiteConsulta.mostraMessagebox('ERROR', 'Falha de conexão com o banco de dados', True)
            else:
                self.limiteConsulta.mostraMessagebox('SUCESSO', f'Histórico do aluno {aluno.nome} removido com sucesso', False)
            finally:
                self.limiteConsulta.limparConsulta()