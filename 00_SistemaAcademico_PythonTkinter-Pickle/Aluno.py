import tkinter as tk
from tkinter import messagebox
import os.path
import pickle

class AlunoDuplicado(Exception):
    pass

class AlunoNaoCadastrado(Exception):
    pass

class CamposNaoPreenchidos(Exception):
    pass 

class Aluno():
    def __init__(self, nroMatric, nome):
        self.__nroMatric = nroMatric
        self.__nome = nome

    def getNroMatric(self):
        return self.__nroMatric
    
    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome
    
class LimiteInsereAluno():
    def __init__(self, controle, root):
        self.janela = root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='CADASTRAR ALUNO', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelNro = tk.Label(self.frameBody, text="Matrícula: ", bg='#76cb69')
        self.labelNome = tk.Label(self.frameBody, text="Nome: ", bg='#76cb69')

        self.inputNro = tk.Entry(self.frameBody, width=20)
        self.inputNome = tk.Entry(self.frameBody, width=35)             
      
        self.buttonEnter = tk.Button(self.frameBody, text="Enter")      
        self.buttonEnter.bind("<Button>", controle.enterHandler)
        self.buttonClear = tk.Button(self.frameBody, text="Clear")      
        self.buttonClear.bind("<Button>", controle.clearHandler)  
        self.buttonFecha = tk.Button(self.frameBody, text="Concluído")      
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

        self.labelNro.grid(row=0, column=0, sticky='W', pady=20)
        self.inputNro.grid(row=0, column=1, sticky='W', pady=20)
        self.labelNome.grid(row=1, column=0, sticky='W', pady=20)
        self.inputNome.grid(row=1, column=1, sticky='W', pady=20)
        self.buttonEnter.grid(row=2, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=2, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=2, column=4, sticky='W', pady=20)

    def mostraMessagebox(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraAlunos():
    def __init__(self, str):
        messagebox.showinfo('Lista de alunos', str)

class LimiteConsultaAluno():
    def __init__(self, controle, root):
        self.janela=root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='CONSULTAR ALUNO', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelMatricula = tk.Label(self.frameBody, text='Matricula: ', bg='#76cb69')
        self.inputTextMatricula = tk.Entry(self.frameBody, width=30)

        self.buttonConsultar = tk.Button(self.frameBody, text='Realizar Consulta')
        self.buttonConsultar.bind('<Button>', controle.consultaAluno)
        self.buttonClear = tk.Button(self.frameBody, text='Clear')      
        self.buttonClear.bind('<Button>', controle.clearAluno)  
        self.buttonFecha = tk.Button(self.frameBody, text='Finalizar')      
        self.buttonFecha.bind('<Button>', controle.fechaAluno)

        self.labelMatricula.grid(row=0, column=0, sticky='W', pady=20)
        self.inputTextMatricula.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonConsultar.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=1, column=4, sticky='W', pady=20)

    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class LimiteExcluiAluno():
    def __init__(self, controle, root):
        self.janela=root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='EXCLUIR ALUNO', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelMatric = tk.Label(self.frameBody, text='Matricula: ', bg='#76cb69')
        self.inputMatric = tk.Entry(self.frameBody, width=30)

        self.buttonDelete = tk.Button(self.frameBody, text='Deletar')        
        self.buttonDelete.bind('<Button>', controle.alunoDelete)
        self.buttonClear = tk.Button(self.frameBody, text='Clear')      
        self.buttonClear.bind('<Button>', controle.clearAlunoDelete)  
        self.buttonFecha = tk.Button(self.frameBody, text='Fechar')      
        self.buttonFecha.bind('<Button>', controle.fechaAlunoDelete)

        self.labelMatric.grid(row=0, column=0, sticky='W', pady=20)
        self.inputMatric.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonDelete.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=1, column=4, sticky='W', pady=20)
    
    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class LimiteAtualizaAluno():
    def __init__(self, controle, root):
        self.janela=root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameTitulo.configure(bg='#76cb69')
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='ATUALIZAR ALUNO', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelMatric = tk.Label(self.frameBody, text='Matrícula: ', bg='#76cb69')
        self.labelNome = tk.Label(self.frameBody, text='Atualizar nome: ', bg='#76cb69')        
        self.inputMatric = tk.Entry(self.frameBody, width=20)
        self.inputNome = tk.Entry(self.frameBody, width=35)
        
        self.buttonAtualizar = tk.Button(self.frameBody, text='Atualizar Aluno')
        self.buttonAtualizar.bind('<Button>', controle.atualizarAluno)
        self.buttonClear = tk.Button(self.frameBody, text='Clear')
        self.buttonClear.bind('<Button>', controle.atualizarClearAluno)
        self.buttonFechar = tk.Button(self.frameBody, text='Fechar')
        self.buttonFechar.bind('<Button>', controle.atualizarFecharAluno)

        self.labelMatric.grid(row=0, column=0, sticky='W', pady=20)        
        self.inputMatric.grid(row=0, column=1, sticky='W', pady=20)        
        self.labelNome.grid(row=1, column=0, sticky='W', pady=20)        
        self.inputNome.grid(row=1, column=1, sticky='W', pady=20)        
        self.buttonAtualizar.grid(row=2, column=3, sticky='W', pady=20)             
        self.buttonClear.grid(row=2, column=4, sticky='W', pady=20)             
        self.buttonFechar.grid(row=2, column=5, sticky='W', pady=20)             

    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class CtrlAluno():       
    def __init__(self):
        if not os.path.isfile("Aluno.pickle"):
            self.listaAlunos = []
        else:
            with open("Aluno.pickle", "rb") as f:
                self.listaAlunos = pickle.load(f)

    #Função para persistencia de dados ---------------------------------------------
    
    def salvaAlunos(self):
        if len(self.listaAlunos) != 0:
            with open("Aluno.pickle","wb") as f:
                pickle.dump(self.listaAlunos, f)

    #Funções auxiliares e de amarrações da classe ---------------------------------------------
    
    def getAluno(self, nroMatric):
        alunoRet = None
        for aluno in self.listaAlunos:
            if aluno.getNroMatric() == nroMatric:
                alunoRet = aluno
        return alunoRet
    
    def getListaNroMatric(self):
        listNroMatric = []
        for matric in self.listaAlunos:
            listNroMatric.append(matric.getNroMatric())
        return listNroMatric
    
    def getAtualizaAluno(self, nroMatric, nome):
        for aluno in self.listaAlunos:
            if nroMatric == aluno.getNroMatric():
                aluno.setNome(nome)

    #Funções que serão chamadas na Main --- Instaciadores ---------------------------

    def insereAlunos(self, root):
        self.limiteIns = LimiteInsereAluno(self, root) 

    def mostraAlunos(self):
        str = 'Nro Matric. -- Nome\n'
        for aluno in self.listaAlunos:
            str += aluno.getNroMatric() + ' -- ' + aluno.getNome() +'\n'       
        self.limiteLista = LimiteMostraAlunos(str)
    
    def consultaAlunos(self, root):
        self.limiteConsulta = LimiteConsultaAluno(self, root)

    def excluiAlunos(self, root):
        self.limiteExclui = LimiteExcluiAluno(self, root)
    
    def atualizaAlunos(self, root):
        self.limiteAtualiza = LimiteAtualizaAluno(self, root)

    #Funções dos Buttons Janela de Inserção de Aluno -----------------------------------

    def enterHandler(self, event):
        nroMatric = self.limiteIns.inputNro.get()
        nome = self.limiteIns.inputNome.get()
        aluno = self.getAluno(nroMatric)
        try:
            if aluno != None:
                raise AlunoDuplicado()
            if len(nroMatric)==0 or len(nome)==0:
                raise CamposNaoPreenchidos()
        except AlunoDuplicado:
            messagebox.showerror('Alerta', 'A matrícula desse aluno já existe')
        except CamposNaoPreenchidos:
            messagebox.showerror('Atenção', 'Todos os campos devem ser preenchidos')
        else:
            aluno = Aluno(nroMatric, nome)
            self.listaAlunos.append(aluno)
            self.limiteIns.mostraMessagebox('Sucesso', 'Aluno cadastrado com sucesso')
            self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNro.delete(0, len(self.limiteIns.inputNro.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.janela.destroy()
    
    #Funções dos Buttons Janela de Consulta do Aluno ----------------------------------------------

    def consultaAluno(self, event):
        nroMatric = self.limiteConsulta.inputTextMatricula.get()
        aluno = self.getAluno(nroMatric)
        try:
            if len(nroMatric)==0:
                raise CamposNaoPreenchidos()
            if aluno == None:
                raise AlunoNaoCadastrado()
        except CamposNaoPreenchidos:
            messagebox.showerror('Atenção', 'Todos os campos devem ser preenchidos')
        except AlunoNaoCadastrado:
            messagebox.showerror('Alerta', 'Aluno não cadastrado')
        else:
            str = 'Aluno cadastrado \nMatrícula -- Nome\n'+aluno.getNroMatric()+' -- '+aluno.getNome()
            LimiteMostraAlunos(str)
        finally:
            self.clearAluno(event)
    
    def clearAluno(self, event):
         self.limiteConsulta.inputTextMatricula.delete(0, len(self.limiteConsulta.inputTextMatricula.get()))
    
    def fechaAluno(self, event):
        self.limiteConsulta.janela.destroy()

    #Funções dos Buttons Janela de Exluir Aluno ----------------------------------------------

    def alunoDelete(self, event):
        nroMatric = self.limiteExclui.inputMatric.get()
        aluno = self.getAluno(nroMatric)
        try:
            if len(nroMatric) == 0:
                raise CamposNaoPreenchidos()
            elif aluno == None:
                raise AlunoNaoCadastrado()
        except CamposNaoPreenchidos:
            messagebox.showerror('Atenção', 'Todos os campos devem ser preenchidos')
        except AlunoNaoCadastrado:
            messagebox.showerror('Alerta', 'Aluno não cadastrado')
        else: 
            self.listaAlunos.remove(aluno)
            self.limiteExclui.mostraMessagebox('Sucesso', 'Aluno excluído com sucesso')
            self.clearAlunoDelete(event)
    
    def clearAlunoDelete(self, event):
        self.limiteExclui.inputMatric.delete(0, len(self.limiteExclui.inputMatric.get()))
    
    def fechaAlunoDelete(self, event):
        self.limiteExclui.janela.destroy()

    #Funções dos Buttons Janela de Atualizar Aluno ----------------------------------------------

    def atualizarAluno(self, event):
        nroMatric = self.limiteAtualiza.inputMatric.get()
        nome = self.limiteAtualiza.inputNome.get()
        aluno = self.getAluno(nroMatric)
        try:
            if len(nroMatric) == 0 or len(nome) == 0:
                raise CamposNaoPreenchidos()
            elif aluno == None:
                raise AlunoNaoCadastrado()
        except CamposNaoPreenchidos:
            messagebox.showerror('Atenção', 'Todos os campos devem ser preenchidos')
        except AlunoNaoCadastrado:
            messagebox.showerror('Alerta', 'Aluno não cadastrado')
        else: 
            self.getAtualizaAluno(nroMatric, nome)
            self.limiteAtualiza.mostraMessagebox('Atualização', 'Nome de aluno atualizado com sucesso')
            self.atualizarClearAluno(event)
    
    def atualizarClearAluno(self, event):
        self.limiteAtualiza.inputMatric.delete(0, len(self.limiteAtualiza.inputMatric.get()))
        self.limiteAtualiza.inputNome.delete(0, len(self.limiteAtualiza.inputNome.get()))
    
    def atualizarFecharAluno(self, event):
        self.limiteAtualiza.janela.destroy() 