from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QDesktopWidget, QLabel, QSpacerItem, QTableWidget, QTableWidgetItem, \
    QHBoxLayout, QSizePolicy, QPushButton, QListView, QMessageBox, QAbstractItemView
from ElencoDipendenti.controller.controller_gestione_dipendenti import ControllerElencoDipendenti
from TabellaOrari.controller.controller_tabella_orari import ControllerTabellaOrari


class VistaTabellaOrari(QWidget):
    def __init__(self, callback):
        super(VistaTabellaOrari, self).__init__()

        # Attributi
        self.controller_tabella_orari = ControllerTabellaOrari()
        self.callback = callback
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.tableWidget = QTableWidget()

        # Titolo e sfondo
        self.show_background("TABELLA ORARI")

        # Configurazione della tabella
        self.tableWidget.setRowCount(15)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.setHorizontalHeaderLabels(['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì',
                                                    'Venerdì', 'Sabato', 'Domenica'])
        self.tableWidget.horizontalHeader().setFont(QFont('Times New Roman', 15, 80))
        self.tableWidget.horizontalHeader().setStyleSheet("color: darkRed")
        self.tableWidget.verticalHeader().hide()
        self.aggiorna()

        # Allineamento e spaziatura layout orizzontale
        self.layout_orizzontale.addSpacerItem(QSpacerItem(50, 0))
        self.layout_orizzontale.addWidget(self.tableWidget)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(100, 0))
        self.layout_orizzontale.addLayout(self.show_pulsantiera())
        self.layout_orizzontale.addSpacerItem(QSpacerItem(85, 0))
        self.layout_verticale.addLayout(self.layout_orizzontale)

        # Spaziatura layout verticale
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 130))

        self.setLayout(self.layout_verticale)

    # Impostazione dello sfondo
    def show_background(self, stringa):
        # Sfondo
        self.setFixedSize(QDesktopWidget().width(), QDesktopWidget().height())
        immagine = QImage("Data/Immagini/VistaTabella.jpg")
        immagine_scalata = immagine.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(immagine_scalata))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 60))
        self.layout_verticale.addWidget(titolo)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 100))

    # Metodo per creazione, stile e funzionamento dei bottoni indietro, aggiungi dipendente e rimuovi dipendente
    def show_pulsantiera(self):
        # Punsante indietro
        layout_pulsanti = QVBoxLayout()
        pulsante_indietro = QPushButton("Indietro")
        pulsante_indietro.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante_indietro.setFont(QFont('Times New Roman', 25, 100, True))
        pulsante_indietro.setFixedSize(250, 100)
        pulsante_indietro.clicked.connect(self.indietro)

        # Punsante aggiungi dipendente
        pulsante_aggiungi = QPushButton("Aggiungi\n Dipendente")
        pulsante_aggiungi.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante_aggiungi.setFont(QFont('Times New Roman', 25, 100, True))
        pulsante_aggiungi.setFixedSize(250, 100)
        pulsante_aggiungi.clicked.connect(self.aggiungi_dipendente)

        # Punsante rimuovi dipendente
        pulsante_rimuovi = QPushButton("Rimuovi\n Dipendente")
        pulsante_rimuovi.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante_rimuovi.setFont(QFont('Times New Roman', 25, 100, True))
        pulsante_rimuovi.setFixedSize(250, 100)
        pulsante_rimuovi.clicked.connect(self.rimuovi_dipendente)

        # Settaggio dei pulsanti
        layout_pulsanti.addWidget(pulsante_aggiungi)
        layout_pulsanti.addWidget(pulsante_rimuovi)
        layout_pulsanti.addWidget(pulsante_indietro)
        return layout_pulsanti

    # Metodo che permette, cliccando il bottone "indietro", di tornare alla vista precedente
    def indietro(self):
        self.controller_tabella_orari.salva_dati()
        self.callback()
        self.close()

    def aggiungi_dipendente(self):
        try:
            riga = self.tableWidget.selectedIndexes()[0].row()
            colonna = self.tableWidget.selectedIndexes()[0].column()
            self.lista_dipendenti = vista_aggiungi(self.tableWidget, riga, colonna,
                                                   self.controller_tabella_orari.aggiungi_a_giorno, self.aggiorna)
            self.lista_dipendenti.show()
        except IndexError:
            QMessageBox.information(self, 'Attenzione!', 'Non hai selezionato nessuna casella.',
                                    QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.critical(self, 'Errore!', 'Qualcosa è andato storto, riprova più tardi.',
                                 QMessageBox.Ok, QMessageBox.Ok)

    def rimuovi_dipendente(self):
        try:
            riga = self.tableWidget.selectedIndexes()[0].row()
            colonna = self.tableWidget.selectedIndexes()[0].column()
            self.controller_tabella_orari.rimuovi_da_giorno(riga, colonna)
            vuoto = QTableWidgetItem()
            vuoto.setText("")
            self.tableWidget.setItem(riga, colonna, vuoto)

        except IndexError:
            QMessageBox.information(self, 'Attenzione!', 'Non hai selezionato nessun dipendente da eliminare.',
                                    QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.critical(self, 'Errore!', 'Qualcosa è andato storto, riprova più tardi.',
                                 QMessageBox.Ok, QMessageBox.Ok)

    def aggiorna(self):
        indice_giorni = len(self.controller_tabella_orari.get_lista_tabella_orari())
        for colonna in range(indice_giorni):
            giorno = self.controller_tabella_orari.get_giorno_from_lista(colonna)
            indice_dipendenti = len(giorno.get_lista())
            for riga in range(indice_dipendenti):
                    dipendente = giorno.get_dipendente(riga)
                    item = QTableWidgetItem()
                    item.setText(dipendente.get_dipendente_str())
                    item.setTextAlignment(Qt.AlignCenter)
                    item.setFont(QFont('Times New Roman', 13, 60))
                    self.tableWidget.setItem(riga, colonna, item)


class vista_aggiungi(QWidget):

    def __init__(self, tabella, riga, colonna, aggiungi_lista, aggiorna):
        super(vista_aggiungi, self).__init__()
        self.setFixedSize(1000, 600)

        # Oggetti passati
        self.tabella = tabella
        self.riga = riga
        self.colonna = colonna
        self.aggiungi_lista = aggiungi_lista
        self.aggiorna = aggiorna

        # Controller
        self.controller_gestione_dipendenti = ControllerElencoDipendenti()

        # Layout
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()

        # Titolo e sfondo
        self.show_background("Elenco Dipendenti")

        # Lista Dipendenti
        self.lista_dipendenti = QListView()

        # Spaziatura e settaggio del layout orizzontale
        self.layout_orizzontale.addSpacerItem(QSpacerItem(100, 0))
        self.show_lista()
        self.layout_orizzontale.addSpacerItem(QSpacerItem(50, 0))
        self.show_pulsantiera()
        self.layout_orizzontale.addSpacerItem(QSpacerItem(50, 0))
        self.layout_verticale1.addLayout(self.layout_orizzontale)

        # Spaziatura
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50))

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
        # Configurazioni iniziali
        font = QFont('Times New Roman', 20, 100, True)
        style = 'QPushButton {background-color: orange; color: black;}'
        layout_pulsanti = QVBoxLayout()

        # Pulsante Aggiungi dipendente
        pulsante_aggiungi = QPushButton("Aggiungi")
        pulsante_aggiungi.setFont(font)
        pulsante_aggiungi.setStyleSheet(style)
        pulsante_aggiungi.setFixedSize(200, 50)
        pulsante_aggiungi.clicked.connect(self.call_seleziona_dipendente)

        pulsante_esci = QPushButton("Esci")
        pulsante_esci.setFont(font)
        pulsante_esci.setStyleSheet(style)
        pulsante_esci.setFixedSize(200, 50)
        pulsante_esci.clicked.connect(self.esci)

        # Settaggio e allineamento pulsanti
        layout_pulsanti.addWidget(pulsante_aggiungi)
        layout_pulsanti.addSpacerItem(QSpacerItem(0, 50))
        layout_pulsanti.addWidget(pulsante_esci)
        self.layout_orizzontale.addLayout(layout_pulsanti)

    # Gestione eccezzione di non aver selezionato nessun dipendente da visualizzare
    def call_seleziona_dipendente(self):
        try:
            selezionato = self.lista_dipendenti.selectedIndexes()[0].row()
            lista = self.controller_gestione_dipendenti.get_lista_elenco_dipendenti()
            dipendente = lista[selezionato]
            self.aggiungi_lista(len(lista), self.colonna, dipendente)
            self.aggiorna()
            self.close()
        except IndexError:
            QMessageBox.information(self, 'Attenzione!', 'Non hai selezionato nessun dipendente da visualizzare.',
                                    QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.critical(self, 'Errore!', 'Qualcosa è andato storto, riprova più tardi.',
                                 QMessageBox.Ok, QMessageBox.Ok)

    # Ritorna la lista dei dipendenti
    def show_lista(self):
        vista_lista_model = QStandardItemModel(self.lista_dipendenti)
        for dipendente in self.controller_gestione_dipendenti.get_lista_elenco_dipendenti():
            item = QStandardItem()
            nome = dipendente.get_dipendente_str()
            item.setText(nome)
            item.setEditable(False)
            item.setFont(QFont('Times New Roman', 20, 100))
            vista_lista_model.appendRow(item)
        self.lista_dipendenti.setModel(vista_lista_model)
        self.layout_orizzontale.addWidget(self.lista_dipendenti)

    # Chiamata indietro
    def esci(self):
        self.close()
