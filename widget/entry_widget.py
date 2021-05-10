# A widget representation of a row from the Goals table.
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

import projectio
from projectio import Row


class EntryWidget(QtWidgets.QPushButton):
    """
    A widget representation of a goal from the goals table.
    """
    def __init__(self, entry: Row, callback, *args, **kwargs):
        super(EntryWidget, self).__init__(*args, **kwargs)
        self.entry = entry
        self.callback = callback
        self.latest_selection = False  # Determines whether the widget should darkened or not
        from main import update_completion
        self.percentage = update_completion(self.entry.get_goal_id())
        self.qss = """
        [accessibleName="entryWidget"] {
            border-radius: 15px 15px 0px 0px;
            border-bottom: 1px solid gray;
        }

        [accessibleName="editButton"] {
            border-radius: 15px 15px 0px 0px;
            background-color: rgba(255, 255, 255, 0);
        }

        QWidget {
            background-color: #E8E8E8;
        }

        QWidget[selected = "0"] {
            background-color: #E8E8E8;
        }

        QWidget[selected = "1"] {
            background-color: #B8B8B8;
        }

        QLabel {
            background-color: rgba(255, 255, 255, 0);
        }

        QCheckBox::indicator {
            width: 30px;
            height: 30px;
            border-radius: 5px;
            background-color: white;
        }

        QCheckBox::indicator::checked {
            background-color: #35B29D;
            background-image: url(resources/checked.png);
        }

        QCheckBox {
            background-color: rgba(255, 255, 255, 0);
        }
        """

        self.setAccessibleName("entryWidget")
        self.setMinimumHeight(60)
        self.setMinimumWidth(410)
        self.setStyleSheet(self.qss)

        # Define the base layout as an HBox.
        layout = QtWidgets.QHBoxLayout()

        # The left-hand side (everything but the delete button) is an inner HBox.
        left = QtWidgets.QHBoxLayout()
        done = QtWidgets.QCheckBox()
        checkbox_state = self.entry.get_completion()
        done.setCheckState(checkbox_state)
        done.clicked.connect(lambda: self.on_check(done.checkState()))
        label = QtWidgets.QLabel(entry.get_goal_name())
        self.percent_label = QtWidgets.QLabel(f'{self.percentage * 100:.2f}%')
        edit = QtWidgets.QPushButton("")
        edit.setAccessibleName("editButton")
        edit.setIcon(QIcon("resources/edit.png"))
        edit.clicked.connect(self.edit)
        left.addWidget(done)
        left.addWidget(label)
        left.addWidget(self.percent_label)
        left.addStretch()
        left.addWidget(edit)

        self.clicked.connect(self.select)

        # Delete button on the right-hand side
        delete = QtWidgets.QPushButton("")
        delete.clicked.connect(self.remove)
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

    # Called when the delete button is clicked.
    def remove(self):
        entry = self.entry
        from widget.delete_widget import DeleteWidget
        message = DeleteWidget(entry.get_goal_name())
        if message.delete_flag:
            goal_id = entry.get_goal_id()
            projectio.delete_goal(goal_id)
            self.callback()
            # Prevents the program from attempting to load a non-existent goal, thus causing it to crash.
            from main import last_goal_id
            if goal_id != last_goal_id:
                from main import on_goal_click
                on_goal_click(last_goal_id)

    # Called when the checkbox is toggled.
    def on_check(self, state):
        self.entry.set_completion(state)

    # Called when the edit button is pressed.
    def edit(self):
        entry = self.entry
        from main import open_edit_goal
        open_edit_goal(entry.get_goal_id())

    # Called when a subgoal of this goal has its checkbox toggled.
    def update_percent_label(self, percentage):
        self.percent_label.clear()
        self.percentage = percentage
        self.percent_label.setText(f'{percentage * 100:.2f}%')

    # Called when the body of the widget is pressed. It will update subgoals, description, and highlights.
    def select(self):
        entry = self.entry
        goal_id = entry.get_goal_id()
        from main import on_goal_click
        on_goal_click(goal_id)

        # Highlight selected goal to indicate its selection
        last_exists = False
        from main import HOME
        index = HOME.goals.count()
        while index >= 2:
            child = HOME.goals.itemAt(index - 2)
            if child.widget():
                child = child.widget()
                if child.latest_selection:
                    last_entry = child
                    last_exists = True
            index -= 1
        if last_exists:  # Only darken last entry backwards if it exists
            last_entry.setStyleSheet(last_entry.qss)
            last_entry.setProperty("selected", 0)
            last_entry.style().unpolish(last_entry)
            last_entry.style().polish(last_entry)
            last_entry.latest_selection = False
        # Set the clicked button to dark grey
        self.setStyleSheet(self.qss)
        self.setProperty("selected", 1)
        self.style().unpolish(self)
        self.style().polish(self)
        self.latest_selection = True