from tkinter import *
from tkinter import ttk, messagebox
from functools import partial

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
            self.listboxDisc.insert(END, disc['codigo'])
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
            if codDisc == disc['codigo']:
                return disc
        return None

class LimiteConsultaHistorico():
    def __init__(self, controle, frame, listaMatricAlunos):
        self.frame = frame

        self.labelTitulo = Label(self.frame, text='CONSULTAR/DELETAR HISTÓRICO', bg='#dfe3ee', font=('Heveltica Bold', 14))
        self.labelTitulo.place(relx=0.20, rely=0.01, relwidth=0.6)

        self.labelMatric = Label(self.frame, text='Matrícula do aluno:', bg= '#dfe3ee', fg = '#107db2')
        self.labelMatric.place(relx=0.1, rely=0.1)
        self.escolhaMatric = StringVar()
        self.comboboxMatric = ttk.Combobox(self.frame, textvariable=self.escolhaMatric)
        self.comboboxMatric['values'] = listaMatricAlunos
        self.comboboxMatric.place(relx=0.1, rely=0.15)

        self.buttonConsultar = Button(self.frame, text='Consultar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=partial(controle.consultaHistorico, self, frame))
        self.buttonConsultar.place(relx=0.45, rely=0.30, relwidth=0.13, relheight=0.08)
        
        self.buttonDeletar = Button(self.frame, text='Deletar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=controle.deletarHistorico)
        self.buttonDeletar.place(relx=0.6, rely=0.30, relwidth=0.13, relheight=0.08)
        
        self.buttonLimpar = Button(self.frame, text='Limpar', bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.limparConsulta)
        self.buttonLimpar.place(relx=0.75, rely=0.30, relwidth=0.13, relheight=0.08)

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def limparConsulta(self):
        self.comboboxMatric.delete(0, 'end')


class LimiterRelatorioHistorico():
    def __init__(self, frame, matric, nome, grade, historicos):
        self.janela = Toplevel()

        #deixar a janela centralizada
        window_height = 550
        window_width = 800
        screen_width = self.janela.winfo_screenwidth()
        screen_height = self.janela.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.janela.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        #adicionar imagem de ícone da janela
        self.janela.iconbitmap('./assets/school.ico')

        self.janela.title('RELATÓRIO DE HISTORICO DO ALUNO')
        self.janela.transient(frame)
        self.janela.focus_force()
        self.janela.grab_set()

        self.frameTitulo = Frame(self.janela)
        self.frameTitulo.pack()
        self.frameInit = Frame(self.janela)
        self.frameInit.pack()
        self.frameTable = Frame(self.janela)
        self.frameTable.pack()
        self.frameFinish = Frame(self.janela)
        self.frameFinish.pack()

        self.labelTitulo = Label(self.frameTitulo, text='HISTORICO DO ALUNO', font=('Heveltica Bold', 14)).pack(pady=30)

        self.labelMatric = Label(self.frameInit, text=f'MATRÍCULA: {matric}', width=200)
        self.labelMatric.pack()
        self.labelNome = Label(self.frameInit, text=f'NOME: {nome}', width=200)
        self.labelNome.pack()
        self.labelGrade = Label(self.frameInit, text=f'GRADE: {grade.anoCurso}', width=200)
        self.labelGrade.pack()

        self.listaDisc = ttk.Treeview(self.frameTable, column=('ano', 'semestre', 'codDisc', 'nomeDisc', 'chDisc', 'nota', 'status'), show='headings')
        self.listaDisc.column('ano', minwidth=0, width=50)
        self.listaDisc.column('semestre', minwidth=0, width=100)
        self.listaDisc.column('codDisc', minwidth=0, width=120)
        self.listaDisc.column('nomeDisc', minwidth=0, width=200)
        self.listaDisc.column('chDisc', minwidth=0, width=40)
        self.listaDisc.column('nota', minwidth=0, width=50)
        self.listaDisc.column('status', minwidth=0, width=100)
        self.listaDisc.heading('ano', text='ANO')
        self.listaDisc.heading('semestre', text='SEMESTRE')
        self.listaDisc.heading('codDisc', text='COD. DISC.')
        self.listaDisc.heading('nomeDisc', text='NOME DISC.')
        self.listaDisc.heading('chDisc', text='C.H.')
        self.listaDisc.heading('nota', text='NOTA')
        self.listaDisc.heading('status', text='STATUS')
        self.listaDisc.pack(pady=30)

        eletiva=0
        obrigatoria=0
        for his in historicos:
            for disc in his.discNotaStatus:
                self.listaDisc.insert('', 'end', values=(his.ano, his.semestre, disc['codigoDisciplina'], disc['nomeDisciplina'], disc['disciplinaCH'], disc['nota'], disc['status']))
                if (disc['obrigatorio'] == True):
                    obrigatoria += int(disc['disciplinaCH'])
                else:
                    eletiva += int(disc['disciplinaCH'])
        
        self.labelObrigatoria = Label(self.frameFinish, text=f'TOTAL DE CARGA HORÁRIA OBRIGATÓRIA: {obrigatoria}', width=200)
        self.labelObrigatoria.pack()
        self.labelEletiva = Label(self.frameFinish, text=f'TOTAL DE CARGA HORÁRIA ELETIVA: {eletiva}', width=200)
        self.labelEletiva.pack()