import json
import os.path
import pickle

from Account.model.account import Account
from Sessione.model.sessione import Sessione

# Classe lista account


class ListaAccount:

    def __init__(self):

        # Definizione degli attributi
        self.lista_account = []
        self.leggi_dati()

    # Metodo per creare l'account
    def crea_account(self, nome, cognome, username, password, eta, altezza, numero_scarpe):
        if self.controlla_username(username):
            return "Username già in uso"
        else:
            self.lista_account.append(Account(nome, cognome, username, password, eta, altezza, numero_scarpe))

    # Metodo per effettuare il login
    def login(self, username, password):
        for account in self.lista_account:
            if account.username == username and account.password == password:
                Sessione.login(account, self.salva_dati)
                return True
        return False

    # Metodo che controlla che non venga inserito un username già esistente
    def controlla_username(self, username):
        for account in self.lista_account:
            if account.username == username:
                return True
        return False

    def controlla_caratteristiche_persona(self, altezza, eta, numero_scarpe):
        if int(altezza) < 50 or int(altezza) > 220 or int(eta) <= 5 or int(eta) > 130 or int(
                numero_scarpe) <= 20 or int(numero_scarpe) > 50:
            return False
        return True

    # Metodo che salva i dati sul pickle
    def salva_dati(self):
        with open('Data/ListaAccount/lista_account_salvata.pickle', 'wb') as dati:
            pickle.dump(self.lista_account, dati, pickle.HIGHEST_PROTOCOL)

    # Metodo che legge i dati dal pickle se esiste o dal json (contiene solo l'account del proprietario)
    def leggi_dati(self):
        if os.path.isfile('Data/ListaAccount/lista_account_salvata.pickle'):
            with open('Data/ListaAccount/lista_account_salvata.pickle', "rb") as file:
                self.lista_account = pickle.load(file)
        else:
            with open("Data/ListaAccount/lista_account.json") as file:
                lista = json.load(file)
                for account_da_aggiungere in lista:
                    acc = Account(account_da_aggiungere["nome"],
                                  account_da_aggiungere["cognome"],
                                  account_da_aggiungere["username"],
                                  account_da_aggiungere["password"],
                                  account_da_aggiungere["eta"],
                                  account_da_aggiungere["altezza"],
                                  account_da_aggiungere["numero_scarpe"])
                    acc.set_permessi(True)
                    self.lista_account.append(acc)
