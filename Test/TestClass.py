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

    # Test del login proprietario
    def test1(self):
        self.assertTrue(self.lista.login("admin", "admin"))

    # Test del login cliente
    def test2(self):
        # Password giusta
        self.assertTrue(self.lista.login("dieg10", "password"))
        # Password sbagliata
        self.assertFalse(self.lista.login("dieg10", "pass"))

    # Verifica credenziali
    def test3(self):
        self.lista.login("dieg10", "password")
        assert (Sessione.get_nome() == "Diego")
        assert (Sessione.get_cognome() == "Mignani")
        assert (Sessione.get_altezza() == "180")
        self.assertFalse(Sessione.get_eta() == "22")

    # Test prenotazione parcheggio
    def test4(self):
        # Prima prenotazione
        self.assertEqual(self.parcheggi.prenota_parcheggio(2), "Prenotazione effettuata")
        # Doppia prenotazione
        self.assertEqual(self.parcheggi.prenota_parcheggio(2), "Hai già una prenotazione")

    # Test prenotazione skipass
    def test5(self):
        # Skipass settimanale
        settimanale = self.skipass.visualizza_lista(3)
        # Prima prenotazione
        self.assertTrue(self.skipass.prenota_skipass(settimanale))
        # Doppia prenotazione
        self.assertFalse(self.skipass.prenota_skipass(settimanale))

    # Test aggiunta attrezzatura da parte del proprietario e prenotazione di quell'attrezzatura dal cliente
    def test6(self):
        # Proprietario
        racchette = Attrezzatura(5, "Racchette", 130)
        self.attrezzatura.aggiungi_attrezzatura(racchette)
        # Cliente
        self.assertEqual(self.attrezzatura.prenota_attrezzatura(racchette), "Prenotazione effettuata")


if __name__ == 'main':
    unittest.main()
