from GestioneParcheggi.model.gestioneparcheggi import GestioneParcheggi

# Controller gestione parcheggi


class ControllerGestioneParcheggi:
    def __init__(self):

        # Prende come model la classe gestione parcheggi
        self.model = GestioneParcheggi()

    # Richiama i metodi della classe gestione parcheggi
    def prenota_parcheggio(self, numero_giorni):
        return self.model.prenota_parcheggio(numero_giorni)

    def get_posti_disponibili(self):
        return self.model.get_posti_disponibili()

    def salva_dati(self):
        self.model.salva_dati()

    def elimina_scadute_prenotazioni(self):
        self.model.elimina_scadute_prenotazioni()

    def aggiungi_parcheggio(self, parcheggio):
        self.model.aggiungi_parcheggio(parcheggio)