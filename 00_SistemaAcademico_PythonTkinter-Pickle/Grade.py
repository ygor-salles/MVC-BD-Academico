import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Disciplina as dic
import Curso as cr
import os.path
import pickle

class GradeDuplicada(Exception):
    pass

class GradeNaoEncontrada(Exception):
    pass

class CamposNaoPreenchidos(Exception):
    pass

class Grade:
    def __init__(self, anoCurso, listaDisc):
        self.__anoCurso = anoCurso
        self.__listaDisc = listaDisc

    def getAnoCurso(self):
        return self.__anoCurso

    def getListaDisc(self):
        return self.__listaDisc
    
        
class LimiteInsereGrade():
    def __init__(self, controle, root, listaCodDisc):
        self.janela = root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='CADASTRAR GRADE', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelAnoCurso = tk.Label(self.frameBody, text='Ano/Curso: ', bg='#76cb69')
        self.labelDisc = tk.Label(self.frameBody, text='Escolha as disciplinas: ', bg='#76cb69')
        
        self.inputAnoCurso = tk.Entry(self.frameBody, width=20)
        
        self.listbox = tk.Listbox(self.frameBody)
        for disc in listaCodDisc:
            self.listbox.insert(tk.END, disc)

        self.buttonInsere = tk.Button(self.frameBody ,text="Insere Disciplina")           
        self.buttonInsere.bind("<Button>", controle.insereHandler)
        self.buttonCria = tk.Button(self.frameBody ,text="Cria Grade")           
        self.buttonCria.bind("<Button>", controle.criaHandler)

        self.labelAnoCurso.grid(row=0, column=0, sticky='W', pady=20)
        self.inputAnoCurso.grid(row=0, column=1, sticky='W', pady=20)
        self.labelDisc.grid(row=1, column=1, sticky='W')
        self.listbox.grid(row=2, column=1, sticky='W')
        self.buttonCria.grid(row=3, column=2, sticky='W', pady=20)
        self.buttonInsere.grid(row=3, column=3, sticky='W', pady=20)
    
    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class LimiteMostra():
    def __init__(self, string):
        messagebox.showinfo('Lista de Grades', string) 

