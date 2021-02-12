from tkinter.constants import ACTIVE, END
from Model.GradeModel import ManipulaBanco
from DAO.Mapeamento import Grade
from View.GradeView import LimiteAlteraGrade, LimiteGrade

class PreencherCampos(Exception): pass

class PreencherCampoId(Exception): pass

class ConexaoBD(Exception): pass

class ErroRequisicao(Exception): pass

class GradeNaoCadastrado(Exception): pass

class GradeSemDisciplina(Exception): pass

class CtrlGrade():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaDiscGrade = []

    def getListaGrades(self):
        return ManipulaBanco.listaGrade()

    # Instanciação da Main ------------------------------------------------------

    def exibirTelaGrade(self, frame1, frame2):
        listaAnoCurso = self.getListaAnoCurso()
        listaGrades = self.getListaGrades()
        listaDisc = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisc()
        self.limiteAltera = LimiteAlteraGrade(self, frame1, frame2, listaAnoCurso, listaGrades, listaDisc)
    
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

    def reloadTabelaAltera(self):
        self.limiteAltera.tabelaDisc.delete(*self.limiteAltera.tabelaDisc.get_children())
        contChild=0
        contParent=0
        for grade in self.getListaGrades():
            self.limiteAltera.tabelaDisc.insert(parent='', index='end', iid=contParent, values=(grade.anoCurso))
            for disc in grade.disciplinas:
                contChild += 1
                self.limiteAltera.tabelaDisc.insert(parent='', index='end', iid=contChild, values=('', disc['codigo'], disc['nome'], disc['cargaHoraria']))
                self.limiteAltera.tabelaDisc.move(f'{contChild}', f'{contParent}', f'{contParent}')
            contParent = contChild+1
            contChild = contParent

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

    def getListaAnoCurso(self):
        listaAnoCurso = []
        listaGrades = self.getListaGrades()
        try:
            if listaGrades == False: raise ConexaoBD()
        except ConexaoBD():
            return None
        else:
            for grade in listaGrades:
                listaAnoCurso.append(grade.anoCurso)
            return listaAnoCurso

    def getListaDiscGrade(self):
        listaDiscGrade = []
        


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

    # Funções da tela altera grade ----------------------------------------------------------
    
    def adicionaGrade(self):
        anoCurso = self.limiteAltera.escolhaGrade.get()
        discSel = self.limiteAltera.listboxAdd.get(ACTIVE)
        try:
            if len(anoCurso)==0 or len(discSel)==0:
                raise PreencherCampos()
        except PreencherCampos:
            self.limiteAltera.mostraMessagebox('ALERTA', 'Todos os campos devem ser preenchidos', True)
        else:
            disciplina = self.ctrlPrincipal.ctrlDisciplina.getDisciplinaByCode(discSel)
            try:
                if disciplina == None: raise ErroRequisicao()
            except ErroRequisicao:
                self.limite.mostraMessagebox('ERROR', 'Houve erro na requisição', True)
            else:
                self.limiteAltera.listaGradeDisc.append({
                    '_id': disciplina.id,
                    'codigo': disciplina.codigo,
                    'nome': disciplina.nome,
                    'cargaHoraria': disciplina.cargaHoraria
                })
                self.limiteAltera.mostraMessagebox('SUCESSO', 'Disciplina inserida na lista', False)
                self.limiteAltera.listboxAdd.delete(ACTIVE)
                self.limiteAltera.listboxRemove.insert(END, discSel)

    def removeGrade(self):
        anoCurso = self.limiteAltera.escolhaGrade.get()
        discSel = self.limiteAltera.listboxRemove.get(ACTIVE)
        try:
            if len(anoCurso)==0 or len(discSel)==0:
                raise PreencherCampos()
        except PreencherCampos:
            self.limiteAltera.mostraMessagebox('ALERTA', 'Todos os campos devem ser preenchidos', True)
        else:
            disciplina = self.ctrlPrincipal.ctrlDisciplina.getDisciplinaByCode(discSel)
            try:
                if disciplina == None: raise ErroRequisicao()
            except ErroRequisicao:
                self.limite.mostraMessagebox('ERROR', 'Houve erro na requisição', True)
            else:
                self.limiteAltera.listaGradeDisc.remove(disciplina)
                self.limiteAltera.mostraMessagebox('SUCESSO', 'Disciplina removida da lista', False)
                self.limiteAltera.listboxRemove.delete(ACTIVE)
                self.limiteAltera.listboxAdd.insert(END, discSel)
    
    def atualizaGrade(self):
        anoCurso = self.limiteAltera.escolhaGrade.get()
        disciplinas = self.limiteAltera.listaGradeDisc
        try:
            if len(anoCurso)==0: raise PreencherCampoId()
            if len(disciplinas)==0: raise GradeSemDisciplina()
        except PreencherCampoId:
            self.limiteAltera.mostraMessagebox('ALERTA', 'Campo Ano/Curso deve ser preenchido', True)
        except GradeSemDisciplina:
            self.limiteAltera.mostraMessagebox('ATENÇÃO', 'A grade deve ter no mínimo uma disciplina', True)
        else:
            status = ManipulaBanco.atualizaGrade(anoCurso, disciplinas)
            try:
                if status == False: raise ConexaoBD()
            except ConexaoBD:
                self.limiteAltera.mostraMessagebox('ERROR', 'Falha de conexão com o Banco de Dados', True)
            else:
                self.limiteAltera.mostraMessagebox('SUCESSO', f'Grade {anoCurso} atualizada com sucesso', False)
                self.reloadTabelaAltera()