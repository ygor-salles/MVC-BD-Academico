from View.GradeView import *
from config.Mapeamento import Grade
from Model.GradeModel import ManipulaBanco

class GradeDuplicada(Exception): pass

class GradeNaoCadastrada(Exception): pass

class CamposNaoPreenchidos(Exception): pass 

class ConexaoBD(Exception): pass

class CtrlGrade():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal

    def getListaGrades(self):
        return ManipulaBanco.listaGrades() 
            
    #Funções que serão chamadas na Main --- Instaciadores (MENU BAR) ---------------------------

    def insereGrades(self, root):
        self.limiteIns = LimiteInsereGrade(self, root) 

    def mostraGrades(self):
        string = 'ANO-CURSO\n'
        grades = self.getListaGrades()
        try:
            if grades == False:
                raise ConexaoBD()
        except:
            LimiteMostraGrades('ERROR', 'Falha de conexão com o banco', True)
        else:
            for grade in grades:
                string += grade.anocurso+'\n'       
            self.limiteLista = LimiteMostraGrades('LISTA DE GRADES', string, False)
    
    def consultaGrades(self, root):
        self.limiteConsulta = LimiteConsultaGrade(self, root)

    def excluiGrades(self, root):
        self.limiteExclui = LimiteExcluiGrade(self, root)
    
    def atualizaGrades(self, root):
        self.limiteAtualiza = LimiteAtualizaGrade(self, root)

    #Funções auxiliares e de amarrações da classe ---------------------------------------------
    


    #Funções de CRUD dos Buttons ----------------------------------------------------

    def enterHandler(self, event):
        anoCurso = self.limiteIns.inputAnoCurso.get()
        try:
            if len(anoCurso)==0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteIns.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            grade = Grade(anocurso=anoCurso)
            status = ManipulaBanco.cadastraGrade(grade)
            print(status)
            try:
                if status == False:
                    raise GradeDuplicada()
            except GradeDuplicada:
                self.limiteIns.mostraMessagebox('ALERTA', 'Essa grade já existe ou falha de conexão', True)
            else:
                self.limiteIns.mostraMessagebox('SUCESSO', 'Grade cadastrada com sucesso', False)
            finally:
                self.limiteIns.clearHandler(event)
        
    def gradeConsulta(self, event):
        anoCurso = self.limiteConsulta.inputAnoCurso.get()
        try:
            if len(anoCurso) == 0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteConsulta.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            grade = ManipulaBanco.consultaGrade(anoCurso)
            try:
                if grade == False: raise ConexaoBD()
                if grade == None: raise GradeNaoCadastrada()
            except ConexaoBD:
                self.limiteConsulta.mostraMessagebox('ERROR', 'Falha de conexão com o Banco de Dados', True)
            except GradeNaoCadastrada:
                self.limiteConsulta.mostraMessagebox('ALERTA', 'Grade não cadastrada', True)
            else:
                string = 'ANO-CURSO\n'+grade.anocurso
                LimiteMostraGrades('CONSULTA GRADE', string, False)
            finally:
                self.limiteConsulta.clearConsulta(event)
            
    def gradeDelete(self, event):
        anoCurso = self.limiteExclui.inputAnoCurso.get()
        try:
            if len(anoCurso)==0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteExclui.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            status = ManipulaBanco.deletaGrade(anoCurso)
            try:
                if status == False:
                    raise GradeNaoCadastrada()
            except GradeNaoCadastrada:
                self.limiteExclui.mostraMessagebox('ALERTA', 'Grade não cadastrada ou falha de conexão com Banco de Dados', True)
            else:
                self.limiteExclui.mostraMessagebox('SUCESSO', 'Grade deletada com sucesso', False)
            finally:
                self.limiteExclui.clearExclusao(event)

    def atualizarGrade(self, event):
        anoCurso = self.limiteAtualiza.get()
        nome = self.limiteAtualiza.inputNome.get()
        try:
            if len(anoCurso) == 0 or len(nome) == 0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteAtualiza.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            status = ManipulaBanco.atualizaGrade(anoCurso, nome)
            try:
                if status == False:
                    raise GradeNaoCadastrada()
            except GradeNaoCadastrada:
                self.limiteAtualiza.mostraMessagebox('ALERTA', 'Grade não cadastrado ou falha de conexão com o Banco de Dados', True)
            else: 
                self.limiteAtualiza.mostraMessagebox('SUCESSO', 'Nome de grade atualizado com sucesso', False)
            finally:
                self.limiteAtualiza.atualizarClearGrade(event)