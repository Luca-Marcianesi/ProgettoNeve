class dipendente:
    def __init__(self, nome, cognome, telefono):
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono

    def get_dipendente_str(self):
        return self.nome + " " + self.cognome

    def get_dipendente_str_x_elenco(self):
        return "Nome: {} \nCognome: {} \nTelefono: {}".format(self.nome,self.cognome,self.telefono)