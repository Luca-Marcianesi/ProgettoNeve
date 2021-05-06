from Dipendenti.model.dipendente import dipendente
class elenco_dipendenti:

    def __init__(self):
        self.elenco = []

    def aggiungi(self, nome, cognome, telefono):
        self.elenco.append(dipendente( nome, cognome, telefono))

    def rimuovi(self, nome, cognome):
        for dipendente in self.elenco:
            if ((dipendente.nome == nome) and (dipendente.cognome == cognome)):
                self.elenco.remove(dipendente)
