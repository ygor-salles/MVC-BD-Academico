import os.path
import pickle
from View.DisciplinaView import *
from Model.DisciplinaModel import Disciplina

class DisciplinaNaoCadastrada(Exception):
    pass

class DisciplinaDuplicada(Exception):
    pass

class CamposNaoPreenchidos(Exception):
    pass

class CtrlDisciplina():       
    def __init__(self):
        if not os.path.isfile("Disciplina.pickle"):
            self.listaDisciplinas =  []
        else:
            with open("Disciplina.pickle", "rb") as f:
                self.listaDisciplinas = pickle.load(f)

    #Função para persistencia de dados ---------------------------------------------
    
    def salvaDisciplinas(self):
        if len(self.listaDisciplinas) != 0:
            with open("Disciplina.pickle","wb") as f:
                pickle.dump(self.listaDisciplinas, f)

    #Funções auxiliares e de amarrações da classe ---------------------------------------------

    def getDisciplina(self, codDisc):
        discRet = None
        for disc in self.listaDisciplinas:
            if disc.getCodigo() == codDisc:
                discRet = disc
        return discRet

    def getListaCodDisciplinas(self):
        listaCod = []
        for disc in self.listaDisciplinas:
            listaCod.append(disc.getCodigo())
        return listaCod

    def getAtualizaDisciplina(self, codDisc, nomeOuCh, string):
        for disc in self.listaDisciplinas:
            if codDisc==disc.getCodigo(): 
                if string=='ch':
                    disc.setCargaHoraria(nomeOuCh)
                else:
                    disc.setNome(nomeOuCh)
            
    #Funções que serão chamadas na Main --- Instaciadores ---------------------------

    def insereDisciplinas(self, root):
        self.limiteIns = LimiteInsereDisciplinas(self, root) 

    def mostraDisciplinas(self):
        string = 'Código -- Nome -- Carga Horária\n'
        for disc in self.listaDisciplinas:
            string += disc.getCodigo()+' -- '+disc.getNome()+' -- '+str(disc.getCargaHoraria())+'\n'
        self.limiteLista = LimiteMostraDisciplinas(string)
    
    def consultaDisciplinas(self, root):
        self.limiteConsulta = LimiteConsultaDisciplina(self, root)

    def excluiDisciplinas(self, root):
        self.limiteExclui = LimiteExcluiDisciplina(self, root)
    
    def atualizaDisciplinas(self, root):
        self.limiteAtualiza = LimiteAtualizaDisciplina(self, root)

    #Funções de CRUD -- Buttons -----------------------------------------------------------

    def enterHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        nome = self.limiteIns.inputNome.get()
        ch = self.limiteIns.inputCargaHoraria.get()
        disc = self.getDisciplina(codigo)
        try:
            if disc != None:
                raise DisciplinaDuplicada()
            if len(codigo)==0 or len(nome)==0 or len(ch)==0:
                raise CamposNaoPreenchidos()
        except DisciplinaDuplicada:
            self.limiteIns.mostraMessagebox('Alerta', 'Disciplina já cadastrada!', True)
        except CamposNaoPreenchidos:
            self.limiteIns.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', True)
        else:
            self.listaDisciplinas.append(Disciplina(codigo, nome, ch))
            self.limiteIns.mostraMessagebox('Sucesso', 'Disciplina cadastrada com sucesso', False)
            self.limiteIns.clearHandler(event)
    
    def consultaHandler(self, event):
        codigo = self.limiteConsulta.inputTextCodigo.get()
        disc = self.getDisciplina(codigo)
        try:
            if len(codigo)==0:
                raise CamposNaoPreenchidos()
            if disc == None:
                raise DisciplinaNaoCadastrada() 
        except CamposNaoPreenchidos:
            self.limiteConsulta.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', True)
        except DisciplinaNaoCadastrada:
            self.limiteConsulta.mostraMessagebox('Alerta', 'Disciplina não cadastrada', True)
        else:
            string = 'Disciplina cadastrada \nCódigo -- Nome -- Carga Horária \n'+codigo+' -- '+disc.getNome()+' -- '+str(disc.getCargaHoraria())
            LimiteMostraDisciplinas(string)
        finally:
            self.limiteConsulta.clearConsulta(event)
    
    def excluirDisciplina(self, event):
        codigo = self.limiteExclui.inputTextCodigo.get()
        disc = self.getDisciplina(codigo)
        try:
            if len(codigo)==0:
                raise CamposNaoPreenchidos()
            if disc == None:
                raise DisciplinaNaoCadastrada() 
        except CamposNaoPreenchidos:
            self.limiteExclui.mostraMessagebox('Atenção', 'Todos os campos devem ser preenchidos', True)
        except DisciplinaNaoCadastrada:
            self.limiteExclui.mostraMessagebox('Alerta', 'Disciplina não cadastrada', True)
        else:
            self.listaDisciplinas.remove(disc)
            self.limiteExclui.mostraMessagebox('Exclusão', 'Disciplina {} excluida com sucesso'.format(codigo), False)
            self.limiteExclui.clearExclusao(event)
    
    def atualizaDisciplina(self, event):
        codDisc = self.limiteAtualiza.inputCodigo.get()
        nome = self.limiteAtualiza.inputNome.get()
        ch = self.limiteAtualiza.inputCargaHoraria.get()
        disc = self.getDisciplina(codDisc)
        try:
            if len(codDisc)==0 or (len(nome)==0 and len(ch)==0):
                raise CamposNaoPreenchidos()
            if disc == None:
                raise DisciplinaNaoCadastrada() 
        except CamposNaoPreenchidos:
            self.limiteAtualiza.mostraMessagebox('Atenção', 'Junto ao código, pelo menos um campo(Nome ou Carga Horária) deve ser preenchido', True)
        except DisciplinaNaoCadastrada:
            self.limiteAtualiza.mostraMessagebox('Alerta', 'Disciplina não cadastrada', True)
        else:
            if len(nome) == 0:
                self.getAtualizaDisciplina(codDisc, ch, 'ch')
            else:
                self.getAtualizaDisciplina(codDisc, nome, 'nome')
            self.limiteAtualiza.mostraMessagebox('Sucesso', 'Disciplina {} atualizada com sucesso'.format(codDisc), False)
            self.limiteAtualiza.clearAtualiza(event) 