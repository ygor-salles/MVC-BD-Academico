import os.path
import pickle
from View.GradeView import *
from Model.GradeModel import Grade

class GradeDuplicada(Exception):
    pass

class GradeNaoEncontrada(Exception):
    pass

class CamposNaoPreenchidos(Exception):
    pass

class CtrlGrade():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaDiscGrade = []
        self.listaCodDisc = []
        self.listaGradeCodDisc = []
        self.testePopula = False
        
        if not os.path.isfile("Grade.pickle"):
            self.listaGrade =  []
        else:
            with open("Grade.pickle", "rb") as f:
                self.listaGrade = pickle.load(f)

    #Função para persistencia de dados ---------------------------------------------
    
    def salvaGrades(self):
        if len(self.listaGrade) != 0:
            with open("Grade.pickle","wb") as f:
                pickle.dump(self.listaGrade, f)
    
    #Funções que serão chamadas na Main --- Instaciadores ---------------------------

    def insereGrade(self, root):        
        self.listaDiscGrade = []
        self.listaCodDisc = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisciplinas()
        self.limiteIns = LimiteInsereGrade(self, root, self.listaCodDisc)
    
    def mostraGrade(self):
        string=''
        for grade in self.listaGrade:
            string += '\nGrade: '+grade.getAnoCurso()+'\n'
            for disc in grade.getListaDisc():
                string += disc.getCodigo()+' -- '+disc.getNome()+' -- '+str(disc.getCargaHoraria())+'\n'
            string += '--------------------------\n'
        self.limiteMostra = LimiteMostra(string)

    def consultaGrade(self, root):
        self.limiteConsulta = LimiteConsultaGrade(self, root)
    
    def excluiGrade(self, root):
        self.limiteExclui = LimiteExcluiGrade(self, root)

    def atualizaGrade(self, root):
        #para o combobox
        listaGradeAnoCurso = [] 
        listaGradeAnoCurso =  self.getListaGradeAnoCurso()
        self.limiteAtualiza = LimiteAtualizaGrade(self, root, listaGradeAnoCurso)

    #Funções Auxiliares e de amarrações da classe -------------------------------------------------------------
    
    def mostraConsultaGrade(self, anoCurso):
        string = 'Grade Cadastrada \n'
        for grade in self.listaGrade:
            if grade.getAnoCurso()==anoCurso:
                string += '\nGrade: '+grade.getAnoCurso()+'\n Listas de disciplinas da Grade: \n'
                for disc in grade.getListaDisc():
                    string += disc.getCodigo()+' -- '+disc.getNome()+' -- '+str(disc.getCargaHoraria())+'\n'
        self.limiteMostra = LimiteMostra(string)
    
    def verificaListaGrade(self, AnoCurso):
        for grade in self.listaGrade:
            if grade.getAnoCurso()==AnoCurso:
                return True
        return False
    
    def getListaGradeAnoCurso(self):
        listGradeAnoCurso = []
        for grade in self.listaGrade:
            listGradeAnoCurso.append(grade.getAnoCurso())
        return listGradeAnoCurso
    
    def getGrade(self, AnoCursoGrade):
        gradeRet = None
        for grade in self.listaGrade:
            if grade.getAnoCurso() == AnoCursoGrade:
                gradeRet = grade
        return gradeRet
    
    def getListaGrade(self):
        return self.listaGrade
    
    def getListaGradeCodDisc(self, anoCurso):
        listaGradeCodDisc = []
        for grade in self.listaGrade:
            if anoCurso == grade.getAnoCurso():
                for codDisc in grade.getListaDisc():
                    listaGradeCodDisc.append(codDisc.getCodigo())
                return listaGradeCodDisc
    
    def getDiscGrade(self, anoCurso, codDisc):
        for grade in self.listaGrade:
            if anoCurso == grade.getAnoCurso():
                for disc in grade.getListaDisc():
                    if codDisc == disc.getCodigo():
                        return disc

    #Funções de CRUD -- Buttons ---------------------------------
    
    # Inserção ---------------------------
    def insereHandler(self, event):
        anoCurso = self.limiteIns.inputAnoCurso.get()
        disciplinaSel = self.limiteIns.listbox.get(tk.ACTIVE)
        disc = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(disciplinaSel)
        try:
            if self.verificaListaGrade(anoCurso) == True:
                raise GradeDuplicada()
            if len(anoCurso)==0 or disc==None:
                raise CamposNaoPreenchidos()
        except GradeDuplicada:
            self.limiteIns.mostraMessagebox('Error', 'Grade já existe!', True)
        except CamposNaoPreenchidos:
            self.limiteIns.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', True)
        else:
            self.listaDiscGrade.append(disc)
            self.limiteIns.mostraMessagebox('Sucesso', 'Disciplina cadastrada com sucesso', False)
            self.limiteIns.listbox.delete(tk.ACTIVE)
    
    def criaHandler(self, event):
        anoCurso = self.limiteIns.inputAnoCurso.get()
        grade = Grade(anoCurso, self.listaDiscGrade)
        self.listaGrade.append(grade)
        self.limiteIns.mostraMessagebox('Sucesso', 'Grade criada com sucesso', False)
        self.limiteIns.janela.destroy()
    
    # Consulta -------------------------------------
    def consultaHandler(self, event):
        anoCurso = self.limiteConsulta.inputAnoCurso.get()
        try:
            if len(anoCurso)==0:
                raise CamposNaoPreenchidos()
            if self.verificaListaGrade(anoCurso) == False:
                raise GradeNaoEncontrada()
        except CamposNaoPreenchidos:
            self.limiteConsulta.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', True)
        except GradeNaoEncontrada:
            self.limiteConsulta.mostraMessagebox('Error', 'Ano de Grade não encontrado', True)
        else:
            self.mostraConsultaGrade(anoCurso)
        finally:
            self.limiteConsulta.clearConsulta(event)

    # Exclusão ------------------------------------------
    def exluiHandler(self, event):
        anoCurso = self.limiteExclui.inputAnoCurso.get()
        grade = self.getGrade(anoCurso)
        try:
            if len(anoCurso)==0:
                raise CamposNaoPreenchidos()
            if grade == None:
                raise GradeNaoEncontrada()
        except CamposNaoPreenchidos:
            self.limiteExclui.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', True)
        except GradeNaoEncontrada:
            self.limiteExclui.mostraMessagebox('Error', 'Ano de Grade não encontrado', True)
        else:
            self.listaGrade.remove(grade)
            self.limiteExclui.mostraMessagebox('Exclusão', 'Grade {} removida com sucesso'.format(anoCurso), False)
            self.limiteExclui.clearExclusao(event)

    # Atualiza ---------------------------------------------------
    def popular(self, event):
        #para os listBox's
        comboAnoCurso = self.limiteAtualiza.escolhaCombo.get()
        self.listaGradeCodDisc = self.getListaGradeCodDisc(comboAnoCurso)
        listaTodasDisciplinas = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisciplinas()
        if self.testePopula == False:
            self.testePopula = self.limiteAtualiza.IsPopularListbox(self.listaGradeCodDisc)
            self.limiteAtualiza.IsPopularListboxTodas(listaTodasDisciplinas ,self.listaGradeCodDisc)
        else:
            self.limiteAtualiza.limparListBox()
            self.limiteAtualiza.IsPopularListbox(self.listaGradeCodDisc)
            self.limiteAtualiza.IsPopularListboxTodas(listaTodasDisciplinas ,self.listaGradeCodDisc)

    def removeDisciplina(self, event):
        comboAnoCurso = self.limiteAtualiza.escolhaCombo.get()
        disciplinaSel = self.limiteAtualiza.listbox.get(tk.ACTIVE)
        disciplina = self.getDiscGrade(comboAnoCurso, disciplinaSel)
        for grade in self.listaGrade:
            if comboAnoCurso == grade.getAnoCurso():
                grade.getListaDisc().remove(disciplina)
        self.limiteAtualiza.mostraMessagebox('Sucesso', 'Disciplina removida com sucesso', False)
        self.popular(event)
    
    def adicionaDisciplina(self, event):
        comboAnoCurso = self.limiteAtualiza.escolhaCombo.get()
        disciplinaSel = self.limiteAtualiza.listboxTodas.get(tk.ACTIVE)
        disciplina = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(disciplinaSel)
        for grade in self.listaGrade:
            if comboAnoCurso == grade.getAnoCurso():
                grade.getListaDisc().append(disciplina)
        self.limiteAtualiza.mostraMessagebox('Sucesso', 'Disciplina adicionada com sucesso', False)
        self.popular(event)