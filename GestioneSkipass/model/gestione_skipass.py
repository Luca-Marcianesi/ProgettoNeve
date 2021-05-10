import json

from Skipass.model.skipass import skipass
from datetime import  timedelta , datetime,date,time
from Prenotazione.model.prenotazione import prenotazione
from Sessione.model.sessione import sessione


class gestione_skipass:

    def __init__(self):
        self.lista_skipass = []
        self.inizio_stagione = None
        self.fine_stagione = None
        self.leggi_dati()

    def prenota(self,skipass_selezionato):
        if date.today() > date.fromisoformat(self.inizio_stagione) and date.today() < date.fromisoformat(self.fine_stagione) :
            if sessione.controlla_prenotazione_effettuata(1):
                if skipass_selezionato.tipo != "stagionale"and skipass_selezionato.tipo != "mensile"and skipass_selezionato.tipo != "settimanale":
                    scadenza = datetime(date.today().year, date.today().month, date.today().day,
                              time.fromisoformat(skipass_selezionato.inizio_validita).hour, time.fromisoformat(skipass_selezionato.inizio_validita).minute,
                              time.fromisoformat(skipass_selezionato.inizio_validita).second)
                    scadenza = scadenza + timedelta(hours = int(skipass_selezionato.durata))
                    sessione.aggiungi_prenotazione(prenotazione(1,scadenza,skipass_selezionato.descrizione))

                else:

                    if skipass_selezionato.tipo != "stagionale" :
                        scadenza = date.today() + timedelta(days = int(skipass_selezionato.durata))
                        sessione.aggiungi_prenotazione(prenotazione(1, scadenza, skipass_selezionato.descrizione))

                    else:
                        sessione.aggiungi_prenotazione(prenotazione(1, self.fine_stagione, skipass_selezionato.descrizione))



    def controlla_skipass_acquistato(self):
        for prenotazione in sessione.get_lista_prenotazioni():
            if prenotazione.get_codice_oggetto() == 1:
                return True
        return False

    def aggiungi_skipass(self,skipass):
        self.lista_skipass.append(skipass)

    def leggi_dati(self):
            with open("GestioneSkipass/data/lista_skipass.json") as file:
                file_oggetto = json.load(file)
                self.inizio_stagione = file_oggetto["data_inizio_stagione"]
                self.fine_stagione = file_oggetto["data_fine_stagione"]
                lista_skipass = file_oggetto["lista_skipass"]
                for oggetto_skipass in lista_skipass :
                        self.aggiungi_skipass(skipass(oggetto_skipass["tipo"],
                                                      oggetto_skipass["descrizione"],oggetto_skipass["inizio_validita"],
                                                      oggetto_skipass["durata(hours)"]))
                lista_abbonamenti = file_oggetto["lista_abbonamenti"]
                for abbonamento in lista_abbonamenti:
                        self.aggiungi_skipass(skipass(abbonamento["tipo"],abbonamento["descrizione"], "", abbonamento["durata(day)"]))

    def visualizza_lista(self):
        lista ="la stagione inizia: {}".format(self.inizio_stagione) + " e finisce: {} \n".format(self.fine_stagione)
        for skipass in self.lista_skipass:
            lista += skipass.print()
        return lista