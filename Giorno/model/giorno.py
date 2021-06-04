import os
import pickle


# Classe che si occupa della definizione della giornata lavorativa
class GiornoLavorativo:
    def __init__(self):

        # Dichiarazione di una lista vuota da riempire con gli oggetti Dipendente
        self.lista_dipendenti_impiegati = []
        # Chiamata del metodo interno leggi_dati per il riempimento della lista con gli elementi salvati
        self.leggi_dati()

    # Metodo per aggiungere un dipendente all'indice dato
    def aggiungi_dipendente(self, riga, dipendente):
        self.lista_dipendenti_impiegati.insert(riga, dipendente)

    # Metodo per rimuovere un dipendente all'indice dato
    def rimuovi_dipendente(self, riga):
        self.lista_dipendenti_impiegati.pop(riga)

    # Metodo che restiruisce il dipendente all'indice dato
    def get_dipendente(self, riga):
        return self.lista_dipendenti_impiegati[riga]

    # Metodo che restituisce la lista dei dipendenti del giorno lavorativo
    def get_lista(self):
        return self.lista_dipendenti_impiegati

    # Metodo che legge i dati dal file pickle se esiste, se no dal file json
    def leggi_dati(self):
        if os.path.isfile('Data/TabellaOrari/dipendenti.pickle'):
            with open('Data/TabellaOrari/dipendenti.pickle', "rb") as file:
                self.lista_dipendenti_impiegati = pickle.load(file)

    # Metodo per salvare i dati nel file pickle
    def salva_dati(self):
        with open('Data/TabellaOrari/dipendenti.pickle', 'wb') as dati:
            pickle.dump(self.lista_dipendenti_impiegati, dati, pickle.HIGHEST_PROTOCOL)
