from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QImage, QBrush, QFont, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QDesktopWidget, QLabel, QSpacerItem, QSizePolicy, QWidget, \
    QListView, QPushButton, QMessageBox

from Dipendenti.controller.controller_dipendente import controller_dipendente
from ElencoDipendenti.controller.controller_gestione_dipendenti import controller_elenco_dipendenti


class vista_elenco_dipendenti(QWidget):
    def __init__(self, callback):
        super(vista_elenco_dipendenti, self).__init__()

        #Attributi
        self.callback = callback
        self.controller_gestione_dipendenti = controller_elenco_dipendenti()
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.layout_verticale2 = QVBoxLayout()
        self.layout_pulsanti = QVBoxLayout()
        self.vista_lista = QListView()

        #Titolo e Background
        self.show_background("Elenco Dipendenti")


        #Spaziatura
        self.layout_orizzontale.addSpacerItem(QSpacerItem(300, 0))


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

        self.layout_orizzontale.addSpacerItem(QSpacerItem(300,0))


        self.layout_verticale1.addLayout(self.layout_orizzontale)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0,200))

        self.show_pulsantiera()
        self.layout_orizzontale.addSpacerItem(QSpacerItem(200, 0))

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


    def show_pulsantiera(self):
        pulsante_apri = QPushButton("Apri")
        pulsante_apri.setFont(QFont('Times New Roman', 20, 100, True))
        pulsante_apri.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante_apri.clicked.connect(self.dipendente_selezionato)
        pulsante_apri.setFixedSize(250, 100)
        pulsante_indietro = QPushButton("Indietro")
        pulsante_indietro.setFont(QFont('Times New Roman', 20, 100, True))
        pulsante_indietro.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante_indietro.setFixedSize(250, 100)
        pulsante_indietro.clicked.connect(self.indietro)
        self.layout_verticale2.addWidget(pulsante_apri)
        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 50))
        self.layout_verticale2.addWidget(pulsante_indietro)
        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 500))
        self.layout_orizzontale.addLayout(self.layout_verticale2)

    def dipendente_selezionato(self):
        try:
            selezionato = self.vista_lista.selectedIndexes()[0].row()
            lista = self.controller_gestione_dipendenti.get_lista_elenco_dipendenti()
            dipendente = lista[selezionato]
            self.vista_informazioni = vista_informazioni(dipendente)
            self.vista_informazioni.show()
        except IndexError:
            QMessageBox.information(self, 'Attenzione!', 'Non hai selezionato nessun dipendente da visualizzare.', QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.critical(self, 'Errore!', 'Qualcosa è andato storto, riprova più tardi.', QMessageBox.Ok, QMessageBox.Ok)

    def indietro(self):
        self.callback()
        self.close()

class vista_informazioni(QWidget):
    def __init__(self, dipendente):
        super(vista_informazioni, self).__init__()
        self.layout_verticale = QVBoxLayout()
        self.controller_dipendente = controller_dipendente(dipendente)
        self.setFixedSize(400, 300)

        label = QLabel(self.controller_dipendente.get_dipendente_str_x_elenco())
        label.setFont(QFont('Times New Roman', 20))
        label.setAlignment(Qt.AlignCenter)

        bottone = QPushButton("Chiudi")
        bottone.clicked.connect(self.call_chiudi)

        self.layout_verticale.addWidget(label)
        self.layout_verticale.addSpacerItem(QSpacerItem(150, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale.addWidget(bottone)

        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Informazioni dipendente')

    def call_chiudi(self):
        self.close()







