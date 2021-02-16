import tkinter as tk

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root

        #deixar a janela centralizada
        window_height = 500
        window_width = 700
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        #adicionar imagem de ícone da janela
        self.root.iconbitmap('./assets/school.ico')

        #Fixar a janela em um só tamanho
        self.root.resizable(True, True)
        self.root.maxsize(width= 1350, height= 700)
        self.root.minsize(width=500, height= 400)

        #MenuBar
        self.menubar = tk.Menu(self.root)        
        self.alunoMenu = tk.Menu(self.menubar)
        self.discipMenu = tk.Menu(self.menubar)
        self.gradeMenu = tk.Menu(self.menubar)
        self.cursoMenu = tk.Menu(self.menubar)
        self.historicoMenu = tk.Menu(self.menubar)
        self.salvaMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar) 

        self.discipMenu.add_command(label="Crud disciplina", command=self.controle.limiteDisiciplina)
        self.menubar.add_cascade(label="Disciplina", menu=self.discipMenu)
        
        self.alunoMenu.add_command(label="Crud aluno", command=self.controle.limiteAluno)
        self.menubar.add_cascade(label="Aluno", menu=self.alunoMenu)

        self.gradeMenu.add_command(label="Crud grade", command=self.controle.limiteGrade)
        self.gradeMenu.add_command(label="Alterar grade", command=self.controle.limiteAlteraGrade)
        self.menubar.add_cascade(label="Grade", menu=self.gradeMenu)

        self.cursoMenu.add_command(label="CRUD CURSO", command=self.controle.limiteCurso)
        self.cursoMenu.add_command(label="Alterar curso", command=self.controle.limiteAlteraCurso)
        self.menubar.add_cascade(label="Curso", menu=self.cursoMenu)
        
        self.historicoMenu.add_command(label="Cadastrar Historico", command=self.controle.limiteHistorico)
        self.menubar.add_cascade(label="Histórico", menu=self.historicoMenu)
        
        # self.menubar.add_cascade(label="Sair", menu=self.sairMenu)

        self.root.config(menu=self.menubar)