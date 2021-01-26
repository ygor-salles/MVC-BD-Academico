import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

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

        self.valor = tk.IntVar()
        self.radio1 = tk.Radiobutton(self.frameBody, text='1', variable=self.valor, value=1, bg='#76cb69')
        self.radio2 = tk.Radiobutton(self.frameBody, text='2', variable=self.valor, value=2, bg='#76cb69')

        self.inputAno = tk.Entry(self.frameBody, width=10)
        
        self.listboxDisciplina = tk.Listbox(self.frameBody)
        for disc in listaDisc:
            self.listboxDisciplina.insert(tk.END, disc)

        self.inputNota = tk.Entry(self.frameBody, width=10)

        self.buttonInsere = tk.Button(self.frameBody, text='Insere Disciplina no Histórico')
        self.buttonInsere.bind('<Button>', controle.insereDisciplina)
        self.buttonCria = tk.Button(self.frameBody, text='Criar Semestre')
        self.buttonCria.bind('<Button>', controle.criaSemestre)

        self.labelAluno.grid(row=0, column=0, sticky='W', pady=5)
        self.comboboxAluno.grid(row=0, column=1, sticky='W', pady=5)
        self.labelSemestre.grid(row=1, column=0, sticky='W', pady=5)
        self.radio1.grid(row=1, column=1, sticky='W', pady=5)
        self.radio2.grid(row=1, column=2, sticky='W', pady=5)
        self.labelAno.grid(row=2, column=0, sticky='W', pady=5)
        self.inputAno.grid(row=2, column=1, sticky='W')
        self.labelListaDisc.grid(row=3, column=1, sticky='W')
        self.listboxDisciplina.grid(row=4, column=1, sticky='W', pady=5)
        self.labelNota.grid(row=5, column=0, sticky='W', pady=5)
        self.inputNota.grid(row=5, column=1, sticky='W', pady=5)
        self.buttonInsere.grid(row=6, column=2, sticky='W', pady=5)
        self.buttonCria.grid(row=6, column=3, sticky='W', pady=5)

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

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
        self.buttonClear.bind('<Button>', self.clearConsulta)
        self.buttonFinaliza = tk.Button(self.frameBody, text='Finalizar')
        self.buttonFinaliza.bind('<Button>', self.finalizaConsulta)

        self.labelMatricAluno.grid(row=0, column=0, sticky='W', pady=20)
        self.inputMatricAluno.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonConsulta.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFinaliza.grid(row=1, column=4, sticky='W', pady=20)

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def clearConsulta(self, event):
        self.inputMatricAluno.delete(0, len(self.inputMatricAluno.get()))
    
    def finalizaConsulta(self, event):
        self.janela.destroy()

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
        self.buttonClear.bind('<Button>', self.clearExclusao)
        self.buttonFinaliza = tk.Button(self.frameBody, text='Finalizar')
        self.buttonFinaliza.bind('<Button>', self.finalizaExclusao)

        self.labelMatricAluno.grid(row=0, column=0, sticky='W', pady=20)
        self.inputMatricAluno.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonConsulta.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFinaliza.grid(row=1, column=4, sticky='W', pady=20)

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def clearExclusao(self, event):
        self.inputMatricAluno.delete(0, 'end')
    
    def finalizaExclusao(self, event):
        self.janela.destroy()