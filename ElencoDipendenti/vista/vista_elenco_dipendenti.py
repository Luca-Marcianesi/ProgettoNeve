from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QImage, QBrush, QFont, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QDesktopWidget, QLabel, QSpacerItem, QSizePolicy, QWidget, \
    QListView, QPushButton, QMessageBox
from ElencoDipendenti.controller.controller_gestione_dipendenti import ControllerElencoDipendenti
from ElencoDipendenti.vista.vista_informazioni_dipendente import VistaInformazioniDipendente
from ElencoDipendenti.vista.vista_aggiungi_dipendente import VistaAggiungiDipendente


# Vista per la visualizzazione della lista di tutti i dipendenti
class VistaElencoDipendenti(QWidget):

    def __init__(self, callback):
        super(VistaElencoDipendenti, self).__init__()

        # Funzione di richiamo della vista precedente
        self.callback = callback

        # Controller dell'attrezzatura importante per effettuare le varie funzioni interne
        self.controller_gestione_dipendenti = ControllerElencoDipendenti()

        # Layout usati per visualizzare e allineare l'intera vista
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()

        # Lista Dipendenti
        self.lista_dipendenti = QListView()
        self.label = QLabel()

        # Definizione della vista successiva
        self.vista_aggiungi = VistaAggiungiDipendente(self.showFullScreen, self.controller_gestione_dipendenti,
                                                      self.aggiorna)
        # Funzione standard che imposta uno sfondo immagine e un titolo nella attuale vista
        self.show_background("Elenco Dipendenti")

        # Spaziatura orizzontale
        self.layout_orizzontale.addSpacerItem(QSpacerItem(300, 0))

        # Creazione e allineamento lista dei dipendenti aggiornata
        self.show_pulsantiera()
        self.aggiorna()
        self.layout_orizzontale.addWidget(self.lista_dipendenti)
        self.layout_orizzontale.addWidget(self.label)

        # Configurazione e allineamento dei pulsanti
        self.layout_orizzontale.addSpacerItem(QSpacerItem(300, 0))
        self.layout_orizzontale.addLayout(self.layout_pulsanti)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(200, 0))

        # Configurazione finale del layout totale
        self.layout_verticale.addLayout(self.layout_orizzontale)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 200))
        self.setLayout(self.layout_verticale)

    # Impostazione dello sfondo e del titolo
    def show_background(self, stringa):
        # Settaggio e ridimensionamento dell'immagine di sfondo dell'attuale vista
        self.setFixedSize(QDesktopWidget().width(), QDesktopWidget().height())
        immagine = QImage("Data/Immagini/ListaAttrezzatura.jpg")
        immagine_scalata = immagine.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(immagine_scalata))
        self.setPalette(palette)

        # Settaggio e allineamento del titolo della vista
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale.addWidget(titolo)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 100, QSizePolicy.Fixed, QSizePolicy.Fixed))

    # Metodo per creazione, stile e funzionamento dei bottoni indietro, apri e aggiungi dipendente
    def show_pulsantiera(self):
        # Layout interni utilizzati per l'allineamento dei tre pulsanti
        self.layout_pulsanti = QVBoxLayout()

        # Configurazione del pulsante Apri
        self.pulsante_apri = self.pulsante("Apri", self.dipendente_selezionato)
        self.layout_pulsanti.addWidget(self.pulsante_apri)
        self.layout_pulsanti.addSpacerItem(QSpacerItem(0, 50))

        # Configurazione del pulsante Aggiungi Dipendente
        self.layout_pulsanti.addWidget(self.pulsante("Aggiungi\nDipendente", self.call_aggiungi_dipendente))
        self.layout_pulsanti.addSpacerItem(QSpacerItem(0, 50))

        # Configurazione del pulsante Indietro
        self.layout_pulsanti.addWidget(self.pulsante("Indietro", self.indietro))

    # Metodo interno per standardizzare e semplificare la creazione di un pulsante
    def pulsante(self, titolo, call):
        pulsante = QPushButton(titolo)
        pulsante.setFont(QFont('Times New Roman', 20, 100, True))
        pulsante.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante.setFixedSize(250, 100)
        pulsante.clicked.connect(call)
        return pulsante

    # Metodo utile per la selezione e la relativa visualizzazione delle informazioni dipendente
    def dipendente_selezionato(self):
        try:
            selezionato = self.lista_dipendenti.selectedIndexes()[0].row()
            lista = self.controller_gestione_dipendenti.get_elenco_dipendenti()
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

    # Resetta la lista dei dipendenti aggiungendo le eventuali modifiche
    def aggiorna(self):
        vista_lista_model = QStandardItemModel(self.lista_dipendenti)
        if not bool(self.controller_gestione_dipendenti.get_elenco_dipendenti()):
            self.layout_orizzontale.removeWidget(self.lista_dipendenti)
            self.lista_dipendenti.deleteLater()
            self.lista_dipendenti = None
            self.layout_pulsanti.removeWidget(self.pulsante_apri)
            self.pulsante_apri.deleteLater()
            self.pulsante_apri = None
            self.label.setText("Non ci sono più dipendenti")
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setFont(QFont('Times New Roman', 25, 100))
            self.label.setStyleSheet('QLabel {background-color: lightBlue; color: black;}')
            self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
            self.layout_orizzontale.addSpacerItem(QSpacerItem(0, 50))

        else:
            for dipendente in self.controller_gestione_dipendenti.get_elenco_dipendenti():
                item = QStandardItem()
                nome = dipendente.get_dipendente_str()
                item.setText(nome)
                item.setEditable(False)
                item.setFont(QFont('Times New Roman', 30, 100))
                vista_lista_model.appendRow(item)
            self.lista_dipendenti.setModel(vista_lista_model)

    # Metodo per la chiamata della vista aggiungi dipendente
    def call_aggiungi_dipendente(self):
        self.vista_aggiungi.show()

    # Metodo che permette di ritornare alla finestra precedente
    def indietro(self):
        self.callback()
        self.close()
