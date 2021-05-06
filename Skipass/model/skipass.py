from datetime import timedelta

class skipass:

    def __init__(self, tipo,descrizione,inizio_validita,durata):
        self.tipo = tipo
        self.descrizione = descrizione
        self.inizio_validita = inizio_validita
        self.durata = durata


    def print(self):
        if self.tipo == "giornaliero" or self.tipo =="mattiniero" or self.tipo =="pomeridiano" :
            unita = "ore"
        else :
            unita = "giorni"
        return "tipo: {}\ndescrizione: {}\ninizio validità: {}\ndurata: {} {}\n\n".format(self.tipo,self.descrizione,self.inizio_validita,self.durata,unita)

