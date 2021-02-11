from tkinter import *
from View.MainView import *
import Controller.AlunoCtrl as al
import Controller.DisciplinasCtrl as dic
import Controller.CursoCtrl as cr
import Controller.GradeCtrl as gr
import Controller.HistoricoCtrl as hist

class ControlePrincipal():
    def __init__(self):
        self.root = Tk()
        self.root.configure(bg='#1e3743')

        self.ctrlAluno = al.CtrlAluno(self)
        self.ctrlDisciplina = dic.CtrlDisciplina(self)
        self.ctrlGrade = gr.CtrlGrade(self)
        self.ctrlCurso = cr.CtrlCurso(self)
        self.ctrlHistorico = hist.CtrlHistorico(self)
        
        self.limite = LimitePrincipal(self.root, self)

        self.frame_1 = Frame(self.root)
        self.frame_1.place()
        self.frame_2 = Frame(self.root)
        self.frame_2.place()

        self.root.title('Sistema Academico YS')
        self.root.mainloop()

    def newFrame1(self):
        self.frame_1.destroy()
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx= 0.02, rely=0.02, relwidth= 0.96, relheight= 0.46)
        return self.frame_1

    def newFrame2(self):
        self.frame_2.destroy()
        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
        return self.frame_2

    def sair(self):
        self.root.destroy()

    ###############################################
    def limiteDisiciplina(self):
        self.ctrlDisciplina.exibirTela(self.newFrame1(), self.newFrame2())

    def limiteAluno(self):
        self.ctrlAluno.exibirTela(self.newFrame1(), self.newFrame2())

    def limiteGrade(self):
        self.ctrlGrade.exibirTela(self.newFrame1(), self.newFrame2())

    def limiteAlteraGrade(self):
        self.ctrlGrade.exibirTelaGrade(self.newFrame1(), self.newFrame2())