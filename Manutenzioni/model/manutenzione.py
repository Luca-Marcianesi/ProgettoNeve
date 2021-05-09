from datetime import timedelta, date


class manutenzione:
    def __init__(self, nome,codice, cadenza, ultima_manutenzione,prossima_manutenzione):
        self.nome = nome
        self.codice = codice
        self.cadenza = cadenza
        self.ultima_manutenzione = ultima_manutenzione
        self.prossima_manutenzione = prossima_manutenzione

    def effettua_manutenzione(self):
        self.ultima_manutenzione = date.today()
        self.prossima_manutenzione = self.ultima_manutenzione + timedelta(days = int(self.cadenza))

    def get_codice(self):
        return self.codice

    def get_manutenzione_str(self):
        return "Codice: {}\nNome: {}\nCadenza: {}\n" \
               "Ultima manutenzione: {}\nProssima Manutenzione: {}\n".format(self.codice,self.nome,self.cadenza,
                                                                             self.ultima_manutenzione,self.prossima_manutenzione)