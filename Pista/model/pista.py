
# Classe pista
class Pista:
    def __init__(self, nome, difficolta, stato):

        # Definizione degli attributi
        self.nome = nome
        self.difficolta = difficolta
        self.stato = stato

    # Metodo per settare lo stato di una pista
    def set_stato(self, stato):
        self.stato = stato

    # Metodo che restituisce il nome di una pista
    def get_nome_str(self):
        return self.nome

    # Metodo che restituisce lo stato di una pista
    def get_stato(self):
        return self.stato

    # Metodo che restituisce la difficoltà di una pista
    def get_difficolta(self):
        return self.difficolta
