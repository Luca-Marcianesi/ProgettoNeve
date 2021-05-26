
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, \
    QDesktopWidget, QSpinBox

from Sessione.model.sessione import Sessione
from GestioneParcheggi.controller.controllergestioneparcheggi import ControllerGestioneParcheggi

# Vista parcheggio


class VistaParcheggio(QWidget):

    def __init__(self, callback):
        super(VistaParcheggio, self).__init__()

        # Controller e layout
        self.controller_gestione_parcheggio = ControllerGestioneParcheggi()
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.callback = callback
        self.num_giorni = 1

        # Mostra sfondo
        self.show_background("PARCHEGGIO CAPANNINA")

        # Spaziatura
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.label = QLabel()
        self.label.setFont(QFont('Times New Roman', 30))
        self.label.setStyleSheet("background-image:url(Data/Immagini/legnopista.jpg)")
        self.label.setAlignment(Qt.AlignCenter)

        self.aggiorna()

        self.layout_orizzontale.addSpacerItem(QSpacerItem(600, 500, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale.addWidget(self.label)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(600, 300, QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.layout_verticale.addLayout(self.layout_orizzontale)

        self.layout_verticale.addSpacerItem(QSpacerItem(0, 200, QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.show_pulsantiera()

        self.layout_verticale.addSpacerItem(QSpacerItem(0, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Parcheggio')

    def aggiorna(self):
        if Sessione.controlla_prenotazione_effettuata(2):  # 2 è il codice assegnato al parcheggio
            self.label.setText("POSTI DISPONIBILI:\n{} ".format
                           (self.controller_gestione_parcheggio.get_posti_disponibili()))
        else:
            self.label.setText("POSTI DISPONIBILI:\n{}\n(prenotazione effettuata)".format
                           (self.controller_gestione_parcheggio.get_posti_disponibili()))

    # Creazione, stile e settaggio sfondo e titolo
    def show_background(self, titolo):

        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        immagine = QImage('Data/Immagini/Parcheggio.jpg')
        img = immagine.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(titolo)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale.addWidget(titolo)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))

    # Creazione, stile e settaggio dei pulsanti
    def show_pulsantiera(self):

        layout_pulsanti = QHBoxLayout()
        layout_pulsanti.setAlignment(Qt.AlignCenter)
        pulsante_indietro = QPushButton("INDIETRO")
        pulsante_indietro.setFont(QFont('Times New Roman', 18, 100, True))
        pulsante_indietro.setFixedSize(250, 100)
        pulsante_indietro.setStyleSheet("background-color: orange")
        pulsante_indietro.clicked.connect(self.indietro)

        pulsante_prenota = QPushButton("PRENOTA")
        pulsante_prenota.setFont(QFont('Times New Roman', 18, 100, True))
        pulsante_prenota.setFixedSize(250, 100)
        pulsante_prenota.setStyleSheet("background-color: orange")
        pulsante_prenota.clicked.connect(self.call_selezione_giorni)

        layout_pulsanti.addWidget(pulsante_prenota)
        layout_pulsanti.addSpacerItem(QSpacerItem(50, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        layout_pulsanti.addWidget(pulsante_indietro)
        self.layout_verticale.addLayout(layout_pulsanti)

    # Chiamata e mostra della vista richiesta giorni
    def call_selezione_giorni(self):
        self.vista = VistaRichiestaGiorni(self.controller_gestione_parcheggio,self.aggiorna)
        self.vista.show()

    # Metodo che permette, cliccando il bottone "indietro", di tornare alla vista precedente
    def indietro(self):
        self.callback()
        self.close()

# Vista richiesta giorni


class VistaRichiestaGiorni(QWidget):

    def __init__(self, controller_parcheggi,aggiorna):
        super(VistaRichiestaGiorni, self).__init__()

        # Controller
        self.controller_parcheggi = controller_parcheggi
        self.layout_verticale = QVBoxLayout()
        self.num_giorni = 1
        self.setFixedSize(400, 300)
        self.aggiorna = aggiorna

        # Descrizione della finestra per scegliere per quanti giorni prenotare
        label = QLabel("NUMERO GIORNI DA PRENOTARE:")
        label.setFont(QFont('Times New Roman', 10))
        label.setSizePolicy(300, 300)
        self.giorni = QSpinBox(self)
        self.giorni.setFont(QFont('Times New Roman', 20))
        self.giorni.setAlignment(Qt.AlignCenter)
        self.giorni.setFixedSize(100, 50)
        self.giorni.lineEdit().setReadOnly(True)

        self.giorni.setRange(1, 5)

        # Creazione, stile e settaggio bottone prenota e layout totale
        bottone = QPushButton("Prenota")
        bottone.clicked.connect(self.call_prenota)

        self.layout_verticale.addWidget(label)
        self.layout_verticale.addSpacerItem(QSpacerItem(150, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale.addWidget(self.giorni)
        self.layout_verticale.addWidget(bottone)

        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Giorni')

    # Metodo prenota
    def call_prenota(self):
        val = self.giorni.value()
        risultato = self.controller_parcheggi.prenota_parcheggio(val)
        self.aggiorna()
        self.vista_chiusa = VistaEsito(risultato)
        self.vista_chiusa.show()
        self.close()

# Vista esito


class VistaEsito(QWidget):
    def __init__(self, risultato):
        super(VistaEsito, self).__init__()
        self.layout_verticale = QVBoxLayout()
        self.setFixedSize(400, 300)

        # Descrizione, creazione e settaggio esito e layout totale
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

    # Metodo per chiudere la finestra corrente
    def call_chiudi(self):
        self.close()
