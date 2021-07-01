from datetime import date, datetime


# Classe che definisce la struttura di un account generale
class Account:
    # Costruttore utile per la assegnazione dei suoi attributi ai parametri passati
    def __init__(self, nome, cognome, username, password, eta, altezza, numero_scarpe):

        # Dati caratteristici di un account
        self.nome = nome
        self.cognome = cognome
        self.username = username
        self.password = password
        self.eta = eta
        self.altezza = altezza
        self.numero_scarpe = numero_scarpe

        """Definisce l'importanza di un account:
                - False se è un account destinato ai clienti
                - True se è destinato al proprietario dello stabilimento    """
        self.permesso = False

        # Lista delle prenotazioni effettuate dal singolo account
        self.lista_prenotazioni = []

    # Metodo per settare l'età
    def set_eta(self, eta):
        self.eta = eta

    # Metodo per settare il numero di scarpe
    def set_numero_scarpe(self, numero_scarpe):
        self.numero_scarpe = numero_scarpe

    # Metodo per settare l'altezza
    def set_altezza(self, altezza):
        self.altezza = altezza

    # Metodo per settare la password
    def set_password(self, password):
        self.password = password

    # Metodo per settare i permessi del proprietario
    def set_permessi(self, permesso):
        self.permesso = permesso

    # Metodo per aggiungere una prenotazione
    def aggiungi_prenotazione(self, prenotazione):
        self.lista_prenotazioni.append(prenotazione)

    # Metodo che restituisce la lista delle prenotazioni
    def get_lista_prenotazioni(self):
        return self.lista_prenotazioni

    # Metodo che restituisce il nome
    def get_nome(self):
        return self.nome

    # Metodo che restituisce il cognome
    def get_cognome(self):
        return self.cognome

    # Metodo che restituisce l'età
    def get_eta(self):
        return self.eta

    # Metodo che restituisce l'altezza
    def get_altezza(self):
        return self.altezza

    # Metodo che restituisce il numero di scarpe
    def get_numero_scarpe(self):
        return self.numero_scarpe

    # Metodo che restituisce i permessi del proprietario
    def get_permessi(self):
        return self.permesso

    # Metodo che elimina le prenotazioni scadute
    def elimina_scadute_prenotazioni(self):
        if self.lista_prenotazioni is None:
            pass
        else:
            for prenotazione in self.lista_prenotazioni:
                controllare = prenotazione.get_scadenza()
                if isinstance(controllare, datetime): # controlla se la variabile "controllare" è del tipo datetime per evitare errori
                    oggi = datetime.now(None)  # viene preso oggi come istanza della classe datetime il parametro None riguarda il fuso orario(time zone)
                else:
                    oggi = date.today()# viene preso oggi come istanza della classe date
                if oggi > controllare:
                    if self.lista_prenotazioni.__len__() == 1:
                        self.lista_prenotazioni.clear()
                    else:
                        self.lista_prenotazioni.remove(prenotazione)

    # Metodo che controlla se una prenotazione è stata effettuata in base al codice dell'oggetto
    def controlla_prenotazione_effettuata(self, codice):
        if self.lista_prenotazioni is not None:
            for prenotazione in self.lista_prenotazioni:
                if prenotazione.get_codice_oggetto() == codice:
                    return False
        return True
