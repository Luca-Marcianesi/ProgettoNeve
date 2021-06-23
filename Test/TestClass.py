import unittest

from Attrezzatura.model.attrezzatura import Attrezzatura
from GestioneParcheggi.controller.controllergestioneparcheggi import ControllerGestioneParcheggi
from GestioneSkipass.controller.controllergestioneskipass import ControllerGestioneSkipass
from ListaAccount.model.listaaccount import ListaAccount
from ListaAttrezzatura.controller.controllerlistaattrezzatura import ControllerListaAttrezzatura
from Sessione.model.sessione import Sessione


class MyTest(unittest.TestCase):

    def setUp(self):
        self.attrezzatura = ControllerListaAttrezzatura()
        self.parcheggi = ControllerGestioneParcheggi()
        self.skipass = ControllerGestioneSkipass()
        self.lista = ListaAccount()
        self.lista.crea_account("Diego", "Mignani", "dieg10", "password", "20", "180", "45")
        self.lista.login("dieg10", "password")

    # Verifica credenziali
    def test2(self):
        self.assertTrue(Sessione.get_nome() == "Diego")
        self.assertTrue(Sessione.get_cognome() == "Mignani")
        self.assertTrue(Sessione.get_altezza() == "180")
        self.assertFalse(Sessione.get_eta() == "22")

    # Test prenotazione parcheggio
    def test3(self):
        # Prima prenotazione
        self.assertEqual(self.parcheggi.prenota_parcheggio(2), "Prenotazione effettuata")
        # Doppia prenotazione
        self.assertEqual(self.parcheggi.prenota_parcheggio(2), "Hai già una prenotazione")

    # Test prenotazione skipass
    def test4(self):
        # Skipass settimanale
        settimanale = self.skipass.visualizza_lista(3)
        # Prima prenotazione
        self.assertTrue(self.skipass.prenota_skipass(settimanale))
        # Doppia prenotazione
        self.assertFalse(self.skipass.prenota_skipass(settimanale))

    # Test aggiunta attrezzatura da parte del proprietario e prenotazione di quell'attrezzatura dal cliente
    def test5(self):
        # Proprietario
        racchette = Attrezzatura(5, "Racchette", 130)
        self.attrezzatura.aggiungi_attrezzatura(racchette)
        # Cliente
        self.assertEqual(self.attrezzatura.prenota_attrezzatura(racchette), "Prenotazione effettuata")


