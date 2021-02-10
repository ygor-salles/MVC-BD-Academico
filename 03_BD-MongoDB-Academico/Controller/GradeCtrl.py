from tkinter.constants import ACTIVE
from Model.GradeModel import ManipulaBanco
from DAO.Mapeamento import Grade
from View.GradeView import LimiteGrade

class PreencherCampos(Exception): pass

class PreencherCampoId(Exception): pass

class ConexaoBD(Exception): pass

class ErroRequisicao(Exception): pass

class GradeNaoCadastrado(Exception): pass

class CtrlGrade():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaDiscGrade = []

    def getListaGrades(self):
        return ManipulaBanco.listaGrade()

    # Instanciação da Main ------------------------------------------------------

    def exibirTela(self, frame1, frame2):
        self.listaDiscGrade = []
        listaGrades = self.getListaGrades()
        listaDisc = self.ctrlPrincipal.ctrlDisciplina.getListaDisciplinas()
        self.limite = LimiteGrade(self, frame1, frame2, listaGrades, listaDisc)

    # Função reload na tabela ----------------------------------------------------

    def reloadTabela(self):
        self.limite.tabelaDisc.delete(*self.limite.tabelaDisc.get_children())
        contChild=0
        contParent=0
        for grade in self.getListaGrades():
            self.limite.tabelaDisc.insert(parent='', index='end', iid=contParent, values=(grade.anoCurso))
            for disc in grade.disciplinas:
                contChild += 1
                self.limite.tabelaDisc.insert(parent='', index='end', iid=contChild, values=('', disc['codigo'], disc['nome'], disc['cargaHoraria']))
                self.limite.tabelaDisc.move(f'{contChild}', f'{contParent}', f'{contParent}')
            contParent = contChild+1
            contChild = contParent

    def reloadOneElement(self, grade):
        self.limite.tabelaDisc.delete(*self.limite.tabelaDisc.get_children())
        cont = 0
        self.limite.tabelaDisc.insert(parent='', index='end', iid=0, values=(grade.anoCurso))
        for disc in grade.disciplinas:
            cont += 1
            self.limite.tabelaDisc.insert(parent='', index='end', iid=cont, values=('', disc['codigo'], disc['nome'], disc['cargaHoraria']))
            self.limite.tabelaDisc.move(f'{cont}', '0', '0')

    # Funções auxiliares e de amarrações de classes

    def converteDict(self, listaDiscGrade):
        listaDict = []
        for i in listaDiscGrade:
            listaDict.append({
                '_id': i.id,
                'codigo': i.codigo,
                'nome': i.nome,
                'cargaHoraria': i.cargaHoraria
            })
        return listaDict

    # Funções de CRUD dos buttons ------------------------------------------------

    def buscaGrade(self):
        anoCurso = self.limite.inputGrade.get()
        if len(self.limite.tabelaDisc.get_children())==1 and len(anoCurso)==0:
            self.reloadTabela()
        else:
            try:
                if len(anoCurso)==0: raise PreencherCampoId()
            except PreencherCampoId:
                self.limite.mostraMessagebox('ALERTA', 'Necessário preencher o campo grade para busca', True)
            else:
                grade = ManipulaBanco.consultaGrade(anoCurso)
                try: 
                    if grade == False: raise ConexaoBD()
                    if grade == None: raise GradeNaoCadastrado()
                except ConexaoBD: self.limite.mostraMessagebox('ERROR', 'Falha de conexão com o Banco de Dados', True)
                except GradeNaoCadastrado: self.limite.mostraMessagebox('ERROR', f'Grade {anoCurso} não cadastrada', True)
                else:
                    self.reloadOneElement(grade)
                finally:
                    self.limite.limpaGrade()

    def insereGrade(self):
        anoCurso = self.limite.inputGrade.get()
        discSel = self.limite.listboxDisc.get(ACTIVE)
        try:
            if len(anoCurso)==0 or len(discSel)==0:
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
                self.listaDiscGrade.append(disciplina)
                self.limite.mostraMessagebox('SUCESSO', 'Disciplina inserida na lista', False)
                self.limite.listboxDisc.delete(ACTIVE)

    def cadastraGrade(self):
        anoCurso = self.limite.inputGrade.get()
        try:
            if len(anoCurso)==0:
                raise PreencherCampos()
        except PreencherCampos:
            self.limite.mostraMessagebox('ALERTA', 'Atenção todos os campos devem ser preenchidos para inserção', True)
        else:
            listaDict = self.converteDict(self.listaDiscGrade)
            grade = Grade(anoCurso=anoCurso, disciplinas=listaDict)
            status = ManipulaBanco.cadastraGrade(grade)
            try:
                if status == False: raise ConexaoBD()
            except ConexaoBD:
                self.limite.mostraMessagebox('ERROR', 'Falha de conexão com o Banco de dados', True)
            else:
                self.limite.mostraMessagebox('SUCESSO', 'Grade cadastrada com sucesso', False)
                self.limite.limpaGrade()
                self.reloadTabela()

    def alteraGrade(self):
        print('Alterando Grade')
    #     anoCurso = self.limite.inputGrade.get()
    #     grade = self.limite.inputGrade.get()
    #     try:
    #         if len(anoCurso)==0:
    #             raise PreencherCampoId()
    #     except PreencherCampoId:
    #         self.limite.mostraMessagebox('ALERTA', 'Selecionar o grade que deseja alterar', True)
    #     else:
    #         status = ManipulaBanco.atualizaGrade(anoCurso)
    #         try:
    #             if status == False: raise ConexaoBD()
    #         except ConexaoBD: self.limite.mostraMessagebox('ERROR', 'Falha de conexão com o banco de dados', True)
    #         else:
    #             self.limite.mostraMessagebox('SUCESSO', f'Grade {anoCurso} alterada com sucesso', False)
    #             self.limite.limpaGrade()
    #             self.reloadTabela() 

    def deletaGrade(self):
        anoCurso = self.limite.inputGrade.get()
        try:
            if len(anoCurso)==0:
                raise PreencherCampoId()
        except PreencherCampoId:
            self.limite.mostraMessagebox('ALERTA', 'Necessário informar o campo de grade para deletar', True)
        else:
            status = ManipulaBanco.deletaGrade(anoCurso)
            try:
                if status == False: raise ErroRequisicao()
            except ErroRequisicao:
                self.limite.mostraMessagebox('ERROR', 'Houve erro na requisição ou o dado informado não existe', True)
            else:
                self.limite.mostraMessagebox('SUCESSO', f'Grade {anoCurso} excluído com sucesso', False)
                self.limite.limpaGrade()
                self.reloadTabela()