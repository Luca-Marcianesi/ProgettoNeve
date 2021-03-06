import json
import os
import pickle
from datetime import date, timedelta, datetime
from Attrezzatura.model.attrezzatura import Attrezzatura
from Sessione.model.sessione import Sessione
from Prenotazione.model.prenotazione import Prenotazione

# Classe lista attrezzatura


class ListaAttrezzatura:
    def __init__(self):
        self.lista_attrezzatura = []
        self.leggi_dati()
        self.elimina_prenotazione_scadute()

    # Metodo per aggiungere un attrezzatura alla lista
    def aggiungi_attrezzatura(self, attrezzatura):
        self.lista_attrezzatura.append(attrezzatura)

    # Metodo per rimuovere un attrezzatura dalla lista
    def rimuovi_attrezzatura(self, attrezzatura):
        self.lista_attrezzatura.remove(attrezzatura)

    # Metodo per salvare i dati sul pickle
    def salva_dati(self):
        with open('Data/ListaAttrezzatura/lista_attrezzatura.pickle', 'wb') as file:
            pickle.dump(self.lista_attrezzatura, file, pickle.HIGHEST_PROTOCOL)

    # Metodo per leggere i dati dal pickle se esiste o dal json
    def leggi_dati(self):
        if os.path.isfile('Data/ListaAttrezzatura/lista_attrezzatura.pickle'):
            with open('Data/ListaAttrezzatura/lista_attrezzatura.pickle', "rb") as file:
                self.lista_attrezzatura = pickle.load(file)
        else:
            with open("Data/ListaAttrezzatura/lista_attrezzatura.json") as file:
                lista_attrezzatura = json.load(file)
                for attrezzatura_da_caricare in lista_attrezzatura:
                    self.aggiungi_attrezzatura(
                        Attrezzatura(attrezzatura_da_caricare["codice"],
                                     attrezzatura_da_caricare["nome"],
                                     attrezzatura_da_caricare["dimensioni"]))

    # Metodo che restituisce la lista dell'attrezzatura
    def get_lista_attrezzatura(self):
        return self.lista_attrezzatura

    # Metodo che restituisce la lista dell'attrezzatura adeguata alle caratteristiche del cliente che richiede
    # un certo tipo di attrezzo
    def get_lista_filtrata(self):
        lista_filtrata = []
        for attrezzatura in self.lista_attrezzatura:
            if attrezzatura.get_stato():
                if self.filtra_dimensioni(attrezzatura.get_dimensioni(), Sessione.get_numero_scarpe(),
                                          Sessione.get_altezza()):
                    if Sessione.controlla_prenotazione_effettuata(attrezzatura.get_codice()):
                        lista_filtrata.append(attrezzatura)
        return lista_filtrata

    # Metodo che confronta le dimensioni di ogni attrezzo con le caratteristiche del cliente
    def filtra_dimensioni(self, dim_attrezzo, numero_scarpe_persona, altezza_persona):
        if int(dim_attrezzo) == int(numero_scarpe_persona) or \
                (int(dim_attrezzo) >= (int(altezza_persona) -10) and int(dim_attrezzo) <= int(altezza_persona)):
            return True
        return False

    # Metodo per prenotare l'attrezzatura
    def prenota_attrezzatura(self, attrezzatura):
        scadenza = datetime.today() + timedelta(days=int(1))
        attrezzatura.prenota(scadenza)
        return Prenotazione(attrezzatura.get_codice(), scadenza, attrezzatura)

    # Metodo per eliminare le prenotazioni scadute
    def elimina_prenotazione_scadute(self):
        for attrezzo in self.lista_attrezzatura:
            if attrezzo.get_scadenza() is not None:
                oggi = datetime.today()
                controllare = attrezzo.get_scadenza()
                if controllare < oggi:
                    attrezzo.elimina_prenotazione()
