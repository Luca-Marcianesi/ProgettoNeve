import unittest
from ListaAccount.model.listaaccount import ListaAccount


class MyTest(unittest.TestCase):

    def test1(self):
        lista = ListaAccount()
        assert (lista.login("admin", "admin") is True)

    def test2(self):
        lista = ListaAccount()
        assert (lista.login("admin", "admin") is True)

if __name__ == 'main':
    unittest.main()