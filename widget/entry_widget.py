from PyQt5 import QtWidgets

import projectio
from projectio import Row


class EntryWidget(QtWidgets.QWidget):

    def remove(self):
        entry = self.entry
        projectio.delete_goal(entry.get_goal_id())
        self.callback()

    # On activation, pass this goal's goal id to main.py. This is so we can easily manipulate the GUI.
    def select(self):
        entry = self.entry
        goal_id = entry.get_goal_id()
        from client import main  # Import statement used here to avoid circular importing.
        main.on_goal_click(goal_id)

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

        # Temporary button used to pull up relevant information about a goal.
        select = QtWidgets.QPushButton("Select")
        select.setFixedWidth(60)
        select.clicked.connect(lambda: self.select())
        left.addWidget(select)

        # Delete button on the right-hand side
        delete = QtWidgets.QPushButton("Delete")
        delete.clicked.connect(lambda: self.remove())

        layout.addLayout(left)
        layout.addWidget(delete)
        self.setLayout(layout)
