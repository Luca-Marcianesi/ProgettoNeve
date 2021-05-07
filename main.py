import sys
from PyQt5.QtWidgets import QApplication
from ListaAccount.vista.VistaLogin import vista_login


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vista_login = vista_login()
    vista_login.show()
    sys.exit(app.exec())