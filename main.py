import sys
from ListaAccount.vista.VistaLogin import VistaLogin
from PyQt5.QtWidgets import QApplication



if __name__ == "__main__":
    app = QApplication(sys.argv)
    pippo = VistaLogin()
    pippo.showMaximized()
    sys.exit(app.exec())