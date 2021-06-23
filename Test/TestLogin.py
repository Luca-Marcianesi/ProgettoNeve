import unittest
from ListaAccount.model.listaaccount import ListaAccount


class MyTest(unittest.TestCase):

    def setUp(self):
        self.lista = ListaAccount()
        self.lista.crea_account("Diego", "Mignani", "dieg10", "password", "20", "180", "45")

    # Test del login proprietario
    def test1(self):
        self.assertTrue(self.lista.login("admin", "admin"))

    # Test del login Cliente:
    def test2(self):
        # Password giusta
        self.assertTrue(self.lista.login("dieg10", "password"))

    # Test del login Cliente:
    def test3(self):
        # Password sbagliata
        self.assertFalse(self.lista.login("dieg10", "pass"))


if __name__ == 'main':
    unittest.main()