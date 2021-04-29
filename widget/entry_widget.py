from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

import projectio
from projectio import Row


class EntryWidget(QtWidgets.QPushButton):

    def remove(self):
        entry = self.entry
        projectio.delete_goal(entry.get_goal_id())
        self.callback()

    # On activation, pass this goal's goal id to main.py. This is so we can easily manipulate the GUI.
    def select(self):
        entry = self.entry
        goal_id = entry.get_goal_id()
        import main  # Import statement used here to avoid circular importing.
        main.on_goal_click(goal_id)

    def __init__(self, entry: Row, callback, *args, **kwargs):
        super(EntryWidget, self).__init__(*args, **kwargs)
        self.entry = entry
        self.callback = callback

        self.setAccessibleName("entryWidget")
        self.setMinimumHeight(65)
        self.setStyleSheet("""
        [accessibleName="entryWidget"] {
            border-radius: 15px 15px 0px 0px;
            border-bottom: 1px solid gray;
        }
        
        [accessibleName="editButton"] {
            border-radius: 15px 15px 0px 0px;
        }
        
        QWidget {
            background-color: #E8E8E8;
        }
        
        QCheckBox::indicator {
            width: 30px;
            height: 30px;
            background-color: white;
            border-radius: 5px;
        }
        
        QCheckBox::indicator::checked {
            background-color: green;
        }
        """)

        # Define the base layout as an HBox.
        layout = QtWidgets.QHBoxLayout()

        # The left-hand side (everything but the delete button) is an inner HBox.
        left = QtWidgets.QHBoxLayout()
        done = QtWidgets.QCheckBox()
        label = QtWidgets.QLabel(entry.get_goal_name())
        edit = QtWidgets.QPushButton("")
        edit.setAccessibleName("editButton")
        edit.setIcon(QIcon("resources/edit.png"))
        left.addWidget(done)
        left.addWidget(label)
        left.addStretch()
        left.addWidget(edit)

        # Temporary button used to pull up relevant information about a goal.
        select = QtWidgets.QPushButton("Select")
        select.setFixedWidth(60)
        select.clicked.connect(lambda: self.select())
        left.addWidget(select)

        # Delete button on the right-hand side
        delete = QtWidgets.QPushButton("")
        delete.clicked.connect(lambda: self.remove())
        delete.setIcon(QIcon("resources/delete.png"))
        delete.setMaximumWidth(38)
        delete.setMinimumWidth(38)
        delete.setMaximumHeight(38)
        delete.setMinimumHeight(38)
        delete.setStyleSheet("""
        QWidget {
            background-color: #B23535;
            border-radius: 5px;
        }
        """)

        layout.addLayout(left)
        layout.addWidget(delete)
        self.setLayout(layout)
