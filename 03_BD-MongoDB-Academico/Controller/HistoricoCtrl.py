from DAO.Mapeamento import Historico
from tkinter.constants import ACTIVE
from View.HistoricoView import LimiteHistorico
from Model.HistoricoModel import ManipulaBanco

class ErroRequisicao(Exception): pass

class ConexaoBD(Exception): pass

class PreencherCampos(Exception): pass

class ErroRequisicao(Exception): pass

class CtrlHistorico():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaDiscNota = []

    def exibirTela(self, frame):
        listaDisciplinas = self.ctrlPrincipal.ctrlDisciplina.getListaDisciplinas()
        listaMatricAlunos = self.ctrlPrincipal.ctrlAluno.getListaMatricAluno()
        try:
            if listaDisciplinas==None or listaMatricAlunos==None: raise ErroRequisicao()
        except ErroRequisicao:
            self.limite.mostraMessagebox('ERROR', 'Houve erro na requisição', True)
        else:
            self.limite = LimiteHistorico(self, frame, listaMatricAlunos, listaDisciplinas)

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
            # self.listaDiscNota.append((disciplina.codigo, disciplina.nome, disciplina.cargaHoraria, nota, status, obrigatorio))
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
