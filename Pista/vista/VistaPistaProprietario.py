from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont, QBrush, QPalette, QImage
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QListView, QPushButton, \
    QDesktopWidget
from Pista.controller.controller_pista import controller_pista


class vista_pista_proprietario(QWidget):
    def __init__(self, pista, callback):
        super(vista_pista_proprietario, self).__init__()

        # Attributi
        self.callback = callback
        self.controller_pista = controller_pista(pista)
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()

        # Sfondo
        self.show_background("PISTA")
        #Descrizione Pista
        label = QLabel("Nome => {}\n".format(self.controller_pista.get_nome_str()) + "\n"
                        "Difficoltà => {}\n".format(self.controller_pista.get_difficolta()) + "\n"
                        "Stato => {}\n".format(self.controller_pista.get_stato()) + "\n")
        label.setFont(QFont('Times New Roman', 30,100))
        label.setStyleSheet('QLabel{background-color: transparent; color: orange;}')
        self.layout_verticale.addWidget(label)

        #Indietro allineati
        self.show_pulsantiera()

        self.layout_verticale.addSpacerItem(QSpacerItem(0, 350, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Impostazione layout totale
        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Pista')

    def call_vista_pista(self):
        pass

    def indietro(self):
        self.callback()
        self.close()

    def show_background(self, stringa):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("Data/Immagini/5.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60,500))
        titolo.setStyleSheet('QLabel {background-color: transparent; color: white;}')
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale.addWidget(titolo)

    def show_pulsantiera(self):
        # Punsante indietro
        pulsante_indietro = QPushButton("INDIETRO")
        pulsante_indietro.setFont(QFont('Times New Roman', 18,100,True))
        pulsante_indietro.setStyleSheet('background-color: orange')
        pulsante_indietro.setFixedSize(250, 100)
        pulsante_indietro.clicked.connect(self.indietro)
        pulsante_modifica_pista = QPushButton("MODIFICA PISTA")
        pulsante_modifica_pista.setFont(QFont('Times New Roman', 16,100,True))
        pulsante_modifica_pista.setStyleSheet('background-color: orange')
        pulsante_modifica_pista.setFixedSize(250, 100)
        #pulsante_indietro.clicked.connect()
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 80, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale.addSpacerItem(QSpacerItem(500, 0))
        self.layout_orizzontale.addWidget(pulsante_indietro)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(50, 0))
        self.layout_orizzontale.addWidget(pulsante_modifica_pista)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(500, 0))
        self.layout_verticale.addLayout(self.layout_orizzontale)