import json
import os.path
import pickle

from Account.model.account import account
from Sessione.model.sessione import sessione

class lista_account:

    def __init__(self):
        self.lista_account = []
        self.leggi_dati()

    def crea_account(self, nome, cognome, username, password, eta, altezza, numero_scarpe):
        if self.controlla_username(username):
            return "Username già in uso"
        else:
            self.lista_account.append(account(nome, cognome, username, password, eta, altezza, numero_scarpe))

    def login(self, username, password):
        for account in self.lista_account:
            if account.username == username and account.password == password:
                sessione.login(account, self.salva_dati)
                return True
        return False

    def controlla_username(self, username):
        for account in self.lista_account:
            if account.username == username:
                return True
        return False

    def salva_dati(self):
        with open('ListaAccount/data/lista_account_salvata.pickle', 'wb') as dati:
            pickle.dump(self.lista_account, dati, pickle.HIGHEST_PROTOCOL)

    def leggi_dati(self):
        if os.path.isfile('ListaAccount/data/lista_account_salvata.pickle'):
            with open('ListaAccount/data/lista_account_salvata.pickle',"rb") as file:
                self.lista_account = pickle.load(file)
        else  :
            with open("ListaAccount/data/lista_account.json") as file:
                lista = json.load(file)
                for account_da_aggiungere in lista :
                    acc = account(account_da_aggiungere["nome"],
                                  account_da_aggiungere["cognome"],
                                  account_da_aggiungere["username"],
                                  account_da_aggiungere["password"],
                                  account_da_aggiungere["eta"],
                                  account_da_aggiungere["altezza"],
                                  account_da_aggiungere["numero_scarpe"])
                    acc.set_permessi(True)
                    self.lista_account.append(acc)

