from ElencoDipendenti.model.elenco_dipendenti import elenco_dipendenti


class controller_elenco_dipendenti:
    def __init__(self):
        self.model = elenco_dipendenti()

    def aggiungi(self, nome, cognome, telefono):
        self.model.aggiungi( nome, cognome, telefono)

    def rimuovi(self, nome, cognome):
        self.model.rimuovi(nome, cognome)
