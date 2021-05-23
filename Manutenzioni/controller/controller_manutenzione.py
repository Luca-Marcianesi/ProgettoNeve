class controller_manutenzione:
    def __init__(self,manutenzione):
        self.model = manutenzione

    def effettua_manutenzione(self):
        self.model.effettua_manutenzione()

    def visualizza_manutenzione(self):
        return self.model.get_manutenzione_str()

    def get_nome(self):
        return self.model.get_nome()

    def get_prossima_scadenza(self):
        return self.model.get_prossima_scadenza()

