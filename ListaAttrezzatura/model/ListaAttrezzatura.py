import json
import os
import pickle
from datetime import date, timedelta

from Attrezzatura.model.attrezzatura import attrezzatura
from Sessione.model.sessione import sessione
from Prenotazione.model.prenotazione import prenotazione


class lista_attrezzatura:
    def __init__(self):
        self.lista_attrezzatura = []
        self.leggi_dati()

    def aggiungi_attrezzatura(self, attrezzatura):
        self.lista_attrezzatura.append(attrezzatura)

    def rimuovi_attrezzatura(self, indice):
        self.lista_attrezzatura.remove(indice)

    def prenota_attrezzatura(self, attrezzatura,numero_giorni):
        attrezzatura.set_stato(False)
        scadenza = date.today() + timedelta(days=int(numero_giorni))
        sessione.aggiungi_prenotazione(prenotazione(attrezzatura.get_codice(),scadenza,attrezzatura))


    def salva_dati(self):
        with open('ListaAttrezzatura/data/lista_attrezzatura.pickle', 'wb') as file:
            pickle.dump(self.lista_account, file, pickle.HIGHEST_PROTOCOL)

    def leggi_dati(self):
        if os.path.isfile('ListaAttrezzatura/data/lista_attrezzatura.pickle'):
            with open('ListaAttrezzatura/data/lista_attrezzatura.pickle',"rb") as file:
                self.lista_account = pickle.load(file)
        else :
                with open("ListaAttrezzatura/data/lista_attrezzatura.json") as file:
                    lista_attrezzatura = json.load(file)
                for attrezzatura_da_caricare in lista_attrezzatura:
                    self.aggiungi_attrezzatura(
                        attrezzatura(attrezzatura_da_caricare["nome"], attrezzatura_da_caricare["codice"], attrezzatura_da_caricare["dimensioni"]))

    def get_lista_attrezzatura(self):
        return self.lista_attrezzatura

    def get_lista_filtrata(self):
        lista_filtrata = []
        for attrezzatura in self.lista_attrezzatura:
            if int(attrezzatura.get_dimensioni())== int(sessione.get_numero_scarpe()) or int(attrezzatura.get_dimensioni()) == int(sessione.get_altezza()) :
                if attrezzatura.get_stato() :
                    lista_filtrata.append(attrezzatura)
        return lista_filtrata

    def prenota_attrezzatura(self,attrezzatura):
        if sessione.controlla_prenotazione_effettuata(attrezzatura.get_codice()):
            scadenza = date.today() + timedelta(hours=int(1))
            attrezzatura.set_stato(False)
            sessione.aggiungi_prenotazione(prenotazione(attrezzatura.get_codice(),
                                                        scadenza,
                                                        attrezzatura))





