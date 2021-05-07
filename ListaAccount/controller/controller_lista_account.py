from ListaAccount.model.lista_account import lista_account

class controller_lista_account():
    def __init__(self):
        self.model = lista_account()

    def crea_account(self, nome, cognome, username, password, eta, altezza, numero_scarpe):
        self.model.crea_account(nome, cognome, username, password, eta, altezza, numero_scarpe)

    def login(self, username, password):
        return self.model.login(username, password)

    def salva_dati(self):
        self.model.salva_dati()