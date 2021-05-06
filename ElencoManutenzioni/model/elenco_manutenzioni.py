import json
import os
import pickle
from datetime import datetime

from Manutenzioni.model.manutenzione import manutenzione

class elenco_manutenzioni:

    def __init__(self):
        self.lista_manutenzioni = []

    def aggiungi_manutenzione(self, manutenzione):
        self.lista_manutenzioni.append(manutenzione)

    def elimina_manutenzione(self, numero):
        self.lista_manutenzioni.remove(numero)

    def aggiorna_stato(self, codice):
        for manutenzione in self.lista_manutenzioni:
            if manutenzione.get_codice() == codice:
                manutenzione.effettua_manutenzione()
                return True
        return False

    def leggi_dati(self):
            if os.path.isfile('ElencoManutenzioni/data/elenco_manutenzioni.pickle'):
                with open('ListaAccount/data/lista_account_salvata.pickle', "rb") as file:
                    self.lista_account = pickle.load(file)
            else :
                with open("Pista/data/lista_piste.json") as file:
                    elenco_manutenzioni = json.load(file)
                for manutenzione in elenco_manutenzioni:
                        self.aggiungi_manutenzione(manutenzione(manutenzione["nome"], manutenzione["cadenza(giorni)"],
                                                                 datetime.today(),
                                                                datetime.today() +datetime.timedelta(days=int(manutenzione["cadenza(giorni)"]))))

    def salva_dati(self):
        with open('ElencoManutenzioni/data/elenco_manutenzioni.pickle', 'wb') as dati:
            pickle.dump(self.lista_account, dati, pickle.HIGHEST_PROTOCOL)