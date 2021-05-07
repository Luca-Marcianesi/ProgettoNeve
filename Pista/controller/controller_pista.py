from Pista.model.pista import pista


class controller_pista():
    def __init__(self):
        self.model = pista()

    def modifica_stato_pista(self):
        self.model.set_stato()

    def get_pista_str(self):
        self.model.get_pista_str()

    def get_nome_str(self):
        self.get_nome_str()