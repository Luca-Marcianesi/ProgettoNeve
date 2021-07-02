from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QBrush, QPalette, QImage
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QPushButton, QDesktopWidget
from Pista.controller.controllerpista import ControllerPista


class VistaPistaProprietario(QWidget):

    def __init__(self, pista, callback, salva_lista_piste, aggiorna_lista):
        super(VistaPistaProprietario, self).__init__()

        # Funzione di richiamo della vista precedente
        self.callback = callback
        # Funzione che aggiorna la lista piste della vista precedente
        self.aggiona_lista = aggiorna_lista
        # Controller relativo alla vista
        self.controller_pista = ControllerPista(pista)
        # Layout utilizzati per l'allineamento dei widget
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        # Metodo per il salvataggio dei dati per la lista pista
        self.salva_lista_piste = salva_lista_piste

        # Metodo stadard utilizzato per il settaggio dello sfondo e del titolo alla finestra
        self.show_background("PISTA")

        # Label che descrive le caratteristiche della pista
        self.label = QLabel()
        self.label.setFont(QFont('Times New Roman', 30, 100))
        self.label.setStyleSheet('QLabel{background-color: transparent; color: orange;}')

        # Funzione che si occupa del riempimento della label
        self.aggiorna()
        self.layout_verticale.addWidget(self.label)

        # Impostazione dei pulsanti indietro e modifica pista
        self.show_pulsantiera()

        # Impostazione layout totale
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 350))
        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Pista')

    # Funzione che imposta lo sfondo e il titolo alla finestra
    def show_background(self, stringa):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("Data/Immagini/VistaPrenotazioneAccount.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60, 500))
        titolo.setStyleSheet('QLabel {background-color: transparent; color: white;}')
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50))
        self.layout_verticale.addWidget(titolo)

    # Funzione che configura il pulsante indietro e modifica pista
    def show_pulsantiera(self):
        # Punsante indietro
        pulsante_indietro = QPushButton("INDIETRO")
        pulsante_indietro.setFont(QFont('Times New Roman', 18, 100, True))
        pulsante_indietro.setStyleSheet('background-color: orange')
        pulsante_indietro.setFixedSize(250, 100)
        pulsante_indietro.clicked.connect(self.indietro)
        # Punsante modifica pista
        pulsante_modifica_pista = QPushButton("MODIFICA\nPISTA")
        pulsante_modifica_pista.setFont(QFont('Times New Roman', 18, 100, True))
        pulsante_modifica_pista.setStyleSheet('background-color: orange')
        pulsante_modifica_pista.setFixedSize(250, 100)
        pulsante_modifica_pista.clicked.connect(self.call_modifica)
        # Aggiunta e allineamento dei pulsanti nei layout
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 80))
        self.layout_orizzontale.addSpacerItem(QSpacerItem(500, 0))
        self.layout_orizzontale.addWidget(pulsante_indietro)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(50, 0))
        self.layout_orizzontale.addWidget(pulsante_modifica_pista)
        self.layout_orizzontale.addSpacerItem(QSpacerItem(500, 0))
        self.layout_verticale.addLayout(self.layout_orizzontale)

    # Metodo che riempie la label con la descrizione della pista
    def aggiorna(self):
        self.label.setText("Nome => {}\n".format(self.controller_pista.get_nome_str()) + "\n"
                           "Difficoltà => {}\n".format(self.controller_pista.get_difficolta()) + "\n"
                           "Stato => {}\n".format(self.controller_pista.get_stato()) + "\n")

    # Chiamata alla vista successiva
    def call_modifica(self):
        self.vista_cambia_stato = VistaCambiaStato(self.controller_pista, self.salva_lista_piste, self.showFullScreen,
                                                   self.aggiona_lista, self.aggiorna)
        self.vista_cambia_stato.show()

    # Metodo che permette di tornare alla vista precedente
    def indietro(self):
        self.callback()
        self.close()


class VistaCambiaStato(QWidget):
    def __init__(self, controller_pista, salva_lista_piste, callback, aggiorna, aggiorna_lista):
        super(VistaCambiaStato, self).__init__()

        # Funzione che richiama la vista precedente
        self.callback = callback
        # Funzione che aggiorna la label della vista precedente
        self.aggiorna = aggiorna
        # Funzione che aggiorna la lista delle piste
        self.aggiorna_lista = aggiorna_lista
        # Funzione che salva i dati della lista piste
        self.salva_lista_piste = salva_lista_piste
        # Controller relativo alla vista
        self.controller_pista = controller_pista
        # Layout utilizzati nella vista
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        # Dimensione fissa della vista
        self.setFixedSize(600, 500)

        # Funzione che permette la configurazione dello sfondo
        self.show_background()

        # Labeol che descrive l'operazione da compiere
        label = QLabel("Seleziona stato della pista:")
        label.setFont(QFont('Times New Roman', 25, 100))
        label.setSizePolicy(500, 200)
        label.setStyleSheet('QLabel{background-color: orange; color: black;}')
        self.layout_verticale.addWidget(label)

        # Pulsante che si occupa della chiusura della pista
        bottone_chiusa = QPushButton("Chiusa")
        bottone_chiusa.setStyleSheet('QPushButton{background-color: orange; color: black;}')
        bottone_chiusa.setFont(QFont('Times New Roman', 18))
        bottone_chiusa.clicked.connect(partial(self.call_modifica_stato, "Chiusa"))

        # Pulsante che si occupa della apertura della pista
        bottone_aperta = QPushButton("Aperta")
        bottone_aperta.setStyleSheet('QPushButton{background-color: orange; color: black;}')
        bottone_aperta.setFont(QFont('Times New Roman', 18))
        bottone_aperta.clicked.connect(partial(self.call_modifica_stato, "Aperta"))

        # Pulsante che si occupa di contrassegnare la pista come prenotata
        bottone_prenotata = QPushButton("Prenotata")
        bottone_prenotata.setStyleSheet('QPushButton{background-color: orange; color: black;}')
        bottone_prenotata.setFont(QFont('Times New Roman', 18))
        bottone_prenotata.clicked.connect(partial(self.call_modifica_stato, "Prenotata"))

        # Impostazione e allineamento dei pulsante nei layout
        self.layout_orizzontale.addWidget(bottone_chiusa)
        self.layout_orizzontale.addWidget(bottone_aperta)
        self.layout_orizzontale.addWidget(bottone_prenotata)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 500))
        self.layout_verticale.addLayout(self.layout_orizzontale)
        self.layout_verticale.addSpacerItem(QSpacerItem(0, 50))

        # Impostazione del layout totale
        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Stato')

    # Funzione che si occupa di modificare lo stato della pista
    def call_modifica_stato(self, stato):
        self.controller_pista.modifica_stato_pista(stato)
        self.salva_lista_piste()
        self.aggiorna()
        self.aggiorna_lista()
        self.callback()
        self.close()

    # Configurazione dello sfondo della finestra
    def show_background(self):
        # Sfondo
        back_img = QImage("Data/Immagini/ModificaPista.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)
