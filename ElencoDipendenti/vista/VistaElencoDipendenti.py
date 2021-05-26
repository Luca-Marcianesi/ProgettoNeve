from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QImage, QBrush, QFont, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QDesktopWidget, QLabel, QSpacerItem, QSizePolicy, QWidget, \
    QListView, QPushButton, QMessageBox

from ElencoDipendenti.controller.controller_gestione_dipendenti import ControllerElencoDipendenti
from ElencoDipendenti.vista.vista_informazioni_dipendente import VistaInformazioniDipendente
from ElencoDipendenti.vista.vistaaggiungidipendente import VistaAggiungiDipendente

# vista elenco dipendenti


class VistaElencoDipendenti(QWidget):

    def __init__(self, callback):
        super(VistaElencoDipendenti, self).__init__()

        # Controller
        self.controller_gestione_dipendenti = ControllerElencoDipendenti()

        # Layout
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.layout_verticale2 = QVBoxLayout()
        self.layout_pulsanti = QVBoxLayout()

        # Callback
        self.callback = callback

        # Viste Collegate
        self.vista_aggiungi = VistaAggiungiDipendente(self.showFullScreen, self.controller_gestione_dipendenti,
                                                      self.aggiorna)

        # Titolo e Background
        self.show_background("Elenco Dipendenti")

        # Spaziatura
        self.layout_orizzontale.addSpacerItem(QSpacerItem(300, 0))

        # Lista Dipendenti
        self.lista_dipendenti = QListView()

        vista_lista_model = self.aggiorna()

        self.layout_orizzontale.addWidget(vista_lista_model)

        # Spaziatura
        self.layout_orizzontale.addSpacerItem(QSpacerItem(300, 0))

        # Inserimento layout
        self.layout_verticale1.addLayout(self.layout_orizzontale)

        # Spaziatura
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 200))

        # Mostra Pulsanti
        self.show_pulsantiera()

        # Spaziatura
        self.layout_orizzontale.addSpacerItem(QSpacerItem(200, 0))

        # Imposta il layout
        self.setLayout(self.layout_verticale1)

    # Mostra sfondo e titolo
    def show_background(self, stringa):

        # Background
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("Data/Immagini/ListaAttrezzatura.jpg")
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

    # Mostra i pulsanti
    def show_pulsantiera(self):

        # Pulsante apri
        self.layout_verticale2.addWidget(self.pulsante("Apri", self.dipendente_selezionato))
        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 50))

        # Pulsante Aggiungi dipendente
        self.layout_verticale2.addWidget(self.pulsante("Aggiungi\nDipendente", self.call_aggiungi_dipendente))
        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 50))

        # Pulsante indietro
        self.layout_verticale2.addWidget(self.pulsante("Indietro", self.indietro))
        self.layout_orizzontale.addLayout(self.layout_verticale2)

    # Crea un pulsante da titolo e gli associa una chiamata
    def pulsante(self, titolo, call):

        pulsante = QPushButton(titolo)
        pulsante.setFont(QFont('Times New Roman', 20, 100, True))
        pulsante.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante.setFixedSize(250, 100)
        pulsante.clicked.connect(call)
        return pulsante

    # Gestione eccezzione di non aver selezionato nessun dipendente da visualizzare
    def dipendente_selezionato(self):
        try:
            selezionato = self.lista_dipendenti.selectedIndexes()[0].row()
            lista = self.controller_gestione_dipendenti.get_lista_elenco_dipendenti()
            dipendente = lista[selezionato]
            self.vista_informazioni = VistaInformazioniDipendente(dipendente,
                                                                  self.controller_gestione_dipendenti.rimuovi,
                                                                  self.controller_gestione_dipendenti.salva_dati,
                                                                  self.aggiorna)
            self.vista_informazioni.show()
        except IndexError:
            QMessageBox.information(self, 'Attenzione!', 'Non hai selezionato nessun dipendente da visualizzare.',
                                    QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.critical(self, 'Errore!', 'Qualcosa è andato storto, riprova più tardi.',
                                 QMessageBox.Ok, QMessageBox.Ok)

    # Ritorna la lista dei dipendenti
    def aggiorna(self):
        vista_lista_model = QStandardItemModel(self.lista_dipendenti)
        for dipendente in self.controller_gestione_dipendenti.get_lista_elenco_dipendenti():
            item = QStandardItem()
            nome = dipendente.get_dipendente_str()
            item.setText(nome)
            item.setEditable(False)
            item.setFont(QFont('Times New Roman', 30, 100))
            vista_lista_model.appendRow(item)
        self.lista_dipendenti.setModel(vista_lista_model)
        return self.lista_dipendenti

    # Chiamata aggiungi dipendente
    def call_aggiungi_dipendente(self):
        self.vista_aggiungi.show()

    # Chiamata indietro
    def indietro(self):
        self.callback()
        self.close()
