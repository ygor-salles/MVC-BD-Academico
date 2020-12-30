from sqlalchemy.sql.base import Executable
from View.AlunoView import *
from config.Mapeamento import Aluno
from Model.AlunoModel import ManipulaBanco
from pprint import pprint

class AlunoDuplicado(Exception):
    pass

class AlunoNaoCadastrado(Exception):
    pass

class CamposNaoPreenchidos(Exception):
    pass 

class ConexaoBD(Exception):
    pass

class CtrlAluno():
    def getListaAlunos(self):
        return ManipulaBanco.listaAlunos() 
            
    #Funções que serão chamadas na Main --- Instaciadores ---------------------------

    def insereAlunos(self, root):
        self.limiteIns = LimiteInsereAluno(self, root) 

    def mostraAlunos(self):
        string = 'Nro Matric. -- Nome\n'
        for aluno in self.getListaAlunos():
            string += aluno.nromatric + ' -- ' + aluno.nome +'\n'       
        self.limiteLista = LimiteMostraAlunos(string)
    
    def consultaAlunos(self, root):
        self.limiteConsulta = LimiteConsultaAluno(self, root)

    def excluiAlunos(self, root):
        self.limiteExclui = LimiteExcluiAluno(self, root)
    
    def atualizaAlunos(self, root):
        self.limiteAtualiza = LimiteAtualizaAluno(self, root)

    #Funções auxiliares e de amarrações da classe ---------------------------------------------
    
    def getAluno(self, nroMatric):
        return ManipulaBanco.consultaAluno(nroMatric)
    
    def getListaNroMatric(self):
        listNroMatric = []
        for matric in self.listaAlunos:
            listNroMatric.append(matric.getNroMatric())
        return listNroMatric
    
    def getAtualizaAluno(self, nroMatric, nome):
        for aluno in self.listaAlunos:
            if nroMatric == aluno.getNroMatric():
                aluno.setNome(nome)

    #Funções de CRUD dos Buttons ----------------------------------------------------

    def enterHandler(self, event):
        nroMatric = self.limiteIns.inputNro.get()
        nome = self.limiteIns.inputNome.get()
        try:
            if len(nroMatric)==0 or len(nome)==0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteIns.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', True)
        else:
            aluno = Aluno(nromatric=nroMatric, nome=nome)
            status = ManipulaBanco.cadastraAluno(aluno)
            print(status)
            try:
                if status == False:
                    raise AlunoDuplicado()
            except AlunoDuplicado:
                self.limiteIns.mostraMessagebox('Alerta', 'A matrícula desse aluno já existe ou falha de conexão', True)
            else:
                self.limiteIns.mostraMessagebox('Sucesso', 'Aluno cadastrado com sucesso', False)
            finally:
                self.limiteIns.clearHandler(event)
        
    def consultaAluno(self, event):
        nroMatric = self.limiteConsulta.inputTextMatricula.get()
        aluno = self.getAluno(nroMatric)
        print(aluno)
        try:
            if len(nroMatric)==0:
                raise CamposNaoPreenchidos()
            if aluno == False:
                raise ConexaoBD()
            if aluno == None:
                raise AlunoNaoCadastrado()
        except CamposNaoPreenchidos:
            self.limiteConsulta.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', True)
        except ConexaoBD:
            self.limiteConsulta.mostraMessagebox('Error', 'Falha de conexão com o Banco', True)
        except AlunoNaoCadastrado:
            self.limiteConsulta.mostraMessagebox('Alerta', 'Aluno não cadastrado', True)
        else:
            string = 'Aluno cadastrado \nMatrícula -- Nome\n'+str(aluno.nromatric)+' -- '+aluno.nome
            LimiteMostraAlunos(string)
        finally:
            self.limiteConsulta.clearAluno(event)

    def alunoDelete(self, event):
        nroMatric = self.limiteExclui.inputMatric.get()
        try:
            if len(nroMatric)==0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteExclui.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', True)
        else:
            status = ManipulaBanco.deletaAluno(nroMatric)
            try:
                if status == False:
                    raise AlunoNaoCadastrado()
            except AlunoNaoCadastrado:
                self.limiteExclui.mostraMessagebox('Alerta', 'Aluno não cadastrado ou falha de conexão', True)
            else:
                self.limiteExclui.mostraMessagebox('Sucesso', 'Aluno deletado com sucesso', False)
            finally:
                self.limiteExclui.clearAlunoDelete(event)

    def atualizarAluno(self, event):
        nroMatric = self.limiteAtualiza.inputMatric.get()
        nome = self.limiteAtualiza.inputNome.get()
        aluno = self.getAluno(nroMatric)
        try:
            if len(nroMatric) == 0 or len(nome) == 0:
                raise CamposNaoPreenchidos()
            elif aluno == None:
                raise AlunoNaoCadastrado()
        except CamposNaoPreenchidos:
            self.limiteAtualiza.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', True)
        except AlunoNaoCadastrado:
            self.limiteAtualiza.mostraMessagebox('Alerta', 'Aluno não cadastrado', True)
        else: 
            self.getAtualizaAluno(nroMatric, nome)
            self.limiteAtualiza.mostraMessagebox('Atualização', 'Nome de aluno atualizado com sucesso', False)
            self.limiteAtualiza.atualizarClearAluno(event)