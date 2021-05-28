from ElencoManutenzioni.model.elenco_manutenzioni import ElencoManutenzioni


# Controller relativo alla classe elenco_manutenzioni
class ControllerElencoManutenzioni:

    def __init__(self):
        # Prende come model la classe elenco manutenzioni
        self.model = ElencoManutenzioni()

    # Metodo che chiama la funzione salva_dati del model
    def salva_dati(self):
        self.model.salva_dati()

    # Metodo che chiama la funzione get_elenco_manutenzioni del model
    def get_elenco_manutenzioni(self):
        return self.model.get_elenco_manutenzioni()
