
# Controller pista
class ControllerPista:
    def __init__(self, pista):

        # Prende come model l'oggetto pista e viene passato come parametro al costruttore
        self.model = pista

    # Richiama i metodi della classe pista
    def modifica_stato_pista(self, stato):
        self.model.set_stato(stato)

    def get_nome_str(self):
        return self.model.get_nome_str()

    def get_stato(self):
        return self.model.get_stato()

    def get_difficolta(self):
        return self.model.get_difficolta()
