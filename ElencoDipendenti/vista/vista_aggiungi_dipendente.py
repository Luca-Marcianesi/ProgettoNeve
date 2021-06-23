from PyQt5.QtGui import QPalette, QBrush, QImage, QFont
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QSpacerItem
from Dipendenti.model.dipendente import Dipendente


# Vista utilizzata per l'inserimento di un nuovo dipendente
class VistaAggiungiDipendente(QWidget):

    def __init__(self, callback, controller, aggiorna):
        super(VistaAggiungiDipendente, self).__init__()

        # Funzione di richiamo della vista precedente
        self.callback = callback
        # Funzione utile per l'aggiornamento della vista precedente dopo la modifica
        self.aggiorna = aggiorna

        # Controller dell'elenco dipendenti importante per effettuare le diverse operazioni
        self.controller_elenco_dipendenti = controller

        # Impostazione le dimensioni della finestra
        self.setFixedSize(800, 600)

        # Layout usati per visualizzare e allineare l'intera vista
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale1 = QHBoxLayout()
        self.layout_orizzontale2 = QHBoxLayout()

        # Dizionario utilizzato per la collezione dei parametri digitati nelle caselle di testo
        self.testo = {}

        # Funzione standard che imposta uno sfondo immagine nella vista
        self.show_background()

        # Creazione caselle di testo per inserimento delle informazioni
        self.casella_testo("Nome")
        self.casella_testo("Cognome")
        self.casella_testo("Numero di telefono")

        # Creazione e configurazione del pulsante "Indietro"
        bottone_indietro = QPushButton("Indietro")
        bottone_indietro.setFont(QFont('Times New Roman', 18, 100, True))
        bottone_indietro.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        bottone_indietro.setFixedSize(150, 80)
        bottone_indietro.clicked.connect(self.indietro)
        self.layout_orizzontale2.addWidget(bottone_indietro)

        # Creazione e configurazione del pulsante "Invia"
        bottone_invio = QPushButton("Invia")
        bottone_invio.setFont(QFont('Times New Roman', 18, 100, True))
        bottone_invio.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        bottone_invio.setFixedSize(150, 80)
        bottone_invio.clicked.connect(self.call_aggiungi_dipendente)
        self.layout_orizzontale2.addWidget(bottone_invio)

        # Impostazione e allineamento del layout totale
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50))
        self.layout_verticale.addLayout(self.layout_orizzontale2)
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(200, 0))
        self.layout_orizzontale1.addLayout(self.layout_verticale)
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(200, 0))
        self.setLayout(self.layout_orizzontale1)
        self.setWindowTitle("Nuovo Dipendente")

    # Metodo interno utile per la semplificare la creazione di una casella di testo
    def casella_testo(self, tipo):
        label = QLabel(tipo + ":")
        label.setFont(QFont('Times New Roman', 18, 100))
        casella = QLineEdit()
        casella.setFont(QFont('Times New Roman', 14))
        self.testo[tipo] = casella
        self.layout_verticale.addWidget(label)
        self.layout_verticale.addWidget(casella)

    # Impostazione dello sfondo
    def show_background(self):
        # Settaggio e ridimensionamento dell'immagine di sfondo dell'attuale vista
        back_img = QImage("Data/Immagini/azzurro.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

    # Metodo che controlla che le stringhe, nell'aggiunta dipendente, non siano vuote
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
