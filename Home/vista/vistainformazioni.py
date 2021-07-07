import webbrowser
from functools import partial
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QDesktopWidget, QWidget, QSizePolicy, QSpacerItem, QHBoxLayout, \
    QPushButton
from PyQt5.QtCore import Qt


# Vista informazioni
class VistaInformazioni(QWidget):

    def __init__(self, callback):
        super(VistaInformazioni, self).__init__()

        # Funzione di richiamo della vista precedente
        self.callback = callback

        # Layout usati per visualizzare e allineare l'intera vista
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale1 = QHBoxLayout()
        self.layout_orizzontale2 = QHBoxLayout()
        self.layout_orizzontale3 = QHBoxLayout()

        # Definizione degli url da inserire nella label
        self.url = "http://www.sarnanoneve.it"
        self.url1 = "https://www.crocebianca.bz.it/it/i-nostri-servizi/soccorso/servizio-soccorso-piste-647.html"

        # Funzione standard che imposta uno sfondo immagine
        self.show_background("INFORMAZIONI")

        # Spaziature
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(790, 0))
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 150))

        # Label contenente le informazioni principali
        self.label()
        self.pulsante_web()
        self.layout_orizzontale2.addSpacerItem(QSpacerItem(542, 0))
        self.label1()
        self.pulsante_web1()

        # Configurazione finale del layout totale
        self.layout_verticale.addLayout(self.layout_orizzontale1)
        self.layout_verticale.addLayout(self.layout_orizzontale2)
        self.layout_verticale.addLayout(self.layout_orizzontale3)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 600))
        self.layout_verticale.addWidget(self.pulsante_indietro())
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50))
        self.setLayout(self.layout_verticale)

    # Creazione, stile e settaggio sfondo e titolo
    def show_background(self, titolo):
        # Settaggio e ridimensionamento dell'immagine di sfondo dell'attuale vista
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("Data/Immagini/VistaInfo.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Settaggio e allineamento del titolo della vista
        titolo = QLabel(titolo)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        titolo.setAlignment(Qt.AlignCenter)
        self.layout_verticale.addWidget(titolo)

    # Descrizione Informazioni del sito sarnano neve
    def label(self):
        label = QLabel("Link utili:")
        label2 = QLabel("Link al sito Sarnano neve:")
        label.setFont(QFont('Times New Roman', 35))
        label2.setFont(QFont('Times New Roman', 25))
        self.layout_orizzontale1.addWidget(label)
        self.layout_orizzontale2.addSpacerItem(QSpacerItem(300, 200))
        self.layout_orizzontale2.addWidget(label2)

    # Descrizione Informazioni del soccorso piste
    def label1(self):
        label = QLabel("Link soccorso piste:")
        label.setFont(QFont('Times New Roman', 25))
        self.layout_orizzontale3.addSpacerItem(QSpacerItem(300, 50))
        self.layout_orizzontale3.addWidget(label)

    # Configurazione e allineamento del pulsante indietro
    def pulsante_indietro(self):
        pulsante_indietro = QPushButton("INDIETRO")
        pulsante_indietro.setFont(QFont('Times New Roman', 20, 100, True))
        pulsante_indietro.setStyleSheet('background-color: orange')
        pulsante_indietro.setFixedSize(250, 100)
        pulsante_indietro.clicked.connect(self.indietro)
        return pulsante_indietro

    # Configurazione e allineamento del primo pulsante Link
    def pulsante_web(self):
        pulsante_web = QPushButton("http://www.sarnanoneve.it")
        pulsante_web.setFont(QFont('Times New Roman', 20))
        pulsante_web.setStyleSheet('QPushButton{background-color: transparent; color: Blue}')
        pulsante_web.clicked.connect(partial(webbrowser.open, self.url))
        self.layout_orizzontale2.addSpacerItem(QSpacerItem(150, 0))
        self.layout_orizzontale2.addWidget(pulsante_web)
        self.layout_orizzontale2.addSpacerItem(QSpacerItem(50, 0))

    # Configurazione e allineamento del secondo pulsante link
    def pulsante_web1(self):
        pulsante_web = QPushButton("https://www.soccorso-piste.it")
        pulsante_web.setFont(QFont('Times New Roman', 20))
        pulsante_web.setStyleSheet('QPushButton{background-color: transparent; color: Blue}')
        pulsante_web.clicked.connect(partial(webbrowser.open, self.url1))
        self.layout_orizzontale3.addWidget(pulsante_web)
        self.layout_orizzontale3.addSpacerItem(QSpacerItem(500, 0))

    # Collegamento del pulsante indietro per tornare alla schermata precedente
    def indietro(self):
        self.callback()
        self.close()
