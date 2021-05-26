from ListaPiste.model.listapiste import ListaPiste


class ControllerListaPiste:
    def __init__(self):
        self.model = ListaPiste()

    def cerca_piste(self, nome):
        self.model.lista_piste(nome)

    def cerca_pista_x_numero(self, posizione):
        self.model.cerca_pista_x_numero(posizione)

    def aggiungi_pista(self, pista):
        self.model.aggiungi_pista(pista)

    def leggi_dati(self):
        self.model.leggi_dati()

    def modifica_pista(self, posizione, stato):
        self.model.modifica_pista(posizione, stato)

    def visualizza_pista(self, numero):
        self.model.visualizza_pista(numero)

    def get_lista(self):
        return self.model.get_lista()

    def set_stato_tutte(self, stato):
        self.model.set_stato_tutte(stato)

    def salva_dati(self):
        self.model.salva_dati()