import json
from Pista.model.pista import pista


class lista_piste:

    def __init__(self):
        self.lista_piste = []
        self.leggi_dati()

    def cerca_pista(self, nome):
        for pista in self.lista_piste:
            if pista.nome == nome:
                return pista
        return "Pista non trovata"

    def cerca_pista_x_numero(self, posizione):
        if posizione <= 0 or posizione > len(self.lista_piste) :
            return  "Pista inesistente"
        else :
            return self.lista_piste[posizione-1]

    def aggiungi_pista(self,pista):
        self.lista_piste.append(pista)

    def leggi_dati(self):
        with open("Pista/data/lista_piste.json") as file:
            lista_piste_inizio = json.load(file)
        for pista_da_caricare in lista_piste_inizio:
            self.aggiungi_pista(pista(pista_da_caricare["nome"],pista_da_caricare["colore"],pista_da_caricare["stato"]))

    def modifica_pista(self,posizione,stato):
        self.cerca_pista_x_numero(posizione).set_stato(stato)

    def visualizza_pista(self,numero):
        return self.lista_piste[numero].get_pista_str()

    def get_lista(self):
        return self.lista_piste
