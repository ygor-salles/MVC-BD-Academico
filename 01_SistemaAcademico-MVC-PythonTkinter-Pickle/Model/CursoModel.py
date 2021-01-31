class Curso:
    def __init__(self, nome, listaAlunos, grade):
        self.__nome = nome
        self.__listaAlunos = listaAlunos
        self.__grade = grade
    
    def getNome(self):
        return self.__nome

    def getListaAlunos(self):
        return self.__listaAlunos
    
    def getGrade(self):
        return self.__grade
    
    def setGrade(self, grade):
        self.__grade = grade