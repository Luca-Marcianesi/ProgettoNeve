import json
from Skipass.model.skipass import Skipass
from datetime import timedelta, datetime, date, time
from Prenotazione.model.prenotazione import Prenotazione


# Classe che si occupa della gestione delle prenotazione degli skipass
class GestioneSkipass:
    def __init__(self):
        # Dichiarazione di una lista vuota da riempire con gli oggetti Skipass
        self.lista_skipass = []
        # Definizioni di due attributi utili per le prenotazioni (non assegnati per provare la funzione)
        self.inizio_stagione = None
        self.fine_stagione = None
        # Chiamata del metodo interno leggi_dati per il riempimento della lista con gli elementi salvati
        self.leggi_dati()
        # Codice identificativo degli skipass
        self.codice_skipass = 1

    # Metodo prenota (privato momentaneamente del controllo della stagione per poter effettuare il metodo)
    def prenota(self, skipass_selezionato):
        # if date.today() > date.fromisoformat(self.inizio_stagione) and
        # date.today() < date.fromisoformat(self.fine_stagione) :
        if skipass_selezionato.tipo != "Stagionale" and skipass_selezionato.tipo != "Mensile" and \
                skipass_selezionato.tipo != "Settimanale":

            scadenza = datetime(date.today().year,  # anno
                                date.today().month,  # mese
                                date.today().day,  # giorno
                                time.fromisoformat(skipass_selezionato.inizio_validita).hour,  # ora
                                time.fromisoformat(skipass_selezionato.inizio_validita).minute,  # minuti
                                time.fromisoformat(skipass_selezionato.get_inizio_validita()).second)  # secondi

            if scadenza.hour < datetime.today().hour:
                return False

            scadenza = scadenza + timedelta(hours=int(skipass_selezionato.get_durata()))

        elif skipass_selezionato.tipo != "Stagionale":
            scadenza = date.today() + timedelta(days=int(skipass_selezionato.get_durata()))

        else:
            scadenza = self.fine_stagione

        return Prenotazione(skipass_selezionato.get_codice(), scadenza, skipass_selezionato)

    # Metodo per aggiungere uno skipass
    def aggiungi_skipass(self, skipass):
        self.lista_skipass.append(skipass)

    # Metodo che restituisce lo skipass in base al numero dato
    def get_skipass_n(self, numero):
        return self.lista_skipass[numero]

    # Metodo che legge i dati dal pickle
    def leggi_dati(self):
        with open("Data/ListaSkipass/lista_skipass.json") as file:
            file_oggetto = json.load(file)
            self.inizio_stagione = file_oggetto["data_inizio_stagione"]
            self.fine_stagione = file_oggetto["data_fine_stagione"]
            lista_skipass = file_oggetto["lista_skipass"]
            for oggetto_skipass in lista_skipass:
                self.aggiungi_skipass(Skipass(oggetto_skipass["codice_oggetto"],
                                              oggetto_skipass["tipo"],
                                              oggetto_skipass["descrizione"],
                                              oggetto_skipass["inizio_validita"],
                                              oggetto_skipass["durata(hours)"]))
            lista_abbonamenti = file_oggetto["lista_abbonamenti"]
            for abbonamento in lista_abbonamenti:
                self.aggiungi_skipass(Skipass(abbonamento["codice_oggetto"],
                                              abbonamento["tipo"],
                                              abbonamento["descrizione"],
                                              "", abbonamento["durata(day)"]))

    # Metodo che restituisce la lista degli skipass
    def visualizza_lista(self):
        lista = "la stagione inizia: {}".format(self.inizio_stagione) + " e finisce: {} \n".format(self.fine_stagione)
        for skipass in self.lista_skipass:
            lista += skipass.print()
        return lista
