import tkinter as tk
from tkinter import messagebox
import os.path
import pickle

class DisciplinaNaoCadastrada(Exception):
    pass

class DisciplinaDuplicada(Exception):
    pass

class CamposNaoPreenchidos(Exception):
    pass

class Disciplina:
    def __init__(self, codigo, nome, cargaHoraria):
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria
        self.__notaAluno = None
    
    def getCodigo(self):
        return self.__codigo
    
    def getNome(self):
        return self.__nome
    
    def getCargaHoraria(self):
        return self.__cargaHoraria

    def setNome(self, nome):
        self.__nome = nome 

    def setCargaHoraria(self, cargaHoraria):
        self.__cargaHoraria = cargaHoraria    

class LimiteInsereDisciplinas():
    def __init__(self, controle, root):
        self.janela = root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='CADASTRAR DISCIPLINA', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelCodigo = tk.Label(self.frameBody, text="Código: ", bg='#76cb69')
        self.labelNome = tk.Label(self.frameBody, text="Nome: ", bg='#76cb69')
        self.labelCargaHoraria = tk.Label(self.frameBody, text='Carga Horária: ', bg='#76cb69')
        
        self.inputCodigo = tk.Entry(self.frameBody, width=20)
        self.inputNome = tk.Entry(self.frameBody, width=35)
        self.inputCargaHoraria = tk.Entry(self.frameBody, width=5)
        
        self.buttonSubmit = tk.Button(self.frameBody, text="Enter")      
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
        self.buttonClear = tk.Button(self.frameBody ,text="Clear")      
        self.buttonClear.bind("<Button>", controle.clearHandler)  
        self.buttonFecha = tk.Button(self.frameBody ,text="Concluído")      
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

        self.labelCodigo.grid(row=0, column=0, sticky='W', pady=20)
        self.inputCodigo.grid(row=0, column=1, sticky='W', pady=20)
        self.labelNome.grid(row=1, column=0, sticky='W', pady=20)
        self.inputNome.grid(row=1, column=1, sticky='W', pady=20)
        self.labelCargaHoraria.grid(row=2, column=0, sticky='W', pady=20)
        self.inputCargaHoraria.grid(row=2, column=1, sticky='W', pady=20)
        self.buttonSubmit.grid(row=3, column=3, sticky='W', pady=20)
        self.buttonClear.grid(row=3, column=4, sticky='W', pady=20)
        self.buttonFecha.grid(row=3, column=5, sticky='W', pady=20)

    def mostraMessagebox(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraDisciplinas():
    def __init__(self, string):
        messagebox.showinfo('Lista de disciplinas', string)

class LimiteConsultaDisciplina():
    def __init__(self, controle, root):
        self.janela=root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='CONSULTAR DISCIPLINA', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelCodigo = tk.Label(self.frameBody, text='Codigo: ', bg='#76cb69')
        self.inputTextCodigo = tk.Entry(self.frameBody, width=30)
    
        self.buttonConsultar = tk.Button(self.frameBody, text='Realizar Consulta')
        self.buttonConsultar.bind('<Button>', controle.consultaHandler)
        self.buttonClear = tk.Button(self.frameBody ,text='Clear')      
        self.buttonClear.bind('<Button>', controle.clearConsulta)  
        self.buttonFecha = tk.Button(self.frameBody ,text='Finalizar')      
        self.buttonFecha.bind('<Button>', controle.fechaConsulta)

        self.labelCodigo.grid(row=0, column=0, sticky='W', pady=20)
        self.inputTextCodigo.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonConsultar.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=1, column=4, sticky='W', pady=20)
    
    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class LimiteExcluiDisciplina():
    def __init__(self, controle, root):
        self.janela=root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='EXCLUIR DISCIPLINA', font=('Heveltica Bold', 14), bg='#76cb69').pack()
        
        self.labelCodigo = tk.Label(self.frameBody, text='Codigo: ', bg='#76cb69')
        self.inputTextCodigo = tk.Entry(self.frameBody, width=30)

        self.buttonExcluir = tk.Button(self.frameBody, text='Excluir')
        self.buttonExcluir.bind('<Button>', controle.excluirDisciplina)
        self.buttonClear = tk.Button(self.frameBody ,text='Clear')      
        self.buttonClear.bind('<Button>', controle.clearExclusao)  
        self.buttonFecha = tk.Button(self.frameBody ,text='Finalizar')      
        self.buttonFecha.bind('<Button>', controle.fechaExclusao)

        self.labelCodigo.grid(row=0, column=0, sticky='W', pady=20)
        self.inputTextCodigo.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonExcluir.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=1, column=4, sticky='W', pady=20)
    
    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class LimiteAtualizaDisciplina():
    def __init__(self, controle, root):
        self.janela = root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='ATUALIZAR DISCIPLINA', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelMensagem = tk.Label(self.frameBody, text='Preencher o campo ou os campos que serão atualizados\n', bg='#76cb69')
        self.labelCodigo = tk.Label(self.frameBody, text="Código: ", bg='#76cb69')
        self.labelNome = tk.Label(self.frameBody, text="Atualizar Nome: ", bg='#76cb69')
        self.labelCargaHoraria = tk.Label(self.frameBody, text='Atualizar Carga Horária: ', bg='#76cb69')
        
        self.inputCodigo = tk.Entry(self.frameBody, width=20)
        self.inputNome = tk.Entry(self.frameBody, width=35)
        self.inputCargaHoraria = tk.Entry(self.frameBody, width=5)
        
        self.buttonSubmit = tk.Button(self.frameBody, text="Enter")      
        self.buttonSubmit.bind("<Button>", controle.atualizaDisciplina)
        self.buttonClear = tk.Button(self.frameBody ,text="Clear")      
        self.buttonClear.bind("<Button>", controle.clearAtualiza)  
        self.buttonFecha = tk.Button(self.frameBody ,text="Concluído")      
        self.buttonFecha.bind("<Button>", controle.fechaAtualiza)

        self.labelMensagem.grid(columnspan=5, pady=15)
        self.labelCodigo.grid(row=1, column=0, sticky='W', pady=20)
        self.inputCodigo.grid(row=1, column=1, sticky='W', pady=20)
        self.labelNome.grid(row=2, column=0, sticky='W', pady=20)
        self.inputNome.grid(row=2, column=1, sticky='W', pady=20)
        self.labelCargaHoraria.grid(row=3, column=0, sticky='W', pady=20)
        self.inputCargaHoraria.grid(row=3, column=1, sticky='W', pady=20)
        self.buttonSubmit.grid(row=4, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=4, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=4, column=4, sticky='W', pady=20)

    def mostraMessagebox(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlDisciplina():       
    def __init__(self):
        if not os.path.isfile("Disciplina.pickle"):
            self.listaDisciplinas =  []
        else:
            with open("Disciplina.pickle", "rb") as f:
                self.listaDisciplinas = pickle.load(f)

    #Função para persistencia de dados ---------------------------------------------
    
    def salvaDisciplinas(self):
        if len(self.listaDisciplinas) != 0:
            with open("Disciplina.pickle","wb") as f:
                pickle.dump(self.listaDisciplinas, f)

    #Funções auxiliares e de amarrações da classe ---------------------------------------------

    def getDisciplina(self, codDisc):
        discRet = None
        for disc in self.listaDisciplinas:
            if disc.getCodigo() == codDisc:
                discRet = disc
        return discRet

    def getListaCodDisciplinas(self):
        listaCod = []
        for disc in self.listaDisciplinas:
            listaCod.append(disc.getCodigo())
        return listaCod

    def getAtualizaDisciplina(self, codDisc, nomeOuCh, string):
        for disc in self.listaDisciplinas:
            if codDisc==disc.getCodigo(): 
                if string=='ch':
                    disc.setCargaHoraria(nomeOuCh)
                else:
                    disc.setNome(nomeOuCh)
            
    #Funções que serão chamadas na Main --- Instaciadores ---------------------------

    def insereDisciplinas(self, root):
        self.limiteIns = LimiteInsereDisciplinas(self, root) 

    def mostraDisciplinas(self):
        string = 'Código -- Nome -- Carga Horária\n'
        for disc in self.listaDisciplinas:
            string += disc.getCodigo()+' -- '+disc.getNome()+' -- '+str(disc.getCargaHoraria())+'\n'
        self.limiteLista = LimiteMostraDisciplinas(string)
    
    def consultaDisciplinas(self, root):
        self.limiteConsulta = LimiteConsultaDisciplina(self, root)

    def excluiDisciplinas(self, root):
        self.limiteExclui = LimiteExcluiDisciplina(self, root)
    
    def atualizaDisciplinas(self, root):
        self.limiteAtualiza = LimiteAtualizaDisciplina(self, root)

    #Funções dos Buttons Janela de Inserção de Disciplina -----------------------------------

    def enterHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        nome = self.limiteIns.inputNome.get()
        ch = self.limiteIns.inputCargaHoraria.get()
        disc = self.getDisciplina(codigo)
        try:
            if disc != None:
                raise DisciplinaDuplicada()
            if len(codigo)==0 or len(nome)==0 or len(ch)==0:
                raise CamposNaoPreenchidos()
        except DisciplinaDuplicada:
            messagebox.showerror('Alerta', 'Disciplina já cadastrada!')
        except CamposNaoPreenchidos:
            messagebox.showerror('Atenção', 'Todos os campos devem ser preenchidos')
        else:
            self.listaDisciplinas.append(Disciplina(codigo, nome, ch))
            self.limiteIns.mostraMessagebox('Sucesso', 'Disciplina cadastrada com sucesso')
            self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputCargaHoraria.delete(0, len(self.limiteIns.inputCargaHoraria.get()))

    def fechaHandler(self, event):
        self.limiteIns.janela.destroy()

    #Funções dos Buttons Janela de Consulta de Disciplina ----------------------------------------------
    
    def consultaHandler(self, event):
        codigo = self.limiteConsulta.inputTextCodigo.get()
        disc = self.getDisciplina(codigo)
        try:
            if len(codigo)==0:
                raise CamposNaoPreenchidos()
            if disc == None:
                raise DisciplinaNaoCadastrada() 
        except CamposNaoPreenchidos:
            messagebox.showerror('Atenção', 'Todos os campos devem ser preenchidos')
        except DisciplinaNaoCadastrada:
            messagebox.showerror('Alerta', 'Disciplina não cadastrada')
        else:
            string = 'Disciplina cadastrada \nCódigo -- Nome -- Carga Horária \n'+codigo+' -- '+disc.getNome()+' -- '+str(disc.getCargaHoraria())
            LimiteMostraDisciplinas(string)
        finally:
            self.clearConsulta(event)
    
    def clearConsulta(self, event):
        self.limiteConsulta.inputTextCodigo.delete(0, len(self.limiteConsulta.inputTextCodigo.get()))
    
    def fechaConsulta(self, event):
        self.limiteConsulta.janela.destroy()

    #Funções dos Buttons Janela de Exclui de Disciplina ----------------------------------------------

    def excluirDisciplina(self, event):
        codigo = self.limiteExclui.inputTextCodigo.get()
        disc = self.getDisciplina(codigo)
        try:
            if len(codigo)==0:
                raise CamposNaoPreenchidos()
            if disc == None:
                raise DisciplinaNaoCadastrada() 
        except CamposNaoPreenchidos:
            messagebox.showerror('Atenção', 'Todos os campos devem ser preenchidos')
        except DisciplinaNaoCadastrada:
            messagebox.showerror('Alerta', 'Disciplina não cadastrada')
        else:
            self.listaDisciplinas.remove(disc)
            self.limiteExclui.mostraMessagebox('Exclusão', 'Disciplina {} excluida com sucesso'.format(codigo))
            self.clearExclusao(event)

    def clearExclusao(self, event):
        self.limiteExclui.inputTextCodigo.delete(0, 'end')

    def fechaExclusao(self, event):
        self.limiteExclui.janela.destroy()

    #Funções dos Buttons Janela de Atualiza de Disciplina ----------------------------------------------

    def atualizaDisciplina(self, event):
        codDisc = self.limiteAtualiza.inputCodigo.get()
        nome = self.limiteAtualiza.inputNome.get()
        ch = self.limiteAtualiza.inputCargaHoraria.get()
        disc = self.getDisciplina(codDisc)
        try:
            if len(codDisc)==0 or (len(nome)==0 and len(ch)==0):
                raise CamposNaoPreenchidos()
            if disc == None:
                raise DisciplinaNaoCadastrada() 
        except CamposNaoPreenchidos:
            messagebox.showerror('Atenção', 'Junto ao código, pelo menos um campo(Nome ou Carga Horária) deve ser preenchido')
        except DisciplinaNaoCadastrada:
            messagebox.showerror('Alerta', 'Disciplina não cadastrada')
        else:
            if len(nome) == 0:
                self.getAtualizaDisciplina(codDisc, ch, 'ch')
            else:
                self.getAtualizaDisciplina(codDisc, nome, 'nome')
            self.limiteAtualiza.mostraMessagebox('Sucesso', 'Disciplina {} atualizada com sucesso'.format(codDisc))
            self.clearAtualiza(event)        
    
    def clearAtualiza(self, event):
        self.limiteAtualiza.inputCodigo.delete(0, 'end')
        self.limiteAtualiza.inputNome.delete(0, 'end')
        self.limiteAtualiza.inputCargaHoraria.delete(0, 'end')
    
    def fechaAtualiza(self, event):
        self.limiteAtualiza.janela.destroy()