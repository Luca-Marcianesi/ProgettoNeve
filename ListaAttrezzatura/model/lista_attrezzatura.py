class listaAttrezzatura:
    def __init__(self):
        self.lista_attrezzatura = []

    def aggiungi_attrezzatura(self, attrezzatura):
        self.lista_attrezzatura.append(attrezzatura)

    def rimuovi_attrezzatura(self, indice):
        self.lista_attrezzatura.remove(indice)

    def set_stato(self, stato):
        self.stato = stato

    def prenota_attrezzatura(self, tipo):
        for attrezzatura in self.lista_attrezzatura:
            if attrezzatura.get_tipo() == tipo:
                attrezzatura.set_stato(False)
            else:
                return "Attrezzatura già prenotata o non disponibile"