import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class LimiteInsereCurso():
    def __init__(self, controle, root):
        self.janela=root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='CADASTRAR CURSO', font=('Heveltica Bold', 14), bg='#76cb69').pack()
        
        self.labelNomeCurso = tk.Label(self.frameBody,text="Nome do curso: ", bg='#76cb69')
        self.inputNomeCurso = tk.Entry(self.frameBody, width=30)

        self.buttonSubmit = tk.Button(self.frameBody, text='Enter')
        self.buttonSubmit.bind('<Button>', controle.enterHandler)
        self.buttonClear = tk.Button(self.frameBody, text='Clear')
        self.buttonClear.bind('<Button>', self.clearHandler)
        self.buttonFecha = tk.Button(self.frameBody, text='Fechar')
        self.buttonFecha.bind('<Button>', self.fechaHandler)

        self.labelNomeCurso.grid(row=0, column=0, sticky='W', pady=20)    
        self.inputNomeCurso.grid(row=0, column=1, sticky='W', pady=20)         
        self.buttonSubmit.grid(row=1, column=2, sticky='W', pady=20)    
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)    
        self.buttonFecha.grid(row=1, column=4, sticky='W', pady=20)    

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def clearHandler(self, event):
        self.inputNomeCurso.delete(0, 'end')

    def fechaHandler(self, event):
        self.janela.destroy()          

class LimiteMostraCursos():
    def __init__(self, titulo, msg, erro):
        if erro:
            messagebox.showerror(titulo, msg)
        else:
            messagebox.showinfo(titulo, msg)

class LimiteConsultaCursos():
    def __init__(self, controle, root):
        self.janela=root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='CONSULTAR CURSO', font=('Heveltica Bold', 14), bg='#76cb69').pack()
    
        self.labelNome = tk.Label(self.frameBody, text='Curso: ', bg='#76cb69')
        self.inputTextNome = tk.Entry(self.frameBody, width=30)

        self.buttonConsultar = tk.Button(self.frameBody, text='Realizar Consulta')
        self.buttonConsultar.bind('<Button>', controle.consultaHandler)
        self.buttonClear = tk.Button(self.frameBody ,text='Clear')      
        self.buttonClear.bind('<Button>', self.clearConsulta)  
        self.buttonFecha = tk.Button(self.frameBody ,text='Finalizar')      
        self.buttonFecha.bind('<Button>', self.fechaConsulta)

        self.labelNome.grid(row=0, column=0, sticky='W', pady=20)
        self.inputTextNome.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonConsultar.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=1, column=4, sticky='W', pady=20)
    
    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def clearConsulta(self, event):
        self.inputTextNome.delete(0, len(self.inputTextNome.get()))

    def fechaConsulta(self, event):
        self.janela.destroy()

class LimiteExcluiCursos():
    def __init__(self, controle, root):
        self.janela=root    
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='EXCLUIR CURSO', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelNome = tk.Label(self.frameBody, text='Curso: ', bg='#76cb69')
        self.inputTextNome = tk.Entry(self.frameBody, width=20)

        self.buttonConsultar = tk.Button(self.frameBody, text='Excluir curso')
        self.buttonConsultar.bind('<Button>', controle.excluiHandler)
        self.buttonClear = tk.Button(self.frameBody ,text='Clear')      
        self.buttonClear.bind('<Button>', self.clearExclusao)  
        self.buttonFecha = tk.Button(self.frameBody ,text='Finalizar')      
        self.buttonFecha.bind('<Button>', self.fechaExclusao)

        self.labelNome.grid(row=0, column=0, sticky='W', pady=20)
        self.inputTextNome.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonConsultar.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=1, column=4, sticky='W', pady=20)
    
    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)
    
    def clearExclusao(self, event):
        self.inputTextNome.delete(0, 'end')
    
    def fechaExclusao(self, event):
        self.janela.destroy()