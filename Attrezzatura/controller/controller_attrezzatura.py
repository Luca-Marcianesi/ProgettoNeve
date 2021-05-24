# Controller dell'attrezzatura
class controller_attrezzatura:

    def __init__(self, attrezzatura):

        # Prende come model la classe attrezzatura
        self.model = attrezzatura

    # Ridefinisce i metodi della classe attrezzatura
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

    def prenota(self, scadenza):
        self.model.prenota(scadenza)

    def get_scadenza(self):
        return self.model.get_scadenza()

    def elimina_prenotazione(self):
        self.model.elimina_prenotazione()

    def get_descrizione(self):
        return self.model.get_descrizione()

