from functools import partial
from PyQt5.QtGui import QFont, QBrush, QPalette, QImage
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, \
    QDesktopWidget, QGridLayout
from ListaPiste.controller.controller_lista_piste import controller_lista_piste
from Pista.vista.VistaPistaProprietario import vista_pista_proprietario
from Pista.vista.VistaPistaProprietario import vista_pista_proprietario


class vista_lista_piste_proprietario(QWidget):
    def __init__(self, callback):
        super(vista_lista_piste_proprietario, self).__init__()

        # Attributi
        self.callback = callback
        self.controller = controller_lista_piste()
        self.vista_pista = None
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale1 = QHBoxLayout()

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


        self.layout_verticale1.addLayout(self.layout_orizzontale1)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 25, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Impostazione layout totale
        self.setLayout(self.layout_verticale1)
        self.setWindowTitle('Lista Piste')


    def call_vista_pista_proprietario(self, pista):
        self.vista_pista_proprietario = vista_pista_proprietario(pista, self.showFullScreen,self.controller.salva_dati)
        self.vista_pista_proprietario.showFullScreen()
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
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(5, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale1.addWidget(pulsante_indietro)

        apri_tutte_le_piste = QPushButton("APRI\nTUTTE")
        apri_tutte_le_piste.setStyleSheet('QPushButton {background-color: orange;}')
        apri_tutte_le_piste.setFont(QFont('Times New Roman', 15, 50, True))
        apri_tutte_le_piste.setFixedSize(100, 100)
        #apri_tutte_le_piste.clicked.connect(self.indietro)
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(5, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale1.addWidget(apri_tutte_le_piste)


        chiudi_tutte_le_piste = QPushButton("CHIUDI\nTUTTE")
        chiudi_tutte_le_piste.setStyleSheet('QPushButton {background-color: orange;}')
        chiudi_tutte_le_piste.setFont(QFont('Times New Roman', 15, 50, True))
        chiudi_tutte_le_piste.setFixedSize(100, 100)
        # apri_tutte_le_piste.clicked.connect(self.indietro)
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(5, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale1.addWidget(chiudi_tutte_le_piste)
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(5000, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.layout_verticale1.addLayout(self.layout_orizzontale1)


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

    def call_vista_pista(self, pista):
        self.vista_pista = vista_pista_proprietario(pista, self.showFullScreen)
        self.vista_pista.showFullScreen()
        self.close()