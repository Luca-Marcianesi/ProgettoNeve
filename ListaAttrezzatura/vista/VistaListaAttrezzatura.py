from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QBrush, QPalette, QImage, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, \
    QSizePolicy, QListView, QPushButton, QDesktopWidget, QMessageBox

from Attrezzatura.vista.VistaAttrezzatura import VistaAttrezzatura
from ListaAttrezzatura.controller.controllerlistaattrezzatura import ControllerListaAttrezzatura

# Vista lista attrezzatura


class VistaListaAttrezzatura(QWidget):
    def __init__(self, callback):
        super(VistaListaAttrezzatura, self).__init__()

        # Controller dell'attrezzatura importante per effettuare le varie funzioni interne
        self.controller_lista_attrezzatura = ControllerListaAttrezzatura()
        # Funzione di richiamo della vista precedente
        self.callback = callback
        # Layout usati per visualizzare e allineare l'intera vista
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.layout_verticale2 = QVBoxLayout()

        # Funzione standard che imposta uno sfondo immagine e un titolo nella attuale vista
        self.show_background("LISTA ATTREZZATURA")

        # Spaziature
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 200))
        self.layout_orizzontale.addSpacerItem(QSpacerItem(200, 0))

        # Widget della lista delle attrezzature
        self.vista_lista = QListView()
        # Label che si occupa di comunicare al cliente che non ci sono attrezzature disponibili
        self.label = QLabel()

        # Funzione che si occupa di settare e allineare i pulsanti "Indietro" e "Prenota"
        self.show_pulsantiera()

        # Funzione che riempie la lista con le attrezzature corrispondenti al cliente
        self.aggiorna()

        # Settaggio e allineamento dei widget ai layout
        self.layout_orizzontale.addWidget(self.vista_lista)
        self.layout_orizzontale.addWidget(self.label)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(800, 0))
        self.layout_orizzontale.addLayout(self.layout_verticale2)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(150, 0))
        self.layout_verticale1.addLayout(self.layout_orizzontale)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 300))

        # Impostazione layout totale
        self.setLayout(self.layout_verticale1)

    # Metodo che, collegato al pulsante "INDIETRO", permette di tornare alla vista precedente
    def indietro(self):
        self.callback()
        self.close()

    # Creazione, settaggio e stile dello sfondo
    def show_background(self, stringa):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("Data/Immagini/imagine.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50))
        self.layout_verticale1.addWidget(titolo)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 100))

    # Creazione, settaggio e stile pulsante "Apri"
    def show_pulsantiera(self):
        self.pulsante_apri = QPushButton("Apri")
        self.pulsante_apri.setFont(QFont('Times New Roman', 20, 100, True))
        self.pulsante_apri.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        self.pulsante_apri.setFixedSize(250, 100)
        self.pulsante_apri.clicked.connect(self.attrezzatura_selezionata)
        self.layout_verticale2.addWidget(self.pulsante_apri)

        # Pulsante indietro
        pulsante_indietro = QPushButton("Indietro")
        pulsante_indietro.setFont(QFont('Times New Roman', 20, 100, True))
        pulsante_indietro.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante_indietro.setFixedSize(250, 100)
        pulsante_indietro.clicked.connect(self.indietro)
        self.layout_verticale2.addWidget(pulsante_indietro)
        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 50))

    # Metodo che si occupa dell'accesso alla vista attrezzatura relativa all'attrezzatura selezionata
    def attrezzatura_selezionata(self):
        try:
            selezionata = self.vista_lista.selectedIndexes()[0].row()
            lista = self.controller_lista_attrezzatura.get_lista_filtrata()
            attrezzatura = lista[selezionata]
            self.vista_attrezzatura = VistaAttrezzatura(self.showFullScreen,
                                                        attrezzatura,
                                                        self.controller_lista_attrezzatura.prenota_attrezzatura,
                                                        self.aggiorna)
            self.vista_attrezzatura.showFullScreen()
            self.close()
        except IndexError:
            QMessageBox.information(self, 'Attenzione!', 'Non hai selezionato nessuna attrezzatura.', QMessageBox.Ok,
                                    QMessageBox.Ok)
        except:
            QMessageBox.critical(self, 'Errore!', 'Qualcosa è andato storto, riprova più tardi.', QMessageBox.Ok,
                                 QMessageBox.Ok)

    # Metodo che si occupa del riempimento della lista attrezzatura
    def aggiorna(self):
        vista_lista_model = QStandardItemModel(self.vista_lista)
        # Se la lista è vuota
        if not bool(self.controller_lista_attrezzatura.get_lista_filtrata()):
            # Rimozione dei pulsanti
            self.layout_orizzontale.removeWidget(self.vista_lista)
            self.vista_lista.deleteLater()
            self.vista_lista = None
            self.layout_verticale2.removeWidget(self.pulsante_apri)
            self.pulsante_apri.deleteLater()
            self.pulsante_apri = None

            self.label.setText("Non ci sono oggetti disponibili adatti\nalle tue caratteristiche")
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setFont(QFont('Times New Roman', 25, 100))
            self.label.setStyleSheet('QLabel {background-color: lightBlue; color: black;}')
            self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
            self.layout_orizzontale.addSpacerItem(QSpacerItem(0, 50))

        else:
            for attrezzatura in self.controller_lista_attrezzatura.get_lista_filtrata():
                item = QStandardItem()
                nome = attrezzatura.get_nome()
                item.setText(nome)
                item.setEditable(False)
                item.setFont(QFont('Times New Roman', 30, 100))
                vista_lista_model.appendRow(item)
            self.vista_lista.setModel(vista_lista_model)
