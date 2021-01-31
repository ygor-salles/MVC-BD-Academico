import tkinter as tk
import Aluno as al 
import Curso as cr 
import Grade as gr 
import Disciplina as dic 
import Historico as hist
from tkinter import messagebox 

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root

        #deixar a janela centralizada
        window_height = 450
        window_width = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        #adicionar imagem de ícone da janela
        self.root.iconbitmap('images/school.ico')

        #Fixar a janela em um só tamanho
        self.root.resizable(False, False)

        #MenuBar
        self.menubar = tk.Menu(self.root)        
        self.alunoMenu = tk.Menu(self.menubar)
        self.discipMenu = tk.Menu(self.menubar)
        self.gradeMenu = tk.Menu(self.menubar)
        self.cursoMenu = tk.Menu(self.menubar)
        self.historicoMenu = tk.Menu(self.menubar)
        self.salvaMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar) 
             
        self.alunoMenu.add_command(label="Insere", command=self.controle.insereAlunos)
        self.alunoMenu.add_command(label="Mostra", command=self.controle.mostraAlunos)
        self.alunoMenu.add_command(label="Consulta", command=self.controle.consultaAlunos)
        self.alunoMenu.add_command(label="Exclui", command=self.controle.excluiAlunos)
        self.alunoMenu.add_command(label="Atualiza", command=self.controle.atualizaAlunos)
        self.menubar.add_cascade(label="Aluno", menu=self.alunoMenu)

        self.discipMenu.add_command(label="Insere", command=self.controle.insereDisciplinas)
        self.discipMenu.add_command(label="Mostra", command=self.controle.mostraDisciplinas)
        self.discipMenu.add_command(label="Consulta", command=self.controle.consultaDisciplinas)        
        self.discipMenu.add_command(label="Exclui", command=self.controle.excluiDisciplinas)        
        self.discipMenu.add_command(label="Atualiza", command=self.controle.atualizaDisciplinas)        
        self.menubar.add_cascade(label="Disciplina", menu=self.discipMenu)

        self.gradeMenu.add_command(label="Insere", command=self.controle.insereGrade)
        self.gradeMenu.add_command(label="Mostra", command=self.controle.mostraGrade)
        self.gradeMenu.add_command(label="Consulta", command=self.controle.consultaGrade)        
        self.gradeMenu.add_command(label="Exclui", command=self.controle.excluiGrade)        
        self.gradeMenu.add_command(label="Atualiza", command=self.controle.atualizaGrade)        
        self.menubar.add_cascade(label="Grade", menu=self.gradeMenu)

        self.cursoMenu.add_command(label="Insere", command=self.controle.insereCursos)
        self.cursoMenu.add_command(label="Mostra", command=self.controle.mostraCursos)
        self.cursoMenu.add_command(label="Consulta", command=self.controle.consultaCursos)        
        self.cursoMenu.add_command(label="Exclui", command=self.controle.excluiCursos)        
        self.cursoMenu.add_command(label="Atualiza", command=self.controle.atualizaCursos)        
        self.menubar.add_cascade(label="Curso", menu=self.cursoMenu)

        self.historicoMenu.add_command(label="Insere", command=self.controle.insereHistoricos)
        self.historicoMenu.add_command(label="Mostra", command=self.controle.mostraHistoricos)
        self.historicoMenu.add_command(label="Consulta", command=self.controle.consultaHistoricos)        
        self.historicoMenu.add_command(label="Exclui", command=self.controle.excluiHistoricos)        
        self.menubar.add_cascade(label="Histórico", menu=self.historicoMenu)

        self.salvaMenu.add_command(label="Salvar os Dados", command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Salvar", menu=self.salvaMenu)

        self.sairMenu.add_command(label="Sair do Programa", command=self.controle.sair)
        self.menubar.add_cascade(label="Sair", menu=self.sairMenu)

        self.root.config(menu=self.menubar)
      
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
    
if __name__ == '__main__':
    c = ControlePrincipal()