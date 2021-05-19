from functools import partial

from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, \
    QDesktopWidget, QSpinBox, QMessageBox
from GestioneParcheggi.controller.controller_gestione_parcheggi import gestione_parcheggi
from Sessione.model.sessione import sessione

class vista_parcheggio(QWidget):

    def __init__(self,callback):
        super(vista_parcheggio, self).__init__()

        self.controller_gestione_parcheggio = gestione_parcheggi()
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.callback = callback
        self.num_giorni = 1

        self.show_background("PARCHEGGIO CAPANNINA")

        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))

        if sessione.controlla_prenotazione_effettuata(6):
            label =QLabel("POSTI DISPONIBILI:\n{} ".format(self.controller_gestione_parcheggio.get_posti_disponibili()))
        else :
            label = QLabel("POSTI DISPONIBILI:\n{}\n(prenotazione effettuata)".format(self.controller_gestione_parcheggio.get_posti_disponibili()))


        label.setFont(QFont('Times New Roman', 30))
        label.setStyleSheet("background-image:url(Pista/data/legno.jpg)")
        label.setAlignment(Qt.AlignCenter)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(600, 500, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale.addWidget(label)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(600, 300, QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.layout_verticale.addLayout(self.layout_orizzontale)

        self.layout_verticale.addSpacerItem(QSpacerItem(0, 200, QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.show_pulsantiera()

        self.layout_verticale.addSpacerItem(QSpacerItem(0, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))


        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Parcheggio')

    def show_background(self,titolo):

        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        immagine = QImage("GestioneParcheggi\data\parcheggio2.jpg")
        img = immagine.scaled(self.width(),self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        titolo =QLabel(titolo)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale.addWidget(titolo)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))

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

    def call_selezione_giorni(self):
        self.vista = vista_richiesta_giorni(self.controller_gestione_parcheggio)
        self.vista.show()

    def indietro(self):
        self.callback()
        self.close()

class vista_richiesta_giorni(QWidget):

    def __init__(self,controller_parcheggi):
        super(vista_richiesta_giorni, self).__init__()

        self.controller_parcheggi = controller_parcheggi
        self.layout_verticale = QVBoxLayout()
        self.num_giorni = 1
        self.setFixedSize(400,300)


        label = QLabel("NUMERO GIORNI DA PRENOTARE:")
        label.setFont(QFont('Times New Roman', 10))
        label.setSizePolicy(300, 300)
        self.giorni = QSpinBox(self)
        self.giorni.setFont(QFont('Times New Roman', 20))
        self.giorni.setAlignment(Qt.AlignCenter)
        self.giorni.setFixedSize(100,50)
        self.giorni.setRange(1, 5)

        bottone = QPushButton("Prenota")
        bottone.clicked.connect(self.call_prenota)

        self.layout_verticale.addWidget(label)
        self.layout_verticale.addSpacerItem(QSpacerItem(150, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale.addWidget(self.giorni)
        self.layout_verticale.addWidget(bottone)


        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Giorni')

    def call_prenota(self):
        val = self.giorni.value()
        risultato =self.controller_parcheggi.prenota_parcheggio(val)
        self.controller_parcheggi.salva_lista_piste()
        sessione.salva_dati()
        self.vista_chiusa = vista_esito(risultato)
        self.vista_chiusa.show()
        self.close()

class vista_esito(QWidget):
    def __init__(self,risultato):
        super(vista_esito, self).__init__()
        self.layout_verticale = QVBoxLayout()
        self.setFixedSize(400, 300)

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

    def call_chiudi(self):
        self.close()











