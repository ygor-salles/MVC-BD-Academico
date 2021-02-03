from Model.DisciplinaModel import ManipulaBanco
from DAO.Mapeamento import Disciplina
from View.DisciplinaView import LimiteDisciplina

class PreencherCampos(Exception): pass

class PreencherCampoId(Exception): pass

class ConexaoBD(Exception): pass

class ErroRequisicao(Exception): pass

class DisciplinaNaoCadastrada(Exception): pass

class CtrlDisciplina():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal

    def getListaDisciplinas(self):
        return ManipulaBanco.listaDisciplina()

    # Instanciação da Main ------------------------------------------------------

    def exibirTela(self, frame1, frame2):
        listaDisciplinas = self.getListaDisciplinas()
        self.limite = LimiteDisciplina(self, frame1, frame2, listaDisciplinas)

    # Função reload na tabela ----------------------------------------------------

    def reloadTabela(self):
        self.limite.tabelaDisc.delete(*self.limite.tabelaDisc.get_children())
        for disc in self.getListaDisciplinas():
            self.limite.tabelaDisc.insert('', 'end', values=(disc.codigo, disc.nome, disc.cargaHoraria))

    def preencheTabela(self):
        for disc in self.getListaDisciplinas():
            self.limite.tabelaDisc.insert('', 'end', values=(disc.codigo, disc.nome, disc.cargaHoraria))
    
    # Funções de CRUD dos buttons ------------------------------------------------

    def buscaDisciplina(self):
        if len(self.limite.tabelaDisc.get_children())==1:
            self.reloadTabela()
        else:
            codDisc = self.limite.inputCodigo.get()
            try:
                if len(codDisc)==0: raise PreencherCampoId()
            except PreencherCampoId:
                self.limite.mostraMessagebox('ALERTA', 'Necessário preencher o campo código para busca', True)
            else:
                disc = ManipulaBanco.consultaDisciplina(codDisc)
                try: 
                    if disc == False: raise ConexaoBD()
                    if disc == None: raise DisciplinaNaoCadastrada()
                except ConexaoBD: self.limite.mostraMessagebox('ERROR', 'Falha de conexão com o Banco de Dados', True)
                except DisciplinaNaoCadastrada: self.limite.mostraMessagebox('ERROR', f'Disciplina {codDisc} não cadastrada', True)
                else:
                    self.limite.tabelaDisc.delete(*self.limite.tabelaDisc.get_children())
                    self.limite.tabelaDisc.insert('', 'end', values=(disc.codigo, disc.nome, disc.cargaHoraria))
                finally:
                    self.limite.limpaDisciplina()

    def insereDisciplina(self):
        codigo = self.limite.inputCodigo.get()
        nome = self.limite.inputNome.get()
        cargaHoraria = self.limite.inputCargaHoraria.get()
        try:
            if len(codigo)==0 or len(nome)==0 or len(cargaHoraria)==0:
                raise PreencherCampos()
        except PreencherCampos:
            self.limite.mostraMessagebox('ALERTA', 'Atenção todos os campos devem ser preenchidos para inserção', True)
        else:
            disc = Disciplina(codigo=codigo, nome=nome, cargaHoraria=int(cargaHoraria))
            status = ManipulaBanco.cadastraDisciplina(disc)
            try:
                if status == False:
                    raise ConexaoBD()
            except ConexaoBD:
                self.limite.mostraMessagebox('ERROR', 'Falha de conexão com o banco de dados')
            else:
                self.limite.mostraMessagebox('SUCESSO', 'Disciplina inserida com sucesso', False)
                self.limite.limpaDisciplina()
                self.reloadTabela()

    def alteraDisciplina(self):
        codigo = self.limite.inputCodigo.get()
        nome = self.limite.inputNome.get()
        ch = self.limite.inputCargaHoraria.get()
        try:
            if len(codigo)==0 or len(nome)==0 or len(ch)==0:
                raise PreencherCampoId()
        except PreencherCampoId:
            self.limite.mostraMessagebox('ALERTA', 'Selecionar a disciplina que deseja alterar', True)
        else:
            status = ManipulaBanco.atualizaDisciplina(codigo, nome, int(ch))
            try:
                if status == False: raise ConexaoBD()
            except ConexaoBD: self.limite.mostraMessagebox('ERROR', 'Falha de conexão com o banco de dados', True)
            else:
                self.limite.mostraMessagebox('SUCESSO', f'Disciplina {codigo} alterada com sucesso', False)
                self.limite.limpaDisciplina()
                self.reloadTabela() 

    def deletaDisciplina(self):
        codigo = self.limite.inputCodigo.get()
        try:
            if len(codigo)==0:
                raise PreencherCampoId()
        except PreencherCampoId:
            self.limite.mostraMessagebox('ALERTA', 'Necessário informar o campo de código para deletar', True)
        else:
            status = ManipulaBanco.deletaDisciplina(codigo)
            try:
                if status == False: raise ErroRequisicao()
            except ErroRequisicao:
                self.limite.mostraMessagebox('ERROR', 'Houve erro na requisição ou o dado informado não existe', True)
            else:
                self.limite.mostraMessagebox('SUCESSO', f'Disciplina {codigo} excluída com sucesso', False)
                self.limite.limpaDisciplina()
                self.reloadTabela()