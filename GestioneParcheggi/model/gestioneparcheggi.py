import json
import os
import pickle
from datetime import date, timedelta

from Sessione.model.sessione import Sessione
from Prenotazione.model.prenotazione import Prenotazione
from Parcheggio.model.parcheggio import Parcheggio

# Classe gestione parcheggi
class gestione_parcheggi:
    def __init__(self):

        # Definizione degli attributi
        self.elenco_parcheggi = []
        self.codice_parcheggio = 2
        self.leggi_dati()
        self.elimina_scadute_prenotazioni()

    # Metodo prenota parcheggio
    def prenota_parcheggio(self,numero_giorni):
        if Sessione.controlla_prenotazione_effettuata(self.codice_parcheggio):
            if self.get_posti_disponibili() > 0:
                for parcheggio in self.elenco_parcheggi:
                    if parcheggio.get_stato():
                        scadenza = date.today() + timedelta(days = int(numero_giorni))
                        parcheggio.prenota(scadenza)
                        Sessione.aggiungi_prenotazione(Prenotazione(parcheggio.get_codice(), scadenza, parcheggio))
                        Sessione.salva_dati()
                        self.salva_dati()
                        return "Prenotazione effettuata"
            return "Posti esauriti"
        return "Hai già una prenotazione"

    # Metodo che restituisce i posti disponibili
    def get_posti_disponibili(self):
        posti = 0
        for parcheggio in self.elenco_parcheggi:
            print(parcheggio.stato)
            if parcheggio.get_stato():
                posti +=1
        return posti

    # Metodo che elimina le prenotazioni scadute
    def elimina_scadute_prenotazioni(self):
            for parcheggio in self.elenco_parcheggi :
                if parcheggio.get_scadenza() != None:
                    oggi = date.today()
                    controllare = parcheggio.get_scadenza()
                    if controllare < oggi:
                        parcheggio.elimina_prenotazione()

    # Metodo salva dati con creazione del pickle
    def salva_dati(self):
        with open('GestioneParcheggi/data/parcheggi.pickle', 'wb') as dati:
            pickle.dump(self.elenco_parcheggi, dati, pickle.HIGHEST_PROTOCOL)

    # Metodo per aggiungere un parcheggio
    def aggiungi_parcheggio(self, parcheggio):
        self.elenco_parcheggi.append(parcheggio)

    # Metodo che legge i dati dal pickle se esiste o dal json
    def leggi_dati(self):
        if os.path.isfile('GestioneParcheggi/data/parcheggi.pickle'):
            with open('GestioneParcheggi/data/parcheggi.pickle', "rb") as file:
                self.elenco_parcheggi = pickle.load(file)
        else:
            with open("GestioneParcheggi/data/parcheggio.json") as file:
                elenco_parcheggi = json.load(file)
            for parcheggio_da_agg in elenco_parcheggi:
                self.aggiungi_parcheggio(
                    Parcheggio(parcheggio_da_agg["codice"], parcheggio_da_agg["numero"], parcheggio_da_agg["stato"]))

