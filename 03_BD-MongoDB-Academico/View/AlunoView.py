from tkinter import *
from tkinter import ttk, messagebox

class LimiteAluno():
    def __init__(self, controle, frame1, frame2, listaAlunos):
        self.frame1 = frame1
        self.frame2 = frame2

        self.labelTitulo = Label(self.frame1, text='ALUNOS', bg='#dfe3ee', font=('Heveltica Bold', 14))
        self.labelTitulo.place(relx=0.38, rely=0.01, relwidth=0.2)

        self.labelNome = Label(self.frame1, text='Nome aluno', bg= '#dfe3ee', fg = '#107db2')
        self.labelNome.place(relx=0.05, rely=0.1)
        self.inputNome = Entry(self.frame1)
        self.inputNome.place(relx=0.05, rely=0.2, relwidth=0.85)

        self.labelMatric = Label(self.frame1, text='Matrícula', bg= '#dfe3ee', fg = '#107db2')
        self.labelMatric.place(relx=0.05, rely=0.35)
        self.inputMatric = Entry(self.frame1)
        self.inputMatric.place(relx=0.05, rely=0.45, relwidth=0.4)

        self.labelCurso = Label(self.frame1, text='Curso', bg= '#dfe3ee', fg = '#107db2')
        self.labelCurso.place(relx=0.5, rely=0.35)
        self.inputCurso = Entry(self.frame1)
        self.inputCurso.place(relx=0.5, rely=0.45, relwidth=0.4)
        
        self.buttonBuscar = Button(self.frame1, text='Buscar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command = self.buscaDisciplina)
        self.buttonBuscar.place(relx=0.05, rely=0.7, relwidth=0.1, relheight=0.15)

        self.buttonLimpar = Button(self.frame1, text= 'Limpar', bd=2, bg = '#107db2',fg = 'white', 
                                font = ('verdana', 8, 'bold'), command= self.limpaDisciplina)
        self.buttonLimpar.place(relx= 0.15, rely=0.7, relwidth=0.1, relheight= 0.15)

        self.buttonInserir = Button(self.frame1, text='Inserir', bd=2, bg = '#107db2',fg = 'white',
                            font = ('verdana', 8, 'bold'), command=self.insereDisciplina)
        self.buttonInserir.place(relx=0.58, rely=0.7, relwidth=0.1, relheight=0.15)

        self.buttonAlterar = Button(self.frame1, text='Alterar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.alteraDisciplina)
        self.buttonAlterar.place(relx=0.7, rely=0.7, relwidth=0.1, relheight=0.15)
        
        self.buttonDeletar = Button(self.frame1, text='Apagar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.deletaDisciplina)
        self.buttonDeletar.place(relx=0.8, rely=0.7, relwidth=0.1, relheight=0.15)

        self.tabelaAlunos = ttk.Treeview(self.frame2, column=('matricula', 'nome', 'curso'), show='headings')
        self.tabelaAlunos.column('matricula', minwidth=0, width=100)
        self.tabelaAlunos.column('nome', minwidth=0, width=250)
        self.tabelaAlunos.column('curso', minwidth=0, width=200)
        self.tabelaAlunos.heading('matricula', text='MATRÍCULA')
        self.tabelaAlunos.heading('nome', text='NOME')
        self.tabelaAlunos.heading('curso', text='CURSO')
        self.tabelaAlunos.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        for disc in listaAlunos:
            self.tabelaAlunos.insert('', 'end', values=(disc.getNroMatric(), disc.getNome(), disc.getCurso()))

        self.scroolLista = Scrollbar(self.frame2, orient='vertical')
        self.tabelaAlunos.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        # self.tabelaAlunos.bind('<Double-1>', self.OnDoubleClick)

    def limpaDisciplina(self):
        print('Limpa aluno')

    def buscaDisciplina(self):
        print('Busca aluno')

    def alteraDisciplina(self):
        print('Altera aluno')

    def deletaDisciplina(self):
        print('Deleta aluno')

    def insereDisciplina(self):
        print('Insere aluno')

