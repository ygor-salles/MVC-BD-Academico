from View.AlunoView import LimiteAluno
from DAO.Mapeamento import Aluno


class CtrlAluno():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal

    def exibirTela(self, frame1, frame2):
        listaAlunos = [
            Aluno(201701, 'Benedito José', 'Sistemas de Informação'),
            Aluno(201702, 'Claudio Magalhaes', 'Sistemas de Informação'),
            Aluno(201703, 'Diana Jacinto', 'Sistemas de Informação'),
            Aluno(201704, 'Duarte Pereira', 'Ciencia da Computação'),
            Aluno(201705, 'Pereira Barbosa', 'Ciencia da Computação'),
            Aluno(201706, 'Joaquim Mamona', 'Sistemas de Informação'),
            Aluno(201707, 'Pangolin Gilberto', 'Ciencia da Computação'),
            Aluno(201708, 'Mario Ribeiro', 'Sistemas de Informação'),
            Aluno(201709, 'Marcos Santos', 'Ciencia da Computação')
        ]
        self.limiteIns = LimiteAluno(self, frame1, frame2, listaAlunos)