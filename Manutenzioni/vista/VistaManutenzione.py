from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QLabel, QSpacerItem, QSizePolicy, QWidget, QHBoxLayout, QVBoxLayout

from Manutenzioni.controller.controllermanutenzione import ControllerManutenzione

# Vista manutenzione


class VistaManutenzione(QWidget):
    def __init__(self, manutenzione, salva_dati, aggiorna):
        super(VistaManutenzione, self).__init__()

        # Controller relativo alla attuale vista
        self.controller_manutenzione = ControllerManutenzione(manutenzione)

        # Funzione salva_dati passata dalla vista elenzo manutenzioni
        self.salva_dati = salva_dati
        # Funzione che aggiorna la vista precedente
        self.aggiorna_lista = aggiorna

        # Layout utilizzati per allineare i widget dellla vista
        self.layout_orizzontale = QHBoxLayout()
        self.layout_verticale = QVBoxLayout()
        self.setFixedSize(550, 280)

        # Label che descrive la attuale manutenzione
        self.label = QLabel(self.controller_manutenzione.visualizza_manutenzione())
        self.label.setFont(QFont('Times New Roman', 20))
        self.label.setAlignment(Qt.AlignCenter)

        # Creazione del bottone chiudi utile per la chiusura della finestra
        bottone_chiudi = QPushButton("Chiudi")
        bottone_chiudi.clicked.connect(self.call_chiudi)

        # Creazione del bottone effettua utile per la effettuare la manutenzione
        bottone_effettua = QPushButton("Effettua manutenzione")
        bottone_effettua.clicked.connect(self.call_effettua)

        # Settaggio e allineamento dei widget nel layout verticale e orizzontale
        self.layout_verticale.addWidget(self.label)
        self.layout_orizzontale.addWidget(bottone_chiudi)
        self.layout_orizzontale.addWidget(bottone_effettua)
        self.layout_verticale.addLayout(self.layout_orizzontale)

        # Impostazione del layout totale e il titolo della finestra
        self.setLayout(self.layout_verticale)
        self.setWindowTitle("Informazioni manutenzione")

    # Metodo per chiudere la finestra corrente
    def call_chiudi(self):
        self.close()

    # Metodo che permette di effettuare una manutenzione, aggiorna la lista e salva i dati
    def call_effettua(self):
        self.controller_manutenzione.effettua_manutenzione()
        self.aggiorna_lista()
        self.salva_dati()
        self.close()
