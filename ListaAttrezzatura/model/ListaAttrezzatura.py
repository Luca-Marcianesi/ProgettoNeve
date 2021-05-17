import json
import os
import pickle
from Attrezzatura.model.attrezzatura import attrezzatura
from Sessione.model.sessione import sessione


class lista_attrezzatura:
    def __init__(self):
        self.lista_attrezzatura = []
        self.leggi_dati()

    def aggiungi_attrezzatura(self, attrezzatura):
        self.lista_attrezzatura.append(attrezzatura)

    def rimuovi_attrezzatura(self, indice):
        self.lista_attrezzatura.remove(indice)

    def set_stato(self, stato):
        self.stato = stato

    def prenota_attrezzatura(self, tipo):
        for attrezzatura in self.lista_attrezzatura:
            if attrezzatura.get_tipo() == tipo:
                attrezzatura.set_stato(False)
            return "Attrezzatura già prenotata o non disponibile"

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
            if int(attrezzatura.get_dimensioni())== int(sessione.get_numero_scarpe()) or int(attrezzatura.get_dimensioni()) == int(sessione.get_altezza()) - 10:
                lista_filtrata.append(attrezzatura)
        return lista_filtrata



