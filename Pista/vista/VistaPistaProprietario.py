from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QBrush, QPalette, QImage
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, \
    QDesktopWidget
from Pista.controller.controllerpista import ControllerPista


class VistaPistaProprietario(QWidget):

    def __init__(self, pista, callback, salva_lista_piste, aggiorna_lista):
        super(VistaPistaProprietario, self).__init__()

        # Attributi
        self.callback = callback
        self.aggiona_lista = aggiorna_lista
        self.controller_pista = ControllerPista(pista)
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.salva_lista_piste = salva_lista_piste

        # Sfondo
        self.show_background("PISTA")
        # Descrizione Pista
        label = QLabel("Nome => {}\n".format(self.controller_pista.get_nome_str()) + "\n"
                        "Difficoltà => {}\n".format(self.controller_pista.get_difficolta()) + "\n"
                        "Stato => {}\n".format(self.controller_pista.get_stato()) + "\n")
        label.setFont(QFont('Times New Roman', 30, 100))
        label.setStyleSheet('QLabel{background-color: transparent; color: orange;}')
        self.layout_verticale.addWidget(label)

        # Indietro allineati
        self.show_pulsantiera()

        self.layout_verticale.addSpacerItem(QSpacerItem(0, 350, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Impostazione layout totale
        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Pista')

    def show_background(self, stringa):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("Data/Immagini/VistaPrenotazioneAccount.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60, 500))
        titolo.setStyleSheet('QLabel {background-color: transparent; color: white;}')
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale.addWidget(titolo)

    def show_pulsantiera(self):
        # Punsante indietro
        pulsante_indietro = QPushButton("INDIETRO")
        pulsante_indietro.setFont(QFont('Times New Roman', 18, 100, True))
        pulsante_indietro.setStyleSheet('background-color: orange')
        pulsante_indietro.setFixedSize(250, 100)
        pulsante_indietro.clicked.connect(self.indietro)
        pulsante_modifica_pista = QPushButton("MODIFICA\n"
                                              "PISTA")
        pulsante_modifica_pista.setFont(QFont('Times New Roman', 18, 100, True))
        pulsante_modifica_pista.setStyleSheet('background-color: orange')
        pulsante_modifica_pista.setFixedSize(250, 100)
        pulsante_modifica_pista.clicked.connect(self.call_modifica)


        self.layout_verticale.addSpacerItem(QSpacerItem(0, 80, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale.addSpacerItem(QSpacerItem(500, 0))
        self.layout_orizzontale.addWidget(pulsante_indietro)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(50, 0))
        self.layout_orizzontale.addWidget(pulsante_modifica_pista)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(500, 0))
        self.layout_verticale.addLayout(self.layout_orizzontale)

    def call_modifica(self):
        self.vista_cambia_stato = VistaCambiaStato(self.controller_pista, self.salva_lista_piste, self.showFullScreen,
                                                   self.aggiona_lista)
        self.vista_cambia_stato.show()

    def indietro(self):
        self.callback()
        self.close()


class VistaCambiaStato(QWidget):

    def __init__(self, controller_pista, salva_lista_piste, callback, aggiorna_lista):
        super(VistaCambiaStato, self).__init__()

        self.callback = callback
        self.aggiorna_lista = aggiorna_lista
        self.salva_lista_piste = salva_lista_piste
        self.controller_pista = controller_pista
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.setFixedWidth(600)
        self.setFixedHeight(500)

        self.show_background()

        label = QLabel("Seleziona stato della pista:")
        label.setFont(QFont('Times New Roman', 25, 100))
        label.setSizePolicy(500, 200)
        label.setStyleSheet('QLabel{background-color: orange; color: black;}')
        self.layout_verticale.addWidget(label)

        bottone_chiusa = QPushButton("Chiusa")
        bottone_chiusa.setStyleSheet('QPushButton{background-color: orange; color: black;}')
        bottone_chiusa.clicked.connect(partial(self.call_modifica_stato, "Chiusa"))

        bottone_aperta = QPushButton("Aperta")
        bottone_aperta.setStyleSheet('QPushButton{background-color: orange; color: black;}')
        bottone_aperta.clicked.connect(partial(self.call_modifica_stato, "Aperta"))

        bottone_prenotata = QPushButton("Prenotata")
        bottone_prenotata.setStyleSheet('QPushButton{background-color: orange; color: black;}')
        bottone_prenotata.clicked.connect(partial(self.call_modifica_stato, "Prenotata"))

        self.layout_orizzontale.addWidget(bottone_chiusa)
        self.layout_orizzontale.addWidget(bottone_aperta)
        self.layout_orizzontale.addWidget(bottone_prenotata)
        self.layout_verticale.addLayout(self.layout_orizzontale)

        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Stato')

    def call_modifica_stato(self, stato):
        self.controller_pista.modifica_stato_pista(stato)
        self.salva_lista_piste()
        self.aggiorna_lista()
        self.callback()
        self.close()

    def show_background(self):
        # Sfondo
        back_img = QImage("Pista/data/ModificaPista.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)
