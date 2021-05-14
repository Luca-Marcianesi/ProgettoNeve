from PyQt5.QtGui import QPalette, QBrush, QImage, QFont, QPixmap
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

        self.sfondo = QLabel('')
        self.sfondo.setStyleSheet('QLabel {background-color: darkCyan}')
        pixmap = QPixmap("ListaAccount/data/2.png")
        self.sfondo.setPixmap(pixmap)
        self.layout_orizzontale1.addWidget(self.sfondo)
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(375,0,QSizePolicy.Fixed, QSizePolicy.Fixed))
        # Sfondo
        self.show_background()

        # Pulsanti


        # Spaziature
        self.layout_verticale.addLayout(self.layout_orizzontale1)


        self.show_pulsantiera()

        # Impostazione layout totale
        self.setLayout(self.layout_verticale)

    def show_background(self):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("ListaAccount/data/im.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo





    def show_pulsantiera(self):
        pulsante_account = self.crea_bottone("ACCOUNT", self.layout_orizzontale1)
        pulsante_account.clicked.connect(self.call_account_loggato)

        pulsante_esci = self.crea_bottone("ESCI", self.layout_orizzontale1)
        pulsante_esci.clicked.connect(self.uscita)

        pulsante_skipass = self.crea_bottone("ACQUISTA \n SKIPASS", self.layout_verticale)
        # pulsante_skipass.clicked.connect(self.call_skipass())

        pulsante_lista_piste = self.crea_bottone("LISTA PISTE", self.layout_verticale)
        pulsante_lista_piste.clicked.connect(self.call_lista_piste)

        pulsante_noleggia_attrezzatura = self.crea_bottone("NOLEGGIA \n ATTREZZATURA", self.layout_verticale)
        # pulsante_noleggia_attrezzatura.clicked.connect(self.call_noleggia_attrezzatura())

        pulsante_prenota_parcheggio = self.crea_bottone("PRENOTA \n PARCHEGGIO", self.layout_verticale)
        pulsante_prenota_parcheggio.clicked.connect(self.call_prenota_parcheggio)


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
        bottone.setFixedSize(300,100)
        bottone.setFont(QFont('Times New Roman', 20,100,True))
        bottone.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        layout.addWidget(bottone)
        return bottone