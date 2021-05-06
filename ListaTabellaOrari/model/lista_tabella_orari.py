class lista_tabella_orari:

    def __init__(self):
        self.lista_tabella_orari = []

    def aggiungi_tabella(self, tabella_orari):
        self.lista_tabella_orari.append(tabella_orari)

    def rimuovi_tabella(self, numero_tabella):
        for tabella in self.lista_tabella_orari:
            if self.lista_tabella_orari[tabella] == numero_tabella:
                self.lista_tabella_orari.remove(tabella)