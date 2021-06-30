# Controller dell'attrezzatura e definizione del costruttore
class ControllerAttrezzatura:

    def __init__(self, attrezzatura):

        # Prende come model la classe attrezzatura
        self.model = attrezzatura

    # Richiama i metodi della classe attrezzatura
    def set_stato(self, stato):
        self.model.set_stato(stato)

    # Restituisce il nome dell'attrezzatura
    def get_nome(self):
        return self.model.get_nome()

    # Restituisce il codice identificativo dell'attrezzatura
    def get_codice(self):
        return self.model.get_codice()

    # Restituisce le dimensioni dell'attrezzatura
    def get_dimensioni(self):
        return self.model.get_dimensioni()

    # Restituisce la disponibilità dell'attrezzatura
    def get_stato(self):
        return self.model.get_stato()

    # Permette di prenotare l'attrezzatura
    def prenota(self, scadenza):
        self.model.prenota(scadenza)

    # Restituisce la data di scadenza dell'attrezzatura
    def get_scadenza(self):
        return self.model.get_scadenza()

    # Permette di eliminare la prenotazione l'attrezzatura
    def elimina_prenotazione(self):
        self.model.elimina_prenotazione()

    # Restituisce la descrizione dell'attrezzatura
    def get_descrizione(self):
        return self.model.get_descrizione()
