import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import Aluno as al
import Disciplina as dic
import Grade as gr
import os.path
import pickle

class MatriculaNaoEncontrada(Exception):
    pass

class CamposNaoPreenchidos(Exception):
    pass

class Historico:
    def __init__(self, listaDisc, aluno):
        self.__listaDisc = listaDisc
        self.__aluno = aluno
        self.__semestre = None
        self.__ano = None
        self.__notaDisc = []
        
    def getListaDisc(self):
        return self.__listaDisc

    def getAluno(self):
        return self.__aluno
    
    def getSemestre(self):
        return self.__semestre
    
    def setSemestre(self, semestre):
        self.__semestre = semestre
    
    def getAno(self):
        return self.__ano
    
    def setAno(self, ano):
        self.__ano = ano
    
    def getNotaDisc(self):
        return self.__notaDisc

    def setNotaDisc(self, notaDisc):
        self.__notaDisc = notaDisc

class LimiteInsereHistorico():
    def __init__(self, controle, root, listaDisc, listaMatricAluno):
        self.janela = root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='CADASTRAR HISTÓRICO DO ALUNO', font=('Heveltica Bold', 14), bg='#76cb69').pack()
    
        self.labelAluno = tk.Label(self.frameBody, text='Nro Matricula do Aluno: ', bg='#76cb69')
        self.labelSemestre = tk.Label(self.frameBody, text='Informe Semestre: ', bg='#76cb69')
        self.labelAno = tk.Label(self.frameBody, text='Informe o ano: ', bg='#76cb69')
        self.labelListaDisc = tk.Label(self.frameBody, text='Selecione as disciplinas \nque o aluno cursou\n no semestre: ', bg='#76cb69')
        self.labelNota = tk.Label(self.frameBody, text='Nota do Aluno na Disciplina: ', bg='#76cb69')

        self.comboAluno = tk.StringVar()
        self.comboboxAluno = ttk.Combobox(self.frameBody, width=15, textvariable=self.comboAluno)
        self.comboboxAluno['values'] = listaMatricAluno

        self.comboSemestre = ttk.Combobox(self.frameBody, values=['1', '2'])

        self.inputAno = tk.Entry(self.frameBody, width=10)
        
        self.listboxDisciplina = tk.Listbox(self.frameBody)
        for disc in listaDisc:
            self.listboxDisciplina.insert(tk.END, disc)

        self.inputNota = tk.Entry(self.frameBody, width=10)

        self.buttonCria = tk.Button(self.frameBody, text='Criar Semestre')
        self.buttonCria.bind('<Button>', controle.criaSemestre)
        self.buttonInsere = tk.Button(self.frameBody, text='Insere Disciplina no Histórico')
        self.buttonInsere.bind('<Button>', controle.insereDisciplina)

        self.labelAluno.grid(row=0, column=0, sticky='W', pady=5)
        self.comboboxAluno.grid(row=0, column=1, sticky='W', pady=5)
        self.labelSemestre.grid(row=1, column=0, sticky='W', pady=5)
        self.comboSemestre.grid(row=1, column=1, sticky='W', pady=5)
        self.labelAno.grid(row=2, column=0, sticky='W', pady=5)
        self.inputAno.grid(row=2, column=1, sticky='W')
        self.labelListaDisc.grid(row=3, column=1, sticky='W')
        self.listboxDisciplina.grid(row=4, column=1, sticky='W', pady=5)
        self.labelNota.grid(row=5, column=0, sticky='W', pady=5)
        self.inputNota.grid(row=5, column=1, sticky='W', pady=5)
        self.buttonInsere.grid(row=6, column=2, sticky='W', pady=5)
        self.buttonCria.grid(row=6, column=3, sticky='W', pady=5)

    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class LimiteMostraHistorico():
    def __init__(self, string):
        messagebox.showinfo('Lista de Historicos', string)