class LimiteConsultaGrade():
    def __init__(self, controle, root):
        self.janela=root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='CONSULTAR GRADE', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelAnoCurso = tk.Label(self.frameBody, text='Ano/Curso: ', bg='#76cb69')
        self.inputAnoCurso = tk.Entry(self.frameBody, width=20)

        self.buttonConsultar = tk.Button(self.frameBody, text='Realizar Consulta')
        self.buttonConsultar.bind('<Button>', controle.consultaHandler)
        self.buttonClear = tk.Button(self.frameBody ,text='Clear')      
        self.buttonClear.bind('<Button>', controle.clearConsulta)  
        self.buttonFecha = tk.Button(self.frameBody ,text='Finalizar')      
        self.buttonFecha.bind('<Button>', controle.fechaConsulta)

        self.labelAnoCurso.grid(row=0, column=0, sticky='W', pady=20)
        self.inputAnoCurso.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonConsultar.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=1, column=4, sticky='W', pady=20)

    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class LimiteExcluiGrade():
    def __init__(self, controle, root):
        self.janela=root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='EXCLUIR GRADE', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelAnoCurso = tk.Label(self.frameBody, text='Ano/Curso: ', bg='#76cb69')
        self.inputAnoCurso = tk.Entry(self.frameBody, width=20)
    
        self.buttonExcluir = tk.Button(self.frameBody, text='Excluir Grade')
        self.buttonExcluir.bind('<Button>', controle.exluiHandler)
        self.buttonClear = tk.Button(self.frameBody ,text='Clear')      
        self.buttonClear.bind('<Button>', controle.clearExclusao)  
        self.buttonFecha = tk.Button(self.frameBody ,text='Finalizar')      
        self.buttonFecha.bind('<Button>', controle.fechaExclusao)

        self.labelAnoCurso.grid(row=0, column=0, sticky='W', pady=20)
        self.inputAnoCurso.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonExcluir.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=1, column=4, sticky='W', pady=20)

    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class LimiteAtualizaGrade():
    def __init__(self, controle, root, listaGradeAnoCurso):
        self.janela = root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='ATUALIZAR GRADE', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelAnoCurso = tk.Label(self.frameBody, text='Ano/Curso: ', bg='#76cb69')
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameBody, width=15 , textvariable=self.escolhaCombo)
        self.combobox['values'] = listaGradeAnoCurso
        self.combobox.bind('<<ComboboxSelected>>', controle.popular)

        self.labelDisc = tk.Label(self.frameBody, text='Remover disciplina: ', bg='#76cb69')
        self.listbox = tk.Listbox(self.frameBody)

        self.labelTodasDisc = tk.Label(self.frameBody, text='Adicionar disciplina', bg='#76cb69')
        self.listboxTodas = tk.Listbox(self.frameBody)

        self.buttonRemove = tk.Button(self.frameBody ,text="Remove Disciplina")           
        self.buttonRemove.bind("<Button>", controle.removeDisciplina)
        self.buttonAdiciona = tk.Button(self.frameBody ,text="Adiciona Disciplina")           
        self.buttonAdiciona.bind("<Button>", controle.adicionaDisciplina)
        self.buttonFecha = tk.Button(self.frameBody ,text="Fechar")           
        self.buttonFecha.bind("<Button>", controle.fechaAtualizacao)

        self.labelAnoCurso.grid(row=0, column=0, sticky='W', pady=20)
        self.combobox.grid(row=0, column=1, sticky='W', pady=20)
        self.labelDisc.grid(row=1, column=1, sticky='W')
        self.listbox.grid(row=2, column=1, sticky='W')
        self.labelTodasDisc.grid(row=1, column=2, sticky='W')
        self.listboxTodas.grid(row=2, column=2, sticky='W')
        self.buttonRemove.grid(row=3, column=1, sticky='W', pady=10)
        self.buttonAdiciona.grid(row=3, column=2, sticky='W', pady=10)
        self.buttonFecha.grid(row=3, column=3, sticky='W', pady=10)
    
    def limparListBox(self):
        self.listbox.delete(0, 'end')
        self.listboxTodas.delete(0, 'end')
    
    def IsPopularListbox(self, listaGradeCodDisc):
        for disc in listaGradeCodDisc:
            self.listbox.insert(tk.END, disc)
        return True
    
    def IsPopularListboxTodas(self, listaTodasDisciplinas, listaGradeCodDisc):
        for todas in listaTodasDisciplinas:
            if todas not in listaGradeCodDisc:
                self.listboxTodas.insert(tk.END, todas)
        return True

    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class CtrlGrade():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaDiscGrade = []
        self.listaCodDisc = []
        self.listaGradeCodDisc = []
        self.testePopula = False
        
        if not os.path.isfile("Grade.pickle"):
            self.listaGrade =  []
        else:
            with open("Grade.pickle", "rb") as f:
                self.listaGrade = pickle.load(f)

    #Função para persistencia de dados ---------------------------------------------
    
    def salvaGrades(self):
        if len(self.listaGrade) != 0:
            with open("Grade.pickle","wb") as f:
                pickle.dump(self.listaGrade, f)
    
    #Funções que serão chamadas na Main --- Instaciadores ---------------------------

    def insereGrade(self, root):        
        self.listaDiscGrade = []
        self.listaCodDisc = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisciplinas()
        self.limiteIns = LimiteInsereGrade(self, root, self.listaCodDisc)
    
    def mostraGrade(self):
        string=''
        for grade in self.listaGrade:
            string += '\nGrade: '+grade.getAnoCurso()+'\n'
            for disc in grade.getListaDisc():
                string += disc.getCodigo()+' -- '+disc.getNome()+' -- '+str(disc.getCargaHoraria())+'\n'
            string += '--------------------------\n'
        self.limiteMostra = LimiteMostra(string)

    def consultaGrade(self, root):
        self.limiteConsulta = LimiteConsultaGrade(self, root)
    
    def excluiGrade(self, root):
        self.limiteExclui = LimiteExcluiGrade(self, root)

    def atualizaGrade(self, root):
        #para o combobox
        listaGradeAnoCurso = [] 
        listaGradeAnoCurso =  self.getListaGradeAnoCurso()
        self.limiteAtualiza = LimiteAtualizaGrade(self, root, listaGradeAnoCurso)

    #Funções Auxiliares e de amarrações da classe -------------------------------------------------------------
    
    def mostraConsultaGrade(self, anoCurso):
        string = 'Grade Cadastrada \n'
        for grade in self.listaGrade:
            if grade.getAnoCurso()==anoCurso:
                string += '\nGrade: '+grade.getAnoCurso()+'\n Listas de disciplinas da Grade: \n'
                for disc in grade.getListaDisc():
                    string += disc.getCodigo()+' -- '+disc.getNome()+' -- '+str(disc.getCargaHoraria())+'\n'
        self.limiteMostra = LimiteMostra(string)
    
    def verificaListaGrade(self, AnoCurso):
        for grade in self.listaGrade:
            if grade.getAnoCurso()==AnoCurso:
                return True
        return False
    
    def getListaGradeAnoCurso(self):
        listGradeAnoCurso = []
        for grade in self.listaGrade:
            listGradeAnoCurso.append(grade.getAnoCurso())
        return listGradeAnoCurso
    
    def getGrade(self, AnoCursoGrade):
        gradeRet = None
        for grade in self.listaGrade:
            if grade.getAnoCurso() == AnoCursoGrade:
                gradeRet = grade
        return gradeRet
    
    def getListaGrade(self):
        return self.listaGrade
    
    def getListaGradeCodDisc(self, anoCurso):
        listaGradeCodDisc = []
        for grade in self.listaGrade:
            if anoCurso == grade.getAnoCurso():
                for codDisc in grade.getListaDisc():
                    listaGradeCodDisc.append(codDisc.getCodigo())
                return listaGradeCodDisc
    
    def getDiscGrade(self, anoCurso, codDisc):
        for grade in self.listaGrade:
            if anoCurso == grade.getAnoCurso():
                for disc in grade.getListaDisc():
                    if codDisc == disc.getCodigo():
                        return disc

    #Funções dos Buttons Janela de Inserção de Grade -----------------------------------

    def insereHandler(self, event):
        anoCurso = self.limiteIns.inputAnoCurso.get()
        disciplinaSel = self.limiteIns.listbox.get(tk.ACTIVE)
        disc = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(disciplinaSel)
        try:
            if self.verificaListaGrade(anoCurso) == True:
                raise GradeDuplicada()
            if len(anoCurso)==0 or disc==None:
                raise CamposNaoPreenchidos()
        except GradeDuplicada:
            messagebox.showerror('Error', 'Grade já existe!')
        except CamposNaoPreenchidos:
            messagebox.showerror('Atenção', 'Todos os campos devem ser preenchidos')
        else:
            self.listaDiscGrade.append(disc)
            self.limiteIns.mostraMessagebox('Sucesso', 'Disciplina cadastrada com sucesso')
            self.limiteIns.listbox.delete(tk.ACTIVE)
    
    def criaHandler(self, event):
        anoCurso = self.limiteIns.inputAnoCurso.get()
        grade = Grade(anoCurso, self.listaDiscGrade)
        self.listaGrade.append(grade)
        self.limiteIns.mostraMessagebox('Sucesso', 'Grade criada com sucesso')
        self.limiteIns.janela.destroy()
    
    #Funções dos Buttons Janela de Consulta Grade -----------------------------------
    
    def consultaHandler(self, event):
        anoCurso = self.limiteConsulta.inputAnoCurso.get()
        try:
            if len(anoCurso)==0:
                raise CamposNaoPreenchidos()
            if self.verificaListaGrade(anoCurso) == False:
                raise GradeNaoEncontrada()
        except CamposNaoPreenchidos:
            messagebox.showerror('Atenção', 'Todos os campos devem ser preenchidos')
        except GradeNaoEncontrada:
            messagebox.showerror('Error', 'Ano de Grade não encontrado')
        else:
            self.mostraConsultaGrade(anoCurso)
        finally:
            self.clearConsulta(event)
    
    def clearConsulta(self, event):
        self.limiteConsulta.inputAnoCurso.delete(0, len(self.limiteConsulta.inputAnoCurso.get()))

    def fechaConsulta(self, event):
        self.limiteConsulta.janela.destroy()

    #Funções dos Buttons Janela de Exclui Grade -----------------------------------

    def exluiHandler(self, event):
        anoCurso = self.limiteExclui.inputAnoCurso.get()
        grade = self.getGrade(anoCurso)
        try:
            if len(anoCurso)==0:
                raise CamposNaoPreenchidos()
            if grade == None:
                raise GradeNaoEncontrada()
        except CamposNaoPreenchidos:
            messagebox.showerror('Atenção', 'Todos os campos devem ser preenchidos')
        except GradeNaoEncontrada:
            messagebox.showerror('Error', 'Ano de Grade não encontrado')
        else:
            self.listaGrade.remove(grade)
            self.limiteExclui.mostraMessagebox('Exclusão', 'Grade {} removida com sucesso'.format(anoCurso))
            self.clearExclusao(event)
    
    def clearExclusao(self, event):
        self.limiteExclui.inputAnoCurso.delete(0, 'end')
    
    def fechaExclusao(self, event):
        self.limiteExclui.janela.destroy()

    #Funções dos Buttons Janela de Atualiza Grade -----------------------------------

    def popular(self, event):
        #para os listBox's
        comboAnoCurso = self.limiteAtualiza.escolhaCombo.get()
        self.listaGradeCodDisc = self.getListaGradeCodDisc(comboAnoCurso)
        listaTodasDisciplinas = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisciplinas()
        if self.testePopula == False:
            self.testePopula = self.limiteAtualiza.IsPopularListbox(self.listaGradeCodDisc)
            self.limiteAtualiza.IsPopularListboxTodas(listaTodasDisciplinas ,self.listaGradeCodDisc)
        else:
            self.limiteAtualiza.limparListBox()
            self.limiteAtualiza.IsPopularListbox(self.listaGradeCodDisc)
            self.limiteAtualiza.IsPopularListboxTodas(listaTodasDisciplinas ,self.listaGradeCodDisc)

    def removeDisciplina(self, event):
        comboAnoCurso = self.limiteAtualiza.escolhaCombo.get()
        disciplinaSel = self.limiteAtualiza.listbox.get(tk.ACTIVE)
        disciplina = self.getDiscGrade(comboAnoCurso, disciplinaSel)
        for grade in self.listaGrade:
            if comboAnoCurso == grade.getAnoCurso():
                grade.getListaDisc().remove(disciplina)
        self.limiteAtualiza.mostraMessagebox('Sucesso', 'Disciplina removida com sucesso')
        self.popular(event)
    
    def adicionaDisciplina(self, event):
        comboAnoCurso = self.limiteAtualiza.escolhaCombo.get()
        disciplinaSel = self.limiteAtualiza.listboxTodas.get(tk.ACTIVE)
        disciplina = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(disciplinaSel)
        for grade in self.listaGrade:
            if comboAnoCurso == grade.getAnoCurso():
                grade.getListaDisc().append(disciplina)
        self.limiteAtualiza.mostraMessagebox('Sucesso', 'Disciplina adicionada com sucesso')
        self.popular(event)

    def fechaAtualizacao(self, event):
        self.limiteAtualiza.janela.destroy()