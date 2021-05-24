
# Controller manutenzione
class controller_manutenzione:
    def __init__(self,manutenzione):

        # Prende come model la classe manutenzione e il controller prende in ingresso la manutenzione
        self.model = manutenzione

    # Richiama i metodi della classe manutenzione
    def effettua_manutenzione(self):
        self.model.effettua_manutenzione()

    def visualizza_manutenzione(self):
        return self.model.get_manutenzione_str()

    def get_nome(self):
        return self.model.get_nome()

    def get_prossima_scadenza(self):
        return self.model.get_prossima_scadenza()