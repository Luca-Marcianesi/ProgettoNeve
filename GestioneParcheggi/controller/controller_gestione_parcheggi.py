from GestioneParcheggi.model.gestione_parcheggi import gestione_parcheggi

class controller_gestione_parcheggi:
    def __init__(self):
        self.model = gestione_parcheggi()

    def prenota_parcheggio(self,numero_giorni):
        return self.model.prenota_parcheggio(numero_giorni)

    def get_posti_disponibili(self):
        return self.model.get_posti_disponibili()

    def salva_dati(self):
        self.model.salva_dati()