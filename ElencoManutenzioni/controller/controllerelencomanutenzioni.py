from ElencoManutenzioni.model.elencomanutenzioni import ElencoManutenzioni

# Controller elenco manutenzioni


class ControllerElencoManutenzioni:

    def __init__(self):

        # Prende come model la classe elenco manutenzioni
        self.model = ElencoManutenzioni()

    # Ridefinisce i metodi della classe elenco manutenzioni
    def salva_dati(self):
        self.model.salva_dati()

    def get_elenco_manutenzioni(self):
        return self.model.get_elenco_manutenzioni()
