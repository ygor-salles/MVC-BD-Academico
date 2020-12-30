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
        #str = 'Nro Matric. -- Nome\n'
        pprint(self.getListaAlunos())
        # for aluno in self.getListaAlunos():
            
        #     str += aluno.getNroMatric() + ' -- ' + aluno.getNome() +'\n'       
        # self.limiteLista = LimiteMostraAlunos(str)
    
    def consultaAlunos(self, root):
        self.limiteConsulta = LimiteConsultaAluno(self, root)

    def excluiAlunos(self, root):
        self.limiteExclui = LimiteExcluiAluno(self, root)
    
    def atualizaAlunos(self, root):
        self.limiteAtualiza = LimiteAtualizaAluno(self, root)

    #Funções auxiliares e de amarrações da classe ---------------------------------------------
    
    def getAluno(self, nroMatric):
        # alunoRet = None
        # for aluno in self.listaAlunos:
        #     if aluno.getNroMatric() == nroMatric:
        #         alunoRet = aluno
        # return alunoRet
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
        aluno = Aluno(nromatric=nroMatric, nome=nome)
        status = ManipulaBanco.cadastraAluno(aluno)
        try:
            if len(nroMatric)==0 or len(nome)==0:
                raise CamposNaoPreenchidos()
            if status == False:
                raise AlunoDuplicado()
        except CamposNaoPreenchidos:
            self.limiteIns.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', True)
        except AlunoDuplicado:
            self.limiteIns.mostraMessagebox('Alerta', 'A matrícula desse aluno já existe ou falha de conexão', True)
            self.limiteIns.clearHandler(event)
        else:
            self.limiteIns.mostraMessagebox('Sucesso', 'Aluno cadastrado com sucesso', False)
            self.limiteIns.clearHandler(event)
            

    def consultaAluno(self, event):
        nroMatric = self.limiteConsulta.inputTextMatricula.get()
        aluno = self.getAluno(nroMatric)
        try:
            if len(nroMatric)==0:
                raise CamposNaoPreenchidos()
            if aluno == False:
                raise AlunoNaoCadastrado()
        except CamposNaoPreenchidos:
            self.limiteConsulta.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', True)
        except AlunoNaoCadastrado:
            self.limiteConsulta.mostraMessagebox('Alerta', 'Aluno não cadastrado', True)
        else:
            string = 'Aluno cadastrado \nMatrícula -- Nome\n'+str(aluno.nromatric)+' -- '+aluno.nome
            LimiteMostraAlunos(string)
        finally:
            self.limiteConsulta.clearAluno(event)

    def alunoDelete(self, event):
        nroMatric = self.limiteExclui.inputMatric.get()
        status = ManipulaBanco.deletaAluno(nroMatric)
        try:
            if len(nroMatric)==0:
                raise CamposNaoPreenchidos()
            if status == False:
                raise AlunoNaoCadastrado()
        except CamposNaoPreenchidos:
            self.limiteExclui.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', True)
        except AlunoNaoCadastrado:
            self.limiteExclui.mostraMessagebox('Alerta', 'Aluno não cadastrado ou falha de conexão', True)
            self.limiteExclui.clearAlunoDelete(event)
        else:
            self.limiteExclui.mostraMessagebox('Sucesso', 'Aluno deletado com sucesso', False)
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