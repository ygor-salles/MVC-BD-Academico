import os.path
import pickle
from View.HistoricoView import *
from Model.HistoricoModel import Historico

class MatriculaNaoEncontrada(Exception):
    pass

class CamposNaoPreenchidos(Exception):
    pass

class CtrlHistorico():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaDisc = []
        self.listaCodDisc = []
        self.notaDisc = []

        if not os.path.isfile("Historico.pickle"):
            self.listaHistoricos =  []
        else:
            with open("Historico.pickle", "rb") as f:
                self.listaHistoricos = pickle.load(f)

    #Função para persistencia de dados ---------------------------------------------
    
    def salvaHistoricos(self):
        if len(self.listaHistoricos) != 0:
            with open("Historico.pickle","wb") as f:
                pickle.dump(self.listaHistoricos, f)

    # Funções instanciadoras, recebe da main ---------------------------------------
    
    def insereHistoricos(self, root):
        self.listaDisc = []
        self.notaDisc = []
        self.listaCodDisc = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisciplinas()
        listaMatricAluno = self.ctrlPrincipal.ctrlAluno.getListaNroMatric()
        self.limiteIns = LimiteInsereHistorico(self, root, self.listaCodDisc, listaMatricAluno)

    def mostraHistoricos(self):
        string = '..................RELATÓRIO DE HISTÓRICOS DOS ALUNOS..................'
        for his in self.listaHistoricos:
            string = self.emitirHistorico(his, string)
        self.limiteMostra = LimiteMostraHistorico(string)

    def consultaHistoricos(self, root):
        self.limiteConsulta = LimiteConsultaHistorico(self, root)

    def excluiHistoricos(self, root):
        self.limiteExclui = LimiteExcluiHistorico(self, root)

    #Funções auxiliares ------------------------------------------------------------

    def emitirHistorico(self, his, string):
        eletiva=0
        obrigatoria=0
        total=0
        string += '\nMatrícula: '+str(his.getAluno().getNroMatric())
        string += '\nNome: '+his.getAluno().getNome()
        string += '\n\n|Ano|Semestre|Cod. Disciplina|Nome Disciplina|CH|Nota|Status|\n'
        encontrou=False
        grade=''
        for hisDisc, nota in his.getNotaDisc():
            if nota >= 6:
                string += '{} - {} - {} - {} - {} - {} - Aprovado\n'.format(his.getAno(), his.getSemestre(), hisDisc.getCodigo(), \
                    hisDisc.getNome(), hisDisc.getCargaHoraria(), nota)
            else:
                string += '{} - {} - {} - {} - {} - {} - Reprovado\n'.format(his.getAno(), his.getSemestre(), hisDisc.getCodigo(), \
                    hisDisc.getNome(), hisDisc.getCargaHoraria(), nota)
            total += int(hisDisc.getCargaHoraria())
            
            for curso in self.ctrlPrincipal.ctrlCurso.listaCursos:
                for aluno in curso.getListaAlunos():
                    if aluno.getNroMatric() == his.getAluno().getNroMatric():
                        grade=curso.getGrade().getAnoCurso()
                        nroMatric = aluno.getNroMatric()
                        for disc in curso.getGrade().getListaDisc():
                            if disc.getCodigo() == hisDisc.getCodigo() and his.getAluno().getNroMatric() == nroMatric:
                                obrigatoria += int(hisDisc.getCargaHoraria())
                        
        eletiva = int(total-obrigatoria)    
        string += '\nGrade: '+str(grade)
        string += '\nTotal Carga Horária obrigatória: {} \nTotal Carga Horária eletiva: {}\n'.format(obrigatoria, eletiva)
        string += '----------------------------------------------------------------------\n'
        return string

    def getHistorico(self, matricAluno):
        historico = None
        for hist in self.listaHistoricos:
            if hist.getAluno().getNroMatric() == matricAluno:
                return hist
        return historico

    #Função de CRUD ----------------------------------------

    # Inserção -----------------------------
    def insereDisciplina(self, event):
        nroMatric = self.limiteIns.comboAluno.get()
        semestre = self.limiteIns.comboSemestre.get()
        ano = self.limiteIns.inputAno.get()
        nota = self.limiteIns.inputNota.get()
        disciplinaSelecionada = self.limiteIns.listboxDisciplina.get(tk.ACTIVE)
        try:
            if len(nroMatric)==0 or len(semestre)==0 or len(ano)==0 or len(nota)==0 or len(disciplinaSelecionada)==0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteIns.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', True)
        else:
            nota=float(nota)
            disciplina = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(disciplinaSelecionada)
            self.listaDisc.append(disciplina)
            self.notaDisc.append((disciplina, nota))
            self.limiteIns.mostraMessagebox('Sucesso', 'Disciplina e nota inserida no histórico com sucesso!', False)
            self.limiteIns.listboxDisciplina.delete(tk.ACTIVE)
            self.limiteIns.inputNota.delete(0, len(self.limiteIns.inputNota.get()))
    
    def criaSemestre(self, event):
        alunoSelecionado = self.limiteIns.comboAluno.get()
        aluno = self.ctrlPrincipal.ctrlAluno.getAluno(alunoSelecionado)
        semestre = self.limiteIns.comboSemestre.get()
        ano = self.limiteIns.inputAno.get()
        historico = Historico(self.listaDisc, aluno)
        historico.setSemestre(semestre)
        historico.setAno(ano)
        historico.setNotaDisc(self.notaDisc)
        self.listaHistoricos.append(historico)
        self.limiteIns.mostraMessagebox('Sucesso', 'Semestre criado no histórico do Aluno com sucesso!', False)
        self.limiteIns.janela.destroy()

    # Consulta ------------------------------------
    def enterConsulta(self, event):
        matricAluno = self.limiteConsulta.inputMatricAluno.get()
        encontrou=False
        try:
            if len(matricAluno)==0:
                raise CamposNaoPreenchidos()
            string= '..................RELATÓRIO DE HISTÓRICO DO ALUNO..................'
            for hist in self.listaHistoricos:
                if matricAluno == hist.getAluno().getNroMatric():
                    encontrou=True
                    string = self.emitirHistorico(hist, string)
            if encontrou==False:
                raise MatriculaNaoEncontrada()
        except CamposNaoPreenchidos:
            self.limiteConsulta.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', True)
        except MatriculaNaoEncontrada:
            self.limiteConsulta.mostraMessagebox('Error', 'Nenhum histórico foi cadastrado para essa matrícula!', True)
        else:
            LimiteMostraHistorico(string)
        finally:
            self.limiteConsulta.clearConsulta(event)

    # Exclui ------------------------------------------
    def excluiHandler(self, event):
        matricAluno = self.limiteExclui.inputMatricAluno.get()
        historico = self.getHistorico(matricAluno)
        try:
            if len(matricAluno)==0:
                raise CamposNaoPreenchidos()
            elif historico == None:
                raise MatriculaNaoEncontrada()
        except CamposNaoPreenchidos:
            self.limiteExclui.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', True)
        except MatriculaNaoEncontrada:
            self.limiteExclui.mostraMessagebox('Alerta', 'Histórico não encontrado', True)
        else:
            self.listaHistoricos.remove(historico)
            self.limiteExclui.mostraMessagebox('Sucesso', 'Histórico de {} excluído com sucesso'.format(matricAluno), False)
            self.limiteExclui.clearExclusao(event) 