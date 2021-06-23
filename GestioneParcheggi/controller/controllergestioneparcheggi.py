from GestioneParcheggi.model.gestioneparcheggi import GestioneParcheggi
from Sessione.model.sessione import Sessione

# Controller relativo alla classe GestioneParcheggi


class ControllerGestioneParcheggi:
    def __init__(self):
        # Prende come model la classe gestione parcheggi
        self.model = GestioneParcheggi()

    # Metodo che controlla se l'account logato ha già una prenotazione se no
    # chiama la funzione prenota_parcheggio del model
    def prenota_parcheggio(self, numero_giorni):
        if Sessione.controlla_prenotazione_effettuata(self.model.codice_parcheggio):
            esito = self.model.prenota_parcheggio(numero_giorni)
            if esito is not None:
                Sessione.aggiungi_prenotazione(esito)
                Sessione.salva_dati()
                risultato = "Prenotazione effettuata"
                return risultato
            return "Posti esauriti"
        return "Hai già una prenotazione"

    # Metodo che chiama la funzione get_posti_disponibili del model
    def get_posti_disponibili(self):
        return self.model.get_posti_disponibili()

    # Metodo che chiama la funzione salva_dati del model
    def salva_dati(self):
        self.model.salva_dati()

    # Metodo che chiama la funzione elimina_scadute_prenotazioni del model
    def elimina_scadute_prenotazioni(self):
        self.model.elimina_scadute_prenotazioni()

    # Metodo che chiama la funzione aggiungi_parcheggio del model
    def aggiungi_parcheggio(self, parcheggio):
        self.model.aggiungi_parcheggio(parcheggio)
