import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from functools import partial

class LimiteInsereHistorico():
    def __init__(self, controle, root, listaDisc, listaMatricAluno):
        self.janela = root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='CADASTRAR HISTÓRICO DO ALUNO', font=('Heveltica Bold', 14), bg='#76cb69').pack()
    
        self.labelAluno = tk.Label(self.frameBody, text='Nro Matricula do Aluno: ', bg='#76cb69')
        self.labelSemestre = tk.Label(self.frameBody, text='Informe Semestre: ', bg='#76cb69')
        self.labelAno = tk.Label(self.frameBody, text='Informe o ano: ', bg='#76cb69')
        self.labelListaDisc = tk.Label(self.frameBody, text='Selecione as disciplinas \nque o aluno cursou\n no semestre: ', bg='#76cb69')
        self.labelNota = tk.Label(self.frameBody, text='Nota do Aluno na Disciplina: ', bg='#76cb69')

        self.comboAluno = tk.StringVar()
        self.comboboxAluno = ttk.Combobox(self.frameBody, width=15, textvariable=self.comboAluno)
        self.comboboxAluno['values'] = listaMatricAluno

        self.valor = tk.IntVar()
        self.radio1 = tk.Radiobutton(self.frameBody, text='1', variable=self.valor, value=1, bg='#76cb69')
        self.radio2 = tk.Radiobutton(self.frameBody, text='2', variable=self.valor, value=2, bg='#76cb69')

        self.inputAno = tk.Entry(self.frameBody, width=10)
        
        self.listboxDisciplina = tk.Listbox(self.frameBody)
        for disc in listaDisc:
            self.listboxDisciplina.insert(tk.END, disc)

        self.inputNota = tk.Entry(self.frameBody, width=10)

        self.buttonInsere = tk.Button(self.frameBody, text='Insere Disciplina no Histórico')
        self.buttonInsere.bind('<Button>', controle.insereDisciplina)
        self.buttonCria = tk.Button(self.frameBody, text='Criar Semestre')
        self.buttonCria.bind('<Button>', controle.criaSemestre)

        self.labelAluno.grid(row=0, column=0, sticky='W', pady=15)
        self.comboboxAluno.grid(row=0, column=1, sticky='W', pady=5)
        self.labelSemestre.grid(row=1, column=0, sticky='W', pady=5)
        self.radio1.grid(row=1, column=1, sticky='W', pady=5)
        self.radio2.grid(row=1, column=2, sticky='W', pady=5)
        self.labelAno.grid(row=2, column=0, sticky='W', pady=5)
        self.inputAno.grid(row=2, column=1, sticky='W')
        self.labelListaDisc.grid(row=3, column=1, sticky='W')
        self.listboxDisciplina.grid(row=4, column=1, sticky='W', pady=5)
        self.labelNota.grid(row=5, column=0, sticky='W', pady=5)
        self.inputNota.grid(row=5, column=1, sticky='W', pady=5)
        self.buttonInsere.grid(row=6, column=2, sticky='W', pady=5)
        self.buttonCria.grid(row=6, column=3, sticky='W', pady=5)

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

class LimiteMostraHistorico():
    def __init__(self, titulo, msg, erro):
        if erro:
            messagebox.showerror(titulo, msg)
        else:
            messagebox.showinfo(titulo, msg)

class LimiteConsultaHistorico():
    def __init__(self, controle, root):
        self.janela = root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='CONSULTAR HISTÓRICO DO ALUNO', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelMatricAluno = tk.Label(self.frameBody, text='Matricula do Aluno: ', bg='#76cb69')
        self.inputMatricAluno = tk.Entry(self.frameBody, width=15)

        self.buttonConsulta = tk.Button(self.frameBody, text='Enter', command=partial(controle.enterConsulta, self, root))
        self.buttonClear = tk.Button(self.frameBody, text='Clear')
        self.buttonClear.bind('<Button>', self.clearConsulta)
        self.buttonFinaliza = tk.Button(self.frameBody, text='Finalizar')
        self.buttonFinaliza.bind('<Button>', self.finalizaConsulta)

        self.labelMatricAluno.grid(row=0, column=0, sticky='W', pady=20)
        self.inputMatricAluno.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonConsulta.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFinaliza.grid(row=1, column=4, sticky='W', pady=20)

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def clearConsulta(self, event):
        self.inputMatricAluno.delete(0, len(self.inputMatricAluno.get()))
    
    def finalizaConsulta(self, event):
        self.janela.destroy()

class LimiteRelatorioHistorico():
    def __init__(self, root, matric, nome, grade, historicos):
        self.janela = tk.Toplevel()

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
        self.janela.transient(root)
        self.janela.focus_force()
        self.janela.grab_set()

        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameInit = tk.Frame(self.janela)
        self.frameInit.pack()
        self.frameTable = tk.Frame(self.janela)
        self.frameTable.pack()
        self.frameFinish = tk.Frame(self.janela)
        self.frameFinish.pack()

        self.labelTitulo = tk.Label(self.frameTitulo, text='HISTORICO DO ALUNO', font=('Heveltica Bold', 14)).pack(pady=30)

        self.labelMatric = tk.Label(self.frameInit, text=f'MATRÍCULA: {matric}', width=200)
        self.labelMatric.pack(pady=2)
        self.labelNome = tk.Label(self.frameInit, text=f'NOME: {nome}', width=200)
        self.labelNome.pack(pady=2)
        self.labelGrade = tk.Label(self.frameInit, text=f'GRADE: {grade.ano}/{grade.curso_id}', width=200)
        self.labelGrade.pack(pady=2)

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
            for disc in his.disciplinas:
                self.listaDisc.insert('', 'end', values=(his.ano, his.semestre, disc.disciplinas.codigo, disc.disciplinas.nome, disc.disciplinas.carga_horaria, disc.nota_disciplina, disc.status))
                if (disc.obrigatorio == True):
                    obrigatoria += int(disc.disciplinas.carga_horaria)
                else:
                    eletiva += int(disc.disciplinas.carga_horaria)
        
        self.labelObrigatoria = tk.Label(self.frameFinish, text=f'TOTAL DE CARGA HORÁRIA OBRIGATÓRIA: {obrigatoria}', width=200)
        self.labelObrigatoria.pack(pady=2)
        self.labelEletiva = tk.Label(self.frameFinish, text=f'TOTAL DE CARGA HORÁRIA ELETIVA: {eletiva}', width=200)
        self.labelEletiva.pack(pady=2)

class LimiteExcluiHistorico():
    def __init__(self, controle, root):
        self.janela = root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='EXCLUIR HISTÓRICO DO ALUNO', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelMatricAluno = tk.Label(self.frameBody, text='Matricula do Aluno: ', bg='#76cb69')
        self.inputMatricAluno = tk.Entry(self.frameBody, width=15)

        self.buttonConsulta = tk.Button(self.frameBody, text='Excluir')
        self.buttonConsulta.bind('<Button>', controle.excluiHandler)
        self.buttonClear = tk.Button(self.frameBody, text='Clear')
        self.buttonClear.bind('<Button>', self.clearExclusao)
        self.buttonFinaliza = tk.Button(self.frameBody, text='Finalizar')
        self.buttonFinaliza.bind('<Button>', self.finalizaExclusao)

        self.labelMatricAluno.grid(row=0, column=0, sticky='W', pady=20)
        self.inputMatricAluno.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonConsulta.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFinaliza.grid(row=1, column=4, sticky='W', pady=20)

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)

    def clearExclusao(self, event):
        self.inputMatricAluno.delete(0, 'end')
    
    def finalizaExclusao(self, event):
        self.janela.destroy()