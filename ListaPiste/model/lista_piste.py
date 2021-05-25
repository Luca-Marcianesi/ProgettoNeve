import json
import os
import pickle

from Pista.model.pista import Pista

# Classe lista piste
class lista_piste:

    def __init__(self):

        # Definizione degli attributi
        self.lista_piste = []
        self.leggi_dati()

    # Metodo che cerca la pista, se esistente, in base al nome
    def cerca_pista(self, nome):
        for pista in self.lista_piste:
            if pista.nome == nome:
                return pista
        return "Pista non trovata"

    # Metodo che cerca la pista in base
    def cerca_pista_x_numero(self, posizione):
        if posizione <= 0 or posizione > len(self.lista_piste) :
            return  "Pista inesistente"
        else :
            return self.lista_piste[posizione-1]

    # Metodo che aggiunge una pista alla lista
    def aggiungi_pista(self,pista):
        self.lista_piste.append(pista)

    # Metodo che permette di modificare una pista
    def modifica_pista(self,posizione,stato):
        self.cerca_pista_x_numero(posizione).set_stato(stato)

    # Metodo che restituisce la pista in base al numero
    def visualizza_pista(self,numero):
        return self.lista_piste[numero].get_pista_str()

    # Metodo che restituisce la lista delle piste
    def get_lista(self):
        return self.lista_piste

    # Metodo che permette di settare lo stato di tutte le piste
    def set_stato_tutte(self,stato):
        for pista in self.lista_piste:
            pista.set_stato(stato)

    # Metodo che permette di salvare i dati in pickle
    def salva_dati(self):
        with open('ListaPiste/data/lista_piste.pickle', 'wb') as file:
            pickle.dump(self.lista_piste, file, pickle.HIGHEST_PROTOCOL)

    # Metodo che permette di leggere i dati da pickle, se esiste, o da json
    def leggi_dati(self):
        if os.path.isfile('ListaPiste/data/lista_piste.pickle'):
            with open('ListaPiste/data/lista_piste.pickle',"rb") as file:
                self.lista_piste = pickle.load(file)
        else :
            with open("ListaPiste/data/lista_piste.json") as file:
                lista_piste_inizio = json.load(file)
            for pista_da_caricare in lista_piste_inizio:
                self.aggiungi_pista(
                    Pista(pista_da_caricare["nome"], pista_da_caricare["colore"], pista_da_caricare["stato"]))