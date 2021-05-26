from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QWidget, QHBoxLayout


# vista Crea account
class VistaCreaAccount(QWidget):

    def __init__(self, callback, controller):
        super(VistaCreaAccount, self).__init__()

        # Definizione degli attributi
        self.callback = callback
        self.controller = controller
        self.testo = {}
        self.setFixedWidth(800)
        self.setFixedHeight(600)
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()

        # Chiamata alla funzione per lo sfondo
        self.show_background()

        # Creazione, settaggio e stile pulsante indietro, invia e parametri account
        self.casella_testo("Nome")
        self.casella_testo("Cognome")
        self.casella_testo("Username")
        self.casella_testo("Password")
        self.casella_testo("Età")
        self.casella_testo("Altezza")
        self.casella_testo("Numero di scarpe")

        indietro = QPushButton("Indietro")
        indietro.clicked.connect(self.indietro)
        self.h_layout.addWidget(indietro)

        invio = QPushButton("Invia")
        invio.clicked.connect(self.crea_account)
        self.h_layout.addWidget(invio)

        # Settaggio layout
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Account")

    # Creazione casella di testo
    def casella_testo(self, tipo):
        label = QLabel(tipo + ":")
        font = label.font()
        font.setPointSize(14)
        label.setFont(font)
        self.v_layout.addWidget(label)
        casella = QLineEdit()
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
