from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QWidget, QHBoxLayout, QSpacerItem


# Vista che gestisce l'interfaccia grafica per la creazione di un account cliente
class VistaCreaAccount(QWidget):

    def __init__(self, callback, controller):
        super(VistaCreaAccount, self).__init__()

        # Funzione che richiama la vista precedente
        self.callback = callback

        # Controller relativo alla vista
        self.controller = controller

        # Dizionario utilizzato per la gestione dei paramentri inseriti nella casella di testo
        self.testo = {}

        # Dimensione della finestra
        self.setFixedWidth(800)
        self.setFixedHeight(600)

        # Layout utilizzati nella vista
        self.v_layout = QVBoxLayout()
        self.h_layout1 = QHBoxLayout()
        self.h_layout2 = QHBoxLayout()

        # Funzione standardizzata per la configurazione dello sfondo
        self.show_background()

        # Creazione, settaggio e stile tramite funzione interna della casella di testo in cui inserire le credenziali
        self.casella_testo("Nome")
        self.casella_testo("Cognome")
        self.casella_testo("Username")
        self.casella_testo("Password")
        self.casella_testo("Età")
        self.casella_testo("Altezza")
        self.casella_testo("Numero di scarpe")

        # Pulsante indietro che richiama la vista precedente
        indietro = QPushButton("INDIETRO")
        indietro.setFont(QFont('Times New Roman', 14, 100, True))
        indietro.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        indietro.setFixedSize(150, 70)
        indietro.clicked.connect(self.indietro)
        self.h_layout2.addWidget(indietro)

        # Pulsante invia che se il processo è andato a buon fine crea l'account con le credenziali inserite
        invio = QPushButton("INVIA")
        invio.setFont(QFont('Times New Roman', 14, 100, True))
        invio.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        invio.setFixedSize(150, 70)
        invio.clicked.connect(self.crea_account)
        self.h_layout2.addWidget(invio)

        # Settaggio e spaziatura del layout totale
        self.v_layout.addLayout(self.h_layout2)
        self.h_layout1.addSpacerItem(QSpacerItem(200, 0))
        self.h_layout1.addLayout(self.v_layout)
        self.h_layout1.addSpacerItem(QSpacerItem(200, 0))
        self.setLayout(self.h_layout1)
        self.setWindowTitle("Nuovo Account")

    # Metodo per la creazione di una label e la casella di testo sotto
    def casella_testo(self, tipo):
        label = QLabel(tipo + ":")
        label.setFont(QFont("Times New Roman", 14, 100))
        self.v_layout.addWidget(label)
        casella = QLineEdit()
        casella.setFont(QFont("Times New Roman", 12))
        self.v_layout.addWidget(casella)
        self.testo[tipo] = casella

    # Metodo per creare l'account con gestione eccezioni
    def crea_account(self):
        nome = self.testo["Nome"].text()
        cognome = self.testo["Cognome"].text()
        username = self.testo["Username"].text()
        password = self.testo["Password"].text()
        eta = self.testo["Età"].text()
        altezza = self.testo["Altezza"].text()
        n_scarpe = self.testo["Numero di scarpe"].text()
        try:
            if self.controlla_informazioni(nome, cognome, username, password, eta, altezza, n_scarpe):
                self.controller.crea_account(nome, cognome, username, password, eta, altezza, n_scarpe)
                self.controller.salva_dati()
                self.callback()
                self.close()
        except ValueError:
            QMessageBox.critical(self, 'Errore!', 'Hai inserito delle informazioni non valide!',
                                 QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.critical(self, 'Errore!', 'Qualcosa è andato storto, riprova più tardi.',
                                 QMessageBox.Ok, QMessageBox.Ok)

    # Metodo che, collegato al bottone "INDIETRO", permette di tornare alla vista precedente
    def indietro(self):
        self.callback()
        self.close()

    # Creazione, settaggio e stile dello sfondo
    def show_background(self):
        # Sfondo
        back_img = QImage("Data/Immagini/azzurro.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

    # Metodo che controlla la validità delle informazioni inserite dall'utente
    def controlla_informazioni(self, nome, cognome, username, password, eta, altezza, numero_scarpe):
        if self.controller.controlla_username(username):
            QMessageBox.critical(self, 'Errore', 'Mi dispiace, questo username è già in uso!', QMessageBox.Ok,
                                 QMessageBox.Ok)
            return False
        elif nome == "" and cognome == "" and username == "" and \
                password == "" and altezza == "" and eta == "" and numero_scarpe == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return False
        elif self.controller.controlla_caratteristiche_persona(altezza, eta, numero_scarpe) is False:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci delle informazioni reali!',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return False
        else:
            return True
