from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

class LimiteInsereGrade():
    def __init__(self, controle, root, listaCursos, listaCodDisc):
        self.janela = root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='CADASTRAR GRADE', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelAno = tk.Label(self.frameBody, text='Ano: ', bg='#76cb69')
        self.inputAno = tk.Entry(self.frameBody, width=10)

        self.labelCurso = tk.Label(self.frameBody, text='Escolha curso: ', bg='#76cb69')
        self.escolhaCurso = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameBody, width=30, textvariable=self.escolhaCurso)
        self.combobox['values'] = listaCursos

        self.labelDisciplina = tk.Label(self.frameBody, text='Escolha disciplinas: ', bg='#76cb69')
        self.listbox = tk.Listbox(self.frameBody)
        for disc in listaCodDisc:
            self.listbox.insert(tk.END, disc)

        self.buttonInsere = tk.Button(self.frameBody, text='Insere disciplina')
        self.buttonInsere.bind('<Button>', controle.insereDisciplina)
        self.buttonCria = tk.Button(self.frameBody, text='Cria Grade')
        self.buttonCria.bind('<Button>', controle.criaGrade)
        
        self.labelAno.grid(row=0, column=0, sticky='W', pady=20)
        self.inputAno.grid(row=0, column=1, sticky='W', pady=20)
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

class LimiteTabelaGrades():
    def __init__(self, root, listaGrades):
        self.janela = root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='RELATÓRIO DE GRADES', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.listaDisc = ttk.Treeview(self.frameBody, column=('ano', 'curso_id'), show='headings')
        self.listaDisc.column('ano', minwidth=0, width=100)
        self.listaDisc.column('curso_id', minwidth=0, width=250)
        self.listaDisc.heading('ano', text='ANO')
        self.listaDisc.heading('curso_id', text='CURSO')
        self.listaDisc.pack(pady=30)

        for grade in listaGrades:
            self.listaDisc.insert('', 'end', values=(grade.ano, grade.curso_id))

class LimiteConsultaGrade():
    def __init__(self, controle, root, listaCursos, listaAno):
        self.janela=root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='CONSULTAR GRADE', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelAno = tk.Label(self.frameBody, text='Ano: ', bg='#76cb69')
        self.escolhaAno = tk.StringVar()
        self.comboboxAno = ttk.Combobox(self.frameBody, width=10, textvariable=self.escolhaAno)
        self.comboboxAno['values'] = listaAno

        self.labelCurso = tk.Label(self.frameBody, text='Curso: ', bg='#76cb69')
        self.escolhaCurso = tk.StringVar()
        self.comboboxCurso = ttk.Combobox(self.frameBody, width=30, textvariable=self.escolhaCurso)
        self.comboboxCurso['values'] = listaCursos

        self.buttonConsultar = tk.Button(self.frameBody, text='Realizar Consulta')
        self.buttonConsultar.bind('<Button>', controle.gradeConsulta)
        self.buttonClear = tk.Button(self.frameBody ,text='Clear')      
        self.buttonClear.bind('<Button>', self.clearConsulta)  
        self.buttonFecha = tk.Button(self.frameBody ,text='Finalizar')      
        self.buttonFecha.bind('<Button>', self.fechaConsulta)

        self.labelAno.grid(row=0, column=0, sticky='W', pady=20)
        self.comboboxAno.grid(row=0, column=1, sticky='W', pady=20)
        self.labelCurso.grid(row=1, column=0, sticky='W', pady=20)
        self.comboboxCurso.grid(row=1, column=1, sticky='W', pady=20)
        self.buttonConsultar.grid(row=2, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=2, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=2, column=4, sticky='W', pady=20)

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def clearConsulta(self, event):
        self.comboboxAno.delete(0, 'end')
        self.comboboxCurso.delete(0, 'end')

    def fechaConsulta(self, event):
        self.janela.destroy()


