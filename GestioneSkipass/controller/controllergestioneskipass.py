from GestioneSkipass.model.gestioneskipass import GestioneSkipass

# Controller gestione skipass


class ControllerGestioneSkipass:
    def __init__(self):

        # Prende come model la classe gestione skipass
        self.model = GestioneSkipass()

    # Richiama i metodi della classe gestione skipass
    def prenota_skipass(self, skipass_selezionato):
        self.model.prenota(skipass_selezionato)

    def get_lista_skipass(self):
        return self.model.visualizza_lista()

    def controlla_skipass_acquistato(self):
        return self.model.controlla_skipass_acquistato()

    def get_skipass_n(self, numero):
        return self.model.get_skipass_n(numero)

    def aggiungi_skipass(self, skipass):
        self.model.aggiungi_skipass(skipass)

    def visualizza_lista(self):
        return self.model.visualizza_lista()
