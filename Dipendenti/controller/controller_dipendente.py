# Controller del dipendente
class controller_dipendente:
    def __init__(self, dipendente):
        # Prende come model l'oggetto dipendente e viene passato come parametro al costruttore
        self.model = dipendente

    # Richiama i metodi della classe dipendente
    def get_dipendente_str(self):
        return self.model.get_dipendente_str()

    def get_dipendente_str_x_elenco(self):
        return self.model.get_dipendente_str_x_elenco()









