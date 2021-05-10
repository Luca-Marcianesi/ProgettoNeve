class attrezzatura:
    def __init__(self, nome, codice ,dimensioni):
        self.stato = True
        self.nome = nome
        self.codice = codice
        self.dimensioni = dimensioni

    def get_codice(self):
        return self.codice

    def get_nome(self):
        return self.nome

    def get_dimensioni(self):
        return self.dimensioni

    def get_stato(self):
        return self.stato

    def set_stato(self, stato):
        self.stato = stato