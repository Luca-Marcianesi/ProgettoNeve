from ListaAttrezzatura.model.ListaAttrezzatura import ListaAttrezzatura
from Sessione.model.sessione import Sessione


class ControllerListaAttrezzatura:
    def __init__(self):

        # Prende come model la classe lista attrezzatura
        self.model = ListaAttrezzatura()

    # Richiama i metodi della classe lista attrezzatura
    def aggiungi_attrezzatura(self, attrezzatura):
        self.model.aggiungi_attrezzatura(attrezzatura)

    def rimuovi_attrezzatura(self, attrezzatura):
        self.model.rimuovi_attrezzatura(attrezzatura)
        self.salva_dati()

    def get_lista_attrezzatura(self):
        return self.model.get_lista_attrezzatura()

    def get_lista_filtrata(self):
        return self.model.get_lista_filtrata()

    def prenota_attrezzatura(self, attrezzatura):
        if Sessione.controlla_prenotazione_effettuata(attrezzatura.get_codice()):
            prenotazione = self.model.prenota_attrezzatura(attrezzatura)
            Sessione.aggiungi_prenotazione(prenotazione)
            self.salva_dati()
            return "Prenotazione effettuata"

    def salva_dati(self):
        self.model.salva_dati()
