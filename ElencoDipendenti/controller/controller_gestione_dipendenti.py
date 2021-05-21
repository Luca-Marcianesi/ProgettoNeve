from ElencoDipendenti.model.elenco_dipendenti import elenco_dipendenti


class controller_elenco_dipendenti:
    def __init__(self):
        self.model = elenco_dipendenti()

    def aggiungi(self, dipendente):
        self.model.aggiungi_dipendente(dipendente)

    def rimuovi(self,dipendente):
        self.model.rimuovi_dipendente(dipendente)

    def get_dipendente(self, nome, cognome):
        return self.model.get_dipendente(nome, cognome)

    def get_lista_elenco_dipendenti(self):
        return self.model.get_lista_elenco_dipendenti()

    def get_lista_elenco_dipendenti_str(self):
        return self.model.get_lista_elenco_dipendenti_str()

    def salva_dati(self):
        self.model.salva_dati()
