class tabella_orari:

    def __init__(self, numero_tabella):
        self.lista_giorni = []
        self.numero_tabella = numero_tabella

    def aggiungi_a_giorno(self, giorno, dipendente):
        self.lista_giorni[giorno].aggiungi_dipendente(dipendente)

    def rimuovi_da_giorno(self, giorno, dipendente):
        self.lista_giorni[giorno].rimuovi_dipendente(dipendente)

    def get_lista_tabella_orari(self):
        return self.lista_giorni

    def get_giorno_from_lista(self, giorno):
        return self.lista_giorni[giorno]