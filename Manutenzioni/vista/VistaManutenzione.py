from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QLabel, QSpacerItem, QSizePolicy, QWidget, QHBoxLayout, QVBoxLayout

from Manutenzioni.controller.controller_manutenzione import controller_manutenzione


class vista_manutenzione(QWidget):
    def __init__(self, manutenzione, salva_dati, aggiorna):
        super(vista_manutenzione, self).__init__()

        # Attributi
        self.salva_dati = salva_dati
        self.aggiorna_lista = aggiorna
        self.controller_manutenzione = controller_manutenzione(manutenzione)
        self.layout_orizzontale = QHBoxLayout()
        self.layout_verticale = QVBoxLayout()
        self.setFixedSize(550, 280)

        # Visualizzazione manutenzione
        self.label = QLabel(self.controller_manutenzione.visualizza_manutenzione())
        label = self.aggiorna()

        # Creazione bottone chiudi
        bottone = QPushButton("Chiudi")
        bottone.clicked.connect(self.call_chiudi)

        bottone1 = QPushButton("Effettua manutenzione")
        bottone1.clicked.connect(self.call_effettua)


        self.layout_verticale.addWidget(label)
        self.layout_verticale.addSpacerItem(QSpacerItem(150, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale.addWidget(bottone)
        self.layout_orizzontale.addWidget(bottone1)
        self.layout_verticale.addLayout(self.layout_orizzontale)

        # Layout totale
        self.setLayout(self.layout_verticale)
        self.setWindowTitle("Informazioni manutenzione")

    def call_chiudi(self):
        self.close()

    def aggiorna(self):
        self.label.setFont(QFont('Times New Roman', 20))
        self.label.setAlignment(Qt.AlignCenter)
        return self.label

    def call_effettua(self):
        self.controller_manutenzione.effettua_manutenzione()
        self.aggiorna()
        self.aggiorna_lista()
        self.salva_dati()
        self.close()


