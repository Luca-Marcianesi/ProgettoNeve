# Classe Dipendente
class dipendente:
    def __init__(self, nome, cognome, telefono):

        # Definizione degli attributi
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono

    # Metodo che restituisce nome e cognome del dipendente
    def get_dipendente_str(self):
        return self.nome + " " + self.cognome

    # Metodo che restituisce nome, cognome, telefono del dipendente con descrizione
    def get_dipendente_str_x_elenco(self):
        return "Nome: {} \nCognome: {} \nTelefono: {}".format(self.nome,self.cognome,self.telefono)