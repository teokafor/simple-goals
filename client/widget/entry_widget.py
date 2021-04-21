from PyQt5 import QtWidgets

from client import projectio
from client.projectio import Row


class EntryWidget(QtWidgets.QWidget):

    def remove(self):
        entry = self.entry
        projectio.delete_goal(entry.get_goal_id())
        self.callback()

    def __init__(self, entry: Row, callback, *args, **kwargs):
        super(EntryWidget, self).__init__(*args, **kwargs)
        self.entry = entry
        self.callback = callback

        # Define the base layout as an HBox.
        layout = QtWidgets.QHBoxLayout()

        # The left-hand side (everything but the delete button) is an inner HBox.
        left = QtWidgets.QHBoxLayout()
        done = QtWidgets.QCheckBox()
        label = QtWidgets.QLabel(entry.get_goal_name())
        edit = QtWidgets.QPushButton("Edit")
        left.addWidget(done)
        left.addWidget(label)
        left.addWidget(edit)

        # Delete button on the right-hand side
        delete = QtWidgets.QPushButton("Delete")
        delete.clicked.connect(lambda: self.remove())

        layout.addLayout(left)
        layout.addWidget(delete)
        self.setLayout(layout)
