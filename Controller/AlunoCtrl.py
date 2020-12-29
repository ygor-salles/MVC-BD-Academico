from View.AlunoView import *
from Model.AlunoModel import Aluno, ManipulaBanco

class AlunoDuplicado(Exception):
    pass

class AlunoNaoCadastrado(Exception):
    pass

class CamposNaoPreenchidos(Exception):
    pass 

class CtrlAluno():
            
    #Funções que serão chamadas na Main --- Instaciadores ---------------------------

    def insereAlunos(self, root):
        self.limiteIns = LimiteInsereAluno(self, root) 

    def mostraAlunos(self):
        str = 'Nro Matric. -- Nome\n'
        for aluno in self.listaAlunos:
            str += aluno.getNroMatric() + ' -- ' + aluno.getNome() +'\n'       
        self.limiteLista = LimiteMostraAlunos(str)
    
    def consultaAlunos(self, root):
        self.limiteConsulta = LimiteConsultaAluno(self, root)

    def excluiAlunos(self, root):
        self.limiteExclui = LimiteExcluiAluno(self, root)
    
    def atualizaAlunos(self, root):
        self.limiteAtualiza = LimiteAtualizaAluno(self, root)

    #Funções auxiliares e de amarrações da classe ---------------------------------------------
    
    def getAluno(self, nroMatric):
        alunoRet = None
        for aluno in self.listaAlunos:
            if aluno.getNroMatric() == nroMatric:
                alunoRet = aluno
        return alunoRet
    
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
        # aluno = self.getAluno(nroMatric)
        # try:
        #     if aluno != None:
        #         raise AlunoDuplicado()
        #     if len(nroMatric)==0 or len(nome)==0:
        #         raise CamposNaoPreenchidos()
        # except AlunoDuplicado:
        #     self.limiteIns.mostraMessagebox('Alerta', 'A matrícula desse aluno já existe', True)
        # except CamposNaoPreenchidos:
        #     self.limiteIns.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', True)
        # else:
        aluno = Aluno(nromatric=nroMatric, nome=nome)
        status = ManipulaBanco.cadastraAluno(aluno)
        print(status)
        self.limiteIns.mostraMessagebox('Sucesso', 'Aluno cadastrado com sucesso', False)
        self.limiteIns.clearHandler(event)

    def consultaAluno(self, event):
        nroMatric = self.limiteConsulta.inputTextMatricula.get()
        aluno = self.getAluno(nroMatric)
        try:
            if len(nroMatric)==0:
                raise CamposNaoPreenchidos()
            if aluno == None:
                raise AlunoNaoCadastrado()
        except CamposNaoPreenchidos:
            self.limiteConsulta.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', True)
        except AlunoNaoCadastrado:
            self.limiteConsulta.mostraMessagebox('Alerta', 'Aluno não cadastrado', True)
        else:
            str = 'Aluno cadastrado \nMatrícula -- Nome\n'+aluno.getNroMatric()+' -- '+aluno.getNome()
            LimiteMostraAlunos(str)
        finally:
            self.limiteConsulta.clearAluno(event)

    def alunoDelete(self, event):
        nroMatric = self.limiteExclui.inputMatric.get()
        aluno = self.getAluno(nroMatric)
        try:
            if len(nroMatric) == 0:
                raise CamposNaoPreenchidos()
            elif aluno == None:
                raise AlunoNaoCadastrado()
        except CamposNaoPreenchidos:
            self.limiteExclui.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', True)
        except AlunoNaoCadastrado:
            self.limiteExclui.mostraMessagebox('Alerta', 'Aluno não cadastrado', True)
        else: 
            self.listaAlunos.remove(aluno)
            self.limiteExclui.mostraMessagebox('Sucesso', 'Aluno excluído com sucesso', False)
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