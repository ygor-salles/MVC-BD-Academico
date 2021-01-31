class Historico:
    def __init__(self, listaDisc, aluno):
        self.__listaDisc = listaDisc
        self.__aluno = aluno
        self.__semestre = None
        self.__ano = None
        self.__notaDisc = []
        
    def getListaDisc(self):
        return self.__listaDisc

    def getAluno(self):
        return self.__aluno
    
    def getSemestre(self):
        return self.__semestre
    
    def setSemestre(self, semestre):
        self.__semestre = semestre
    
    def getAno(self):
        return self.__ano
    
    def setAno(self, ano):
        self.__ano = ano
    
    def getNotaDisc(self):
        return self.__notaDisc

    def setNotaDisc(self, notaDisc):
        self.__notaDisc = notaDisc