from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QBrush, QPalette, QImage, QStandardItemModel, QStandardItem, QColor
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, \
    QListView, QPushButton, QDesktopWidget, QMessageBox
from Attrezzatura.vista.VistaAttrezzaturaProprietario import VistaAttrezzaturaProprietario
from ListaAttrezzatura.controller.controllerlistaattrezzatura import ControllerListaAttrezzatura
from Attrezzatura.vista.VistaAggiungiAttrezzatura import VistaAggiungiAttrezzatura


# Vista lista attrezzatura proprietario
class VistaListaAttrezzaturaProprietario(QWidget):
    def __init__(self, callback):
        super(VistaListaAttrezzaturaProprietario, self).__init__()

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
        self.layout_orizzontale.addSpacerItem(QSpacerItem(100, 0))

        # Widget lista
        self.vista_lista = QListView()
        # Label che illustra al cliente che non ci sono attrezzature disponibili
        self.label = QLabel()
        # Funzione che si occupa di settare e allineare i pulsanti "Indietro" e "Prenota"
        self.crea_pulsantiera()
        # Funzione che riempie la lista con l'attrezzatura o se vuota con un messaggio standard
        self.aggiorna()

        # Configurazione e allineamento dei widget ai layout
        self.layout_orizzontale.addWidget(self.vista_lista)
        self.layout_orizzontale.addWidget(self.label)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(500, 0))
        self.layout_orizzontale.addLayout(self.layout_verticale2)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(150, 0))
        self.layout_verticale1.addLayout(self.layout_orizzontale)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 200))

        # Impostazione layout totale
        self.setLayout(self.layout_verticale1)

    # Metodo che, collegato al pulsante "INDIETRO", permette di tornare alla vista precedente
    def indietro(self):
        self.callback()
        self.close()

    # Creazione, settaggio e stile dello sfondo e del titolo
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

    # Metodo che configura i pulsanti "indietro" e "aggiungi"
    def crea_pulsantiera(self):
        self.pulsante_apri = self.pulsante("Apri", self.attrezzatura_selezionata)
        self.layout_verticale2.addWidget(self.pulsante_apri)

        # Pulsante aggiungi
        pulsante_aggiungi = self.pulsante("Aggiungi\nattrezzatura", self.aggiungi)
        self.layout_verticale2.addWidget(pulsante_aggiungi)

        # Pulsante indietro
        pulsante_indietro = self.pulsante("Indietro", self.indietro)
        self.layout_verticale2.addWidget(pulsante_indietro)

    # Metodo che si occupa di riempire la lista con tutte le attrezzature
    def aggiorna(self):
        vista_lista_model = QStandardItemModel(self.vista_lista)
        if not bool(self.controller_lista_attrezzatura.get_lista_attrezzatura()):
            item = QStandardItem()
            item.setText("\nLista vuota\nInserire una nuova attrezzatura\n\n")
            item.setEditable(False)
            item.setTextAlignment(Qt.AlignCenter)
            item.setForeground(QColor(0, 0, 255))
            item.setFont(QFont('Times New Roman', 35, 100))
            vista_lista_model.appendRow(item)
            self.vista_lista.setModel(vista_lista_model)
        else:
            for attrezzatura in self.controller_lista_attrezzatura.get_lista_attrezzatura():
                item = QStandardItem()
                nome = attrezzatura.get_nome()
                if attrezzatura.get_stato():
                    item.setForeground(QColor(0, 255, 0))
                else:
                    item.setForeground(QColor(255, 0, 0))
                item.setText(nome)
                item.setEditable(False)
                item.setFont(QFont('Times New Roman', 30, 100))
                vista_lista_model.appendRow(item)
            self.vista_lista.setModel(vista_lista_model)

    # Metodo che gestisce l'apertura della vista attrezzatura relativa a quella selezionata
    def attrezzatura_selezionata(self):
        try:
            selezionata = self.vista_lista.selectedIndexes()[0].row()
            lista = self.controller_lista_attrezzatura.get_lista_attrezzatura()
            attrezzatura = lista[selezionata]
            self.vista_attrezzatura = VistaAttrezzaturaProprietario(
                self.showFullScreen, attrezzatura, self.controller_lista_attrezzatura.rimuovi_attrezzatura,
                self.aggiorna)
            self.vista_attrezzatura.showFullScreen()
        except IndexError:
            QMessageBox.information(self, 'Attenzione!', 'Non hai selezionato nessuna attrezzatura.', QMessageBox.Ok,
                                    QMessageBox.Ok)
        except:
            QMessageBox.critical(self, 'Errore!', 'Qualcosa è andato storto, riprova più tardi.', QMessageBox.Ok,
                                 QMessageBox.Ok)

    # Metodo per la creazione di un pulsante standard
    def pulsante(self, nome, call):
        pulsante = QPushButton(nome)
        pulsante.setFont(QFont('Times New Roman', 20, 100, True))
        pulsante.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante.setFixedSize(250, 100)
        pulsante.clicked.connect(call)
        return pulsante

    # Metodo per l'aggiunta di una nuova attrezzatura che poi è possibile prenotare
    def aggiungi(self):
        self.vista_aggiungi_attrezzatura = VistaAggiungiAttrezzatura(
            self.showFullScreen, self.controller_lista_attrezzatura, self.aggiorna)
        self.vista_aggiungi_attrezzatura.show()