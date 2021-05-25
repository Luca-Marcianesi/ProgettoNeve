from PyQt5.QtGui import QFont, QImage, QPalette, QBrush, QStandardItemModel, QStandardItem, QColor
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, \
    QPushButton, QListView
from PyQt5.QtCore import Qt
from Sessione.controller.controller_sessione import controller_sessione

# Vista prenotazione account
class vista_prenotazione_account(QWidget):

    def __init__(self, callback):
        super(vista_prenotazione_account, self).__init__()

        # Attributi
        self.controller = controller_sessione()
        self.callback = callback
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale1 = QHBoxLayout()
        self.layout_orizzontale2 = QHBoxLayout()

        # Sfondo
        self.show_background("PRENOTAZIONI ACCOUNT")

        self.layout_orizzontale1.addSpacerItem(QSpacerItem(400, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # label
        self.lista_prenotazioni = QListView()

        vista_lista_model = self.aggiorna()

        self.layout_orizzontale1.addWidget(vista_lista_model)

        self.layout_verticale.addLayout(self.layout_orizzontale1)

        # Spaziatura
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(400, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 100, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale2.addSpacerItem(QSpacerItem(700, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Pulsante indietro allineato
        pulsante_indietro = QPushButton("INDIETRO")
        pulsante_indietro.setFont(QFont('Times New Roman', 30))
        pulsante_indietro.setFixedSize(400, 150)
        pulsante_indietro.clicked.connect(self.indietro)
        self.layout_orizzontale2.addWidget(pulsante_indietro)
        self.layout_orizzontale2.addSpacerItem(QSpacerItem(700, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Conclusione

        self.layout_verticale.addLayout(self.layout_orizzontale2)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 100, QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.setLayout(self.layout_verticale)

    # Metodo che, collegato al pulsante "INDIETRO", permette di tornare alla vista precedente
    def indietro(self):
        self.callback()
        self.close()

    # Creazione, settaggio e stile sfondo
    def show_background(self, stringa):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("Data/Immagini/5.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale.addWidget(titolo)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Ritorna la lista delle prenotazioni
    def aggiorna(self):
        vista_lista_model = QStandardItemModel(self.lista_prenotazioni)
        if self.controller.get_lista_prenotazioni() == []:
            label = QLabel(" Non hai effetuato prenotazioni")
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
                item.setForeground(QColor(237, 118, 14))
                item.setText(stringa)
                item.setEditable(False)
                item.setFont(QFont('Times New Roman', 30, 100))
                vista_lista_model.appendRow(item)
            self.lista_prenotazioni.setModel(vista_lista_model)
            self.lista_prenotazioni.setStyleSheet("background-color: lightBlue")
            return self.lista_prenotazioni