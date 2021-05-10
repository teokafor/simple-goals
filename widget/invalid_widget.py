from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


class InvalidWidget(QtWidgets.QWidget):
    """
    This widget represents an error dialog box which appears when an input field for a goal is invalid.
    """

    def __init__(self, *args, **kwargs):
        super(InvalidWidget, self).__init__(*args, **kwargs)
        QMessageBox.warning(self, 'Error!', f'Input fields cannot be left blank.\nPlease try again.')
