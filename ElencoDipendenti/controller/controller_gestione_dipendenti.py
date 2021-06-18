from ElencoDipendenti.model.elenco_dipendenti import ElencoDipendenti


# Controller gestione dipendenti
class ControllerElencoDipendenti:

    def __init__(self):
        # Prende come model la classe elenco dipendenti
        self.model = ElencoDipendenti()

    # Metodo che richiama il metodo aggiungi_dipendente della classe elenco dipendenti
    def aggiungi(self, dipendente):
        self.model.aggiungi_dipendente(dipendente)

    # Metodo che richiama il metodo rimuovi_dipendente della classe elenco dipendenti
    def rimuovi(self, dipendente):
        self.model.rimuovi_dipendente(dipendente)

    # Metodo che richiama il metodo get_dipendente della classe elenco dipendenti
    def get_dipendente(self, nome, cognome):
        return self.model.get_dipendente(nome, cognome)

    # Metodo che richiama il metodo get_lista_elenco_dipendenti della classe elenco dipendenti
    def get_elenco_dipendenti(self):
        return self.model.get_elenco_dipendenti()

    # Metodo che richiama il metodo get_lista_elenco_dipendenti_str della classe elenco dipendenti
    def get_elenco_dipendenti_str(self):
        return self.model.get_elenco_dipendenti_str()

    # Metodo che richiama il metodo salva_dati della classe elenco dipendenti
    def salva_dati(self):
        self.model.salva_dati()
