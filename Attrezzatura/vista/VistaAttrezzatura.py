from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem,\
    QDesktopWidget, QLabel, QPushButton, QMessageBox
from Attrezzatura.controller.controller_attrezzatura import ControllerAttrezzatura
from Sessione.model.sessione import Sessione


# VistaAttrezzatura eseguita in seguito della selezione nella prorpia lista
class VistaAttrezzatura(QWidget):
    def __init__(self, callback, attrezzatura, prenota_attrezzatura, aggiorna):
        super(VistaAttrezzatura, self).__init__()

        # Funzione utile per l'aggiornamento della vista precedente dopo la modifica
        self.aggiorna = aggiorna
        # Funzione di richiamo della vista precedente
        self.callback = callback
        # Funzione che permette di prenotare l'attrezzatura visualizzata nell'elenco attrezzatura
        self.prenota = prenota_attrezzatura
        # Oggetto selezionato nella vista precedente
        self.attrezzatura = attrezzatura

        # Controller dell'attrezzatura importante per effettuare le varie funzioni interne
        self.controller = ControllerAttrezzatura(self.attrezzatura)

        # Layout usati per visualizzare e allineare l'intera vista
        self.layout_verticale2 = QVBoxLayout()
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()

        # Funzione standard che imposta uno sfondo immagine e un titolo nella attuale vista
        self.show_background("ATTREZZATURA")

        # Spaziatura orizzontale
        self.layout_orizzontale.addSpacerItem(QSpacerItem(500, 0))

        # Allineamento e settaggio della Label che descrive le principali caratteristiche dell'attrezzatura
        label = QLabel("Nome: {}".format(self.controller.get_nome()) + "\n"
                       "Lunghezza: {}".format(self.controller.get_dimensioni()) + " cm" + "\n"
                       "Stato: {}".format(self.stato_attrezzatura()))
        label.setFont(QFont('Times New Roman', 30, 75))
        label.setStyleSheet("background-image:url(Data/Immagini/legno.jpg)")
        label.setAlignment(Qt.AlignCenter)
        label.setFixedSize(700, 200)
        self.layout_verticale2.addWidget(label)

        # Spaziatura verticale
        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 100))

        # Funzione che si occupa di settare e allineare i pulsanti "Indietro" e "Prenota"
        self.show_pulsantiera()

        # Impostazione e allineamento del layout totale
        self.layout_orizzontale.addLayout(self.layout_verticale2)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(500, 0))
        self.layout_verticale1.addLayout(self.layout_orizzontale)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 250))
        self.setLayout(self.layout_verticale1)

    # Metodo che permette, cliccando il bottone "Indietro", di tornare alla vista precedente
    def indietro(self):
        self.callback()
        self.close()

    # Impostazione dello sfondo e del titolo
    def show_background(self, stringa):
        # Settaggio e ridimensionamento dell'immagine di sfondo dell'attuale vista
        self.setFixedSize(QDesktopWidget().width(), QDesktopWidget().height())
        immagine = QImage("Data/Immagini/VistaAttrezzatura.jpg")
        immagine_scalata = immagine.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(immagine_scalata))
        self.setPalette(palette)

        # Settaggio e allineamento del titolo della vista
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 60))
        self.layout_verticale1.addWidget(titolo)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 150))

    # Metodo per creazione, stile e funzionamento dei bottoni indietro e prenota
    def show_pulsantiera(self):
        # Layout interni utilizzati per l'allineamento dei due pulsanti
        layout_pulsanti1 = QVBoxLayout()
        layout_pulsanti2 = QHBoxLayout()

        # Configurazione del pulsante Indietro
        pulsante_indietro = QPushButton("Indietro")
        pulsante_indietro.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante_indietro.setFont(QFont('Times New Roman', 30, 100, True))
        pulsante_indietro.setFixedSize(300, 100)
        pulsante_indietro.clicked.connect(self.indietro)

        # Configurazione del pulsante Prenota
        pulsante_prenota = QPushButton("Prenota")
        pulsante_prenota.setStyleSheet('QPushButton{background-color: orange; color: black;}')
        pulsante_prenota.setFont(QFont('Times New Roman', 30, 100, True))
        pulsante_prenota.setFixedSize(300, 100)
        pulsante_prenota.clicked.connect(self.prenotazione)

        # Inserimento dei due pulsanti dei layout interni
        layout_pulsanti1.addWidget(pulsante_prenota)
        layout_pulsanti1.addSpacerItem(QSpacerItem(0, 100))
        layout_pulsanti1.addWidget(pulsante_indietro)
        layout_pulsanti2.addLayout(layout_pulsanti1)

        # Inserimento dei due pulsanti del layout globale
        self.layout_verticale2.addLayout(layout_pulsanti2)

    # Metodo che controlla lo stato dell'attrezzatura
    def stato_attrezzatura(self):
        if self.controller.get_stato():
            return "Disponibile"
        return "Non disponibile"

    # Metodo per la prenotazione
    def prenotazione(self):
        risultato = self.prenota(self.attrezzatura)
        if risultato != "Prenotazione effettuata":
            risultato = "Hai già prenotato questa attrezzatura!"
        QMessageBox.information(self, "Esito", risultato, QMessageBox.Ok, QMessageBox.Ok)
        Sessione.salva_dati()
        self.aggiorna()
        self.callback()
        self.close()
