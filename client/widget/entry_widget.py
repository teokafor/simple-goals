from PyQt5 import QtWidgets


class EntryWidget(QtWidgets.QWidget):

    def __init__(self, title, *args, **kwargs):
        super(EntryWidget, self).__init__(*args, **kwargs)

        # Define the base layout as an HBox.
        layout = QtWidgets.QHBoxLayout()

        # The left-hand side (everything but the delete button) is an inner HBox.
        left = QtWidgets.QHBoxLayout()
        done = QtWidgets.QCheckBox()
        label = QtWidgets.QLabel(title)
        edit = QtWidgets.QPushButton("Edit")
        left.addWidget(done)
        left.addWidget(label)
        left.addWidget(edit)

        # Delete button on the right-hand side
        delete = QtWidgets.QPushButton("Delete")

        layout.addLayout(left)
        layout.addWidget(delete)
        self.setLayout(layout)
