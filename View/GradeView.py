from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

class LimiteInsereGrade():
    def __init__(self, controle, root, listaCursos, listaDisc):
        self.janela = root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='CADASTRAR GRADE', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelAnoCurso = tk.Label(self.frameBody, text='Ano/Curso: ', bg='#76cb69')
        self.inputAnoCurso = tk.Entry(self.frameBody, width=20)

        self.labelCurso = tk.Label(self.frameBody, text='Escolha curso: ', bg='#76cb69')
        self.escolhaCurso = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameBody, width=30, textvariable=self.escolhaCurso)
        self.combobox['values'] = listaCursos

        self.labelDisciplina = tk.Label(self.frameBody, text='Escolha disciplinas: ', bg='#76cb69')
        self.listbox = tk.Listbox(self.frameBody)
        for disc in listaDisc:
            self.listbox.insert(tk.END, disc.codigo)

        self.buttonInsere = tk.Button(self.frameBody, text='Insere disciplina')
        self.buttonInsere.bind('<Button>', controle.insereDisciplina)
        self.buttonCria = tk.Button(self.frameBody, text='Cria Grade')
        self.buttonCria.bind('<Button>', controle.criaGrade)
        
        self.labelAnoCurso.grid(row=0, column=0, sticky='W', pady=20)
        self.inputAnoCurso.grid(row=0, column=1, sticky='W', pady=20)
        self.labelCurso.grid(row=1, column=0, sticky='W', pady=20)
        self.combobox.grid(row=1, column=1, sticky='W', pady=20)
        self.labelDisciplina.grid(row=2, column=0, sticky='W', pady=20)
        self.listbox.grid(row=2, column=1, sticky='W', pady=20)
        self.buttonInsere.grid(row=3, column=2, sticky='W', pady=20)
        self.buttonCria.grid(row=3, column=3, sticky='W', pady=20)
    
    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

class LimiteMostraGrades():
    def __init__(self, titulo, msg, erro):
        if erro:
            messagebox.showerror(titulo, msg)
        else:
            messagebox.showinfo(titulo, msg)

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
        self.buttonConsultar.bind('<Button>', controle.gradeConsulta)
        self.buttonClear = tk.Button(self.frameBody ,text='Clear')      
        self.buttonClear.bind('<Button>', self.clearConsulta)  
        self.buttonFecha = tk.Button(self.frameBody ,text='Finalizar')      
        self.buttonFecha.bind('<Button>', self.fechaConsulta)

        self.labelAnoCurso.grid(row=0, column=0, sticky='W', pady=20)
        self.inputAnoCurso.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonConsultar.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=1, column=4, sticky='W', pady=20)

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def clearConsulta(self, event):
        self.inputAnoCurso.delete(0, len(self.inputAnoCurso.get()))

    def fechaConsulta(self, event):
        self.janela.destroy()


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
        self.buttonExcluir.bind('<Button>', controle.gradeDelete)
        self.buttonClear = tk.Button(self.frameBody ,text='Clear')      
        self.buttonClear.bind('<Button>', self.clearExclusao)  
        self.buttonFecha = tk.Button(self.frameBody ,text='Finalizar')      
        self.buttonFecha.bind('<Button>', self.fechaExclusao)

        self.labelAnoCurso.grid(row=0, column=0, sticky='W', pady=20)
        self.inputAnoCurso.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonExcluir.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=1, column=4, sticky='W', pady=20)

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def clearExclusao(self, event):
        self.inputAnoCurso.delete(0, 'end')
    
    def fechaExclusao(self, event):
        self.janela.destroy()

class LimiteAtualizaGrade():
    def __init__(self, controle, root, listaGrade, listaCurso):
        self.janela = root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='ATUALIZAR GRADE', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelGrade = tk.Label(self.frameBody, text='Escolha grade: ', bg='#76cb69')
        self.escolhaGrade = tk.StringVar()
        self.comboboxGrade = ttk.Combobox(self.frameBody, width=30, textvariable=self.escolhaGrade)
        self.comboboxGrade['values'] = listaGrade

        self.labelCurso = tk.Label(self.frameBody, text='Atualizar curso: ', bg='#76cb69')
        self.escolhaCurso = tk.StringVar()
        self.comboboxCurso = ttk.Combobox(self.frameBody, width=30, textvariable=self.escolhaCurso)
        self.comboboxCurso['values'] = listaCurso

        self.buttonAtualizar = tk.Button(self.frameBody, text='Atualizar Grade')
        self.buttonAtualizar.bind('<Button>', controle.atualizarGrade)
        self.buttonClear = tk.Button(self.frameBody, text='Clear')
        self.buttonClear.bind('<Button>', self.clearAtualizar)
        self.buttonFechar = tk.Button(self.frameBody, text='Fechar')
        self.buttonFechar.bind('<Button>', self.fechaAtualizacao)

        self.labelGrade.grid(row=0, column=0, sticky='W', pady=20)
        self.comboboxGrade.grid(row=0, column=1, sticky='W', pady=20)
        self.labelCurso.grid(row=1, column=0, sticky='W', pady=20)
        self.comboboxCurso.grid(row=1, column=1, sticky='W', pady=20)
        self.buttonAtualizar.grid(row=2, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=2, column=3, sticky='W', pady=20)
        self.buttonFechar.grid(row=2, column=4, sticky='W', pady=20)
    
    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def fechaAtualizacao(self, event):
        self.janela.destroy()

    def clearAtualizar(self, event):
        self.comboboxCurso.delete(0, 'end')
        self.comboboxGrade.delete(0, 'end')