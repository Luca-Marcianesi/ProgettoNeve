from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont, QBrush, QPalette, QImage
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QListView, QPushButton, \
    QDesktopWidget
from Pista.controller.controllerpista import ControllerPista

# Vista pista
class vista_pista(QWidget):
    def __init__(self, pista, callback):
        super(vista_pista, self).__init__()

        # Attributi
        self.callback = callback
        self.controller_pista = ControllerPista(pista)
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.layout_orizzontale2 = QHBoxLayout()
        self.setFixedSize(1000,700)

        # Sfondo
        self.show_background("PISTA")

        #Descrizione Pista
        label = QLabel("Nome => {}\n".format(self.controller_pista.get_nome_str()) + "\n"
                        "Difficoltà => {}\n".format(self.controller_pista.get_difficolta()) + "\n"
                        "Stato => {}\n".format(self.controller_pista.get_stato()) + "\n")
        label.setFont(QFont('Times New Roman', 30,100))
        label.setStyleSheet('QLabel{background-color: transparent; color: black;}')
        self.layout_orizzontale.addSpacerItem(QSpacerItem(200, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale.addWidget(label)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(200, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.layout_verticale.addLayout(self.layout_orizzontale)


        self.layout_verticale.addLayout(self.layout_orizzontale2)

        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        # Impostazione layout totale
        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Pista')

    # ???
    def call_vista_pista(self):
        pass

    # Metodo che, collegato al pulsante "INDIETRO"
    def indietro(self):
        self.callback()
        self.close()

    def show_background(self, stringa):
        # Sfondo
        back_img = QImage("Data/Immagini/6.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 40,100))
        titolo.setStyleSheet('QLabel {background-color: transparent; color: orange;}')
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 20, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale.addWidget(titolo)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))