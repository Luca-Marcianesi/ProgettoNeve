
# Classe tabella orari
import os
import pickle

from Giorno.model.giorno import GiornoLavorativo


class tabella_orari:

    def __init__(self):

        # Definizione attributi
        self.lista_giorni = []
        self.aggiungi_giorni()
        self.leggi_dati()

    # Metodo che aggiunge un dipendente ad un certo giorno della lista giorni
    def aggiungi_a_giorno(self, riga, colonna, dipendente):
        self.lista_giorni[colonna].aggiungi_dipendente(riga, dipendente)

    # Metodo che rimove un dipendente da un certo giorno dalla lista dei giorni
    def rimuovi_da_giorno(self, colonna, riga):
        self.get_giorno_from_lista(colonna).rimuovi_dipendente(riga)

    # Metodo che restituisce la lista dei giorni
    def get_lista_tabella_orari(self):
        return self.lista_giorni

    # Metodo che restituisce il giorno scelto dalla lista
    def get_giorno_from_lista(self, colonna):
        return self.lista_giorni[colonna]

    # Metodo che legge i dati dal pickle se esiste o dal json
    def leggi_dati(self):
        if os.path.isfile('Data/TabellaOrari/tabella_orari.pickle'):
            with open('Data/TabellaOrari/tabella_orari.pickle', "rb") as file:
                self.lista_giorni = pickle.load(file)

    # Metodo per salvare i dati
    def salva_dati(self):
        with open('Data/TabellaOrari/tabella_orari.pickle', 'wb') as dati:
            pickle.dump(self.lista_giorni, dati, pickle.HIGHEST_PROTOCOL)

    def aggiungi_giorni(self):
        for colonne in range(7):
            giorno = GiornoLavorativo()
            self.lista_giorni.append(giorno)