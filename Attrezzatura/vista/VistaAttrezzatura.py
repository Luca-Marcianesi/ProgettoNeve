from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QDesktopWidget, QLabel, \
    QPushButton

from Attrezzatura.controller.controller_attrezzatura import controller_attrezzatura
from Attrezzatura.model.attrezzatura import attrezzatura


class vista_attrezzatura(QWidget):
    def __init__(self):
        super(vista_attrezzatura, self).__init__()


        #Attributi
        self.controller = controller_attrezzatura(attrezzatura("scii", 1, "180"))
        self.layout_verticale2 = QVBoxLayout()
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()

        # Sfondo
        self.show_background("ATTREZZATURA")


        self.layout_orizzontale.addSpacerItem(QSpacerItem(50, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))


        # Descrizione Pista
        label = QLabel("Nome: {}".format(self.controller.get_nome()) + "\n"
                    "Dimensione: {}".format(self.controller.get_dimensioni()) + "\n"
                    "Stato: {}".format(self.controller.get_stato()))
        label.setFont(QFont('Times New Roman', 30))
        label.setStyleSheet("background-image:url(Attrezzatura/data/legno.jpg)")
        label.setAlignment(Qt.AlignCenter)
        self.layout_verticale2.addWidget(label)


        # Pulsanti Apri e Indietro allineati
        self.show_pulsantiera()
        self.layout_orizzontale.addLayout(self.layout_verticale2)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(50, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Impostazione layout totale
        self.layout_verticale1.addLayout(self.layout_orizzontale)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 400, QSizePolicy.Fixed, QSizePolicy.Fixed))
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
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 20, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addWidget(titolo)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 100, QSizePolicy.Fixed, QSizePolicy.Fixed))

    def show_pulsantiera(self):
        # Punsante indietro
        layout_pulsanti = QHBoxLayout()
        pulsante_indietro = QPushButton()
        pulsante_indietro.setStyleSheet("background-image:url(Attrezzatura/data/arrow.jpg)")
        pulsante_indietro.setFont(QFont('Times New Roman', 18))
        pulsante_indietro.setFixedSize(100, 100)
        pulsante_indietro.clicked.connect(self.indietro)
        layout_pulsanti.addSpacerItem(QSpacerItem(50, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        layout_pulsanti.addWidget(pulsante_indietro)
        layout_pulsanti.addSpacerItem(QSpacerItem(50, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale2.addLayout(layout_pulsanti)
