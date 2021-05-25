# Classe giorno lavorativo


class GiornoLavorativo:
    def __init__(self, giorno):

        # Definizione attributi
        self.giorno = giorno
        self.lista_dipendenti_impiegati = []

    # Metodo per aggiungere un dipendente
    def aggiungi_dipendente(self, dipendente):
        self.lista_dipendenti_impiegati.append(dipendente)

    # Metodo per rimuovere un dipendente
    def rimuovi_dipendente(self, dipendente):
        self.lista_dipendenti_impiegati.remove(dipendente)

    # Metodo che restituisce il giorno
    def get_giorno(self):
        return self.giorno
