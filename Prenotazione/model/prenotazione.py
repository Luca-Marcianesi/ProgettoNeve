# Classe prenotazione


class Prenotazione:

    def __init__(self, codice_oggetto, scadenza, oggetto):
        self.codice_oggetto = codice_oggetto
        self.oggetto = oggetto
        self.scadenza = scadenza

    # Metodo che restituisce la descrizione della prenotazione
    def get_descrizione(self):
        return "Prenotazione: {}  \nScadenza: {}".format(self.oggetto.get_descrizione(),
                                                      self.scadenza.isoformat(timespec='minutes'))  # troncamento

    # Metodo che restituisce il codice dell'oggetto
    def get_codice_oggetto(self):
        return self.codice_oggetto

    # Metodo che restituisce la scadenza
    def get_scadenza(self):
        return self.scadenza

    # Metodo che restituisce la descrizione dell'oggetto (skipass/parcheggio/attrezzatura)
    def get_descrizione_oggetto(self):
        return self.oggetto.get_descrizione()
