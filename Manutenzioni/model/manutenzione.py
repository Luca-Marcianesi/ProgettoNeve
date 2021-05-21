from datetime import timedelta, date


class manutenzione:
    def __init__(self, nome, cadenza, ultima_manutenzione,prossima_scadenza):
        self.nome = nome
        self.cadenza = cadenza
        self.ultima_manutenzione = ultima_manutenzione
        self.prossima_scadenza = prossima_scadenza

    def effettua_manutenzione(self):
        self.ultima_manutenzione = date.today()
        self.prossima_manutenzione = self.ultima_manutenzione + timedelta(days = int(self.cadenza))

    def get_nome(self):
        return self.nome

    def get_prossima_scadenza(self):
        return self.prossima_scadenza


    def get_manutenzione_str(self):
        return "Nome: {}\nCadenza: {}\n" \
               "Ultima manutenzione: {}\nProssima Manutenzione: {}\n".format(self.nome,self.cadenza,
                                                                             self.ultima_manutenzione,self.prossima_manutenzione)