class attrezzatura:
    def __init__(self, codice, nome ,dimensioni):
        self.codice = codice
        self.stato = True
        self.nome = nome
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

    def get_descrizione(self):
        return self.nome + " " + str(self.dimensioni)