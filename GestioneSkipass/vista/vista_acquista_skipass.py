from functools import partial
from PyQt5.QtGui import QPalette, QBrush, QImage, QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QSizePolicy, QSpacerItem, \
    QDesktopWidget, QHBoxLayout
from PyQt5.QtCore import Qt
from Skipass.vista.vistaskipass import VistaSkipass
from GestioneSkipass.controller.controllergestioneskipass import ControllerGestioneSkipass


# Vista utile per la gestione della prenotazione dello skipass
class VistaAcquistaSkipass(QWidget):

    def __init__(self, callback):
        super(VistaAcquistaSkipass, self).__init__()

        # Funzione di richiamo della vista precedente
        self.callback = callback

        # Controller della gestione skipass importante per effettuare le varie funzioni
        self.controller_gestione_skipass = ControllerGestioneSkipass()

        # Layout usati per visualizzare e allineare l'intera vista
        self.layout_verticale1 = QVBoxLayout()
        self.layout_verticale2 = QVBoxLayout()
        self.layout_verticale3 = QVBoxLayout()
        self.layout_orizzontale1 = QHBoxLayout()
        self.layout_orizzontale2 = QHBoxLayout()

        # Funzione standard che imposta uno sfondo immagine e un titolo nella attuale vista
        self.show_background("PRENOTA SKIPASS")

        # Settaggio layout e creazione dei vari pulsanti skipass
        self.layout_verticale2.addWidget(self.show_pulsante
                                         ("Mattiniero", self.controller_gestione_skipass.visualizza_lista(0)))
        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 50))
        self.layout_verticale2.addWidget(self.show_pulsante
                                         ("Pomeridiano", self.controller_gestione_skipass.visualizza_lista(1)))
        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 50))

        self.layout_verticale2.addWidget(self.show_pulsante
                                         ("Giornaliero", self.controller_gestione_skipass.visualizza_lista(2)))

        self.layout_verticale3.addWidget(self.show_pulsante
                                         ("Settimanale", self.controller_gestione_skipass.visualizza_lista(3)))
        self.layout_verticale3.addSpacerItem(QSpacerItem(0, 50))

        self.layout_verticale3.addWidget(self.show_pulsante
                                         ("Mensile", self.controller_gestione_skipass.visualizza_lista(4)))
        self.layout_verticale3.addSpacerItem(QSpacerItem(0, 50))

        self.layout_verticale3.addWidget(self.show_pulsante
                                         ("Stagionale", self.controller_gestione_skipass.visualizza_lista(5)))

        # Allineamento e configurazione layout orizzontale
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(40, 0))
        self.layout_orizzontale1.addLayout(self.layout_verticale2)
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(300, 0))
        self.layout_orizzontale1.addLayout(self.layout_verticale3)
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(40, 0))

        # Allineamento e configurazione layout verticale
        self.layout_verticale1.addLayout(self.layout_orizzontale1)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50))
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50))

        # Allineamento e configurazione layout orizzontale
        self.layout_orizzontale2.addSpacerItem(QSpacerItem(20, 0))
        self.layout_orizzontale2.addWidget(self.show_pulsante_indietro("Indietro", self.indietro))
        self.layout_orizzontale2.addSpacerItem(QSpacerItem(20, 0))

        # Configurazione finale del layout totale
        self.layout_verticale1.addLayout(self.layout_orizzontale1)
        self.layout_verticale1.addLayout(self.layout_verticale2)
        self.layout_verticale1.addLayout(self.layout_orizzontale2)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 200))
        self.setLayout(self.layout_verticale1)

    # Metodo per la creazione e funzionamento del bottone indietro
    def show_pulsante_indietro(self, titolo, call):
        pulsante_esci = self.crea_bottone(titolo)
        pulsante_esci.clicked.connect(call)
        return pulsante_esci

    # Creazione, stile e settaggio sfondo e titolo
    def show_background(self, stringa):
        # Settaggio e ridimensionamento dell'immagine di sfondo dell'attuale vista
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("Data/Immagini/VistaSkipass.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Settaggio e allineamento del titolo della vista
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addWidget(titolo)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))

    # Metodo per mostrare il pulsante associato ad ogni skipass
    def show_pulsante(self, titolo, skipass):
        pulsante_skipass = self.crea_bottone(titolo)
        pulsante_skipass.clicked.connect(partial(self.call_skipass, skipass))
        return pulsante_skipass

    # Metodo per richiamare la vista skipass
    def call_skipass(self, skipass):
        self.vista_skipass = VistaSkipass(skipass, self.showFullScreen, self.controller_gestione_skipass)
        self.vista_skipass.showFullScreen()
        self.close()

    # Metodo per la configurazione un bottone standard
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
