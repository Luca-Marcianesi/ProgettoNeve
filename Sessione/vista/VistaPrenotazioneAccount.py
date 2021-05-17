from PyQt5.QtGui import QFont, QImage, QPalette, QBrush
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, \
    QPushButton
from PyQt5.QtCore import Qt
from Sessione.controller.controller_sessione import controller_sessione


class vista_prenotazione_account(QWidget):

    def __init__(self, callback):
        super(vista_prenotazione_account, self).__init__()
        # Attributi
        self.controller = controller_sessione()
        self.callback = callback
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()

        # Sfondo
        self.show_background("PRENOTAZIONI ACCOUNT")

        # label
        if self.controller.get_lista_prenotazioni_str() == "":
            self.label = QLabel("Nessuna prenotazione")
        else:
            self.label = QLabel(self.controller.get_lista_prenotazioni_str())
        self.label.setFont(QFont('Times New Roman', 30))
        self.label.setAlignment(Qt.AlignCenter)
        self.layout_verticale.addWidget(self.label)

        # Spaziatura
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 100, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale.addSpacerItem(QSpacerItem(700, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Pulsante indietro allineato
        pulsante_indietro = QPushButton("INDIETRO")
        pulsante_indietro.setFont(QFont('Times New Roman', 30))
        pulsante_indietro.setFixedSize(400, 150)
        pulsante_indietro.clicked.connect(self.indietro)
        self.layout_orizzontale.addWidget(pulsante_indietro)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(700, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Conclusione
        self.layout_verticale.addLayout(self.layout_orizzontale)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 100, QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.setLayout(self.layout_verticale)

    def indietro(self):
        self.callback()
        self.close()

    def show_background(self, stringa):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("Data/Immagini/6.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale.addWidget(titolo)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))
