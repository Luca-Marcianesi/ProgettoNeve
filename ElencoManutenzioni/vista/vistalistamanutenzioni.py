from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QBrush, QPalette, QImage, QStandardItemModel, QStandardItem, QColor
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, \
    QSizePolicy, QListView, QPushButton, QDesktopWidget, QMessageBox
from ElencoManutenzioni.controller.controllerelencomanutenzioni import ControllerElencoManutenzioni
from datetime import date
from Manutenzioni.vista.VistaManutenzione import VistaManutenzione


# Vista lista manutenzioni
class VistaListaManutenzioni(QWidget):

    def __init__(self, callback):
        super(VistaListaManutenzioni, self).__init__()

        # Attributi
        self.controller_elenco_manutenzioni = ControllerElencoManutenzioni()
        self.callback = callback
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.layout_verticale2 = QVBoxLayout()

        # Sfondo
        self.show_background("ELENCO MANUTENZIONI")

        # Spaziatura
        self.layout_orizzontale.addSpacerItem(QSpacerItem(100, 0))

        # Lista
        self.vista_elenco = QListView()

        # Chiamata funzione aggiorna
        vista_lista_model = self.aggiorna()

        # Aggiunta al layout
        self.layout_orizzontale.addWidget(vista_lista_model)

        # Pulsanti Apri e Indietro allineati
        self.show_pulsantiera()

        # Spaziatura
        self.layout_orizzontale.addLayout(self.layout_verticale2)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(150, 0))
        self.layout_verticale1.addLayout(self.layout_orizzontale)

        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 400))

        # Impostazione layout totale
        self.setLayout(self.layout_verticale1)
        self.setWindowTitle('Elenco Manutenzioni')

    # Metodo aggiorna facciata
    def aggiorna(self):
        vista_lista_model = QStandardItemModel(self.vista_elenco)
        for manutenzione in self.controller_elenco_manutenzioni.get_elenco_manutenzioni():
            item = QStandardItem()
            oggi = date.today()
            scadenza = manutenzione.get_prossima_scadenza()
            nome = manutenzione.get_nome()
            stringa = str(nome)

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

    # Creazione, settaggio e stile dello sfondo
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
        titolo.setStyleSheet("color: white")
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addWidget(titolo)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 100, QSizePolicy.Fixed, QSizePolicy.Fixed))

    # Creazione, settaggio e stile dei pulsanti
    def show_pulsantiera(self):

        pulsante_apri = self.pulsante("Apri", self.manutenzione_selezionata)
        self.layout_verticale2.addWidget(pulsante_apri)

        # Punsante indietro
        pulsante_indietro = self.pulsante("Indietro", self.indietro)
        self.layout_verticale2.addWidget(pulsante_indietro)
        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 50))

    # Metodo per la creazione di un pulsante
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
