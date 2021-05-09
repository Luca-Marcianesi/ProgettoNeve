class giorno_lavorativo:
    def __init__(self,giorno):
        self.giorno = giorno
        self.lista_dipendenti_impiegati = []

    def aggiungi_dipendente(self,dipendente):
        self.lista_dipendenti_impiegati.append(dipendente)

    def rimuovi_dipendente(self, dipendente):
        self.lista_dipendenti_impiegati.remove(dipendente)

    def get_giorno(self):
        return self.giorno


