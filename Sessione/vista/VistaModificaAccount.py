from PyQt5.QtGui import QFont, QImage, QPalette, QBrush
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QWidget, \
    QHBoxLayout, QSizePolicy, QSpacerItem, QDesktopWidget
from PyQt5.QtCore import Qt
from Sessione.controller.controllersessione import ControllerSessione


# Vista modifica account
class VistaModificaAccount(QWidget):

    def __init__(self, aggiorna, callback):
        super(VistaModificaAccount, self).__init__()

        # Attributi
        self.aggiorna = aggiorna
        self.callback = callback
        self.controller_sessione = ControllerSessione()
        self.layout_verticale1 = QVBoxLayout()
        self.layout_verticale2 = QVBoxLayout()
        self.layout_orizzontale1 = QHBoxLayout()
        self.layout_orizzontale2 = QHBoxLayout()
        self.testo = {}

        # Sfondo
        self.show_background("MODIFICA LE \nCREDENZIALI")

        # Spaziatura
        self.layout_orizzontale2.addSpacerItem(QSpacerItem(700, 0))

        # Caselle di testo allineate
        self.casella_testo("PASSWORD")
        self.casella_testo("ETÀ")
        self.casella_testo("ALTEZZA")
        self.casella_testo("NUMERO DI SCARPE")

        # Spaziatura
        self.layout_orizzontale2.addLayout(self.layout_verticale2)
        self.layout_orizzontale2.addSpacerItem(QSpacerItem(700, 0))

        # Pulsanti Indietro e Invia
        self.show_pulsatiera()

        # Impostazione layout
        self.setLayout(self.layout_verticale1)
        self.setWindowTitle("Cambia Credenziali")

    # Creazione, settaggio, stile e aggiunta al layout dei pulsanti
    def show_pulsatiera(self):
        # Indietro
        pulsante_indietro = self.crea_bottone("INDIETRO", self.layout_orizzontale1)
        pulsante_indietro.clicked.connect(self.indietro)

        # Invio
        pulsante_invio = self.crea_bottone("INVIA", self.layout_orizzontale1)
        pulsante_invio.clicked.connect(self.cambia_dati)

        self.layout_verticale2.addLayout(self.layout_orizzontale1)
        self.layout_verticale1.addLayout(self.layout_orizzontale2)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 100))

    # Creazione, settaggio e stile caselle di testo
    def casella_testo(self, tipo):
        # Label
        label = QLabel(tipo + ":")
        label.setStyleSheet("color : orange ")
        label.setFont(QFont('Times New Roman', 30))
        label.setAlignment(Qt.AlignCenter)
        self.layout_verticale2.addWidget(label)

        # Casella di testo
        casella = QLineEdit()
        font = casella.font()
        font.setPointSize(15)
        casella.setFont(font)
        casella.setAlignment(Qt.AlignCenter)
        self.layout_verticale2.addWidget(casella)
        self.testo[tipo] = casella

    # Metodo cambia dati con gestione eccezioni
    def cambia_dati(self):
        password = self.testo["PASSWORD"].text()
        eta = self.testo["ETÀ"].text()
        altezza = self.testo["ALTEZZA"].text()
        numero_scarpe = self.testo["NUMERO DI SCARPE"].text()
        try:
            if self.controlla_informazioni(password, eta, altezza, numero_scarpe):
                self.controller_sessione.cambia_password(password)
                self.controller_sessione.cambia_eta(eta)
                self.controller_sessione.cambia_altezza(altezza)
                self.controller_sessione.cambia_numero_scarpe(numero_scarpe)
                self.controller_sessione.salva_dati()
                self.callback()
                self.aggiorna()
                self.close()
        except ValueError:
            QMessageBox.critical(self, 'Errore', 'Hai inserito delle informazioni non valide', QMessageBox.Ok,
                                 QMessageBox.Ok)
        except:
            QMessageBox.critical(self, 'Errore', 'Qualcosa è andato storto, riprova più tardi', QMessageBox.Ok,
                                 QMessageBox.Ok)

    # Metodo che, collegato al pulsante "INDIETRO", permette di tornare alla vista precedente
    def indietro(self):
        self.callback()
        self.close()

    # Creazione, settaggio e stile sfondo
    def show_background(self, stringa):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("Data/Immagini/VistaTabella.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60, 100))
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        titolo.setStyleSheet('QLabel {color: orange}')
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50))
        self.layout_verticale1.addWidget(titolo)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 150))

    # Metodo che crea un bottone generico
    def crea_bottone(self, tipo, layout):
        bottone = QPushButton(tipo)
        bottone.setFixedSize(300, 100)
        bottone.setFont(QFont('Times New Roman', 20, 100, True))
        bottone.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        layout.addWidget(bottone)
        return bottone

        # Metodo che controlla la validità delle informazioni inserite dall'utente
    def controlla_informazioni(self, password, eta, altezza, numero_scarpe):
        if password == "" and eta == "" and altezza == "" and numero_scarpe == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return False
        elif int(altezza) < 50 or int(altezza) > 220 or int(eta) <= 5 or int(eta) > 130 or int(numero_scarpe) <= 20 or\
                int(numero_scarpe) > 50:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci delle informazioni reali!', QMessageBox.Ok,
                                 QMessageBox.Ok)
            return False
        else:
            return True
