from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QDesktopWidget, QLabel, QSpacerItem, QTableWidget, QTableWidgetItem, \
    QHBoxLayout, QPushButton, QMessageBox, QAbstractItemView

from TabellaOrari.controller.controller_tabella_orari import ControllerTabellaOrari
from TabellaOrari.vista.VistaAggiungi import vista_aggiungi


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
        self.tableWidget.horizontalHeader().setStyleSheet(" ::section {""background-color: orange; color: blue;}")
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setStyleSheet("background-color: lightBlue")
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
        titolo.setStyleSheet("color: orange")
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
            riga = self.tableWidget.selectedIndexes()[0].row()  # trova la riga selezionata
            colonna = self.tableWidget.selectedIndexes()[0].column()        # trova la colonna selezionata
            self.lista_dipendenti = vista_aggiungi(self.tableWidget, riga, colonna,
                                                   partial(self.controller_tabella_orari.get_dipendenti_impiegati,
                                                           colonna),
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
            self.tableWidget.setItem(riga, colonna, QTableWidgetItem())   # sovrascrivo con un item vuoto
            self.controller_tabella_orari.rimuovi_da_giorno(colonna, riga)  # rimuovo l'iteme vuoto
            self.controller_tabella_orari.salva_dati()
            self.aggiorna()
        except IndexError:
            QMessageBox.information(self, 'Attenzione!', 'Non hai selezionato nessun dipendente da eliminare.',
                                    QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.critical(self, 'Errore!', 'Qualcosa è andato storto, riprova più tardi.',
                                 QMessageBox.Ok, QMessageBox.Ok)

    def aggiorna(self):
        indice_giorni = len(self.controller_tabella_orari.get_tabella_orari())
        for colonna in range(indice_giorni):
            giorno = self.controller_tabella_orari.get_giorno_from_lista(colonna)
            indice_dipendenti = len(giorno.get_lista())
            for riga in range(15):
                if riga < indice_dipendenti:
                    dipendente = giorno.get_dipendente(riga)
                    item = QTableWidgetItem()
                    item.setText(dipendente.get_dipendente_str())
                    item.setTextAlignment(Qt.AlignCenter)
                    item.setFont(QFont('Times New Roman', 13, 70))
                    self.tableWidget.setItem(riga, colonna, item)
                else:
                    self.tableWidget.setItem(riga, colonna, QTableWidgetItem())
