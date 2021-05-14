from PyQt5.QtGui import QPalette, QBrush, QImage, QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QSizePolicy, QSpacerItem, \
    QDesktopWidget, QHBoxLayout
from PyQt5.QtCore import Qt

from ListaAttrezzatura.vista.VistaListaAttrezzatura import vista_lista_attrezzatura
from ListaPiste.vista.VistaListaPiste import vista_lista_piste
from Sessione.vista.VistaAccountLoggato import vista_account_loggato
from GestioneParcheggi.vista.vista_parcheggio import vista_parcheggio


class vista_home(QWidget):

    def __init__(self):
        super(vista_home, self).__init__()

        # Attributi
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale1 = QHBoxLayout()
        self.layout_orizzontale2 = QHBoxLayout()

        # Sfondo
        self.show_background("SarnanoNeve")

        # Pulsanti
        self.show_pulsantiera()

        # Spaziature
        self.layout_verticale.addLayout(self.layout_orizzontale1)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 10, QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.layout_verticale.addLayout(self.layout_orizzontale2)
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
        pulsante_account = self.crea_bottone("ACCOUNT", self.layout_orizzontale1)
        pulsante_account.clicked.connect(self.call_account_loggato)

        pulsante_lista_piste = self.crea_bottone("LISTA PISTE", self.layout_orizzontale1)
        pulsante_lista_piste.clicked.connect(self.call_lista_piste)

        pulsante_prenota_parcheggio = self.crea_bottone("PRENOTA \n PARCHEGGIO", self.layout_orizzontale1)
        pulsante_prenota_parcheggio.clicked.connect(self.call_prenota_parcheggio)

        self.layout_verticale.addSpacerItem(QSpacerItem(0, 25, QSizePolicy.Fixed, QSizePolicy.Fixed))

        pulsante_noleggia_attrezzatura = self.crea_bottone("NOLEGGIA \n ATTREZZATURA", self.layout_orizzontale2)
        #pulsante_noleggia_attrezzatura.clicked.connect(self.call_noleggia_attrezzatura())
        
        pulsante_skipass = self.crea_bottone("ACQUISTA \n SKIPASS", self.layout_orizzontale2)
        #pulsante_skipass.clicked.connect(self.call_skipass())

        pulsante_esci = self.crea_bottone("ESCI", self.layout_orizzontale2)
        pulsante_esci.clicked.connect(self.uscita)

    def call_lista_piste(self):
        self.vista_lista_piste = vista_lista_piste(self.show)
        self.vista_lista_piste.showFullScreen()
        self.close()

    def call_account_loggato(self):
        self.vista_info_account = vista_account_loggato(self.showFullScreen)
        self.vista_info_account.showFullScreen()
        self.close()

    def call_prenota_parcheggio(self):
        self.vista_prenota_parcheggio = vista_parcheggio(self.showFullScreen)
        self.vista_prenota_parcheggio.showFullScreen()
        self.close()

    def call_noleggia_attrezzatura(self):
        self.vista_lista_attrezzatura = vista_lista_attrezzatura(self.showFullScreen)
        self.vista_lista_attrezzatura.showFullScreen()
        self.close()

    def call_skipass(self):
        pass

    def uscita(self):
        self.close()

    def crea_bottone(self, tipo, layout):
        bottone = QPushButton(tipo)
        bottone.setFixedSize(500,200)
        bottone.setFont(QFont('Times New Roman', 25))
        bottone.setStyleSheet('QPushButton {background-color: transparent; color: orange;}')
        layout.addWidget(bottone)
        return bottone