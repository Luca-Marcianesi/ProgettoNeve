from ListaPiste.model.listapiste import ListaPiste


class ControllerListaPiste:
    def __init__(self):
        self.model = ListaPiste()

    def aggiungi_pista(self, pista):
        self.model.aggiungi_pista(pista)

    def leggi_dati(self):
        self.model.leggi_dati()

    def get_lista(self):
        return self.model.get_lista()

    def set_stato_tutte(self, stato):
        self.model.set_stato_tutte(stato)

    def salva_dati(self):
        self.model.salva_dati()
