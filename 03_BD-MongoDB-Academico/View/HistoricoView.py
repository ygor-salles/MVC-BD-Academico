from tkinter import *
from tkinter import ttk, messagebox

class LimiteHistorico():
    def __init__(self, controle, frame, listaMatricAlunos, listaDisciplinas):
        self.frame = frame
        self.listaDisciplinas = listaDisciplinas

        self.labelTitulo = Label(self.frame, text='CADASTRAR HISTÓRICO', bg='#dfe3ee', font=('Heveltica Bold', 14))
        self.labelTitulo.place(relx=0.25, rely=0.01, relwidth=0.5)

        self.labelMatric = Label(self.frame, text='Matrícula do aluno:', bg= '#dfe3ee', fg = '#107db2')
        self.labelMatric.place(relx=0.1, rely=0.1)
        self.escolhaMatric = StringVar()
        self.comboboxMatric = ttk.Combobox(self.frame, textvariable=self.escolhaMatric)
        self.comboboxMatric['values'] = listaMatricAlunos
        self.comboboxMatric.place(relx=0.1, rely=0.15, relwidth=0.25)

        self.labelAno = Label(self.frame, text='Ano: ',  bg= '#dfe3ee', fg = '#107db2')
        self.labelAno.place(relx=0.5, rely=0.1)
        self.inputAno = Entry(self.frame)
        self.inputAno.place(relx=0.5, rely=0.15, relwidth=0.20)

        self.labelSemestre = Label(self.frame, text='Semestre: ', bg= '#dfe3ee', fg = '#107db2')
        self.labelSemestre.place(relx=0.1, rely=0.30)
        self.valorSemestre = IntVar()
        self.radio1 = Radiobutton(self.frame, text='1', variable=self.valorSemestre, value='1', bg='#dfe3ee')
        self.radio1.place(relx=0.30, rely=0.3)
        self.radio2 = Radiobutton(self.frame, text='2', variable=self.valorSemestre, value='2', bg='#dfe3ee')
        self.radio2.place(relx=0.45, rely=0.3)

        self.labelDisc = Label(self.frame, text='Selecione as disciplinas que o aluno cursou no semetre', bg='#dfe3ee', fg='#107db2')
        self.labelDisc.place(relx=0.1, rely=0.40)
        self.listboxDisc = Listbox(self.frame)
        for disc in listaDisciplinas:
            self.listboxDisc.insert(END, disc.codigo)
        self.listboxDisc.place(relx=0.1, rely=0.45, relheight=0.30)

        self.labelNota = Label(self.frame, text='Nota do aluno na disciplina', bg='#dfe3ee', fg='#107db2')
        self.labelNota.place(relx=0.1, rely=0.80)
        self.inputNota = Entry(self.frame)
        self.inputNota.place(relx=0.1, rely=0.85, relwidth=0.2)
        
        self.buttonInserir = Button(self.frame, text='Inserir', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=controle.inserirHistorico)
        self.buttonInserir.place(relx=0.7, rely=0.85, relwidth=0.13, relheight=0.08)
        
        self.buttonCadastrar = Button(self.frame, text='Cadastrar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=controle.cadastrarSemestre)
        self.buttonCadastrar.place(relx=0.85, rely=0.85, relwidth=0.13, relheight=0.08)

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def limpaDiscNota(self):
        self.inputNota.delete(0, 'end')
        self.listboxDisc.delete(ACTIVE)

    def getDisciplinaByCode(self, codDisc):
        for disc in self.listaDisciplinas:
            if codDisc == disc.codigo:
                return disc
        return None