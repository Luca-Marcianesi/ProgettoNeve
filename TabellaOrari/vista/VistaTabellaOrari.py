from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont, QStandardItem, QStandardItemModel, QColor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QDesktopWidget, QLabel, QSpacerItem, QTableWidget, QTableWidgetItem, \
    QHBoxLayout, QSizePolicy, QPushButton, QListView, QMessageBox, QAbstractItemDelegate, QAbstractItemView

from ElencoDipendenti.controller.controller_gestione_dipendenti import ControllerElencoDipendenti


class vista_tabella_orari(QWidget):
    def __init__(self, callback):
        super(vista_tabella_orari, self).__init__()

        self.callback = callback
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()

        self.show_background("TABELLA ORARI")
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(15)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.setHorizontalHeaderLabels(['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì',
                                                    'Venerdì', 'Sabato', 'Domenica'])
        self.tableWidget.horizontalHeader().setFont(QFont('Times New Roman', 15, 80))


        self.layout_orizzontale.addSpacerItem(QSpacerItem(50, 0))
        self.layout_orizzontale.addWidget(self.tableWidget)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(105, 0))
        self.layout_orizzontale.addLayout(self.show_pulsantiera())
        self.layout_orizzontale.addSpacerItem(QSpacerItem(50, 0))
        self.layout_verticale1.addLayout(self.layout_orizzontale)

        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 140))
        self.setLayout(self.layout_verticale1)


    # Impostazione dello sfondo
    def show_background(self, stringa):
        # Sfondo
        self.setFixedSize(QDesktopWidget().width(), QDesktopWidget().height())
        self.setStyleSheet("background-image: ListaAttrezzatura/data/1.jpg")
        immagine = QImage("ListaAttrezzatura/data/1.jpg")
        immagine = immagine.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(immagine))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 60))
        self.layout_verticale1.addWidget(titolo)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 100))

    # Metodo per creazione, stile e funzionamento dei bottoni indietro e prenota
    def show_pulsantiera(self):
        # Punsante indietro
        layout_pulsanti = QVBoxLayout()
        pulsante_indietro = QPushButton("Indietro")
        pulsante_indietro.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante_indietro.setFont(QFont('Times New Roman', 25, 100, True))
        pulsante_indietro.setFixedSize(250, 100)
        pulsante_indietro.clicked.connect(self.indietro)

        pulsante_aggiungi = QPushButton("Aggiungi\n Dipendente")
        pulsante_aggiungi.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante_aggiungi.setFont(QFont('Times New Roman', 25, 100, True))
        pulsante_aggiungi.setFixedSize(250, 100)
        pulsante_aggiungi.clicked.connect(self.aggiungi_dipendente)

        pulsante_rimuovi = QPushButton("Rimuovi\n Dipendente")
        pulsante_rimuovi.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante_rimuovi.setFont(QFont('Times New Roman', 25, 100, True))
        pulsante_rimuovi.setFixedSize(250, 100)
        pulsante_rimuovi.clicked.connect(self.rimuovi_dipendente)

        layout_pulsanti.addWidget(pulsante_aggiungi)
        layout_pulsanti.addWidget(pulsante_rimuovi)
        layout_pulsanti.addWidget(pulsante_indietro)
        return layout_pulsanti

    # Metodo che permette, cliccando il bottone "indietro", di tornare alla vista precedente
    def indietro(self):
        self.callback()
        self.close()

    def aggiungi_dipendente(self):
        riga = self.tableWidget.selectedIndexes()[0].row()
        colonna = self.tableWidget.selectedIndexes()[0].column()
        self.lista_dipendenti = vista_aggiungi(self.tableWidget, riga, colonna)
        self.lista_dipendenti.show()

    def rimuovi_dipendente(self):
        try:
            riga = self.tableWidget.selectedIndexes()[0].row()
            colonna = self.tableWidget.selectedIndexes()[0].column()
            vuoto = QTableWidgetItem()
            vuoto.setText("")
            self.tableWidget.setItem(riga, colonna, vuoto)

        except IndexError:
            QMessageBox.information(self, 'Attenzione!', 'Non hai selezionato nessun dipendente da visualizzare.',
                                    QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.critical(self, 'Errore!', 'Qualcosa è andato storto, riprova più tardi.',
                                 QMessageBox.Ok, QMessageBox.Ok)


class vista_aggiungi(QWidget):

    def __init__(self, tabella, riga, colonna):
        super(vista_aggiungi, self).__init__()

        self.setFixedSize(1000, 600)

        # Oggetti passati
        self.tabella = tabella
        self.riga = riga
        self.colonna = colonna

        # Controller
        self.controller_gestione_dipendenti = ControllerElencoDipendenti()

        # Layout
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.layout_verticale2 = QVBoxLayout()
        self.layout_pulsanti = QVBoxLayout()

        # Titolo e Background
        self.show_background("Elenco Dipendenti")

        # Spaziatura
        self.layout_orizzontale.addSpacerItem(QSpacerItem(100, 0))

        # Lista Dipendenti
        self.lista_dipendenti = QListView()

        vista_lista_model = self.aggiorna()

        self.layout_orizzontale.addWidget(vista_lista_model)

        # Spaziatura
        self.layout_orizzontale.addSpacerItem(QSpacerItem(50, 0))

        # Inserimento layout
        self.layout_verticale1.addLayout(self.layout_orizzontale)

        # Spaziatura
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50))

        # Mostra Pulsanti
        self.show_pulsantiera()

        # Spaziatura
        self.layout_orizzontale.addSpacerItem(QSpacerItem(50, 0))

        # Imposta il layout
        self.setLayout(self.layout_verticale1)

    # Mostra sfondo e titolo
    def show_background(self, stringa):
        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addWidget(titolo)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))

    # Mostra i pulsanti
    def show_pulsantiera(self):
        # Pulsante Aggiungi dipendente
        self.layout_verticale2.addWidget(self.pulsante("Aggiungi", self.call_aggiungi_dipendente))
        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 50))
        # Pulsante esci
        self.layout_verticale2.addWidget(self.pulsante("Esci", self.esci))
        self.layout_orizzontale.addLayout(self.layout_verticale2)

     # Crea un pulsante da titolo e gli associa una chiamata
    def pulsante(self, titolo, call):
        pulsante = QPushButton(titolo)
        pulsante.setFont(QFont('Times New Roman', 20, 100, True))
        pulsante.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante.setFixedSize(200, 50)
        pulsante.clicked.connect(call)
        return pulsante

    # Gestione eccezzione di non aver selezionato nessun dipendente da visualizzare
    def call_aggiungi_dipendente(self):
        try:
            selezionato = self.lista_dipendenti.selectedIndexes()[0].row()
            lista = self.controller_gestione_dipendenti.get_lista_elenco_dipendenti()
            dipendente = lista[selezionato]
            persona = QTableWidgetItem()
            persona.setFont(QFont('Times New Roman', 13, 80))
            persona.setText(dipendente.get_dipendente_str())
            self.tabella.setItem(self.riga, self.colonna, persona)
            self.close()
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
            item.setFont(QFont('Times New Roman', 20, 100))
            vista_lista_model.appendRow(item)
        self.lista_dipendenti.setModel(vista_lista_model)
        return self.lista_dipendenti

    # Chiamata indietro
    def esci(self):
        self.close()
