import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Aluno as al
import Grade as gr
import os.path
import pickle

class CursoNaoCadastrado(Exception):
    pass

class CamposNaoPreenchidos(Exception):
    pass

class Curso:
    def __init__(self, nome, listaAlunos, grade):
        self.__nome = nome
        self.__listaAlunos = listaAlunos
        self.__grade = grade
    
    def getNome(self):
        return self.__nome

    def getListaAlunos(self):
        return self.__listaAlunos
    
    def getGrade(self):
        return self.__grade
    
    def setGrade(self, grade):
        self.__grade = grade

class LimiteInsereCurso():
    def __init__(self, controle, root, listaGradeAnoCurso, listaNroMatric):
        self.janela=root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='CADASTRAR CURSO', font=('Heveltica Bold', 14), bg='#76cb69').pack()
        
        self.labelNomeCurso = tk.Label(self.frameBody,text="Nome do curso: ", bg='#76cb69')
        self.inputNomeCurso = tk.Entry(self.frameBody, width=30)
        
        self.labelGrade = tk.Label(self.frameBody,text="Escolha a grade: ", bg='#76cb69')
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameBody, width = 15 , textvariable = self.escolhaCombo)
        self.combobox['values'] = listaGradeAnoCurso
          
        self.labelAluno = tk.Label(self.frameBody,text="Alunos sem matrícula\n em curso .. Matricular: ", bg='#76cb69') 
        self.listbox = tk.Listbox(self.frameBody)
        for nro in listaNroMatric:
            self.listbox.insert(tk.END, nro)

        self.buttonInsere = tk.Button(self.frameBody ,text="Insere aluno")           
        self.buttonInsere.bind("<Button>", controle.insereAluno)
        self.buttonCria = tk.Button(self.frameBody ,text="Cria Curso")           
        self.buttonCria.bind("<Button>", controle.criaCurso)

        self.labelNomeCurso.grid(row=0, column=0, sticky='W', pady=20)    
        self.inputNomeCurso.grid(row=0, column=1, sticky='W', pady=20)    
        self.labelGrade.grid(row=1, column=0, sticky='W', pady=20)    
        self.combobox.grid(row=1, column=1, sticky='W', pady=20)    
        self.labelAluno.grid(row=2, column=1, sticky='W')    
        self.listbox.grid(row=3, column=1, sticky='W')    
        self.buttonInsere.grid(row=4, column=2, sticky='W', pady=20)    
        self.buttonCria.grid(row=4, column=3, sticky='W', pady=20)    

    def mostraMessagebox(self, titulo, msg):
        messagebox.showinfo(titulo, msg)            

class LimiteMostraCursos():
    def __init__(self, str):
        messagebox.showinfo('Lista de Cursos', str)

