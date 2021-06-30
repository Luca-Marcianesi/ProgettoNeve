from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QBrush, QPalette, QImage
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy
from Pista.controller.controllerpista import ControllerPista


# Vista che descrive la pista selezionata
class VistaPista(QWidget):
    def __init__(self, pista, callback):
        super(VistaPista, self).__init__()

        # Funzione che richiama la vista precedente
        self.callback = callback
        # Controller relativo alla vista
        self.controller_pista = ControllerPista(pista)
        # Layout utilizzati dalla vista per l'allineamento dei widget
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.layout_orizzontale2 = QHBoxLayout()
        # Settaggio della dimensione della finestra
        self.setFixedSize(1000, 700)

        # Funzione standard per l'impostazione dello sfondo e il titolo alla vista
        self.show_background("PISTA")

        # Descrizione della pista
        label = QLabel("Nome => {}\n".format(self.controller_pista.get_nome_str()) + "\n"
                       "Difficoltà => {}\n".format(self.controller_pista.get_difficolta()) + "\n"
                       "Stato => {}\n".format(self.controller_pista.get_stato()) + "\n")
        label.setFont(QFont('Times New Roman', 30, 100))
        label.setStyleSheet('QLabel{background-color: transparent; color: black;}')
        self.layout_orizzontale.addSpacerItem(QSpacerItem(200, 0))
        self.layout_orizzontale.addWidget(label)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(200, 0))

        self.layout_verticale.addLayout(self.layout_orizzontale)

        self.layout_verticale.addLayout(self.layout_orizzontale2)

        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50))
        # Impostazione layout totale
        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Pista')

    # Metodo che, collegato al pulsante "INDIETRO"
    def indietro(self):
        self.callback()
        self.close()

    # Funzione interna alla vista per il settaggio dello sfondo e del titolo
    def show_background(self, stringa):
        # Sfondo
        back_img = QImage("Data/Immagini/VistaPista.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 40, 100))
        titolo.setStyleSheet('QLabel {background-color: transparent; color: orange;}')
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 20))
        self.layout_verticale.addWidget(titolo)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50))
