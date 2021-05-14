
from PyQt5.QtGui import QFont, QBrush, QPalette, QImage
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, \
    QDesktopWidget, QGridLayout, QLabel
from PyQt5.QtCore import Qt


class vista_skipass(QWidget):
    def __init__(self, skipass):
        super(vista_skipass, self).__init__()

        # Attributi
        #self.callback = callback
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.skipass = skipass

        # Sfondo
        self.show_background("Prenota" + "\n"
                             "Skipass")

        # Descrizione Skipass
        label = QLabel("Tipologia => {}\n".format(self.skipass.get_tipo()) + "\n"
                       "Descrizione => {}\n".format(self.skipass.get_descrizione()) + "\n"
                       "Durata dello skipass => {}\n".format(self.skipass.get_durata()) + "\n")
        label.setFont(QFont('Times New Roman', 30))
        self.layout_verticale.addWidget(label)

        # Pulsante
        self.pulsante_prenota = self.crea_bottone("Prenota", self.layout_orizzontale)
        #self.pulsante_prenota.clicked.connect(self.call_prenota_parcheggio)

        self.layout_orizzontale.addSpacerItem(QSpacerItem(50, 0))

        self.pulsante_indietro = self.crea_bottone("Indietro", self.layout_orizzontale)
        # self.pulsante_prenota.clicked.connect(self.call_prenota_parcheggio)

        self.layout_orizzontale.addSpacerItem(QSpacerItem(1300, 0))

        self.layout_verticale.addLayout(self.layout_orizzontale)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 100))

        # Impostazione layout totale
        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Skipass')


    def show_background(self, titolo):
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("GestioneSkipass/data/vista_skipass.webp")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)
        titolo = QLabel(titolo)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale.addWidget(titolo)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))

    """
    def show_pulsante_indietro(self):
        # Punsante indietro
        pulsante_indietro = QPushButton()
        #pulsante_indietro.setStyleSheet("background-image:url(Attrezzatura/data/arrow.jpg)")
        pulsante_indietro.setFont(QFont('Times New Roman', 18))
        pulsante_indietro.setFixedSize(100, 100)
        pulsante_indietro.clicked.connect(self.indietro)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(5, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale.addWidget(pulsante_indietro)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(5000, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addLayout(self.layout_orizzontale)
    """

    def indietro(self):
        self.callback()
        self.close()

    def crea_bottone(self, tipo, layout):
        bottone = QPushButton(tipo)
        bottone.setFixedSize(300, 100)
        bottone.setFont(QFont('Times New Roman', 20, 100, True))
        bottone.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        layout.addWidget(bottone)
        return bottone