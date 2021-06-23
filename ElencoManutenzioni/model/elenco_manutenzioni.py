import json
import os
import pickle
from datetime import date, timedelta
from Manutenzioni.model.manutenzione import Manutenzione


# Classe per la visualizzazione del elenco delle manutenzioni
class ElencoManutenzioni:

    def __init__(self):
        # Dichiarazione di una lista vuota da riempire con gli oggetti Manutenzione
        self.elenco_manutenzioni = []
        # Chiamata del metodo interno leggi_dati per il riempimento della lista con gli elementi salvati
        self.leggi_dati()

    # Metodo per aggiungere una manutenzione
    def aggiungi_manutenzione(self, manutenzione):
        self.elenco_manutenzioni.append(manutenzione)

    # Metodo per la restituzione dell'elenco delle manutenzioni
    def get_elenco_manutenzioni(self):
        return self.elenco_manutenzioni

    # Metodo che legge i dati dal file pickle se esiste, se no dal json
    def leggi_dati(self):
        if os.path.isfile('Data/ElencoManutenzioni/elenco_manutenzioni.pickle'):
            with open('Data/ElencoManutenzioni/elenco_manutenzioni.pickle', "rb") as file:
                self.elenco_manutenzioni = pickle.load(file)
        else:
            with open("Data/ElencoManutenzioni/elenco_manutenzioni.json") as file:
                elenco_manutenzioni = json.load(file)
            for manutenzione_da_aggiungere in elenco_manutenzioni:
                self.aggiungi_manutenzione(Manutenzione(manutenzione_da_aggiungere["nome"],
                                                        manutenzione_da_aggiungere["cadenza(giorni)"],
                                                        date.today(),
                                                        date.today() +
                                                        timedelta(days=int(manutenzione_da_aggiungere
                                                                           ["cadenza(giorni)"]))))

    # Metodo per salvare i dati nel file pickle
    def salva_dati(self):
        with open('Data/ElencoManutenzioni/elenco_manutenzioni.pickle', 'wb') as dati:
            pickle.dump(self.elenco_manutenzioni, dati, pickle.HIGHEST_PROTOCOL)
