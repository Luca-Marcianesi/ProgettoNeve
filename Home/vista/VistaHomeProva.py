from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QDesktopWidget, QWidget, QSizePolicy, \
    QPushButton
from PyQt5.QtCore import Qt

class vista_home_prova(QWidget):
    def __init__(self):
        super(vista_home_prova, self).__init__()


        # Attributi
        self.layout_verticale = QVBoxLayout()

        # Impostazione Layout totale
        self.show_background("AUGURI INGEGNERE")
        self.layout_verticale.addWidget(self.pulsante_indietro())
        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Informazioni')

    # Impostazione dello sfondo
    def show_background(self, titolo):
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("Home/data/prova.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(titolo)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 40,100,True))
        titolo.setStyleSheet('color: red')
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        titolo.setAlignment(Qt.AlignCenter)
        self.layout_verticale.addWidget(titolo)

    # Pulsante indietro
    def pulsante_indietro(self):
        pulsante_indietro = QPushButton("INDIETRO")
        pulsante_indietro.setFont(QFont('Times New Roman', 20, 100, True))
        pulsante_indietro.setStyleSheet('background-color: orange')
        pulsante_indietro.setFixedSize(250, 100)
        pulsante_indietro.clicked.connect(self.indietro)
        return pulsante_indietro


    # Collegamento del pulsante indietro per tornare alla schermata precedente
    def indietro(self):
        self.close()

