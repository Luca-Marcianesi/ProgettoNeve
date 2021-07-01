from functools import partial
from PyQt5.QtGui import QFont, QBrush, QPalette, QImage
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, \
    QDesktopWidget, QGridLayout
from ListaPiste.controller.controllerlistapiste import ControllerListaPiste
from Pista.vista.VistaPistaProprietario import VistaPistaProprietario


class VistaListaPisteProprietario(QWidget):
    def __init__(self, callback):
        super(VistaListaPisteProprietario, self).__init__()

        # Funzione che richiama la vista precedente
        self.callback = callback
        # Controller relativo alla vista
        self.controller = ControllerListaPiste()
        self.vista_pista = None
        # Layout utilizzati nella vista per l'allineamento dei widget
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale1 = QHBoxLayout()

        # Funzione standard che imposta lo sfondo e il titolo alla vista
        self.show_background()

        # Spaziatura layout verticale
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 850))

        # Funzione che configura il pulsante indietro
        self.show_pulsante_indietro()

        # Spaziatura layout verticale
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 20))

        # Creazione layout a griglia
        self.layout_piste = QGridLayout()

        # Chiamata funzione aggiorna
        self.aggiorna()

        # Settaggio layout verticale
        self.layout_verticale1.addLayout(self.layout_piste)

        # Settaggio layout verticale e spaziatura layout verticale
        self.layout_verticale1.addLayout(self.layout_orizzontale1)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 25))

        # Impostazione layout totale
        self.setLayout(self.layout_verticale1)
        self.setWindowTitle('Lista Piste')

    # Creazione, settaggio e stile sfondo
    def show_background(self):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("Data/Immagini/ImmaginePiste.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

    # Creazione, settaggio, stile, mostra e aggiunta al layout di vari pulsanti
    def show_pulsante_indietro(self):

        # Metodo per creazione, stile e funzionamento dei bottoni indietro
        pulsante_indietro = QPushButton()
        pulsante_indietro.setStyleSheet('QPushButton {background-color: lightBlue;}')
        pulsante_indietro.setStyleSheet("background-image:url(Data/Immagini/FrecciaIndietro.jpg)")
        pulsante_indietro.setFixedSize(100, 100)
        pulsante_indietro.clicked.connect(self.indietro)
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(5, 0))
        self.layout_orizzontale1.addWidget(pulsante_indietro)

        # Pulsante che apre tutte le piste
        apri_tutte_le_piste = QPushButton("APRI\nTUTTE")
        apri_tutte_le_piste.setStyleSheet('QPushButton {background-color: orange;}')
        apri_tutte_le_piste.setFont(QFont('Times New Roman', 15, 50, True))
        apri_tutte_le_piste.setFixedSize(100, 100)
        apri_tutte_le_piste.clicked.connect(self.call_apri_tutte)
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(5, 0))
        self.layout_orizzontale1.addWidget(apri_tutte_le_piste)

        # Pulsante che chiude tutte le piste
        chiudi_tutte_le_piste = QPushButton("CHIUDI\nTUTTE")
        chiudi_tutte_le_piste.setStyleSheet(' QPushButton {background-color: orange;}')
        chiudi_tutte_le_piste.setFont(QFont('Times New Roman', 15, 50, True))
        chiudi_tutte_le_piste.setFixedSize(100, 100)
        chiudi_tutte_le_piste.clicked.connect(self.call_chiudi_tutte)
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(5, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale1.addWidget(chiudi_tutte_le_piste)
        self.layout_orizzontale1.addSpacerItem(QSpacerItem(5000, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addLayout(self.layout_orizzontale1)

    # Metodo che aggiorna la finestra
    def aggiorna(self):
        # Punsante indietro
        riga = 0
        colonna = 0
        indice_pista = 1
        for pista in self.controller.get_lista():
            simbolo = "●"
            bottone = QPushButton("[{}]  ".format(indice_pista) + pista.get_nome_str() + simbolo)
            bottone.setFont(QFont('Times New Roman', 18))
            if pista.get_stato() == "Aperta":
                bottone.setStyleSheet('QPushButton {background-color: lightBlue; color: green;}')
            else:
                bottone.setStyleSheet('QPushButton {background-color: lightBlue; color: red;}')
            bottone.clicked.connect(partial(self.call_vista_pista_proprietario, pista))
            if colonna == 5 or colonna == 10:
                colonna = 0
                riga += 1
            self.layout_piste.addWidget(bottone, riga, colonna)
            colonna += 1
            indice_pista += 1

    # Metodo che chiama e mostra la vista pista
    def call_vista_pista_proprietario(self, pista):
        self.vista_pista_proprietario = VistaPistaProprietario(pista,
                                                               self.showFullScreen,
                                                               self.controller.salva_dati,
                                                               self.aggiorna)
        self.vista_pista_proprietario.showFullScreen()
        self.close()

    # Metodo che setta lo stato di tutte le piste a "APERTA"
    def call_apri_tutte(self):
        self.controller.set_stato_tutte("Aperta")
        self.controller.salva_dati()
        self.aggiorna()

    # Metodo che setta lo stato di tutte le piste a "CHIUSA"
    def call_chiudi_tutte(self):
        self.controller.set_stato_tutte("Chiusa")
        self.controller.salva_dati()
        self.aggiorna()

    # Metodo che, collegato al pulsante indietro, permette di tornare alla vista precedente
    def indietro(self):
        self.callback()
        self.close()
