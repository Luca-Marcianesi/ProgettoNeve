from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QLabel, QSpacerItem, QSizePolicy, QWidget, QHBoxLayout, QVBoxLayout

from Manutenzioni.controller.controller_manutenzione import controller_manutenzione


class vista_manutenzione(QWidget):
    def __init__(self, manutenzione):
        super(vista_manutenzione, self).__init__()

        # Attributi
        self.controller_manutenzione = controller_manutenzione(manutenzione)
        self.layout_orizzontale = QHBoxLayout()
        self.layout_verticale = QVBoxLayout()
        self.setFixedSize(550, 280)

        # Visualizzazione manutenzione
        label = QLabel(self.controller_manutenzione.visualizza_manutenzione())
        label.setFont(QFont('Times New Roman', 20))
        label.setAlignment(Qt.AlignCenter)

        # Creazione bottone chiudi
        bottone = QPushButton("Chiudi")
        bottone.clicked.connect(self.call_chiudi)

        self.layout_verticale.addWidget(label)
        self.layout_verticale.addSpacerItem(QSpacerItem(150, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale.addWidget(bottone)
        self.layout_verticale.addLayout(self.layout_orizzontale)

        # Layout totale
        self.setLayout(self.layout_verticale)
        self.setWindowTitle("Informazioni manutenzione")

    def call_chiudi(self):
        self.close()