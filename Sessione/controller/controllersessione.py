from Sessione.model.sessione import Sessione

# Controller sessione


class ControllerSessione:

    def __init__(self):

        # Prende come model la classe sessione
        self.model = Sessione()

    # Richiama i metodi della classe sessione
    def cambia_password(self, password):
        self.model.cambia_password(password)

    def cambia_eta(self, eta):
        self.model.cambia_eta(eta)

    def cambia_altezza(self, altezza):
        self.model.cambia_altezza(altezza)

    def cambia_numero_scarpe(self, numero_scarpe):
        self.model.cambia_numero_scarpe(numero_scarpe)

    def get_lista_prenotazioni(self):
        return self.model.get_lista_prenotazioni()

    def aggiungi_prenotazione(self, prenotazione):
        self.model.aggiungi_prenotazione(prenotazione)

    def get_nome_str(self):
        return self.model.get_nome()

    def get_cognome_str(self):
        return self.model.get_cognome()

    def get_altezza_str(self):
        return self.model.get_altezza()

    def get_numero_scarpe_str(self):
        return self.model.get_numero_scarpe()

    def get_eta_str(self):
        return self.model.get_eta()

    def get_permessi(self):
        return self.model.get_permessi()

    def salva_dati(self):
        self.model.salva_dati()
