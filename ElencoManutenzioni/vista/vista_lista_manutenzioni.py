from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QBrush, QPalette, QImage, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, \
    QSizePolicy, QListView, QPushButton, QDesktopWidget, QAction, QMessageBox
from ElencoManutenzioni.controller.controlle_elenco_manutenzioni import controller_elenco_manutenzioni

from Manutenzioni.controller.controller_manutenzione import controller_manutenzione


class vista_lista_manutenzioni(QWidget):

    def __init__(self,callback):
        super(vista_lista_manutenzioni, self).__init__()

        # Attributi
        self.controller_elenco_manutenzioni = controller_elenco_manutenzioni()
        self.callback = callback
        self.vista_informazioni_manutenzione = vista_manutenzione
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.layout_verticale2 = QVBoxLayout()

        # Sfondo
        self.show_background("ELENCO MANUTENZIONI")


        self.layout_orizzontale.addSpacerItem(QSpacerItem(100, 0))

        # Lista
        self.vista_elenco = QListView()
        self.vista_elenco.setStyleSheet("background-color: cyan")
        vista_lista_model = QStandardItemModel(self.vista_elenco)
        for manutenzione in self.controller_elenco_manutenzioni.get_elenco_manutenzioni():
            item = QStandardItem()
            scadenza = manutenzione.get_prossima_scadenza()
            nome = manutenzione.get_nome()
            stringa = str(nome) + "  " + str(scadenza)
            item.setText(stringa)
            item.setEditable(False)
            item.setFont(QFont('Times New Roman', 25, 100))
            item.setTextAlignment(Qt.AlignCenter)
            vista_lista_model.appendRow(item)
        self.vista_elenco.setModel(vista_lista_model)
        self.layout_orizzontale.addWidget(self.vista_elenco)

        #self.layout_orizzontale.addSpacerItem(QSpacerItem(400, 0))

        # Pulsanti Apri e Indietro allineati
        self.show_pulsantiera()

        # Spaziatura
        self.layout_orizzontale.addLayout(self.layout_verticale2)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(150, 0))
        self.layout_verticale1.addLayout(self.layout_orizzontale)

        self.layout_verticale1.addSpacerItem(QSpacerItem(0,400))

        # Impostazione layout totale
        self.setLayout(self.layout_verticale1)
        self.setWindowTitle('Elenco Manutenzioni')

    def indietro(self):
        self.callback()
        self.controller_elenco_manutenzioni.salva_dati()
        self.close()

    def show_background(self, stringa):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("ElencoManutenzioni/data/sfondo.jpg")
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
        pulsante_apri.setFixedSize(250, 100)
        pulsante_apri.clicked.connect(self.manutenzione_selezionata)
        self.layout_verticale2.addWidget(pulsante_apri)


        # Punsante indietro
        pulsante_indietro = QPushButton("Indietro")
        pulsante_indietro.setFont(QFont('Times New Roman', 20, 100, True))
        pulsante_indietro.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante_indietro.setFixedSize(250, 100)
        pulsante_indietro.clicked.connect(self.indietro)
        self.layout_verticale2.addWidget(pulsante_indietro)
        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 50))

    def manutenzione_selezionata(self):
        try:
            selezionata = self.vista_elenco.selectedIndexes()[0].row()
            lista = self.controller_elenco_manutenzioni.get_elenco_manutenzioni()
            manutenzione = lista[selezionata]
            self.vista_informazioni_manutenzione = vista_manutenzione(manutenzione)
            self.vista_informazioni_manutenzione.show()
        except IndexError:
            QMessageBox.information(self, 'Attenzione!', 'Non hai selezionato nessuna manutenzione da visualizzare.',
                                    QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.critical(self, 'Errore!', 'Qualcosa è andato storto, riprova più tardi.',
                                 QMessageBox.Ok, QMessageBox.Ok)


class vista_manutenzione(QWidget):
    def __init__(self, manutenzione):
        super(vista_manutenzione, self).__init__()

        # Attributi
        self.controller_manutenzione = controller_manutenzione(manutenzione)
        self.layout_orizzontale = QHBoxLayout()
        self.layout_verticale = QVBoxLayout()
        self.setFixedSize(550, 280)

        # Visualizzazione manutenzione
        label = QLabel(self.controller_manutenzione.visualizza_manutenzione())
        label.setFont(QFont('Times New Roman', 20))
        label.setAlignment(Qt.AlignCenter)

        # Creazione bottone chiudi
        bottone = QPushButton("Chiudi")
        bottone.clicked.connect(self.call_chiudi)

        self.layout_verticale.addWidget(label)
        self.layout_verticale.addSpacerItem(QSpacerItem(150, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale.addWidget(bottone)
        self.layout_verticale.addLayout(self.layout_orizzontale)

        # Layout totale
        self.setLayout(self.layout_verticale)
        self.setWindowTitle("Informazioni manutenzione")

    def call_chiudi(self):
        self.close()