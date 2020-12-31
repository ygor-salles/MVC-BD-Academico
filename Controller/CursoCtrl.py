from Model.CursoModel import ManipulaBanco
from View.CursoView import *
from config.Mapeamento import Curso

class CursoNaoCadastrado(Exception): pass

class CamposNaoPreenchidos(Exception): pass

class CursoDuplicado(Exception): pass

class ConexaoBD(Exception): pass

class CtrlCurso():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaAlunosCurso = []
        self.testePopula = False

    def getListaCursos(self):
        return ManipulaBanco.listaCursos()

    # Funções Auxiliares ----------------------------------------------------------
    
    

    # Funções instancioadores, recebe da main ---------------------------

    def insereCursos(self, root):
        self.limiteIns = LimiteInsereCurso(self, root)

    def mostraCursos(self):
        string = 'CURSOS:\n\n'
        cursos = self.getListaCursos()
        try:
            if cursos == False:
                raise ConexaoBD()
        except ConexaoBD:
            LimiteMostraCursos('ERROR', 'Falha de conexão com o Banco de Dados', True)
        else:
            for curso in cursos:
                string += curso.nome+'\n'
            self.limiteMostra = LimiteMostraCursos('LISTA DE CURSOS', string, False)
    
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
    def enterHandler(self, event):
        nome = self.limiteIns.inputNomeCurso.get()
        try:
            if len(nome) == 0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteIns.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            curso = Curso(nome=nome)
            status = ManipulaBanco.cadastraCurso(curso)
            try:
                if status == False:
                    raise CursoDuplicado()
            except CursoDuplicado:
                self.limiteIns.mostraMessagebox('ALERTA', 'O curso já existe ou falha de conexão com Banco de Dados', True)
            else:
                self.limiteIns.mostraMessagebox('SUCESSO', 'Curso cadastrado com sucesso!', False)
            finally:
                self.limiteIns.clearHandler(event)

    #Consulta -------------------------------------
    def consultaHandler(self, event):
        nome = self.limiteConsulta.inputTextNome.get()
        try:
            if len(nome) == 0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteConsulta.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            curso = ManipulaBanco.consultaCurso(nome)
            try:
                if curso == False: raise ConexaoBD()
                if curso == None: raise CursoNaoCadastrado()
            except ConexaoBD:
                self.limiteConsulta.mostraMessagebox('ERROR', 'Falha de conexão com o Banco de Dados', True)
            except CursoNaoCadastrado:
                self.limiteConsulta.mostraMessagebox('ALERTA', 'Curso não cadastrado', True)
            else:
                string = 'CURSO\n'+curso.nome
                LimiteMostraCursos('CONSULTA CURSO', string, False)
            finally:
                self.limiteConsulta.clearConsulta(event)


    #Exclusão -------------------------------------
    def excluiHandler(self, event):
        nomeCurso = self.limiteExclui.inputTextNome.get()
        try:
            if len(nomeCurso) == 0: raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteExclui.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            status = ManipulaBanco.deletaCurso(nomeCurso)
            print(status)
            try:
                if status == False: raise CursoNaoCadastrado()
            except CursoNaoCadastrado:
                self.limiteExclui.mostraMessagebox('ALERTA', 'Curso não cadastrado ou falha de conexão com Banco de Dados', True)
            else:
                self.limiteExclui.mostraMessagebox('SUCESSO', 'Curso deletado com sucesso', False)
            finally:
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
        for curs in self.getListaCursos():
            if nomeCurso == curs.getNome():
                curs.setGrade(grade)
        self.limiteAtualiza.mostraMessagebox('Sucesso', 'Grade alterada com sucesso', False)
        self.exibir(event)