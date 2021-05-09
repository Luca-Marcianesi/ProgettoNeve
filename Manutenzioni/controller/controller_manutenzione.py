class controller_manutenzione():
    def __init__(self,manutenzione):
        self.model = manutenzione

    def effettua_manutenzione(self):
        self.model.effettua_manutenzione()

    def visualizza_manutenzione(self):
        self.model.get_manutenzione_str()

    def get_codice(self):
        return self.model.get_codice()