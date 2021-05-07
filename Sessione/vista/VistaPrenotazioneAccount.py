from PyQt5.QtGui import QFont, QImage, QPalette, QBrush
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, \
    QPushButton
from PyQt5.QtCore import Qt
from Sessione.controller.controller_sessione import controller_account_loggato


class vista_prenotazione_account(QWidget):

    def __init__(self, callback):
        super(vista_prenotazione_account, self).__init__()
        self.controller = controller_account_loggato()
        self.callback = callback
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        self.controller = controller_account_loggato()
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        back_img = QImage("ListaAccount/data/im.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel("PRENOTAZIONI ACCOUNT")
        titolo.setAlignment(Qt.AlignCenter)
        self.cambia_font(60, titolo)
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.v_layout.addWidget(titolo)
        self.v_layout.addSpacerItem(QSpacerItem(0, 80, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # label
        if self.controller.get_lista_prenotazioni() == None:
            self.label = QLabel("Nessuna prenotazione")
        else:
            self.label = QLabel(self.controller.get_lista_prenotazioni())

        self.label.setAlignment(Qt.AlignCenter)
        self.v_layout.addSpacerItem(QSpacerItem(500, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.v_layout.addWidget(self.cambia_font(30, self.label))
        self.v_layout.addSpacerItem(QSpacerItem(0, 300, QSizePolicy.Fixed, QSizePolicy.Fixed))


        self.h_layout.addSpacerItem(QSpacerItem(700, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        indietro = QPushButton("INDIETRO")
        self.cambia_font(30, indietro)
        indietro.setFixedSize(400, 150)
        indietro.clicked.connect(self.indietro)
        self.h_layout.addWidget(indietro)

        self.h_layout.addSpacerItem(QSpacerItem(700, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addSpacerItem(QSpacerItem(0, 100, QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.setLayout(self.v_layout)

    def indietro(self):
        self.callback()
        self.close()

    def cambia_font(self, numero, label):
        label.setFont(QFont('Times New Roman', numero))
        return label