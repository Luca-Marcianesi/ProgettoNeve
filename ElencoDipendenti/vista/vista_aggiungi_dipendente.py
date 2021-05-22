from PyQt5.QtGui import QPalette, QBrush, QImage
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget

from Dipendenti.model.dipendente import dipendente


class vista_aggiungi_dipendente(QWidget):

    def __init__(self, callback, controller):
        super(vista_aggiungi_dipendente, self).__init__()
        self.callback = callback
        self.controller = controller
        self.testo = {}
        self.setFixedWidth(800)
        self.setFixedHeight(600)
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()

        self.show_background()

        self.casella_testo("Nome")
        self.casella_testo("Cognome")
        self.casella_testo("Numero di telefono")

        indietro = QPushButton("Indietro")
        indietro.clicked.connect(self.indietro)
        self.h_layout.addWidget(indietro)

        invio = QPushButton("Invia")
        invio.clicked.connect(self.crea_account)
        self.h_layout.addWidget(invio)


        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Dipendente")

    def casella_testo(self, tipo):
        label = QLabel(tipo + ":")
        font = label.font()
        font.setPointSize(14)
        label.setFont(font)
        self.v_layout.addWidget(label)
        casella = QLineEdit()
        self.v_layout.addWidget(casella)
        self.testo[tipo] = casella

    def crea_account(self):
        nome = self.testo["Nome"].text()
        cognome = self.testo["Cognome"].text()
        numero_di_telefono = self.testo["Numero di telefono"].text()
        if self.controlla_informazioni1(nome, cognome,numero_di_telefono) :
            self.controller.aggiungi(dipendente(nome,cognome,numero_di_telefono))
            self.controller.salva_dati()
            self.callback()
            self.close()

    def show_background(self):
        # Sfondo
        back_img = QImage("Data/Immagini/azzurro.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

    def controlla_informazioni1(self, nome, cognome, numero_di_telefono):
        if nome != "" and cognome != "" and numero_di_telefono != "" :
             return True
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',QMessageBox.Ok, QMessageBox.Ok)
            return False
    def indietro(self):
        self.callback()
        self.close()