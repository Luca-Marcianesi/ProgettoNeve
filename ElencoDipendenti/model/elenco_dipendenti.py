import json
import os
import pickle

from Dipendenti.model.dipendente import dipendente


class elenco_dipendenti:

    def __init__(self):
        self.elenco = []
        self.leggi_dati()

    def aggiungi_dipendente(self, dipendente):
        self.elenco.append(dipendente)

    def rimuovi_dipendente(self, nome, cognome):
        for dipendente in self.elenco:
            if dipendente.nome == nome and dipendente.cognome == cognome:
                self.elenco.remove(dipendente)
            else:
                return "Dipendente non trovato"


    def get_dipendente(self, nome, cognome):
        for dipendente in self.elenco:
            if dipendente.nome == nome and dipendente.cognome == cognome:
                return dipendente
            else:
                return "Dipendente non trovato"

    def get_lista_elenco_dipendenti(self):
        return self.elenco


    def salva_dati(self):
        with open('ElencoDipendenti/data/lista_dipendenti_salvata.pickle', 'wb') as dati:
            pickle.dump(self.elenco, dati, pickle.HIGHEST_PROTOCOL)

    def leggi_dati(self):
        if os.path.isfile('ElencoDipendenti/data/lista_dipendenti_salvata.pickle'):
            with open('ElencoDipendenti/data/lista_dipendenti_salvata.pickle', "rb") as file:
                self.elenco = pickle.load(file)
        else:
            with open("ElencoDipendenti/data/lista_dipendenti.json") as file:
                lista_dipendenti = json.load(file)
            for dipendenti_da_caricare in lista_dipendenti:
                self.aggiungi_dipendente(dipendente(dipendenti_da_caricare["nome"], dipendenti_da_caricare["cognome"],
                                 dipendenti_da_caricare["numero di telefono"]))
