from tkinter import *
from tkinter import ttk, messagebox

class LimiteCurso():
    def __init__(self, controle, frame1, frame2, listaCursos, listaDisc):
        self.frame1 = frame1
        self.frame2 = frame2

        self.labelTitulo = Label(self.frame1, text='CURSOS', bg='#dfe3ee', font=('Heveltica Bold', 14))
        self.labelTitulo.place(relx=0.38, rely=0.01, relwidth=0.2)

        self.labelCurso = Label(self.frame1, text='Curso', bg= '#dfe3ee', fg = '#107db2')
        self.labelCurso.place(relx=0.05, rely=0.15)
        self.inputCurso = Entry(self.frame1)
        self.inputCurso.place(relx=0.05, rely=0.25, relwidth=0.4)

        self.labelGrade = Label(self.frame1, text='Grade (ano)', bg= '#dfe3ee', fg = '#107db2')
        self.labelGrade.place(relx=0.05, rely=0.40)
        self.inputGrade = Entry(self.frame1)
        self.inputGrade.place(relx=0.05, rely=0.50, relwidth=0.4)

        self.labelDisc = Label(self.frame1, text='Disciplinas',  bg= '#dfe3ee', fg = '#107db2')
        self.labelDisc.place(relx=0.55, rely=0.15)
        self.listboxDisc = Listbox(self.frame1)
        for disc in listaDisc:
            self.listboxDisc.insert(END, disc.codigo)
        self.listboxDisc.place(relx=0.55, rely=0.25, relheight=0.70)
        
        self.buttonBuscar = Button(self.frame1, text='Buscar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command = controle.buscaCurso)
        self.buttonBuscar.place(relx=0.05, rely=0.80, relwidth=0.1, relheight=0.15)

        self.buttonLimpar = Button(self.frame1, text= 'Limpar', bd=2, bg = '#107db2',fg = 'white', 
                                font = ('verdana', 8, 'bold'), command= self.limpaCurso)
        self.buttonLimpar.place(relx= 0.15, rely=0.80, relwidth=0.1, relheight= 0.15)

        self.buttonAlterar = Button(self.frame1, text='Alterar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=controle.alteraCurso)
        self.buttonAlterar.place(relx=0.3, rely=0.80, relwidth=0.1, relheight=0.15)
        
        self.buttonDeletar = Button(self.frame1, text='Apagar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=controle.deletaCurso)
        self.buttonDeletar.place(relx=0.4, rely=0.80, relwidth=0.1, relheight=0.15)

        self.buttonInserir = Button(self.frame1, text='Inserir', bd=2, bg = '#107db2',fg = 'white',
                            font = ('verdana', 8, 'bold'), command=controle.insereCurso)
        self.buttonInserir.place(relx=0.77, rely=0.80, relwidth=0.1, relheight=0.15)
        
        self.buttonInserir = Button(self.frame1, text='Cadastrar', bd=2, bg = '#107db2',fg = 'white',
                            font = ('verdana', 8, 'bold'), command=controle.cadastraCurso)
        self.buttonInserir.place(relx=0.89, rely=0.80, relwidth=0.1, relheight=0.15)

        self.tabelaDisc = ttk.Treeview(self.frame2, column=('curso', 'grade'), show='headings')
        self.tabelaDisc.column('curso', minwidth=0, width=100)
        self.tabelaDisc.column('grade', minwidth=0, width=50)
        self.tabelaDisc.heading('curso', text='CURSO')
        self.tabelaDisc.heading('grade', text='GRADE')
        self.tabelaDisc.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        for curso in listaCursos:
            self.tabelaDisc.insert(parent='', index='end', values=(curso.nome, curso.grade.ano))
            for disc in curso.grade.disciplinas:
                self.tabelaDisc.insert(parent='', index='end', values=(disc['codigo'], disc['nome'], disc['cargaHoraria']))


        self.scroolLista = Scrollbar(self.frame2, orient='vertical')
        self.tabelaDisc.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.tabelaDisc.bind('<Double-1>', self.OnDoubleClick)

    def limpaCurso(self):
        self.inputCurso.config(state=NORMAL)
        self.inputCurso.delete(0, 'end')
        self.inputGrade.delete(0, 'end')

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def OnDoubleClick(self, event):
        self.inputCurso.config(state=NORMAL)
        self.limpaCurso()
        self.tabelaDisc.selection()

        for n in self.tabelaDisc.selection():
            col1, col2 = self.tabelaDisc.item(n, 'values')
            self.inputCurso.insert(END, col1)
            self.inputCurso.config(state=DISABLED)
            self.inputGrade.insert(END, col2)
        