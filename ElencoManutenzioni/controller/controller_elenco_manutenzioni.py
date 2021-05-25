from ElencoManutenzioni.model.elenco_manutenzioni import elenco_manutenzioni

# Controller elenco manutenzioni
class controller_elenco_manutenzioni():

    def __init__(self):

        # Prende come model la classe elenco manutenzioni
        self.model = elenco_manutenzioni()

    # Ridefinisce i metodi della classe elenco manutenzioni
    def salva_dati(self):
        self.model.salva_dati()

    def get_elenco_manutenzioni(self):
        return self.model.get_elenco_manutenzioni()