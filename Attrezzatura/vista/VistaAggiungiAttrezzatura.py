import json

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QWidget, QHBoxLayout, QSpinBox, \
    QSizePolicy, QSpacerItem
from Attrezzatura.model.attrezzatura import attrezzatura


# vista Crea account
class vista_aggiungi_attrezzatura(QWidget):

    def __init__(self, callback, controller,aggiorna):
        super(vista_aggiungi_attrezzatura, self).__init__()

        # Definizione degli attributi
        self.callback = callback
        self.aggiorna = aggiorna
        self.controller_lista_attrezzatura = controller
        self.testo = {}
        self.setFixedSize(1000,1000)
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()

        # Chiamata alla funzione per lo sfondo
        self.show_background()

        label = QLabel("Nome:")
        font = label.font()
        font.setPointSize(14)
        label.setFont(font)
        self.layout_verticale.addWidget(label)
        self.casella = QLineEdit()
        self.layout_verticale.addWidget(self.casella)

        codici = QLabel()
        codici.setText(self.leggi_codici_json())
        codici.setFont(QFont('Times New Roman', 15))


        label1 = QLabel("Codice Oggetto:")
        label1.setFont(QFont('Times New Roman', 20))
        label1.setSizePolicy(500, 500)

        self.codice = QSpinBox(self)
        self.codice.setFont(QFont('Times New Roman', 20))
        self.codice.setAlignment(Qt.AlignCenter)
        self.codice.setFixedSize(300, 150)
        self.codice.lineEdit().setReadOnly(True)
        self.codice.setRange(3, 20)

        label2 = QLabel("Dimensioni")
        label2.setFont(QFont('Times New Roman', 20))
        label2.setSizePolicy(500, 500)

        self.dimensioni = QSpinBox(self)
        self.dimensioni.setFont(QFont('Times New Roman', 20))
        self.dimensioni.setAlignment(Qt.AlignCenter)
        self.dimensioni.setFixedSize(300, 150)
        #self.dimensioni.lineEdit().setReadOnly(True)
        self.dimensioni.setRange(1, 200)

        self.layout_verticale.addWidget(label)
        self.layout_verticale.addWidget(codici)
        self.layout_verticale.addWidget(label1)
        self.layout_verticale.addWidget(self.codice)
        self.layout_verticale.addWidget(label2)
        self.layout_verticale.addWidget(self.dimensioni)

        indietro = QPushButton("Indietro")
        indietro.clicked.connect(self.indietro)
        indietro.setFixedSize(200,100)
        indietro.setStyleSheet('background-color: orange')
        self.layout_orizzontale.addWidget(indietro)

        invio = QPushButton("Aggiungi")
        invio.clicked.connect(self.aggiungi)
        invio.setFixedSize(200,100)
        invio.setStyleSheet('background-color: orange')
        self.layout_orizzontale.addWidget(invio)

        # Settaggio layout
        self.layout_verticale.addLayout(self.layout_orizzontale)
        self.setLayout(self.layout_verticale)
        self.setWindowTitle("Nuova Attrezzatura")

    # Creazione, settaggio e stile dello sfondo
    def show_background(self):
        # Sfondo
        back_img = QImage("Data/Immagini/azzurro.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        titolo = QLabel("AGGIUNGI ATTREZZATURA")
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 40))
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale.addWidget(titolo)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))

# Metodo che, collegato al bottone "INDIETRO", permette di tornare alla vista precedente
    def indietro(self):
        self.callback()
        self.close()

    def aggiungi(self):
        self.nome = self.casella.text()
        dimensioni = int(self.dimensioni.value())
        codice = self.codice.value()
        if self.nome != "":
            self.controller_lista_attrezzatura.aggiungi_attrezzatura(attrezzatura(codice,self.nome,dimensioni))
            self.aggiorna()
            QMessageBox.information(self, '', 'Oggetto aggiunto.', QMessageBox.Ok,QMessageBox.Ok)
        else :
            QMessageBox.critical(self, 'Errore', 'Controlla le informazioni.', QMessageBox.Ok, QMessageBox.Ok)

    def leggi_codici_json(self):
        with open("Data/data/codici.json") as file:
            file = json.load(file)
            stringa = ""
        for oggetto in file:
            stringa += oggetto["descrizione"]
        return stringa

