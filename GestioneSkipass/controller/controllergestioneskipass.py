from GestioneSkipass.model.gestioneskipass import GestioneSkipass


# Controller relativo alla classe GestioneSkipass
from Sessione.model.sessione import Sessione


class ControllerGestioneSkipass:
    def __init__(self):
        # Prende come model la classe gestione skipass
        self.model = GestioneSkipass()

    # Metodo che chiama la funzione prenota_skipass del model
    def prenota_skipass(self, skipass_selezionato):
        if Sessione.controlla_prenotazione_effettuata(self.model.codice_skipass):
            prenotazione = self.model.prenota(skipass_selezionato)
            Sessione.aggiungi_prenotazione(prenotazione)

    # Metodo che chiama la funzione get_lista_skipass del model
    def get_lista_skipass(self):
        return self.model.visualizza_lista()

    # Metodo che chiama la funzione controlla_skipass_acquistato del model
    def controlla_skipass_acquistato(self):
        return Sessione.controlla_prenotazione_effettuata(self.model.codice_skipass)

    # Metodo che chiama la funzione get_skipass_n del model
    def visualizza_lista(self, numero):
        return self.model.get_skipass_n(numero)

    # Metodo che chiama la funzione aggiungi_skipass del model
    def aggiungi_skipass(self, skipass):
        self.model.aggiungi_skipass(skipass)
