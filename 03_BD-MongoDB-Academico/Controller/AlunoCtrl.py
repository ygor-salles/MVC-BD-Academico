from Model.AlunoModel import ManipulaBanco
from DAO.Mapeamento import Aluno
from View.AlunoView import LimiteAluno

class PreencherCampos(Exception): pass

class PreencherCampoId(Exception): pass

class ConexaoBD(Exception): pass

class ErroRequisicao(Exception): pass

class AlunoNaoCadastrado(Exception): pass

class CtrlAluno():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal

    def getListaAlunos(self):
        return ManipulaBanco.listaAluno()

    # Instanciação da Main ------------------------------------------------------

    def exibirTela(self, frame1, frame2):
        listaAlunos = self.getListaAlunos()
        self.limite = LimiteAluno(self, frame1, frame2, listaAlunos)

    # Função reload na tabela ----------------------------------------------------

    def reloadTabela(self):
        self.limite.tabelaDisc.delete(*self.limite.tabelaDisc.get_children())
        for aluno in self.getListaAlunos():
            self.limite.tabelaDisc.insert('', 'end', values=(aluno.matricula, aluno.nome, aluno.curso))

    def preencheTabela(self):
        for aluno in self.getListaAlunos():
            self.limite.tabelaDisc.insert('', 'end', values=(aluno.matricula, aluno.nome, aluno.curso))
    
    # Funções de CRUD dos buttons ------------------------------------------------

    def buscaAluno(self):
        if len(self.limite.tabelaDisc.get_children())==1:
            self.reloadTabela()
        else:
            matricula = self.limite.inputMatric.get()
            try:
                if len(matricula)==0: raise PreencherCampoId()
            except PreencherCampoId:
                self.limite.mostraMessagebox('ALERTA', 'Necessário preencher o campo matrícula para busca', True)
            else:
                aluno = ManipulaBanco.consultaAluno(int(matricula))
                try: 
                    if aluno == False: raise ConexaoBD()
                    if aluno == None: raise AlunoNaoCadastrado()
                except ConexaoBD: self.limite.mostraMessagebox('ERROR', 'Falha de conexão com o Banco de Dados', True)
                except AlunoNaoCadastrado: self.limite.mostraMessagebox('ERROR', f'Aluno {matricula} não cadastrado', True)
                else:
                    self.limite.tabelaDisc.delete(*self.limite.tabelaDisc.get_children())
                    self.limite.tabelaDisc.insert('', 'end', values=(aluno.matricula, aluno.nome, aluno.curso))
                finally:
                    self.limite.limpaAluno()

    def insereAluno(self):
        matricula = self.limite.inputMatric.get()
        nome = self.limite.inputNome.get()
        curso = self.limite.inputCurso.get()
        try:
            if len(matricula)==0 or len(nome)==0 or len(curso)==0:
                raise PreencherCampos()
        except PreencherCampos:
            self.limite.mostraMessagebox('ALERTA', 'Atenção todos os campos devem ser preenchidos para inserção', True)
        else:
            aluno = Aluno(matricula=int(matricula), nome=nome, curso=curso)
            status = ManipulaBanco.cadastraAluno(aluno)
            try:
                if status == False:
                    raise ErroRequisicao()
            except ErroRequisicao:
                self.limite.mostraMessagebox('ERROR', 'Houve erro na requisição ou matrícula já existente', True)
            else:
                self.limite.mostraMessagebox('SUCESSO', 'Aluno inserido com sucesso', False)
                self.limite.limpaAluno()
                self.reloadTabela()

    def alteraAluno(self):
        matricula = self.limite.inputMatric.get()
        nome = self.limite.inputNome.get()
        curso = self.limite.inputCurso.get()
        try:
            if len(matricula)==0 or len(nome)==0 or len(curso)==0:
                raise PreencherCampoId()
        except PreencherCampoId:
            self.limite.mostraMessagebox('ALERTA', 'Selecionar o aluno que deseja alterar', True)
        else:
            status = ManipulaBanco.atualizaAluno(int(matricula), nome, curso)
            try:
                if status == False: raise ConexaoBD()
            except ConexaoBD: self.limite.mostraMessagebox('ERROR', 'Falha de conexão com o banco de dados', True)
            else:
                self.limite.mostraMessagebox('SUCESSO', f'Aluno {matricula} alterada com sucesso', False)
                self.limite.limpaAluno()
                self.reloadTabela() 

    def deletaAluno(self):
        matricula = self.limite.inputMatric.get()
        try:
            if len(matricula)==0:
                raise PreencherCampoId()
        except PreencherCampoId:
            self.limite.mostraMessagebox('ALERTA', 'Necessário informar o campo de matrícula para deletar', True)
        else:
            status = ManipulaBanco.deletaAluno(int(matricula))
            try:
                if status == False: raise ErroRequisicao()
            except ErroRequisicao:
                self.limite.mostraMessagebox('ERROR', 'Houve erro na requisição ou o dado informado não existe', True)
            else:
                self.limite.mostraMessagebox('SUCESSO', f'Aluno {matricula} excluído com sucesso', False)
                self.limite.limpaAluno()
                self.reloadTabela()