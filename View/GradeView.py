from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

class LimiteInsereGrade():
    def __init__(self, controle, root):
        self.janela = root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='CADASTRAR GRADE', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelAnoCurso = tk.Label(self.frameBody, text='Ano/Curso: ', bg='#76cb69')
        self.inputAnoCurso = tk.Entry(self.frameBody, width=20)

        self.buttonEnter = tk.Button(self.frameBody, text='Enter')
        self.buttonEnter.bind('<Button>', controle.enterHandler)
        self.buttonClear = tk.Button(self.frameBody, text='Clear')
        self.buttonClear.bind('<Button>', self.clearHandler)
        self.buttonFecha = tk.Button(self.frameBody, text='Fechar')
        self.buttonFecha.bind('<Button>', self.fechaHandler)

        self.labelAnoCurso.grid(row=0, column=0, sticky='W', pady=20)
        self.inputAnoCurso.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonEnter.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=1, column=4, sticky='W', pady=20)
    
    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def clearHandler(self, event):
        self.inputAnoCurso.delete(0, 'end')
    
    def fechaHandler(self, event):
        self.janela.destroy()

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
        self.buttonFecha.bind("<Button>", self.fechaAtualizacao)

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
    
    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def fechaAtualizacao(self, event):
        self.janela.destroy()