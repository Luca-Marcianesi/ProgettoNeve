import json
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QWidget, QHBoxLayout, QSpinBox, \
    QSizePolicy, QSpacerItem
from Attrezzatura.model.attrezzatura import Attrezzatura


# Vista usata per l'inserimento di una nuova attrezzatura da parte del proprietario
class VistaAggiungiAttrezzatura(QWidget):

    def __init__(self, callback, controller_lista_attrezzatura, aggiorna):
        super(VistaAggiungiAttrezzatura, self).__init__()

        # Funzione di richiamo della vista precedente
        self.callback = callback
        # Funzione utile per l'aggiornamento della vista precedente dopo la modifica
        self.aggiorna = aggiorna
        # Controller della lista attrezzatura importante per effettuare le varie funzioni interne
        self.controller_lista_attrezzatura = controller_lista_attrezzatura
        # Dizionario testo utile per conservare i vari paramentri digitati nella casella di testo
        self.testo = {}

        # Configurazione della dimensione e creazione dei layout principali della vista
        self.setFixedSize(1000, 800)
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale1 = QHBoxLayout()
        self.layout_orizzontale2 = QHBoxLayout()

        # Funzione standard che imposta uno sfondo immagine e un titolo nella attuale vista
        self.show_background("AGGIUNGI ATTREZZATURA")

        # Label per la descrizione della casella di testo
        label_nome = QLabel("Nome:")
        label_nome.setFont(QFont('Times New Roman', 20, 100))
        self.layout_verticale.addWidget(label_nome)

        # Casella di testo per l'inserimento del nome
        self.casella = QLineEdit()
        self.layout_orizzontale2.addWidget(self.casella)
        self.layout_orizzontale2.addSpacerItem(QSpacerItem(500, 0))
        self.layout_verticale.addLayout(self.layout_orizzontale2)

        # Label per la visualizzazione dei codici utilizzati nella lista attrezzatura
        codici = QLabel()
        codici.setText(self.leggi_codici_json())
        codici.setFont(QFont('Times New Roman', 15))
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 20))
        self.layout_verticale.addWidget(codici)

        # Label per la descrizione della SpinBox
        label_codici = QLabel("Codice Oggetto:")
        label_codici.setFont(QFont('Times New Roman', 20))
        label_codici.setSizePolicy(500, 500)
        self.layout_verticale.addWidget(label_codici)

        # QSpinBox per l'inserimento del codice identificativo
        self.spin_codice = QSpinBox(self)
        self.spin_codice.setFont(QFont('Times New Roman', 20))
        self.spin_codice.setAlignment(Qt.AlignCenter)
        self.spin_codice.setFixedSize(150, 70)
        self.spin_codice.lineEdit().setReadOnly(True)
        self.spin_codice.setRange(3,6)
        self.layout_verticale.addWidget(self.spin_codice)

        # Label per la descrizione della SpinBox
        label_dimensioni = QLabel("Dimensioni")
        label_dimensioni.setFont(QFont('Times New Roman', 20))
        label_dimensioni.setSizePolicy(500, 500)
        self.layout_verticale.addWidget(label_dimensioni)

        # QSpinBox per l'inserimento delle dimensioni dell'attrezzatura
        self.dimensioni = QSpinBox(self)
        self.dimensioni.setFont(QFont('Times New Roman', 20))
        self.dimensioni.setAlignment(Qt.AlignCenter)
        self.dimensioni.setFixedSize(150, 70)
        self.dimensioni.setRange(1, 200)
        self.layout_verticale.addWidget(self.dimensioni)

        # Funzione che si occupa di settare e allineare i pulsanti "Indietro" e "Aggiungi"
        self.show_pulsantiera()

        # Settaggio layout totale
        self.layout_verticale.addLayout(self.layout_orizzontale1)
        self.setLayout(self.layout_verticale)
        self.setWindowTitle("Nuova Attrezzatura")

    # Impostazione dello sfondo e del titolo
    def show_background(self, stringa):

        # Settaggio e ridimensionamento dell'immagine di sfondo dell'attuale vista
        back_img = QImage("Data/Immagini/azzurro.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Settaggio e allineamento del titolo della vista
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 40))
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 20))
        self.layout_verticale.addWidget(titolo)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 30))

    # Metodo per creazione, stile e funzionamento del bottone Aggiungi
    def show_pulsantiera(self):

        # Configurazione del pulsante Aggiungi
        invio = QPushButton("Aggiungi")
        invio.setFont(QFont('Times New Roman', 25, 100, True))
        invio.clicked.connect(self.aggiungi)
        invio.setFixedSize(200, 100)
        invio.setStyleSheet('background-color: orange')

        # Inserimento del pulsante del layout globale
        self.layout_orizzontale1.addWidget(invio)

    # Metodo utile per l'inserimento della nuova attrezzatura appena configurata
    def aggiungi(self):
        nome = self.casella.text()
        dimensioni = int(self.dimensioni.value())
        codice = self.spin_codice.value()
        if nome != "":
            self.controller_lista_attrezzatura.aggiungi_attrezzatura(Attrezzatura(codice, nome, dimensioni))
            self.controller_lista_attrezzatura.salva_dati()
            self.aggiorna()
            self.close()
            QMessageBox.information(self, '', 'Oggetto aggiunto.', QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.critical(self, 'Errore', 'Controlla le informazioni.', QMessageBox.Ok, QMessageBox.Ok)

    # Metodo per la visualizzazione dei codici indentificativi delle attrezzature standard
    def leggi_codici_json(self):
        with open("Data/data/codici.json") as file:
            file = json.load(file)
            stringa = ""
        for oggetto in file:
            stringa += oggetto["descrizione"]
        return stringa
