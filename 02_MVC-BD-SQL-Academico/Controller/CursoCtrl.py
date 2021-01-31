from Model.CursoModel import ManipulaBanco
from View.CursoView import *
from DAO.Mapeamento import Curso

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
    
    def getListaNomeCursos(self):
        listaNomeCursos = []
        cursos = self.getListaCursos()
        try:
            if self.getListaCursos() == False:
                raise ConexaoBD()
        except ConexaoBD:
            return None
        else:
            for curso in cursos:
                listaNomeCursos.append(curso.nome)
            return listaNomeCursos

    # Funções instancioadores, recebe da main ---------------------------

    def insereCursos(self, root):
        self.limiteIns = LimiteInsereCurso(self, root)

    def relatorioCursos(self, root):
        cursos = self.getListaCursos()
        try:
            if cursos == False:
                raise ConexaoBD()
        except:
            LimiteMostraCursos('ERROR', 'Falha de conexão com o banco', True)
        else:
            LimiteTabelaCursos(root, cursos)
    
    def consultaCursos(self, root):
        listaCursos = self.getListaNomeCursos()
        self.limiteConsulta = LimiteConsultaCursos(self, root, listaCursos)

    def excluiCursos(self, root):
        listaCursos = self.getListaNomeCursos()
        self.limiteExclui = LimiteExcluiCursos(self, root, listaCursos)

    #Funções de CRUD dos Buttons ----------------------------------------------------

    #Inserção -----------------------------------------
    def enterHandler(self, event):
        nome = self.limiteIns.inputCurso.get()
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
        nome = self.limiteConsulta.escolhaCurso.get()
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
                string = f'{curso.nome}\n'
                if curso.grade == None:
                    string += 'SEM GRADE\n'
                else:
                    string += f'Grade: {curso.grade.ano}\n'
                string += '\nALUNOS MATRICULADOS: \n'
                for aluno in curso.alunos:
                    string += f'{aluno.nro_matric} -- {aluno.nome}\n'
                string += '---------------------------\n'
                LimiteMostraCursos('CONSULTA CURSO', string, False)
            finally:
                self.limiteConsulta.clearConsulta(event)

    #Exclusão -------------------------------------
    def excluiHandler(self, event):
        nomeCurso = self.limiteExclui.escolhaCurso.get()
        try:
            if len(nomeCurso) == 0: raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteExclui.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            status = ManipulaBanco.deletaCurso(nomeCurso)
            try:
                if status == False: raise CursoNaoCadastrado()
            except CursoNaoCadastrado:
                self.limiteExclui.mostraMessagebox('ALERTA', 'Curso não cadastrado ou falha de conexão com Banco de Dados', True)
            else:
                self.limiteExclui.mostraMessagebox('SUCESSO', 'Curso deletado com sucesso', False)
            finally:
                self.limiteExclui.clearExclusao(event)            