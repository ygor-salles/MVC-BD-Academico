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
        
        self.buttonBuscar = Button(self.frame1, text='Buscar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command = controle.buscaAluno)
        self.buttonBuscar.place(relx=0.05, rely=0.7, relwidth=0.1, relheight=0.15)

        self.buttonLimpar = Button(self.frame1, text= 'Limpar', bd=2, bg = '#107db2',fg = 'white', 
                                font = ('verdana', 8, 'bold'), command= self.limpaAluno)
        self.buttonLimpar.place(relx= 0.15, rely=0.7, relwidth=0.1, relheight= 0.15)

        self.buttonInserir = Button(self.frame1, text='Inserir', bd=2, bg = '#107db2',fg = 'white',
                            font = ('verdana', 8, 'bold'), command=controle.insereAluno)
        self.buttonInserir.place(relx=0.58, rely=0.7, relwidth=0.1, relheight=0.15)

        self.buttonAlterar = Button(self.frame1, text='Alterar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=controle.alteraAluno)
        self.buttonAlterar.place(relx=0.7, rely=0.7, relwidth=0.1, relheight=0.15)
        
        self.buttonDeletar = Button(self.frame1, text='Apagar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=controle.deletaAluno)
        self.buttonDeletar.place(relx=0.8, rely=0.7, relwidth=0.1, relheight=0.15)

        self.tabelaDisc = ttk.Treeview(self.frame2, column=('matricula', 'nome'), show='headings')
        self.tabelaDisc.column('matricula', minwidth=0, width=150, anchor=CENTER)
        self.tabelaDisc.column('nome', minwidth=0, width=250, anchor=CENTER)
        self.tabelaDisc.heading('matricula', text='MATRÍCULA')
        self.tabelaDisc.heading('nome', text='NOME')
        self.tabelaDisc.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        for aluno in listaAlunos:
            self.tabelaDisc.insert('', 'end', values=(aluno.matricula, aluno.nome))

        self.scroolLista = Scrollbar(self.frame2, orient='vertical')
        self.tabelaDisc.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.tabelaDisc.bind('<Double-1>', self.OnDoubleClick)

    def limpaAluno(self):
        self.inputMatric.config(state=NORMAL)
        self.inputMatric.delete(0, 'end')
        self.inputNome.delete(0, 'end')

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def OnDoubleClick(self, event):
        self.inputMatric.config(state=NORMAL)
        self.limpaAluno()
        self.tabelaDisc.selection()

        for n in self.tabelaDisc.selection():
            col1, col2 = self.tabelaDisc.item(n, 'values')
            self.inputMatric.insert(END, col1)
            self.inputMatric.config(state=DISABLED)
            self.inputNome.insert(END, col2)
        