
class controller_attrezzatura:

    def __init__(self, attrezzatura):
        self.model = attrezzatura

    def get_tipo(self):
        return self.model.get_tipo()

    def set_stato(self, stato):
        self.model.set_stato(stato)

    def set_nome(self, nome):
        return self.model.set_nome(nome)
