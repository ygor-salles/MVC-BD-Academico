from View.AlunoView import *
from config.Mapeamento import Aluno
from Model.AlunoModel import ManipulaBanco

class AlunoDuplicado(Exception): pass

class AlunoNaoCadastrado(Exception): pass

class CamposNaoPreenchidos(Exception): pass 

class ConexaoBD(Exception): pass

class CtrlAluno():
    def getListaAlunos(self):
        return ManipulaBanco.listaAlunos() 
            
    #Funções que serão chamadas na Main --- Instaciadores (MENU BAR) ---------------------------

    def insereAlunos(self, root):
        self.limiteIns = LimiteInsereAluno(self, root) 

    def mostraAlunos(self):
        string = 'MATRÍCULA -- NOME\n'
        alunos = self.getListaAlunos()
        try:
            if alunos == False:
                raise ConexaoBD()
        except:
            LimiteMostraAlunos('ERROR', 'Falha de conexão com o banco', True)
        else:
            for aluno in alunos:
                string += str(aluno.nromatric) + ' -- ' + aluno.nome +'\n'       
            self.limiteLista = LimiteMostraAlunos('LISTA DE ALUNOS', string, False)
    
    def consultaAlunos(self, root):
        self.limiteConsulta = LimiteConsultaAluno(self, root)

    def excluiAlunos(self, root):
        self.limiteExclui = LimiteExcluiAluno(self, root)
    
    def atualizaAlunos(self, root):
        self.limiteAtualiza = LimiteAtualizaAluno(self, root)

    #Funções auxiliares e de amarrações da classe ---------------------------------------------
    


    #Funções de CRUD dos Buttons ----------------------------------------------------

    def enterHandler(self, event):
        nroMatric = self.limiteIns.inputNro.get()
        nome = self.limiteIns.inputNome.get()
        try:
            if len(nroMatric)==0 or len(nome)==0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteIns.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            aluno = Aluno(nromatric=nroMatric, nome=nome)
            status = ManipulaBanco.cadastraAluno(aluno)
            print(status)
            try:
                if status == False:
                    raise AlunoDuplicado()
            except AlunoDuplicado:
                self.limiteIns.mostraMessagebox('ALERTA', 'A matrícula desse aluno já existe ou falha de conexão', True)
            else:
                self.limiteIns.mostraMessagebox('SUCESSO', 'Aluno cadastrado com sucesso', False)
            finally:
                self.limiteIns.clearHandler(event)
        
    def consultaAluno(self, event):
        nroMatric = str(self.limiteConsulta.inputTextMatricula.get())
        try:
            if len(nroMatric) == 0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteConsulta.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            aluno = ManipulaBanco.consultaAluno(nroMatric)
            try:
                if aluno == False: raise ConexaoBD()
                if aluno == None: raise AlunoNaoCadastrado()
            except ConexaoBD:
                self.limiteConsulta.mostraMessagebox('ERROR', 'Falha de conexão com o Banco de Dados', True)
            except AlunoNaoCadastrado:
                self.limiteConsulta.mostraMessagebox('ALERTA', 'Aluno não cadastrado', True)
            else:
                string = 'MATRÍCULA -- NOME\n'+str(aluno.nromatric)+' -- '+aluno.nome
                LimiteMostraAlunos('CONSULTA ALUNO', string, False)
            finally:
                self.limiteConsulta.clearAluno(event)
            
    def alunoDelete(self, event):
        nroMatric = self.limiteExclui.inputMatric.get()
        try:
            if len(nroMatric)==0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteExclui.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            status = ManipulaBanco.deletaAluno(nroMatric)
            try:
                if status == False:
                    raise AlunoNaoCadastrado()
            except AlunoNaoCadastrado:
                self.limiteExclui.mostraMessagebox('ALERTA', 'Aluno não cadastrado ou falha de conexão com Banco de Dados', True)
            else:
                self.limiteExclui.mostraMessagebox('SUCESSO', 'Aluno deletado com sucesso', False)
            finally:
                self.limiteExclui.clearAlunoDelete(event)

    def atualizarAluno(self, event):
        nroMatric = self.limiteAtualiza.inputMatric.get()
        nome = self.limiteAtualiza.inputNome.get()
        try:
            if len(nroMatric) == 0 or len(nome) == 0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteAtualiza.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            status = ManipulaBanco.atualizaAluno(nroMatric, nome)
            try:
                if status == False:
                    raise AlunoNaoCadastrado()
            except AlunoNaoCadastrado:
                self.limiteAtualiza.mostraMessagebox('ALERTA', 'Aluno não cadastrado ou falha de conexão com o Banco de Dados', True)
            else: 
                self.limiteAtualiza.mostraMessagebox('SUCESSO', 'Nome de aluno atualizado com sucesso', False)
            finally:
                self.limiteAtualiza.atualizarClearAluno(event)