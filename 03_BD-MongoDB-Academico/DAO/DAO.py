from DAO.Mapeamento import Disciplina

class DAOCrud():
    def insere(obj):
        obj.save()
    
    def listaDisciplinas():
        return Disciplina.query.all()

    def buscaDisciplina(codigo):
        return Disciplina.query.filter(Disciplina.codigo == codigo).first()

    def removeDisciplina(codigo):
        disc = Disciplina.query.filter(Disciplina.codigo == codigo).first()
        disc.remove()

    def atualizaDisciplina(codigo, nome, cargaHoraria):
        disciplina: Disciplina = Disciplina.query.filter(Disciplina.codigo == codigo).first()
        disciplina.nome = nome
        disciplina.cargaHoraria = cargaHoraria
        disciplina.save()
    