import tkinter as tk
from View.MainView import *
import Controller.AlunoCtrl as al
import Controller.DisciplinaCtrl as dic
import Controller.GradeCtrl as gr
import Controller.CursoCtrl as cr
import Controller.HistoricoCtrl as hist

class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg='#76cb69')

        self.ctrlAluno = al.CtrlAluno(self)
        self.ctrlDisciplina = dic.CtrlDisciplina(self)
        self.ctrlGrade = gr.CtrlGrade(self)
        self.ctrlCurso = cr.CtrlCurso(self)
        self.ctrlHistorico = hist.CtrlHistorico(self)
    
        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Sistema Acadêmico YS")
        self.frameTela = tk.Frame(self.root)
        self.frameTela.pack()
        self.root.mainloop()

    def newFrame(self):
        self.frameTela.destroy()
        self.frameTela = tk.Frame(self.root)
        self.frameTela.pack()
        self.frameTela.configure(bg='#76cb69')
        return self.frameTela

    ###############################################   
    def insereAlunos(self):
        self.ctrlAluno.insereAlunos(self.newFrame())

    def relatorioAlunos(self):
        self.ctrlAluno.relatorioAlunos(self.newFrame())
    
    def consultaAlunos(self):
        self.ctrlAluno.consultaAlunos(self.newFrame())
    
    def excluiAlunos(self):
        self.ctrlAluno.excluiAlunos(self.newFrame())

    def atualizaAlunos(self):
        self.ctrlAluno.atualizaAlunos(self.newFrame())

    ###############################################
    def insereDisciplinas(self):
        self.ctrlDisciplina.insereDisciplinas(self.newFrame())

    def relatorioDisciplinas(self):
        self.ctrlDisciplina.relatorioDisciplinas(self.newFrame())

    def consultaDisciplinas(self):
        self.ctrlDisciplina.consultaDisciplinas(self.newFrame())

    def excluiDisciplinas(self):
        self.ctrlDisciplina.excluiDisciplinas(self.newFrame())

    def atualizaDisciplinas(self):
        self.ctrlDisciplina.atualizaDisciplinas(self.newFrame())

    ###############################################
    def insereGrade(self):
        self.ctrlGrade.insereGrades(self.newFrame())

    def relatorioGrade(self):
        self.ctrlGrade.relatorioGrade(self.newFrame())
    
    def consultaGrade(self):
        self.ctrlGrade.consultaGrades(self.newFrame())

    def excluiGrade(self):
        self.ctrlGrade.excluiGrades(self.newFrame())

    def atualizaGrade(self):
        self.ctrlGrade.atualizaGrades(self.newFrame())

    ###############################################
    def insereCursos(self):
        self.ctrlCurso.insereCursos(self.newFrame())

    def relatorioCursos(self):
        self.ctrlCurso.relatorioCursos(self.newFrame())
    
    def consultaCursos(self):
        self.ctrlCurso.consultaCursos(self.newFrame())

    def excluiCursos(self):
        self.ctrlCurso.excluiCursos(self.newFrame())
    
    ###############################################
    def insereHistoricos(self):
        self.ctrlHistorico.insereHistoricos(self.newFrame())

    def mostraHistoricos(self):
        self.ctrlHistorico.mostraHistoricos()
    
    def consultaHistoricos(self):
        self.ctrlHistorico.consultaHistoricos(self.newFrame())
    
    def excluiHistoricos(self):
        self.ctrlHistorico.excluiHistoricos(self.newFrame())

    ###############################################    
    def sair(self):
        self.root.destroy()