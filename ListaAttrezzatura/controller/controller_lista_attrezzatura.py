from ListaAttrezzatura.model.ListaAttrezzatura import lista_attrezzatura

class controller_lista_attrezzatura:
    def __init__(self):
        self.model = lista_attrezzatura()

    def aggiungi_attrezzatura(self, attrezzatura):
        self.model.aggiungi_attrezzatura(attrezzatura)

    def rimuovi_attrezzatura(self, indice):
        self.model.rimuovi_attrezzatura(indice)

    def set_stato(self, stato):
        self.model.set_stato(stato)

    def prenota_attrezzatura(self, tipo):
        self.model.prenota_attrezzatura(tipo)

    def get_lista_attrezzatura(self):
        return self.model.get_lista_attrezzatura()

    def get_lista_filtrata(self):
        return self.model.get_lista_filtrata()
