
# Classe parcheggio
class parcheggio:
    def __init__(self, codice, numero, stato):

        # Definizione degli attributi
        self.codice = codice
        self.numero = numero
        self.stato = stato
        self.scadenza = None

    # Metodo che restituisce il codice del parcheggio
    def get_codice(self):
        return self.codice

    # Metodo che restituisce la scadenza del parcheggio
    def get_scadenza(self):
        return self.scadenza

    # Metodo che setta la scadenza del parcheggio
    def set_scadenza(self,scadenza):
        self.scadenza = scadenza

    # Metodo che restituisce lo stato di un parcheggio
    def get_stato(self):
        return self.stato

    # Metodo che permette di prenotare un parcheggio
    def prenota(self,scadenza):
        self.scadenza = scadenza
        self.stato = False

    # Metodo per eliminare la prenotazione del parcheggio
    def elimina_prenotazione(self):
        self.scadenza = None
        self.stato = True

    # Metodo che restituisce il numero del parcheggio
    def get_numero(self):
        return self.numero

    # Metodo che restituisce la descrizione del parcheggio
    def get_descrizione(self):
        return "Parcheggio numero {}".format(self.numero)

