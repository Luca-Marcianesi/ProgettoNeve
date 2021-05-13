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

        # Attributi
        self.label = QLabel()
        self.callback = callback
        self.controller = controller_sessione()
        self.layout_verticale1 = QVBoxLayout()
        self.layout_verticale2 = QVBoxLayout()
        self.layout_verticale3 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()

        # Sfondo
        self.show_background("INFORMAZIONI ACCOUNT")

        # Spaziatura
        self.layout_verticale3.addSpacerItem(QSpacerItem(500, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.aggiorna()

        self.layout_verticale3.addWidget(self.label)

        # Spaziatura
        self.layout_verticale3.addSpacerItem(QSpacerItem(500, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale.addLayout(self.layout_verticale3)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(700, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Pulsanti cambia credenziali, prenotazioni e indietro + allineamento
        self.show_pulsantiera()

        # Spaziatura
        self.layout_orizzontale.addSpacerItem(QSpacerItem(150, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addLayout(self.layout_orizzontale)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 200, QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.setLayout(self.layout_verticale1)

    def show_pulsantiera(self):
        pulsante_credenziali = QPushButton("CAMBIA\nCREDENZIALI")
        pulsante_credenziali.setFont(QFont('Times New Roman', 30))
        pulsante_credenziali.setFixedSize(400, 150)
        pulsante_credenziali.clicked.connect(self.call_modifica_credenziali)
        self.layout_verticale2.addWidget(pulsante_credenziali)

        pulsante_prenotazioni = QPushButton("PRENOTAZIONI")
        pulsante_prenotazioni.setFont(QFont('Times New Roman', 30))
        pulsante_prenotazioni.setFixedSize(400, 150)
        pulsante_prenotazioni.clicked.connect(self.vista_prenotazioni)
        self.layout_verticale2.addWidget(pulsante_prenotazioni)

        pulsante_indietro = QPushButton("INDIETRO")
        pulsante_indietro.setFont(QFont('Times New Roman', 30))
        pulsante_indietro.setFixedSize(400, 150)
        pulsante_indietro.clicked.connect(self.indietro)
        self.layout_verticale2.addWidget(pulsante_indietro)
        self.layout_orizzontale.addLayout(self.layout_verticale2)

    def indietro(self):
        self.callback()
        self.close()

    def call_modifica_credenziali(self):
        self.vista_modifica_credenziali = vista_modifica_account(self.aggiorna, self.showFullScreen)
        self.vista_modifica_credenziali.showFullScreen()
        self.close()

    def vista_prenotazioni(self):
        self.vista_prenotazione_account = vista_prenotazione_account(self.showFullScreen)
        self.vista_prenotazione_account.showFullScreen()
        self.close()

    def show_background(self, stringa):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("ListaAccount/data/im.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addWidget(titolo)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))

    def aggiorna(self):
        # Label
        self.label = QLabel("Nome: {}".format(self.controller.get_nome_str()) + "\n"
                            "Cognome: {}".format(self.controller.get_cognome_str()) + "\n"
                            "Età: {}".format(self.controller.get_eta_str()) + "\n"
                            "Altezza: {}".format(self.controller.get_altezza_str()) + "\n"
                            "Numero di scarpe: {}".format(self.controller.get_numero_scarpe_str()))
        self.label.setFont(QFont('Times New Roman', 30))
