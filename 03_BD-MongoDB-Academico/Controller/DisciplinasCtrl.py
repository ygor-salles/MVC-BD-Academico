from View.DisciplinaView import LimiteDisciplina


class CtrlDisciplina():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal

    def exibirTela(self, frame1, frame2):
        self.limiteIns = LimiteDisciplina(self, frame1, frame2)