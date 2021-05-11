from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QSizePolicy, QSpacerItem, \
    QMessageBox
from ListaAccount.controller.controller_lista_account import controller_lista_account
from Home.vista.VistraHome import vista_home

from ListaAccount.vista.VistaCreaAccount import vista_crea_account


class vista_login(QWidget):

    def __init__(self,  parent=None):
        super(vista_login, self).__init__(parent)

        # Attributi
        self.controller_lista_account = controller_lista_account()
        self.credenziali = {}
        self.layout_verticale1 = QVBoxLayout()
        self.layout_verticale2 = QVBoxLayout()
        self.layout_orizzontale1 = QHBoxLayout()
        self.layout_orizzontale2 = QHBoxLayout()

        # Sfondo
        self.show_background("SARNANO NEVE")

        # Spaziatura tra lato sinitro e caselle
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(200, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Caselle username e password
        self.casella_testo("USERNAME")
        casella_ps = self.casella_testo("PASSWORD")
        casella_ps.setEchoMode(QLineEdit.Password)

        # Spaziatura tra caselle e pulsanti
        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))

        #Accedi
        accedi = QPushButton("ACCEDI")
        accedi.setFixedSize(150,70)
        self.cambia_font(12, accedi)
        self.layout_orizzontale2.addWidget(accedi)
        accedi.clicked.connect(self.entra)

        #Crea Account
        crea_account = QPushButton("CREA \n ACCOUNT")
        crea_account.setFixedSize(150,70)
        self.cambia_font(12, crea_account)
        self.layout_orizzontale2.addWidget(crea_account)
        crea_account.clicked.connect(self.crea)
        self.layout_verticale2.addLayout(self.layout_orizzontale2)

        # Allineamento layout orizzontale1
        self.layout_orizzontale1.addLayout(self.layout_verticale2)
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(200, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addLayout(self.layout_orizzontale1)

        self.setLayout(self.layout_verticale1)
        self.setWindowTitle("Login")

    def crea(self):
        self.crea_view = vista_crea_account(self.show, self.controller_lista_account)
        self.crea_view.show()
        self.close()

    def cambia_font(self, numero, label):
        label.setFont(QFont('Times New Roman',numero))
        return label

    def entra(self):
        username = self.credenziali["USERNAME"].text()
        password = self.credenziali["PASSWORD"].text()
        if self.controller_lista_account.login(username, password):
            self.accesso_view = vista_home(self.controller_lista_account.salva_dati)
            self.accesso_view.showFullScreen()
            self.close()
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',QMessageBox.Ok, QMessageBox.Ok)

    def casella_testo(self, tipo):
        # Label
        label = QLabel(tipo + ":")
        label.setFont(QFont('Times New Roman', 25))
        label.setAlignment(Qt.AlignCenter)
        self.layout_verticale2.addWidget(label)

        #Casella di testo
        casella = QLineEdit()
        font = casella.font()
        font.setPointSize(10)
        casella.setFont(font)
        self.layout_verticale2.addWidget(casella)
        self.credenziali[tipo] = casella
        return casella

    def show_background(self, stringa):
        # Sfondo
        self.setFixedWidth(800)
        self.setFixedHeight(600)
        back_img = QImage("ListaAccount\data\img.png")
        img = back_img.scaled(800, 600)
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 40))
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addWidget(titolo)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 80, QSizePolicy.Fixed, QSizePolicy.Fixed))