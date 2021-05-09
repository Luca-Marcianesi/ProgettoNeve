class pista:
    def __init__(self, nome, difficolta, stato):
        self.nome = nome
        self.difficolta = difficolta
        self.stato = stato

    def set_stato(self, stato):
        self.stato = stato

    def get_pista_str(self):
        return "Nome: {}".format(self.nome) + "\n" \
                "Difficoltà: {}".format(self.difficolta) + "\n"\
                "Stato: {}".format(self.stato) + "\n"


    def get_nome_str(self):
        return self.nome

    def get_stato(self):
        return self.stato

    def get_difficolta(self):
        return self.difficolta