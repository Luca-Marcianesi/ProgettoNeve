from datetime import timedelta, date

# Classe manutenzione
class manutenzione:
    def __init__(self, nome, cadenza, ultima_manutenzione, prossima_scadenza):
        self.nome = nome
        self.cadenza = cadenza
        self.ultima_manutenzione = ultima_manutenzione
        self.prossima_scadenza = prossima_scadenza

    # Metodo che permette di effettuare una manutenzione
    def effettua_manutenzione(self):
        self.ultima_manutenzione = date.today()
        self.prossima_scadenza = self.ultima_manutenzione + timedelta(days=int(self.cadenza))

    # Metodo che restituisce il nome della manutenzione
    def get_nome(self):
        return self.nome

    # Metodo che restituisce la scadenza di una manutenzione
    def get_prossima_scadenza(self):
        return self.prossima_scadenza

    # Metodo che restituisce di una manutenzione con la sua descrizione
    def get_manutenzione_str(self):
        return "Nome: {}\nCadenza: {} giorni\n" \
               "Ultima manutenzione: {}\nProssima Manutenzione: {}\n".format(self.nome, self.cadenza,
                                                                             self.ultima_manutenzione, self.prossima_scadenza)
