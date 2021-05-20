import json
import os
import pickle
from datetime import date,timedelta

from Manutenzioni.model.manutenzione import manutenzione

class elenco_manutenzioni:

    def __init__(self):
        self.elenco_manutenzioni = []
        self.leggi_dati()

    def aggiungi_manutenzione(self, manutenzione):
        self.elenco_manutenzioni.append(manutenzione)

    def elimina_manutenzione(self, numero):
        self.elenco_manutenzioni.remove(numero)

    def aggiorna_stato(self, codice):
        for manutenzione in self.elenco_manutenzioni:
            if manutenzione.get_codice() == codice:
                manutenzione.effettua_manutenzione()
                return True
        return False

    def get_elenco_manutenzioni(self):
        print(self.elenco_manutenzioni)
        return self.elenco_manutenzioni

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

    def salva_dati(self):
        with open('ElencoManutenzioni/data/elenco_manutenzioni.pickle', 'wb') as dati:
            pickle.dump(self.elenco_manutenzioni, dati, pickle.HIGHEST_PROTOCOL)