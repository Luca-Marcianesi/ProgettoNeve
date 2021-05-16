from PyQt5.QtGui import QPalette, QBrush, QImage, QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QSizePolicy, QSpacerItem, \
    QDesktopWidget, QHBoxLayout

from ListaAttrezzatura.vista.VistaListaAttrezzatura import vista_lista_attrezzatura
from ListaPiste.vista.VistaListaPiste import vista_lista_piste
from Sessione.vista.VistaAccountLoggato import vista_account_loggato


class vista_home_proprietario(QWidget):

    def __init__(self):
        super(vista_home_proprietario, self).__init__()

        # Attributi
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale1 = QHBoxLayout()
        self.layout_orizzontale2 = QHBoxLayout()
        self.layout_orizzontale3 = QHBoxLayout()

        self.sfondo = QLabel('')
        self.sfondo.setStyleSheet('QLabel {background-color: darkCyan}')
        pixmap = QPixmap("ListaAccount/data/2.png")
        self.sfondo.setPixmap(pixmap)
        self.layout_orizzontale1.addWidget(self.sfondo)
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(300,0,QSizePolicy.Fixed, QSizePolicy.Fixed))
        # Sfondo
        self.show_background()

        # Pulsanti


        # Spaziature
        self.layout_verticale.addLayout(self.layout_orizzontale1)

        self.layout_verticale.addLayout(self.layout_orizzontale2)

        self.layout_verticale.addLayout(self.layout_orizzontale3)

        self.show_pulsantiera()
        # Impostazione layout totale
        self.setLayout(self.layout_verticale)

    def show_background(self):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("Data/Immagini/2.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

    def show_pulsantiera(self):
        pulsante_account = self.crea_bottone("ACCOUNT", self.layout_orizzontale1)
        #pulsante_account.clicked.connect(self.call_account_loggato)

        self.layout_orizzontale1.addSpacerItem(QSpacerItem(50,0))


        pulsante_esci = self.crea_bottone("ESCI", self.layout_orizzontale1)
        pulsante_esci.clicked.connect(self.uscita)

        pulsante_skipass = self.crea_bottone("ELENCO \nDIPENDENTI", self.layout_orizzontale2)
        #pulsante_skipass.clicked.connect(self.call_skipass)

        self.layout_orizzontale2.addSpacerItem(QSpacerItem(100, 0))

        pulsante_lista_piste = self.crea_bottone("LISTA PISTE", self.layout_orizzontale2)
        #pulsante_lista_piste.clicked.connect(self.call_lista_piste)

        pulsante_noleggia_attrezzatura = self.crea_bottone("MODIFICA \n ATTREZZATURA", self.layout_orizzontale3)
        # pulsante_noleggia_attrezzatura.clicked.connect(self.call_noleggia_attrezzatura())

        self.layout_orizzontale3.addSpacerItem(QSpacerItem(100, 0))

        pulsante_prenota_parcheggio = self.crea_bottone("MANUTENZIONI", self.layout_orizzontale3)
        #pulsante_prenota_parcheggio.clicked.connect(self.call_prenota_parcheggio)

        pulsante_prenota_parcheggio = self.crea_bottone("TABELLA \nORARI", self.layout_verticale)
        # pulsante_prenota_parcheggio.clicked.connect(self.call_prenota_parcheggio)

        self.layout_orizzontale2.addSpacerItem(QSpacerItem(1300,0))
        self.layout_orizzontale3.addSpacerItem(QSpacerItem(1300, 0))

        self.layout_verticale.addSpacerItem(QSpacerItem(0,150))


    def call_lista_piste(self):
        self.vista_lista_piste = vista_lista_piste(self.show)
        self.vista_lista_piste.showFullScreen()
        self.close()

    def call_account_loggato(self):
        self.vista_info_account = vista_account_loggato(self.showFullScreen)
        self.vista_info_account.showFullScreen()
        self.close()

    def call_noleggia_attrezzatura(self):
        self.vista_lista_attrezzatura = vista_lista_attrezzatura(self.showFullScreen)
        self.vista_lista_attrezzatura.showFullScreen()
        self.close()

    def uscita(self):
        self.close()

    def crea_bottone(self, tipo, layout):
        bottone = QPushButton(tipo)
        bottone.setFixedSize(300,100)
        bottone.setFont(QFont('Times New Roman', 20,100,True))
        bottone.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        layout.addWidget(bottone)
        return bottone