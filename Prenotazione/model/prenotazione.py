class prenotazione():
    def __init__(self,codice_oggetto,scadenza,oggetto):
        self.codice_oggetto = codice_oggetto
        self.oggetto = oggetto
        self.scadenza = scadenza

    def get_descrizione(self):
        return "Prenotazione: {}  \nScadenza: {}".format(self.oggetto.get_descrizione(),self.scadenza)

    def get_codice_oggetto(self):
        return self.codice_oggetto

    def get_scadenza(self):
        return self.scadenza