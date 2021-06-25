import unittest
from Attrezzatura.model.attrezzatura import Attrezzatura
from GestioneParcheggi.controller.controllergestioneparcheggi import ControllerGestioneParcheggi
from GestioneSkipass.controller.controllergestioneskipass import ControllerGestioneSkipass
from ListaAccount.model.listaaccount import ListaAccount
from ListaAttrezzatura.controller.controllerlistaattrezzatura import ControllerListaAttrezzatura
from Sessione.model.sessione import Sessione


class TestClass(unittest.TestCase):
    # Configurazione degli attributi utilizzati nella classe
    def setUp(self):
        self.attrezzatura = ControllerListaAttrezzatura()
        self.parcheggi = ControllerGestioneParcheggi()
        self.skipass = ControllerGestioneSkipass()
        self.lista = ListaAccount()
        self.lista.crea_account("Diego", "Mignani", "dieg10", "password", "20", "180", "45")
        self.lista.login("dieg10", "password")

    # Test del login Proprietario:
    def test1(self):
        self.assertTrue(self.lista.login("admin", "admin"))

    # Test del login Cliente:
    def test2(self):
        # Password sbagliata
        self.assertFalse(self.lista.login("dieg10", "pass"))
        # Password giusta
        self.assertTrue(self.lista.login("dieg10", "password"))

    # Verifica credenziali
    def test3(self):
        self.assertEqual(Sessione.get_nome(), "Diego")
        self.assertEqual(Sessione.get_cognome(), "Mignani")
        self.assertEqual(Sessione.get_altezza(), "180")
        self.assertEqual(Sessione.get_eta(), "20")
        self.assertEqual(Sessione.get_numero_scarpe(), "45")

    # Test modifica password
    def test4(self):
        Sessione.cambia_password("pass")
        self.assertTrue(self.lista.login("dieg10", "pass"))

    # Test modifica credenziali
    def test5(self):
        Sessione.cambia_eta("18")
        Sessione.cambia_altezza("190")
        Sessione.cambia_numero_scarpe("44")
        self.assertEqual(Sessione.get_altezza(), "190")
        self.assertEqual(Sessione.get_eta(), "18")
        self.assertEqual(Sessione.get_numero_scarpe(), "44")

    # Test prenotazione parcheggio
    def test6(self):
        # Prima prenotazione
        self.assertEqual(self.parcheggi.prenota_parcheggio(2), "Prenotazione effettuata")
        # Doppia prenotazione
        self.assertEqual(self.parcheggi.prenota_parcheggio(2), "Hai già una prenotazione")

    # Test prenotazione skipass
    def test7(self):
        # Skipass settimanale
        settimanale = self.skipass.visualizza_lista(3)
        # Prima prenotazione
        self.assertTrue(self.skipass.prenota_skipass(settimanale))
        # Doppia prenotazione
        self.assertFalse(self.skipass.prenota_skipass(settimanale))

    # Test aggiunta attrezzatura da parte del proprietario e prenotazione di quell'attrezzatura dal cliente
    def test8(self):
        # Proprietario
        racchette = Attrezzatura(5, "Racchette", 130)
        self.attrezzatura.aggiungi_attrezzatura(racchette)
        # Cliente
        self.assertEqual(self.attrezzatura.prenota_attrezzatura(racchette), "Prenotazione effettuata")

if __name__ == "__main__":
    unittest.main()
