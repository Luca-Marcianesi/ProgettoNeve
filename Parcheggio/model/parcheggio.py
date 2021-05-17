class parcheggio:
    def __init__(self, codice, numero, stato, scadenza):
        self.codice = codice
        self.numero = numero
        self.stato = stato
        self.scadenza = scadenza

    def get_codice(self):
        return self.codice

    def set_stato(self, stato):
        self.stato = stato

    def get_numero(self):
        return self.numero

