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