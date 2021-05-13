from PyQt5.QtGui import QPalette, QBrush, QImage, QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QSizePolicy, QSpacerItem, \
    QDesktopWidget, QHBoxLayout
from PyQt5.QtCore import Qt

class vista_acquista_skipass(QWidget):

    def __init__(self):
        super(vista_acquista_skipass, self).__init__()

        # Attributi
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.layout_verticale1 = QHBoxLayout()
        self.layout_verticale2 = QVBoxLayout()

        # Sfondo
        self.show_background("Prenota Skipass")

        # Pulsanti
        self.show_pulsantiera()

        # Spaziature
        self.layout_verticale.addLayout(self.layout_orizzontale)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 10, QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.layout_verticale.addLayout(self.layout_verticale1)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 5, QSizePolicy.Expanding, QSizePolicy.Expanding))

        # Impostazione layout totale
        self.setLayout(self.layout_verticale)

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
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale.addWidget(titolo)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))

    def show_pulsantiera(self):
        pulsante_skipass1 = self.crea_bottone("Skipass Mattiniero", self.layout_orizzontale)
        pulsante_skipass1.clicked.connect(self.call_skipass1)


        pulsante_skipass2 = self.crea_bottone("Skipass Pomeridiano", self.layout_orizzontale)
        pulsante_skipass2.clicked.connect(self.call_skipass2)

        pulsante_skipass3 = self.crea_bottone("Skipass Giornaliero", self.layout_orizzontale)
        pulsante_skipass3.clicked.connect(self.call_skipass3)

        self.layout_verticale.addSpacerItem(QSpacerItem(0, 25, QSizePolicy.Fixed, QSizePolicy.Fixed))

        pulsante_skipass4 = self.crea_bottone("Skipass Settimanale", self.layout_verticale1)
        pulsante_skipass4.clicked.connect(self.call_skipass4)

        pulsante_skipass5 = self.crea_bottone("Skipass Mensile", self.layout_verticale1)
        pulsante_skipass5.clicked.connect(self.call_skipass5)

        pulsante_skipass6 = self.crea_bottone("Skipass Stagionale", self.layout_verticale1)
        pulsante_skipass6.clicked.connect(self.call_skipass6)

        pulsante_esci = self.crea_bottone("Indietro", self.layout_verticale1)
        pulsante_esci.clicked.connect(self.uscita)

    def call_skipass1(self):
        self.controller_gestione_skipass.prenota_skipass(self)
        self.close()

    def call_skipass2(self):
        self.controller_gestione_skipass.prenota_skipass(self)
        self.close()

    def call_skipass3(self):
        self.controller_gestione_skipass.prenota_skipass(self)
        self.close()

    def call_skipass4(self):
        self.controller_gestione_skipass.prenota_skipass(self)
        self.close()

    def call_skipass5(self):
        self.controller_gestione_skipass.prenota_skipass(self)
        self.close()

    def call_skipass6(self):
        self.controller_gestione_skipass.prenota_skipass(self)
        self.close()

    def uscita(self):
        self.close()

    def crea_bottone(self, tipo, layout):
        bottone = QPushButton(tipo)
        bottone.setFixedSize(500, 200)
        bottone.setFont(QFont('Times New Roman', 25))
        layout.addWidget(bottone)
        return bottone

    def indietro(self):
        self.callback()
        self.close()