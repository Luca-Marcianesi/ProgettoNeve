from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, \
    QDesktopWidget, QSpinBox, QMessageBox
from Sessione.model.sessione import Sessione
from GestioneParcheggi.controller.controllergestioneparcheggi import ControllerGestioneParcheggi


# Vista utile per la gestione della prenotazione del parcheggio
class VistaParcheggio(QWidget):

    def __init__(self, callback):
        super(VistaParcheggio, self).__init__()

        # Funzione di richiamo della vista precedente
        self.callback = callback

        # Controller della gestione parcheggi importante per effettuare le varie funzioni
        self.controller_gestione_parcheggio = ControllerGestioneParcheggi()

        # Layout usati per visualizzare e allineare l'intera vista
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()

        # Label usata per la descrizione dei parcheggi
        self.label = QLabel()
        self.label.setFont(QFont('Times New Roman', 30))
        self.label.setStyleSheet("background-image:url(Data/Immagini/legnopista.jpg)")
        self.label.setAlignment(Qt.AlignCenter)

        # Funzione standard che imposta uno sfondo immagine e un titolo nella attuale vista
        self.show_background("PARCHEGGIO CAPANNINA")

        # Spaziatura verticale
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Aggiornamento e allineamento label modificata
        self.aggiorna()
        self.layout_orizzontale.addSpacerItem(QSpacerItem(600, 500, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale.addWidget(self.label)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(600, 300, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Settaggio e allineamento del layout orizzontale a quello verticale
        self.layout_verticale.addLayout(self.layout_orizzontale)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 200, QSizePolicy.Fixed, QSizePolicy.Fixed))

        # Configurazione e allineamento dei pulsanti
        self.show_pulsantiera()

        # Configurazione finale del layout totale
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 150, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Parcheggio')

    # Metodo utile per l'aggiornamento della label
    def aggiorna(self):
        if Sessione.controlla_prenotazione_effettuata(2):  # 2 è il codice assegnato al parcheggio
            self.label.setText("POSTI DISPONIBILI:\n{} ".format
                           (self.controller_gestione_parcheggio.get_posti_disponibili()))
        else:
            self.label.setText("POSTI DISPONIBILI:\n{}\n(prenotazione effettuata)".format
                           (self.controller_gestione_parcheggio.get_posti_disponibili()))

    # Creazione, stile e settaggio sfondo e titolo
    def show_background(self, titolo):
        # Settaggio e ridimensionamento dell'immagine di sfondo dell'attuale vista
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        immagine = QImage('Data/Immagini/Parcheggio.jpg')
        img = immagine.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Settaggio e allineamento del titolo della vista
        titolo = QLabel(titolo)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        titolo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale.addWidget(titolo)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))

    # Metodo per creazione, stile e funzionamento dei bottoni indietro e prenota
    def show_pulsantiera(self):
        # Layout interni utilizzati per l'allineamento dei tre pulsanti
        layout_pulsanti = QHBoxLayout()
        layout_pulsanti.setAlignment(Qt.AlignCenter)

        # Configurazione del pulsante Indietro
        pulsante_indietro = QPushButton("INDIETRO")
        pulsante_indietro.setFont(QFont('Times New Roman', 18, 100, True))
        pulsante_indietro.setFixedSize(250, 100)
        pulsante_indietro.setStyleSheet("background-color: orange")
        pulsante_indietro.clicked.connect(self.indietro)

        # Configurazione del pulsante Prenota
        pulsante_prenota = QPushButton("PRENOTA")
        pulsante_prenota.setFont(QFont('Times New Roman', 18, 100, True))
        pulsante_prenota.setFixedSize(250, 100)
        pulsante_prenota.setStyleSheet("background-color: orange")
        pulsante_prenota.clicked.connect(self.call_selezione_giorni)

        # Inserimento e allineamento dei tre pulsanti del layout globale
        layout_pulsanti.addWidget(pulsante_prenota)
        layout_pulsanti.addSpacerItem(QSpacerItem(50, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        layout_pulsanti.addWidget(pulsante_indietro)
        self.layout_verticale.addLayout(layout_pulsanti)

    # Chiamata e mostra della vista richiesta giorni
    def call_selezione_giorni(self):
        self.vista = VistaRichiestaGiorni(self.controller_gestione_parcheggio,self.aggiorna)
        self.vista.show()

    # Metodo che permette, cliccando il bottone "indietro", di tornare alla vista precedente
    def indietro(self):
        self.callback()
        self.close()


# Vista utile per l'inserimento dei giorni per la prenotazione del parcheggio
class VistaRichiestaGiorni(QWidget):

    def __init__(self, controller_parcheggi,aggiorna):
        super(VistaRichiestaGiorni, self).__init__()

        # Controller della gestione parcheggi importante per effettuare le varie funzioni
        self.controller_parcheggi = controller_parcheggi
        # Funzione di aggiornamento della vista precedente
        self.aggiorna = aggiorna
        # Layout usato per visualizzare e allineare l'intera vista
        self.layout_verticale = QVBoxLayout()
        self.setFixedSize(400, 300)

        # Descrizione della finestra per scegliere per quanti giorni prenotare
        layout_label = QHBoxLayout()
        label = QLabel("NUMERO GIORNI\nDA PRENOTARE:")
        label.setFont(QFont('Times New Roman', 24, 100))
        label.setSizePolicy(300, 300)
        label.setAlignment(Qt.AlignCenter)
        layout_label.addWidget(label)
        self.layout_verticale.addLayout(layout_label)

        # Configurazione della SpinBox
        layout_spinbox = QHBoxLayout()
        giorni = QSpinBox(self)
        giorni.setFont(QFont('Times New Roman', 20))
        giorni.setAlignment(Qt.AlignCenter)
        giorni.setFixedSize(100, 50)
        giorni.lineEdit().setReadOnly(True)
        giorni.setRange(1, 5)
        layout_spinbox.addSpacerItem(QSpacerItem(50, 0))
        layout_spinbox.addWidget(giorni)
        layout_spinbox.addSpacerItem(QSpacerItem(50, 0))
        self.layout_verticale.addLayout(layout_spinbox)

        # Creazione e configurazione del bottone prenota
        layout_pulsante = QHBoxLayout()
        bottone = QPushButton("Prenota")
        bottone.setFont(QFont('Times New Roman', 22))
        bottone.setFixedSize(270, 60)
        bottone.clicked.connect(self.call_prenota)
        layout_pulsante.addWidget(bottone)
        self.layout_verticale.addLayout(layout_pulsante)

        # Configurazione finale del layout totale
        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Giorni')

    # Metodo per effettuare la prenotazione
    def call_prenota(self):
        val = self.giorni.value()
        risultato = self.controller_parcheggi.prenota_parcheggio(val)
        QMessageBox.information(self, "Esito", risultato, QMessageBox.Ok, QMessageBox.Ok)
        self.aggiorna()
        self.close()
