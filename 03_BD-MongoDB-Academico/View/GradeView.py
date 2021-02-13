from tkinter import *
from tkinter import ttk, messagebox

class LimiteGrade():
    def __init__(self, controle, frame1, frame2, listaGrades, listaDisc):
        self.frame1 = frame1
        self.frame2 = frame2

        self.labelTitulo = Label(self.frame1, text='GRADES', bg='#dfe3ee', font=('Heveltica Bold', 14))
        self.labelTitulo.place(relx=0.38, rely=0.01, relwidth=0.2)

        self.labelGrade = Label(self.frame1, text='ANO/CURSO (2017/SIN):', bg= '#dfe3ee', fg = '#107db2')
        self.labelGrade.place(relx=0.05, rely=0.20)
        self.placeholder = StringVar(None)
        self.placeholder.set('Ex: 2017/SIN')
        self.inputGrade = Entry(self.frame1, textvariable=self.placeholder)
        self.inputGrade.bind('<Enter>', self.clearBox)
        self.inputGrade.place(relx=0.26, rely=0.20, relwidth=0.2)

        self.labelDisc = Label(self.frame1, text='Disciplinas p/ cadastro: ',  bg= '#dfe3ee', fg = '#107db2')
        self.labelDisc.place(relx=0.05, rely=0.35)
        self.listboxDisc = Listbox(self.frame1)
        for disc in listaDisc:
            self.listboxDisc.insert(END, disc.codigo)
        self.listboxDisc.place(relx=0.26, rely=0.35, relheight=0.60)
        
        self.buttonBuscar = Button(self.frame1, text='Buscar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command = controle.buscaGrade)
        self.buttonBuscar.place(relx=0.70, rely=0.20, relwidth=0.12, relheight=0.15)

        self.buttonLimpar = Button(self.frame1, text= 'Limpar', bd=2, bg = '#107db2',fg = 'white', 
                                font = ('verdana', 8, 'bold'), command= self.limpaGrade)
        self.buttonLimpar.place(relx=0.85, rely=0.20, relwidth=0.12, relheight= 0.15)
        
        self.buttonInserir = Button(self.frame1, text='Inserir', bd=2, bg = '#107db2',fg = 'white',
                            font = ('verdana', 8, 'bold'), command=controle.insereDisc)
        self.buttonInserir.place(relx=0.70, rely=0.50, relwidth=0.12, relheight=0.15)

        self.buttonDeletar = Button(self.frame1, text='Apagar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=controle.deletaGrade)
        self.buttonDeletar.place(relx=0.85, rely=0.50, relwidth=0.12, relheight=0.15)
        
        self.buttonCadastrar = Button(self.frame1, text='Cadastrar', bd=2, bg = '#107db2',fg = 'white',
                            font = ('verdana', 8, 'bold'), command=controle.cadastraGrade)
        self.buttonCadastrar.place(relx=0.85, rely=0.80, relwidth=0.12, relheight=0.15)

        self.tabelaDisc = ttk.Treeview(self.frame2)
        self.tabelaDisc['columns'] = ('grade', 'discCodigo', 'discNome', 'discCH')  
        self.tabelaDisc.column('#0', minwidth=0, width=5)
        self.tabelaDisc.column('grade', minwidth=0, width=50)
        self.tabelaDisc.column('discCodigo', minwidth=0, width=100)
        self.tabelaDisc.column('discNome', minwidth=0, width=195)
        self.tabelaDisc.column('discCH', minwidth=0, width=50)
        self.tabelaDisc.heading('#0', text='', anchor=W)
        self.tabelaDisc.heading('grade', text='GRADE')
        self.tabelaDisc.heading('discCodigo', text='CODIGO DISC')
        self.tabelaDisc.heading('discNome', text='NOME DISC')
        self.tabelaDisc.heading('discCH', text='CH DISC')
        self.tabelaDisc.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        contChild=0
        contParent=0
        for grade in listaGrades:
            self.tabelaDisc.insert(parent='', index='end', iid=contParent, values=(grade.anoCurso))
            for disc in grade.disciplinas:
                contChild += 1
                self.tabelaDisc.insert(parent='', index='end', iid=contChild, values=('', disc['codigo'], disc['nome'], disc['cargaHoraria']))
                self.tabelaDisc.move(f'{contChild}', f'{contParent}', f'{contParent}')
            contParent = contChild+1
            contChild = contParent

        self.scroolLista = Scrollbar(self.frame2, orient='vertical')
        self.tabelaDisc.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.tabelaDisc.bind('<Double-1>', self.OnDoubleClick)

    def fechaJanela(self):
        self.frame1.destroy()
        self.frame2.destroy()
    
    def limpaGrade(self):
        self.inputGrade.config(state=NORMAL)
        self.inputGrade.delete(0, 'end')

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def OnDoubleClick(self, event):
        self.inputGrade.config(state=NORMAL)
        self.limpaGrade()
        self.tabelaDisc.selection()

        for n in self.tabelaDisc.selection():
            col1 = self.tabelaDisc.item(n, 'values')
            self.inputGrade.insert(END, col1)
            self.inputGrade.config(state=DISABLED)

    def clearBox(self, event):
        self.inputGrade.delete(0, 'end')

class LimiteAlteraGrade():
    def __init__(self, controle, frame1, frame2, listaAnoCurso, listaGrades, listaDisc):
        self.frame1 = frame1
        self.frame2 = frame2
        self.listaAnoCurso = listaAnoCurso
        self.listaGrade = listaGrades
        self.listaDisc = listaDisc
        self.testePopula = False
        self.listaGradeDisc = []

        self.labelTitulo = Label(self.frame1, text='ATUALIZAR GRADE', bg='#dfe3ee', font=('Heveltica Bold', 14))
        self.labelTitulo.place(relx=0.25, rely=0.01, relwidth=0.5)

        self.labelGrade = Label(self.frame1, text='ANO/CURSO:', bg= '#dfe3ee', fg = '#107db2')
        self.labelGrade.place(relx=0.05, rely=0.25)
        self.escolhaGrade = StringVar()
        self.comboboxGrade = ttk.Combobox(self.frame1, textvariable=self.escolhaGrade)
        self.comboboxGrade['values'] = listaAnoCurso
        self.comboboxGrade.bind('<<ComboboxSelected>>', self.popular)
        self.comboboxGrade.place(relx=0.20, rely=0.25, relwidth=0.2)

        self.labelAdd = Label(self.frame1, text='Add disciplinas',  bg= '#dfe3ee', fg = '#107db2')
        self.labelAdd.place(relx=0.70, rely=0.20)
        self.listboxAdd = Listbox(self.frame1)
        self.listboxAdd.place(relx=0.70, rely=0.30, relheight=0.50, relwidth=0.15)

        self.labelRemove = Label(self.frame1, text='Disciplinas da grade',  bg= '#dfe3ee', fg = '#107db2')
        self.labelRemove.place(relx=0.50, rely=0.20)
        self.listboxRemove = Listbox(self.frame1)
        self.listboxRemove.place(relx=0.50, rely=0.30, relheight=0.50, relwidth=0.15)

        self.buttonRemover = Button(self.frame1, text='Remover', bd=2, bg = '#107db2',fg = 'white',
                            font = ('verdana', 8, 'bold'), command=controle.removeDisciplina)
        self.buttonRemover.place(relx=0.50, rely=0.82, relwidth=0.12, relheight=0.15)
        
        self.buttonAdicionar = Button(self.frame1, text='Adicionar', bd=2, bg = '#107db2',fg = 'white',
                            font = ('verdana', 8, 'bold'), command=controle.adicionaDisciplina)
        self.buttonAdicionar.place(relx=0.70, rely=0.82, relwidth=0.12, relheight=0.15)
        
        self.buttonAtualizar = Button(self.frame1, text='Atualizar', bd=2, bg = '#107db2',fg = 'white',
                            font = ('verdana', 8, 'bold'), command=controle.atualizaGrade)
        self.buttonAtualizar.place(relx=0.05, rely=0.82, relwidth=0.12, relheight=0.15)

        self.tabelaDisc = ttk.Treeview(self.frame2)
        self.tabelaDisc['columns'] = ('grade', 'discCodigo', 'discNome', 'discCH')  
        self.tabelaDisc.column('#0', minwidth=0, width=5)
        self.tabelaDisc.column('grade', minwidth=0, width=50)
        self.tabelaDisc.column('discCodigo', minwidth=0, width=100)
        self.tabelaDisc.column('discNome', minwidth=0, width=195)
        self.tabelaDisc.column('discCH', minwidth=0, width=50)
        self.tabelaDisc.heading('#0', text='', anchor=W)
        self.tabelaDisc.heading('grade', text='GRADE')
        self.tabelaDisc.heading('discCodigo', text='CODIGO DISC')
        self.tabelaDisc.heading('discNome', text='NOME DISC')
        self.tabelaDisc.heading('discCH', text='CH DISC')
        self.tabelaDisc.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        contChild=0
        contParent=0
        for grade in listaGrades:
            self.tabelaDisc.insert(parent='', index='end', iid=contParent, values=(grade.anoCurso))
            for disc in grade.disciplinas:
                contChild += 1
                self.tabelaDisc.insert(parent='', index='end', iid=contChild, values=('', disc['codigo'], disc['nome'], disc['cargaHoraria']))
                self.tabelaDisc.move(f'{contChild}', f'{contParent}', f'{contParent}')
            contParent = contChild+1
            contChild = contParent

        self.scroolLista = Scrollbar(self.frame2, orient='vertical')
        self.tabelaDisc.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.tabelaDisc.bind('<Double-1>', self.OnDoubleClick)
    
    def limpaGrade(self):
        self.comboboxGrade.delete(0, 'end')

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def OnDoubleClick(self, event):
        self.limpaGrade()
        self.tabelaDisc.selection()

        for n in self.tabelaDisc.selection():
            col1 = self.tabelaDisc.item(n, 'values')
            self.comboboxGrade.insert(END, col1)
    
    def getListaGradeCodDisc(self, anoCurso):
        listaGradeCodDisc = []
        for grade in self.listaGrade:
            if anoCurso == grade.anoCurso:
                for disc in grade.disciplinas:
                    listaGradeCodDisc.append(disc['codigo'])
                return listaGradeCodDisc

    def getListaGradeDisc(self, anoCurso):
        listaGradeDisc = []
        for grade in self.listaGrade:
            if anoCurso == grade.anoCurso:
                for disc in grade.disciplinas:
                    listaGradeDisc.append(disc)
                return listaGradeDisc
    
    def limparListBox(self):
        self.listboxRemove.delete(0, 'end')
        self.listboxAdd.delete(0, 'end')
    
    def IsPopularListbox(self, listaGradeCodDisc):
        for disc in listaGradeCodDisc:
            self.listboxRemove.insert(END, disc)
        return True
    
    def IsPopularListboxTodas(self, listaTodasDisciplinas, listaGradeCodDisc):
        for todas in listaTodasDisciplinas:
            if todas not in listaGradeCodDisc:
                self.listboxAdd.insert(END, todas)
        return True
    
    def popular(self, event):
        #para os listBox's
        self.limparListBox()
        comboAnoCurso = self.escolhaGrade.get()
        listaGradeCodDisc = self.getListaGradeCodDisc(comboAnoCurso)
        self.listaGradeDisc = self.getListaGradeDisc(comboAnoCurso)
        if self.testePopula == False:
            self.testePopula = self.IsPopularListbox(listaGradeCodDisc)
            self.IsPopularListboxTodas(self.listaDisc ,listaGradeCodDisc)
        else:
            self.limparListBox()
            self.IsPopularListbox(listaGradeCodDisc)
            self.IsPopularListboxTodas(self.listaDisc ,listaGradeCodDisc)

