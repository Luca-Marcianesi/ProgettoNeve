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
        self.layout_verticale1 = QVBoxLayout()
        self.layout_verticale2 = QVBoxLayout()
        self.layout_orizzontale1 = QHBoxLayout()

        # Sfondo
        self.show_background("Prenota Skipass")

        self.layout_verticale1.addWidget(self.show_pulsante("Mattiniero", self.call_skipass1))
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50))
        self.layout_verticale1.addWidget(self.show_pulsante("Pomeridiano", self.call_skipass2))
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50))
        self.layout_verticale1.addWidget(self.show_pulsante("Giornaliero", self.call_skipass3))

        self.layout_verticale2.addWidget(self.show_pulsante("Settimanale", self.call_skipass4))
        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 50))
        self.layout_verticale2.addWidget(self.show_pulsante("Mensile", self.call_skipass5))
        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 50))
        self.layout_verticale2.addWidget(self.show_pulsante("Stagionale", self.call_skipass6))

        self.layout_orizzontale.addSpacerItem(QSpacerItem(40, 0))
        self.layout_orizzontale.addLayout(self.layout_verticale1)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(300, 0))
        self.layout_orizzontale.addLayout(self.layout_verticale2)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(40, 0))
        self.layout_verticale.addLayout(self.layout_orizzontale)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50))
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(20, 0))
        self.layout_orizzontale1.addWidget(self.show_pulsante("Indietro", self.indietro))
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50))
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(20, 0))


        # Pulsanti
        #self.show_pulsante()

        # Spaziature
        self.layout_verticale.addLayout(self.layout_orizzontale)
        self.layout_verticale.addLayout(self.layout_verticale1)
        self.layout_verticale.addLayout(self.layout_orizzontale1)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 200, QSizePolicy.Expanding, QSizePolicy.Expanding))

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


    def show_pulsante(self, titolo, call):
        pulsante_skipass = self.crea_bottone(titolo)
        pulsante_skipass.clicked.connect(call)
        return pulsante_skipass
        #pulsante_esci = self.crea_bottone("Indietro")
        #pulsante_esci.clicked.connect(self.uscita)

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

    def crea_bottone(self, tipo):
        bottone = QPushButton(tipo)
        bottone.setFixedSize(350, 100)
        bottone.setFont(QFont('Times New Roman', 25))
        #layout.addWidget(bottone)
        return bottone

    def indietro(self):
        self.callback()
        self.close()