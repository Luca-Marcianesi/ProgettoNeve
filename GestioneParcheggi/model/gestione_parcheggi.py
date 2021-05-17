import json
import os
import pickle
from datetime import date, timedelta

from Sessione.model.sessione import sessione
from Prenotazione.model.prenotazione import prenotazione


class gestione_parcheggi:
    def __init__(self):
        self.elenco_parcheggi = []
        self.codice_parcheggio = 6
        self.leggi_dati()
        self.elimina_scadute_prenotazioni()

    def prenota_parcheggio(self,numero_giorni):
        if sessione.controlla_prenotazione_effettuata(self.codice_parcheggio) :
            if self.get_posti_disponibili() > 0:
                for parcheggio in self.elenco_parcheggi:
                    if parcheggio.get_stato():
                        scadenza = date.today() + timedelta(days = int(numero_giorni))
                        sessione.aggiungi_prenotazione(prenotazione(parcheggio.get_codice(),scadenza,parcheggio))


    def get_posti_disponibili(self):
        posti = 0
        for parcheggio in self.elenco_parcheggi:
            if parcheggio.get_stato():
                posti +=1
        return posti

    def elimina_scadute_prenotazioni(self):
        if self.lista_prenotazioni_parcheggi == None:
            pass
        else :
            for prenotazione in self.lista_prenotazioni_parcheggi :
                if prenotazione.get_scadenza() < date.today() :
                    self.lista_prenotazioni_parcheggi.remove(prenotazione)


    def salva_dati(self):
        with open('GestioneParcheggi/data/parcheggi.pickle', 'wb') as dati:
            pickle.dump(self.lista_prenotazioni_parcheggi, dati, pickle.HIGHEST_PROTOCOL)

    def aggiungi_parcheggio(self,parcheggio):
        self.elenco_parcheggi.append(parcheggio)

    def leggi_dati(self):
        if os.path.isfile('GestioneParcheggi/data/parcheggi.pickle'):
            with open('GestioneParcheggi/data/parcheggi.pickle',"rb") as file:
                self.lista_prenotazioni_parcheggi = pickle.load(file)
        else :
            with open("ListaPiste/data/lista_piste.json") as file:
                elenco_parcheggi = json.load(file)
            for parcheggio in elenco_parcheggi:
                self.aggiungi_parcheggio(
                    parcheggio(parcheggio["codice"], parcheggio["numero"], parcheggio["stato"]))