class LimiteExcluiGrade():
    def __init__(self, controle, root, listaAno, listaCurso):
        self.janela=root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='EXCLUIR GRADE', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelAno = tk.Label(self.frameBody, text='Ano: ', bg='#76cb69')
        self.escolhaAno = tk.StringVar()
        self.comboboxAno = ttk.Combobox(self.frameBody, width=10, textvariable=self.escolhaAno)
        self.comboboxAno['values'] = listaAno

        self.labelCurso = tk.Label(self.frameBody, text='Curso: ', bg='#76cb69')
        self.escolhaCurso = tk.StringVar()
        self.comboboxCurso = ttk.Combobox(self.frameBody, width=30, textvariable=self.escolhaCurso)
        self.comboboxCurso['values'] = listaCurso
    
        self.buttonExcluir = tk.Button(self.frameBody, text='Excluir Grade')
        self.buttonExcluir.bind('<Button>', controle.gradeDelete)
        self.buttonClear = tk.Button(self.frameBody ,text='Clear')      
        self.buttonClear.bind('<Button>', self.clearExclusao)  
        self.buttonFecha = tk.Button(self.frameBody ,text='Finalizar')      
        self.buttonFecha.bind('<Button>', self.fechaExclusao)

        self.labelAno.grid(row=0, column=0, sticky='W', pady=20)
        self.comboboxAno.grid(row=0, column=1, sticky='W', pady=20)
        self.labelCurso.grid(row=1, column=0, sticky='W', pady=20)
        self.comboboxCurso.grid(row=1, column=1, sticky='W', pady=20)
        self.buttonExcluir.grid(row=2, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=2, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=2, column=4, sticky='W', pady=20)

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def clearExclusao(self, event):
        self.comboboxAno.delete(0, 'end')
        self.comboboxCurso.delete(0, 'end')
    
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
        self.comboboxGrade = ttk.Combobox(self.frameBody, width=20, textvariable=self.escolhaGrade)
        self.comboboxGrade['values'] = listaGrade

        self.labelCurso = tk.Label(self.frameBody, text='Atualizar curso: ', bg='#76cb69')
        self.escolhaCurso = tk.StringVar()
        self.comboboxCurso = ttk.Combobox(self.frameBody, width=20, textvariable=self.escolhaCurso)
        self.comboboxCurso['values'] = listaCurso
        self.comboboxCurso.bind('<<ComboboxSelected>>', controle.popular)

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

        self.labelGrade.grid(row=0, column=0, sticky='W', pady=20)
        self.comboboxGrade.grid(row=0, column=1, sticky='W', pady=20)
        self.labelCurso.grid(row=1, column=0, sticky='W', pady=20)
        self.comboboxCurso.grid(row=1, column=1, sticky='W', pady=20)
        self.labelDisc.grid(row=2, column=1, sticky='W')
        self.listbox.grid(row=3, column=1, sticky='W')
        self.labelTodasDisc.grid(row=2, column=2, sticky='W')
        self.listboxTodas.grid(row=3, column=2, sticky='W')
        self.buttonRemove.grid(row=4, column=1, sticky='W', pady=10)
        self.buttonAdiciona.grid(row=4, column=2, sticky='W', pady=10)
        self.buttonFecha.grid(row=4, column=3, sticky='W', pady=10)
    
    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def fechaAtualizacao(self, event):
        self.janela.destroy()

    def IsPopularListbox(self, listaGradeCodDisc):
        for disc in listaGradeCodDisc:
            self.listbox.insert(tk.END, disc)
        return True

    def IsPopularListboxTodas(self, listaTodasDisciplinas, listaGradeCodDisc):
        for todas in listaTodasDisciplinas:
            if todas not in listaGradeCodDisc:
                self.listboxTodas.insert(tk.END, todas)
        return True

    def limparListBox(self):
        self.listbox.delete(0, 'end')
        self.listboxTodas.delete(0, 'end')