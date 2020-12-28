import tkinter as tk
from tkinter import messagebox

class LimitePrincipal():
    def __init__(self, controle):
        self.root = tk.Tk()
        self.root.configure(bg='#76cb69')

        #deixar a janela centralizada
        window_height = 450
        window_width = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        #adicionar imagem de ícone da janela
        self.root.iconbitmap('./images/school.ico')

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
             
        self.alunoMenu.add_command(label="Insere", command=controle.insereAlunos)
        self.alunoMenu.add_command(label="Mostra", command=controle.mostraAlunos)
        self.alunoMenu.add_command(label="Consulta", command=controle.consultaAlunos)
        self.alunoMenu.add_command(label="Exclui", command=controle.excluiAlunos)
        self.alunoMenu.add_command(label="Atualiza", command=controle.atualizaAlunos)
        self.menubar.add_cascade(label="Aluno", menu=self.alunoMenu)

        # self.discipMenu.add_command(label="Insere", command=controle.insereDisciplinas)
        # self.discipMenu.add_command(label="Mostra", command=controle.mostraDisciplinas)
        # self.discipMenu.add_command(label="Consulta", command=controle.consultaDisciplinas)        
        # self.discipMenu.add_command(label="Exclui", command=controle.excluiDisciplinas)        
        # self.discipMenu.add_command(label="Atualiza", command=controle.atualizaDisciplinas)        
        # self.menubar.add_cascade(label="Disciplina", menu=self.discipMenu)

        # self.gradeMenu.add_command(label="Insere", command=controle.insereGrade)
        # self.gradeMenu.add_command(label="Mostra", command=controle.mostraGrade)
        # self.gradeMenu.add_command(label="Consulta", command=controle.consultaGrade)        
        # self.gradeMenu.add_command(label="Exclui", command=controle.excluiGrade)        
        # self.gradeMenu.add_command(label="Atualiza", command=controle.atualizaGrade)        
        # self.menubar.add_cascade(label="Grade", menu=self.gradeMenu)

        # self.cursoMenu.add_command(label="Insere", command=controle.insereCursos)
        # self.cursoMenu.add_command(label="Mostra", command=controle.mostraCursos)
        # self.cursoMenu.add_command(label="Consulta", command=controle.consultaCursos)        
        # self.cursoMenu.add_command(label="Exclui", command=controle.excluiCursos)        
        # self.cursoMenu.add_command(label="Atualiza", command=controle.atualizaCursos)        
        # self.menubar.add_cascade(label="Curso", menu=self.cursoMenu)

        # self.historicoMenu.add_command(label="Insere", command=controle.insereHistoricos)
        # self.historicoMenu.add_command(label="Mostra", command=controle.mostraHistoricos)
        # self.historicoMenu.add_command(label="Consulta", command=controle.consultaHistoricos)        
        # self.historicoMenu.add_command(label="Exclui", command=controle.excluiHistoricos)        
        # self.menubar.add_cascade(label="Histórico", menu=self.historicoMenu)

        # self.salvaMenu.add_command(label="Salvar os Dados", command=controle.salvaDados)
        # self.menubar.add_cascade(label="Salvar", menu=self.salvaMenu)

        # self.sairMenu.add_command(label="Sair do Programa", command=self.sair)
        # self.menubar.add_cascade(label="Sair", menu=self.sairMenu)

        self.root.config(menu=self.menubar)

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

    def mostraMessagebox(self, titulo, msg, erro):
        if erro == False:
            messagebox.showinfo(titulo, msg)
        else:
            messagebox.showerror(titulo, msg)
        
    def sair(self):
        self.root.destroy()

    