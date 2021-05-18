import json
import os
import pickle
from datetime import date, timedelta

from Sessione.model.sessione import sessione
from Prenotazione.model.prenotazione import prenotazione
from Parcheggio.model.parcheggio import parcheggio


class gestione_parcheggi:
    def __init__(self):
        self.elenco_parcheggi = []
        self.codice_parcheggio = 6
        self.leggi_dati()
        #self.elimina_scadute_prenotazioni()

    def prenota_parcheggio(self,numero_giorni):
        if sessione.controlla_prenotazione_effettuata(self.codice_parcheggio) :
            if self.get_posti_disponibili() > 0:
                for parcheggio in self.elenco_parcheggi:
                    if parcheggio.get_stato():
                        parcheggio.set_stato(False)
                        scadenza = date.today() + timedelta(days = int(numero_giorni))
                        sessione.aggiungi_prenotazione(prenotazione(parcheggio.get_codice(),scadenza,parcheggio))
                        return "Prenotazione effettuata"
            return "Posti esauriti"
        return "Hai già una prenotazione"

    def get_posti_disponibili(self):
        posti = 0
        for parcheggio in self.elenco_parcheggi:
            if parcheggio.get_stato():
                posti +=1
        return posti
    """
    def elimina_scadute_prenotazioni(self):
        if self.lista_prenotazioni_parcheggi == None:
            pass
        else :
            for prenotazione in self.lista_prenotazioni_parcheggi :
                if prenotazione.get_scadenza() < date.today() :
                    self.lista_prenotazioni_parcheggi.remove(prenotazione)
    """

    def salva_dati(self):
        with open('GestioneParcheggi/data/parcheggi.pickle', 'wb') as dati:
            pickle.dump(self.elenco_parcheggi, dati, pickle.HIGHEST_PROTOCOL)

    def aggiungi_parcheggio(self,parcheggio):
        self.elenco_parcheggi.append(parcheggio)

    def leggi_dati(self):
        if os.path.isfile('GestioneParcheggi/data/parcheggi.pickle'):
            with open('GestioneParcheggi/data/parcheggi.pickle',"rb") as file:
                self.elenco_parcheggi = pickle.load(file)
        else :
            with open("GestioneParcheggi/data/parcheggio.json") as file:
                elenco_parcheggi = json.load(file)
            for parcheggio_da_agg in elenco_parcheggi:
                self.aggiungi_parcheggio(
                    parcheggio(parcheggio_da_agg["codice"], parcheggio_da_agg["numero"], parcheggio_da_agg["stato"]))

