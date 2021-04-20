import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from client.screen.home import Ui_MainWindow as HomeWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = QMainWindow()
    home = HomeWindow()
    home.setupUi(root)
    root.show()
    sys.exit(app.exec_())
