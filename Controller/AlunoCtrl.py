from View.AlunoView import *
from DAO.Mapeamento import Aluno
from Model.AlunoModel import ManipulaBanco
from pprint import pprint

class AlunoDuplicado(Exception): pass

class AlunoNaoCadastrado(Exception): pass

class CamposNaoPreenchidos(Exception): pass 

class ConexaoBD(Exception): pass

class CtrlAluno():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal

    def getListaAlunos(self):
        return ManipulaBanco.listaAlunos() 

    # Funções auxiliares e de amarrações da classe ---------------------------------------------
    
    def getListaMatricAluno(self):
        listaMatricAluno = []
        alunos = self.getListaAlunos()
        try:
            if alunos == False:
                raise ConexaoBD()
        except ConexaoBD:
            return None
        else:
            for aluno in alunos:
                listaMatricAluno.append(aluno.nro_matric)
            return listaMatricAluno

    def getNomeAluno(self, matric):
        alunos = self.getListaAlunos()
        try:
            if alunos == False:
                raise ConexaoBD()
        except ConexaoBD:
            return None
        else:
            for aluno in alunos:
                if int(matric) == aluno.nro_matric:
                    return aluno.nome
            return None
            
    #Funções que serão chamadas na Main --- Instaciadores (MENU BAR) ---------------------------

    def insereAlunos(self, root):
        listaCursos = self.ctrlPrincipal.ctrlCurso.getListaNomeCursos()
        if listaCursos == None:
            LimiteMostraAlunos('ERROR', 'Falha de conexão com o Banco de Dados', True)
        else:
            self.limiteIns = LimiteInsereAluno(self, root, listaCursos) 

    def mostraAlunos(self):
        string = 'MATRÍCULA -- NOME -- CURSO\n\n'
        alunos = self.getListaAlunos()
        try:
            if alunos == False:
                raise ConexaoBD()
        except:
            LimiteMostraAlunos('ERROR', 'Falha de conexão com o banco', True)
        else:
            for aluno in alunos: 
                if aluno.curso_id == None:      
                    string += f'* {aluno.nro_matric} -- {aluno.nome} -- SEM CURSO\n'
                else:
                    string += f'* {aluno.nro_matric} -- {aluno.nome} -- {aluno.curso_id}\n'
            self.limiteLista = LimiteMostraAlunos('LISTA DE ALUNOS', string, False)
    
    def relatorioAlunos(self, root):
        alunos = self.getListaAlunos()
        try:
            if alunos == False:
                raise ConexaoBD()
        except:
            LimiteMostraAlunos('ERROR', 'Falha de conexão com o banco', True)
        else:
            LimiteTabelaAlunos(root, alunos)
    
    def consultaAlunos(self, root):
        self.limiteConsulta = LimiteConsultaAluno(self, root)

    def excluiAlunos(self, root):
        self.limiteExclui = LimiteExcluiAluno(self, root)
    
    def atualizaAlunos(self, root):
        listaCursos = self.ctrlPrincipal.ctrlCurso.getListaNomeCursos()
        if listaCursos == None:
            LimiteMostraAlunos('ERROR', 'Falha de conexão com o Banco de Dados', True)
        else:
            self.limiteAtualiza = LimiteAtualizaAluno(self, root, listaCursos)

    #Funções de CRUD dos Buttons ----------------------------------------------------

    def enterHandler(self, event):
        nroMatric = self.limiteIns.inputNro.get()
        nome = self.limiteIns.inputNome.get()
        curso = self.limiteIns.escolhaCombo.get()
        print(curso)
        try:
            if len(nroMatric)==0 or len(nome)==0 or len(curso)==0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteIns.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            aluno = Aluno(nro_matric=nroMatric, nome=nome, curso_id=curso)
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
            pprint(aluno)
            try:
                if aluno == False: raise ConexaoBD()
                if aluno == None: raise AlunoNaoCadastrado()
            except ConexaoBD:
                self.limiteConsulta.mostraMessagebox('ERROR', 'Falha de conexão com o Banco de Dados', True)
            except AlunoNaoCadastrado:
                self.limiteConsulta.mostraMessagebox('ALERTA', 'Aluno não cadastrado', True)
            else:
                if aluno.curso_id == None:
                    string = f'MATRÍCULA -- NOME -- CURSO \n{aluno.nro_matric} -- {aluno.nome} -- SEM CURSO\n'
                else:
                    string = f'MATRÍCULA -- NOME -- CURSO \n{aluno.nro_matric} -- {aluno.nome} -- {aluno.curso_id}\n'
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
        curso = self.limiteAtualiza.escolhaCurso.get()
        try:
            if len(nroMatric) == 0 or len(nome) == 0 or len(curso) == 0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteAtualiza.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            status = ManipulaBanco.atualizaAluno(nroMatric, nome, curso)
            try:
                if status == False:
                    raise AlunoNaoCadastrado()
            except AlunoNaoCadastrado:
                self.limiteAtualiza.mostraMessagebox('ALERTA', 'Aluno não cadastrado ou falha de conexão com o Banco de Dados', True)
            else: 
                self.limiteAtualiza.mostraMessagebox('SUCESSO', 'Nome de aluno e curso atualizado com sucesso', False)
            finally:
                self.limiteAtualiza.atualizarClearAluno(event)