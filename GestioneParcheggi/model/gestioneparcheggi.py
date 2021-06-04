import json
import os
import pickle
from datetime import date, timedelta

from Sessione.model.sessione import Sessione
from Prenotazione.model.prenotazione import Prenotazione
from Parcheggio.model.parcheggio import Parcheggio


# Classe che si occupa della gestione delle prenotazione dei parcheggi
class GestioneParcheggi:
    def __init__(self):

        # Dichiarazione di una lista vuota da riempire con gli oggetti Parcheggio
        self.elenco_parcheggi = []
        # Codice degli oggetti parcheggio
        self.codice_parcheggio = 2
        # Chiamata del metodo interno leggi_dati per il riempimento della lista con gli elementi salvati
        self.leggi_dati()
        # Eliminazione dalla lista di tutte le prenotazioni scadute
        self.elimina_scadute_prenotazioni()

    # Metodo che si occupa della prenotazione del parcheggio
    def prenota_parcheggio(self, numero_giorni):
        if Sessione.controlla_prenotazione_effettuata(self.codice_parcheggio):
            if self.get_posti_disponibili() > 0:
                for parcheggio in self.elenco_parcheggi:
                    if parcheggio.get_stato():
                        scadenza = date.today() + timedelta(days=int(numero_giorni))
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
            if parcheggio.get_stato():
                posti += 1
        return posti

    # Metodo che elimina le prenotazioni scadute
    def elimina_scadute_prenotazioni(self):
        for parcheggio in self.elenco_parcheggi:
            if parcheggio.get_scadenza() is not None:
                oggi = date.today()
                controllare = parcheggio.get_scadenza()
                if controllare < oggi:
                    parcheggio.elimina_prenotazione()

    # Metodo salva dati con creazione del file pickle
    def salva_dati(self):
        with open('Data/GestioneParcheggio/parcheggi.pickle', 'wb') as dati:
            pickle.dump(self.elenco_parcheggi, dati, pickle.HIGHEST_PROTOCOL)

    # Metodo per aggiungere un parcheggio
    def aggiungi_parcheggio(self, parcheggio):
        self.elenco_parcheggi.append(parcheggio)

    # Metodo che legge i dati dal file pickle se esiste, se no dal json
    def leggi_dati(self):
        if os.path.isfile('Data/GestioneParcheggio/parcheggi.pickle'):
            with open('Data/GestioneParcheggio/parcheggi.pickle', "rb") as file:
                self.elenco_parcheggi = pickle.load(file)
        else:
            with open("Data/GestioneParcheggio/parcheggio.json") as file:
                elenco_parcheggi = json.load(file)
            for parcheggio_da_agg in elenco_parcheggi:
                self.aggiungi_parcheggio(
                    Parcheggio(parcheggio_da_agg["codice"], parcheggio_da_agg["numero"], parcheggio_da_agg["stato"]))
