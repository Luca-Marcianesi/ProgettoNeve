from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QDesktopWidget, QSpacerItem, \
    QSizePolicy
from PyQt5.QtCore import Qt
from Sessione.controller.controller_sessione import controller_sessione
from Sessione.vista.VistaModificaAccount import vista_modifica_account
from Sessione.vista.VistaPrenotazioneAccount import vista_prenotazione_account


class vista_account_loggato(QWidget):

    def __init__(self, callback):
        super(vista_account_loggato, self).__init__()
        self.callback = callback


        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        self.controller = controller_sessione()
        self.v1_layout = QVBoxLayout()
        self.v2_layout = QVBoxLayout()
        self.v3_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        back_img = QImage("ListaAccount/data/im.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel("INFORMAZIONI ACCOUNT")
        titolo.setAlignment(Qt.AlignCenter)
        self.cambia_font(60, titolo)
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.v1_layout.addWidget(titolo)
        self.v1_layout.addSpacerItem(QSpacerItem(0, 80, QSizePolicy.Fixed, QSizePolicy.Fixed))

        #label
        label = QLabel( "Nome: {}".format(self.controller.get_nome_str()) + "\n"
                        "Cognome: {}".format(self.controller.get_cognome_str()) + "\n"
                        "Età: {}".format(self.controller.get_eta_str()) + "\n"
                        "Altezza: {}".format(self.controller.get_altezza_str()) + "\n"
                        "Numero di scarpe: {}".format(self.controller.get_numero_scarpe_str())
                       )
        #label.setStyleSheet("background-color:white")
        self.v3_layout.addSpacerItem(QSpacerItem(500, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.v3_layout.addWidget(self.cambia_font(30, label))
        self.v3_layout.addSpacerItem(QSpacerItem(500, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.h_layout.addLayout(self.v3_layout)

        self.h_layout.addSpacerItem(QSpacerItem(700, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        cambia_credenziali = QPushButton("CAMBIA\nCREDENZIALI")
        self.cambia_font(30, cambia_credenziali)
        cambia_credenziali.setFixedSize(400,150)
        cambia_credenziali.clicked.connect(self.vista_credenziali)
        self.v2_layout.addWidget(cambia_credenziali)

        prenotazioni = QPushButton("PRENOTAZIONI")
        self.cambia_font(30, prenotazioni)
        prenotazioni.setFixedSize(400,150)
        prenotazioni.clicked.connect(self.vista_prenotazioni)
        self.v2_layout.addWidget(prenotazioni)

        indietro = QPushButton("INDIETRO")
        self.cambia_font(30, indietro)
        indietro.setFixedSize(400, 150)
        indietro.clicked.connect(self.indietro)
        self.v2_layout.addWidget(indietro)

        self.h_layout.addLayout(self.v2_layout)
        self.h_layout.addSpacerItem(QSpacerItem(150, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.v1_layout.addLayout(self.h_layout)
        self.v1_layout.addSpacerItem(QSpacerItem(0, 200, QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.setLayout(self.v1_layout)

    def indietro(self):
        self.callback()
        self.close()

    def cambia_font(self, numero, label):
        label.setFont(QFont('Times New Roman',numero))
        return label

    def vista_credenziali(self):
        self.modifica_credenziali = vista_modifica_account(self.show)
        self.modifica_credenziali.showFullScreen()
        self.close()

    def vista_prenotazioni(self):
        self.vista_prenotazione = vista_prenotazione_account(self.show)
        self.vista_prenotazione.showFullScreen()
        self.close()