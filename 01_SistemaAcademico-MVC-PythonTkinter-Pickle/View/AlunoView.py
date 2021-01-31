import tkinter as tk
from tkinter import messagebox

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
        self.buttonClear.bind("<Button>", self.clearHandler)  
        self.buttonFecha = tk.Button(self.frameBody, text="Concluído")      
        self.buttonFecha.bind("<Button>", self.fechaHandler)

        self.labelNro.grid(row=0, column=0, sticky='W', pady=20)
        self.inputNro.grid(row=0, column=1, sticky='W', pady=20)
        self.labelNome.grid(row=1, column=0, sticky='W', pady=20)
        self.inputNome.grid(row=1, column=1, sticky='W', pady=20)
        self.buttonEnter.grid(row=2, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=2, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=2, column=4, sticky='W', pady=20)

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)
    
    def clearHandler(self, event):
        self.inputNro.delete(0, len(self.inputNro.get()))
        self.inputNome.delete(0, len(self.inputNome.get()))

    def fechaHandler(self, event):
        self.janela.destroy()

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
        self.buttonClear.bind('<Button>', self.clearAluno)  
        self.buttonFecha = tk.Button(self.frameBody, text='Finalizar')      
        self.buttonFecha.bind('<Button>', self.fechaAluno)

        self.labelMatricula.grid(row=0, column=0, sticky='W', pady=20)
        self.inputTextMatricula.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonConsultar.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=1, column=4, sticky='W', pady=20)

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def clearAluno(self, event):
         self.inputTextMatricula.delete(0, len(self.inputTextMatricula.get()))
    
    def fechaAluno(self, event):
        self.janela.destroy()

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
        self.buttonClear.bind('<Button>', self.clearAlunoDelete)  
        self.buttonFecha = tk.Button(self.frameBody, text='Fechar')      
        self.buttonFecha.bind('<Button>', self.fechaAlunoDelete)

        self.labelMatric.grid(row=0, column=0, sticky='W', pady=20)
        self.inputMatric.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonDelete.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=1, column=4, sticky='W', pady=20)
    
    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def clearAlunoDelete(self, event):
        self.inputMatric.delete(0, len(self.inputMatric.get()))
    
    def fechaAlunoDelete(self, event):
        self.janela.destroy()

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
        self.buttonClear.bind('<Button>', self.atualizarClearAluno)
        self.buttonFechar = tk.Button(self.frameBody, text='Fechar')
        self.buttonFechar.bind('<Button>', self.atualizarFecharAluno)

        self.labelMatric.grid(row=0, column=0, sticky='W', pady=20)        
        self.inputMatric.grid(row=0, column=1, sticky='W', pady=20)        
        self.labelNome.grid(row=1, column=0, sticky='W', pady=20)        
        self.inputNome.grid(row=1, column=1, sticky='W', pady=20)        
        self.buttonAtualizar.grid(row=2, column=3, sticky='W', pady=20)             
        self.buttonClear.grid(row=2, column=4, sticky='W', pady=20)             
        self.buttonFechar.grid(row=2, column=5, sticky='W', pady=20)             

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)
    
    def atualizarClearAluno(self, event):
        self.inputMatric.delete(0, len(self.inputMatric.get()))
        self.inputNome.delete(0, len(self.inputNome.get()))
    
    def atualizarFecharAluno(self, event):
        self.janela.destroy() 