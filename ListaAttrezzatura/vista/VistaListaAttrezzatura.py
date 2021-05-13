from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QBrush, QPalette, QImage, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QListView, QPushButton, \
    QDesktopWidget

from ListaAttrezzatura.controller.controller_lista_attrezzatura import controller_lista_attrezzatura



class vista_lista_attrezzatura(QWidget):
    def __init__(self, callback):
        super(vista_lista_attrezzatura, self).__init__()


        # Attributi
        self.controller = controller_lista_attrezzatura()
        self.callback = callback
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.layout_verticale2 = QVBoxLayout()

        # Sfondo
        self.show_background("LISTA PISTE")

        # Lista
        vista_lista = QListView()
        vista_lista_model = QStandardItemModel(vista_lista)
        for attrezzatura in self.controller.get_lista_attrezzatura():
            item = QStandardItem()
            item.setText(attrezzatura.get_nome())
            item.setEditable(False)
            item.setFont(QFont('Times New Roman', 16))
            vista_lista_model.appendRow(item)
        vista_lista.setModel(vista_lista_model)
        self.layout_orizzontale.addWidget(vista_lista)

        # Pulsanti Apri e Indietro allineati
        self.show_pulsantiera()

        # Spaziatura
        self.layout_orizzontale.addSpacerItem(QSpacerItem(150, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addLayout(self.layout_orizzontale)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Impostazione layout totale
        self.setLayout(self.layout_verticale1)
        self.setWindowTitle('Lista Attrezzatura')

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
        back_img = QImage("ListaAttrezzatura/data/attrezzatura.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        #self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))
        #self.layout_verticale1.addWidget(titolo)
        #self.layout_verticale1.addSpacerItem(QSpacerItem(0, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))

    def show_pulsantiera(self):
        # Punsante indietro
        pulstante_indietro = QPushButton("INDIETRO")
        pulstante_indietro.setFont(QFont('Times New Roman', 18))
        pulstante_indietro.setFixedSize(250, 100)
        pulstante_indietro.clicked.connect(self.indietro)
        self.layout_verticale1.addWidget(pulstante_indietro)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 500, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale.addLayout(self.layout_verticale1)