import os.path
import pickle
from View.CursoView import *
from Model.CursoModel import Curso

class CursoNaoCadastrado(Exception):
    pass

class CamposNaoPreenchidos(Exception):
    pass

class AlunoCadastradoEmOutroCurso(Exception):
    pass

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

    #Funções de CRUD dos Buttons ----------------------------------------------------

    #Inserção -----------------------------------------
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
            self.limiteIns.mostraMessagebox('Atenção', 'Todos os campos deve ser preenchidos', True)
        except AlunoCadastradoEmOutroCurso:
            self.limiteIns.mostraMessagebox('Atenção', 'Esse aluno está cadastrado em outro curso', True)
        else:
            aluno = self.ctrlPrincipal.ctrlAluno.getAluno(alunoSelecionado)
            self.listaAlunosCurso.append(aluno)
            self.limiteIns.mostraMessagebox('Sucesso', 'Aluno Matriculado no Curso', False)
            self.limiteIns.listbox.delete(tk.ACTIVE)

    def criaCurso(self, event):
        nomeCurso = self.limiteIns.inputNomeCurso.get()
        gradeSelecionada = self.limiteIns.escolhaCombo.get()        
        grade = self.ctrlPrincipal.ctrlGrade.getGrade(gradeSelecionada)
        curso = Curso(nomeCurso, self.listaAlunosCurso, grade)
        self.listaCursos.append(curso)
        self.limiteIns.mostraMessagebox('Sucesso', 'Alunos matriculados no curso {} com sucesso'.format(nomeCurso), False)
        self.limiteIns.janela.destroy()

    #Consulta -------------------------------------
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
            self.limiteConsulta.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos!', True)
        except CursoNaoCadastrado:
            self.limiteConsulta.mostraMessagebox('Error', 'Curso não cadastrado!', True)
        else:
            LimiteMostraCursos(string)
        finally:
            self.limiteConsulta.clearConsulta(event)

    #Exclusão -------------------------------------
    def excluiHandler(self, event):
        nomeCurso = self.limiteExclui.inputTextNome.get()
        curso = self.getCurso(nomeCurso)
        try:
            if len(nomeCurso)==0:
                raise CamposNaoPreenchidos()
            elif curso == None:
                raise CursoNaoCadastrado()
        except CamposNaoPreenchidos:
            self.limiteExclui.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', True)
        except CursoNaoCadastrado:
            self.limiteExclui.mostraMessagebox('Alerta', 'Curso não cadastrado', True)
        else:
            self.listaCursos.remove(curso)
            self.limiteExclui.mostraMessagebox('Sucesso', 'Curso removido com sucesso', False)
            self.limiteExclui.clearExclusao(event)            

    #Atualização --------------------------------------------
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
        self.limiteAtualiza.mostraMessagebox('Atualização', 'Aluno removido com sucesso', False)
        self.exibir(event)
    
    def adiciona(self, event):
        alunoSelecionado = self.limiteAtualiza.listboxSemMatricula.get(tk.ACTIVE)
        aluno = self.ctrlPrincipal.ctrlAluno.getAluno(alunoSelecionado)
        self.listaAlunosCurso.append(aluno)
        self.limiteAtualiza.mostraMessagebox('Atualização', 'Aluno inserido com sucesso', False)
        self.exibir(event)

    def alteraGrade(self, event):
        nomeCurso = self.limiteAtualiza.escolhaCurso.get()
        anoCurso = self.limiteAtualiza.escolhaAnoGrade.get()
        grade = self.ctrlPrincipal.ctrlGrade.getGrade(anoCurso)
        for curs in self.listaCursos:
            if nomeCurso == curs.getNome():
                curs.setGrade(grade)
        self.limiteAtualiza.mostraMessagebox('Sucesso', 'Grade alterada com sucesso', False)
        self.exibir(event)