class LimiteConsultaCursos():
    def __init__(self, controle, root):
        self.janela=root
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='CONSULTAR CURSO', font=('Heveltica Bold', 14), bg='#76cb69').pack()
    
        self.labelNome = tk.Label(self.frameBody, text='Curso: ', bg='#76cb69')
        self.inputTextNome = tk.Entry(self.frameBody, width=20)

        self.buttonConsultar = tk.Button(self.frameBody, text='Realizar Consulta')
        self.buttonConsultar.bind('<Button>', controle.consultaHandler)
        self.buttonClear = tk.Button(self.frameBody ,text='Clear')      
        self.buttonClear.bind('<Button>', controle.clearConsulta)  
        self.buttonFecha = tk.Button(self.frameBody ,text='Finalizar')      
        self.buttonFecha.bind('<Button>', controle.fechaConsulta)

        self.labelNome.grid(row=0, column=0, sticky='W', pady=20)
        self.inputTextNome.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonConsultar.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=1, column=4, sticky='W', pady=20)
    
    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class LimiteExcluiCursos():
    def __init__(self, controle, root):
        self.janela=root    
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='EXCLUIR CURSO', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelNome = tk.Label(self.frameBody, text='Curso: ', bg='#76cb69')
        self.inputTextNome = tk.Entry(self.frameBody, width=20)

        self.buttonConsultar = tk.Button(self.frameBody, text='Excluir curso')
        self.buttonConsultar.bind('<Button>', controle.excluiHandler)
        self.buttonClear = tk.Button(self.frameBody ,text='Clear')      
        self.buttonClear.bind('<Button>', controle.clearExclusao)  
        self.buttonFecha = tk.Button(self.frameBody ,text='Finalizar')      
        self.buttonFecha.bind('<Button>', controle.fechaExclusao)

        self.labelNome.grid(row=0, column=0, sticky='W', pady=20)
        self.inputTextNome.grid(row=0, column=1, sticky='W', pady=20)
        self.buttonConsultar.grid(row=1, column=2, sticky='W', pady=20)
        self.buttonClear.grid(row=1, column=3, sticky='W', pady=20)
        self.buttonFecha.grid(row=1, column=4, sticky='W', pady=20)
    
    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class LimiteAtualizaCursos():
    def __init__(self, controle, root, listaCursos, listaAnoGrade):
        self.janela=root    
        self.frameTitulo = tk.Frame(self.janela)
        self.frameTitulo.pack()
        self.frameBody = tk.Frame(self.janela)
        self.frameBody.pack()
        self.frameBody.configure(bg='#76cb69')
        self.labelTitulo = tk.Label(self.frameTitulo, text='ATUALIZAR CURSO', font=('Heveltica Bold', 14), bg='#76cb69').pack()

        self.labelCurso = tk.Label(self.frameBody, text='Escolha o curso: ', bg='#76cb69')
        self.escolhaCurso = tk.StringVar()
        self.comboboxCurso = ttk.Combobox(self.frameBody, width=30, textvariable=self.escolhaCurso)
        self.comboboxCurso['values'] = listaCursos
        self.comboboxCurso.bind('<<ComboboxSelected>>', controle.exibir)

        self.labelAnoGrade = tk.Label(self.frameBody, text='Alterar Ano/Grade:', bg='#76cb69')
        self.escolhaAnoGrade = tk.StringVar()
        self.comboboxAnoGrade = ttk.Combobox(self.frameBody, width=15, textvariable=self.escolhaAnoGrade)
        self.comboboxAnoGrade['values'] = listaAnoGrade

        self.buttonAlteraGrade = tk.Button(self.frameBody, text='Alterar Grade')
        self.buttonAlteraGrade.bind('<Button>', controle.alteraGrade)

        self.labelMatriculado = tk.Label(self.frameBody, text='Remover Alunos', bg='#76cb69')
        self.listboxMatriculado = tk.Listbox(self.frameBody)

        self.labelSemMatricula = tk.Label(self.frameBody, text='Adicionar Alunos', bg='#76cb69')
        self.listboxSemMatricula = tk.Listbox(self.frameBody)

        self.buttonRemove = tk.Button(self.frameBody, text='Remove Aluno')
        self.buttonRemove.bind('<Button>', controle.remove)
        self.buttonAdiciona = tk.Button(self.frameBody, text='Adiciona Aluno')
        self.buttonAdiciona.bind('<Button>', controle.adiciona)
        self.buttonFecha = tk.Button(self.frameBody, text='Fechar')
        self.buttonFecha.bind('<Button>', controle.fecharAtualizacao)

        self.labelCurso.grid(row=0, column=0, sticky='W', pady=15)
        self.comboboxCurso.grid(row=0, column=1, sticky='W', pady=15)
        self.labelAnoGrade.grid(row=1, column=0, sticky='W', pady=15)
        self.comboboxAnoGrade.grid(row=1, column=1, sticky='W', pady=15)
        self.buttonAlteraGrade.grid(row=1, column=2, sticky='W', pady=15)
        self.labelMatriculado.grid(row=2, column=1, sticky='W')
        self.listboxMatriculado.grid(row=3, column=1, sticky='W')
        self.labelSemMatricula.grid(row=2, column=2, sticky='W')
        self.listboxSemMatricula.grid(row=3, column=2, sticky='W')
        self.buttonRemove.grid(row=4, column=1, sticky='W', pady=15)
        self.buttonAdiciona.grid(row=4, column=2, sticky='W', pady=15)
        self.buttonFecha.grid(row=4, column=3, sticky='W', pady=15)
    
    def limparListbox(self):
        self.listboxMatriculado.delete(0, 'end')
        self.listboxSemMatricula.delete(0, 'end')
    
    def isPopularListboxMatriculado(self, alunos):
        for aluno in alunos:
            self.listboxMatriculado.insert(tk.END, aluno.getNroMatric())
        return True
    
    def isPopularListboxSemMatricula(self, alunos):
        for aluno in alunos:
            self.listboxSemMatricula.insert(tk.END, aluno)
        return True

    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class CtrlCurso():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaAlunosCurso = []
        self.testePopula = False

        if not os.path.isfile("Curso.pickle"):
            self.listaCursos =  []
        else:
            with open("Curso.pickle", "rb") as f:
                self.listaCursos = pickle.load(f)

    #Função para persistencia de dados ---------------------------------------------
    
    def salvaCursos(self):
        if len(self.listaCursos) != 0:
            with open("Curso.pickle","wb") as f:
                pickle.dump(self.listaCursos, f)

    # Funções Auxiliares ----------------------------------------------------------
    
    def verificaAluno(self, nroMatric):
        alunoRet = nroMatric
        for curso in self.listaCursos:
            for aluno in curso.getListaAlunos():
                if aluno.getNroMatric() == nroMatric:
                    alunoRet = None
        return alunoRet

    def getCurso(self, nomeCurso):
        cursoRet = None
        for curso in self.listaCursos:
            if curso.getNome() == nomeCurso:
                cursoRet = curso
        return cursoRet

    def getListaNomeCurso(self):
        nomeCurso = []
        for cur in self.listaCursos:
            nomeCurso.append(cur.getNome())
        return nomeCurso

    def getAlunosCurso(self, comboCurso):
        alunosCurso = []
        for curso in self.listaCursos:
            if comboCurso == curso.getNome():
                return curso.getListaAlunos()

    def getIndiceAnoGrade(self, comboCurso):
        indice = 0
        for curso in self.listaCursos:
            if comboCurso == curso.getNome():
                return indice
            indice += 1

    def getAlunoCurso(self, matricAluno, nomeCurso):
        for curs in self.listaCursos:
            if nomeCurso == curs.getNome():
                for aluno in curs.getListaAlunos():
                    if aluno.getNroMatric() == matricAluno:
                        return aluno

    # Funções instancioadores, recebe da main ---------------------------

    def insereCursos(self, root):
        self.listaAlunosCurso = []
        listaGradeAnoCurso = self.ctrlPrincipal.ctrlGrade.getListaGradeAnoCurso()
        #Para inserir no listbox apenas alunos que não estão matriculados em outro curso
        listaMatricExclusiva = []
        for matric in self.ctrlPrincipal.ctrlAluno.getListaNroMatric():
            listaMatricExclusiva.append(self.verificaAluno(matric))
        
        self.limiteIns = LimiteInsereCurso(self, root, listaGradeAnoCurso, listaMatricExclusiva)

    def mostraCursos(self):
        string = ''
        for curso in self.listaCursos:
            string += 'Nome do Curso: '+curso.getNome()+'\n'
            string += 'Grade: '+curso.getGrade().getAnoCurso()+'\n'
            string += 'Listagem de alunos matriculados: \n'
            for aluno in curso.getListaAlunos():
                string += aluno.getNroMatric() + ' - ' + aluno.getNome() + '\n'
            string += '------------------------------------------------\n'
        self.limiteMostra = LimiteMostraCursos(string)
    
    def consultaCursos(self, root):
        self.limiteConsulta = LimiteConsultaCursos(self, root)

    def excluiCursos(self, root):
        self.limiteExclui = LimiteExcluiCursos(self, root)
    
    def atualizaCursos(self, root):
        listaCursos = self.getListaNomeCurso()
        listaGradeAnoCurso = self.ctrlPrincipal.ctrlGrade.getListaGradeAnoCurso()
        self.limiteAtualiza = LimiteAtualizaCursos(self, root, listaCursos, listaGradeAnoCurso)

    #Funções de Buttons da Tela Insere Curso ------------------------------------------------------------
    
    def insereAluno(self, event):
        nomeCurso = self.limiteIns.inputNomeCurso.get()
        gradeSelecionada = self.limiteIns.escolhaCombo.get()
        alunoSelecionado = self.limiteIns.listbox.get(tk.ACTIVE)
        try:
            if len(nomeCurso)==0 or len(gradeSelecionada)==0 or len(alunoSelecionado)==0:
                raise CamposNaoPreenchidos()
            if alunoSelecionado in self.listaCursos:
                raise AlunoCadastradoEmOutroCurso()
        except CamposNaoPreenchidos:
            messagebox.showerror('Atenção', 'Todos os campos deve ser preenchidos')
        else:
            aluno = self.ctrlPrincipal.ctrlAluno.getAluno(alunoSelecionado)
            self.listaAlunosCurso.append(aluno)
            self.limiteIns.mostraMessagebox('Sucesso', 'Aluno Matriculado no Curso')
            self.limiteIns.listbox.delete(tk.ACTIVE)

    def criaCurso(self, event):
        nomeCurso = self.limiteIns.inputNomeCurso.get()
        gradeSelecionada = self.limiteIns.escolhaCombo.get()        
        grade = self.ctrlPrincipal.ctrlGrade.getGrade(gradeSelecionada)
        curso = Curso(nomeCurso, self.listaAlunosCurso, grade)
        self.listaCursos.append(curso)
        self.limiteIns.mostraMessagebox('Sucesso', 'Alunos matriculados no curso {} com sucesso'.format(nomeCurso))
        self.limiteIns.janela.destroy()     

    # Funções do Buttons de consulta do Curso -------------------------------------------------------

    def consultaHandler(self, event):
        nome = self.limiteConsulta.inputTextNome.get()
        encontrou=False
        try:
            if len(nome)==0:
                raise CamposNaoPreenchidos()    
            string = ''
            for curso in self.listaCursos:
                if nome == curso.getNome():
                    encontrou=True
                    string += 'Nome: '+curso.getNome()+'\n'
                    string += 'Grade: '+curso.getGrade().getAnoCurso()+'\n'
                    string += 'Listagem de alunos matriculados: \n'
                    for aluno in curso.getListaAlunos():
                        string += aluno.getNroMatric() + ' - ' + aluno.getNome() + '\n'
                    break
            if encontrou==False:
                raise CursoNaoCadastrado()
        except CamposNaoPreenchidos:
            messagebox.showerror('Atenção', 'Todos os campos devem ser preenchidos!')
        except CursoNaoCadastrado:
            messagebox.showerror('Error', 'Curso não cadastrado!')
        else:
            LimiteMostraCursos(string)
        finally:
            self.clearConsulta(event)
    
    def clearConsulta(self, event):
        self.limiteConsulta.inputTextNome.delete(0, len(self.limiteConsulta.inputTextNome.get()))

    def fechaConsulta(self, event):
        self.limiteConsulta.janela.destroy()

    # Funções do Buttons de exclusão do Curso -------------------------------------------------------

    def excluiHandler(self, event):
        nomeCurso = self.limiteExclui.inputTextNome.get()
        curso = self.getCurso(nomeCurso)
        try:
            if len(nomeCurso)==0:
                raise CamposNaoPreenchidos()
            elif curso == None:
                raise CursoNaoCadastrado()
        except CamposNaoPreenchidos:
            messagebox.showerror('Atenção', 'Todos os campos devem ser preenchidos')
        except CursoNaoCadastrado:
            messagebox.showerror('Alerta', 'Curso não cadastrado')
        else:
            self.listaCursos.remove(curso)
            self.limiteExclui.mostraMessagebox('Sucesso', 'Curso removido com sucesso')
            self.clearExclusao(event)            

    def clearExclusao(self, event):
        self.limiteExclui.inputTextNome.delete(0, 'end')
    
    def fechaExclusao(self, event):
        self.limiteExclui.janela.destroy()

    # Funções do Buttons de atualização do Curso -------------------------------------------------------

    def exibir(self, event):
        comboCurso = self.limiteAtualiza.comboboxCurso.get()
        self.listaAlunosCurso = self.getAlunosCurso(comboCurso)
        listaMatricExclusiva = []
        indice = self.getIndiceAnoGrade(comboCurso)
        for matric in self.ctrlPrincipal.ctrlAluno.getListaNroMatric():
            listaMatricExclusiva.append(self.verificaAluno(matric))
        if self.testePopula == False:
            self.testePopula = self.limiteAtualiza.isPopularListboxMatriculado(self.listaAlunosCurso)
            self.limiteAtualiza.isPopularListboxSemMatricula(listaMatricExclusiva)
            self.limiteAtualiza.comboboxAnoGrade.current(indice)
        else:
            self.limiteAtualiza.limparListbox()
            self.limiteAtualiza.isPopularListboxMatriculado(self.listaAlunosCurso)
            self.limiteAtualiza.isPopularListboxSemMatricula(listaMatricExclusiva)
            self.limiteAtualiza.comboboxAnoGrade.current(indice)

    def remove(self, event):
        nomeCurso = self.limiteAtualiza.escolhaCurso.get()
        alunoSelecionado = self.limiteAtualiza.listboxMatriculado.get(tk.ACTIVE)
        aluno = self.getAlunoCurso(alunoSelecionado, nomeCurso)
        self.listaAlunosCurso.remove(aluno)
        self.limiteAtualiza.mostraMessagebox('Atualização', 'Aluno removido com sucesso')
        self.exibir(event)
    
    def adiciona(self, event):
        alunoSelecionado = self.limiteAtualiza.listboxSemMatricula.get(tk.ACTIVE)
        aluno = self.ctrlPrincipal.ctrlAluno.getAluno(alunoSelecionado)
        self.listaAlunosCurso.append(aluno)
        self.limiteAtualiza.mostraMessagebox('Atualização', 'Aluno inserido com sucesso')
        self.exibir(event)

    def alteraGrade(self, event):
        nomeCurso = self.limiteAtualiza.escolhaCurso.get()
        anoCurso = self.limiteAtualiza.escolhaAnoGrade.get()
        grade = self.ctrlPrincipal.ctrlGrade.getGrade(anoCurso)
        for curs in self.listaCursos:
            if nomeCurso == curs.getNome():
                curs.setGrade(grade)
        self.limiteAtualiza.mostraMessagebox('Sucesso', 'Grade alterada com sucesso')
        self.exibir(event)

    def fecharAtualizacao(self, event):
        self.limiteAtualiza.janela.destroy()
