# Objects of this class are only created if inputs are invalid. Displays a warning message on creation.
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


class InvalidWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(InvalidWidget, self).__init__(*args, **kwargs)
        QMessageBox.warning(self, 'Error!', f'Input fields cannot be left blank.\nPlease try again.')