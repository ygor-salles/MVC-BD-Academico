import tkinter as tk
from tkinter import messagebox

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
        self.buttonClear.bind("<Button>", self.clearHandler)  
        self.buttonFecha = tk.Button(self.frameBody ,text="Concluído")      
        self.buttonFecha.bind("<Button>", self.fechaHandler)

        self.labelCodigo.grid(row=0, column=0, sticky='W', pady=20)
        self.inputCodigo.grid(row=0, column=1, sticky='W', pady=20)
        self.labelNome.grid(row=1, column=0, sticky='W', pady=20)
        self.inputNome.grid(row=1, column=1, sticky='W', pady=20)
        self.labelCargaHoraria.grid(row=2, column=0, sticky='W', pady=20)
        self.inputCargaHoraria.grid(row=2, column=1, sticky='W', pady=20)
        self.buttonSubmit.grid(row=3, column=3, sticky='W', pady=20)
        self.buttonClear.grid(row=3, column=4, sticky='W', pady=20)
        self.buttonFecha.grid(row=3, column=5, sticky='W', pady=20)

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def clearHandler(self, event):
        self.inputCodigo.delete(0, len(self.inputCodigo.get()))
        self.inputNome.delete(0, len(self.inputNome.get()))
        self.inputCargaHoraria.delete(0, len(self.inputCargaHoraria.get()))

    def fechaHandler(self, event):
        self.janela.destroy()

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
        self.buttonClear.bind('<Button>', self.clearConsulta)  
        self.buttonFecha = tk.Button(self.frameBody ,text='Finalizar')      
        self.buttonFecha.bind('<Button>', self.fechaConsulta)

        self.labelCodigo.grid(row=0, column=0, sticky='W', pady=20)
        self.inputTextCodigo.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonConsultar.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=1, column=4, sticky='W', pady=20)
    
    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def clearConsulta(self, event):
        self.inputTextCodigo.delete(0, len(self.inputTextCodigo.get()))
    
    def fechaConsulta(self, event):
        self.janela.destroy()


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
        self.buttonClear.bind('<Button>', self.clearExclusao)  
        self.buttonFecha = tk.Button(self.frameBody ,text='Finalizar')      
        self.buttonFecha.bind('<Button>', self.fechaExclusao)

        self.labelCodigo.grid(row=0, column=0, sticky='W', pady=20)
        self.inputTextCodigo.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonExcluir.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=1, column=4, sticky='W', pady=20)
    
    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def clearExclusao(self, event):
        self.inputTextCodigo.delete(0, 'end')

    def fechaExclusao(self, event):
        self.janela.destroy()

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
        self.buttonClear.bind("<Button>", self.clearAtualiza)  
        self.buttonFecha = tk.Button(self.frameBody ,text="Concluído")      
        self.buttonFecha.bind("<Button>", self.fechaAtualiza)

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

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def clearAtualiza(self, event):
        self.inputCodigo.delete(0, 'end')
        self.inputNome.delete(0, 'end')
        self.inputCargaHoraria.delete(0, 'end')
    
    def fechaAtualiza(self, event):
        self.janela.destroy()