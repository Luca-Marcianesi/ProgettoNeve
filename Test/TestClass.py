import unittest
from GestioneParcheggi.model.gestioneparcheggi import GestioneParcheggi
from ListaAccount.model.listaaccount import ListaAccount
from Sessione.model.sessione import Sessione


class MyTest(unittest.TestCase):

    def setUp(self):
        self.parcheggi = GestioneParcheggi()
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
        assert (Sessione.get_eta() == "22")

    def test4(self):
        self.parcheggi.prenota_parcheggio(2)

if __name__ == 'main':
    unittest.main()