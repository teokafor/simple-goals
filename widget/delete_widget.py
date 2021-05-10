from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


class DeleteWidget(QtWidgets.QWidget):
    """
    Objects of this class are instantiated from the delete method in EntryWidget.
    """
    def __init__(self, goal_name, *args, **kwargs):
        super(DeleteWidget, self).__init__(*args, **kwargs)
        self.goal_name = goal_name
        self.delete_flag = False

        message_box = QMessageBox.question(self, f'Delete {self.goal_name}?', f'Are you sure you want to delete {self.goal_name}?')
        if message_box == QMessageBox.Yes:
            self.delete_flag = True