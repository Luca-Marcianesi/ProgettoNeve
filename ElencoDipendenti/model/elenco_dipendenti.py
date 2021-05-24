import json
import os
import pickle

from Dipendenti.model.dipendente import dipendente

# Classe elenco dipendenti
class elenco_dipendenti:

    def __init__(self):

        # Definizione attributi
        self.elenco = []
        self.leggi_dati()

    # Metodo per aggiungere un dipendente
    def aggiungi_dipendente(self, dipendente):
        self.elenco.append(dipendente)

    # Metodo per rimuovere un dipendente
    def rimuovi_dipendente(self, dipendente):
        self.elenco.remove(dipendente)

    # Metodo che restituisce un dipendente se è presente nella lista
    def get_dipendente(self, nome, cognome):
        for dipendente in self.elenco:
            if dipendente.nome == nome and dipendente.cognome == cognome:
                return dipendente
            else:
                return "Dipendente non trovato"

    # Metodo che restituisce l'elenco dei dipendenti
    def get_lista_elenco_dipendenti(self):
        return self.elenco

    # Metodo che restituisce l'elenco con il nome dei dipendenti
    def get_lista_elenco_dipendenti_str(self):
        elenco =""
        for dipendente in self.elenco:
            elenco = elenco + dipendente.nome +"\n"
        return elenco

    # Metodo per creare il pickle contenente i dipendenti presi dall'elenco
    def salva_dati(self):
        with open('ElencoDipendenti/data/lista_dipendenti_salvata.pickle', 'wb') as dati:
            pickle.dump(self.elenco, dati, pickle.HIGHEST_PROTOCOL)

    # Metodo che legge i dati dal pickle se esiste o dal json
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
