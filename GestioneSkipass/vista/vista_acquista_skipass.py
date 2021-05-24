from functools import partial

from PyQt5.QtGui import QPalette, QBrush, QImage, QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QSizePolicy, QSpacerItem, \
    QDesktopWidget, QHBoxLayout
from PyQt5.QtCore import Qt
from Skipass.vista.VistaSkipass import vista_skipass
from GestioneSkipass.controller.controller_gestione_skipass import controller_gestione_skipass

# Vista acquista skipass
class vista_acquista_skipass(QWidget):

    def __init__(self, callback):
        super(vista_acquista_skipass, self).__init__()

        # Controller
        self.controller_gestione_skipass = controller_gestione_skipass()


        # Attributi
        self.callback = callback
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.layout_verticale1 = QVBoxLayout()
        self.layout_verticale2 = QVBoxLayout()
        self.layout_orizzontale1 = QHBoxLayout()

        # Sfondo
        self.show_background("PRENOTA SKIPASS")

        # Settaggio layout e creazione dei vari skipass
        self.layout_verticale1.addWidget(self.show_pulsante("Mattiniero", self.controller_gestione_skipass.get_skipass_n(0)))
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50))
        self.layout_verticale1.addWidget(self.show_pulsante("Pomeridiano", self.controller_gestione_skipass.get_skipass_n(1)))
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50))

        self.layout_verticale1.addWidget(self.show_pulsante("Giornaliero", self.controller_gestione_skipass.get_skipass_n(2)))



        self.layout_verticale2.addWidget(self.show_pulsante("Settimanale", self.controller_gestione_skipass.get_skipass_n(3)))
        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 50))

        self.layout_verticale2.addWidget(self.show_pulsante("Mensile", self.controller_gestione_skipass.get_skipass_n(4)))
        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 50))

        self.layout_verticale2.addWidget(self.show_pulsante("Stagionale", self.controller_gestione_skipass.get_skipass_n(5)))

        # Spaziature e settaggio layout
        self.layout_orizzontale.addSpacerItem(QSpacerItem(40, 0))
        self.layout_orizzontale.addLayout(self.layout_verticale1)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(300, 0))
        self.layout_orizzontale.addLayout(self.layout_verticale2)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(40, 0))
        self.layout_verticale.addLayout(self.layout_orizzontale)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50))
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(20, 0))
        self.layout_orizzontale1.addWidget(self.show_pulsante_indietro("Indietro", self.indietro))
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50))
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(20, 0))

        # Spaziature
        self.layout_verticale.addLayout(self.layout_orizzontale)
        self.layout_verticale.addLayout(self.layout_verticale1)
        self.layout_verticale.addLayout(self.layout_orizzontale1)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 200, QSizePolicy.Expanding, QSizePolicy.Expanding))

        # Impostazione layout totale
        self.setLayout(self.layout_verticale)


    def show_pulsante_indietro(self,titolo,call):
        pulsante_esci = self.crea_bottone(titolo)
        pulsante_esci.clicked.connect(call)
        return pulsante_esci

    def show_background(self, stringa):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("GestioneSkipass/data/1.jpg")
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

    # Metodo per mostrare il pulsante associato ad ogni skipass
    def show_pulsante(self, titolo, skipass):
        pulsante_skipass = self.crea_bottone(titolo)
        pulsante_skipass.clicked.connect(partial(self.call_skipass, skipass))
        return pulsante_skipass

    # Metodo per richiamare la vista skipass
    def call_skipass(self,skipass):
        self.vista_skipass = vista_skipass(skipass, self.showFullScreen, self.controller_gestione_skipass)
        self.vista_skipass.showFullScreen()
        self.close()

    # Metodo per creare un bottone
    def crea_bottone(self, tipo):
        bottone = QPushButton(tipo)
        bottone.setFixedSize(350, 100)
        bottone.setFont(QFont('Times New Roman', 20, 100, True))
        bottone.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        return bottone

    # Metodo che permette, cliccando il bottone "indietro", di tornare alla vista precedente
    def indietro(self):
        self.callback()
        self.close()