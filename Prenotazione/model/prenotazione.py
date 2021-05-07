class prenotazione():
    def __init__(self,codice_oggetto,scadenza,descrizione):
        self.codice_oggetto = codice_oggetto
        self.descrizione = descrizione
        self.scadenza = scadenza

    def get_prenotazione_str(self):
        return "Prenotazione: {}  \nScadenza: {}".format(self.descrizione,self.scadenza)

    def get_codice_oggetto(self):
        return self.codice_oggetto

    def get_scadenza(self):
        return self.scadenza