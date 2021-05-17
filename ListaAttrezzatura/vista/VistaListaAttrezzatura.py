from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QBrush, QPalette, QImage, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, \
    QSizePolicy, QListView, QPushButton, QDesktopWidget

from Attrezzatura.vista.VistaAttrezzatura import vista_attrezzatura
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
        self.show_background("LISTA ATTREZZATURA")

        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 200))

        self.layout_orizzontale.addSpacerItem(QSpacerItem(100, 0))

        # Lista
        self.vista_lista = QListView()
        vista_lista_model = QStandardItemModel(self.vista_lista)
        if self.controller.get_lista_filtrata() == []:
            label = QLabel(" Non ci sono oggetti disponibili adatti\nalle tue caratteristiche")
            label.setAlignment(Qt.AlignCenter)
            label.setFont(QFont('Times New Roman', 25, 100))
            label.setStyleSheet('QLabel {background-color: white; color: black;}')
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
            self.layout_orizzontale.addSpacerItem(QSpacerItem(0, 50))
            self.layout_orizzontale.addWidget(label)

        else:
            for attrezzatura in self.controller.get_lista_filtrata():
                item = QStandardItem()
                nome = attrezzatura.get_nome()
                item.setText(nome)
                item.setEditable(False)
                item.setFont(QFont('Times New Roman', 30, 100))
                vista_lista_model.appendRow(item)
            self.vista_lista.setModel(vista_lista_model)
            self.layout_orizzontale.addWidget(self.vista_lista)

        self.layout_orizzontale.addSpacerItem(QSpacerItem(1000, 0))

        # Pulsanti Apri e Indietro allineati
        self.show_pulsantiera()

        # Spaziatura
        self.layout_orizzontale.addSpacerItem(QSpacerItem(150, 0))
        self.layout_verticale1.addLayout(self.layout_orizzontale)

        if self.controller.get_lista_filtrata() == []:
            self.layout_verticale1.addSpacerItem(QSpacerItem(0, 350))
        else:
            self.layout_verticale1.addSpacerItem(QSpacerItem(0, 150))

        # Impostazione layout totale
        self.setLayout(self.layout_verticale1)
        self.setWindowTitle('Lista Attrezzatura')

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
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addWidget(titolo)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 100, QSizePolicy.Fixed, QSizePolicy.Fixed))

    def show_pulsantiera(self):
        if not self.controller.get_lista_filtrata() == []:
            pulsante_apri = QPushButton("Apri")
            pulsante_apri.setFont(QFont('Times New Roman', 20, 100, True))
            pulsante_apri.setStyleSheet('QPushButton {background-color: orange; color: black;}')
            pulsante_apri.setFixedSize(250, 100)
            pulsante_apri.clicked.connect(self.attrezzatura_selezionata)
            self.layout_verticale2.addWidget(pulsante_apri)
        # Punsante indietro
        pulsante_indietro = QPushButton("Indietro")
        pulsante_indietro.setFont(QFont('Times New Roman', 20, 100, True))
        pulsante_indietro.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante_indietro.setFixedSize(250, 100)
        pulsante_indietro.clicked.connect(self.indietro)
        self.layout_verticale2.addWidget(pulsante_indietro)
        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 50))
        self.layout_orizzontale.addLayout(self.layout_verticale2)

    def attrezzatura_selezionata(self):
        selezionata = self.vista_lista.selectedIndexes()[0].row()
        lista = self.controller.get_lista_filtrata()
        attrezzatura = lista[selezionata]
        self.vista_attrezzatura = vista_attrezzatura(self.showFullScreen, attrezzatura)
        self.vista_attrezzatura.showFullScreen()
        self.close()