class LimiteConsultaHistorico():
    def __init__(self, controle, root):
        self.janela = root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='CONSULTAR HISTÓRICO DO ALUNO', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelMatricAluno = tk.Label(self.frameBody, text='Matricula do Aluno: ', bg='#76cb69')
        self.inputMatricAluno = tk.Entry(self.frameBody, width=15)

        self.buttonConsulta = tk.Button(self.frameBody, text='Enter')
        self.buttonConsulta.bind('<Button>', controle.enterConsulta)
        self.buttonClear = tk.Button(self.frameBody, text='Clear')
        self.buttonClear.bind('<Button>', controle.clearConsulta)
        self.buttonFinaliza = tk.Button(self.frameBody, text='Finalizar')
        self.buttonFinaliza.bind('<Button>', controle.finalizaConsulta)

        self.labelMatricAluno.grid(row=0, column=0, sticky='W', pady=20)
        self.inputMatricAluno.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonConsulta.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFinaliza.grid(row=1, column=4, sticky='W', pady=20)

class LimiteExcluiHistorico():
    def __init__(self, controle, root):
        self.janela = root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='EXCLUIR HISTÓRICO DO ALUNO', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelMatricAluno = tk.Label(self.frameBody, text='Matricula do Aluno: ', bg='#76cb69')
        self.inputMatricAluno = tk.Entry(self.frameBody, width=15)

        self.buttonConsulta = tk.Button(self.frameBody, text='Excluir')
        self.buttonConsulta.bind('<Button>', controle.excluiHandler)
        self.buttonClear = tk.Button(self.frameBody, text='Clear')
        self.buttonClear.bind('<Button>', controle.clearExclusao)
        self.buttonFinaliza = tk.Button(self.frameBody, text='Finalizar')
        self.buttonFinaliza.bind('<Button>', controle.finalizaExclusao)

        self.labelMatricAluno.grid(row=0, column=0, sticky='W', pady=20)
        self.inputMatricAluno.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonConsulta.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFinaliza.grid(row=1, column=4, sticky='W', pady=20)

    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

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
    
    #Função dos Buttons de Inserção de Histórico ----------------------------------------

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
            messagebox.showerror('Atenção', 'Todos os campos devem ser preenchidos')
        else:
            nota=float(nota)
            disciplina = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(disciplinaSelecionada)
            self.listaDisc.append(disciplina)
            self.notaDisc.append((disciplina, nota))
            self.limiteIns.mostraMessagebox('Sucesso', 'Disciplina e nota inserida no histórico com sucesso!')
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
        self.limiteIns.mostraMessagebox('Sucesso', 'Semestre criado no histórico do Aluno com sucesso!')
        self.limiteIns.janela.destroy()

    # Funções dos Buttons de Consulta ------------------------------------------------------------------------

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
            messagebox.showerror('Atenção', 'Todos os campos devem ser preenchidos')
        except MatriculaNaoEncontrada:
            messagebox.showerror('Error', 'Nenhum histórico foi cadastrado para essa matrícula!')
        else:
            LimiteMostraHistorico(string)
        finally:
            self.clearConsulta(event)
    
    def clearConsulta(self, event):
        self.limiteConsulta.inputMatricAluno.delete(0, len(self.limiteConsulta.inputMatricAluno.get()))
    
    def finalizaConsulta(self, event):
        self.limiteConsulta.janela.destroy()

    # Funções dos Buttons de Exclusão ------------------------------------------------------------------------

    def excluiHandler(self, event):
        matricAluno = self.limiteExclui.inputMatricAluno.get()
        historico = self.getHistorico(matricAluno)
        try:
            if len(matricAluno)==0:
                raise CamposNaoPreenchidos()
            elif historico == None:
                raise MatriculaNaoEncontrada()
        except CamposNaoPreenchidos:
            messagebox.showerror('Atenção', 'Todos os campos devem ser preenchidos')
        except MatriculaNaoEncontrada:
            messagebox.showerror('Alerta', 'Histórico não encontrado')
        else:
            self.listaHistoricos.remove(historico)
            self.limiteExclui.mostraMessagebox('Sucesso', 'Histórico de {} excluído com sucesso'.format(matricAluno))
            self.clearExclusao(event)

    def clearExclusao(self, event):
        self.limiteExclui.inputMatricAluno.delete(0, 'end')
    
    def finalizaExclusao(self, event):
        self.limiteExclui.janela.destroy()