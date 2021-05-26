from functools import partial
from PyQt5.QtGui import QFont, QBrush, QPalette, QImage
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, \
    QDesktopWidget, QGridLayout
from ListaPiste.controller.controllerlistapiste import ControllerListaPiste
from Pista.vista.VistaPista import vista_pista

# Vista lista piste


class VistaListaPiste(QWidget):
    def __init__(self, callback):
        super(VistaListaPiste, self).__init__()

        # Attributi
        self.callback = callback
        self.controller = ControllerListaPiste()
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

    # Metodo che chiama e mostra la vista pista
    def call_vista_pista(self, pista):
        self.vista_pista = vista_pista(pista, self.showFullScreen)
        self.vista_pista.show()

    # Metodo che, collegato al pulsante "INDIETRO", permette di tornare alla vista precedente
    def indietro(self):
        self.callback()
        self.close()

    # Creazione settaggio e stile dello sfondo
    def show_background(self):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("Data/Immagini/ImmaginePiste.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

    # Creazione, settaggio, aggiunta al layout e stile pulsante indietro
    def show_pulsante_indietro(self):

        # Punsante indietro
        pulsante_indietro = QPushButton()
        pulsante_indietro.setStyleSheet('QPushButton {background-color: lightBlue;}')
        pulsante_indietro.setStyleSheet("background-image:url(Data/Immagini/FrecciaIndietro.jpg)")
        pulsante_indietro.setFixedSize(100, 100)
        pulsante_indietro.clicked.connect(self.indietro)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(5, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale.addWidget(pulsante_indietro)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(5000, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addLayout(self.layout_orizzontale)

    # Creazione, settaggio, aggiunta al layout e stile della descrizione piste
    def show_pulsantiera_piste(self):
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
            else:
                bottone.setStyleSheet('QPushButton {background-color: lightBlue; color: red;}')
            bottone.clicked.connect(partial(self.call_vista_pista, pista))
            if colonna == 5 or colonna == 10:
                colonna = 0
                riga += 1
            layout_piste.addWidget(bottone, riga, colonna)
            colonna += 1
            indice_pista += 1
        self.layout_verticale1.addLayout(layout_piste)
