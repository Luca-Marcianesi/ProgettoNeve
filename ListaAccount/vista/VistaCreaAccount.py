from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QWidget, QHBoxLayout, \
    QDesktopWidget


class vista_crea_account(QWidget):

    def __init__(self, callback, controller):
        super(vista_crea_account, self).__init__()
        self.callback = callback
        self.controller = controller
        self.testo = {}
        self.setFixedWidth(800)
        self.setFixedHeight(600)
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()

        self.show_background()

        self.casella_testo("Nome")
        self.casella_testo("Cognome")
        self.casella_testo("Username")
        self.casella_testo("Password")
        self.casella_testo("Età")
        self.casella_testo("Altezza")
        self.casella_testo("Numero di scarpe")

        indietro = QPushButton("Indietro")
        indietro.clicked.connect(self.indietro)
        self.h_layout.addWidget(indietro)

        invio = QPushButton("Invia")
        invio.clicked.connect(self.crea_account)
        self.h_layout.addWidget(invio)


        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Account")

    def casella_testo(self, tipo):
        label = QLabel(tipo + ":")
        font = label.font()
        font.setPointSize(14)
        label.setFont(font)
        self.v_layout.addWidget(label)
        casella = QLineEdit()
        self.v_layout.addWidget(casella)
        self.testo[tipo] = casella

    def crea_account(self):
        nome = self.testo["Nome"].text()
        cognome = self.testo["Cognome"].text()
        username = self.testo["Username"].text()
        password = self.testo["Password"].text()
        eta = self.testo["Età"].text()
        altezza = self.testo["Altezza"].text()
        n_scarpe = self.testo["Numero di scarpe"].text()

        if nome != "" and cognome != "" and username != "" and password != "" and eta != "" and altezza != "" and n_scarpe != "":
            self.controller.crea_account(nome, cognome, username, password, eta, altezza, n_scarpe)
            self.controller.salva_dati()
            self.callback()
            self.close()
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)

    def indietro(self):
        self.callback()
        self.close()

    def show_background(self):
        # Sfondo
        back_img = QImage("Data/Immagini/azzurro.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)