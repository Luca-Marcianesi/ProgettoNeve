from PyQt5.QtGui import QPalette, QBrush, QImage, QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QSizePolicy, QSpacerItem, \
    QDesktopWidget, QHBoxLayout

from ElencoDipendenti.vista.VistaElencoDipendenti import vista_elenco_dipendenti
from ListaAttrezzatura.vista.VistaListaAttrezzatura import vista_lista_attrezzatura
from ListaPiste.vista.VistaListaPisteProprietario import vista_lista_piste_proprietario
from Sessione.vista.VistaAccountLoggato import vista_account_loggato
from ElencoManutenzioni.vista.vista_lista_manutenzioni import vista_lista_manutenzioni
from ListaAttrezzatura.vista.vista_lista_attrezzatura_proprietario import vista_lista_attrezzatura_proprietario

# Classe vista home proprietario
class vista_home_proprietario(QWidget):

    def __init__(self,callback):
        super(vista_home_proprietario, self).__init__()

        # Attributi
        self.callback = callback
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

        # Spaziature
        self.layout_verticale.addLayout(self.layout_orizzontale1)

        self.layout_verticale.addLayout(self.layout_orizzontale2)

        self.layout_verticale.addLayout(self.layout_orizzontale3)

        self.show_pulsantiera()

        # Impostazione layout totale
        self.setLayout(self.layout_verticale)

    # Creazione, settaggio e stile dello sfondo
    def show_background(self):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("Data/Immagini/2.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

    # Creazione, settaggio e stile dei pulsanti
    def show_pulsantiera(self):
        pulsante_account = self.crea_bottone("ACCOUNT", self.layout_orizzontale1)
        pulsante_account.clicked.connect(self.call_account_loggato)

        self.layout_orizzontale1.addSpacerItem(QSpacerItem(50,0))


        pulsante_esci = self.crea_bottone("LOGOUT", self.layout_orizzontale1)
        pulsante_esci.clicked.connect(self.uscita)

        pulsante_dipendenti = self.crea_bottone("ELENCO \nDIPENDENTI", self.layout_orizzontale2)
        pulsante_dipendenti.clicked.connect(self.call_elenco_dipendenti)

        self.layout_orizzontale2.addSpacerItem(QSpacerItem(100, 0))

        pulsante_lista_piste = self.crea_bottone("LISTA PISTE", self.layout_orizzontale2)
        pulsante_lista_piste.clicked.connect(self.call_lista_piste_proprietario)

        pulsante_modifica_attrezzatura = self.crea_bottone("MODIFICA \n ATTREZZATURA", self.layout_orizzontale3)
        pulsante_modifica_attrezzatura.clicked.connect(self.call_attrezzatura)

        self.layout_orizzontale3.addSpacerItem(QSpacerItem(100, 0))

        pulsante_manutenzioni = self.crea_bottone("MANUTENZIONI", self.layout_orizzontale3)
        pulsante_manutenzioni.clicked.connect(self.call_manutenzioni)

        pulsante_tabella = self.crea_bottone("TABELLA \nORARI", self.layout_verticale)
        # pulsante_tabella.clicked.connect(self.call_prenota_parcheggio)

        self.layout_orizzontale2.addSpacerItem(QSpacerItem(1300,0))
        self.layout_orizzontale3.addSpacerItem(QSpacerItem(1300, 0))

        self.layout_verticale.addSpacerItem(QSpacerItem(0,150))

    # Metodo che chiama e mostra la vista liste proprietario
    def call_lista_piste_proprietario(self):
        self.vista_lista_piste_proprietario = vista_lista_piste_proprietario(self.show)
        self.vista_lista_piste_proprietario.showFullScreen()
        self.close()

    # Metodo che mostra e chiama la vista account loggato
    def call_account_loggato(self):
        self.vista_info_account = vista_account_loggato(self.showFullScreen)
        self.vista_info_account.showFullScreen()
        self.close()

    # Metodo che chiama e mostra la vista modifica attrezzatura
    def call_modifica_attrezzatura(self):
        self.vista_lista_attrezzatura = vista_lista_attrezzatura(self.showFullScreen)
        self.vista_lista_attrezzatura.showFullScreen()
        self.close()

    # Metodo che chiama e mostra la vista lista manutenzioni
    def call_manutenzioni(self):
        self.vista_lista_manutenzioni = vista_lista_manutenzioni(self.showFullScreen)
        self.vista_lista_manutenzioni.showFullScreen()
        self.close()

    # Metodo che chiama e mostra la vista elenco dipendenti
    def call_elenco_dipendenti(self):
        self.vista_elenco_dipendenti = vista_elenco_dipendenti(self.showFullScreen)
        self.vista_elenco_dipendenti.showFullScreen()
        self.close()

    # Metodo che chiama e mostra la vista attrezzatura
    def call_attrezzatura(self):
        self.vista_attrezzatura = vista_lista_attrezzatura_proprietario(self.showFullScreen)
        self.vista_attrezzatura.showFullScreen()
        self.close()

    # Metodo che, collegato al bottone "LOGOUT", permette di uscire
    def uscita(self):
        self.callback()
        self.close()

    # Metodo crea bottone generale
    def crea_bottone(self, tipo, layout):
        bottone = QPushButton(tipo)
        bottone.setFixedSize(300,100)
        bottone.setFont(QFont('Times New Roman', 20, 100, True))
        bottone.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        layout.addWidget(bottone)
        return bottone