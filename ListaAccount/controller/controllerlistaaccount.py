from ListaAccount.model.listaaccount import ListaAccount

# Controller lista account


class ControllerListaAccount:
    def __init__(self):

        # Prende come model la classe lista account
        self.model = ListaAccount()

    # Richiama i metodi della classe lista account
    def crea_account(self, nome, cognome, username, password, eta, altezza, numero_scarpe):
        self.model.crea_account(nome, cognome, username, password, eta, altezza, numero_scarpe)

    def login(self, username, password):
        return self.model.login(username, password)

    def salva_dati(self):
        self.model.salva_dati()

    def controlla_username(self, username):
        return self.model.controlla_username(username)
