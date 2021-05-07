
class account:
    def __init__(self, nome, cognome, username, password, eta, altezza, numero_scarpe):
        self.nome = nome
        self.cognome = cognome
        self.username = username
        self.password = password
        self.eta = eta
        self.altezza = altezza
        self.numero_scarpe = numero_scarpe
        self.lista_prenotazioni = []
#account

    def set_eta(self, eta):
        self.eta = eta

    def set_numero_scarpe(self, numero_scarpe):
        self.numero_scarpe = numero_scarpe

    def set_altezza(self, altezza):
        self.altezza = altezza

    def aggiungi_prenotazione(self, prenotazione):
        self.lista_prenotazioni.append(prenotazione)

    def rimuovi_prenotazione(self, tipo):
        self.lista_prenotazioni.remove(tipo)

    def get_lista_prenotazioni(self):
        return self.lista_prenotazioni

    def get_nome(self):
        return self.nome

    def get_cognome(self):
        return self.cognome

    def get_eta(self):
        return self.eta

    def get_altezza(self):
        return self.altezza

    def get_numero_scarpe(self):
        return self.numero_scarpe

    def set_password(self, password):
        self.password = password

    def v_lista(self):
        for prenotazione in self.lista_prenotazioni :
            prenotazione.visualizza()