from PyQt5.QtGui import QPalette, QBrush, QImage, QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QSizePolicy, QSpacerItem, \
    QDesktopWidget, QHBoxLayout
from PyQt5.QtCore import Qt

from ListaPiste.vista.VistaListaPiste import vista_piste
from Sessione.vista.VistaAccountLoggato import vista_account_loggato


class vista_accesso(QWidget):

    def __init__(self, controller):
        super(vista_accesso, self).__init__()
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        self.v_layout = QVBoxLayout()
        self.controller = controller

        #Titolo
        titolo = QLabel("SARNANO NEVE")
        titolo.setAlignment(Qt.AlignCenter)
        self.cambia_font(60, titolo)
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.v_layout.addSpacerItem(QSpacerItem(0, 5, QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.v_layout.addWidget(titolo)
        self.v_layout.addSpacerItem(QSpacerItem(0, 5, QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.h1_layout = QHBoxLayout()
        info_account = self.crea_bottone("Account", self.h1_layout)
        info_account.clicked.connect(self.show_info_account)
        lista_piste = self.crea_bottone("Lista Piste", self.h1_layout)
        lista_piste.clicked.connect(self.show_lista_piste)
        prenota = self.crea_bottone("Prenota \n parcheggio", self.h1_layout)

        back_img = QImage("ListaAccount/data/im.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)


        self.h2_layout = QHBoxLayout()
        noleggia_attrezzatura = self.crea_bottone("Noleggia \n attrezzatura", self.h2_layout)
        skipass = self.crea_bottone("Acquista \n skipass", self.h2_layout)
        esci = self.crea_bottone("Esci", self.h2_layout)
        esci.clicked.connect(self.uscita)


        self.v_layout.addLayout(self.h1_layout)
        self.v_layout.addSpacerItem(QSpacerItem(0, 10, QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.v_layout.addLayout(self.h2_layout)
        self.v_layout.addSpacerItem(QSpacerItem(0, 5, QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.setLayout(self.v_layout)

    def cambia_font(self, numero, label):
        label.setFont(QFont('Times New Roman',numero))
        return label

    def crea_bottone(self, tipo, layout):
        bottone = QPushButton(tipo)
        bottone.setFixedSize(500,200)
        self.cambia_font(25, bottone)
        layout.addWidget(bottone)
        return bottone

    def show_lista_piste(self):
        self.vista_lista_piste = vista_piste(self.show)
        self.vista_lista_piste.showFullScreen()
        self.close()

    def show_info_account(self):
        self.vista_info_account = vista_account_loggato(self.show)
        self.vista_info_account.showFullScreen()
        self.close()

    def uscita(self):
        self.controller.salva_dati()
        self.close()