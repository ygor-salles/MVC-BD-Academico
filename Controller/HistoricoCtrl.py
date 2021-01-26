from View.HistoricoView import *
from DAO.Mapeamento import Historico, HistoricoDisciplina
from Model.HistoricoModel import ManipulaBanco
from pprint import pprint

class HistoricoDuplicada(Exception): pass

class HistoricoNaoCadastrada(Exception): pass

class CamposNaoPreenchidos(Exception): pass 

class ConexaoBD(Exception): pass

class ErroRequisicao(Exception): pass

class CtrlHistorico():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaDiscHistorico = []

    def getListaHistoricos(self):
        return ManipulaBanco.listaHistoricos() 

    #Funções auxiliares e de amarrações da classe ---------------------------------------------

    def verificaObrigatoriedadeDisc(self, ano, curso, codDisc):
        return ManipulaBanco.consultaGradeDisc(ano, curso, codDisc)

    def buscaGradeDoAluno(self, matric):
        todosCursos = self.ctrlPrincipal.ctrlCurso.getListaCursos()
        try:
            if todosCursos == False:
                raise ConexaoBD()
        except ConexaoBD:
            return None
        else:
            for curso in todosCursos:
                for aluno in curso.alunos:
                    if aluno.nro_matric == int(matric):
                        return curso.grade
            return None

    def getListaCodHist(self):
        listaCodHist = []
        historicos = self.getListaHistoricos()
        try:
            if historicos == False:
                raise ConexaoBD()
        except ConexaoBD:
            return None
        else:
            for hist in historicos:
                listaCodHist.append(hist.id)
            return listaCodHist

    def emitirHistorico(self, his, string):
        eletiva=0
        obrigatoria=0
        grade = self.buscaGradeDoAluno(his.nro_matric)
        string += f'\nMatrícula: {his.nro_matric}'
        string += f'\nNome: {his.aluno.nome}'
        string += f'\nGrade: {grade.ano}/{grade.curso_id}'
        string += '\n\n|Ano|Semestre|Cod. Disciplina|Nome Disciplina|CH|Nota|Status|\n'
        for disc in his.disciplinas:
            string += f'{his.ano} - {his.semestre} - {disc.disciplinas.codigo} - {disc.disciplinas.nome} \
                - {disc.disciplinas.carga_horaria} - {disc.nota_disciplina} - {disc.status}'
            if (disc.obrigatorio == True):
                obrigatoria += int(disc.disciplinas.carga_horaria)
            else:
                eletiva += int(disc.disciplinas.carga_horaria) 
        string += f'\nTotal Carga Horária obrigatória: {obrigatoria} \nTotal Carga Horária eletiva: {eletiva}\n'             
        return string
        
            
    #Funções que serão chamadas na Main --- Instaciadores (MENU BAR) ---------------------------

    def insereHistoricos(self, root):
        self.listaDiscHistorico = []
        listaCodDisc = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisc()
        listaMatricAluno = self.ctrlPrincipal.ctrlAluno.getListaMatricAluno()
        self.limiteIns = LimiteInsereHistorico(self, root, listaCodDisc, listaMatricAluno)

    def mostraHistoricos(self):
        string = '..................RELATÓRIO DE HISTÓRICOS DOS ALUNOS..................'
        historicos = self.getListaHistoricos()
        try:
            if historicos == False:
                raise ConexaoBD()
        except:
            LimiteMostraHistorico('ERROR', 'Falha de conexão com o banco', True)
        else:
            for his in historicos:
                string = self.emitirHistorico(his, string)
            self.limiteMostra = LimiteMostraHistorico(string)
    
    def consultaHistoricos(self, root):
        self.limiteConsulta = LimiteConsultaHistorico(self, root)

    def excluiHistoricos(self, root):
        self.limiteExclui = LimiteExcluiHistorico(self, root)
    

    #Funções de CRUD dos Buttons ----------------------------------------------------

    # inserir -----------------------------------------------------------
    def insereDisciplina(self, event):
        matric = self.limiteIns.comboAluno.get()
        semestre = str(self.limiteIns.valor.get())
        ano = self.limiteIns.inputAno.get()
        disciplina_id = self.limiteIns.listboxDisciplina.get(tk.ACTIVE)
        nota_disciplina = self.limiteIns.inputNota.get()
        if float(nota_disciplina) >= 6: status = 'APROVADO'
        else: status = 'REPROVADO'
        # verificar se a disciplina é obrigatória
        gradeDoAluno = self.buscaGradeDoAluno(matric)
        try:
            if len(matric)==0 or len(semestre)==0 or len(ano)==0 or len(disciplina_id)==0 or len(nota_disciplina)==0:
                raise CamposNaoPreenchidos()
            if gradeDoAluno==None:
                raise ErroRequisicao()
        except CamposNaoPreenchidos:
            self.limiteIns.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        except ErroRequisicao:
            self.limiteIns.mostraMessagebox('ERROR', 'Houve erro na requisição', True)
        else:
            if self.verificaObrigatoriedadeDisc(gradeDoAluno.ano, gradeDoAluno.curso_id, disciplina_id) == None: 
                obrigatorio = False
            else: 
                obrigatorio = True
            self.listaDiscHistorico.append((disciplina_id, nota_disciplina, status, obrigatorio))
            self.limiteIns.mostraMessagebox('SUCESSO', 'Disciplina inserida na lista', False)
            self.limiteIns.listboxDisciplina.delete(tk.ACTIVE)
            self.limiteIns.inputNota.delete(0, 'end')

    def criaSemestre(self, event):
        matric = self.limiteIns.comboAluno.get()
        semestre = str(self.limiteIns.valor.get())
        ano = self.limiteIns.inputAno.get()
        try:
            if len(matric)==0 or len(semestre)==0 or len(ano)==0:
                raise CamposNaoPreenchidos()         
        except CamposNaoPreenchidos:
            self.limiteIns.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            relacionamento = []
            historico = Historico(nro_matric=matric, semestre=semestre, ano=ano)
            ManipulaBanco.cadastraHistorico(historico)
            idHistorico = ManipulaBanco.retornaByIdHistorico()
            for disc, nota, stat, obg in self.listaDiscHistorico:
                hist_disc = HistoricoDisciplina(historico_id=idHistorico, disciplina_id=disc,
                nota_disciplina=nota, status=stat, obrigatorio=obg)
                relacionamento.append(hist_disc)
            ManipulaBanco.cadastraListaDiscHistorico(relacionamento)
            self.limiteIns.mostraMessagebox('SUCESSO', 'Semestre criado com sucesso', False)
            self.limiteIns.janela.destroy()
        
    # consultar -----------------------------------------------------------
    def enterConsulta(self, event):
        matric = self.limiteConsulta.inputMatricAluno.get()
        try:
            if len(matric) == 0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteConsulta.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            historicosAluno = ManipulaBanco.consultaHistorico(matric)
            try:
                if historicosAluno == False: raise ConexaoBD()
                if historicosAluno == None: raise HistoricoNaoCadastrada()
            except ConexaoBD:
                self.limiteConsulta.mostraMessagebox('ERROR', 'Falha de conexão com o Banco de Dados', True)
            except HistoricoNaoCadastrada:
                self.limiteConsulta.mostraMessagebox('ALERTA', 'Historico não cadastrada', True)
            else:
                string = '..................RELATÓRIO DE HISTÓRICO DO ALUNO..................'
                string += self.emitirHistorico(historicosAluno, string)
                LimiteMostraHistorico('CONSULTA HISTÓRICO DO ALUNO', string, False)
            finally:
                self.limiteConsulta.clearConsulta(event)
            
    # deletar -----------------------------------------------------------
    def excluiHandler(self, event):
        matric = self.limiteExclui.inputMatricAluno.get()
        try:
            if len(matric)==0:
                raise CamposNaoPreenchidos()
        except CamposNaoPreenchidos:
            self.limiteExclui.mostraMessagebox('ATENÇÃO', 'Todos os campos devem ser preenchidos', True)
        else:
            status = ManipulaBanco.deletaHistorico(matric)
            try:
                if status == False:
                    raise HistoricoNaoCadastrada()
            except HistoricoNaoCadastrada:
                self.limiteExclui.mostraMessagebox('ALERTA', 'Historico não cadastrado ou falha de conexão com Banco de Dados', True)
            else:
                self.limiteExclui.mostraMessagebox('SUCESSO', 'Historico deletado com sucesso', False)
            finally:
                self.limiteExclui.clearExclusao(event)