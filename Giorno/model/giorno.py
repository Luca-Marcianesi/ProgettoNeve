# Classe giorno lavorativo
import os
import pickle


class GiornoLavorativo:
    def __init__(self):

        # Definizione attributi
        self.lista_dipendenti_impiegati = []
        self.leggi_dati()

    # Metodo per aggiungere un dipendente
    def aggiungi_dipendente(self, riga, dipendente):
        self.lista_dipendenti_impiegati.insert(riga, dipendente)

    # Metodo per rimuovere un dipendente
    def rimuovi_dipendente(self, riga):
        self.lista_dipendenti_impiegati.remove(riga)

    def get_dipendente(self, riga):
        return self.lista_dipendenti_impiegati[riga]

    def get_lista(self):
        return self.lista_dipendenti_impiegati

    # Metodo che legge i dati dal pickle se esiste o dal json
    def leggi_dati(self):
        if os.path.isfile('Data/TabellaOrari/dipendenti.pickle'):
            with open('Data/TabellaOrari/dipendenti.pickle', "rb") as file:
                self.lista_dipendenti_impiegati = pickle.load(file)

    # Metodo per salvare i dati
    def salva_dati(self):
        with open('Data/TabellaOrari/dipendenti.pickle', 'wb') as dati:
            pickle.dump(self.lista_dipendenti_impiegati, dati, pickle.HIGHEST_PROTOCOL)
