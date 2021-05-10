
class controller_attrezzatura:

    def __init__(self, attrezzatura):
        self.model = attrezzatura

    def set_stato(self, stato):
        self.model.set_stato(stato)

    def get_nome(self):
        return self.model.get_nome()

    def get_codice(self):
        self.model.get_codice()

    def get_dimensioni(self):
        return self.model.get_dimensioni()

    def get_stato(self):
        return self.model.get_stato()

