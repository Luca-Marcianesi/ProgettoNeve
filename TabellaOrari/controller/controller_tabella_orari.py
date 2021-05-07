from TabellaOrari.model.tabella_orari import tabella_orari

class Controller_tabella_orari:
    def __init__(self, numero_tabella):
        self.model = tabella_orari(numero_tabella)

    def aggiungi_a_giorno(self, giorno, dipendente):
        self.model.aggiungi_a_giorno(giorno, dipendente)

    def rimuovi_da_giorno(self, giorno, dipendente):
        self.model.rimuovi_da_giorno(giorno, dipendente)

    def get_lista_tabella_orari(self):
        return self.model.get_lista_tabella_orari()



