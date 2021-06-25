from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, \
    QHBoxLayout, QSizePolicy, QSpacerItem, QMessageBox
from Home.vista.VistaHomeProprietrario import vista_home_proprietario
from ListaAccount.controller.controllerlistaaccount import ControllerListaAccount
from Home.vista.VistaHome import VistaHome
from ListaAccount.vista.VistaCreaAccount import VistaCreaAccount
from Sessione.model.sessione import Sessione


# vista login
class VistaLogin(QWidget):

    def __init__(self, parent=None):
        super(VistaLogin, self).__init__(parent)

        # Controller relativo alla vista
        self.controller = ControllerListaAccount()

        # Dizionario utilizzato per gestire i dati inseriti
        self.credenziali = {}

        # Viste successive
        self.accesso_proprietario = vista_home_proprietario(self.show)
        self.crea_view = VistaCreaAccount(self.show, self.controller)
        self.accesso_view = VistaHome(self.show)

        # Layout usati per allineare i widget della vista
        self.layout_verticale1 = QVBoxLayout()
        self.layout_verticale2 = QVBoxLayout()
        self.layout_orizzontale1 = QHBoxLayout()
        self.layout_orizzontale2 = QHBoxLayout()

        # Funzione standard per l'inserimendo dello sfondo e del titolo nella vista
        self.show_background("SARNANONEVE")

        # Spaziatura tra lato sinitro e caselle
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(200, 0))

        # Caselle username e password
        self.casella_testo("USERNAME")
        casella_ps = self.casella_testo("PASSWORD")
        # Istruzione per nascondere la digitura della password
        casella_ps.setEchoMode(QLineEdit.Password)

        # Spaziatura tra caselle e pulsanti
        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 50))

        # Allineamento e configurazione del pulsante accedi
        accedi = QPushButton("ACCEDI")
        accedi.setFixedSize(150, 70)
        accedi.setFont(QFont('Times New Roman', 14, 100, True))
        accedi.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        self.layout_orizzontale2.addWidget(accedi)
        accedi.clicked.connect(self.call_login)

        # Allineamento e configurazione del pulsante
        crea_account = QPushButton("CREA \n ACCOUNT")
        crea_account.setFixedSize(150, 70)
        crea_account.setFont(QFont('Times New Roman', 14, 100, True))
        crea_account.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        self.layout_orizzontale2.addWidget(crea_account)
        crea_account.clicked.connect(self.call_crea_account)
        self.layout_verticale2.addLayout(self.layout_orizzontale2)

        # Allineamento layout orizzontale1
        self.layout_orizzontale1.addLayout(self.layout_verticale2)
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(200, 0))
        self.layout_verticale1.addLayout(self.layout_orizzontale1)

        # Settaggio layout toale
        self.setLayout(self.layout_verticale1)
        self.setWindowTitle("Login")

    # Metodo, collegato al bottone, per creare l'account
    def call_crea_account(self):
        self.crea_view.show()
        self.close()

    # Metodo per effettuare il login con la differenziazione tra cliente e proprietario
    def call_login(self):
        username = self.credenziali["USERNAME"].text()
        password = self.credenziali["PASSWORD"].text()
        if self.controller.login(username, password):
            if Sessione.get_permessi():
                self.accesso_proprietario.showFullScreen()
                self.close()
            else:
                self.accesso_view.showFullScreen()
                self.close()
        else:
            QMessageBox.critical(self, 'Errore', 'Credenziali errate',
                                 QMessageBox.Ok, QMessageBox.Ok)

    # Metodo standard utile per la creazione della casella di testo
    def casella_testo(self, tipo):
        # Label sopra la casella di testo
        label = QLabel(tipo + ":")
        label.setFont(QFont('Times New Roman', 25))
        label.setAlignment(Qt.AlignCenter)
        self.layout_verticale2.addWidget(label)

        # Casella di testo
        casella = QLineEdit()
        font = casella.font()
        font.setPointSize(10)
        casella.setFont(font)
        self.layout_verticale2.addWidget(casella)
        self.credenziali[tipo] = casella
        return casella

    # Creazione, settaggio e stile dello sfondo
    def show_background(self, stringa):
        # Sfondo della vista
        self.setFixedWidth(800)
        self.setFixedHeight(600)
        back_img = QImage("Data/Immagini/VistaLogin.png")
        img = back_img.scaled(800, 600)
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo della finestra
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 40))
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 10, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addWidget(titolo)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 120, QSizePolicy.Fixed, QSizePolicy.Fixed))
