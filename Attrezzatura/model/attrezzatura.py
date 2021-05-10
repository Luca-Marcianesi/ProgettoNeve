class attrezzatura:
    def __init__(self, nome, codice ,dimensioni):
        self.stato = True
        self.nome = nome
        self.codice = codice
        self.dimensioni = dimensioni

    def get_tipo(self):
        return self.tipo

    def set_stato(self, stato):
        self.stato = stato

    def set_nome(self, nome):
        self.nome = nome