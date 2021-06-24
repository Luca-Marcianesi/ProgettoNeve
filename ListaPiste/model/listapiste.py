import json
import os
import pickle

from Pista.model.pista import Pista

# Classe lista piste


class ListaPiste:

    def __init__(self):

        # Definizione degli attributi
        self.lista_piste = []
        self.leggi_dati()

    # Metodo che restituisce la lista delle piste
    def get_lista(self):
        return self.lista_piste

    # Metodo che permette di settare lo stato di tutte le piste
    def set_stato_tutte(self, stato):
        for pista in self.lista_piste:
            pista.set_stato(stato)

    # Metodo che permette di salvare i dati in pickle
    def salva_dati(self):
        with open('Data/ListaPiste/lista_piste.pickle', 'wb') as file:
            pickle.dump(self.lista_piste, file, pickle.HIGHEST_PROTOCOL)

    # Metodo che permette di leggere i dati da pickle, se esiste, o da json
    def leggi_dati(self):
        if os.path.isfile('Data/ListaPiste/lista_piste.pickle'):
            with open('Data/ListaPiste/lista_piste.pickle', "rb") as file:
                self.lista_piste = pickle.load(file)
        else:
            with open("Data/ListaPiste/lista_piste.json") as file:
                lista_piste_inizio = json.load(file)
            for pista_da_caricare in lista_piste_inizio:
                self.lista_piste.append(
                    Pista(pista_da_caricare["nome"], pista_da_caricare["colore"], pista_da_caricare["stato"]))
