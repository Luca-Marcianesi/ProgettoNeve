
class Controller_tabella_orari:
    def __init__(self, tabella_orari):
        self.model = tabella_orari

    def aggiungi_a_giorno(self, giorno, dipendente):
        self.model.aggiungi_a_giorno(giorno, dipendente)

    def rimuovi_da_giorno(self, giorno, dipendente):
        self.model.rimuovi_da_giorno(giorno, dipendente)

    def get_lista_tabella_orari(self):
        return self.model.get_lista_tabella_orari()

    def get_giorno_from_lista(self, giorno):
        return self.model.get_giorno_from_lista(giorno)

    def get_numero_tabella(self):
        return self.model.get_numero_tabella()
