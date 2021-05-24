import json
import os
import pickle
from datetime import date,timedelta

from Manutenzioni.model.manutenzione import manutenzione

# Classe manutenzioni
class elenco_manutenzioni:

    def __init__(self):
        self.elenco_manutenzioni = []
        self.leggi_dati()

    # Metodo per aggiungere una manutenzione
    def aggiungi_manutenzione(self, manutenzione):
        self.elenco_manutenzioni.append(manutenzione)

    # Metodo per eliminare una manutenzione
    def elimina_manutenzione(self, numero):
        self.elenco_manutenzioni.remove(numero)

    # Metodo per aggiornare lo stato di una manutenzione tramite il codice
    def aggiorna_stato(self, codice):
        for manutenzione in self.elenco_manutenzioni:
            if manutenzione.get_codice() == codice:
                manutenzione.effettua_manutenzione()
                return True
        return False

    # Restituisce l'elenco delle manutenzioni
    def get_elenco_manutenzioni(self):
        print(self.elenco_manutenzioni)
        return self.elenco_manutenzioni

    # Metodo che legge i dati dal pickle se esiste o dal json
    def leggi_dati(self):
            if os.path.isfile('ElencoManutenzioni/data/elenco_manutenzioni.pickle'):
                with open('ElencoManutenzioni/data/elenco_manutenzioni.pickle', "rb") as file:
                    self.elenco_manutenzioni = pickle.load(file)
            else :
                with open("ElencoManutenzioni/data/elenco_manutenzioni.json") as file:
                    elenco_manutenzioni = json.load(file)
                for manutenzione_da_aggiungere in elenco_manutenzioni:
                        self.aggiungi_manutenzione(manutenzione(manutenzione_da_aggiungere["nome"],
                                                                manutenzione_da_aggiungere["cadenza(giorni)"],
                                                                date.today(),
                                                                date.today() + timedelta(days=int(manutenzione_da_aggiungere["cadenza(giorni)"]))))

    # Metodo per salvare i dati
    def salva_dati(self):
        with open('ElencoManutenzioni/data/elenco_manutenzioni.pickle', 'wb') as dati:
            pickle.dump(self.elenco_manutenzioni, dati, pickle.HIGHEST_PROTOCOL)