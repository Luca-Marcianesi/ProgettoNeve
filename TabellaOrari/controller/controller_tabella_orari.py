
# Controller tabella orari
from TabellaOrari.model.tabella_orari import tabella_orari


class ControllerTabellaOrari:

    def __init__(self):
        # Prende come model l'oggetto tabella orari e viene passato a costruttore
        self.model = tabella_orari()

    # Richiama i metodi della classe tabella orari
    def aggiungi_a_giorno(self, riga, colonna, dipendente):
        self.model.aggiungi_a_giorno(riga,colonna, dipendente)

    def rimuovi_da_giorno(self, colonna, riga):
        self.model.rimuovi_da_giorno(colonna, riga)

    def get_lista_tabella_orari(self):
        return self.model.get_lista_tabella_orari()

    def get_dipendenti_impiegati(self, colonna):
        return self.model.get_dipendenti_impiegati(colonna)

    def get_giorno_from_lista(self, colonna):
        return self.model.get_giorno_from_lista(colonna)

    def salva_dati(self):
        return self.model.salva_dati()
