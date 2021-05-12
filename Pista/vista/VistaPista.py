from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont, QBrush, QPalette, QImage, QColor
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QListView, QPushButton, \
    QDesktopWidget
from Pista.controller.controller_pista import controller_pista
from ListaPiste.model.lista_piste import lista_piste


class vista_pista(QWidget):
    def __init__(self):
        super(vista_pista, self).__init__()

        # Attributi
        lista = lista_piste()
        self.controller = controller_pista(lista.cerca_pista_x_numero(15))
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.layout_verticale2 = QVBoxLayout()


        # Sfondo
        self.show_background("PISTA")

        #Descrizione Pista
        label = QLabel("\nNOME => {}\n".format(self.controller.get_nome_str()) +
                        "DIFFICOLTÀ => {}\n".format(self.controller.get_difficolta()) +
                        "STATO => {}\n".format(self.controller.get_stato()) )
        label.setFont(QFont('Times New Roman', 30))
        label.setStyleSheet("background-image:url(Pista/data/download.jpg)")
        label.setAlignment(Qt.AlignCenter)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(500, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale2.addWidget(label)

        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Indietro allineati
        self.show_pulsantiera()

        self.layout_orizzontale.addLayout(self.layout_verticale2)

        self.layout_orizzontale.addSpacerItem(QSpacerItem(500, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))




        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale.addLayout(self.layout_orizzontale)

        self.layout_verticale.addSpacerItem(QSpacerItem(0, 275, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Impostazione layout totale
        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Pista')

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
        back_img = QImage("Pista/data/Sarnano_Sassotetto.jpg")
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
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))

    def show_pulsantiera(self):

        # Punsante indietro
        layout_pulsanti = QHBoxLayout()
        pulsante_indietro = QPushButton("INDIETRO")
        pulsante_indietro.setFont(QFont('Times New Roman', 18))
        pulsante_indietro.setFixedSize(250, 100)
        pulsante_indietro.clicked.connect(self.indietro)
        layout_pulsanti.addSpacerItem(QSpacerItem(50, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        layout_pulsanti.addWidget(pulsante_indietro)
        layout_pulsanti.addSpacerItem(QSpacerItem(50, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale2.addLayout(layout_pulsanti)