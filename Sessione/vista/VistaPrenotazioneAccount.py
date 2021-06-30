from PyQt5.QtGui import QFont, QImage, QPalette, QBrush, QStandardItemModel, QStandardItem, QColor
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, \
    QPushButton, QListView
from PyQt5.QtCore import Qt
from Sessione.controller.controllersessione import ControllerSessione

# Vista prenotazione account


class VistaPrenotazioneAccount(QWidget):

    def __init__(self, callback):
        super(VistaPrenotazioneAccount, self).__init__()

        # Controller associato alla vista
        self.controller = ControllerSessione()
        # Funzione che richiama la vista precendente
        self.callback = callback

        # Layout utilizzati per l'allineamento dei widget
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale1 = QHBoxLayout()
        self.layout_orizzontale2 = QHBoxLayout()

        # Funzione standard che imposta un titolo e uno sfondo alla vista
        self.show_background("PRENOTAZIONI ACCOUNT")

        # Lista delle prenotazioni effettuate
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(400, 0))
        self.lista_prenotazioni = QListView()

        # Riempimento della lista
        vista_lista_model = self.aggiorna()
        self.layout_orizzontale1.addWidget(vista_lista_model)
        self.layout_verticale.addLayout(self.layout_orizzontale1)

        # Spaziature
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(400, 0))
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 100))
        self.layout_orizzontale2.addSpacerItem(QSpacerItem(700, 0))

        # Configurazione e allineamento del pulsante indietro
        pulsante_indietro = QPushButton("INDIETRO")
        pulsante_indietro.setFont(QFont('Times New Roman', 30))
        pulsante_indietro.setStyleSheet("background-color: orange")
        pulsante_indietro.setFixedSize(400, 150)
        pulsante_indietro.clicked.connect(self.indietro)
        self.layout_orizzontale2.addWidget(pulsante_indietro)
        self.layout_orizzontale2.addSpacerItem(QSpacerItem(700, 0))

        # Impostazione del layout totale
        self.layout_verticale.addLayout(self.layout_orizzontale2)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 100))
        self.setLayout(self.layout_verticale)

    # Metodo che, collegato al pulsante "INDIETRO", permette di tornare alla vista precedente
    def indietro(self):
        self.callback()
        self.close()

    # Creazione, settaggio e stile sfondo e titolo
    def show_background(self, stringa):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("Data/Immagini/VistaPrenotazioneAccount.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        titolo.setStyleSheet('color: black')
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale.addWidget(titolo)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))

    # Ritorna la lista delle prenotazioni aggiornata
    def aggiorna(self):
        vista_lista_model = QStandardItemModel(self.lista_prenotazioni)
        lista_prenotazioni = self.controller.get_lista_prenotazioni()
        if not lista_prenotazioni:
            label = QLabel("Non hai effetuato prenotazioni")
            label.setAlignment(Qt.AlignCenter)
            label.setFont(QFont('Times New Roman', 25, 100))
            label.setStyleSheet('QLabel {background-color: lightBlue; color: black;}')
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
            return label

        else:
            for prenotazione in self.controller.get_lista_prenotazioni():
                item = QStandardItem()
                nome = prenotazione.get_descrizione_oggetto()
                scadenza = prenotazione.get_scadenza()
                stringa = nome + "\nScadenza: " + str(scadenza)
                item.setForeground(QColor(237, 118, 14))  # imposta il colore alla scritta dell'item
                item.setText(stringa)
                item.setEditable(False)
                item.setFont(QFont('Times New Roman', 30, 100))
                vista_lista_model.appendRow(item)
            self.lista_prenotazioni.setModel(vista_lista_model)
            self.lista_prenotazioni.setStyleSheet("background-color: lightBlue")
            return self.lista_prenotazioni
