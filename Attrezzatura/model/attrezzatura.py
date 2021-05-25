# Classe attrezzatura e definizione del costruttore
class attrezzatura:
    def __init__(self, codice, nome, dimensioni):

        # Definizione degli attributi
        self.codice = codice
        self.stato = True
        self.nome = nome
        self.dimensioni = dimensioni
        self.scdenza = None

    # Metodo che restituisce il codice dell'attrezzatura
    def get_codice(self):
        return self.codice

    # Metodo per prenotare l'attrezzatura
    def prenota(self,scadenza):
        self.scadenza = scadenza
        self.stato = False

    # Metodo che restituisce la scadenza della prenotazione
    def get_scadenza(self):
        return self.scadenza

    # Metodo che restituisce il nome dell'attrezzatura
    def get_nome(self):
        return self.nome

    # Metodo per eliminare una prenotazione
    def elimina_prenotazione(self):
        self.set_stato((True))
        self.scdenza = None

    # Metodo che restituisce le dimensioni dell'attrezzatura
    def get_dimensioni(self):
        return self.dimensioni

    # Metodo che restituisce lo stato dell'attrezzatura(disponibile/non disponibile)
    def get_stato(self):
        return self.stato

    # Metodo per settare lo stato dell'attrezzatura(disponibile/non disponibile)
    def set_stato(self, stato):
        self.stato = stato

    # Metodo che restituisce la descrizione dell'attrezzatura
    def get_descrizione(self):
        return self.nome + " " + str(self.dimensioni)