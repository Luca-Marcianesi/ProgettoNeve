from PyQt5.QtGui import QFont, QImage, QPalette, QBrush
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QWidget, QHBoxLayout, QSizePolicy, \
    QSpacerItem, QDesktopWidget
from PyQt5.QtCore import Qt

from Sessione.controller.controller_sessione import controller_sessione


class vista_modifica_account(QWidget):

    def __init__(self, callback):
        super(vista_modifica_account, self).__init__()
        self.callback = callback
        self.controller = controller_sessione()
        self.testo = {}
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        self.controller = controller_sessione()
        self.v1_layout = QVBoxLayout()
        self.v2_layout = QVBoxLayout()
        self.h1_layout = QHBoxLayout()
        self.h2_layout = QHBoxLayout()
        back_img = QImage("ListaAccount/data/im.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel("MODIFICA LE CREDENZIALI")
        titolo.setAlignment(Qt.AlignCenter)
        self.cambia_font(60, titolo)
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.v1_layout.addWidget(titolo)

        self.v1_layout.addSpacerItem(QSpacerItem(0, 80, QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.h2_layout.addSpacerItem(QSpacerItem(700, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.casella_testo("PASSWORD")
        self.casella_testo("ETÀ")
        self.casella_testo("ALTEZZA")
        self.casella_testo("NUMERO DI SCARPE")

        self.h2_layout.addLayout(self.v2_layout)
        self.h2_layout.addSpacerItem(QSpacerItem(700, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        indietro = QPushButton("INDIETRO")
        indietro.setFont(QFont('Times New Roman', 17))
        indietro.setFixedSize(200, 70)
        indietro.clicked.connect(self.indietro)
        self.h1_layout.addWidget(indietro)

        invio = QPushButton("INVIA")
        invio.setFont(QFont('Times New Roman', 17))
        invio.setFixedSize(200, 70)
        invio.clicked.connect(self.cambia_dati)
        self.h1_layout.addWidget(invio)

        self.v2_layout.addLayout(self.h1_layout)
        self.v1_layout.addLayout(self.h2_layout)

        self.v1_layout.addSpacerItem(QSpacerItem(0, 100, QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.setLayout(self.v1_layout)
        self.setWindowTitle("Cambia Credenziali")

    def casella_testo(self, tipo):
        label = QLabel(tipo + ":")
        self.cambia_font(30, label)
        self.v2_layout.addWidget(label)
        casella = QLineEdit()
        font = casella.font()
        font.setPointSize(15)
        casella.setFont(font)
        casella.setAlignment(Qt.AlignCenter)
        self.v2_layout.addWidget(casella)
        self.testo[tipo] = casella

    def cambia_dati(self):
        password = self.testo["PASSWORD"].text()
        eta = self.testo["ETÀ"].text()
        altezza = self.testo["ALTEZZA"].text()
        numero_scarpe = self.testo["NUMERO DI SCARPE"].text()

        if password != "" and eta != "" and altezza != "" and numero_scarpe != "":
            self.controller.cambia_password(password)
            self.controller.cambia_eta(eta)
            self.controller.cambia_altezza(altezza)
            self.controller.cambia_numero_scarpe(numero_scarpe)
            #self.controller.salva_dati()
            self.callback()
            self.close()
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                 QMessageBox.Ok, QMessageBox.Ok)

    def indietro(self):
        self.callback()
        self.close()

    def cambia_font(self, numero, label):
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont('Times New Roman', numero))
        return label