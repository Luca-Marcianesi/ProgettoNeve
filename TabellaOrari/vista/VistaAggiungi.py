from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QListView, QSpacerItem, QPushButton, QMessageBox, \
    QLabel, QWidget

from ElencoDipendenti.controller.controller_gestione_dipendenti import ControllerElencoDipendenti


class vista_aggiungi(QWidget):

    def __init__(self, tabella, riga, colonna, dipendenti_impiegati, aggiungi_lista, aggiorna):
        super(vista_aggiungi, self).__init__()
        self.setFixedSize(1000, 600)

        # Oggetti passati
        self.tabella = tabella
        self.riga = riga
        self.colonna = colonna
        self.aggiungi_lista = aggiungi_lista
        self.aggiorna = aggiorna
        self.dipendenti_impiegati = dipendenti_impiegati

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
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50))
        self.layout_verticale1.addWidget(titolo)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50))

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
        flag = True
        try:
            selezionato = self.lista_dipendenti.selectedIndexes()[0].row()
            lista = self.controller_gestione_dipendenti.get_elenco_dipendenti()
            dipendente = lista[selezionato]
            for impiegato in self.dipendenti_impiegati():
                if impiegato.get_dipendente_str() == dipendente.get_dipendente_str():
                    flag = False
                    QMessageBox.information(self, 'Attenzione!', 'Questo dipendente è già stato aggiunto',
                                            QMessageBox.Ok, QMessageBox.Ok)
            if flag:
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
        for dipendente in self.controller_gestione_dipendenti.get_elenco_dipendenti():
            item = QStandardItem()
            nome = dipendente.get_dipendente_str()
            item.setText(nome)
            item.setEditable(False)
            item.setFont(QFont('Times New Roman', 20, 100))
            vista_lista_model.appendRow(item)
        self.lista_dipendenti.setModel(vista_lista_model)
        self.lista_dipendenti.setStyleSheet("background-color: lightBlue")
        self.layout_orizzontale.addWidget(self.lista_dipendenti)

    # Chiamata indietro
    def esci(self):
        self.close()
