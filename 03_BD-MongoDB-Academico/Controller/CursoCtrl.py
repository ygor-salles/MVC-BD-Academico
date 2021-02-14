from tkinter.constants import ACTIVE, END
from Model.CursoModel import ManipulaBanco
from DAO.Mapeamento import Curso
from View.CursoView import LimiteAlteraCurso, LimiteCurso

class PreencherCampos(Exception): pass

class PreencherCampoId(Exception): pass

class ConexaoBD(Exception): pass

class ErroRequisicao(Exception): pass

class CursoNaoCadastrado(Exception): pass

class CursoSemAluno(Exception): pass

class CtrlCurso():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaAlunoCurso = []

    def getListaCursos(self):
        return ManipulaBanco.listaCurso()

    # Instanciação da Main ------------------------------------------------------

    def exibirTelaCurso(self, frame1, frame2):
        listaNomeCurso = self.getListaNomeCurso()
        listaCursos = self.getListaCursos()

        listaAlunos = self.ctrlPrincipal.ctrlAluno.getListaMatricAluno()
        #Para inserir no listbox apenas alunos que não estão matriculados em outro curso
        listaMatricExclusiva = []
        for matric in listaAlunos:
            listaMatricExclusiva.append(self.verificaAluno(matric))
        self.limiteAltera = LimiteAlteraCurso(self, frame1, frame2, listaNomeCurso, listaCursos, listaMatricExclusiva)
    
    def exibirTela(self, frame1, frame2):
        self.listaAlunoCurso = []
        listaCursos = self.getListaCursos()

        listaAlunos = self.ctrlPrincipal.ctrlAluno.getListaMatricAluno()
        #Para inserir no listbox apenas alunos que não estão matriculados em outro curso
        listaMatricExclusiva = []
        for matric in listaAlunos:
            listaMatricExclusiva.append(self.verificaAluno(matric))

        listaGrades = self.ctrlPrincipal.ctrlGrade.getListaAnoCurso()
        self.limite = LimiteCurso(self, frame1, frame2, listaCursos, listaMatricExclusiva, listaGrades)

    # Função reload na tabela ----------------------------------------------------

    def reloadTabela(self):
        self.limite.tabelaAl.delete(*self.limite.tabelaAl.get_children())
        contChild=0
        contParent=0
        for curso in self.getListaCursos():
            self.limite.tabelaAl.insert(parent='', index='end', iid=contParent, values=(curso.nome, curso.grade.anoCurso))
            for aluno in curso.alunos:
                contChild += 1
                self.limite.tabelaAl.insert(parent='', index='end', iid=contChild, values=('', '', aluno['matricula'], aluno['nome'], aluno['curso']))
                self.limite.tabelaAl.move(f'{contChild}', f'{contParent}', f'{contParent}')
            contParent = contChild+1
            contChild = contParent

    def reloadOneElement(self, curso):
        self.limite.tabelaAl.delete(*self.limite.tabelaAl.get_children())
        cont = 0
        self.limite.tabelaAl.insert(parent='', index='end', iid=0, values=(curso.nome, curso.grade.anoCurso))
        for aluno in curso.alunos:
            cont += 1
            self.limite.tabelaAl.insert(parent='', index='end', iid=cont, values=('', '', aluno['matricula'], aluno['nome'], aluno['curso']))
            self.limite.tabelaAl.move(f'{cont}', '0', '0')

    def reloadTabelaAltera(self):
        self.limiteAltera.tabelaAl.delete(*self.limiteAltera.tabelaAl.get_children())
        contChild=0
        contParent=0
        for curso in self.getListaCursos():
            self.limiteAltera.tabelaAl.insert(parent='', index='end', iid=contParent, values=(curso.nome, curso.grade.anoCurso))
            for aluno in curso.alunos:
                contChild += 1
                self.limiteAltera.tabelaAl.insert(parent='', index='end', iid=contChild, values=('', '', aluno['matricula'], aluno['nome'], aluno['curso']))
                self.limiteAltera.tabelaAl.move(f'{contChild}', f'{contParent}', f'{contParent}')
            contParent = contChild+1
            contChild = contParent

    # Funções auxiliares e de amarrações de classes ------------------------------------

    def converteDict(self, listaAlunoCurso):
        listaDict = []
        for i in listaAlunoCurso:
            listaDict.append({
                '_id': i.id,
                'matricula': i.matricula,
                'nome': i.nome,
                'curso': i.curso
            })
        return listaDict

    def getListaNomeCurso(self):
        listaNomeCurso = []
        listaCursos = self.getListaCursos()
        try:
            if listaCursos == False: raise ConexaoBD()
        except ConexaoBD():
            return None
        else:
            for curso in listaCursos:
                listaNomeCurso.append(curso.nome)
            return listaNomeCurso

    def getAlunoCurso(self, matricula):
        listaAlunoCurso = self.limiteAltera.listaCursoAl
        for aluno in listaAlunoCurso:
            if aluno['matricula'] == matricula:
                return aluno
        return None 

    def verificaAluno(self, matricula):
        listaCursos = self.getListaCursos()
        try:
            if listaCursos == False: raise ConexaoBD()
        except ConexaoBD(): return False
        else:
            for curso in listaCursos:
                for aluno in curso.alunos:
                    if aluno['matricula'] == matricula:
                        return None
            return matricula

    # Funções de CRUD dos buttons ------------------------------------------------

    def buscaCurso(self):
        nomeCurso = self.limite.inputCurso.get()
        if len(self.limite.tabelaAl.get_children())==1 and len(nomeCurso)==0:
            self.reloadTabela()
        else:
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
                except CursoNaoCadastrado: self.limite.mostraMessagebox('ERROR', f'Curso {nomeCurso} não cadastrada', True)
                else:
                    self.reloadOneElement(curso)
                finally:
                    self.limite.limpaCurso()

    def insereAl(self):
        nomeCurso = self.limite.inputCurso.get()
        alunoSel = self.limite.listboxAluno.get(ACTIVE)
        grade = self.limite.escolhaGrade.get()
        try:
            if len(nomeCurso)==0 or len(str(alunoSel))==0 or len(grade)==0:
                raise PreencherCampos()
        except PreencherCampos:
            self.limite.mostraMessagebox('ALERTA', 'Atenção todos os campos devem ser preenchidos para inserção', True)
        else:
            aluno = self.ctrlPrincipal.ctrlAluno.getAlunoByCode(alunoSel)
            try:
                if aluno == None: raise ErroRequisicao()
            except ErroRequisicao: self.limite.mostraMessagebox('ERROR', 'Houve erro na requisição', True)
            else:
                self.listaAlunoCurso.append(aluno)
                self.limite.mostraMessagebox('SUCESSO', 'Aluno inserido na lista', False)
                self.limite.listboxAluno.delete(ACTIVE)

    def cadastraCurso(self):
        nomeCurso = self.limite.inputCurso.get()
        anoCurso = self.limite.escolhaGrade.get()
        try:
            if len(nomeCurso)==0 or len(anoCurso)==0: raise PreencherCampos()
        except PreencherCampos:
            self.limite.mostraMessagebox('ALERTA', 'Atenção todos os campos devem ser preenchidos para inserção', True)
        else:
            listaDict = self.converteDict(self.listaAlunoCurso)
            grade = self.ctrlPrincipal.ctrlGrade.getObjGrade(anoCurso)
            curso = Curso(nome=nomeCurso, alunos=listaDict, grade=grade)
            status = ManipulaBanco.cadastraCurso(curso)
            try:
                if status == False: raise ConexaoBD()
            except ConexaoBD:
                self.limite.mostraMessagebox('ERROR', 'Falha de conexão com o Banco de dados', True)
            else:
                self.limite.mostraMessagebox('SUCESSO', 'Curso cadastrado com sucesso', False)
                self.limite.limpaCurso()
                self.reloadTabela() 

    def deletaCurso(self):
        nomeCurso = self.limite.inputCurso.get()
        try:
            if len(nomeCurso)==0: raise PreencherCampoId()
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

    # Funções da tela altera curso ----------------------------------------------------------
    
    def adicionaAluno(self):
        nomeCurso = self.limiteAltera.escolhaCurso.get()
        alunoSel = self.limiteAltera.listboxAdd.get(ACTIVE)
        try:
            if len(nomeCurso)==0 or len(str(alunoSel))==0:
                raise PreencherCampos()
        except PreencherCampos:
            self.limiteAltera.mostraMessagebox('ALERTA', 'Todos os campos devem ser preenchidos', True)
        else:
            aluno = self.ctrlPrincipal.ctrlAluno.getAlunoByCode(alunoSel)
            try:
                if aluno == None: raise ErroRequisicao()
            except ErroRequisicao:
                self.limite.mostraMessagebox('ERROR', 'Houve erro na requisição', True)
            else:
                self.limiteAltera.listaCursoAl.append({
                    '_id': aluno.id,
                    'matricula': aluno.matricula,
                    'nome': aluno.nome,
                    'curso': aluno.curso
                })
                self.limiteAltera.mostraMessagebox('SUCESSO', 'Aluno inserido na lista', False)
                self.limiteAltera.listboxAdd.delete(ACTIVE)
                self.limiteAltera.listboxRemove.insert(END, alunoSel)

    def removeAluno(self):
        nomeCurso = self.limiteAltera.escolhaCurso.get()
        alunoSel = self.limiteAltera.listboxRemove.get(ACTIVE)
        try:
            if len(nomeCurso)==0 or len(str(alunoSel))==0:
                raise PreencherCampos()
        except PreencherCampos:
            self.limiteAltera.mostraMessagebox('ALERTA', 'Todos os campos devem ser preenchidos', True)
        else:
            aluno = self.getAlunoCurso(alunoSel)
            try:
                if aluno == None: raise ErroRequisicao()
            except ErroRequisicao:
                self.limite.mostraMessagebox('ERROR', 'Houve erro na requisição', True)
            else:
                self.limiteAltera.listaCursoAl.remove(aluno)
                self.limiteAltera.mostraMessagebox('SUCESSO', 'Aluno removido da lista', False)
                self.limiteAltera.listboxRemove.delete(ACTIVE)
                status = self.ctrlPrincipal.ctrlAluno.getAlunoByCode(alunoSel)
                if status != None:
                    self.limiteAltera.listboxAdd.insert(END, alunoSel)
    
    def atualizaCurso(self):
        nomeCurso = self.limiteAltera.escolhaCurso.get()
        alunos = self.limiteAltera.listaCursoAl
        try:
            if len(nomeCurso)==0: raise PreencherCampoId()
            if len(alunos)==0: raise CursoSemAluno()
        except PreencherCampoId:
            self.limiteAltera.mostraMessagebox('ALERTA', 'Campo Ano/Curso deve ser preenchido', True)
        except CursoSemAluno:
            self.limiteAltera.mostraMessagebox('ATENÇÃO', 'O curso deve ter no mínimo um aluno', True)
        else:
            status = ManipulaBanco.atualizaCurso(nomeCurso, alunos)
            try:
                if status == False: raise ConexaoBD()
            except ConexaoBD:
                self.limiteAltera.mostraMessagebox('ERROR', 'Falha de conexão com o Banco de Dados', True)
            else:
                self.limiteAltera.mostraMessagebox('SUCESSO', f'Curso {nomeCurso} atualizado com sucesso', False)
                self.limiteAltera.fechaJanela()