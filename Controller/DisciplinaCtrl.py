from sqlalchemy.sql.sqltypes import ARRAY
from View.DisciplinaView import *
from config.Mapeamento import Disciplina
from Model.DisciplinaModel import ManipulaBanco

class DisciplinaDuplicada(Exception): pass

class DisciplinaNaoCadastrada(Exception): pass

class CamposNaoPreenchidos(Exception): pass 

class ConexaoBD(Exception): pass

class CtrlDisciplina():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal

    def getListaDisciplinas(self):
        return ManipulaBanco.listaDisciplinas() 
            
    #Funções que serão chamadas na Main --- Instaciadores (MENU BAR) ---------------------------

    def insereDisciplinas(self, root):
        self.limiteIns = LimiteInsereDisciplina(self, root)

    def mostraDisciplinas(self):
        string = 'CÓDIGO -- NOME -- CH\n\n'
        disciplinas = self.getListaDisciplinas()
        try:
            if disciplinas == False:
                raise ConexaoBD()
        except:
            LimiteMostraDisciplinas('ERROR', 'Falha de conexão com o banco', True)
        else:
            for disciplina in disciplinas:
                string += '* '+disciplina.codigo+' -- '+disciplina.nome+' -- '+str(disciplina.cargahoraria)+'\n'       
            self.limiteLista = LimiteMostraDisciplinas('LISTA DE DISCIPLINAS', string, False)
    
    def consultaDisciplinas(self, root):
        self.limiteConsulta = LimiteConsultaDisciplina(self, root)

    def excluiDisciplinas(self, root):
        self.limiteExclui = LimiteExcluiDisciplina(self, root)
    
    def atualizaDisciplinas(self, root):
        self.limiteAtualiza = LimiteAtualizaDisciplina(self, root)

    #Funções auxiliares e de amarrações da classe ---------------------------------------------
    


    #Funções de CRUD dos Buttons ----------------------------------------------------

    def enterHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        nome = self.limiteIns.inputNome.get()
        ch = self.limiteIns.inputCargaHoraria.get()
        try:
            if len(codigo)==0 or len(nome)==0 or len(ch)==0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteIns.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            disciplina = Disciplina(codigo=codigo, nome=nome, cargahoraria=ch)
            status = ManipulaBanco.cadastraDisciplina(disciplina)
            print(status)
            try:
                if status == False:
                    raise DisciplinaDuplicada()
            except DisciplinaDuplicada:
                self.limiteIns.mostraMessagebox('ALERTA', 'Essa disciplina já existe ou falha de conexão com o Banco de dados', True)
            else:
                self.limiteIns.mostraMessagebox('SUCESSO', 'Disciplina cadastrada com sucesso', False)
            finally:
                self.limiteIns.clearHandler(event)
        
    def disciplinaConsulta(self, event):
        codigo = self.limiteConsulta.inputTextCodigo.get()
        try:
            if len(codigo) == 0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteConsulta.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            disciplina = ManipulaBanco.consultaDisciplina(codigo)
            try:
                if disciplina == False: raise ConexaoBD()
                if disciplina == None: raise DisciplinaNaoCadastrada()
            except ConexaoBD:
                self.limiteConsulta.mostraMessagebox('ERROR', 'Falha de conexão com o Banco de Dados', True)
            except DisciplinaNaoCadastrada:
                self.limiteConsulta.mostraMessagebox('ALERTA', 'Disciplina não cadastrada', True)
            else:
                string = 'CODIGO -- NOME -- CH\n\n'+disciplina.codigo+' -- '+disciplina.nome+' -- '+str(disciplina.cargahoraria)
                LimiteMostraDisciplinas('CONSULTA DISCIPLINA', string, False)
            finally:
                self.limiteConsulta.clearConsulta(event)
            
    def disciplinaDelete(self, event):
        codigo = self.limiteExclui.inputTextCodigo.get()
        try:
            if len(codigo)==0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteExclui.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            status = ManipulaBanco.deletaDisciplina(codigo)
            try:
                if status == False:
                    raise DisciplinaNaoCadastrada()
            except DisciplinaNaoCadastrada:
                self.limiteExclui.mostraMessagebox('ALERTA', 'Disciplina não cadastrada ou falha de conexão com Banco de Dados', True)
            else:
                self.limiteExclui.mostraMessagebox('SUCESSO', 'Disciplina deletada com sucesso', False)
            finally:
                self.limiteExclui.clearExclusao(event)

    def atualizarDisciplina(self, event):
        codigo = self.limiteAtualiza.inputCodigo.get()
        nome = self.limiteAtualiza.inputNome.get()
        ch = self.limiteAtualiza.inputCargaHoraria.get()
        try:
            if len(codigo) == 0 or len(nome) == 0 or len(ch) == 0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteAtualiza.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            status = ManipulaBanco.atualizaDisciplina(codigo, nome, ch)
            try:
                if status == False:
                    raise DisciplinaNaoCadastrada()
            except DisciplinaNaoCadastrada:
                self.limiteAtualiza.mostraMessagebox('ALERTA', 'Disciplina não cadastrada ou falha de conexão com o Banco de Dados', True)
            else: 
                self.limiteAtualiza.mostraMessagebox('SUCESSO', 'Nome de disciplina e carga horária atualizado com sucesso', False)
            finally:
                self.limiteAtualiza.clearAtualiza(event)