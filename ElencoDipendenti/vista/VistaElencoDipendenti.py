from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QImage, QBrush, QFont, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QDesktopWidget, QLabel, QSpacerItem, QSizePolicy, QWidget, \
    QListView

from ElencoDipendenti.controller.controller_gestione_dipendenti import controller_elenco_dipendenti


class vista_elenco_dipendenti(QWidget):
    def __init__(self):
        super(vista_elenco_dipendenti, self).__init__()

        #Attributi
        #self.callback = callback
        self.controller_gestione_dipendenti = controller_elenco_dipendenti()
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.layout_pulsanti = QVBoxLayout()
        self.vista_lista = QListView()

        #Titolo e Background
        self.show_background("Elenco Dipendenti")


        #Spaziatura
        self.layout_orizzontale.addSpacerItem(QSpacerItem(50, 0))


        #Lista
        vista_lista_model = QStandardItemModel(self.vista_lista)
        for dipendente in self.controller_gestione_dipendenti.get_lista_elenco_dipendenti():
            item = QStandardItem()
            nome = dipendente.get_dipendente_str()
            item.setText(nome)
            item.setEditable(False)
            item.setFont(QFont('Times New Roman', 30, 100))
            vista_lista_model.appendRow(item)
        self.vista_lista.setModel(vista_lista_model)
        self.layout_orizzontale.addWidget(self.vista_lista)

        self.layout_orizzontale.addSpacerItem(QSpacerItem(100,0))


        self.layout_verticale1.addLayout(self.layout_orizzontale)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0,100))
        self.setLayout(self.layout_verticale1)


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