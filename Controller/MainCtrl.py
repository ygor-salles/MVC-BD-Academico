from View.MainView import LimitePrincipal
import Controller.AlunoCtrl as al
# import Controller.DisciplinaCtrl as dic
# import Controller.GradeCtrl as gr
# import Controller.CursoCtrl as cr
# import Controller.HistoricoCtrl as hist

class ControlePrincipal():       
    def __init__(self):

        self.ctrlAluno = al.CtrlAluno()
        # self.ctrlDisciplina = dic.CtrlDisciplina()
        # self.ctrlGrade = gr.CtrlGrade(self)
        # self.ctrlCurso = cr.CtrlCurso(self)
        # self.ctrlHistorico = hist.CtrlHistorico(self)
    
        self.limite = LimitePrincipal(self) 

    ###############################################   
    def insereAlunos(self):
        print('Deu certo')
        # self.limite.mostraMessagebox('Teste', 'Testando isso', False)
        # self.ctrlAluno.insereAlunos(self.limite.newFrame())

    def mostraAlunos(self):
        self.ctrlAluno.mostraAlunos()
    
    def consultaAlunos(self):
        self.ctrlAluno.consultaAlunos(self.limite.newFrame())
    
    def excluiAlunos(self):
        self.ctrlAluno.excluiAlunos(self.limite.newFrame())

    def atualizaAlunos(self):
        self.ctrlAluno.atualizaAlunos(self.limite.newFrame())

    ###############################################
    def insereDisciplinas(self):
        self.ctrlDisciplina.insereDisciplinas(self.limite.newFrame())

    def mostraDisciplinas(self):
        self.ctrlDisciplina.mostraDisciplinas()

    def consultaDisciplinas(self):
        self.ctrlDisciplina.consultaDisciplinas(self.limite.newFrame())

    def excluiDisciplinas(self):
        self.ctrlDisciplina.excluiDisciplinas(self.limite.newFrame())

    def atualizaDisciplinas(self):
        self.ctrlDisciplina.atualizaDisciplinas(self.limite.newFrame())

    ###############################################
    def insereGrade(self):
        self.ctrlGrade.insereGrade(self.limite.newFrame())

    def mostraGrade(self):
        self.ctrlGrade.mostraGrade()
    
    def consultaGrade(self):
        self.ctrlGrade.consultaGrade(self.limite.newFrame())

    def excluiGrade(self):
        self.ctrlGrade.excluiGrade(self.limite.newFrame())

    def atualizaGrade(self):
        self.ctrlGrade.atualizaGrade(self.limite.newFrame())

    ###############################################
    def insereCursos(self):
        self.ctrlCurso.insereCursos(self.limite.newFrame())

    def mostraCursos(self):
        self.ctrlCurso.mostraCursos()
    
    def consultaCursos(self):
        self.ctrlCurso.consultaCursos(self.limite.newFrame())

    def excluiCursos(self):
        self.ctrlCurso.excluiCursos(self.limite.newFrame())
    
    def atualizaCursos(self):
        self.ctrlCurso.atualizaCursos(self.limite.newFrame())
    
    ###############################################
    def insereHistoricos(self):
        self.ctrlHistorico.insereHistoricos(self.limite.newFrame())

    def mostraHistoricos(self):
        self.ctrlHistorico.mostraHistoricos()
    
    def consultaHistoricos(self):
        self.ctrlHistorico.consultaHistoricos(self.limite.newFrame())
    
    def excluiHistoricos(self):
        self.ctrlHistorico.excluiHistoricos(self.limite.newFrame())

    ###############################################
    def salvaDados(self):
        self.ctrlAluno.salvaAlunos()
        self.ctrlDisciplina.salvaDisciplinas()
        self.ctrlGrade.salvaGrades()
        self.ctrlCurso.salvaCursos()
        self.ctrlHistorico.salvaHistoricos()
        self.limite.mostraMessagebox('Backup', 'Arquivos salvos com sucesso!', False)

    