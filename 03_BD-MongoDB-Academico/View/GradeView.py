from tkinter import *
from tkinter import ttk, messagebox

class LimiteGrade():
    def __init__(self, controle, frame1, frame2, listaGrades, listaDisc):
        self.frame1 = frame1
        self.frame2 = frame2

        self.labelTitulo = Label(self.frame1, text='GRADES', bg='#dfe3ee', font=('Heveltica Bold', 14))
        self.labelTitulo.place(relx=0.38, rely=0.01, relwidth=0.2)

        self.labelGrade = Label(self.frame1, text='ANO/CURSO - (2017/SIN)', bg= '#dfe3ee', fg = '#107db2')
        self.labelGrade.place(relx=0.05, rely=0.15)
        self.inputGrade = Entry(self.frame1)
        self.inputGrade.place(relx=0.05, rely=0.25, relwidth=0.4)

        self.labelDisc = Label(self.frame1, text='Disciplinas',  bg= '#dfe3ee', fg = '#107db2')
        self.labelDisc.place(relx=0.55, rely=0.15)
        self.listboxDisc = Listbox(self.frame1)
        for disc in listaDisc:
            self.listboxDisc.insert(END, disc.codigo)
        self.listboxDisc.place(relx=0.55, rely=0.25, relheight=0.70)
        
        self.buttonBuscar = Button(self.frame1, text='Buscar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command = controle.buscaGrade)
        self.buttonBuscar.place(relx=0.05, rely=0.80, relwidth=0.1, relheight=0.15)

        self.buttonLimpar = Button(self.frame1, text= 'Limpar', bd=2, bg = '#107db2',fg = 'white', 
                                font = ('verdana', 8, 'bold'), command= self.limpaGrade)
        self.buttonLimpar.place(relx= 0.15, rely=0.80, relwidth=0.1, relheight= 0.15)

        self.buttonAlterar = Button(self.frame1, text='Alterar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=controle.alteraGrade)
        self.buttonAlterar.place(relx=0.3, rely=0.80, relwidth=0.1, relheight=0.15)
        
        self.buttonDeletar = Button(self.frame1, text='Apagar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=controle.deletaGrade)
        self.buttonDeletar.place(relx=0.4, rely=0.80, relwidth=0.1, relheight=0.15)

        self.buttonInserir = Button(self.frame1, text='Inserir', bd=2, bg = '#107db2',fg = 'white',
                            font = ('verdana', 8, 'bold'), command=controle.insereGrade)
        self.buttonInserir.place(relx=0.77, rely=0.80, relwidth=0.1, relheight=0.15)
        
        self.buttonInserir = Button(self.frame1, text='Cadastrar', bd=2, bg = '#107db2',fg = 'white',
                            font = ('verdana', 8, 'bold'), command=controle.cadastraGrade)
        self.buttonInserir.place(relx=0.89, rely=0.80, relwidth=0.1, relheight=0.15)

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
        