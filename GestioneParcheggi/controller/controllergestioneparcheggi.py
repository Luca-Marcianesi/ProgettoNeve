from GestioneParcheggi.model.gestioneparcheggi import GestioneParcheggi


# Controller relativo alla classe GestioneParcheggi
class ControllerGestioneParcheggi:
    def __init__(self):
        # Prende come model la classe gestione parcheggi
        self.model = GestioneParcheggi()

    # Metodo che chiama la funzione prenota_parcheggio del model
    def prenota_parcheggio(self, numero_giorni):
        return self.model.prenota_parcheggio(numero_giorni)

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
