class elenco_dipendenti:

    def __init__(self):
        self.elenco = []

    def aggiungi_dipendente(self, dipendente):
        self.elenco.append(dipendente)

    def rimuovi_dipendente(self, nome, cognome):
        for dipendente in self.elenco:
            if dipendente.nome == nome and dipendente.cognome == cognome:
                self.elenco.remove(dipendente)
            else:
                return "Dipendente non trovato"


    def get_dipendente(self, nome, cognome):
        for dipendente in self.elenco:
            if dipendente.nome == nome and dipendente.cognome == cognome:
                return dipendente
            else:
                return "Dipendente non trovato"

    def get_lista_elenco_dipendenti(self):
        return self.elenco
