import json

from Skipass.model.skipass import skipass
from datetime import  timedelta , datetime,date,time
from Prenotazione.model.prenotazione import prenotazione
from Sessione.model.sessione import Sessione

# Classe gestione skipass
class gestione_skipass:

    def __init__(self):

        # Definizione attributi
        self.lista_skipass = []
        self.inizio_stagione = None
        self.fine_stagione = None
        self.leggi_dati()
        self.codice_skipass = 1

    # Metodo prenota
    def prenota(self,skipass_selezionato):
        #if date.today() > date.fromisoformat(self.inizio_stagione) and date.today() < date.fromisoformat(self.fine_stagione) :
            if Sessione.controlla_prenotazione_effettuata(self.codice_skipass):

                if skipass_selezionato.tipo != "Stagionale"and skipass_selezionato.tipo != "Mensile"and skipass_selezionato.tipo != "Settimanale":

                    scadenza = datetime(date.today().year, date.today().month, date.today().day,
                                time.fromisoformat(skipass_selezionato.inizio_validita).hour,
                                time.fromisoformat(skipass_selezionato.inizio_validita).minute,
                                time.fromisoformat(skipass_selezionato.get_inizio_validita()).second)

                    scadenza = scadenza + timedelta(hours = int(skipass_selezionato.get_durata()))

                    Sessione.aggiungi_prenotazione(prenotazione(skipass_selezionato.get_codice(),
                                                                scadenza,
                                                                skipass_selezionato))

                else:

                    if skipass_selezionato.tipo != "Stagionale" :

                        scadenza = date.today() + timedelta(days = int(skipass_selezionato.get_durata()))

                        Sessione.aggiungi_prenotazione(prenotazione(skipass_selezionato.get_codice(),
                                                                    scadenza,
                                                                    skipass_selezionato))

                    else:
                        Sessione.aggiungi_prenotazione(prenotazione(skipass_selezionato.get_codice(),
                                                                    self.fine_stagione,
                                                                    skipass_selezionato))
    # Metodo che controlla se lo skipass è già stato acquistato
    def controlla_skipass_acquistato(self):
        for prenotazione in Sessione.get_lista_prenotazioni():
            if prenotazione.get_codice_oggetto() == self.codice_skipass:
                return True
        return False

    # Metodo per aggiungere uno skipass
    def aggiungi_skipass(self,skipass):
        self.lista_skipass.append(skipass)

    # Metodo che restituisce lo skipass in base al numero dato
    def get_skipass_n(self,numero):
        return self.lista_skipass[numero]

    # Metodo che legge i dati dal pickle
    def leggi_dati(self):
            with open("GestioneSkipass/data/lista_skipass.json") as file:
                file_oggetto = json.load(file)
                self.inizio_stagione = file_oggetto["data_inizio_stagione"]
                self.fine_stagione = file_oggetto["data_fine_stagione"]
                lista_skipass = file_oggetto["lista_skipass"]
                for oggetto_skipass in lista_skipass :
                        self.aggiungi_skipass(skipass(oggetto_skipass["codice_oggetto"],
                                                      oggetto_skipass["tipo"],
                                                      oggetto_skipass["descrizione"],oggetto_skipass["inizio_validita"],
                                                      oggetto_skipass["durata(hours)"]))
                lista_abbonamenti = file_oggetto["lista_abbonamenti"]
                for abbonamento in lista_abbonamenti:
                        self.aggiungi_skipass(skipass(abbonamento["codice_oggetto"],
                                                      abbonamento["tipo"],
                                                      abbonamento["descrizione"],
                                                      "", abbonamento["durata(day)"]))

    # Metodo che restituisce la lista degli skipass
    def visualizza_lista(self):
        lista ="la stagione inizia: {}".format(self.inizio_stagione) + " e finisce: {} \n".format(self.fine_stagione)
        for skipass in self.lista_skipass:
            lista += skipass.print()
        return lista