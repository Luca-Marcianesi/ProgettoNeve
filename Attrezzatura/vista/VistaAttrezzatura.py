from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QDesktopWidget, QLabel, \
    QPushButton

from Attrezzatura.controller.controller_attrezzatura import controller_attrezzatura


class vista_attrezzatura(QWidget):
    def __init__(self, attrezzatura):
        super(vista_attrezzatura, self).__init__()


        #Attributi
        self.controller = controller_attrezzatura(attrezzatura)
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.layout_verticale2 = QVBoxLayout()
        self.layout_verticale3 = QVBoxLayout()

        # Sfondo
        self.show_background("ATTREZZATURA")

        # Spaziatura
        self.layout_orizzontale.addSpacerItem(QSpacerItem(150, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Descrizione Pista
        label = QLabel("Nome: {}".format(self.controller.get_nome()) + "\n"
                    "Dimensione: {}".format(self.controller.get_dimensioni()) + "\n"
                    "Stato: {}".format(self.controller.get_stato()) + "\n")
        label.setFont(QFont('Times New Roman', 30))
        self.layout_verticale3.addWidget(label)

        # Spaziatura
        self.layout_verticale3.addSpacerItem(QSpacerItem(500, 500, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale.addLayout(self.layout_verticale3)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(700, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Pulsanti Apri e Indietro allineati
        self.show_pulsantiera()

        # Spaziatura
        self.layout_orizzontale.addSpacerItem(QSpacerItem(150, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addLayout(self.layout_orizzontale)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Impostazione layout totale
        self.setLayout(self.layout_verticale1)
        self.setWindowTitle('Attrezzatura')

    def closeEvent(self, event):
        pass


    def call_vista_pista(self):
        pass

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
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addWidget(titolo)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))

    def show_pulsantiera(self):
        # Punsante indietro
        layout_pulsanti = QVBoxLayout()
        pulstante_indietro = QPushButton("INDIETRO")
        pulstante_indietro.setFont(QFont('Times New Roman', 18))
        pulstante_indietro.setFixedSize(250, 100)
        pulstante_indietro.clicked.connect(self.indietro)
        layout_pulsanti.addWidget(pulstante_indietro)
        layout_pulsanti.addStretch()
        layout_pulsanti.addSpacerItem(QSpacerItem(0, 500, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale.addLayout(layout_pulsanti)
