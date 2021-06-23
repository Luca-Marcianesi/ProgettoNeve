import unittest
from ListaAccount.model.listaaccount import ListaAccount
from Sessione.model.sessione import Sessione


class MyTest(unittest.TestCase):

    def setUp(self):
        self.lista = ListaAccount()
        self.lista.crea_account("Edoardo", "Tarulli", "edo10", "password", "20", "180", "45")
        self.lista.login("edo10", "password")

    # Verifica visualizza credenziali
    def test1(self):
        self.assertTrue(Sessione.get_nome() == "Diego")
        self.assertTrue(Sessione.get_cognome() == "Mignani")
        self.assertTrue(Sessione.get_altezza() == "180")
        self.assertFalse(Sessione.get_eta() == "22")
        self.assertFalse(Sessione.get_numero_scarpe == "42")

    # Test modifica credenziali
    def test2(self):
        Sessione.cambia_eta("18")
        Sessione.cambia_altezza("190")
        Sessione.cambia_numero_scarpe("44")
        self.assertFalse(Sessione.get_altezza() == "170")
        self.assertTrue(Sessione.get_eta() == "18")
        self.assertTrue(Sessione.get_numero_scarpe == "44")

    # Test modifica password
    def test3(self):
        Sessione.cambia_password("pass")
        self.assertTrue(self.lista.login("dieg10", "pass"))


if __name__ == 'main':
    unittest.main()