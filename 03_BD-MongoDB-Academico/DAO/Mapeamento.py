class Disciplina():
    def __init__(self, codigo, nome, ch):
        self.__codigo = codigo
        self.__nome = nome
        self.__ch = ch

    def getCodigo(self):
        return self.__codigo
    
    def getNome(self):
        return self.__nome

    def getCargaHoraria(self):
        return self.__ch

    def setNome(self, nome):
        self.__nome = nome
    
    def setCargaHoraria(self, ch):
        self.__ch = ch

class Aluno():
    def __init__(self, nroMatric, nome, curso):
        self.__nroMatric = nroMatric
        self.__nome = nome
        self.__curso = curso

    def getNroMatric(self):
        return self.__nroMatric
    
    def getNome(self):
        return self.__nome

    def getCurso(self):
        return self.__curso