# Controller della classe Dipendente
class ControllerDipendente:

    def __init__(self, dipendente):
        # Prende come model l'oggetto dipendente e viene passato come parametro al costruttore
        self.model = dipendente

    # Metodo che richiama il metodo get_dipendente_str della classe Dipendente
    def get_dipendente_str(self):
        return self.model.get_dipendente_str()
    # Metodo che richiama il metodo get_dipendente_str_x_elenco della classe Dipendente
    def get_dipendente_str_x_elenco(self):
        return self.model.get_dipendente_str_x_elenco()
