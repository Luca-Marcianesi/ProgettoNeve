import webbrowser
from functools import partial

from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QDesktopWidget, QWidget, QSizePolicy, QSpacerItem, QHBoxLayout, \
    QPushButton
from PyQt5.QtCore import Qt

class vista_informazioni(QWidget):
    def __init__(self, callback):
        super(vista_informazioni, self).__init__()


        # Attributi
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.layout_orizzontale1 = QHBoxLayout()
        self.url = "http://www.sarnanoneve.it"
        self.url1 = ""
        self.callback = callback

        # Impostazione Layout totale
        self.show_background("INFORMAZIONI")
        self.layout_orizzontale.addSpacerItem(QSpacerItem(790, 0))
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 150))
        self.label()
        self.pulsante_web()
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(542, 0))
        self.label1()
        self.pulsante_web1()
        self.layout_orizzontale.addSpacerItem(QSpacerItem(500, 0))
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(500, 0))
        self.layout_verticale.addLayout(self.layout_orizzontale)
        self.layout_verticale.addLayout(self.layout_orizzontale1)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 600))
        self.layout_verticale.addWidget(self.pulsante_indietro())
        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Informazioni')

    # Impostazione dello sfondo
    def show_background(self, titolo):
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("Home/data/pinguinonuvola.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(titolo)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 40))
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        titolo.setAlignment(Qt.AlignCenter)
        self.layout_verticale.addWidget(titolo)

    # Descrizione Informazioni
    def label(self):
        label = QLabel("Link utili!\n"
                       "Link al sito Sarnano neve:\n")
        label.setFont(QFont('Times New Roman', 25))
        self.layout_orizzontale.addWidget(label)

    # Descrizione Informazioni
    def label1(self):
        label = QLabel("Link \n"
                       "soccorso piste:")
        label.setFont(QFont('Times New Roman', 25))
        self.layout_orizzontale1.addWidget(label)

    # Pulsante indietro
    def pulsante_indietro(self):
        pulsante_indietro = QPushButton("INDIETRO")
        pulsante_indietro.setFont(QFont('Times New Roman', 20, 100, True))
        pulsante_indietro.setStyleSheet('background-color: orange')
        pulsante_indietro.setFixedSize(250, 100)
        pulsante_indietro.clicked.connect(self.indietro)
        return pulsante_indietro

    # Primo pulsante Link
    def pulsante_web(self):
        pulsante_web = QPushButton("http://www.sarnanoneve.it")
        pulsante_web.setFont(QFont('Times New Roman', 18))
        pulsante_web.setStyleSheet('QPushButton{background-color: transparent; color: Blue}')
        pulsante_web.setFixedSize(400, 200)
        pulsante_web.clicked.connect(partial(webbrowser.open,self.url))
        self.layout_orizzontale.addWidget(pulsante_web)

    # Secondo pulsante link
    def pulsante_web1(self):
        pulsante_web = QPushButton("Link soccorso piste")
        pulsante_web.setFont(QFont('Times New Roman', 18))
        pulsante_web.setStyleSheet('QPushButton{background-color: transparent; color: Blue}')
        pulsante_web.setFixedSize(400, 200)
        pulsante_web.clicked.connect(partial(webbrowser.open,self.url1))
        self.layout_orizzontale1.addWidget(pulsante_web)

    # Collegamento del pulsante indietro per tornare alla schermata precedente
    def indietro(self):
        self.callback()
        self.close()

