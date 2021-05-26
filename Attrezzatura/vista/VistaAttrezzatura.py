from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, \
                            QDesktopWidget, QLabel, QPushButton
from Attrezzatura.controller.controller_attrezzatura import ControllerAttrezzatura
from Sessione.model.sessione import Sessione

# vista dell'attrezzatura


class VistaAttrezzatura(QWidget):
    def __init__(self, callback, attrezzatura, prenota, aggiorna):
        super(VistaAttrezzatura, self).__init__()

        # Attributi
        self.aggiorna = aggiorna
        self.attrezzatura = attrezzatura
        self.controller = ControllerAttrezzatura(self.attrezzatura)
        self.callback = callback
        self.prenota = prenota
        self.layout_verticale2 = QVBoxLayout()
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()

        # Sfondo
        self.show_background("ATTREZZATURA")

        # Spaziatura orizzontale
        self.layout_orizzontale.addSpacerItem(QSpacerItem(500, 0))

        # Descrizione Pista, aggiunta al layout e spaziatura
        label = QLabel("Nome: {}".format(self.controller.get_nome()) + "\n"
                       "Lunghezza: {}".format(self.controller.get_dimensioni()) + " cm" + "\n"
                       "Stato: {}".format(self.stato_attrezzatura()))
        label.setFont(QFont('Times New Roman', 30, 75))
        label.setStyleSheet("background-image:url(Attrezzatura/data/legnopista.jpg)")
        label.setAlignment(Qt.AlignCenter)
        label.setFixedSize(500, 200)
        self.layout_verticale2.addWidget(label)

        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 100))

        # Pulsante Indietro allineato
        self.show_pulsantiera()
        self.layout_orizzontale.addLayout(self.layout_verticale2)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(500, 0))

        # Impostazione layout totale
        self.layout_verticale1.addLayout(self.layout_orizzontale)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 250))
        self.setLayout(self.layout_verticale1)

    # Metodo che permette, cliccando il bottone "indietro", di tornare alla vista precedente
    def indietro(self):
        self.callback()
        self.close()

    # Impostazione dello sfondo
    def show_background(self, stringa):
        # Sfondo
        self.setFixedSize(QDesktopWidget().width(), QDesktopWidget().height())
        immagine = QImage(" Data/Immagini/VistaAttrezzatura.jpg")
        immagine = immagine.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(immagine))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 60))
        self.layout_verticale1.addWidget(titolo)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 150))

    # Metodo per creazione, stile e funzionamento dei bottoni indietro e prenota
    def show_pulsantiera(self):
        # Punsante indietro
        layout_pulsanti1 = QVBoxLayout()
        layout_pulsanti2 = QHBoxLayout()
        pulsante_indietro = QPushButton("Indietro")
        pulsante_indietro.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante_indietro.setFont(QFont('Times New Roman', 30, 100, True))
        pulsante_indietro.setFixedSize(300, 100)
        pulsante_indietro.clicked.connect(self.indietro)

        pulsante_prenota = QPushButton("Prenota")
        pulsante_prenota.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante_prenota.setFont(QFont('Times New Roman', 30, 100, True))
        pulsante_prenota.setFixedSize(300, 100)
        pulsante_prenota.clicked.connect(self.prenotazione)
        layout_pulsanti1.addWidget(pulsante_prenota)

        layout_pulsanti1.addSpacerItem(QSpacerItem(0, 100))
        layout_pulsanti1.addWidget(pulsante_indietro)
        layout_pulsanti2.addLayout(layout_pulsanti1)

        self.layout_verticale2.addLayout(layout_pulsanti2)

    # Metodo che controlla lo stato dell'attrezzatura
    def stato_attrezzatura(self):
        if self.controller.get_stato():
            return "Disponibile"
        return "Non disponibile"

    # Metodo per la prenotazione
    def prenotazione(self):
        risultato = self.prenota(self.attrezzatura)
        self.vista_chiusura = VistaEsito(risultato)
        self.vista_chiusura.show()
        self.aggiorna()
        Sessione.salva_dati()


# Classe esito -> compare una finestra una volta fatta la prenotazione
class VistaEsito(QWidget):
    def __init__(self, risultato):
        super(VistaEsito, self).__init__()
        self.layout_verticale = QVBoxLayout()
        self.setMaximumSize(500, 200)

        # Controllo dello stato per la stampa a finestra
        if risultato != "Prenotazione effettuata":
            risultato = "Hai già prenotato questa attrezzatura!"

        # Creazione, aggiunta e descrizione della finestra
        label = QLabel(risultato)
        label.setFont(QFont('Times New Roman', 20))
        label.setAlignment(Qt.AlignCenter)

        bottone = QPushButton("Chiudi")
        bottone.clicked.connect(self.call_chiudi)

        self.layout_verticale.addWidget(label)
        self.layout_verticale.addSpacerItem(QSpacerItem(150, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale.addWidget(bottone)

        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Esito')

    # Metodo per la chiusura della finestra
    def call_chiudi(self):
        self.close()
