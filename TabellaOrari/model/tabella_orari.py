
# Classe tabella orari
class tabella_orari:

    def __init__(self):

        # Definizione attributi
        self.lista_giorni = []

    # Metodo che aggiunge un dipendente ad un certo giorno della lista giorni
    def aggiungi_a_giorno(self, giorno, dipendente):
        self.lista_giorni[giorno].aggiungi_dipendente(dipendente)

    # Metodo che rimove un dipendente da un certo giorno dalla lista dei giorni
    def rimuovi_da_giorno(self, giorno, dipendente):
        self.lista_giorni[giorno].rimuovi_dipendente(dipendente)

    # Metodo che restituisce la lista dei giorni
    def get_lista_tabella_orari(self):
        return self.lista_giorni

    # Metodo che restituisce il giorno scelto dalla lista
    def get_giorno_from_lista(self, giorno):
        return self.lista_giorni[giorno]