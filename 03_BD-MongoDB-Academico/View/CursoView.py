from tkinter import *
from tkinter import ttk, messagebox

class LimiteCurso():
    def __init__(self, controle, frame1, frame2, listaCursos, listaAlunos, listaGrades):
        self.frame1 = frame1
        self.frame2 = frame2

        self.labelTitulo = Label(self.frame1, text='CURSOS', bg='#dfe3ee', font=('Heveltica Bold', 14))
        self.labelTitulo.place(relx=0.38, rely=0.01, relwidth=0.2)

        self.labelCurso = Label(self.frame1, text='CURSO: ', bg= '#dfe3ee', fg = '#107db2')
        self.labelCurso.place(relx=0.02, rely=0.20)
        self.inputCurso = Entry(self.frame1)
        self.inputCurso.place(relx=0.10, rely=0.20, relwidth=0.3)

        self.labelGrade = Label(self.frame1, text='GRADE: ', bg= '#dfe3ee', fg = '#107db2')
        self.labelGrade.place(relx=0.02, rely=0.35)
        self.escolhaGrade = StringVar()
        self.comboboxGrade = ttk.Combobox(self.frame1, textvariable=self.escolhaGrade)
        self.comboboxGrade['values'] = listaGrades
        self.comboboxGrade.place(relx=0.10, rely=0.35)

        self.labelAluno = Label(self.frame1, text='Alunos p/ cadastro: ',  bg= '#dfe3ee', fg = '#107db2')
        self.labelAluno.place(relx=0.50, rely=0.18)
        self.listboxAluno = Listbox(self.frame1)
        for aluno in listaAlunos:
            self.listboxAluno.insert(END, aluno)
        self.listboxAluno.place(relx=0.50, rely=0.28, relheight=0.65)
        
        self.buttonBuscar = Button(self.frame1, text='Buscar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command = controle.buscaCurso)
        self.buttonBuscar.place(relx=0.02, rely=0.80, relwidth=0.12, relheight=0.15)

        self.buttonLimpar = Button(self.frame1, text= 'Limpar', bd=2, bg = '#107db2',fg = 'white', 
                                font = ('verdana', 8, 'bold'), command= self.limpaCurso)
        self.buttonLimpar.place(relx=0.17, rely=0.80, relwidth=0.12, relheight= 0.15)
        
        self.buttonInserir = Button(self.frame1, text='Inserir', bd=2, bg = '#107db2',fg = 'white',
                            font = ('verdana', 8, 'bold'), command=controle.insereAl)
        self.buttonInserir.place(relx=0.86, rely=0.50, relwidth=0.12, relheight=0.15)

        self.buttonDeletar = Button(self.frame1, text='Apagar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=controle.deletaCurso)
        self.buttonDeletar.place(relx=0.86, rely=0.20, relwidth=0.12, relheight=0.15)
        
        self.buttonCadastrar = Button(self.frame1, text='Cadastrar', bd=2, bg = '#107db2',fg = 'white',
                            font = ('verdana', 8, 'bold'), command=controle.cadastraCurso)
        self.buttonCadastrar.place(relx=0.86, rely=0.80, relwidth=0.12, relheight=0.15)

        self.tabelaAl = ttk.Treeview(self.frame2)
        self.tabelaAl['columns'] = ('curso', 'grade', 'alMatricula', 'alNome', 'alCurso')  
        self.tabelaAl.column('#0', minwidth=0, width=5)
        self.tabelaAl.column('curso', minwidth=0, width=80)
        self.tabelaAl.column('grade', minwidth=0, width=60)
        self.tabelaAl.column('alMatricula', minwidth=0, width=50)
        self.tabelaAl.column('alNome', minwidth=0, width=125)
        self.tabelaAl.column('alCurso', minwidth=0, width=80)
        self.tabelaAl.heading('#0', text='', anchor=W)
        self.tabelaAl.heading('curso', text='CURSO')
        self.tabelaAl.heading('grade', text='GRADE')
        self.tabelaAl.heading('alMatricula', text='MATRIC ALUNO')
        self.tabelaAl.heading('alNome', text='NOME ALUNO')
        self.tabelaAl.heading('alCurso', text='CURSO DO ALUNO')
        self.tabelaAl.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        contChild=0
        contParent=0
        for curso in listaCursos:
            self.tabelaAl.insert(parent='', index='end', iid=contParent, values=(curso.nome, curso.grade.anoCurso))
            for aluno in curso.alunos:
                contChild += 1
                self.tabelaAl.insert(parent='', index='end', iid=contChild, values=('', '', aluno['matricula'], aluno['nome'], aluno['curso']))
                self.tabelaAl.move(f'{contChild}', f'{contParent}', f'{contParent}')
            contParent = contChild+1
            contChild = contParent

        self.scroolLista = Scrollbar(self.frame2, orient='vertical')
        self.tabelaAl.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.tabelaAl.bind('<Double-1>', self.OnDoubleClick)

    def limpaCurso(self):
        self.inputCurso.config(state=NORMAL)
        self.inputCurso.delete(0, 'end')
        self.comboboxGrade.delete(0, 'end')

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def OnDoubleClick(self, event):
        self.inputCurso.config(state=NORMAL)
        self.limpaCurso()
        self.tabelaAl.selection()

        for n in self.tabelaAl.selection():
            col1 = self.tabelaAl.item(n, 'values')
            self.inputCurso.insert(END, col1)
            self.inputCurso.config(state=DISABLED)

class LimiteAlteraCurso():
    def __init__(self, controle, frame1, frame2, listaNomeCurso, listaCursos, listaAlunos):
        self.frame1 = frame1
        self.frame2 = frame2
        self.listaCurso = listaCursos
        self.listaAlunos = listaAlunos
        self.listaCursoAl = []

        self.labelTitulo = Label(self.frame1, text='ATUALIZAR CURSO', bg='#dfe3ee', font=('Heveltica Bold', 14))
        self.labelTitulo.place(relx=0.25, rely=0.01, relwidth=0.5)

        self.labelCurso = Label(self.frame1, text='NOME CURSO:', bg= '#dfe3ee', fg = '#107db2')
        self.labelCurso.place(relx=0.05, rely=0.25)
        self.escolhaCurso = StringVar()
        self.comboboxCurso = ttk.Combobox(self.frame1, textvariable=self.escolhaCurso)
        self.comboboxCurso['values'] = listaNomeCurso
        self.comboboxCurso.bind('<<ComboboxSelected>>', self.popular)
        self.comboboxCurso.place(relx=0.20, rely=0.25, relwidth=0.25)

        self.labelAdd = Label(self.frame1, text='Add alunos',  bg= '#dfe3ee', fg = '#107db2')
        self.labelAdd.place(relx=0.70, rely=0.20)
        self.listboxAdd = Listbox(self.frame1)
        self.listboxAdd.place(relx=0.70, rely=0.30, relheight=0.50, relwidth=0.15)

        self.labelRemove = Label(self.frame1, text='Alunos do curso',  bg= '#dfe3ee', fg = '#107db2')
        self.labelRemove.place(relx=0.50, rely=0.20)
        self.listboxRemove = Listbox(self.frame1)
        self.listboxRemove.place(relx=0.50, rely=0.30, relheight=0.50, relwidth=0.15)

        self.buttonRemover = Button(self.frame1, text='Remover', bd=2, bg = '#107db2',fg = 'white',
                            font = ('verdana', 8, 'bold'), command=controle.removeAluno)
        self.buttonRemover.place(relx=0.50, rely=0.82, relwidth=0.12, relheight=0.15)
        
        self.buttonAdicionar = Button(self.frame1, text='Adicionar', bd=2, bg = '#107db2',fg = 'white',
                            font = ('verdana', 8, 'bold'), command=controle.adicionaAluno)
        self.buttonAdicionar.place(relx=0.70, rely=0.82, relwidth=0.12, relheight=0.15)
        
        self.buttonAtualizar = Button(self.frame1, text='Atualizar', bd=2, bg = '#107db2',fg = 'white',
                            font = ('verdana', 8, 'bold'), command=controle.atualizaCurso)
        self.buttonAtualizar.place(relx=0.05, rely=0.82, relwidth=0.12, relheight=0.15)

        self.tabelaAl = ttk.Treeview(self.frame2)
        self.tabelaAl['columns'] = ('curso', 'grade', 'alMatricula', 'alNome', 'alCurso')  
        self.tabelaAl.column('#0', minwidth=0, width=5)
        self.tabelaAl.column('curso', minwidth=0, width=80)
        self.tabelaAl.column('grade', minwidth=0, width=60)
        self.tabelaAl.column('alMatricula', minwidth=0, width=50)
        self.tabelaAl.column('alNome', minwidth=0, width=125)
        self.tabelaAl.column('alCurso', minwidth=0, width=80)
        self.tabelaAl.heading('#0', text='', anchor=W)
        self.tabelaAl.heading('curso', text='CURSO')
        self.tabelaAl.heading('grade', text='GRADE')
        self.tabelaAl.heading('alMatricula', text='MATRIC ALUNO')
        self.tabelaAl.heading('alNome', text='NOME ALUNO')
        self.tabelaAl.heading('alCurso', text='CURSO DO ALUNO')
        self.tabelaAl.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        contChild=0
        contParent=0
        for curso in listaCursos:
            self.tabelaAl.insert(parent='', index='end', iid=contParent, values=(curso.nome, curso.grade.anoCurso))
            for aluno in curso.alunos:
                contChild += 1
                self.tabelaAl.insert(parent='', index='end', iid=contChild, values=('', '', aluno['matricula'], aluno['nome'], aluno['curso']))
                self.tabelaAl.move(f'{contChild}', f'{contParent}', f'{contParent}')
            contParent = contChild+1
            contChild = contParent

        self.scroolLista = Scrollbar(self.frame2, orient='vertical')
        self.tabelaAl.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.tabelaAl.bind('<Double-1>', self.OnDoubleClick)

    def fechaJanela(self):
        self.frame1.destroy()
        self.frame2.destroy()
    
    def limpaCurso(self):
        self.comboboxCurso.delete(0, 'end')

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def OnDoubleClick(self, event):
        self.limpaCurso()
        self.tabelaAl.selection()

        for n in self.tabelaAl.selection():
            col1 = self.tabelaAl.item(n, 'values')
            self.comboboxCurso.insert(END, col1)
    
    def getListaCursoMatricAluno(self, nomeCurso):
        listaCursoMatricAluno = []
        for curso in self.listaCurso:
            if nomeCurso == curso.nome:
                for aluno in curso.alunos:
                    listaCursoMatricAluno.append(aluno['matricula'])
                return listaCursoMatricAluno

    def getListaCursoAluno(self, nomeCurso):
        listaCursoAl = []
        for curso in self.listaCurso:
            if nomeCurso == curso.nome:
                for aluno in curso.alunos:
                    listaCursoAl.append(aluno)
                return listaCursoAl
    
    def limparListBox(self):
        self.listboxRemove.delete(0, 'end')
        self.listboxAdd.delete(0, 'end')
    
    def IsPopularListbox(self, listaCursoMatricAluno):
        for aluno in listaCursoMatricAluno:
            self.listboxRemove.insert(END, aluno)
        return True
    
    def IsPopularListboxTodas(self, listaTodosAlunos, listaCursoMatricAluno):
        for todos in listaTodosAlunos:
            if todos not in listaCursoMatricAluno:
                self.listboxAdd.insert(END, todos)
        return True
    
    def popular(self, event):
        #para os listBox's
        self.limparListBox()
        comboNomeCurso = self.escolhaCurso.get()
        listaCursoMatricAluno = self.getListaCursoMatricAluno(comboNomeCurso)
        self.listaCursoAl = self.getListaCursoAluno(comboNomeCurso)
        self.IsPopularListbox(listaCursoMatricAluno)
        self.IsPopularListboxTodas(self.listaAlunos ,listaCursoMatricAluno)

