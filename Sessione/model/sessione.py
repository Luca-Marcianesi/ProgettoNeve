
# Classe globale sessione


class Sessione:

    # Attributi
    account_loggato = None
    funzione_salva_dati = None

    # Metodo per fare il login
    @classmethod
    def login(cls, account, salva_dati):
        cls.funzione_salva_dati = salva_dati
        cls.account_loggato = account
        cls.elimina_prenotazioni_scadute()

    # Metodo per settare l'età
    @classmethod
    def cambia_eta(cls, eta):
        cls.account_loggato.set_eta(eta)

    # Metodo per settare il numero di scarpe
    @classmethod
    def cambia_numero_scarpe(cls, numero_scarpe):
        cls.account_loggato.set_numero_scarpe(numero_scarpe)

    # Metodo per settare l'altezza
    @classmethod
    def cambia_altezza(cls, altezza):
        cls.account_loggato.set_altezza(altezza)

    # Metodo per settare la password
    @classmethod
    def cambia_password(cls, password):
        cls.account_loggato.set_password(password)

    # Metodo per aggiungere una prenotazione
    @classmethod
    def aggiungi_prenotazione(cls, prenotazione):
        cls.account_loggato.aggiungi_prenotazione(prenotazione)

    # Metodo che restituisce la lista delle prenotazioni
    @classmethod
    def get_lista_prenotazioni(cls):
        return cls.account_loggato.get_lista_prenotazioni()

    # Metodo che restituisce il nome dell'account loggato
    @classmethod
    def get_nome(cls):
        return cls.account_loggato.get_nome()

    # Metodo che restituisce il cognome dell'account loggato
    @classmethod
    def get_cognome(cls):
        return cls.account_loggato.get_cognome()

    # Metodo che restituisce l'età dell'account loggato
    @classmethod
    def get_eta(cls):
        return cls.account_loggato.get_eta()

    # Metodo che restituisce il numero di scarpe dell'account loggato
    @classmethod
    def get_numero_scarpe(cls):
        return cls.account_loggato.get_numero_scarpe()

    # Metodo che restituisce l'altezza dell'account loggato
    @classmethod
    def get_altezza(cls):
        return cls.account_loggato.get_altezza()

    # Metodo che restituisce i permessi, per il login del proprietario
    @classmethod
    def get_permessi(cls):
        return cls.account_loggato.get_permessi()

    # Metodo per eliminare le prenotazioni scadute
    @classmethod
    def elimina_prenotazioni_scadute(cls):
        cls.account_loggato.elimina_scadute_prenotazioni()

    # Metodo che controlla se sia stata effettuata una prenotazione
    @classmethod
    def controlla_prenotazione_effettuata(cls, codice):
        return cls.account_loggato.controlla_prenotazione_effettuata(codice)

    # Metodo salva dati che verrà richiamato nella classe che lo necessita
    @classmethod
    def salva_dati(cls):
        cls.funzione_salva_dati()
