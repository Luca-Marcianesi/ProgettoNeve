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

    def salva_dati(self):
        with open('ListaAttrezzatura/data/lista_attrezzatura.pickle', 'wb') as file:
            pickle.dump(self.lista_attrezzatura, file, pickle.HIGHEST_PROTOCOL)

    def leggi_dati(self):
        if os.path.isfile('ListaAttrezzatura/data/lista_attrezzatura.pickle'):
            with open('ListaAttrezzatura/data/lista_attrezzatura.pickle',"rb") as file:
                self.lista_attrezzatura = pickle.load(file)
        else :
                with open("ListaAttrezzatura/data/lista_attrezzatura.json") as file:
                    lista_attrezzatura = json.load(file)
                for attrezzatura_da_caricare in lista_attrezzatura:
                    self.aggiungi_attrezzatura(
                        attrezzatura(attrezzatura_da_caricare["codice"], attrezzatura_da_caricare["nome"], attrezzatura_da_caricare["dimensioni"]))

    def get_lista_attrezzatura(self):
        return self.lista_attrezzatura

    def get_lista_filtrata(self):
        lista_filtrata = []
        for attrezzatura in self.lista_attrezzatura:
            if attrezzatura.get_stato():
                    if self.filtra_dimenisoni(attrezzatura.get_dimensioni(),sessione.get_numero_scarpe(),sessione.get_altezza())  :
                                    for attrezzo_prenotato in sessione.get_lista_prenotazioni():
                                        if attrezzo_prenotato.get_codice_oggetto() != attrezzatura.get_codice():
                                            lista_filtrata.append(attrezzatura)
        return lista_filtrata

    def filtra_dimenisoni(self,dim_attrezzo,numero_scarpe_persona,altezza_persona):
        if int(dim_attrezzo) == int(numero_scarpe_persona) or int(dim_attrezzo) == int(altezza_persona):
            return True
        return False
    def prenota_attrezzatura(self,attrezzatura):
        if sessione.controlla_prenotazione_effettuata(attrezzatura.get_codice()):
            scadenza = date.today() + timedelta(hours=int(1))
            attrezzatura.set_stato(False)
            sessione.aggiungi_prenotazione(prenotazione(attrezzatura.get_codice(),
                                                        scadenza,
                                                        attrezzatura))
            return "Prenotazione effettuata"





