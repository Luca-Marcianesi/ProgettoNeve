from GestioneSkipass.model.gestione_skipass import gestione_skipass
class controller_gestione_skipass():
    def __init__(self):
        self.model = gestione_skipass()

    def prenota_skipass(self,skipass_selezionato):
        self.model.prenota(skipass_selezionato)

    def get_lista_skipass(self):
        return self.model.visualizza_lista()

    def controlla_skipass_acquistato(self):
        return self.model.controlla_skipass_acquistato()