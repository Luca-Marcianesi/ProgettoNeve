
class skipass:

    def __init__(self, tipo,descrizione,inizio_validita,durata):
        self.tipo = tipo
        self.descrizione = descrizione
        self.inizio_validita = inizio_validita
        self.durata = durata

    def get_tipo(self):
        return self.tipo

    def get_descrizione(self):
        return self.descrizione

    def get_inizio_validita(self):
        return self.inizio_validita

    def get_durata(self):
        return self.durata



