
class controller_pista():
    def __init__(self, pista):
        self.model = pista

    def modifica_stato_pista(self,stato):
        self.model.set_stato(stato)

    def get_pista_str(self):
        self.model.get_pista_str()

    def get_nome_str(self):
        return self.model.get_nome_str()

    def get_stato(self):
        return self.model.get_stato()

    def get_difficolta(self):
        return self.model.get_difficolta()

