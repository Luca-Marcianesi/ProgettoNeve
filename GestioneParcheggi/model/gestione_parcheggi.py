import os
import pickle
from datetime import date, timedelta

from Sessione.model.sessione import sessione
from Prenotazione.model.prenotazione import prenotazione


class gestione_parcheggi:
    def __init__(self):
        self.lista_prenotazioni_parcheggi = []
        self.posti_disponibili = None
        self.leggi_dati()
        print(self.posti_disponibili )
        self.elimina_scadute_prenotazioni()
        self.calcola_posti()
        print(self.posti_disponibili)

    def prenota_parcheggio(self,numero_giorni):
        if sessione.controlla_prenotazione_effettuata(6) :
            if self.posti_disponibili > 0:
                scadenza = date.today() + timedelta(days = int(numero_giorni))
                prenotazione_da_aggiungere  = prenotazione(6,scadenza,"parcheggio numero:{}".format(self.posti_disponibili))
                sessione.aggiungi_prenotazione(prenotazione_da_aggiungere)
                self.aggiungi_prenotazione(prenotazione_da_aggiungere)
                self.posti_disponibili -= 1
                return "Prenotazione effettuata"
            return "Posti terminati"
        return "Possiedi già un parcheggio prenotato"

    def calcola_posti(self):
        self.posti_disponibili = 30 - self.lista_prenotazioni_parcheggi.__len__()

    def aggiungi_prenotazione(self,prenotazione):
        self.lista_prenotazioni_parcheggi.append(prenotazione)

    def elimina_scadute_prenotazioni(self):
        if self.lista_prenotazioni_parcheggi == None:
            pass
        else :
            for prenotazione in self.lista_prenotazioni_parcheggi :
                if prenotazione.get_scadenza() < date.today() :
                    self.lista_prenotazioni_parcheggi.remove(prenotazione)
                    self.posti_disponibili += 1

    def get_posti_disponibili(self):
        return self.posti_disponibili

    def salva_dati(self):
        with open('GestioneParcheggi/data/parcheggi.pickle', 'wb') as dati:
            pickle.dump(self.lista_prenotazioni_parcheggi, dati, pickle.HIGHEST_PROTOCOL)

    def leggi_dati(self):
        if os.path.isfile('GestioneParcheggi/data/parcheggi.pickle'):
            with open('GestioneParcheggi/data/parcheggi.pickle',"rb") as file:
                self.lista_prenotazioni_parcheggi = pickle.load(file)
        else :
            self.posti_disponibili = 30

