from tkinter.constants import ACTIVE
from Model.CursoGradeModel import ManipulaBanco
from DAO.Mapeamento import Curso, Disciplina, Grade
from View.CursoGradeView import LimiteCurso

class PreencherCampos(Exception): pass

class PreencherCampoId(Exception): pass

class ConexaoBD(Exception): pass

class ErroRequisicao(Exception): pass

class CursoNaoCadastrado(Exception): pass

class CtrlCurso():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaDiscCurso = []

    def getListaCursos(self):
        return ManipulaBanco.listaCurso()

    # Instanciação da Main ------------------------------------------------------

    def exibirTela(self, frame1, frame2):
        self.listaDiscCurso = []
        listaCursos = self.getListaCursos()
        listaDisc = self.ctrlPrincipal.ctrlDisciplina.getListaDisciplinas()
        self.limite = LimiteCurso(self, frame1, frame2, listaCursos, listaDisc)

    # Função reload na tabela ----------------------------------------------------

    def reloadTabela(self):
        self.limite.tabelaDisc.delete(*self.limite.tabelaDisc.get_children())
        for curso in self.getListaCursos():
            self.limite.tabelaDisc.insert(parent='', index='end', values=(curso.nome, curso.grade.ano))
            for disc in curso.grade.disciplinas:
                self.limite.tabelaDisc.insert(parent='', index='end', values=(disc.codigo, disc.nome, disc.cargaHoraria))
 
    # Funções de CRUD dos buttons ------------------------------------------------

    def buscaCurso(self):
        if len(self.limite.tabelaDisc.get_children())==1:
            self.reloadTabela()
        else:
            nomeCurso = self.limite.inputCurso.get()
            try:
                if len(nomeCurso)==0: raise PreencherCampoId()
            except PreencherCampoId:
                self.limite.mostraMessagebox('ALERTA', 'Necessário preencher o campo curso para busca', True)
            else:
                curso = ManipulaBanco.consultaCurso(nomeCurso)
                try: 
                    if curso == False: raise ConexaoBD()
                    if curso == None: raise CursoNaoCadastrado()
                except ConexaoBD: self.limite.mostraMessagebox('ERROR', 'Falha de conexão com o Banco de Dados', True)
                except CursoNaoCadastrado: self.limite.mostraMessagebox('ERROR', f'Curso {nomeCurso} não cadastrado', True)
                else:
                    self.limite.tabelaDisc.delete(*self.limite.tabelaDisc.get_children())
                    self.limite.tabelaDisc.insert(parent='', index='end', values=(curso.nome, curso.grade.ano))
                    for disc in curso.grade.disciplinas:
                        self.limite.tabelaDisc.insert(parent='', index='end', values=(disc.codigo, disc.nome, disc.cargaHoraria))
                finally:
                    self.limite.limpaCurso()

    def insereCurso(self):
        nomeCurso = self.limite.inputCurso.get()
        anoGrade = self.limite.inputGrade.get()
        discSel = self.limite.listboxDisc.get(ACTIVE)
        try:
            if len(nomeCurso)==0 or len(anoGrade)==0 or len(discSel)==0:
                raise PreencherCampos()
        except PreencherCampos:
            self.limite.mostraMessagebox('ALERTA', 'Atenção todos os campos devem ser preenchidos para inserção', True)
        else:
            disciplina = self.ctrlPrincipal.ctrlDisciplina.getDisciplinaByCode(discSel)
            try:
                if disciplina == None:
                    raise ErroRequisicao()
            except ErroRequisicao:
                self.limite.mostraMessagebox('ERROR', 'Houve erro na requisição', True)
            else:
                self.listaDiscCurso.append(disciplina)
                self.limite.mostraMessagebox('SUCESSO', 'Disciplina inserida na lista', False)
                self.limite.listboxDisc.delete(ACTIVE)

    def cadastraCurso(self):
        nomeCurso = self.limite.inputCurso.get()
        anoGrade = self.limite.inputGrade.get()
        discSel = self.limite.listboxDisc.get(ACTIVE)
        try:
            if len(nomeCurso)==0 or len(anoGrade)==0 or len(discSel)==0:
                raise PreencherCampos()
        except PreencherCampos:
            self.limite.mostraMessagebox('ALERTA', 'Atenção todos os campos devem ser preenchidos para inserção', True)
        else:
            grade = Grade(ano=anoGrade, disciplinas=self.listaDiscCurso)
            curso = Curso(nome=nomeCurso, grade=grade)
            status = ManipulaBanco.cadastraCurso(curso)
            try:
                if status == False: raise ConexaoBD()
            except ConexaoBD:
                self.limite.mostraMessagebox('ERROR', 'Falha de conexão com o Banco de dados', True)
            else:
                self.limite.mostraMessagebox('SUCESSO', 'Curso cadastrado com sucesso', False)
                self.limite.limpaCurso()
                self.reloadTabela()

    def alteraCurso(self):
        nomeCurso = self.limite.inputCurso.get()
        grade = self.limite.inputGrade.get()
        try:
            if len(nomeCurso)==0 or len(grade)==0:
                raise PreencherCampoId()
        except PreencherCampoId:
            self.limite.mostraMessagebox('ALERTA', 'Selecionar o curso que deseja alterar', True)
        else:
            status = ManipulaBanco.atualizaCurso(nomeCurso, int(grade))
            try:
                if status == False: raise ConexaoBD()
            except ConexaoBD: self.limite.mostraMessagebox('ERROR', 'Falha de conexão com o banco de dados', True)
            else:
                self.limite.mostraMessagebox('SUCESSO', f'Curso {nomeCurso} alterada com sucesso', False)
                self.limite.limpaCurso()
                self.reloadTabela() 

    def deletaCurso(self):
        nomeCurso = self.limite.inputCurso.get()
        try:
            if len(nomeCurso)==0:
                raise PreencherCampoId()
        except PreencherCampoId:
            self.limite.mostraMessagebox('ALERTA', 'Necessário informar o campo de curso para deletar', True)
        else:
            status = ManipulaBanco.deletaCurso(nomeCurso)
            try:
                if status == False: raise ErroRequisicao()
            except ErroRequisicao:
                self.limite.mostraMessagebox('ERROR', 'Houve erro na requisição ou o dado informado não existe', True)
            else:
                self.limite.mostraMessagebox('SUCESSO', f'Curso {nomeCurso} excluído com sucesso', False)
                self.limite.limpaCurso()
                self.reloadTabela()