import tkinter as tk
from tkinter.constants import FALSE

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root

        #deixar a janela centralizada
        window_height = 500
        window_width = 650
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        #adicionar imagem de ícone da janela
        self.root.iconbitmap('./assets/school.ico')

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
             
        self.discipMenu.add_command(label="Inserir", command=self.controle.insereDisciplinas)
        self.discipMenu.add_command(label="Listar", command=self.controle.mostraDisciplinas)
        self.discipMenu.add_command(label="Relatório", command=self.controle.relatorioDisciplinas)
        self.discipMenu.add_command(label="Consultar por id", command=self.controle.consultaDisciplinas)        
        self.discipMenu.add_command(label="Excluir", command=self.controle.excluiDisciplinas)        
        self.discipMenu.add_command(label="Atualizar", command=self.controle.atualizaDisciplinas)        
        self.menubar.add_cascade(label="Disciplina", menu=self.discipMenu)

        self.cursoMenu.add_command(label="Inserir", command=self.controle.insereCursos)
        self.cursoMenu.add_command(label="Listar", command=self.controle.mostraCursos)
        self.cursoMenu.add_command(label="Relatório", command=self.controle.relatorioCursos)
        self.cursoMenu.add_command(label="Consultar por id", command=self.controle.consultaCursos)        
        self.cursoMenu.add_command(label="Excluir", command=self.controle.excluiCursos)                
        self.menubar.add_cascade(label="Curso", menu=self.cursoMenu)

        self.gradeMenu.add_command(label="Inserir", command=self.controle.insereGrade)
        self.gradeMenu.add_command(label="Listar", command=self.controle.mostraGrade)
        self.gradeMenu.add_command(label="Relatório", command=self.controle.relatorioGrade)
        self.gradeMenu.add_command(label="Consultar por id", command=self.controle.consultaGrade)        
        self.gradeMenu.add_command(label="Excluir", command=self.controle.excluiGrade)        
        self.gradeMenu.add_command(label="Atualizar", command=self.controle.atualizaGrade)        
        self.menubar.add_cascade(label="Grade", menu=self.gradeMenu)

        self.alunoMenu.add_command(label="Inserir", command=self.controle.insereAlunos)
        self.alunoMenu.add_command(label="Listar", command=self.controle.mostraAlunos)
        self.alunoMenu.add_command(label="Relatório", command=self.controle.relatorioAlunos)
        self.alunoMenu.add_command(label="Consultar por id", command=self.controle.consultaAlunos)
        self.alunoMenu.add_command(label="Excluir", command=self.controle.excluiAlunos)
        self.alunoMenu.add_command(label="Atualizar", command=self.controle.atualizaAlunos)
        self.menubar.add_cascade(label="Aluno", menu=self.alunoMenu)

        self.historicoMenu.add_command(label="Inserir", command=self.controle.insereHistoricos)
        self.historicoMenu.add_command(label="Consultar por aluno", command=self.controle.consultaHistoricos)        
        self.historicoMenu.add_command(label="Excluir", command=self.controle.excluiHistoricos)        
        self.menubar.add_cascade(label="Histórico", menu=self.historicoMenu)

        # self.salvaMenu.add_command(label="Salvar os Dados", command=self.controle.salvaDados)
        # self.menubar.add_cascade(label="Salvar", menu=self.salvaMenu)

        # self.sairMenu.add_command(label="Sair do Programa", command=self.controle.sair)
        # self.menubar.add_cascade(label="Sair", menu=self.sairMenu)

        self.root.config(menu=self.menubar)