from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QDesktopWidget, QLabel, \
    QPushButton, QMessageBox
from Attrezzatura.controller.controller_attrezzatura import controller_attrezzatura
from Sessione.model.sessione import sessione


class vista_attrezzatura(QWidget):
    def __init__(self, callback, attrezzatura, prenota, aggiorna):
        super(vista_attrezzatura, self).__init__()

        # Attributi
        self.aggiorna = aggiorna
        self.attrezzatura = attrezzatura
        self.controller = controller_attrezzatura(self.attrezzatura)
        self.callback = callback
        self.prenota = prenota
        self.layout_verticale2 = QVBoxLayout()
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()

        # Sfondo
        self.show_background("ATTREZZATURA")

        self.layout_orizzontale.addSpacerItem(QSpacerItem(500, 0))

        # Descrizione Pista
        label = QLabel("Nome: {}".format(self.controller.get_nome()) + "\n"
                       "Lunghezza: {}".format(self.controller.get_dimensioni()) + " cm" + "\n"
                       "Stato: {}".format(self.stato_attrezzatura()))
        label.setFont(QFont('Times New Roman', 30))
        label.setStyleSheet("background-image:url(Attrezzatura/data/legno.jpg)")
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

    def indietro(self):
        self.callback()
        self.close()

    def show_background(self, stringa):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("ListaAttrezzatura/data/1.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 60))
        self.layout_verticale1.addWidget(titolo)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 150))

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

    def stato_attrezzatura(self):
        if self.controller.get_stato():
            return "Disponibile"
        return "Non disponibile"

    def prenotazione(self):
        self.prenota(self.attrezzatura)
        risultato = "Attrezzatura prenotata"
        self.vista_chiusura = vista_esito(risultato)
        self.vista_chiusura.show()
        self.aggiorna()
        sessione.salva_dati()



class vista_esito(QWidget):
    def __init__(self,risultato):
        super(vista_esito, self).__init__()
        self.layout_verticale = QVBoxLayout()
        self.setFixedSize(200, 100)

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
