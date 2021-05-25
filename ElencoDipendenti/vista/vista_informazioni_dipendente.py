from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QSpacerItem, QSizePolicy, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QWidget
from Dipendenti.controller.controller_dipendente import controller_dipendente
from PyQt5.QtCore import Qt

# vista informazioni dipendente
class vista_informazioni(QWidget):

    def __init__(self, dipendente, rimuovi, salva_dati,aggiorna):

        super(vista_informazioni, self).__init__()

        # Layout
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.setFixedSize(400, 300)

        # Definizione degli attributi
        self.dipendente = dipendente
        self.controller_dipendente = controller_dipendente(self.dipendente)
        self.rimuovi = rimuovi
        self.salva_dati = salva_dati
        self.aggiorna = aggiorna

        # Descrizione del dipendente
        label = QLabel(self.controller_dipendente.get_dipendente_str_x_elenco())
        label.setFont(QFont('Times New Roman', 20))
        label.setAlignment(Qt.AlignCenter)

        # Creazione e funzionamento dei bottoni
        bottone = QPushButton("Chiudi")
        bottone.clicked.connect(self.call_chiudi)

        bottone_elimina = QPushButton("Elimina")
        bottone_elimina.clicked.connect(self.call_elimina)

        # Settaggio del layout totale
        self.layout_verticale.addWidget(label)
        self.layout_verticale.addSpacerItem(QSpacerItem(150, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale.addWidget(bottone)
        self.layout_orizzontale.addWidget(bottone_elimina)
        self.layout_verticale.addLayout(self.layout_orizzontale)

        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Informazioni dipendente')

    # Metodo per chiudere la finestra corrente
    def call_chiudi(self):
        self.close()

    # Metodo per eliminare un dipendente
    def call_elimina(self):
        self.rimuovi(self.dipendente)
        self.aggiorna()
        self.salva_dati()
        self.close()