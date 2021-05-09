
class lista_tabella_orari:

    def __init__(self):
        self.lista_tabella_orari = []

    def aggiungi_tabella(self, tabella_orari):
        self.lista_tabella_orari.append(tabella_orari)

    def rimuovi_tabella(self, numero_tabella):
        for tabella in self.lista_tabella_orari:
            if tabella.get_numero_tabella == numero_tabella:
                self.lista_tabella_orari.remove(tabella)

    def get_lista_tabella_orari(self):
        return self.lista_tabella_orari
