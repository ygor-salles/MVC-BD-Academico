from View.GradeView import *
from DAO.Mapeamento import Grade, GradeDisciplina
from Model.GradeModel import ManipulaBanco

class GradeDuplicada(Exception): pass

class GradeNaoCadastrada(Exception): pass

class CamposNaoPreenchidos(Exception): pass 

class ConexaoBD(Exception): pass

class CtrlGrade():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaDiscGrade = []
        self.testePopula = False
        self.listaGradeCodDisc = []

    def getListaGrades(self):
        return ManipulaBanco.listaGrades() 
            
    #Funções que serão chamadas na Main --- Instaciadores (MENU BAR) ---------------------------

    def insereGrades(self, root):
        self.listaDiscGrade = []
        listaCursos = self.ctrlPrincipal.ctrlCurso.getListaNomeCursos()
        listaDisciplinas = self.ctrlPrincipal.ctrlDisciplina.getListaCodDiscAtivas()
        if listaCursos == None:
            LimiteMostraGrades('ERROR', 'Falha de conexão com Banco de Dados', True)
        else:
            self.limiteIns = LimiteInsereGrade(self, root, listaCursos, listaDisciplinas) 

    def relatorioGrade(self, root):
        grades = self.getListaGrades()
        try:
            if grades == False:
                raise ConexaoBD()
        except:
            LimiteMostraGrades('ERROR', 'Falha de conexão com o banco', True)
        else:
            LimiteTabelaGrades(root, grades)
    
    def consultaGrades(self, root):
        listaCursos = self.ctrlPrincipal.ctrlCurso.getListaNomeCursos()
        listaAno = self.getlistaGradeById()
        if listaCursos == None or listaAno == None:
            LimiteMostraGrades('ERROR', 'Falha de conexão com Banco de Dados', True)
        else:
            self.limiteConsulta = LimiteConsultaGrade(self, root, listaCursos, listaAno)

    def excluiGrades(self, root):
        listaCursos = self.ctrlPrincipal.ctrlCurso.getListaNomeCursos()
        listaAno = self.getlistaGradeById()
        if listaCursos == None or listaAno == None:
            LimiteMostraGrades('ERROR', 'Falha de conexão com Banco de Dados', True)
        else:
            self.limiteExclui = LimiteExcluiGrade(self, root, listaAno, listaCursos)
    
    def atualizaGrades(self, root):
        listaCursos = self.ctrlPrincipal.ctrlCurso.getListaNomeCursos()
        listaAno = self.getlistaGradeById()
        if listaCursos == None or listaAno == None:
            LimiteMostraGrades('ERROR', 'Falha de conexão com Banco de Dados', True)
        else:
            self.limiteAtualiza = LimiteAtualizaGrade(self, root, listaAno, listaCursos)

    #Funções auxiliares e de amarrações da classe ---------------------------------------------
    
    def getlistaGradeById(self):
        listaGradeById = []
        grades = self.getListaGrades()
        try:
            if grades == False:
                raise ConexaoBD()
        except ConexaoBD:
            return None
        else:
            for grade in grades:
                listaGradeById.append(grade.ano)
            return listaGradeById

    def getListaGradeCodDisc(self, cursoCombo, anoCombo):
        listaGradeCodDisc = []
        for grade in self.getListaGrades():
            if cursoCombo==grade.curso_id and anoCombo==str(grade.ano):
                for disc in grade.disciplinas:
                    listaGradeCodDisc.append(disc.codigo)
                return listaGradeCodDisc

    #Funções de CRUD dos Buttons ----------------------------------------------------

    # inserção ----------------------------------
    def insereDisciplina(self, event):
        ano = self.limiteIns.inputAno.get()
        cursoSelecionado = self.limiteIns.escolhaCurso.get()
        discSelecionada = self.limiteIns.listbox.get(tk.ACTIVE)
        try:
            if len(ano)==0 or len(cursoSelecionado)==0 or len(discSelecionada)==0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteIns.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            self.listaDiscGrade.append(discSelecionada)
            self.limiteIns.mostraMessagebox('SUCESSO', 'Disciplina inserida na lista', False)
            self.limiteIns.listbox.delete(tk.ACTIVE)

    def criaGrade(self, event):
        ano = self.limiteIns.inputAno.get()
        cursoSelecionado = self.limiteIns.escolhaCurso.get()
        try:
            if len(ano)==0 or len(cursoSelecionado)==0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteIns.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            relacionamento = []
            grade = Grade(ano=ano, curso_id=cursoSelecionado)
            ManipulaBanco.cadastraGrade(grade)
            for i in self.listaDiscGrade:
                grade_disc = GradeDisciplina(grade_id_ano=ano, grade_id_curso=cursoSelecionado, disciplina_id=i)
                relacionamento.append(grade_disc)
            ManipulaBanco.cadastraGradeDisciplina(relacionamento)
            self.limiteIns.mostraMessagebox('SUCESSO', 'Disciplina inseridas na grade %s com sucesso'%ano, False)
            self.limiteIns.janela.destroy()
        
    # consulta ----------------------------------
    def gradeConsulta(self, event):
        ano = self.limiteConsulta.escolhaAno.get()
        curso = self.limiteConsulta.escolhaCurso.get()
        try:
            if len(ano) == 0 or len(curso) == 0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteConsulta.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            grade = ManipulaBanco.consultaGrade(ano, curso)
            try:
                if grade == False: raise ConexaoBD()
                if grade == None: raise GradeNaoCadastrada()
            except ConexaoBD:
                self.limiteConsulta.mostraMessagebox('ERROR', 'Falha de conexão com o Banco de Dados', True)
            except GradeNaoCadastrada:
                self.limiteConsulta.mostraMessagebox('ALERTA', 'Grade não cadastrada', True)
            else:
                string = f'Grade: {grade.ano}\n'
                string += f'Curso: {grade.curso_id}\n'
                string += '\nDisciplinas da grade: '
                for disc in grade.disciplinas:
                    string += f'\n{disc.codigo} -- {disc.nome} -- {disc.carga_horaria}hr'
                LimiteMostraGrades('CONSULTA GRADE', string, False)
            finally:
                self.limiteConsulta.clearConsulta(event)
            
    # deleta ----------------------------------
    def gradeDelete(self, event):
        ano = self.limiteExclui.escolhaAno.get()
        curso = self.limiteExclui.escolhaCurso.get()
        try:
            if len(ano)==0 or len(curso)==0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteExclui.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            status = ManipulaBanco.deletaGrade(ano, curso)
            try:
                if status == False:
                    raise GradeNaoCadastrada()
            except GradeNaoCadastrada:
                self.limiteExclui.mostraMessagebox('ALERTA', 'Grade não cadastrada ou falha de conexão com Banco de Dados', True)
            else:
                self.limiteExclui.mostraMessagebox('SUCESSO', 'Grade deletada com sucesso', False)
            finally:
                self.limiteExclui.clearExclusao(event)

    # atualização ----------------------------------

    def popular(self, event):
        #para os listBox's
        comboCurso = self.limiteAtualiza.escolhaCurso.get()
        comboAno = self.limiteAtualiza.escolhaGrade.get()
        self.listaGradeCodDisc = self.getListaGradeCodDisc(comboCurso, comboAno)
        listaTodasDisciplinas = self.ctrlPrincipal.ctrlDisciplina.getListaCodDiscAtivas()
        if self.testePopula == False:
            self.testePopula = self.limiteAtualiza.IsPopularListbox(self.listaGradeCodDisc)
            self.limiteAtualiza.IsPopularListboxTodas(listaTodasDisciplinas ,self.listaGradeCodDisc)
        else:
            self.limiteAtualiza.limparListBox()
            self.limiteAtualiza.IsPopularListbox(self.listaGradeCodDisc)
            self.limiteAtualiza.IsPopularListboxTodas(listaTodasDisciplinas ,self.listaGradeCodDisc)
    
    def removeDisciplina(self, event):
        comboCurso = self.limiteAtualiza.escolhaCurso.get()
        comboAno = self.limiteAtualiza.escolhaGrade.get()
        disciplinaSel = self.limiteAtualiza.listbox.get(tk.ACTIVE)
        status = ManipulaBanco.removerDisciplinaDaGrade(comboAno, comboCurso, disciplinaSel) 
        try:
            if status == False:
                raise ConexaoBD()
        except ConexaoBD:
            self.limiteAtualiza.mostraMessagebox('ERROR', 'Falha de conexão com Banco de Dados', True)
        else:
            self.limiteAtualiza.mostraMessagebox('Sucesso', 'Disciplina removida com sucesso', False)
            self.popular(event)
    
    def adicionaDisciplina(self, event):
        comboCurso = self.limiteAtualiza.escolhaCurso.get()
        comboAno = self.limiteAtualiza.escolhaGrade.get()
        disciplinaSel = self.limiteAtualiza.listboxTodas.get(tk.ACTIVE)
        gradeDisciplina = GradeDisciplina(grade_id_ano=comboAno, grade_id_curso=comboCurso, disciplina_id=disciplinaSel)
        status = ManipulaBanco.inserirDisciplinaNaGrade(gradeDisciplina) 
        try:
            if status == False:
                raise ConexaoBD()
        except ConexaoBD:
            self.limiteAtualiza.mostraMessagebox('ERROR', 'Falha de conexão com Banco de Dados', True)
        else:
            self.limiteAtualiza.mostraMessagebox('Sucesso', 'Disciplina inserida com sucesso', False)
            self.popular(event)