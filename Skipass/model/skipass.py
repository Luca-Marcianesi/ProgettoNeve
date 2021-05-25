
# Classe skipass
class skipass:

    def __init__(self,codice, tipo,descrizione,inizio_validita,durata):

        # Definizione attributi
        self.codice = codice
        self.tipo = tipo
        self.descrizione = descrizione
        self.inizio_validita = inizio_validita
        self.durata = durata

    # Metodo che restituisce il codice
    def get_codice(self):
        return self.codice

    # Metodo che restituisce il tipo
    def get_tipo(self):
        return self.tipo

    # Metodo che restituisce la desccrizione
    def get_descrizione(self):
        return self.descrizione

    # Metodo che restituisce l'inizio validità dello skipass
    def get_inizio_validita(self):
        return self.inizio_validita

    # Metodo che restituisce la durata dello skipass
    def get_durata(self):
        return self.durata




