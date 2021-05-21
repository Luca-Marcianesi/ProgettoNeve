from functools import partial
from PyQt5.QtGui import QFont, QBrush, QPalette, QImage
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, \
    QDesktopWidget, QGridLayout
from ListaPiste.controller.controller_lista_piste import controller_lista_piste
from Pista.vista.VistaPista import vista_pista


class vista_lista_piste(QWidget):
    def __init__(self, callback):
        super(vista_lista_piste, self).__init__()

        # Attributi
        self.callback = callback
        self.controller = controller_lista_piste()
        self.vista_pista = None
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.layout_verticale2 = QVBoxLayout()

        # Sfondo
        self.show_background()

        # Spaziatura
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 850, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Pulsanti Apri
        self.show_pulsante_indietro()

        # Spaziatura
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 20, QSizePolicy.Fixed, QSizePolicy.Fixed))
        # Pulsanti Apri
        self.show_pulsantiera_piste()

        # Spaziatura
        self.layout_verticale1.addLayout(self.layout_orizzontale)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 25, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Impostazione layout totale
        self.setLayout(self.layout_verticale1)
        self.setWindowTitle('Lista Piste')

    def call_vista_pista(self, pista):
        self.vista_pista = vista_pista(pista, self.showFullScreen)
        self.vista_pista.showFullScreen()
        self.close()

    def indietro(self):
        self.callback()
        self.close()

    def show_background(self):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("ListaPiste/data/Immagine_piste.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

    def show_pulsante_indietro(self):

        # Punsante indietro
        pulsante_indietro = QPushButton()
        pulsante_indietro.setStyleSheet('QPushButton {background-color: lightBlue;}')
        pulsante_indietro.setStyleSheet("background-image:url(Attrezzatura/data/arrow.jpg)")
        pulsante_indietro.setFixedSize(100, 100)
        pulsante_indietro.clicked.connect(self.indietro)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(5, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale.addWidget(pulsante_indietro)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(5000, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addLayout(self.layout_orizzontale)

    def show_pulsantiera_piste(self):
        # Punsante indietro
        layout_piste = QGridLayout()
        riga = 0
        colonna = 0
        indice_pista = 1
        for pista in self.controller.get_lista():
            simbolo = "●"
            bottone = QPushButton("[{}]  ".format(indice_pista) + pista.get_nome_str() + simbolo)
            bottone.setFont(QFont('Times New Roman', 18))
            if pista.get_stato() == "Aperta":
                bottone.setStyleSheet('QPushButton {background-color: lightBlue; color: green;}')
            else :
                bottone.setStyleSheet('QPushButton {background-color: lightBlue; color: red;}')
            bottone.clicked.connect(partial(self.call_vista_pista, pista))
            if colonna == 5 or colonna == 10:
                colonna = 0
                riga += 1
            layout_piste.addWidget(bottone, riga, colonna)
            colonna += 1
            indice_pista += 1
        self.layout_verticale1.addLayout(layout_piste)
