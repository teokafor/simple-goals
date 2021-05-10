from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


class DeleteWidget(QtWidgets.QWidget):
    """
    This widget represents a dialog box that confirms whether the user wants to delete a specified goal.
    """

    def __init__(self, goal_name, *args, **kwargs):
        """
        Primary constructor for DeleteWidget.

        :param goal_name: the name of the goal that is being deleted. Displayed in the dialog box this widget provides.
        """
        super(DeleteWidget, self).__init__(*args, **kwargs)
        self.goal_name = goal_name
        self.delete_flag = False

        message_box = QMessageBox.question(self, f'Delete {self.goal_name}?',
                                           f'Are you sure you want to delete {self.goal_name}?')
        if message_box == QMessageBox.Yes:
            self.delete_flag = True
