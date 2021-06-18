from ListaAccount.model.listaaccount import ListaAccount


# Controller relativo alla classe ListaAccount
class ControllerListaAccount:
    def __init__(self):
        # Prende come model la classe lista account
        self.model = ListaAccount()

    # Metodo che chiama la funzione crea_account del model
    def crea_account(self, nome, cognome, username, password, eta, altezza, numero_scarpe):
        self.model.crea_account(nome, cognome, username, password, eta, altezza, numero_scarpe)

    # Metodo che chiama la funzione login del model
    def login(self, username, password):
        return self.model.login(username, password)

    # Metodo che chiama la funzione salva_dati del model
    def salva_dati(self):
        self.model.salva_dati()

    # Metodo che chiama la funzione controlla_username del model
    def controlla_username(self, username):
        return self.model.controlla_username(username)

    # Metodo che chiama la funzione controlla_caratteristiche_persona del model
    def controlla_caratteristiche_persona(self,altezza, eta, numero_scarpe):
        return self.model.controlla_caratteristiche_persona(altezza, eta, numero_scarpe)

