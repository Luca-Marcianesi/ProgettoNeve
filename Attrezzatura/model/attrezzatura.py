class attrezzatura:
    def __init__(self, codice, nome ,dimensioni):
        self.codice = codice
        self.stato = True
        self.nome = nome
        self.dimensioni = dimensioni
        self.scdenza = None

    def get_codice(self):
        return self.codice

    def prenota(self,scadenza):
        self.scdenza = scadenza
        self.stato = False

    def get_scadenza(self):
        return self.scdenza

    def get_nome(self):
        return self.nome

    def elimina_prenotazione(self):
        self.set_stato((True))
        self.scdenza = None

    def get_dimensioni(self):
        return self.dimensioni

    def get_stato(self):
        return self.stato

    def set_stato(self, stato):
        self.stato = stato

    def get_descrizione(self):
        return self.nome + " " + str(self.dimensioni)