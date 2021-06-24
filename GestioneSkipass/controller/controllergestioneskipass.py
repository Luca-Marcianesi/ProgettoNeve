from GestioneSkipass.model.gestioneskipass import GestioneSkipass
from Sessione.model.sessione import Sessione


# Controller relativo alla classe GestioneSkipass
class ControllerGestioneSkipass:
    def __init__(self):
        # Prende come model la classe gestione skipass
        self.model = GestioneSkipass()

    # Metodo che chiama la funzione prenota_skipass del model
    def prenota_skipass(self, skipass_selezionato):
        if Sessione.controlla_prenotazione_effettuata(self.model.codice_skipass):
            prenotazione = self.model.prenota(skipass_selezionato)
            if prenotazione != False:
                Sessione.aggiungi_prenotazione(prenotazione)
                return True
            return False

    # Metodo che chiama la funzione visualizza_lista del model
    def get_lista_skipass(self):
        return self.model.visualizza_lista()

    # Metodo che chiama la funzione get_skipass_n del model
    def visualizza_lista(self, numero):
        return self.model.get_skipass_n(numero)

    # Metodo che chiama la funzione aggiungi_skipass del model
    def aggiungi_skipass(self, skipass):
        self.model.aggiungi_skipass(skipass)
