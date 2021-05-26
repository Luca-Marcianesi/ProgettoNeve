from PyQt5.QtGui import QPalette, QBrush, QImage
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget

from Dipendenti.model.dipendente import Dipendente

# vista aggiungi dipendente


class VistaAggiungiDipendente(QWidget):

    def __init__(self, callback, controller, aggiorna):
        super(VistaAggiungiDipendente, self).__init__()

        # Callback
        self.callback = callback

        # Controller
        self.controller_elenco_dipendenti = controller

        # Funzione aggiorna elenco dipendenti
        self.aggiorna = aggiorna

        # Imposta le dimensioni della finestra
        self.setFixedSize(800, 600)

        # Layout
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()

        self.testo = {}

        # Mostra lo sfondo
        self.show_background()

        # Creazione caselle per inserimento info
        self.casella_testo("Nome")
        self.casella_testo("Cognome")
        self.casella_testo("Numero di telefono")

        # Bottone indietro
        indietro = QPushButton("Indietro")
        indietro.clicked.connect(self.indietro)
        self.h_layout.addWidget(indietro)

        # Bottone invia
        invio = QPushButton("Invia")
        invio.clicked.connect(self.call_aggiungi_dipendente)
        self.h_layout.addWidget(invio)

        # Inmpostazione layout
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Dipendente")

    # Creazione e inserimento casella di testo
    def casella_testo(self, tipo):

        label = QLabel(tipo + ":")
        font = label.font()
        font.setPointSize(14)
        label.setFont(font)
        self.v_layout.addWidget(label)
        casella = QLineEdit()
        self.v_layout.addWidget(casella)
        self.testo[tipo] = casella

    # Creazione e stile dello sfondo
    def show_background(self):
        # Sfondo
        back_img = QImage("Data/Immagini/azzurro.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

    # Metodo che controlla che non venga inserito niente nel momento dell'aggiunta dipendente
    def controlla_informazioni1(self, nome, cognome, numero_di_telefono):
        if str(nome) != "" and str(cognome) != "" and int(numero_di_telefono) != "":
            return True
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return False

    # Chiamata per aggiungere un dipendente
    def call_aggiungi_dipendente(self):
        nome = self.testo["Nome"].text()
        cognome = self.testo["Cognome"].text()
        numero_di_telefono = self.testo["Numero di telefono"].text()
        try:
            if self.controlla_informazioni1(nome, cognome, numero_di_telefono):
                self.controller_elenco_dipendenti.aggiungi(Dipendente(nome, cognome, numero_di_telefono))
                self.controller_elenco_dipendenti.salva_dati()
                self.aggiorna()
                self.callback()
                self.close()
        except ValueError:
            QMessageBox.critical(self, 'Errore', 'Hai inserito delle informazioni non valide.',
                                 QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.critical(self, 'Errore', 'Qualcosa è andato storto, riprova più tardi',
                                 QMessageBox.Ok, QMessageBox.Ok)

    # Metodo che permette, cliccando il bottone "indietro", di tornare alla vista precedente
    def indietro(self):
        self.callback()
        self.close()