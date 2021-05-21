from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QImage, QBrush, QFont, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QDesktopWidget, QLabel, QSpacerItem, QSizePolicy, QWidget, \
    QListView, QPushButton, QMessageBox, QLineEdit

from Dipendenti.controller.controller_dipendente import controller_dipendente
from ElencoDipendenti.controller.controller_gestione_dipendenti import controller_elenco_dipendenti
from Dipendenti.model.dipendente import dipendente


class vista_elenco_dipendenti(QWidget):
    def __init__(self, callback):
        super(vista_elenco_dipendenti, self).__init__()

        #Attributi
        self.callback = callback
        self.controller_gestione_dipendenti = controller_elenco_dipendenti()
        self.layout_verticale1 = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.layout_verticale2 = QVBoxLayout()
        self.layout_pulsanti = QVBoxLayout()
        self.vista_lista = QListView()
        self.vista_aggiungi = vista_aggiungi_dipendente(self.showFullScreen, self.controller_gestione_dipendenti)

        #Titolo e Background
        self.show_background("Elenco Dipendenti")


        #Spaziatura
        self.layout_orizzontale.addSpacerItem(QSpacerItem(300, 0))


        #Lista
        vista_lista_model = QStandardItemModel(self.vista_lista)
        for dipendente in self.controller_gestione_dipendenti.get_lista_elenco_dipendenti():
            item = QStandardItem()
            nome = dipendente.get_dipendente_str()
            item.setText(nome)
            item.setEditable(False)
            item.setFont(QFont('Times New Roman', 30, 100))
            vista_lista_model.appendRow(item)
        self.vista_lista.setModel(vista_lista_model)
        self.layout_orizzontale.addWidget(self.vista_lista)

        self.layout_orizzontale.addSpacerItem(QSpacerItem(300,0))


        self.layout_verticale1.addLayout(self.layout_orizzontale)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0,200))

        self.show_pulsantiera()
        self.layout_orizzontale.addSpacerItem(QSpacerItem(200, 0))

        self.setLayout(self.layout_verticale1)


    def show_background(self, stringa):
        # Sfondo
        self.setFixedWidth(QDesktopWidget().width())
        self.setFixedHeight(QDesktopWidget().height())
        back_img = QImage("ListaAttrezzatura/data/attrezzatura.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

        # Titolo
        titolo = QLabel(stringa)
        titolo.setAlignment(Qt.AlignCenter)
        titolo.setFont(QFont('Times New Roman', 60))
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_verticale1.addWidget(titolo)
        self.layout_verticale1.addSpacerItem(QSpacerItem(0, 100, QSizePolicy.Fixed, QSizePolicy.Fixed))


    def show_pulsantiera(self):
        pulsante_apri = QPushButton("Apri")
        pulsante_apri.setFont(QFont('Times New Roman', 20, 100, True))
        pulsante_apri.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante_apri.clicked.connect(self.dipendente_selezionato)
        pulsante_apri.setFixedSize(250, 100)




        pulsante_indietro = QPushButton("Indietro")
        pulsante_indietro.setFont(QFont('Times New Roman', 20, 100, True))
        pulsante_indietro.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante_indietro.setFixedSize(250, 100)
        pulsante_indietro.clicked.connect(self.indietro)

        pulsante_aggiungi = QPushButton("Aggiungi\nDipendente")
        pulsante_aggiungi.setFont(QFont('Times New Roman', 20, 100, True))
        pulsante_aggiungi.setStyleSheet('QPushButton {background-color: orange; color: black;}')
        pulsante_aggiungi.setFixedSize(250, 100)
        pulsante_aggiungi.clicked.connect(self.call_aggiungi_dipendente)


        self.layout_verticale2.addWidget(pulsante_apri)
        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 50))
        self.layout_verticale2.addWidget(pulsante_aggiungi)
        self.layout_verticale2.addSpacerItem(QSpacerItem(0, 50))
        self.layout_verticale2.addWidget(pulsante_indietro)
        self.layout_orizzontale.addLayout(self.layout_verticale2)

    def dipendente_selezionato(self):
        try:
            selezionato = self.vista_lista.selectedIndexes()[0].row()
            lista = self.controller_gestione_dipendenti.get_lista_elenco_dipendenti()
            dipendente = lista[selezionato]
            self.vista_informazioni = vista_informazioni(dipendente,self.controller_gestione_dipendenti.rimuovi,
                                                         self.controller_gestione_dipendenti.salva_dati)
            self.vista_informazioni.show()
        except IndexError:
            QMessageBox.information(self, 'Attenzione!', 'Non hai selezionato nessun dipendente da visualizzare.', QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.critical(self, 'Errore!', 'Qualcosa è andato storto, riprova più tardi.', QMessageBox.Ok, QMessageBox.Ok)

    def call_aggiungi_dipendente(self):
        self.vista_aggiungi.show()
        self.close()

    def indietro(self):
        self.callback()
        self.close()

class vista_informazioni(QWidget):
    def __init__(self, dipendente,rimuovi,salva_dati):
        super(vista_informazioni, self).__init__()
        self.layout_verticale = QVBoxLayout()
        self.layout_orizzontale = QHBoxLayout()
        self.dipendente = dipendente
        self.controller_dipendente = controller_dipendente(self.dipendente)
        self.setFixedSize(400, 300)
        self.rimuovi = rimuovi
        self.salva_dati = salva_dati

        label = QLabel(self.controller_dipendente.get_dipendente_str_x_elenco())
        label.setFont(QFont('Times New Roman', 20))
        label.setAlignment(Qt.AlignCenter)

        bottone = QPushButton("Chiudi")
        bottone.clicked.connect(self.call_chiudi)

        bottone_elimina = QPushButton("Elimina")
        bottone_elimina.clicked.connect(self.call_elimina)

        self.layout_verticale.addWidget(label)
        self.layout_verticale.addSpacerItem(QSpacerItem(150, 0, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.layout_orizzontale.addWidget(bottone)
        self.layout_orizzontale.addWidget(bottone_elimina)
        self.layout_verticale.addLayout(self.layout_orizzontale)

        self.setLayout(self.layout_verticale)
        self.setWindowTitle('Informazioni dipendente')


    def call_chiudi(self):
        self.close()

    def call_elimina(self):
        self.rimuovi(self.dipendente)
        self.salva_dati()
        self.close()


class vista_aggiungi_dipendente(QWidget):

    def __init__(self, callback, controller):
        super(vista_aggiungi_dipendente, self).__init__()
        self.callback = callback
        self.controller = controller
        self.testo = {}
        self.setFixedWidth(800)
        self.setFixedHeight(600)
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()

        self.show_background()

        self.casella_testo("Nome")
        self.casella_testo("Cognome")
        self.casella_testo("Numero di telefono")

        indietro = QPushButton("Indietro")
        indietro.clicked.connect(self.indietro)
        self.h_layout.addWidget(indietro)

        invio = QPushButton("Invia")
        invio.clicked.connect(self.crea_account)
        self.h_layout.addWidget(invio)


        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Dipendente")

    def casella_testo(self, tipo):
        label = QLabel(tipo + ":")
        font = label.font()
        font.setPointSize(14)
        label.setFont(font)
        self.v_layout.addWidget(label)
        casella = QLineEdit()
        self.v_layout.addWidget(casella)
        self.testo[tipo] = casella

    def crea_account(self):
        nome = self.testo["Nome"].text()
        cognome = self.testo["Cognome"].text()
        numero_di_telefono = self.testo["Numero di telefono"].text()
        if self.controlla_informazioni1(nome, cognome,numero_di_telefono) :
            self.controller.aggiungi(dipendente(nome,cognome,numero_di_telefono))
            self.controller.salva_dati()
            self.callback()
            self.close()


    def indietro(self):
        self.callback()
        self.close()

    def show_background(self):
        # Sfondo
        back_img = QImage("Data/Immagini/azzurro.jpg")
        img = back_img.scaled(self.width(), self.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

    def controlla_informazioni1(self, nome, cognome, numero_di_telefono):
        if nome != "" and cognome != "" and numero_di_telefono != "" :
             return True
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',QMessageBox.Ok, QMessageBox.Ok)
            return False






