from tkinter import *
from tkinter import ttk, messagebox

class LimiteDisciplina():
    def __init__(self, controle, frame1, frame2):
        self.frame1 = frame1
        self.frame2 = frame2

        self.canvas_bt = Canvas(self.frame1, bd=0, bg='#1e3743', highlightbackground = 'gray',
            highlightthickness=5)
        self.canvas_bt.place(relx= 0.19, rely= 0.08, relwidth= 0.22, relheight=0.19)

        ### Criação do botao limpar
        self.bt_limpar = Button(self.frame1, text= "Limpar", bd=2, bg = '#107db2',fg = 'white',
                                activebackground='#108ecb', activeforeground="white"
                                , font = ('verdana', 8, 'bold'), command= self.limpaDisciplina)
        self.bt_limpar.place(relx= 0.2, rely=0.1, relwidth=0.1, relheight= 0.15)
        ### Criação do botao buscar
        self.bt_limpar = Button(self.frame1, text="Buscar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command = self.buscaDisciplina)
        self.bt_limpar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        ### Criação do botao alterar
        self.bt_limpar = Button(self.frame1, text="Alterar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.alteraDisciplina)
        self.bt_limpar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao apagar
        self.bt_limpar = Button(self.frame1, text="Apagar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.deletaDisciplina)
        self.bt_limpar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        ## Criação da label e entrada do codigo
        self.lb_codigo = Label(self.frame1, text = "Código", bg= '#dfe3ee', fg = '#107db2')
        self.lb_codigo.place(relx= 0.05, rely= 0.05 )

        self.codigo_entry = Entry(self.frame1 )
        self.codigo_entry.place(relx= 0.05, rely= 0.15, relwidth= 0.08)

        ## Criação da label e entrada do nome
        self.lb_nome = Label(self.frame1, text="Nome", bg= '#dfe3ee', fg = '#107db2')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        ## Criação da label e entrada do telefone
        self.lb_nome = Label(self.frame1, text="Telefone", bg= '#dfe3ee', fg = '#107db2')
        self.lb_nome.place(relx=0.05, rely=0.6)

        self.fone_entry = Entry(self.frame1)
        self.fone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        ## Criação da label e entrada da cidade
        self.lb_nome = Label(self.frame1, text="Cidade", bg= '#dfe3ee', fg = '#107db2')
        self.lb_nome.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

        self.listaCli = ttk.Treeview(self.frame2, height=3,
                                     column=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        # self.listaCli.bind("<Double-1>", self.OnDoubleClick)

    def limpaDisciplina(self, event):
        print('Limpa disciplina')

    def buscaDisciplina(self, event):
        print('Busca disciplina')

    def alteraDisciplina(self, event):
        print('Altera disciplina')

    def deletaDisciplina(self, event):
        print('Deleta disciplina')

