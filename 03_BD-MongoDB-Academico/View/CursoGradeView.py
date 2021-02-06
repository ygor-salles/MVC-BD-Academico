from tkinter import *
from tkinter import ttk, messagebox

class LimiteCurso():
    def __init__(self, controle, frame1, frame2, listaCursos):
        self.frame1 = frame1
        self.frame2 = frame2

        self.labelTitulo = Label(self.frame1, text='CURSOS', bg='#dfe3ee', font=('Heveltica Bold', 14))
        self.labelTitulo.place(relx=0.38, rely=0.01, relwidth=0.2)

        self.labelCurso = Label(self.frame1, text='Curso', bg= '#dfe3ee', fg = '#107db2')
        self.labelCurso.place(relx=0.5, rely=0.35)
        self.inputCurso = Entry(self.frame1)
        self.inputCurso.place(relx=0.5, rely=0.2, relwidth=0.4)

        self.labelGrade = Label(self.frame1, text='Grade (ano)', bg= '#dfe3ee', fg = '#107db2')
        self.labelGrade.place(relx=0.05, rely=0.35)
        self.inputGrade = Entry(self.frame1)
        self.inputGrade.place(relx=0.05, rely=0.2, relwidth=0.4)
        
        self.buttonBuscar = Button(self.frame1, text='Buscar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command = controle.buscaCurso)
        self.buttonBuscar.place(relx=0.05, rely=0.7, relwidth=0.1, relheight=0.15)

        self.buttonLimpar = Button(self.frame1, text= 'Limpar', bd=2, bg = '#107db2',fg = 'white', 
                                font = ('verdana', 8, 'bold'), command= self.limpaCurso)
        self.buttonLimpar.place(relx= 0.15, rely=0.7, relwidth=0.1, relheight= 0.15)

        self.buttonInserir = Button(self.frame1, text='Inserir', bd=2, bg = '#107db2',fg = 'white',
                            font = ('verdana', 8, 'bold'), command=controle.insereCurso)
        self.buttonInserir.place(relx=0.58, rely=0.7, relwidth=0.1, relheight=0.15)

        self.buttonAlterar = Button(self.frame1, text='Alterar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=controle.alteraCurso)
        self.buttonAlterar.place(relx=0.7, rely=0.7, relwidth=0.1, relheight=0.15)
        
        self.buttonDeletar = Button(self.frame1, text='Apagar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=controle.deletaCurso)
        self.buttonDeletar.place(relx=0.8, rely=0.7, relwidth=0.1, relheight=0.15)

        self.tabelaDisc = ttk.Treeview(self.frame2, column=('matricula', 'nome', 'curso'), show='headings')
        self.tabelaDisc.column('matricula', minwidth=0, width=100, anchor=CENTER)
        self.tabelaDisc.column('nome', minwidth=0, width=150)
        self.tabelaDisc.column('curso', minwidth=0, width=150, anchor=CENTER)
        self.tabelaDisc.heading('matricula', text='MATRÍCULA')
        self.tabelaDisc.heading('nome', text='NOME')
        self.tabelaDisc.heading('curso', text='CURSO')
        self.tabelaDisc.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        for aluno in listaCursos:
            self.tabelaDisc.insert('', 'end', values=(aluno.matricula, aluno.nome, aluno.curso))

        self.scroolLista = Scrollbar(self.frame2, orient='vertical')
        self.tabelaDisc.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.tabelaDisc.bind('<Double-1>', self.OnDoubleClick)

    def limpaCurso(self):
        self.inputMatric.config(state=NORMAL)
        self.inputMatric.delete(0, 'end')
        self.inputNome.delete(0, 'end')
        self.inputCurso.delete(0, 'end')

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def OnDoubleClick(self, event):
        self.inputMatric.config(state=NORMAL)
        self.limpaCurso()
        self.tabelaDisc.selection()

        for n in self.tabelaDisc.selection():
            col1, col2, col3 = self.tabelaDisc.item(n, 'values')
            self.inputMatric.insert(END, col1)
            self.inputMatric.config(state=DISABLED)
            self.inputNome.insert(END, col2)
            self.inputCurso.insert(END, col3)
        