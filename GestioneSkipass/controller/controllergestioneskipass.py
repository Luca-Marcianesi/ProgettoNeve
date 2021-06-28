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
            if prenotazione is not False:
                Sessione.aggiungi_prenotazione(prenotazione)
                return 'Skipass prenotato!'
            return 'Skipass al momento non disponibile torna domani'
        return 'Hai già prenotato uno skipass!'

    # Metodo che chiama la funzione get_skipass_n del model
    def get_skipass_per_numero(self, numero):
        return self.model.get_skipass_per_numero(numero)

