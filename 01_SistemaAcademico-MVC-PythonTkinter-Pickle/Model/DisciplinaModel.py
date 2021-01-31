class Disciplina:
    def __init__(self, codigo, nome, cargaHoraria):
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria
    
    def getCodigo(self):
        return self.__codigo
    
    def getNome(self):
        return self.__nome
    
    def getCargaHoraria(self):
        return self.__cargaHoraria

    def setNome(self, nome):
        self.__nome = nome 

    def setCargaHoraria(self, cargaHoraria):
        self.__cargaHoraria = cargaHoraria 