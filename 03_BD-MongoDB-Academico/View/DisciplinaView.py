from tkinter import *
from tkinter import ttk, messagebox

class LimiteDisciplina():
    def __init__(self, controle, frame1, frame2, listaDisciplinas):
        self.frame1 = frame1
        self.frame2 = frame2

        self.labelTitulo = Label(self.frame1, text='DISCIPLINAS', bg='#dfe3ee', font=('Heveltica Bold', 14))
        self.labelTitulo.place(relx=0.38, rely=0.01, relwidth=0.2)

        self.labelNome = Label(self.frame1, text='Nome disciplina', bg= '#dfe3ee', fg = '#107db2')
        self.labelNome.place(relx=0.05, rely=0.1)
        self.inputNome = Entry(self.frame1)
        self.inputNome.place(relx=0.05, rely=0.2, relwidth=0.85)

        self.labelCodigo = Label(self.frame1, text='Código', bg= '#dfe3ee', fg = '#107db2')
        self.labelCodigo.place(relx=0.05, rely=0.35)
        self.inputCodigo = Entry(self.frame1)
        self.inputCodigo.place(relx=0.05, rely=0.45, relwidth=0.4)

        self.labelCargaHoraria = Label(self.frame1, text='Carga Horaria', bg= '#dfe3ee', fg = '#107db2')
        self.labelCargaHoraria.place(relx=0.5, rely=0.35)
        self.inputCargaHoraria = Entry(self.frame1)
        self.inputCargaHoraria.place(relx=0.5, rely=0.45, relwidth=0.4)
        
        self.buttonBuscar = Button(self.frame1, text='Buscar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command = controle.buscaDisciplina)
        self.buttonBuscar.place(relx=0.05, rely=0.7, relwidth=0.1, relheight=0.15)

        self.buttonLimpar = Button(self.frame1, text= 'Limpar', bd=2, bg = '#107db2',fg = 'white', 
                                font = ('verdana', 8, 'bold'), command= self.limpaDisciplina)
        self.buttonLimpar.place(relx= 0.15, rely=0.7, relwidth=0.1, relheight= 0.15)

        self.buttonInserir = Button(self.frame1, text='Inserir', bd=2, bg = '#107db2',fg = 'white',
                            font = ('verdana', 8, 'bold'), command=controle.insereDisciplina)
        self.buttonInserir.place(relx=0.58, rely=0.7, relwidth=0.1, relheight=0.15)

        self.buttonAlterar = Button(self.frame1, text='Alterar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=controle.alteraDisciplina)
        self.buttonAlterar.place(relx=0.7, rely=0.7, relwidth=0.1, relheight=0.15)
        
        self.buttonDeletar = Button(self.frame1, text='Apagar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=controle.deletaDisciplina)
        self.buttonDeletar.place(relx=0.8, rely=0.7, relwidth=0.1, relheight=0.15)

        self.tabelaDisc = ttk.Treeview(self.frame2, column=('codigo', 'nome', 'ch'), show='headings')
        self.tabelaDisc.column('codigo', minwidth=0, width=100)
        self.tabelaDisc.column('nome', minwidth=0, width=250)
        self.tabelaDisc.column('ch', minwidth=0, width=50, anchor=CENTER)
        self.tabelaDisc.heading('codigo', text='CODIGO')
        self.tabelaDisc.heading('nome', text='NOME')
        self.tabelaDisc.heading('ch', text='CH')
        self.tabelaDisc.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        for disc in listaDisciplinas:
            self.tabelaDisc.insert('', 'end', values=(disc.codigo, disc.nome, disc.cargaHoraria))

        self.scroolLista = Scrollbar(self.frame2, orient='vertical')
        self.tabelaDisc.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.tabelaDisc.bind('<Double-1>', self.OnDoubleClick)

    def limpaDisciplina(self):
        self.inputCodigo.config(state=NORMAL)
        self.inputCodigo.delete(0, 'end')
        self.inputNome.delete(0, 'end')
        self.inputCargaHoraria.delete(0, 'end')

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def OnDoubleClick(self, event):
        self.inputCodigo.config(state=NORMAL)
        self.limpaDisciplina()
        self.tabelaDisc.selection()

        for n in self.tabelaDisc.selection():
            col1, col2, col3 = self.tabelaDisc.item(n, 'values')
            self.inputCodigo.insert(END, col1)
            self.inputCodigo.config(state=DISABLED)
            self.inputNome.insert(END, col2)
            self.inputCargaHoraria.insert(END, col3)
        