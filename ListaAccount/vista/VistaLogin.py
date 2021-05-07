from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QSizePolicy, QSpacerItem, \
    QGridLayout, QMessageBox
from ListaAccount.controller.controller_lista_account import controller_lista_account
from ListaAccount.vista.VistaAccesso import vista_accesso
from ListaAccount.vista.VistaCreaAccount import vista_crea_account


class vista_login(QWidget):

    def __init__(self,  parent=None):
        super(vista_login, self).__init__(parent)
        self.controller = controller_lista_account()
        self.credenziali = {}
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        self.g_layout = QGridLayout()

        #Allignment and space
        self.setFixedWidth(800)
        self.setFixedHeight(600)
        back_img = QImage("ListaAccount\data\img.png")
        img = back_img.scaled(800, 600)
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)


        h_spacer = QSpacerItem(600, 50, QSizePolicy.Expanding, QSizePolicy.Expanding)
        v_spacer = QSpacerItem(600, 50, QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.g_layout.addItem(v_spacer, 0, 0)
        self.g_layout.addItem(h_spacer, 1, 0)
        self.g_layout.addItem(h_spacer, 1, 3)
        self.g_layout.addItem(v_spacer, 2, 0)

        titolo = QLabel("SARNANO NEVE")
        self.cambia_font(40, titolo)
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.v_layout.addWidget(titolo)
        self.v_layout.addSpacerItem(QSpacerItem(0,150,QSizePolicy.Expanding, QSizePolicy.Expanding))

        #LabelUsername
        u_label = QLabel("USERNAME")
        self.cambia_font(25, u_label)
        u_label.setAlignment(Qt.AlignCenter)
        u_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.v_layout.addWidget(u_label)

        #LineEditUsername
        casella_us = QLineEdit(self)
        casella_us.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.v_layout.addWidget(casella_us)
        self.credenziali["USERNAME"] = casella_us

        self.v_layout.addSpacerItem(QSpacerItem(0, 25, QSizePolicy.Fixed, QSizePolicy.Fixed))

        #LabelPassword
        p_label = QLabel("PASSWORD")
        self.cambia_font(25,p_label)
        p_label.setAlignment(Qt.AlignCenter)
        p_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.v_layout.addWidget(p_label)

        #LineEditPassword
        casella_pass = QLineEdit(self)
        casella_pass.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        casella_pass.setEchoMode(QLineEdit.Password)
        self.v_layout.addWidget(casella_pass)
        self.credenziali["PASSWORD"] = casella_pass

        self.v_layout.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))

        #Accedi
        accedi = QPushButton("ACCEDI")
        accedi.setFixedSize(150,70)
        self.cambia_font(12, accedi)
        self.h_layout.addWidget(accedi)
        accedi.clicked.connect(self.entra)

        #Crea Account
        crea_account = QPushButton("CREA \n ACCOUNT")
        crea_account.setFixedSize(150,70)
        self.cambia_font(12, crea_account)
        self.h_layout.addWidget(crea_account)
        crea_account.clicked.connect(self.crea)


        self.v_layout.addLayout(self.h_layout)
        self.g_layout.addLayout(self.v_layout, 1, 2)
        self.setLayout(self.g_layout)
        self.setWindowTitle("Login")


    def crea(self):
        self.crea_view = vista_crea_account(self.show, self.controller)
        self.crea_view.show()
        self.close()

    def cambia_font(self, numero, label):
        label.setFont(QFont('Times New Roman',numero))
        return label

    def entra(self):
        username = self.credenziali["USERNAME"].text()
        password = self.credenziali["PASSWORD"].text()
        if self.controller.login(username, password):
            self.accesso_view = vista_accesso(self.controller)
            self.accesso_view.showFullScreen()
            self.close()
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',QMessageBox.Ok, QMessageBox.Ok)
