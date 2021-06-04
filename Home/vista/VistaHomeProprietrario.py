from PyQt5.QtGui import QPalette, QBrush, QImage, QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QSizePolicy, QSpacerItem, \
    QDesktopWidget, QHBoxLayout
from ElencoDipendenti.vista.vista_elenco_dipendenti import VistaElencoDipendenti
from ListaAttrezzatura.vista.VistaListaAttrezzatura import VistaListaAttrezzatura
from ListaPiste.vista.VistaListaPisteProprietario import VistaListaPisteProprietario
from Sessione.vista.VistaAccountLoggato import VistaAccountLoggato
from ElencoManutenzioni.vista.vista_lista_manutenzioni import VistaListaManutenzioni
from ListaAttrezzatura.vista.vistalistaattrezzaturaproprietario import VistaListaAttrezzaturaProprietario
from TabellaOrari.vista.VistaTabellaOrari import VistaTabellaOrari


# Vista per la navigazione nell'area riservata del proprietario
class vista_home_proprietario(QWidget):

    def __init__(self, callback):
        super(vista_home_proprietario, self).__init__()

        # Funzione di richiamo della vista precedente
        self.callback = callback

        # Layout usati per visualizzare e allineare l'intera vista
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale1 = QHBoxLayout()
        self.layout_orizzontale2 = QHBoxLayout()
        self.layout_orizzontale3 = QHBoxLayout()

        # Allineamento del Logo dello stabilimento SARNANONEVE
        self.sfondo = QLabel('')
        self.sfondo.setStyleSheet('QLabel {background-color: darkCyan}')
        pixmap = QPixmap("Data/Immagini/LogoVistaHome.png")
        self.sfondo.setPixmap(pixmap)
        self.layout_orizzontale1.addWidget(self.sfondo)
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(300,0,QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Funzione standard che imposta uno sfondo immagine
        self.show_background()

        # Aggiunta dei layout orizzontali al layout totale
        self.layout_verticale.addLayout(self.layout_orizzontale1)
        self.layout_verticale.addLayout(self.layout_orizzontale2)
        self.layout_verticale.addLayout(self.layout_orizzontale3)

        # Configurazione e allineamento dei pulsanti
        self.show_pulsantiera()

        # Configurazione finale del layout totale
        self.setLayout(self.layout_verticale)

    # Creazione, settaggio e stile dello sfondo
    def show_background(self):
        # Settaggio e ridimensionamento dell'immagine di sfondo dell'attuale vista
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("Data/Immagini/VistaHome.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

    # Metodo per la creazione, configurazione e funzionamento dei pulsanti della vista Home
    def show_pulsantiera(self):

        # Configurazione del pulsante Account
        pulsante_account = self.crea_bottone("ACCOUNT", self.layout_orizzontale1)
        pulsante_account.clicked.connect(self.call_account_loggato)

        # Spaziatura orizzontale
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(50,0))

        # Configurazione del pulsante Logout
        pulsante_esci = self.crea_bottone("LOGOUT", self.layout_orizzontale1)
        pulsante_esci.clicked.connect(self.uscita)

        # Configurazione del pulsante Elenco Dipendenti
        pulsante_dipendenti = self.crea_bottone("ELENCO \nDIPENDENTI", self.layout_orizzontale2)
        pulsante_dipendenti.clicked.connect(self.call_elenco_dipendenti)

        # Spaziatura orizzontale
        self.layout_orizzontale2.addSpacerItem(QSpacerItem(100, 0))

        # Configurazione del pulsante Lista Pista
        pulsante_lista_piste = self.crea_bottone("LISTA PISTE", self.layout_orizzontale2)
        pulsante_lista_piste.clicked.connect(self.call_lista_piste_proprietario)

        # Configurazione del pulsante Modifica Attrezzatura
        pulsante_modifica_attrezzatura = self.crea_bottone("MODIFICA \n ATTREZZATURA", self.layout_orizzontale3)
        pulsante_modifica_attrezzatura.clicked.connect(self.call_attrezzatura)

        # Spaziatura orizzontale
        self.layout_orizzontale3.addSpacerItem(QSpacerItem(100, 0))

        # Configurazione del pulsante Manutenzioni
        pulsante_manutenzioni = self.crea_bottone("MANUTENZIONI", self.layout_orizzontale3)
        pulsante_manutenzioni.clicked.connect(self.call_manutenzioni)

        # Configurazione del pulsante Tabella Orari
        pulsante_tabella = self.crea_bottone("TABELLA \nORARI", self.layout_verticale)
        pulsante_tabella.clicked.connect(self.call_tabella)

        # Allineamento e configurazione dei layout
        self.layout_orizzontale2.addSpacerItem(QSpacerItem(1300,0))
        self.layout_orizzontale3.addSpacerItem(QSpacerItem(1300, 0))
        self.layout_verticale.addSpacerItem(QSpacerItem(0,150))

    # Metodo che chiama e mostra la vista liste proprietario
    def call_lista_piste_proprietario(self):
        self.vista_lista_piste_proprietario = VistaListaPisteProprietario(self.show)
        self.vista_lista_piste_proprietario.showFullScreen()
        self.close()

    # Metodo che mostra e chiama la vista account loggato
    def call_account_loggato(self):
        self.vista_info_account = VistaAccountLoggato(self.showFullScreen)
        self.vista_info_account.showFullScreen()
        self.close()

    # Metodo che chiama e mostra la vista modifica attrezzatura
    def call_modifica_attrezzatura(self):
        self.vista_lista_attrezzatura = VistaListaAttrezzatura(self.showFullScreen)
        self.vista_lista_attrezzatura.showFullScreen()
        self.close()

    # Metodo che chiama e mostra la vista lista manutenzioni
    def call_manutenzioni(self):
        self.vista_lista_manutenzioni = VistaListaManutenzioni(self.showFullScreen)
        self.vista_lista_manutenzioni.showFullScreen()
        self.close()

    # Metodo che chiama e mostra la vista elenco dipendenti
    def call_elenco_dipendenti(self):
        self.vista_elenco_dipendenti = VistaElencoDipendenti(self.showFullScreen)
        self.vista_elenco_dipendenti.showFullScreen()
        self.close()

    # Metodo che chiama e mostra la vista attrezzatura
    def call_attrezzatura(self):
        self.vista_attrezzatura = VistaListaAttrezzaturaProprietario(self.showFullScreen)
        self.vista_attrezzatura.showFullScreen()
        self.close()

    # Metodo che chiama e mostra la vista tabella orari
    def call_tabella(self):
        self.tabella = VistaTabellaOrari(self.showFullScreen)
        self.tabella.showFullScreen()
        self.close()

    # Metodo che, collegato al bottone "LOGOUT", permette di uscire
    def uscita(self):
        self.callback()
        self.close()

    # Metodo che semplifica la creazione di un pulsante standard
    def crea_bottone(self, tipo, layout):
        bottone = QPushButton(tipo)
        bottone.setFixedSize(300,100)
        bottone.setFont(QFont('Times New Roman', 20, 100, True))
        bottone.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        layout.addWidget(bottone)
        return bottone
