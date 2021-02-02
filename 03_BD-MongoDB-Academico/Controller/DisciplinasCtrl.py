from DAO.Mapeamento import Disciplina
from View.DisciplinaView import LimiteDisciplina

class PreencherCampos(Exception): pass

class PreencherCampoId(Exception): pass

class CtrlDisciplina():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaDisciplinas = []

    def exibirTela(self, frame1, frame2):
        self.listaDisciplinas = [
            Disciplina('COM110', 'Fundamentos de Programação', 80),
            Disciplina('COM111', 'Estrutura de Dados', 96),
            Disciplina('MAT001', 'Calculo 1', 96),
            Disciplina('SIN130', 'Fundamentos de Computação', 64),
            Disciplina('COM312', 'Informática de Sociedade', 64),
            Disciplina('MAT011', 'GA', 64)
        ]
        self.limite = LimiteDisciplina(self, frame1, frame2, self.listaDisciplinas)
    
    def buscaDisciplina(self):
        self.limite.tabelaDisc.delete(*self.limite.tabelaDisc.get_children())
        codDisc = self.limite.inputCodigo.get()
        encontrou = False
        if len(codDisc)!=0:
            for disc in self.listaDisciplinas:
                if codDisc == disc.getCodigo():
                    self.limite.tabelaDisc.insert('', 'end', values=(disc.getCodigo(), disc.getNome(), disc.getCargaHoraria()))
                    encontrou = True
                    break
        else:
            for disc in self.listaDisciplinas:
                self.limite.tabelaDisc.insert('', 'end', values=(disc.getCodigo(), disc.getNome(), disc.getCargaHoraria()))
        if not encontrou and len(codDisc)!=0: 
            self.limite.mostraMessagebox('ERROR', f'Código de disciplina {codDisc} não encontrado', True)
        self.limite.limpaDisciplina()

    def insereDisciplina(self):
        codigo = self.limite.inputCodigo.get()
        nome = self.limite.inputNome.get()
        cargaHoraria = self.limite.inputCargaHoraria.get()
        try:
            if len(codigo)==0 or len(nome)==0 or len(cargaHoraria)==0:
                raise PreencherCampos()
        except PreencherCampos:
            self.limite.mostraMessagebox('ALERTA', 'Atenção todos os campos devem ser preenchidos para inserção', True)
        else:
            self.listaDisciplinas.append(Disciplina(codigo, nome, cargaHoraria))
            self.limite.mostraMessagebox('SUCESSO', 'Disciplina inserida com sucesso', False)
            self.limite.limpaDisciplina()

    def alteraDisciplina(self):
        codigo = self.limite.inputCodigo.get()
        nome = self.limite.inputNome.get()
        ch = self.limite.inputCargaHoraria.get()
        try:
            if len(codigo)==0 or len(nome)==0 or len(ch)==0:
                raise PreencherCampos()
        except PreencherCampos:
            self.limite.mostraMessagebox('ALERTA', 'Selecionar a disciplina que deseja alterar', True)
        else:
            for disc in self.listaDisciplinas:
                if disc.getCodigo() == codigo: 
                    disc.setNome(nome)
                    disc.setCargaHoraria(ch)
                    break
            self.limite.mostraMessagebox('SUCESSO', f'Disciplina {codigo} alterada com sucesso', False)
            self.limite.limpaDisciplina()
            self.buscaDisciplina() # Mesmo que fazer reload

    def deletaDisciplina(self):
        codigo = self.limite.inputCodigo.get()
        nome = self.limite.inputNome.get()
        ch = self.limite.inputCargaHoraria.get()
        try:
            if len(codigo)==0:
                raise PreencherCampoId()
        except PreencherCampoId:
            self.limite.mostraMessagebox('ALERTA', 'Necessário informar o campo de código para deletar', True)
        else:
            for disc in self.listaDisciplinas:
                if disc.getCodigo() == codigo: 
                    self.listaDisciplinas.remove(disc)
                    break
            self.limite.mostraMessagebox('SUCESSO', f'Disciplina {codigo} excluída com sucesso', False)
            self.limite.limpaDisciplina()
            self.buscaDisciplina() # Mesmo que fazer reload