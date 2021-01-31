class Grade:
    def __init__(self, anoCurso, listaDisc):
        self.__anoCurso = anoCurso
        self.__listaDisc = listaDisc

    def getAnoCurso(self):
        return self.__anoCurso

    def getListaDisc(self):
        return self.__listaDisc