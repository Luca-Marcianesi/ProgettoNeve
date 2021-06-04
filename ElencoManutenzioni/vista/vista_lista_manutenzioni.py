from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QBrush, QPalette, QImage, QStandardItemModel, QStandardItem, QColor
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, \
    QSizePolicy, QListView, QPushButton, QDesktopWidget, QMessageBox
from ElencoManutenzioni.controller.controller_elenco_manutenzioni import ControllerElencoManutenzioni
from datetime import date
from Manutenzioni.vista.VistaManutenzione import VistaManutenzione


# Vista utile per la visualizzazione della lista delle manutenzioni
class VistaListaManutenzioni(QWidget):

    def __init__(self, callback):
        super(VistaListaManutenzioni, self).__init__()

        # Funzione di richiamo della vista precedente
        self.callback = callback

        # Controller dell'attrezzatura importante per effettuare le varie funzioni
        self.controller_elenco_manutenzioni = ControllerElencoManutenzioni()

        # Layout usati per visualizzare e allineare l'intera vista
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()

        # Lista manutenzioni
        self.vista_elenco = QListView()

        # Funzione standard che imposta uno sfondo immagine e un titolo nella attuale vista
        self.show_background("ELENCO MANUTENZIONI")

        # Spaziatura orizzontale
        self.layout_orizzontale.addSpacerItem(QSpacerItem(100, 0))

        # Creazione e allineamento lista delle manutenzioni aggiornata
        vista_lista_aggiornata = self.aggiorna()
        self.layout_orizzontale.addWidget(vista_lista_aggiornata)

        # Configurazione e allineamento dei pulsanti
        self.show_pulsantiera()
        self.layout_orizzontale.addSpacerItem(QSpacerItem(150, 0))

        # Configurazione finale del layout totale
        self.layout_verticale.addLayout(self.layout_orizzontale)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 400))
        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Elenco Manutenzioni')

    # Resetta la lista delle manutenzioni aggiungendo le eventuali modifiche, e gestione dei colori
    def aggiorna(self):
        vista_lista_model = QStandardItemModel(self.vista_elenco)
        for manutenzione in self.controller_elenco_manutenzioni.get_elenco_manutenzioni():
            item = QStandardItem()
            oggi = date.today()
            scadenza = manutenzione.get_prossima_scadenza()
            nome = manutenzione.get_nome()
            stringa = str(nome)
            # Colore della label cambia a seconda dell'urgenza della manutenzione
            if oggi > scadenza:
                item.setForeground(QColor(255, 0, 0))
                stringa += " [URGENTE]"
            if scadenza == oggi:
                item.setForeground(QColor(255, 200, 0))
            elif scadenza > oggi:
                item.setForeground(QColor(0, 255, 0))
            item.setText(stringa)
            item.setEditable(False)
            item.setFont(QFont('Times New Roman', 25, 100))
            item.setTextAlignment(Qt.AlignCenter)
            vista_lista_model.appendRow(item)
        self.vista_elenco.setModel(vista_lista_model)
        self.vista_elenco.setStyleSheet("background-color: black")
        return self.vista_elenco

    # Metodo che permette, cliccando il bottone "indietro", di tornare alla vista precedente
    def indietro(self):
        self.callback()
        self.controller_elenco_manutenzioni.salva_dati()
        self.close()

    # Impostazione dello sfondo e del titolo
    def show_background(self, stringa):
        # Settaggio e ridimensionamento dell'immagine di sfondo dell'attuale vista
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("Data/Immagini/VistaListaManutenzioni.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Settaggio e allineamento del titolo della vista
        titolo = QLabel(stringa)
        titolo.setStyleSheet("color: white")
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale.addWidget(titolo)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 100, QSizePolicy.Fixed, QSizePolicy.Fixed))

    # Metodo per creazione, stile e funzionamento dei bottoni indietro e apri
    def show_pulsantiera(self):
        # Layout interni utilizzati per l'allineamento dei tre pulsanti
        layout_pulsanti = QVBoxLayout()

        # Configurazione del pulsante Apri
        pulsante_apri = self.pulsante("Apri", self.manutenzione_selezionata)
        layout_pulsanti.addWidget(pulsante_apri)

        # Configurazione del pulsante Indietro
        pulsante_indietro = self.pulsante("Indietro", self.indietro)
        layout_pulsanti.addWidget(pulsante_indietro)

        # Inserimento e allineamento dei tre pulsanti del layout globale
        layout_pulsanti.addSpacerItem(QSpacerItem(0, 50))
        self.layout_orizzontale.addLayout(layout_pulsanti)

    # Metodo interno per standardizzare e semplificare la creazione di un pulsante
    def pulsante(self, nome, call):
        pulsante = QPushButton(nome)
        pulsante.setFont(QFont('Times New Roman', 20, 100, True))
        pulsante.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante.setFixedSize(250, 100)
        pulsante.clicked.connect(call)
        return pulsante

    # Metodo che controlla che venga selezionata una manutenzione al click di "apri"
    def manutenzione_selezionata(self):
        try:
            selezionata = self.vista_elenco.selectedIndexes()[0].row()
            lista = self.controller_elenco_manutenzioni.get_elenco_manutenzioni()
            manutenzione = lista[selezionata]
            self.vista_informazioni_manutenzione = VistaManutenzione(manutenzione,
                                                                     self.controller_elenco_manutenzioni.salva_dati,
                                                                     self.aggiorna)
            self.vista_informazioni_manutenzione.show()

        except IndexError:
            QMessageBox.information(self, 'Attenzione!', 'Non hai selezionato nessuna manutenzione da visualizzare.',
                                    QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.critical(self, 'Errore!', 'Qualcosa è andato storto, riprova più tardi.',
                                 QMessageBox.Ok, QMessageBox.Ok)
