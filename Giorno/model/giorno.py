class giorno_lavorativo:
    def __init__(self,giorno):
        self.giorno = giorno
        self.lista_dipendenti_impiegati = []

    def aggiungi_dipendente(self,dipendente):
        self.lista_dipendenti_impiegati.append(dipendente)

    def rimuovi_dipendente(self, dipendente):
        for dipendente in self.lista_dipendenti_impiegati:
            if dipendente.nome == self.lista_dipendenti_impiegati[dipendente].nome and dipendente.cognome == self.lista_dipendenti_impiegati[dipendente].cognome:
                return self.lista_dipendenti_impiegati.remove(dipendente)
            else:
                return "Dipendente non trovato"

    def get_giorno(self):
        return self.giorno

    def get_dipendente(self, dipendente):
        for dipendente in self.lista_dipendenti_impiegati:
            if dipendente.nome == self.lista_dipendenti_impiegati[dipendente].nome and dipendente.cognome == self.lista_dipendenti_impiegati[dipendente].cognome:
                return self.lista_dipendenti_impiegati[dipendente]
            else:
                return "Dipendente non trovato"

