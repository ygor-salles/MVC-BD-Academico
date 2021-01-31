import tkinter as tk
from tkinter import messagebox
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

        self.ctrlAluno = al.CtrlAluno()
        self.ctrlDisciplina = dic.CtrlDisciplina()
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

    def mostraAlunos(self):
        self.ctrlAluno.mostraAlunos()
    
    def consultaAlunos(self):
        self.ctrlAluno.consultaAlunos(self.newFrame())
    
    def excluiAlunos(self):
        self.ctrlAluno.excluiAlunos(self.newFrame())

    def atualizaAlunos(self):
        self.ctrlAluno.atualizaAlunos(self.newFrame())

    ###############################################
    def insereDisciplinas(self):
        self.ctrlDisciplina.insereDisciplinas(self.newFrame())

    def mostraDisciplinas(self):
        self.ctrlDisciplina.mostraDisciplinas()

    def consultaDisciplinas(self):
        self.ctrlDisciplina.consultaDisciplinas(self.newFrame())

    def excluiDisciplinas(self):
        self.ctrlDisciplina.excluiDisciplinas(self.newFrame())

    def atualizaDisciplinas(self):
        self.ctrlDisciplina.atualizaDisciplinas(self.newFrame())

    ###############################################
    def insereGrade(self):
        self.ctrlGrade.insereGrade(self.newFrame())

    def mostraGrade(self):
        self.ctrlGrade.mostraGrade()
    
    def consultaGrade(self):
        self.ctrlGrade.consultaGrade(self.newFrame())

    def excluiGrade(self):
        self.ctrlGrade.excluiGrade(self.newFrame())

    def atualizaGrade(self):
        self.ctrlGrade.atualizaGrade(self.newFrame())

    ###############################################
    def insereCursos(self):
        self.ctrlCurso.insereCursos(self.newFrame())

    def mostraCursos(self):
        self.ctrlCurso.mostraCursos()
    
    def consultaCursos(self):
        self.ctrlCurso.consultaCursos(self.newFrame())

    def excluiCursos(self):
        self.ctrlCurso.excluiCursos(self.newFrame())
    
    def atualizaCursos(self):
        self.ctrlCurso.atualizaCursos(self.newFrame())
    
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
    def salvaDados(self):
        self.ctrlAluno.salvaAlunos()
        self.ctrlDisciplina.salvaDisciplinas()
        self.ctrlGrade.salvaGrades()
        self.ctrlCurso.salvaCursos()
        self.ctrlHistorico.salvaHistoricos()
        messagebox.showinfo('Backup', 'Arquivos salvos com sucesso!')
        
    def sair(self):
        self.root.destroy()