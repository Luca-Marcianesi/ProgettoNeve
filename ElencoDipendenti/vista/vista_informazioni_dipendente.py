from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QSpacerItem, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QWidget
from Dipendenti.controller.controller_dipendente import ControllerDipendente
from PyQt5.QtCore import Qt


# Vista utilizzata per la visualizzazione delle informazioni principali del dipendente
class VistaInformazioniDipendente(QWidget):

    def __init__(self, dipendente, rimuovi, salva_dati, aggiorna):
        super(VistaInformazioniDipendente, self).__init__()

        # Funzione utile per l'aggiornamento della vista precedente dopo la modifica
        self.aggiorna = aggiorna
        # Funzione per la rimozione del dipendente
        self.rimuovi = rimuovi
        # Funzione ultile per il salvataggio dei dipendenti modificati
        self.salva_dati = salva_dati
        # Oggetto selezionato dalla vista precedente
        self.dipendente = dipendente

        # Controller del dipendente utile per le varie operazioni da effettuare
        self.controller_dipendente = ControllerDipendente(self.dipendente)

        # Layout usati per la visualizzazione e l'allineamento della vista
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()

        # Configurazione della dimensione della finestra
        self.setFixedSize(400, 300)

        # Allineamento e settaggio della Label che descrive le principali inforazioni del dipendente
        label = QLabel(self.controller_dipendente.get_dipendente_str_x_elenco())
        label.setFont(QFont('Times New Roman', 20))
        label.setAlignment(Qt.AlignCenter)
        self.layout_verticale.addWidget(label)
        self.layout_verticale.addSpacerItem(QSpacerItem(150, 0))

        # Creazione e configurazione del bottone "Chiudi"
        bottone_chiudi = QPushButton("Chiudi")
        bottone_chiudi.clicked.connect(self.call_chiudi)
        self.layout_orizzontale.addWidget(bottone_chiudi)

        # Creazione e configurazione del bottone "Elimina"
        bottone_elimina = QPushButton("Elimina")
        bottone_elimina.clicked.connect(self.call_elimina)
        self.layout_orizzontale.addWidget(bottone_elimina)

        # Impostazione e allineamento del layout totale
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
