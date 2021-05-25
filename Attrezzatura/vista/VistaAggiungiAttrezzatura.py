from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QWidget, QHBoxLayout, QSpinBox
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
        self.setFixedWidth(800)
        self.setFixedHeight(600)
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()

        # Chiamata alla funzione per lo sfondo
        self.show_background()

        #label = QLabel("Codici")

        label1 = QLabel("Codice Oggetto:")
        label1.setFont(QFont('Times New Roman', 10))
        label1.setSizePolicy(300, 300)

        self.codice = QSpinBox(self)
        self.codice.setFont(QFont('Times New Roman', 20))
        self.codice.setAlignment(Qt.AlignCenter)
        self.codice.setFixedSize(100, 50)
        self.codice.lineEdit().setReadOnly(True)
        self.codice.setRange(1, 5)

        label2 = QLabel("Dimensioni")
        label2.setFont(QFont('Times New Roman', 10))
        label2.setSizePolicy(300, 300)

        self.dimensioni = QSpinBox(self)
        self.dimensioni.setFont(QFont('Times New Roman', 20))
        self.dimensioni.setAlignment(Qt.AlignCenter)
        self.dimensioni.setFixedSize(100, 50)
        self.dimensioni.lineEdit().setReadOnly(True)
        self.dimensioni.setRange(1, 200)

        indietro = QPushButton("Indietro")
        indietro.clicked.connect(self.indietro)
        self.h_layout.addWidget(indietro)

        invio = QPushButton("Invia")
        invio.clicked.connect(self.crea_account)
        self.h_layout.addWidget(invio)

        # Settaggio layout
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuova Attrezzatura")

    # Creazione, settaggio e stile dello sfondo
    def show_background(self):
        # Sfondo
        back_img = QImage("Data/Immagini/azzurro.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

# Metodo che, collegato al bottone "INDIETRO", permette di tornare alla vista precedente
    def indietro(self):
        val = self.giorni.value()
        self.callback()
        self.close()

    def aggiungi(self):
        dimensioni = self.dimensioni.value()
        codice = self.codice.value()
        self.controller_lista_attrezzatura.aggiungi_attrezzatura(attrezzatura(codice,"",dimensioni))
        self.aggiorna()

